from collections import Counter
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "content-taxonomy-tag-review.md"


def review_rows():
    text = REVIEW.read_text(encoding="utf-8")
    section = text.split("## Complete decision inventory", 1)[1].split("## T05 handoff", 1)[0]
    rows = []
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        tag = cells[0].strip("`")
        rows.append(
            {
                "tag": tag,
                "uses": int(cells[1]),
                "public": int(cells[2]),
                "hidden": int(cells[3]),
                "decision": cells[4],
                "target": cells[5].strip("`"),
                "reason": cells[6],
                "items": cells[7],
            }
        )
    return text, rows


class ContentTagReviewTests(unittest.TestCase):
    def test_review_covers_the_complete_t04_snapshot(self):
        _, rows = review_rows()
        self.assertEqual(157, len(rows))
        self.assertEqual(157, len({row["tag"] for row in rows}))
        self.assertEqual(165, sum(row["uses"] for row in rows))
        self.assertEqual(Counter({1: 150, 2: 6, 3: 1}), Counter(row["uses"] for row in rows))
        for row in rows:
            self.assertEqual(row["uses"], row["public"] + row["hidden"], row["tag"])
            self.assertTrue(row["reason"], row["tag"])
            self.assertTrue(row["items"], row["tag"])

    def test_change_set_is_finite_and_has_legacy_url_strategy(self):
        text, rows = review_rows()
        decisions = {row["tag"]: (row["decision"], row["target"]) for row in rows}
        self.assertEqual(Counter({"KEEP": 155, "MERGE": 1, "RETIRE": 1}), Counter(row["decision"] for row in rows))
        self.assertEqual(("MERGE", "System Bus"), decisions["Bus"])
        self.assertEqual(("RETIRE", "—"), decisions["Changelog"])
        self.assertRegex(text, r"/tags/bus/.*?/tags/system-bus/")
        self.assertRegex(text, r"/tags/changelog/.*?/tags/neutriverse/")

    def test_review_explicitly_protects_one_off_and_hidden_semantics(self):
        text, _ = review_rows()
        self.assertIn("A one-off tag is kept", text)
        self.assertIn("hidden-only tags remain semantically intact", text)
        self.assertNotIn("frequency threshold", text.lower())


if __name__ == "__main__":
    unittest.main()
