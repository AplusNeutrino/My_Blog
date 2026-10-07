import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SidebarKeyboardTest(unittest.TestCase):
    @unittest.skipUnless(shutil.which("node"), "Node required for controller behavior checks")
    def test_collapse_focus_state_and_breakpoint_recovery(self):
        hook = (ROOT / "_includes/metadata-hook.html").read_text(encoding="utf-8")
        scripts = re.findall(r"<script>(.*?)</script>", hook, re.S)
        controller = next(s for s in scripts if "neutriverse-sidebar-collapsed" in s)
        controller = re.sub(r"const pageLayout = .*?;", "const pageLayout = 'home';", controller)
        # Run the actual controller with a minimal DOM boundary; this verifies
        # state/focus effects, while viewport layout still needs browser evidence.
        harness = r"""
const assert = require('node:assert/strict');
const vm = require('node:vm');
class Element {
  constructor(id) {
    this.id = id; this.attrs = {}; this.events = {}; this.inert = false;
    this.classes = new Set(); this.offsetWidth = 44;
    this.classList = {
      toggle: (k, on) => on ? this.classes.add(k) : this.classes.delete(k),
      add: (...ks) => ks.forEach(k => this.classes.add(k)),
      remove: (...ks) => ks.forEach(k => this.classes.delete(k))
    };
  }
  setAttribute(k, v) { this.attrs[k] = v; }
  removeAttribute(k) { delete this.attrs[k]; }
  addEventListener(k, fn) { this.events[k] = fn; }
  querySelector() { return null; }
  focus() { document.activeElement = this; }
  fire(k, key) {
    let prevented = false;
    this.events[k]({key, preventDefault() { prevented = true; }});
    return prevented;
  }
}
const sidebar = new Element('sidebar'), avatar = new Element('avatar');
const body = new Element('body'), events = {}, stored = new Map();
let recall, onResize;
body.appendChild = e => { recall = e; };
const media = {matches: true, addEventListener: (name, fn) => { onResize = fn; }};
global.document = {
  body, activeElement: null,
  getElementById: id => ({sidebar, avatar})[id],
  querySelector: () => recall,
  createElement: () => new Element('recall'),
  addEventListener: (name, fn) => { events[name] = fn; }
};
global.localStorage = {getItem: k => stored.get(k), setItem: (k,v) => stored.set(k,v)};
global.window = {
  matchMedia: () => media, addEventListener() {}, setTimeout: fn => fn()
};
vm.runInThisContext(CONTROLLER);
events.DOMContentLoaded();
assert.equal(sidebar.inert, false);
assert.equal(recall.hidden, true);
assert.equal(avatar.attrs.role, 'button');
assert.equal(avatar.attrs['aria-expanded'], 'true');
assert.equal(avatar.fire('keydown', ' '), true);
assert.equal(sidebar.inert, true);
assert.equal(sidebar.attrs['aria-hidden'], 'true');
assert.equal(recall.hidden, false);
assert.equal(document.activeElement, recall);
assert.equal(recall.attrs['aria-expanded'], 'false');
assert.equal(stored.get('neutriverse-sidebar-collapsed'), 'true');
recall.fire('click');
assert.equal(sidebar.inert, false);
assert.equal(sidebar.attrs['aria-hidden'], undefined);
assert.equal(document.activeElement, avatar);
assert.equal(recall.hidden, true);
assert.equal(avatar.attrs['aria-expanded'], 'true');
assert.equal(sidebar.fire('keydown', 'Escape'), true);
assert.equal(document.activeElement, recall);
assert.equal(sidebar.inert, true);
// Crossing into the native mobile shell must not leave its sidebar inert.
media.matches = false; onResize();
assert.equal(sidebar.inert, false);
assert.equal(recall.hidden, true);
assert.equal(avatar.attrs.role, undefined);
assert.equal(avatar.attrs['aria-expanded'], undefined);
assert.equal(avatar.attrs['aria-label'], '返回 Neutriverse 首页');
assert.equal(avatar.fire('keydown', ' '), false);
console.log('sidebar controller behavior passed');
""".replace("CONTROLLER", json.dumps(controller))
        result = subprocess.run(["node"], input=harness, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("behavior passed", result.stdout)

    def test_hidden_recall_is_not_overridden_by_grid_display(self):
        css = (ROOT / "assets/css/neutriverse-sections.css").read_text(encoding="utf-8")
        rule = re.search(r"\.site-sidebar-recall\[hidden\]\s*\{([^}]+)\}", css).group(1)
        self.assertIn("display: none !important", rule)


    def test_mobile_sidebar_controller_contracts(self):
        script = (ROOT / "assets/js/neutriverse-navigation.js").read_text(encoding="utf-8")
        self.assertIn("aria-controls', 'sidebar", script)
        self.assertIn("aria-expanded', String(isOpen)", script)
        self.assertIn("document.body.hasAttribute('sidebar-display')", script)
        self.assertIn("new MutationObserver(syncMobileSidebar)", script)
        self.assertIn("event.key === 'Escape'", script)
        self.assertIn("mobileFocusable()[0]?.focus()", script)
        self.assertIn("mobileTrigger.focus()", script)
        self.assertIn("event.shiftKey && document.activeElement === first", script)
        self.assertIn("!mobileQuery.matches", script)
        self.assertIn("mobileTrigger.click()", script)

    def test_mobile_sidebar_touch_targets_and_containment(self):
        css = (ROOT / "assets/css/neutriverse-sections.css").read_text(encoding="utf-8")
        trigger_rule = re.search(r"#sidebar-trigger\s*\{([^}]+)\}", css).group(1)
        self.assertIn("min-width: 2.75rem", trigger_rule)
        self.assertIn("min-height: 2.75rem", trigger_rule)
        mobile_rule = re.search(
            r"@media \(max-width: 849px\)\s*\{(.*?)\n\}", css, re.S
        ).group(1)
        self.assertIn("overflow-y: auto", mobile_rule)
        self.assertIn("overscroll-behavior: contain", mobile_rule)
        self.assertIn("min-height: 2.75rem", mobile_rule)

if __name__ == "__main__":
    unittest.main()
