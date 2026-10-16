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

    def test_refresh_validation_uses_one_atomic_dom_sample(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        tree = ast.parse(source)
        sample = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                      and n.name == 'rating_chart_snapshot')
        namespace = {}
        exec(compile(ast.Module(body=[sample], type_ignores=[]), '<rating-snapshot>', 'exec'), namespace)

        class Driver:
            calls = 0
            def execute_script(self, script):
                self.calls += 1
                for value in ('.pgl-chart-hit', '.pgl-chart-label', '.pgl-chart-area',
                              '[data-rating-scope].is-active', '#pgl-rating-summary'):
                    self.assert_selector(value, script)
                return {'hits':['1: 0'], 'labels':['1'], 'area':True,
                        'active':['all'], 'summary':'0 rated works'}
            def assert_selector(self, value, script):
                if value not in script:
                    raise AssertionError(value)

        driver = Driver()
        result = namespace['rating_chart_snapshot'](driver)
        self.assertEqual(driver.calls, 1)
        self.assertEqual(result['active'], ['all'])
        helper = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                      and n.name == 'library_rating_controls')
        verify = next(n for n in helper.body if isinstance(n, ast.FunctionDef) and n.name == 'verify')
        contract = ast.get_source_segment(source, verify)
        self.assertIn('snapshot = rating_chart_snapshot(d)', contract)
        self.assertIn("snapshot['hits'] == expected", contract)
        self.assertIn("snapshot['active'] == [scope]", contract)
        self.assertNotIn('find_elements', contract)
        self.assertNotIn('except', contract)

    def test_tooltips_stay_inside_shell_and_usable_viewport(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        self.assertIn('clientViewport:document.documentElement.clientWidth', source)
        self.assertIn("r['right'] <= geometry['clientViewport']+1", source)
        self.assertIn("r['right'] <= geometry['shell']['right']+1", source)
        for filename in ('assets/pgl/pgl.js', 'assets/pgl/pgl-rating-polish.js'):
            js = Path(filename).read_text()
            self.assertIn('getBoundingClientRect().width', js)
            self.assertIn('clamp(${inset}px,', js)
            self.assertIn('calc(100% - ${inset}px)', js)
