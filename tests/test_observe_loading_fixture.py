"""Execute fixture JS on native-like properties; not browser acceptance."""
import ast
from pathlib import Path
import subprocess
import unittest


class ObserveLoadingFixtureTests(unittest.TestCase):
    def scripts(self):
        tree = ast.parse(Path('tools/check_observe_dialog.py').read_text())
        scripts = []
        class Driver:
            def execute_script(self, script):
                scripts.append(script)
        for name in ('pin_loading_controls', 'restore_loading_controls'):
            node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
            ns = {}
            exec(compile(ast.Module(body=[node], type_ignores=[]), '<loading-fixture>', 'exec'), ns)
            ns[name](Driver())
        return scripts

    def run_fixture(self, broken=False):
        pin, restore = self.scripts()
        if broken:
            pin = "for(const n of Object.values(nodes))n.disabled=true;"
        program = r'''
const assert=require('node:assert/strict');
const proto={get disabled(){return !!this.attributeDisabled},
 set disabled(value){this.attributeDisabled=!!value}};
const nodes={refreshAstroButton:Object.create(proto),exportChartButton:Object.create(proto)};
const document={getElementById(id){return nodes[id]}};
nodes.refreshAstroButton.disabled=true;nodes.exportChartButton.disabled=true;
''' + pin + r'''
// Same writes as request completion; do not change the fixture's disabled DOM state.
nodes.refreshAstroButton.disabled=false;nodes.exportChartButton.disabled=false;
assert.equal(nodes.refreshAstroButton.disabled,true,'Fixture precondition must survive callbacks');
assert.equal(nodes.refreshAstroButton.attributeDisabled,true);
''' + restore + r'''
assert.equal(nodes.refreshAstroButton.disabled,false,'Restore latest requested state');
assert.equal(nodes.exportChartButton.disabled,false);
for(const n of Object.values(nodes)){
 assert.equal(Object.hasOwn(n,'disabled'),false);
 assert.equal(Object.hasOwn(n,'__uiDisabledFixture'),false);
}
// No callback: restore the originally requested state as well.
nodes.refreshAstroButton.disabled=false;nodes.exportChartButton.disabled=true;
''' + pin + restore + r'''
assert.equal(nodes.refreshAstroButton.disabled,false);
assert.equal(nodes.exportChartButton.disabled,true);
'''
        return subprocess.run(['node', '-e', program], capture_output=True, text=True)

    def test_async_requests_stay_isolated_and_latest_values_are_restored(self):
        result = self.run_fixture()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_old_one_off_disable_is_rejected(self):
        result = self.run_fixture(broken=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Fixture precondition must survive callbacks', result.stderr)
