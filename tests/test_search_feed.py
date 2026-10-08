import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = (ROOT / "_data" / "neutriverse_discovery.yml").read_text(encoding="utf-8")
SEARCH = (ROOT / "assets" / "js" / "data" / "search.json").read_text(encoding="utf-8")
FEED = (ROOT / "feed.xml").read_text(encoding="utf-8")
HEAD = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
CHECKER = (ROOT / "tools" / "check_search_feed.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "pages-deploy.yml").read_text(encoding="utf-8")


class SearchFeedTest(unittest.TestCase):
    def test_discovery_policy_is_explicit_and_bounded(self):
        self.assertIn("schema_version: 1", CONFIG)
        self.assertEqual(2, CONFIG.count("include_posts: true"))
        self.assertEqual(2, CONFIG.count("include_fragments: true"))
        self.assertEqual(2, CONFIG.count("exclude_hidden: true"))
        self.assertIn("path: /feed.xml", CONFIG)
        self.assertIn("format: atom", CONFIG)
        self.assertIn("limit: 20", CONFIG)

    def test_search_indexes_public_posts_and_original_fragments(self):
        self.assertIn("site.posts | where_exp: 'post', 'post.hidden != true'", SEARCH)
        self.assertIn("fragment_page.fragments", SEARCH)
        self.assertIn("fragment_page.url", SEARCH)
        self.assertIn('"type": "fragment"', SEARCH)
        self.assertIn("fragment.text | jsonify", SEARCH)

    def test_atom_feed_combines_public_writing_on_the_existing_route(self):
        self.assertIn("permalink: /feed.xml", FEED)
        self.assertIn("item.hidden != true", FEED)
        self.assertIn("visible_posts | concat: fragments | sort: 'date' | reverse", FEED)
        self.assertIn("slice: 0, discovery.limit", FEED)
        self.assertIn("fragment_page.url", FEED)
        self.assertIn('xmlns="http://www.w3.org/2005/Atom"', FEED)

    def test_pages_advertise_and_validate_the_feed(self):
        self.assertIn('rel="alternate" type="application/atom+xml"', HEAD)
        self.assertIn("site.data.neutriverse_discovery.feed.path", HEAD)
        self.assertIn("hidden post leaked into Search", CHECKER)
        self.assertIn("hidden post leaked into feed", CHECKER)
        build = WORKFLOW.index("- name: Build site")
        check = WORKFLOW.index("- name: Validate Search and Atom feed")
        upload = WORKFLOW.index("- name: Upload site artifact")
        self.assertLess(build, check)
        self.assertLess(check, upload)
        self.assertIn('python tools/check_search_feed.py "_site${{ steps.pages.outputs.base_path }}"', WORKFLOW)

    def test_built_output_validator_ignores_commented_fragment_example(self):
        self.assertIn('text.split("---", 2)', CHECKER)
        self.assertIn("front_matter,", CHECKER)


if __name__ == "__main__":
    unittest.main()
