import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LAYOUT = ROOT / "_layouts" / "occult-atlas.html"
STYLES = ROOT / "occult-atlas-app" / "styles.css"
CONFIG = ROOT / "_data" / "occult_atlas.yml"


class OccultAtlasThemeTest(unittest.TestCase):
    @staticmethod
    def _relative_luminance(color):
        channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        channels = [
            value / 12.92
            if value <= 0.04045
            else ((value + 0.055) / 1.055) ** 2.4
            for value in channels
        ]
        return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

    @classmethod
    def _contrast_ratio(cls, foreground, background):
        lighter, darker = sorted(
            (cls._relative_luminance(foreground), cls._relative_luminance(background)),
            reverse=True,
        )
        return (lighter + 0.05) / (darker + 0.05)

    def test_layout_reuses_the_main_site_theme_controller(self):
        source = LAYOUT.read_text(encoding="utf-8")
        controller = "{% include poe-night-mode.html %}"
        stylesheet = "occult-atlas-app/styles.css"

        self.assertIn(controller, source)
        self.assertLess(source.index(controller), source.index(stylesheet))

    def test_light_theme_defines_the_complete_atlas_palette(self):
        source = STYLES.read_text(encoding="utf-8")
        match = re.search(
            r"html\[data-mode='light'\],\s*"
            r"html\[data-bs-theme='light'\]\s*\{(?P<body>.*?)\n\}",
            source,
            re.DOTALL,
        )

        self.assertIsNotNone(match)
        light_palette = match.group("body")
        for token in (
            "--atlas-void",
            "--atlas-main",
            "--atlas-surface",
            "--atlas-heading",
            "--atlas-text",
            "--atlas-chart-ring",
            "--atlas-chart-grid",
            "--atlas-chart-state",
            "--atlas-callout-fill",
        ):
            self.assertIn(token, light_palette)

        self.assertIn("color-scheme: light", light_palette)

        colors = dict(
            re.findall(r"(--atlas-[\w-]+):\s*(#[0-9a-fA-F]{6})", light_palette)
        )
        self.assertGreaterEqual(
            self._contrast_ratio(colors["--atlas-heading"], colors["--atlas-main"]),
            4.5,
        )
        self.assertGreaterEqual(
            self._contrast_ratio(colors["--atlas-text"], colors["--atlas-main"]),
            4.5,
        )
        self.assertGreaterEqual(
            self._contrast_ratio(colors["--atlas-muted"], colors["--atlas-main"]),
            4.5,
        )

    def test_theme_sensitive_chart_colors_use_palette_tokens(self):
        source = STYLES.read_text(encoding="utf-8")

        self.assertIn("stroke: var(--atlas-chart-ring)", source)
        self.assertIn("stroke: var(--atlas-chart-grid)", source)
        self.assertIn("background: var(--atlas-chart-state)", source)
        self.assertIn("fill: var(--atlas-callout-fill)", source)

    def test_asset_version_is_bumped_for_theme_css(self):
        source = CONFIG.read_text(encoding="utf-8")

        self.assertIn('asset_version: "38"', source)

    def test_existing_responsive_breakpoints_still_cover_mobile(self):
        source = STYLES.read_text(encoding="utf-8")

        self.assertIn("@media (max-width: 1100px)", source)
        self.assertIn("@media (max-width: 700px)", source)
        self.assertIn("@media (max-width: 430px)", source)


if __name__ == "__main__":
    unittest.main()
