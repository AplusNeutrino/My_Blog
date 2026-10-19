import importlib.util
import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('like_gate', ROOT / 'tools/check_like_scripts.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class LikeCompressionTest(unittest.TestCase):
    def script(self):
        source = (ROOT / '_includes/post-like.html').read_text(encoding='utf-8')
        return re.search(r'<script>(.*?)</script>', source, re.S).group(1)

    def test_folded_script_parses_and_initializes_five_independent_controls(self):
        folded = ' '.join(self.script().split())
        gate.validate('<script>' + folded + '</script>', 1)
        harness = r'''
const vm = require('node:vm');
const assert = require('node:assert/strict');
const values = new Map();
const roots = Array.from({length:5}, (_,i) => {
  const button = {attrs:{},classList:{add(){}},setAttribute(k,v){this.attrs[k]=v},
    addEventListener(k,v){this[k]=v}};
  const count = {textContent:'...'};
  return {dataset:{likeKey:'/thoughts/fragment-'+(i+1)},button,count,
    querySelector(s){return s==='.post-like-button'?button:count}};
});
function load(){
  const context = {window:{location:{pathname:'/thoughts/'}},
    document:{readyState:'complete',querySelectorAll:()=>roots},
    localStorage:{getItem:k=>values.get(k)||null,setItem:(k,v)=>values.set(k,v)}};
  vm.runInNewContext(SOURCE, context);
}
(async()=>{
  load();
  assert.deepEqual(roots.map(r=>r.count.textContent),['0','0','0','0','0']);
  await roots[0].button.click();
  await roots[0].button.click();
  assert.equal(roots[0].count.textContent,'1');
  assert.equal(roots[0].button.attrs['aria-pressed'],'true');
  assert.equal(roots[1].count.textContent,'0');
  assert.equal(roots[0].button.disabled,false);
  load();
  assert.equal(roots[0].count.textContent,'1');
  assert.equal(roots[0].button.attrs['aria-pressed'],'true');
})().catch(e=>{console.error(e);process.exitCode=1});
'''
        result = subprocess.run(['node', '-e', 'const SOURCE = ' + json.dumps(folded) + ';' + harness],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_gate_rejects_the_actual_swallowed_tail_regression(self):
        broken = self.script().replace('/* A like', '// A like').replace('new total. */', 'new total.')
        with self.assertRaisesRegex(AssertionError, 'Compressed like script'):
            gate.validate('<script>' + ' '.join(broken.split()) + '</script>', 1)

    def test_gate_requires_all_five_rendered_scripts(self):
        with self.assertRaisesRegex(AssertionError, 'Expected 5'):
            gate.validate('<script>' + self.script() + '</script>', 5)
