import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALE = (ROOT / "_data" / "locales" / "zh-CN.yml").read_text(encoding="utf-8")
EXPECTED = {
    "about.md": "中间层漫游指南",
    "archives.md": "中间层时间线",
    "categories.md": "中间文段索引",
    "library.md": "中间层大图书馆",
    "links.md": "中间层友情链接",
    "tags.md": "中间文段标签",
    "thoughts.md": "中间思维片段",
}


class TabTitlesTest(unittest.TestCase):
    def test_custom_tab_front_matter_titles_have_locale_aliases(self):
        for filename, expected in EXPECTED.items():
            source = (ROOT / "_tabs" / filename).read_text(encoding="utf-8")
            match = re.search(r"^title:\\s*[\"']?(.+?)[\"']?\\s*$", source, re.MULTILINE)
            self.assertIsNotNone(match, filename)
            self.assertEqual(match.group(1), expected, filename)
            self.assertIn(f"  {expected}: {expected}", LOCALE, filename)

    def test_aliases_are_documented_as_head_title_contract(self):
        self.assertIn("page.title | downcase", LOCALE)
        self.assertIn("<title>", LOCALE)


if __name__ == "__main__":
    unittest.main()
