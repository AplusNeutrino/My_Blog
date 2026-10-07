from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAYOUT = (ROOT / "_layouts" / "home.html").read_text(encoding="utf-8")
CONFIG = (ROOT / "_data" / "neutriverse_home.yml").read_text(encoding="utf-8")


class HomepageMixedStreamTest(unittest.TestCase):
    def test_identity_and_explore_use_public_shared_sources(self):
        self.assertIn("home_config.identity", LAYOUT)
        self.assertIn("NEUTRIVERSE", CONFIG)
        self.assertIn("owner: Neutrino", CONFIG)
        self.assertIn("neutriverse-primary-nav.html", LAYOUT)
        self.assertIn('data-home-section="identity"', LAYOUT)
        self.assertIn('data-home-section="explore"', LAYOUT)

    def test_posts_and_fragments_share_one_real_date_stream(self):
        self.assertIn(
            "site.posts | where_exp: 'item', 'item.hidden != true'", LAYOUT
        )
        self.assertIn("home_fragment_page.fragments", LAYOUT)
        self.assertIn(
            "home_visible_posts | concat: home_fragments | sort: 'date' | reverse",
            LAYOUT,
        )
        self.assertIn("limit: home_config.latest_transmissions.limit", LAYOUT)
        self.assertIn("fragment_source: thoughts.fragments", CONFIG)
        self.assertIn("limit: 8", CONFIG)

    def test_project_log_is_secondary_and_not_a_type(self):
        self.assertIn("home_config.project_logs", LAYOUT)
        self.assertIn("Project Log /", LAYOUT)
        self.assertIn("project: Akasha Notes", CONFIG)
        self.assertIn("project: Toyosatomimi's Headphone", CONFIG)
        types = (ROOT / "_data" / "content_taxonomy.yml").read_text(encoding="utf-8")
        self.assertEqual(
            set(re.findall(r"^  (fragment|note|essay):$", types, re.MULTILINE)),
            {"fragment", "note", "essay"},
        )
        self.assertNotRegex(types, r"^  project(?:_| )?log:", msg=types)

    def test_old_category_wall_and_home_pagination_are_removed(self):
        for marker in (
            "home-category-filter",
            "data-home-filter",
            "data-home-pager",
            "data-primary-category",
            "all_pinned",
        ):
            self.assertNotIn(marker, LAYOUT)

    def test_t20_sections_are_not_implemented_early(self):
        for section_id in ("current_signal", "featured", "system_status"):
            self.assertNotIn(f'data-home-section="{section_id}"', LAYOUT)


if __name__ == "__main__":
    unittest.main()
