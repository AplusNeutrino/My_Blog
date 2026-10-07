from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CONFIG = (ROOT / "_data" / "neutriverse_home.yml").read_text(encoding="utf-8")
LAYOUT = (ROOT / "_layouts" / "home.html").read_text(encoding="utf-8")


class HomepageConfigurationTest(unittest.TestCase):
    def test_section_order_is_explicit_and_stable(self):
        order = re.search(
            r"section_order:\n(?P<body>(?:  - .+\n)+)", CONFIG
        )
        self.assertIsNotNone(order)
        self.assertEqual(
            re.findall(r"  - ([a-z_]+)", order.group("body")),
            [
                "identity",
                "latest_transmissions",
                "explore",
                "current_signal",
                "featured",
                "system_status",
            ],
        )

    def test_sources_and_visibility_policy_are_explicit(self):
        for contract in (
            "primary_source: visible_posts",
            "fragment_source: thoughts.fragments",
            "project_log_relation: project",
            "source: neutriverse_sections.sections",
            "post_scope: visible_posts",
        ):
            self.assertIn(contract, CONFIG)
        self.assertEqual(CONFIG.count("hidden_policy: exclude"), 2)

    def test_current_signal_uses_only_the_approved_site_fact(self):
        self.assertIn("title: Neutriverse 网站重构", CONFIG)
        self.assertIn("source: approved_master_plan", CONFIG)
        for forbidden in ("工作", "考试", "住址", "健康"):
            self.assertNotIn(forbidden, CONFIG)

    def test_latest_visible_post_is_primary_and_featured_has_one_source(self):
        self.assertIn("site.data.neutriverse_home", LAYOUT)
        self.assertIn(
            "home_visible_posts = site.posts | where_exp: 'item', "
            "'item.hidden != true'",
            LAYOUT,
        )
        self.assertIn(
            "home_visible_posts | concat: home_fragments | sort: 'date' | reverse",
            LAYOUT,
        )
        self.assertNotIn("site.data.home_recommend", LAYOUT)
        self.assertNotIn("all_pinned", LAYOUT)
        self.assertIn('data-home-section="latest_transmissions"', LAYOUT)
        self.assertIn("home_config.featured", CONFIG)

    def test_legacy_recommend_file_contains_no_duplicate_values(self):
        legacy = (ROOT / "_data" / "home_recommend.yml").read_text(encoding="utf-8")
        self.assertIn("_data/neutriverse_home.yml", legacy)
        self.assertNotRegex(legacy, r"^sub_rec_", msg=legacy)


if __name__ == "__main__":
    unittest.main()
