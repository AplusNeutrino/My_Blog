import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MobileTopbarTests(unittest.TestCase):
    def test_custom_layouts_use_page_title_before_layout_fallback(self):
        source = (ROOT / '_includes/topbar.html').read_text(encoding='utf-8')
        branch = source.index("page.layout == 'neutriverse-section'")
        fallback = source.index('layout[page.layout]')
        self.assertLess(branch, fallback)
        self.assertIn('page.title | escape', source[branch:fallback])
        self.assertIn('title="{{ page.title | escape }}"', source)

    def test_long_title_does_not_grow_over_controls(self):
        source = (ROOT / 'assets/css/neutriverse-sections.css').read_text(encoding='utf-8')
        block = source.split('#topbar-title {', 1)[1].split('}', 1)[0]
        for rule in ('min-width: 0', 'overflow: hidden', 'text-overflow: ellipsis'):
            self.assertIn(rule, block)


if __name__ == '__main__':
    unittest.main()
