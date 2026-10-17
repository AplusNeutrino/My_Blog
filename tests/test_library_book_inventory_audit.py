"""Wiring regressions only; CI browser and human screenshot review remain required."""
import ast
from pathlib import Path
import unittest


class LibraryBookInventoryAuditTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_book_inventory_controls')
        return source, ast.get_source_segment(source, node)

    def test_complete_inventory_and_page_identity(self):
        source, helper = self.helper()
        for text in ("i['category'] == 'book'", "('in_progress', 'completed')",
                     'range(1, page_count+1)', 'set(seen) == set(books)',
                     'not set(ordered).intersection(seen)', 'len(set(ordered)) == len(ordered)',
                     "min(page_size, len(books)-(number-1)*page_size)",
                     "'#pgl-pagination [aria-current=\"page\"]'"):
            self.assertIn(text, helper)
        self.assertIn('book_inventory = library_book_inventory_controls(', source)
        self.assertIn("'bookInventory':book_inventory", source)

    def test_native_loading_geometry_and_honest_screenshot_scope(self):
        _, helper = self.helper()
        for text in ('scrollIntoView', 'e.decode()', "image['width'] > 0", "image['height'] > 0",
                     "initial['cards'][index]", "c['before']['top'] >= c['viewportHeight']",
                     "observed['clientViewport']+1", 'check_bounds(geometry())',
                     "capture(number, 'first'", "capture(number, 'last'", 'save_screenshot',
                     'full-page-and-first-last-card-viewports-per-book-page'):
            self.assertIn(text, helper)
        for forbidden in ('.src =', '.loading =', 'dispatchEvent', '.focus()', 'except'):
            self.assertNotIn(forbidden, helper)

    def test_reload_previous_reentry_use_real_controls(self):
        _, helper = self.helper()
        for text in ('driver.refresh()', 'driver.current_url == last_url', 'ids() == last_ids',
                     "click('#pgl-pagination .pgl-page-nav:first-child')", "ids() == pages[-2]['ids']",
                     "click('#pgl-pagination .pgl-page-nav:last-child')", "ids() == first_ids",
                     "click('#pgl-back')", "'page' not in params()", 'not urlsplit(driver.current_url).query'):
            self.assertIn(text, helper)

    def test_capture_requires_real_panel_close_not_dom_visibility_alone(self):
        _, helper = self.helper()
        self.assertIn("click('.pgl-advanced summary')", helper)
        self.assertIn("wait.until(lambda d: not d.find_element(By.CSS_SELECTOR, '.pgl-advanced').get_attribute('open'))", helper)
        capture = helper.split('def capture(page_number, state, selector):', 1)[1].split('    ready()', 1)[0]
        self.assertLess(capture.index("get_attribute('open')"), capture.index('save_screenshot'))
