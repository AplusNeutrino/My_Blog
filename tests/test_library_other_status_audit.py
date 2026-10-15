"""Audit wiring only; does not replace Chrome or visual acceptance."""
import ast
from pathlib import Path
import unittest


class LibraryOtherStatusAuditTests(unittest.TestCase):
    def test_real_status_controls_reload_isolation_and_geometry(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_other_status_controls')
        helper = ast.get_source_segment(source, node)
        for text in ('element.click()', 'driver.refresh()', 'ids() == expected',
                     "verify('game', 'dropped')", "verify('game', 'on_hold')",
                     "verify('book', 'on_hold')", "get_attribute('data-category') == category",
                     "get_attribute('data-status') == status", '.pgl-empty', '.pgl-status',
                     "capture('book-hold')", "capture('game-hold')", "capture('game-dropped')",
                     "capture('cleared')", "ids() == dropped_ids", "ids() == book_ids",
                     "geometry['page'] <= geometry['viewport']+1", "c['scroll'] <= c['client']+1",
                     'save_screenshot', 'write_text(json.dumps(geometry'):
            self.assertIn(text, helper)
        self.assertIn('other_status = library_other_status_controls(', source)
        self.assertIn("'otherStatus':other_status", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('localStorage.setItem', helper)
        self.assertIn("source: '', year: '', sort: 'updated', page: 1", Path('assets/pgl/pgl.js').read_text())
