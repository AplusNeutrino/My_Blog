import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ModuleNavigationTest(unittest.TestCase):
    def test_probe_module_links_to_occult_atlas_and_ravenis(self):
        source = (ROOT / "_includes" / "probe-tracking-module.html").read_text(
            encoding="utf-8"
        )

        self.assertIn("href=\"{{ '/occult-atlas/' | relative_url }}\"", source)
        self.assertIn("<span>OCCULT ATLAS</span>", source)
        self.assertIn("<strong>星图</strong>", source)
        self.assertIn("href=\"{{ '/ravenis/' | relative_url }}\"", source)
        self.assertIn("<span>RAVENIS</span>", source)
        self.assertIn("<strong>渡鸦之眼</strong>", source)

    def test_ravenis_page_uses_eyes_title(self):
        source = (ROOT / "ravenis" / "index.html").read_text(encoding="utf-8")

        self.assertIn('title: "渡鸦之眼（Ravenis’ Eyes）"', source)


if __name__ == "__main__":
    unittest.main()
