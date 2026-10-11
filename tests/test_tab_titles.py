import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")
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
    def test_custom_tab_front_matter_titles_are_preserved(self):
        for filename, expected in EXPECTED.items():
            source = (ROOT / "_tabs" / filename).read_text(encoding="utf-8")
            title_line = next(
                (line for line in source.splitlines() if line.startswith("title:")),
                None,
            )
            self.assertIsNotNone(title_line, filename)
            actual = title_line.split(":", 1)[1].strip().strip("\"'")
            self.assertEqual(actual, expected, filename)

    def test_head_falls_back_to_custom_tab_title(self):
        self.assertIn(
            "site.data.locales[include.lang].tabs[tab_key] | default: page.title",
            HEAD,
        )


if __name__ == "__main__":
    unittest.main()
