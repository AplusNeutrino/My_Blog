"""UI-011 regression wiring; actual screenshot acceptance remains separate."""
import ast
from pathlib import Path
import unittest


class LibraryLedgerOverlapTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'library_ledger_controls')
        return source, ast.get_source_segment(source, node)

    def test_scoped_edge_reserve_not_global_button_mutation(self):
        css = Path('assets/pgl/pgl.css').read_text()
        media = css.split('@media (max-width: 1199px) {', 1)[1].split('@media', 1)[0]
        self.assertIn('.pgl-category-ledger-item,.pgl-wishlist-entry { padding-inline-end:3.5rem; }', media)
        self.assertNotIn('#back-to-top', media)
        self.assertNotIn('font-size', media)
        self.assertNotIn('display:none', media)

    def test_real_text_intersection_and_scroll_scenarios(self):
        source, helper = self.helper()
        for text in ('window.scrollBy', 'range.getClientRects()', "not geometry['overlaps']",
                     "geometry['clientViewport']", "geometry['buttonHit']", 'document.elementFromPoint',
                     "g['selectedInButtonBand']", 'len(counts) == 8', 'len(wishlist_counts) == 7',
                     "ledger-{state}-{width}-{theme}-library.json", 'save_screenshot'):
            self.assertIn(text, helper)
        self.assertIn('ledger_result = library_ledger_controls(', source)
        self.assertIn("'ledger':ledger_result", source)

    def test_real_navigation_and_fixed_button_not_synthetic_click(self):
        _, helper = self.helper()
        for text in ('entry.click()', 'back.click()', 'top.click()', 'return scrollY <= 1',
                     "'book'", "'comic'", "'music'", "'wishlist-entry'", "'wishlist-first'", "'wishlist-last'"):
            self.assertIn(text, helper)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('.focus()', helper)
        self.assertNotIn('except', helper)
