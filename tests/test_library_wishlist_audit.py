"""Audit wiring only; real responsive screenshots remain required."""
import ast
from pathlib import Path
import unittest


class LibraryWishlistAuditTests(unittest.TestCase):
    def test_real_navigation_reload_counts_isolation_and_geometry(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_wishlist_controls')
        helper = ast.get_source_segment(source, node)
        for text in ('element.click()', 'driver.refresh()', 'ids() == expected',
                     'sum(counts.values())', "get_attribute('data-category') == category",
                     "get_attribute('data-status') == 'wishlist'", '.pgl-empty',
                     "capture('index')", "capture('category')", "capture('reloaded')", "capture('empty')",
                     "require(not params()", 'ids() == book_ids',
                     "geometry['page'] <= geometry['viewport']+1", "e['scroll'] <= e['client']+1",
                     'save_screenshot', 'write_text(json.dumps(geometry'):
            self.assertIn(text, helper)
        self.assertIn('wishlist = library_wishlist_controls(', source)
        self.assertIn("'wishlist':wishlist", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('localStorage.setItem', helper)
        self.assertNotIn('execute_script("arguments[0].click', helper)
