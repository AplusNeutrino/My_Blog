import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class AtlasDialogFocusTest(unittest.TestCase):
    def run_focus(self, source):
        # Execute the actual focus functions, not a copied implementation.
        functions = source[source.index('function setChartControlOpen('):source.index('async function loadAstrologySnapshot(')]
        harness = r'''
const assert = require('node:assert/strict');
const frames = [];
const document = {activeElement:null,body:{classList:{toggle(){}}}};
const control = (id,disabled=false) => ({id,disabled,hidden:false,offsetParent:{},
  focus(){if(!this.disabled)document.activeElement=this;}});
const refresh=control('refresh',true),exportButton=control('export',true);
const date=control('date'),last=control('last'),trigger=control('trigger');
const controls=[refresh,exportButton,date,last];
const panel={hidden:true,focus(){document.activeElement=this;},
 querySelector(){return refresh;},
 querySelectorAll(selector){assert.ok(selector.includes(':disabled'));return controls.filter(c=>!c.disabled);}};
const elements={chartControlPanel:panel,chartControlToggle:trigger};
trigger.setAttribute=()=>{};
const window={requestAnimationFrame(fn){frames.push(fn);}};
trigger.focus(); setChartControlOpen(true); frames.shift()();
assert.equal(document.activeElement,date,'Disabled loading buttons must be skipped');
let prevented=false;
trapChartControlFocus({shiftKey:true,preventDefault(){prevented=true;}});
assert.ok(prevented); assert.equal(document.activeElement,last);
trapChartControlFocus({shiftKey:false,preventDefault(){}});
assert.equal(document.activeElement,date);
setChartControlOpen(false,{restoreFocus:true});
assert.equal(document.activeElement,trigger);
refresh.disabled=false;exportButton.disabled=false;
setChartControlOpen(true);frames.shift()();
assert.equal(document.activeElement,refresh,'Loaded first button stays preferred');
setChartControlOpen(false,{restoreFocus:true});
setChartControlOpen(true);setChartControlOpen(false,{restoreFocus:true});frames.shift()();
assert.equal(document.activeElement,trigger,'Closed panel must not steal focus');
controls.forEach(c=>c.hidden=true);
setChartControlOpen(true);frames.shift()();assert.equal(document.activeElement,panel);
'''
        return subprocess.run(['node', '-e', harness + '\n' + functions],capture_output=True,text=True)

    def test_actual_focus_functions_skip_disabled_and_preserve_boundaries(self):
        result = self.run_focus((ROOT/'occult-atlas-app/app.js').read_text())
        self.assertEqual(result.returncode,0,result.stderr)

    def test_original_first_button_fault_is_rejected(self):
        source=(ROOT/'occult-atlas-app/app.js').read_text().replace(
            'chartControlFocusTargets()[0]',
            'elements.chartControlPanel.querySelector("button, input, [tabindex=\'0\']")')
        result=self.run_focus(source)
        self.assertNotEqual(result.returncode,0)
        self.assertIn('Disabled loading buttons must be skipped',result.stderr)
