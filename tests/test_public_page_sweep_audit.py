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
                      'range.getClientRects()',"'.nv-home-transmission, .nv-home-featured-card'",'s.opacity',
                      "observed['recentTextButton']['overlaps']",'Homepage recent/featured text covered by back-to-top'):
            self.assertIn(token,helper)
        css=Path('assets/css/neutriverse-sections.css').read_text()
        self.assertIn('padding-right: calc(1rem + 2.75rem);',css)
        self.assertIn('@media (max-width: 1199.98px)',css)

    def test_featured_outer_column_keeps_button_lane_without_changing_grid(self):
        _,helper=self.helper()
        self.assertIn('.nv-home-transmission, .nv-home-featured-card',helper)
        self.assertIn('surface:card.className',helper)
        css=Path('assets/css/neutriverse-sections.css').read_text()
        outer='@media (min-width: 768px) and (max-width: 1199.98px)'
        self.assertIn(outer,css)
        start=css.index(outer,css.index('/* UI-013:'))
        block=css[start:css.index('.nv-home-featured-card > p:first-child',start)]
        self.assertIn('.nv-home-featured-list > li:nth-child(2n) .nv-home-featured-card',block)
        self.assertIn('@media (max-width: 767.98px)',block)
        self.assertEqual(block.count('padding-right: calc(1rem + 2.75rem);'),2)
        self.assertNotIn('grid-template-columns',block)

    def test_observe_about_intro_range_rejects_missing_scope_and_intersections(self):
        _,helper=self.helper()
        block=helper[helper.index("elif name in ('observe', 'about'):"):helper.index('Public page native viewports have a coverage gap')]
        for token in ('[data-neutriverse-section="observe"] .nv-section-intro',
                      '[data-about-profile] .about-info-text', 'document.createTreeWalker',
                      'range.getClientRects()', "intro['rootCount'] == 1 and intro['textNodes'] > 0",
                      "require(not intro['overlaps']", 'intro-text-overlap-',
                      'r.left<br.right&&r.right>br.left&&r.top<br.bottom&&r.bottom>br.top'):
            self.assertIn(token,block)
        self.assertLess(block.index('driver.save_screenshot'),block.index('require('))

    def test_intro_lane_is_mobile_only_and_does_not_change_content_or_button(self):
        css=Path('assets/css/neutriverse-sections.css').read_text()
        start=css.index('/* UI-014:')
        block=css[start:css.index('.nv-section-links {',start)]
        for token in ('@media (max-width: 767.98px)',
                      "[data-neutriverse-section='observe'] .nv-section-intro",
                      '[data-about-profile] .about-info-text', 'padding-right: 2.75rem;'):
            self.assertIn(token,block)
        for token in ('#back-to-top', 'display:', 'font-size:', 'position:', 'grid-template'):
            self.assertNotIn(token,block)

    def test_font_failure_diagnostics_preserve_original_ready_wait_and_raise(self):
        source,_=self.helper()
        settle=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='settle')
        helper=ast.get_source_segment(source,settle)
        self.assertIn('document.fonts.ready.then(() => done(true))',helper)
        self.assertNotIn('catch',helper)
        self.assertNotIn('set_script_timeout',helper)
        start=source.index("output / 'scene-failure.png'")
        end=source.index("kind = 'think'",start)
        failure=source[start:end]
        for token in ('fontSetStatus:document.fonts.status','[...document.fonts]',
                      'f.status',"performance.getEntriesByType('resource')",'responseEnd',
                      "output / 'scene-failure.json'",'raise'):
            self.assertIn(token,failure)
