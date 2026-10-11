import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALE = (ROOT / "_data" / "locales" / "zh-CN.yml").read_text(encoding="utf-8")
EXPECTED = {
    "about.md": ("about", "中间层漫游指南"),
    "archives.md": ("archives", "中间层时间线"),
    "categories.md": ("categories", "中间文段索引"),
    "library.md": ("library", "中间层大图书馆"),
    "links.md": ("links", "中间层友情链接"),
    "tags.md": ("tags", "中间文段标签"),
    "thoughts.md": ("thoughts", "中间思维片段"),
}


class TabTitlesTest(unittest.TestCase):
    def test_custom_tabs_use_stable_locale_identifier_titles(self):
        for filename, (identifier, localized) in EXPECTED.items():
            source = (ROOT / "_tabs" / filename).read_text(encoding="utf-8")
            title_line = next(
                (line for line in source.splitlines() if line.startswith("title:")),
                None,
            )
            self.assertIsNotNone(title_line, filename)
            actual = title_line.split(":", 1)[1].strip().strip("\"'")
            self.assertEqual(actual, identifier, filename)
            self.assertIn(f"  {identifier}: {localized}", LOCALE, filename)

    def test_identifiers_are_documented_as_head_title_contract(self):
        self.assertIn("_tabs front matter titles as stable identifier keys", LOCALE)
        self.assertIn("contextual <title>", LOCALE)


if __name__ == "__main__":
    unittest.main()
