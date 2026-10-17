"""Wiring regressions only; actual PNGs and human visual review are still required."""
# Historical filename retained; native row views replace unreliable CDP full pages.
import ast
from pathlib import Path
import unittest


class LibraryBookRowViewportAuditTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_book_row_viewports')
        return source, ast.get_source_segment(source, node)

    def test_native_viewports_no_cdp_layout_or_loader_override(self):
        source, helper = self.helper()
        for text in ('get_screenshot_as_png', 'scrollIntoView', 'requestAnimationFrame', "get_attribute('open')",
                     'i.naturalWidth', 'i.naturalHeight', "i['complete']", "i['width'] > 0"):
            self.assertIn(text, helper)
        for forbidden in ('execute_cdp_cmd', 'captureBeyondViewport', 'set_window_size', 'setDeviceMetricsOverride', '.style', '.src =', '.loading =', 'dispatchEvent', 'except'):
            self.assertNotIn(forbidden, helper)
        self.assertIn('row_views = library_book_row_viewports(', source)
        self.assertIn("row_views['coveredIds'] == ordered", source)

    def test_actual_png_dimensions_and_complete_row_coverage(self):
        _, helper = self.helper()
        for text in ("raw[12:16] == b'IHDR'", "int.from_bytes(raw[16:20], 'big')",
                     "int.from_bytes(raw[20:24], 'big')", "image_width == observed['viewport']['width']",
                     "image_height == observed['viewport']['height']", "c['top'] >= observed['topbarBottom']",
                     "c['bottom'] <= observed['viewport']['height']", 'covered == expected',
                     "observed['viewport']['clientWidth']+1", "f'{stem}.png').write_bytes(raw)",
                     "f'{stem}.json').write_text", "for start in range(0, len(cards), columns)"):
            self.assertIn(text, helper)
