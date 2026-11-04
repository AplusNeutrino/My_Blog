import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / "_data" / "neutriverse_about.yml").read_text(encoding="utf-8")
PROFILE = (ROOT / "_includes" / "neutriverse-about-profile.html").read_text(
    encoding="utf-8"
)
CONFIG = (ROOT / "_config.yml").read_text(encoding="utf-8")
HOME = (ROOT / "_data" / "neutriverse_home.yml").read_text(encoding="utf-8")


class AboutIdentityCurrentlyTest(unittest.TestCase):
    def test_currently_is_a_dated_site_signal_not_a_personal_claim(self):
        for marker in (
            "title: 目前正在整理这个网站",
            'as_of: "2026-10-08"',
            "notice: 网站维护状态 · 非个人实时状态",
            "source_label: 来源：已批准的 Neutriverse 重构主计划",
            'data-about-current data-as-of="{{ about.currently.as_of }}"',
            '<time datetime="{{ about.currently.as_of }}">',
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA + PROFILE)
        self.assertIn("title: 目前正在整理这个网站", HOME)

    def test_maintenance_metadata_stays_in_source_not_public_html(self):
        for marker in (
            "file: _data/neutriverse_about.yml",
            "field: currently",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA)
        self.assertNotIn("about.currently.maintenance", PROFILE)
        self.assertNotIn("MAINTAIN", PROFILE)

    def test_public_coordinates_are_limited_to_existing_site_configuration(self):
        expected = (
            ("neutriverse.uk", 'url: "https://neutriverse.uk"'),
            ("AplusNeutrino", "username: AplusNeutrino"),
            ("@Neutrino_X", "username: Neutrino_X"),
            ("/links/", None),
        )
        for value, config_marker in expected:
            with self.subTest(value=value):
                self.assertIn(value, DATA)
                if config_marker:
                    self.assertIn(config_marker, CONFIG)
        self.assertNotIn("mailto:", DATA)
        self.assertNotIn("email", DATA.lower())

    def test_external_coordinates_use_safe_new_tab_attributes(self):
        self.assertIn("{% if link.external %}", PROFILE)
        self.assertIn('target="_blank" rel="noopener noreferrer"', PROFILE)
        self.assertIn("{% if link.external %}{{ link.url }}{% else %}", PROFILE)
        self.assertIn("{{ link.url | relative_url }}{% endif %}", PROFILE)

    def test_public_copy_avoids_meta_philosophy_and_preserves_real_lists(self):
        for marker in (
            "title: 站点与友链",
            "title: 2026 年 8 月的记录",
            "title: 待读书单",
            "title: 待看清单",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA)
        for marker in (
            "这个站如何生长",
            "清晰导航先于世界观",
            "状态应当可维护且诚实",
            "Neutrino 状态监控",
            "FUTURE READING STACK",
            "FUTURE MEDIA STACK",
            "data-about-philosophy",
        ):
            with self.subTest(marker=marker):
                self.assertNotIn(marker, DATA + PROFILE)

    def test_historical_snapshot_remains_separate_and_explicit(self):
        self.assertIn('as_of: "2026-08-17"', DATA)
        self.assertIn("notice: 历史快照 · 非实时状态", DATA)
        self.assertIn("data-about-snapshot", PROFILE)
        self.assertLess(PROFILE.index("data-about-current"), PROFILE.index("data-about-snapshot"))


if __name__ == "__main__":
    unittest.main()
