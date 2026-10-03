import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERIES_INCLUDE = ROOT / "_includes" / "post-series.html"


class PostSeriesVisibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = SERIES_INCLUDE.read_text(encoding="utf-8")

    def test_series_panel_requires_explicit_series_on_visible_page(self):
        self.assertIn("{% if page.series and page.hidden != true %}", self.template)

    def test_series_posts_exclude_hidden_content(self):
        self.assertIn(
            "where: 'series', page.series | where_exp: 'post', 'post.hidden != true'",
            self.template,
        )

    def test_category_fallback_is_removed(self):
        self.assertNotIn("page.categories", self.template)
        self.assertNotIn("data-series-posts", self.template)
        self.assertNotIn("Legacy fallback", self.template)


if __name__ == "__main__":
    unittest.main()
