import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (ROOT / "tools" / "check_responsive_accessibility.py").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(encoding="utf-8")
LIGHT_CSS = (ROOT / "assets" / "css" / "ProsperoLight.css").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "pages-deploy.yml").read_text(encoding="utf-8")


class ResponsiveAccessibilityGateTest(unittest.TestCase):
    def test_gate_covers_required_viewports_themes_and_surfaces(self):
        for width in (390, 768, 1024, 1366):
            self.assertIn(f"({width},", SCRIPT)
        self.assertIn('THEMES = ("dark", "light")', SCRIPT)
        for path in ('"/"', '"/think/"', '"/build/"', '"/observe/"', '"/about/"'):
            self.assertIn(path, SCRIPT)

    def test_gate_checks_overflow_reading_focus_contrast_and_motion(self):
        for contract in (
            "bodyScrollWidth",
            'result["width"] <= 740',
            'result["height"] >= minimum_height',
            'result["outlineWidth"] >= 2',
            'result["ratio"] >= 4.5',
            "prefers-reduced-motion: reduce",
        ):
            self.assertIn(contract, SCRIPT)

    def test_shared_css_has_uniform_focus_and_motion_fallbacks(self):
        self.assertIn(":is(a, button, input, select, textarea, [tabindex]):focus-visible", CSS)
        self.assertIn("@media (prefers-reduced-motion: reduce)", CSS)
        self.assertIn("animation: none !important", CSS)
        self.assertIn("transition: none !important", CSS)

    def test_light_theme_uses_accessible_interface_accent(self):
        self.assertIn("--nv-accent: var(--prospero-teal-deep);", LIGHT_CSS)
        self.assertIn("--nv-focus: var(--prospero-teal-deep);", LIGHT_CSS)

    def test_production_workflow_runs_the_gate_after_build(self):
        build = WORKFLOW.index("- name: Build site")
        gate = WORKFLOW.index("- name: Validate responsive accessibility matrix in Chrome")
        upload = WORKFLOW.index("- name: Upload site artifact")
        self.assertLess(build, gate)
        self.assertLess(gate, upload)
        self.assertIn('python tools/check_responsive_accessibility.py "_site${{ steps.pages.outputs.base_path }}"', WORKFLOW)


if __name__ == "__main__":
    unittest.main()
