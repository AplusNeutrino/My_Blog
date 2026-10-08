from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
INCLUDE = (ROOT / "_includes" / "neutriverse-observe-app-nav.html").read_text(
    encoding="utf-8"
)
RAVENIS = (ROOT / "ravenis" / "index.html").read_text(encoding="utf-8")
ATLAS = (ROOT / "_layouts" / "occult-atlas.html").read_text(encoding="utf-8")
METADATA = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-observe-shell.css").read_text(
    encoding="utf-8"
)


class ObserveAppNavigationTest(unittest.TestCase):
    def test_both_apps_use_the_same_catalog_driven_navigation(self):
        self.assertIn(
            "{% include neutriverse-observe-app-nav.html current='ravenis' %}",
            RAVENIS,
        )
        self.assertIn(
            "{% include neutriverse-observe-app-nav.html current='occult-atlas' %}",
            ATLAS,
        )
        self.assertIn("site.data.neutriverse_projects.projects", INCLUDE)
        self.assertIn("project.contexts contains 'observe'", INCLUDE)
        self.assertIn("project.links.application", INCLUDE)
        self.assertIn("nv_observe_project.detail_url", INCLUDE)

    def test_navigation_has_real_wayfinding_and_no_hidden_tools(self):
        self.assertIn("{{ '/' | relative_url }}", INCLUDE)
        self.assertIn("{{ '/observe/' | relative_url }}", INCLUDE)
        self.assertIn('aria-current="page"', INCLUDE)
        self.assertIn("data-observe-project-link", INCLUDE)
        self.assertNotIn('href="#"', INCLUDE)
        self.assertNotIn("<script", INCLUDE)
        for forbidden in ("Gate", "NAVI", "MMXProj", "/gate/", "/navi/"):
            self.assertNotIn(forbidden, INCLUDE)

    def test_shared_styles_load_after_each_application_stylesheet(self):
        shared = "neutriverse-observe-shell.css"
        self.assertIn(shared, METADATA)
        self.assertIn(shared, ATLAS)
        self.assertLess(ATLAS.index("occult-atlas-app/styles.css"), ATLAS.index(shared))
        self.assertIn(".ravenis-app-shell > .nv-observe-app-nav", CSS)
        self.assertIn(".nv-observe-app-frame > .astro-home", CSS)
        self.assertIn("min-height: 44px", CSS)
        self.assertIn("@media (max-width: 700px)", CSS)
        self.assertIn("@media (prefers-reduced-motion: reduce)", CSS)

    def test_application_contracts_and_visibility_stay_in_place(self):
        for identifier in (
            'id="ravenis-day-select"',
            'id="ravenis-slot-nav"',
            'id="ravenis-search"',
        ):
            self.assertIn(identifier, RAVENIS)
        for identifier in (
            'id="chartControlToggle"',
            'id="chartControlPanel"',
            'id="astroChart"',
        ):
            self.assertIn(identifier, ATLAS)
        self.assertIn("robots: noindex,nofollow", RAVENIS)
        self.assertIn('<meta name="robots" content="noindex, nofollow">', ATLAS)
        self.assertIn("window.OCCULT_ATLAS_APP_BASE", ATLAS)
        self.assertIn("occult-atlas-app/app.js", ATLAS)
        self.assertIn("assets/js/ravenis.js", RAVENIS)


if __name__ == "__main__":
    unittest.main()
