from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads(
    (ROOT / "_data" / "neutriverse_projects.yml").read_text(encoding="utf-8")
)["projects"]
OBSERVE = [project for project in CATALOG if "observe" in project["contexts"]]
INCLUDE = (ROOT / "_includes" / "neutriverse-observe-list.html").read_text(
    encoding="utf-8"
)
LAYOUT = (ROOT / "_layouts" / "neutriverse-section.html").read_text(
    encoding="utf-8"
)
SECTION_DATA = (ROOT / "_data" / "neutriverse_sections.yml").read_text(
    encoding="utf-8"
)
PAGE = (ROOT / "observe" / "index.md").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(
    encoding="utf-8"
)


class ObserveDirectoryTest(unittest.TestCase):
    def test_directory_is_derived_from_the_two_approved_catalog_entities(self):
        self.assertEqual([project["id"] for project in OBSERVE], [
            "ravenis",
            "occult-atlas",
        ])
        self.assertIn("site.data.neutriverse_projects.projects", INCLUDE)
        self.assertIn("project.contexts contains 'observe'", INCLUDE)
        for forbidden in ("MMXProj", "/gate/", "/navi/"):
            self.assertNotIn(forbidden, INCLUDE)

    def test_project_records_and_application_entries_stay_distinct(self):
        expected = {
            "ravenis": ("/build/ravenis/", "/ravenis/"),
            "occult-atlas": ("/build/occult-atlas/", "/occult-atlas/"),
        }
        for project in OBSERVE:
            fact, application = expected[project["id"]]
            self.assertEqual(project["detail_url"], fact)
            self.assertEqual(project["links"]["application"], application)
            self.assertNotEqual(fact, application)
            self.assertNotEqual(fact, "/observe/")
            self.assertNotEqual(application, "/observe/")
        self.assertIn('data-observe-action="project"', INCLUDE)
        self.assertIn('data-observe-action="application"', INCLUDE)

    def test_observe_does_not_keep_a_second_handwritten_project_list(self):
        block = re.search(
            r"  - id: observe\n(?P<body>.*?)(?=\n  - id:|\Z)",
            SECTION_DATA,
            re.DOTALL,
        )
        self.assertIsNotNone(block)
        body = block.group("body")
        self.assertNotIn("    links:", body)
        self.assertIn("routes: [/observe/, /ravenis/, /occult-atlas/, /occult-atlas-app/]", body)
        self.assertIn("neutriverse-observe-list.html", LAYOUT)
        self.assertIn("page.section_id == 'observe'", LAYOUT)

    def test_directory_is_indexable_while_applications_remain_noindex(self):
        self.assertNotIn("robots:", PAGE)
        self.assertNotIn("sitemap: false", PAGE)
        ravenis = (ROOT / "ravenis" / "index.html").read_text(encoding="utf-8")
        occult_layout = (
            ROOT / "_layouts" / "occult-atlas.html"
        ).read_text(encoding="utf-8")
        self.assertIn("robots: noindex,nofollow", ravenis)
        self.assertIn('<meta name="robots" content="noindex, nofollow">', occult_layout)

    def test_cards_explain_noindex_and_have_no_javascript_dependency(self):
        self.assertIn("应用保持 noindex", INCLUDE)
        self.assertIn("href=", INCLUDE)
        self.assertNotIn("<script", INCLUDE)
        self.assertNotIn('href="#"', INCLUDE)

    def test_shared_styles_are_two_column_and_mobile_safe(self):
        for token in (
            "var(--nv-surface-1)",
            "var(--nv-surface-2)",
            "var(--nv-text-strong)",
            "var(--nv-border)",
            "var(--nv-focus)",
        ):
            self.assertIn(token, CSS)
        self.assertIn(".nv-observe-grid", CSS)
        self.assertRegex(
            CSS,
            re.compile(
                r"@media \(max-width: 767\.98px\).*?"
                r"\.nv-observe-grid\s*\{.*?"
                r"grid-template-columns: minmax\(0, 1fr\)",
                re.DOTALL,
            ),
        )


if __name__ == "__main__":
    unittest.main()
