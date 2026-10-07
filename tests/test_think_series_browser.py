import json
import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ThinkSeriesBrowserTest(unittest.TestCase):
    def test_series_definitions_have_stable_ids_and_labels(self):
        taxonomy = (ROOT / "_data" / "content_taxonomy.yml").read_text(encoding="utf-8")
        series_block = re.search(
            r"^series:\n(?P<body>.*?)(?=^types:)", taxonomy, re.MULTILINE | re.DOTALL
        )
        self.assertIsNotNone(series_block)
        pairs = re.findall(
            r"^  - id: ([a-z0-9-]+)\n    label: (.+)$",
            series_block.group("body"),
            re.MULTILINE,
        )
        self.assertEqual(
            [
                ("database-systems", "Database Systems"),
                ("computer-architecture", "Computer Architecture"),
                ("computer-networks", "Computer Networks"),
            ],
            pairs,
        )

    def test_series_counts_match_public_explicit_metadata(self):
        baseline = json.loads(
            (ROOT / "docs" / "neutriverse-restructure-baseline.json").read_text(encoding="utf-8")
        )
        counts = Counter(
            post["series"]
            for post in baseline["posts"]
            if not post["hidden"] and post["published"] and post["series"]
        )
        self.assertEqual(
            {
                "Database Systems": 10,
                "Computer Architecture": 8,
                "Computer Networks": 10,
            },
            dict(counts),
        )
        self.assertEqual(28, sum(counts.values()))

    def test_directory_and_filter_reuse_the_writing_source(self):
        browser = (
            ROOT / "_includes" / "neutriverse-series-browser.html"
        ).read_text(encoding="utf-8")
        writing = (
            ROOT / "_includes" / "neutriverse-writing-list.html"
        ).read_text(encoding="utf-8")
        script = (
            ROOT / "assets" / "js" / "neutriverse-writing-filters.js"
        ).read_text(encoding="utf-8")

        self.assertIn("site.data.content_taxonomy.series", browser)
        self.assertIn("include.items | where: 'series', series.label | sort: 'date'", browser)
        self.assertIn("?series={{ series.id | url_encode }}", browser)
        self.assertNotIn("categories", browser)
        self.assertNotRegex(browser, r">\s*(?:10|8)\s*<")
        self.assertIn("neutriverse-series-browser.html items=nv_writing_items", writing)
        self.assertIn('name="series"', writing)
        self.assertIn("data-writing-series=", writing)
        self.assertIn("'series'", script)
        self.assertIn("allowedSeries", script)
        self.assertIn("item.series === state.series", script)
        self.assertIn("[data-writing-series-link]", script)

    def test_post_series_is_chronological_and_has_bounded_neighbors(self):
        include = (ROOT / "_includes" / "post-series.html").read_text(encoding="utf-8")
        self.assertIn(
            "site.posts | where: 'series', page.series | where_exp: 'post', "
            "'post.hidden != true' | sort: 'date'",
            include,
        )
        self.assertIn("site.data.content_taxonomy.series | where: 'label', page.series | first", include)
        self.assertIn("?series={{ series_id | url_encode }}", include)
        self.assertIn("current_index > 0", include)
        self.assertIn("current_index < last_index", include)
        self.assertIn("series_posts[previous_index]", include)
        self.assertIn("series_posts[next_index]", include)
        self.assertIn('rel="prev" data-series-previous', include)
        self.assertIn('rel="next" data-series-next', include)
        self.assertNotIn("page.categories", include)


if __name__ == "__main__":
    unittest.main()
