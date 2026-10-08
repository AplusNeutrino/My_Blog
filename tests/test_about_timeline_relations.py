import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / "_data" / "neutriverse_about.yml").read_text(encoding="utf-8")
PROFILE = (ROOT / "_includes" / "neutriverse-about-profile.html").read_text(
    encoding="utf-8"
)
ABOUT = (ROOT / "_tabs" / "about.md").read_text(encoding="utf-8")
SECTIONS = (ROOT / "_data" / "neutriverse_sections.yml").read_text(
    encoding="utf-8"
)


class AboutTimelineRelationsTest(unittest.TestCase):
    def test_timeline_is_sourced_and_chronological(self):
        timeline = DATA.split("\ntimeline:\n", 1)[1].split("\nrelations:\n", 1)[0]
        dates = re.findall(r'^    - date: "(\d{4}-\d{2}-\d{2})"$', timeline, re.MULTILINE)
        self.assertEqual(len(dates), 5)
        self.assertEqual(dates, sorted(dates))
        self.assertEqual(timeline.count("      source_label:"), 5)
        self.assertEqual(timeline.count("      source_url:"), 5)
        self.assertEqual(timeline.count("      external:"), 5)
        for commit in (
            "bfcdf3493efee6a1576456b793df28ac911421e8",
            "32feb1bbd35ea6b6151d79c45057d07a71da748c",
            "406cbef6805d1fb063300124e59dab75783c0773",
        ):
            self.assertIn(
                f"https://github.com/AplusNeutrino/My_Blog/commit/{commit}", timeline
            )
        for route in (
            "/posts/阿卡夏便笺akashanotes/",
            "/posts/丰聪耳机toyosatomimisheadphone/",
        ):
            self.assertIn(route, timeline)

    def test_timeline_renderer_exposes_dates_sources_and_safe_external_links(self):
        for marker in (
            "data-about-timeline",
            'datetime="{{ event.date }}"',
            "{{ event.source_label }}",
            "event.source_url | relative_url",
            'target="_blank" rel="noopener noreferrer"',
        ):
            self.assertIn(marker, PROFILE)

    def test_relation_cards_keep_public_actions_and_make_travel_inert(self):
        relations = DATA.split("\nrelations:\n", 1)[1].split("\nsnapshot:\n", 1)[0]
        self.assertEqual(relations.count("    - id:"), 3)
        for route in ("/library/", "/links/"):
            self.assertIn(f"      url: {route}", relations)
        travel = relations.split("    - id: travel\n", 1)[1]
        self.assertIn("status: 能力保留 · 当前未公开", travel)
        self.assertIn("action_label: 暂未开放", travel)
        self.assertNotIn("      url:", travel)
        self.assertIn('data-about-relation="{{ relation.id }}"', PROFILE)
        self.assertIn("{% if relation.url %}", PROFILE)
        self.assertIn('aria-disabled="true"', PROFILE)

    def test_hidden_travel_implementation_and_library_sync_are_untouched(self):
        for marker in (
            "travel_globe_enabled = false",
            "site.data.travel_regions",
            "site.data.travel_boundary_sources",
            "assets/js/travel-globe.js",
        ):
            self.assertIn(marker, ABOUT)
        self.assertNotIn("/about/#travel-globe-title", SECTIONS)
        self.assertIn("/about/#about-relations-title", SECTIONS)
        self.assertTrue(
            (ROOT / "_data" / "prospero_great_library" / "sync_status.json").exists()
        )

    def test_timeline_is_site_history_not_archive_or_private_biography(self):
        timeline = DATA.split("\ntimeline:\n", 1)[1].split("\nrelations:\n", 1)[0]
        self.assertIn("写作发布时间线仍由 Archive 单独承担", timeline)
        for private_marker in ("住址", "单位", "邮箱", "健康"):
            self.assertNotIn(private_marker, timeline)


if __name__ == "__main__":
    unittest.main()
