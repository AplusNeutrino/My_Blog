from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
LAYOUT = (ROOT / "_layouts" / "home.html").read_text(encoding="utf-8")
CONFIG = (ROOT / "_data" / "neutriverse_home.yml").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(encoding="utf-8")


class HomepageCompletionTest(unittest.TestCase):
    def test_all_six_sections_are_rendered_in_configured_order(self):
        markers = [
            f'data-home-section="{section}"'
            for section in (
                "identity",
                "latest_transmissions",
                "explore",
                "current_signal",
                "featured",
                "system_status",
            )
        ]
        positions = [LAYOUT.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))

    def test_current_signal_reads_only_the_approved_config(self):
        self.assertIn("home_config.current_signal.title", LAYOUT)
        self.assertIn("home_config.current_signal.summary", LAYOUT)
        self.assertIn("home_config.current_signal.url", LAYOUT)
        self.assertIn("title: Neutriverse 网站重构", CONFIG)
        self.assertNotIn("site.time", LAYOUT)

    def test_featured_records_have_public_fallbacks_and_a_limit(self):
        self.assertIn("home_config.featured.posts", LAYOUT)
        self.assertIn("site.data.home_popular.posts", LAYOUT)
        self.assertIn("home_visible_posts", LAYOUT)
        self.assertIn("home_featured_urls | push: home_candidate.url", LAYOUT)
        self.assertIn("limit: home_featured_limit", LAYOUT)
        self.assertNotIn("view_count", LAYOUT)

    def test_status_is_derived_and_project_metric_degrades_naturally(self):
        self.assertIn(
            "home_record_count = home_visible_posts.size | plus: home_fragments.size",
            LAYOUT,
        )
        self.assertIn("home_latest_transmission = home_transmissions | first", LAYOUT)
        self.assertIn("site.data.neutriverse_projects.projects", LAYOUT)
        self.assertIn(
            "if home_project_catalog and home_project_catalog.size > 0", LAYOUT
        )
        self.assertNotRegex(CONFIG, r"project_count:\s*\d+")

    def test_mobile_and_theme_styles_use_shared_tokens(self):
        for token in (
            "var(--nv-surface-1)",
            "var(--nv-surface-2)",
            "var(--nv-text-strong)",
            "var(--nv-border)",
        ):
            self.assertIn(token, CSS)
        self.assertIn(".nv-home-featured-list", CSS)
        self.assertIn(".nv-home-status-grid", CSS)
        self.assertIn("@media (max-width: 767.98px)", CSS)


if __name__ == "__main__":
    unittest.main()
