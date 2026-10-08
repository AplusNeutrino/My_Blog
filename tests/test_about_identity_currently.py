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
            "title: Neutriverse 网站重构",
            'as_of: "2026-10-08"',
            "notice: 网站维护状态 · 非个人实时状态",
            "source_label: 来源：已批准的 Neutriverse 重构主计划",
            'data-about-current data-as-of="{{ about.currently.as_of }}"',
            '<time datetime="{{ about.currently.as_of }}">',
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA + PROFILE)
        self.assertIn("title: Neutriverse 网站重构", HOME)

    def test_currently_has_one_explicit_maintenance_point(self):
        for marker in (
            "file: _data/neutriverse_about.yml",
            "field: currently",
            "about.currently.maintenance.file",
            "about.currently.maintenance.field",
            "about.currently.maintenance.note",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA + PROFILE)

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

    def test_philosophy_matches_the_approved_information_architecture(self):
        for marker in (
            "写作属于网站本身",
            "清晰导航先于世界观",
            "连续性比重写更重要",
            "状态应当可维护且诚实",
            "THINK、BUILD、OBSERVE、ABOUT",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA)
        self.assertIn("about.philosophy.principles", PROFILE)

    def test_historical_snapshot_remains_separate_and_explicit(self):
        self.assertIn('as_of: "2026-08-17"', DATA)
        self.assertIn("notice: 历史快照 · 非实时状态", DATA)
        self.assertIn("data-about-snapshot", PROFILE)
        self.assertLess(PROFILE.index("data-about-current"), PROFILE.index("data-about-snapshot"))


if __name__ == "__main__":
    unittest.main()
