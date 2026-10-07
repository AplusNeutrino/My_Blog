from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ThinkRetrievalEntriesTest(unittest.TestCase):
    def test_think_declares_real_archive_tags_and_search_entries(self):
        data = (ROOT / "_data" / "neutriverse_sections.yml").read_text(encoding="utf-8")
        self.assertIn("kind: Archive\n        url: /archives/", data)
        self.assertIn("kind: Tags\n        url: /tags/", data)
        self.assertIn("kind: Search\n        action: search", data)

        include = (ROOT / "_includes" / "neutriverse-section-links.html").read_text(
            encoding="utf-8"
        )
        self.assertIn("link.action == 'search'", include)
        self.assertIn("data-nv-search-trigger", include)
        self.assertIn('type="button"', include)
        self.assertNotIn('href="#"', include)

    def test_all_search_proxies_are_wired_to_the_native_search(self):
        script = (ROOT / "assets" / "js" / "neutriverse-navigation.js").read_text(
            encoding="utf-8"
        )
        self.assertIn("querySelectorAll('[data-nv-search-trigger]')", script)
        self.assertIn("searchTriggers.forEach", script)
        self.assertIn("document.getElementById('search-trigger')", script)
        self.assertIn("searchInput?.focus()", script)

    def test_archive_tags_and_search_index_filter_hidden_posts(self):
        archive = (ROOT / "_layouts" / "archives.html").read_text(encoding="utf-8")
        tags = (ROOT / "_layouts" / "tags.html").read_text(encoding="utf-8")
        tag = (ROOT / "_layouts" / "tag.html").read_text(encoding="utf-8")
        search = (ROOT / "assets" / "js" / "data" / "search.json").read_text(
            encoding="utf-8"
        )
        hidden_filter = "where_exp: 'post', 'post.hidden != true'"
        for source in (archive, tags, tag, search):
            self.assertIn(hidden_filter, source)

    def test_legacy_retrieval_routes_remain_unchanged(self):
        archives = (ROOT / "_tabs" / "archives.md").read_text(encoding="utf-8")
        tags = (ROOT / "_tabs" / "tags.md").read_text(encoding="utf-8")
        self.assertIn("layout: archives", archives)
        self.assertIn("layout: tags", tags)
        self.assertNotIn("permalink:", archives)
        self.assertNotIn("permalink:", tags)


if __name__ == "__main__":
    unittest.main()
