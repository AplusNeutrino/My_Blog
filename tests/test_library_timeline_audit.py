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

    def test_real_load_refresh_keyboard_and_screenshots(self):
        source, helper = self.helper()
        for text in ('button.click()', 'driver.refresh()', 'button.send_keys(Keys.ENTER)',
                     'rows() == expected', "capture('start'", "capture('tail'",
                     "capture('reloaded'", 'save_screenshot', 'reload did not reset lazy timeline'):
            self.assertIn(text, helper)
        self.assertIn('timeline_result = library_timeline_controls(', source)
        self.assertIn("'timeline':timeline_result", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('innerHTML =', helper)

    def test_one_shot_loader_matches_existing_product_not_stale_button(self):
        _, helper = self.helper()
        markup = Path('_includes/pgl/library.html').read_text()
        product = Path('assets/pgl/pgl.js').read_text()
        self.assertIn('<div id="pgl-timeline"><button id="pgl-load-timeline"', markup)
        self.assertIn('box.replaceChildren(list)', product)
        self.assertIn("not driver.find_elements(By.ID, 'pgl-load-timeline')", helper)
        self.assertIn("'#pgl-timeline ul')) == 1", helper)
        self.assertNotIn('old_list.id', helper)
        self.assertEqual(helper.count('button.click()'), 1)

    def test_specific_row_and_page_overflow_diagnostics_are_strict(self):
        _, helper = self.helper()
        for text in ("r['scroll'] <= r['client']+1", "geometry['scrollX']", 'row overflow',
                     'page overflow', "timeline-{state}-{width}-{theme}-library.json"):
            self.assertIn(text, helper)
