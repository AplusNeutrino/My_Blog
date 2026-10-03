from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TagVisibilityAndRedirectTests(unittest.TestCase):
    def test_public_tag_index_filters_hidden_posts_and_counts_visible_relations(self):
        template = (ROOT / "_layouts" / "tags.html").read_text(encoding="utf-8")
        self.assertIn("where_exp: 'post', 'post.hidden != true'", template)
        self.assertIn("visible_tag_posts.size > 0", template)
        self.assertIn("plus: visible_tag_posts.size", template)
        self.assertNotIn("site.tags[t].size", template)

    def test_tag_detail_filters_hidden_posts(self):
        template = (ROOT / "_layouts" / "tag.html").read_text(encoding="utf-8")
        self.assertIn("page.posts | where_exp: 'post', 'post.hidden != true'", template)
        self.assertIn("{% for post in visible_posts %}", template)
        self.assertIn("暂无公开记录", template)

    def test_trending_tags_ignore_hidden_only_relations(self):
        template = (ROOT / "_includes" / "trending-tags.html").read_text(encoding="utf-8")
        self.assertIn("where_exp: 'post', 'post.hidden != true'", template)
        self.assertIn("{% if tag_size > 0 %}", template)

    def test_legacy_tag_routes_are_noindex_redirects(self):
        cases = {
            "bus": "/tags/system-bus/",
            "changelog": "/tags/neutriverse/",
        }
        for source, target in cases.items():
            with self.subTest(source=source):
                page = (ROOT / "tags" / source / "index.html").read_text(encoding="utf-8")
                self.assertIn(f"permalink: /tags/{source}/", page)
                self.assertIn("sitemap: false", page)
                self.assertIn('name="robots" content="noindex, follow"', page)
                self.assertGreaterEqual(page.count(target), 3)


if __name__ == "__main__":
    unittest.main()
