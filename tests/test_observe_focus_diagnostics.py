"""Actual diagnostic helper wiring; not a browser or visual acceptance test."""
import ast
from pathlib import Path
import unittest


class ObserveFocusDiagnosticsTests(unittest.TestCase):
    def test_helper_collects_public_focus_and_enabled_controls_without_mutation(self):
        source = Path('tools/check_observe_dialog.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'loading_focus_metrics')
        ns = {}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<focus-diagnostic>', 'exec'), ns)
        scripts = []
        class Driver:
            def execute_script(self, script):
                scripts.append(script)
                return {'focusIsLast': False, 'inside': True}
        self.assertEqual(ns['loading_focus_metrics'](Driver()), {'focusIsLast': False, 'inside': True})
        script = scripts[0]
        for token in ('document.activeElement', 'button:not(:disabled)', 'offsetParent',
                      'focusIsLast:', 'requestButtons:', 'planetNodes:'):
            self.assertIn(token, script)
        for forbidden in ('localStorage', 'fetch(', '.focus()', '.disabled=', 'headers'):
            self.assertNotIn(forbidden, script)
        self.assertIn("assert row['loadingAfterReverseTab']['focusIsLast']", source)
