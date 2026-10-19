"""Execute the actual audit guard, not browser/visual acceptance."""
import ast
from pathlib import Path
import unittest


class ObserveHistoryAuditTests(unittest.TestCase):
    def setUp(self):
        self.source = Path('tools/check_observe_history.py').read_text()
        node = next(n for n in ast.parse(self.source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'assert_ready')
        ns = {}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<history-guard>', 'exec'), ns)
        self.guard = ns['assert_ready']
        self.data = dict(stateHidden=True, state=None, disabled=[False]*4,
                         nodes=10, planetRows=14, title='历史星盘 · Placidus',
                         status='2020/01/01 12:00 · Swiss Ephemeris',
                         date='2020-01-01T12:00', label='UI-A12c CHECK')

    def test_actual_guard_accepts_completed_exact_history_only(self):
        self.guard(self.data, True)
        for changes in ({'stateHidden':False,'state':'loading'},
                        {'stateHidden':False,'state':'error'},
                        {'disabled':[False,False,True,False]},
                        {'nodes':0}, {'planetRows':0},
                        {'title':'本地实时星盘 · Placidus'},
                        {'status':'2026/10/19 14:00 · Swiss Ephemeris'},
                        {'date':'2021-01-01T12:00'}):
            with self.subTest(changes=changes), self.assertRaises(AssertionError):
                self.guard(dict(self.data, **changes), True)

    def test_return_now_rejects_stale_history_or_uncleared_label(self):
        current = dict(self.data, title='本地实时星盘 · Placidus', label='')
        self.guard(current)
        for changes in ({'title':'历史星盘 · Placidus'}, {'label':'UI-A12c CHECK'}):
            with self.assertRaises(AssertionError):
                self.guard(dict(current, **changes))

    def test_no_service_fixture_and_failure_is_not_silently_skipped(self):
        for forbidden in ('window.fetch =', 'Network.setRequestInterception',
                          'pin_loading_controls(', 'localStorage.clear', '.disabled ='):
            self.assertNotIn(forbidden, self.source)
        self.assertIn("'Input.dispatchTouchEvent'", self.source)
        self.assertIn("'type':'touchStart'", self.source)
        self.assertIn("'type':'touchEnd'", self.source)
        self.assertIn("row['failure'] = snapshot(driver)\n                        raise", self.source)
        self.assertIn("'2020/01/01 12:00' in data['status']", self.source)

    def test_workflow_preserves_old_gates_and_separate_evidence(self):
        workflow = Path('.github/workflows/pages-deploy.yml').read_text()
        self.assertEqual(workflow.count('run: python tools/check_observe_history.py '), 2)
        for name in ('neutriverse-observe-history-', 'neutriverse-live-observe-history-',
                     'check_observe_dialog.py', 'check_atlas_planet_icons.py',
                     'check_think_build_visual.py', 'content_restructure_baseline.py'):
            self.assertIn(name, workflow)
