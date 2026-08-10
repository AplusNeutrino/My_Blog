import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEME_INCLUDE = ROOT / "_includes" / "poe-night-mode.html"
DAY_THEME = ROOT / "assets" / "css" / "ProsperoLight.css"
NIGHT_THEME = ROOT / "assets" / "css" / "NormaiNight.css"


class ThemeToggleRegressionTest(unittest.TestCase):
    def test_inline_script_survives_jekyll_html_compression(self):
        """Line comments swallow code when the compress layout folds JS to one line."""
        source = THEME_INCLUDE.read_text(encoding="utf-8")
        scripts = re.findall(r"<script[^>]*>(.*?)</script>", source, re.DOTALL)

        self.assertEqual(len(scripts), 1)
        self.assertNotRegex(
            scripts[0],
            r"(?m)^\s*//",
            "Inline JavaScript must use block comments because layout: compress folds lines",
        )

    def test_toggle_replaces_chirpy_dropdown_with_direct_switch(self):
        source = THEME_INCLUDE.read_text(encoding="utf-8")

        self.assertIn("menu?.remove()", source)
        self.assertIn("toggle.classList.remove('dropdown-toggle', 'show')", source)
        self.assertIn("event.stopImmediatePropagation()", source)
        self.assertIn("setPreference(getVisualMode() === 'light' ? 'dark' : 'light')", source)

    def test_custom_theme_scopes_match_chirpy_root_specificity(self):
        """Chirpy scopes palette values with :root[data-bs-theme], not html[data-*]."""
        for path in (DAY_THEME, NIGHT_THEME):
            with self.subTest(path=path.name):
                source = path.read_text(encoding="utf-8")
                self.assertNotRegex(
                    source,
                    r"\bhtml\[data-(?:mode|bs-theme)=",
                    "Theme selectors must match Chirpy's :root specificity",
                )

    def test_daylight_owns_bootstrap_related_post_and_comment_surfaces(self):
        source = DAY_THEME.read_text(encoding="utf-8")

        self.assertIn("--bs-body-bg: var(--prospero-page);", source)
        self.assertRegex(
            source,
            r"(?s)#related-posts \.post-preview.*?background:\s*var\(--prospero-surface-1\)",
        )
        self.assertRegex(
            source,
            r"(?s)\.twikoo-comments\s*,.*?background:\s*var\(--prospero-surface-1\)",
        )
        self.assertRegex(
            source,
            r"(?s)\.twikoo-comments \.el-input__inner.*?background:\s*var\(--prospero-page\)",
        )

    def test_night_theme_owns_bootstrap_and_related_post_surfaces(self):
        source = NIGHT_THEME.read_text(encoding="utf-8")

        self.assertIn("--bs-body-bg: var(--night-void);", source)
        self.assertRegex(
            source,
            r"(?s)#related-posts \.post-preview.*?background:\s*var\(--night-surface-1\)",
        )


if __name__ == "__main__":
    unittest.main()
