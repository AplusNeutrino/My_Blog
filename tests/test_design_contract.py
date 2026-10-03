import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN = (ROOT / "DESIGN.md").read_text(encoding="utf-8")


class DesignContractTest(unittest.TestCase):
    def test_four_primary_entrances_are_canonical(self):
        for name, description, route in (
            ("THINK", "我如何思考与表达", "/think/"),
            ("BUILD", "我正在制作什么", "/build/"),
            ("OBSERVE", "我持续观察什么", "/observe/"),
            ("ABOUT", "我是谁以及这个站如何生长", "/about/"),
        ):
            with self.subTest(name=name):
                self.assertIn(f"| {name} | {description} | `{route}`", DESIGN)

    def test_legacy_information_architecture_conflicts_are_removed(self):
        self.assertNotIn("Keep Chirpy's current information architecture", DESIGN)
        self.assertNotIn("quiet, unlisted reading room", DESIGN)
        self.assertNotIn("no tab entry, no sitemap entry", DESIGN)
        self.assertIn("replaces the old first-level tab model", DESIGN)

    def test_dual_theme_semantics_and_controller_are_fixed(self):
        for value in (
            "Night and Prospero Light express the same hierarchy, semantics, actions and content",
            "`data-mode`",
            "`data-bs-theme`",
            "`neutriverse-theme-preference`",
            "must not reset filters, scroll position, form values, application state or the current route",
        ):
            with self.subTest(value=value):
                self.assertIn(value, DESIGN)

    def test_required_semantic_tokens_are_defined(self):
        for token in (
            "--nv-canvas",
            "--nv-surface-1",
            "--nv-surface-2",
            "--nv-border",
            "--nv-text",
            "--nv-text-strong",
            "--nv-text-muted",
            "--nv-accent",
            "--nv-signal",
            "--nv-anomaly",
            "--nv-focus",
        ):
            with self.subTest(token=token):
                self.assertIn(f"`{token}`", DESIGN)

    def test_typography_spacing_and_reading_measure_are_defined(self):
        for value in (
            "Long-form body text: approximately 17px",
            "line-height 1.75–1.9",
            "reading measure 700–740px",
            "8px primary rhythm with a 4px micro-step",
            "Essential labels and controls: normally at least 12px",
        ):
            with self.subTest(value=value):
                self.assertIn(value, DESIGN)

    def test_focus_touch_motion_and_responsive_contracts_are_defined(self):
        for value in (
            "2px solid `--nv-focus`",
            "3px offset",
            "44×44px",
            "390, 768, 1024 and 1366px",
            "Page-level horizontal scrolling is prohibited",
            "`prefers-reduced-motion: reduce`",
            "`transition: all` is prohibited",
        ):
            with self.subTest(value=value):
                self.assertIn(value, DESIGN)

    def test_shared_components_cover_required_states(self):
        for component in (
            "Primary entrance",
            "Section header",
            "Record card",
            "Project card",
            "Filter group",
            "Status / tag",
            "Empty / loading / error",
            "Pagination",
            "Utility link",
        ):
            with self.subTest(component=component):
                self.assertIn(f"| {component} |", DESIGN)
        self.assertIn("Links navigate; buttons change state or perform an action", DESIGN)

    def test_special_surface_boundaries_match_route_contract(self):
        self.assertIn("Ravenis is a publicly discoverable OBSERVE interface reached from `/observe/`", DESIGN)
        self.assertIn("Occult Atlas is publicly discoverable from `/observe/`", DESIGN)
        self.assertIn("Gate and NAVI retain their existing URLs and hidden-discovery level", DESIGN)
        self.assertIn("These are ABOUT relationships, not new top-level entrances", DESIGN)


if __name__ == "__main__":
    unittest.main()
