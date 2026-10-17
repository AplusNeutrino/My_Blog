"""Wiring regressions only; actual PNGs and human visual review are still required."""
import ast
from pathlib import Path
import unittest


class LibraryBookFullPageAuditTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_book_full_page')
        return source, ast.get_source_segment(source, node)

    def test_real_full_page_no_layout_or_loader_override(self):
        source, helper = self.helper()
        for text in ('Page.captureScreenshot', "'captureBeyondViewport':True", "'clip':clip",
                     'scrollTo({top:0,left:0', 'requestAnimationFrame', "get_attribute('open')",
                     'i.naturalWidth', 'i.naturalHeight', "i['complete']", "i['width'] > 0"):
            self.assertIn(text, helper)
        for forbidden in ('set_window_size', 'setDeviceMetricsOverride', '.style', '.src =', '.loading =', 'dispatchEvent', 'except'):
            self.assertNotIn(forbidden, helper)
        self.assertIn('full_page = library_book_full_page(', source)
        self.assertIn("[c['id'] for c in full_page['cards']] == ordered", source)

    def test_actual_png_dimensions_and_every_card_inside_clip(self):
        _, helper = self.helper()
        for text in ("raw[12:16] == b'IHDR'", "int.from_bytes(raw[16:20], 'big')",
                     "int.from_bytes(raw[20:24], 'big')", "image_width == clip['width']",
                     "image_height == clip['height']", "c['top'] >= 0", "c['bottom'] <= clip['height']",
                     "observed['viewport']['clientWidth']+1", "f'{stem}.png').write_bytes(raw)",
                     "f'{stem}.json').write_text", 'cards:[...document.querySelectorAll'):
            self.assertIn(text, helper)
