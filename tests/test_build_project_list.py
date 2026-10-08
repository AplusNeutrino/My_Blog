from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads(
    (ROOT / "_data" / "neutriverse_projects.yml").read_text(encoding="utf-8")
)["projects"]
INCLUDE = (ROOT / "_includes" / "neutriverse-project-list.html").read_text(
    encoding="utf-8"
)
LAYOUT = (ROOT / "_layouts" / "neutriverse-section.html").read_text(
    encoding="utf-8"
)
SCRIPT = (ROOT / "assets" / "js" / "neutriverse-project-filters.js").read_text(
    encoding="utf-8"
)
PAGE = (ROOT / "build" / "index.md").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(
    encoding="utf-8"
)


class BuildProjectListTest(unittest.TestCase):
    def test_build_renders_only_the_seven_approved_catalog_projects(self):
        self.assertEqual(
            [project["id"] for project in CATALOG],
            [
                "fitzsight",
                "akasha-notes",
                "toyosatomimis-headphone",
                "ravenis",
                "occult-atlas",
                "gate",
                "officespire",
            ],
        )
        self.assertIn("site.data.neutriverse_projects.projects", INCLUDE)
        self.assertIn("for project in project_catalog", INCLUDE)
        self.assertNotIn("MMXProj", INCLUDE + PAGE)

    def test_each_authorized_card_resolves_to_a_real_current_action(self):
        expected = {
            "fitzsight": "/build/fitzsight/",
            "akasha-notes": "/build/akasha-notes/",
            "toyosatomimis-headphone": "/build/toyosatomimis-headphone/",
            "ravenis": "/ravenis/",
            "occult-atlas": "/occult-atlas/",
            "officespire": "https://github.com/AplusNeutrino/OfficeSpire",
        }
        resolved = {}
        for project in CATALOG:
            links = project.get("links", {})
            if project.get("detail_url"):
                resolved[project["id"]] = project["detail_url"]
            elif links.get("application"):
                resolved[project["id"]] = links["application"]
            elif project.get("related_posts"):
                resolved[project["id"]] = project["related_posts"][0]["url"]
            elif links.get("repository"):
                resolved[project["id"]] = links["repository"]
        self.assertEqual(resolved, expected)

    def test_gate_is_visible_as_a_record_without_exposing_its_tool_route(self):
        gate = next(project for project in CATALOG if project["id"] == "gate")
        self.assertEqual(gate["visibility"], "unlisted_noindex")
        self.assertNotIn("links", gate)
        self.assertNotIn("/gate/", INCLUDE)
        self.assertIn("工具入口保持未公开", INCLUDE)

    def test_status_filter_uses_only_catalog_status_and_unspecified(self):
        known = [project["status"] for project in CATALOG if project.get("status")]
        unspecified = [project for project in CATALOG if not project.get("status")]
        self.assertEqual(known, ["implemented_unverified"])
        self.assertEqual(len(unspecified), 6)
        self.assertIn("map: 'status' | compact | uniq | sort", INCLUDE)
        self.assertIn("data-project-filter=\"unspecified\"", INCLUDE)
        self.assertNotIn("active", INCLUDE.lower())
        self.assertNotIn("complete", INCLUDE.lower())

    def test_filter_is_progressive_and_url_state_is_shareable(self):
        self.assertIn("data-project-status=", INCLUDE)
        self.assertIn("catalog.dataset.projectFilterReady", SCRIPT)
        self.assertIn("url.searchParams.set('status', status)", SCRIPT)
        self.assertIn("window.addEventListener('popstate'", SCRIPT)
        self.assertIn("window.history.replaceState", SCRIPT)
        self.assertNotIn("display: none", INCLUDE)

    def test_build_layout_uses_catalog_instead_of_legacy_three_link_block(self):
        self.assertIn("neutriverse-project-list.html", LAYOUT)
        self.assertIn("neutriverse-project-filters.js", LAYOUT)
        self.assertIn("unless page.section_id == 'build'", LAYOUT)
        self.assertIn("七个项目实体", PAGE)

    def test_mobile_and_theme_styles_use_shared_tokens(self):
        for token in (
            "var(--nv-surface-1)",
            "var(--nv-surface-2)",
            "var(--nv-text-strong)",
            "var(--nv-border)",
            "var(--nv-focus)",
        ):
            self.assertIn(token, CSS)
        self.assertIn(".nv-project-grid", CSS)
        self.assertIn("@media (max-width: 767.98px)", CSS)


if __name__ == "__main__":
    unittest.main()
