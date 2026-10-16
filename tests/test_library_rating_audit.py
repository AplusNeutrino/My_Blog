"""Audit wiring only; Chrome screenshots and real keyboard checks remain required."""
import ast
from pathlib import Path
import unittest


class LibraryRatingAuditTests(unittest.TestCase):
    def test_actual_scopes_data_keyboard_tooltips_and_refresh(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_rating_controls')
        helper = ast.get_source_segment(source, node)
        for value in ('rating_curve_distribution', 'element.click()', 'driver.refresh()',
                      'all_button.send_keys(Keys.SHIFT, Keys.TAB)', 'ActionChains(driver)',
                      'document.activeElement', 'tooltip(0)', 'tooltip(len(bins)-1)',
                      'scopes["all"][index]', 'numbers[0] == total', 'abs(numbers[1]-mean)',
                      "capture('tooltip-last')", "capture('tooltip-first')", "verify('all')",
                      'save_screenshot', 'write_text(json.dumps(geometry',
                      "geometry['page'] <= geometry['viewport']+1", "'Rating tooltip outside viewport'"):
            self.assertIn(value, helper)
        self.assertIn('rating_result = library_rating_controls(', source)
        self.assertIn("'rating':rating_result", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('.focus()', helper)
        self.assertNotIn('localStorage.setItem', helper)
