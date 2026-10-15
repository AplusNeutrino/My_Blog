"""Audit wiring, not a substitute for real browser or screenshot acceptance."""
import ast
from pathlib import Path
import unittest


class LibraryTimelineAuditTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'library_timeline_controls')
        return source, ast.get_source_segment(source, node)

    def test_real_load_repeat_refresh_keyboard_and_screenshots(self):
        source, helper = self.helper()
        for text in ('button.click()', 'driver.refresh()', 'button.send_keys(Keys.ENTER)',
                     'old_list.id', 'rows() == expected', "capture('start'", "capture('tail'",
                     "capture('reloaded'", 'save_screenshot', 'reload did not reset lazy timeline'):
            self.assertIn(text, helper)
        self.assertIn('timeline_result = library_timeline_controls(', source)
        self.assertIn("'timeline':timeline_result", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('innerHTML =', helper)

    def test_specific_row_and_page_overflow_diagnostics_are_strict(self):
        _, helper = self.helper()
        for text in ("r['scroll'] <= r['client']+1", "geometry['scrollX']", 'row overflow',
                     'page overflow', "timeline-{state}-{width}-{theme}-library.json"):
            self.assertIn(text, helper)
