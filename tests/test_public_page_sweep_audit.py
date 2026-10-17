"""Audit wiring, not a substitute for real Chrome or human screenshot review."""
import ast
from pathlib import Path
import unittest


class PublicPageSweepAuditTests(unittest.TestCase):
    def helper(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef)
                  and n.name=='public_page_sweep')
        return source,ast.get_source_segment(source,node)

    def test_native_png_and_contiguous_main_coverage(self):
        _,helper=self.helper()
        for token in ('get_screenshot_as_png', "raw[12:16] == b'IHDR'", 'raw[16:20]', 'raw[20:24]',
                      'scroll_from_origin', 'ScrollOrigin.from_viewport', 'coverage gap',
                      "covered >= frames[-1]['mainEnd']-1", "observed['viewport']['clientWidth']+1"):
            self.assertIn(token,helper)
        for token in ('captureBeyondViewport', 'execute_cdp_cmd', 'set_window_size', '.style', 'dispatchEvent'):
            self.assertNotIn(token,helper)

    def test_real_public_navigation_return_and_top(self):
        source,helper=self.helper()
        for token in ('link.click()', 'driver.back()', 'd.current_url == original',
                      "By.ID, 'back-to-top'", 'top.click()', 'return scrollY <= 1',
                      "'/think/'", "'/build/'", "'/observe/'", "'/about/'",
                      "'/build/ravenis/'", "'/build/occult-atlas/'", "'/library/'", "'/links/'"):
            self.assertIn(token,helper)
        self.assertIn('public_page_sweep(driver, wait, output, width, theme, public_name)',source)
        self.assertIn("output / 'public-page-audit.json'",source)
        self.assertNotIn("'/navi/",helper)
        self.assertNotIn("'/gate/",helper)

    def test_return_settle_failure_retains_animation_evidence_and_reraises(self):
        _,helper=self.helper()
        for token in ('public-return-failure-', 'document.getAnimations()', 'a.playState',
                      'a.currentTime', 'getComputedTiming()', 'visitedBeforeFailure',
                      'settle-after-browser-back', 'except Exception:', 'raise'):
            self.assertIn(token,helper)
        self.assertIn('settle(driver, wait, theme)',helper)
        self.assertNotIn('setTimeout',helper)

    def test_real_pointer_leaves_hover_before_unchanged_settle(self):
        _,helper=self.helper()
        self.assertIn('pointer.pointer_action.move_to_location(width//2, 8)',helper)
        self.assertLess(helper.index('pointer.perform()'),helper.index('settle(driver, wait, theme)'))
        self.assertNotIn('.cancel()',helper)

    def test_home_recent_text_range_rejects_button_intersections(self):
        _,helper=self.helper()
        for token in ("if name == 'home':",'document.createTreeWalker','document.createRange()',
                      'range.getClientRects()',"'.nv-home-transmission'",'s.opacity',
                      "observed['recentTextButton']['overlaps']",'Homepage recent text covered by back-to-top'):
            self.assertIn(token,helper)
        css=Path('assets/css/neutriverse-sections.css').read_text()
        self.assertIn('padding-right: calc(1rem + 2.75rem);',css)
        self.assertIn('@media (max-width: 1199.98px)',css)
