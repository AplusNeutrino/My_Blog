import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEME_INCLUDE = ROOT / "_includes" / "poe-night-mode.html"


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


if __name__ == "__main__":
    unittest.main()
