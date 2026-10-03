import ast
from collections import Counter
import csv
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "docs/content-taxonomy-migration.md"
REPORT = ROOT / "docs/content-taxonomy-final-report.md"


def front_matter(path):
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.S)
    if not match:
        raise AssertionError(f"missing front matter: {path}")
    return match.group(1)


def scalar(block, name):
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", block, re.M)
    if not match:
        return None
    value = match.group(1)
    if value in ("", "null", "~"):
        return None
    return value.strip('"\'')


def list_value(block, name):
    match = re.search(rf"^{re.escape(name)}:\s*(.*)$", block, re.M)
    if not match:
        return []
    inline = match.group(1).strip()
    if inline.startswith("[") and inline.endswith("]"):
        # CSV handles commas while preserving quoted numeric strings such as "8086".
        return [x.strip().strip('"\'') for x in next(csv.reader([inline[1:-1]], skipinitialspace=True))]
    following = block[match.end():]
    result = [inline[1:].strip().strip('"\'')] if inline.startswith("-") else []
    for index, line in enumerate(following.splitlines()):
        if index == 0 and not line.strip():
            continue
        item = re.match(r"^\s+-\s+(.*?)\s*$", line)
        if not item:
            break
        result.append(item.group(1).strip('"\''))
    return result


def audit_tables():
    section = None
    articles, fragments = [], []
    for line in AUDIT.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Article migration table"):
            section = "article"
        elif line.startswith("## Fragment inventory"):
            section = "fragment"
        elif line.startswith("## "):
            section = None
        if section == "article" and re.match(r"^\| \d+ \|", line):
            articles.append([x.strip() for x in line.strip("|").split("|")])
        elif section == "fragment" and re.match(r"^\| 20\d\d-", line):
            fragments.append([x.strip() for x in line.strip("|").split("|")])
    return articles, fragments


def fragment_objects():
    block = front_matter(ROOT / "_tabs/thoughts.md")
    objects = []
    current = None
    for line in block.splitlines():
        start = re.match(r'^\s+- text:\s*(.+?)\s*$', line)
        if start:
            if current:
                objects.append(current)
            current = {"text": ast.literal_eval(start.group(1))}
            continue
        field = re.match(r"^\s{4}(date|type|topic|tags):\s*(.*?)\s*$", line)
        if current is not None and field:
            key, value = field.groups()
            if key == "tags":
                current[key] = [x.strip().strip('"\'') for x in next(csv.reader([value[1:-1]], skipinitialspace=True))]
            else:
                current[key] = value.strip('"\'')
    if current:
        objects.append(current)
    return objects


class ContentTaxonomyConsistencyTest(unittest.TestCase):
    def test_current_sources_match_authoritative_audit_and_report(self):
        article_rows, fragment_rows = audit_tables()
        self.assertEqual(44, len(article_rows))
        self.assertEqual(5, len(fragment_rows))

        actual = {}
        for path in sorted((ROOT / "_posts").glob("*.md")):
            block = front_matter(path)
            actual[path.name] = {
                "type": scalar(block, "type"),
                "topic": scalar(block, "topic"),
                "series": scalar(block, "series"),
                "tags": list_value(block, "tags"),
            }

        audited_items = []
        old_tags, final_tags = set(), set()
        for row in article_rows:
            _, filename, _, old, kind, topic, series, tags, confidence, _ = row
            self.assertEqual("confident", confidence, filename)
            expected = {
                "type": kind,
                "topic": topic,
                "series": None if series == "—" else series,
                "tags": [x.strip() for x in tags.split(";") if x.strip()],
            }
            self.assertEqual(expected, actual[filename], filename)
            audited_items.append(expected)
            old_tags.update(x.strip() for x in old.split(";") if x.strip())
            final_tags.update(expected["tags"])

        fragments = fragment_objects()
        self.assertEqual(5, len(fragments))
        by_date = {x["date"]: x for x in fragments}
        for date, old, kind, topic, tags, _ in fragment_rows:
            expected_tags = [x.strip() for x in tags.split(";") if x.strip()]
            self.assertEqual(kind, by_date[date]["type"])
            self.assertEqual(topic, by_date[date]["topic"])
            self.assertEqual(expected_tags, by_date[date]["tags"])
            audited_items.append({"type": kind, "topic": topic, "series": None, "tags": expected_tags})
            old_tags.update(x.strip() for x in old.split(",") if x.strip())
            final_tags.update(expected_tags)

        self.assertEqual({"note": 39, "essay": 5, "fragment": 5}, dict(Counter(x["type"] for x in audited_items)))
        self.assertEqual({"computation": 38, "humanity": 6, "otaku": 4, "arts": 1}, dict(Counter(x["topic"] for x in audited_items)))
        self.assertEqual({"Database Systems": 10, "Computer Architecture": 8, "Computer Networks": 10}, dict(Counter(x["series"] for x in audited_items if x["series"])))
        self.assertEqual(93, len(old_tags))
        self.assertEqual(157, len(final_tags))

        report = REPORT.read_text(encoding="utf-8")
        for topic, count in (("computation", 38), ("humanity", 6), ("otaku", 4), ("arts", 1)):
            self.assertRegex(report, rf"\| `{topic}` \| {count} \|")


if __name__ == "__main__":
    unittest.main()
