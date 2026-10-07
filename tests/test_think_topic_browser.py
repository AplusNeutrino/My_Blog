import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ThinkTopicBrowserTest(unittest.TestCase):
    def test_topic_browser_uses_one_ordered_taxonomy_source(self):
        taxonomy = (ROOT / "_data" / "content_taxonomy.yml").read_text(encoding="utf-8")
        order_match = re.search(r"^topic_order:\n(?P<body>(?:  - .+\n){4})", taxonomy)
        self.assertIsNotNone(order_match)
        self.assertEqual(
            ["computation", "humanity", "otaku", "arts"],
            re.findall(r"^  - (\w+)$", order_match.group("body"), re.MULTILINE),
        )

        browser = (
            ROOT / "_includes" / "neutriverse-topic-browser.html"
        ).read_text(encoding="utf-8")
        self.assertIn("site.data.content_taxonomy.topic_order", browser)
        self.assertIn("site.data.content_taxonomy.topics[topic_id]", browser)
        self.assertIn("include.items | where: 'topic', topic_id", browser)
        self.assertIn("?topic={{ topic_id | url_encode }}", browser)
        self.assertNotRegex(browser, r">\s*(?:34|6|3|1)\s*<")

    def test_topic_counts_match_the_public_authoritative_inventory(self):
        baseline = json.loads(
            (ROOT / "docs" / "neutriverse-restructure-baseline.json").read_text(encoding="utf-8")
        )
        public_items = [
            post for post in baseline["posts"] if not post["hidden"] and post["published"]
        ] + [fragment for fragment in baseline["fragments"] if not fragment["hidden"]]
        counts = Counter(item["topic"] for item in public_items)
        self.assertEqual(
            {"computation": 34, "humanity": 6, "otaku": 3, "arts": 1},
            dict(counts),
        )
        self.assertEqual(44, sum(counts.values()))

    def test_browser_is_wired_to_the_existing_ledger_and_shareable_state(self):
        writing = (
            ROOT / "_includes" / "neutriverse-writing-list.html"
        ).read_text(encoding="utf-8")
        script = (
            ROOT / "assets" / "js" / "neutriverse-writing-filters.js"
        ).read_text(encoding="utf-8")
        css = (
            ROOT / "assets" / "css" / "neutriverse-sections.css"
        ).read_text(encoding="utf-8")

        self.assertIn("neutriverse-topic-browser.html items=nv_writing_items", writing)
        self.assertIn("[data-writing-topic-link]", script)
        self.assertIn("link.dataset.writingTopicLink", script)
        self.assertIn("render({ historyMode: 'push' })", script)
        for selector in (
            ".nv-topic-browser",
            ".nv-topic-browser-list",
            ".nv-topic-browser-link",
            ".nv-topic-browser-count",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, css)


if __name__ == "__main__":
    unittest.main()
