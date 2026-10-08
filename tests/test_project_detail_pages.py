from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads(
    (ROOT / "_data" / "neutriverse_projects.yml").read_text(encoding="utf-8")
)["projects"]
BY_ID = {project["id"]: project for project in CATALOG}
LAYOUT = (ROOT / "_layouts" / "neutriverse-project.html").read_text(
    encoding="utf-8"
)
CARDS = (ROOT / "_includes" / "neutriverse-project-list.html").read_text(
    encoding="utf-8"
)
METADATA = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(
    encoding="utf-8"
)


class ProjectDetailPagesTest(unittest.TestCase):
    PROJECTS = {
        "fitzsight": ("FitzSight", "/build/fitzsight/"),
        "akasha-notes": ("Akasha Notes", "/build/akasha-notes/"),
        "toyosatomimis-headphone": (
            "Toyosatomimi's Headphone",
            "/build/toyosatomimis-headphone/",
        ),
        "ravenis": ("Ravenis", "/build/ravenis/"),
        "occult-atlas": ("Occult Atlas", "/build/occult-atlas/"),
        "gate": ("Gate", "/build/gate/"),
        "officespire": ("OfficeSpire", "/build/officespire/"),
    }

    def test_all_catalog_projects_have_canonical_data_driven_pages(self):
        for project_id, (title, permalink) in self.PROJECTS.items():
            with self.subTest(project=project_id):
                page = (
                    ROOT / "build" / project_id / "index.md"
                ).read_text(encoding="utf-8")
                self.assertIn("layout: neutriverse-project", page)
                self.assertIn(f"permalink: {permalink}", page)
                self.assertIn(f"project_id: {project_id}", page)
                self.assertIn(title, page)
                self.assertEqual(BY_ID[project_id]["detail_url"], permalink)

    def test_noindex_project_pages_keep_visibility_boundaries(self):
        for project_id in ("ravenis", "occult-atlas", "gate"):
            page = (ROOT / "build" / project_id / "index.md").read_text(
                encoding="utf-8"
            )
            self.assertIn("robots: noindex,nofollow", page)
            self.assertIn("sitemap: false", page)
        self.assertIn("page.layout == 'neutriverse-project'", METADATA)
        self.assertIn("page.robots", METADATA)
        office = (ROOT / "build" / "officespire" / "index.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("robots:", office)
        self.assertNotIn("sitemap: false", office)

    def test_layout_has_overview_status_actions_logs_and_sources(self):
        for marker in (
            'id="project-overview"',
            'data-project-status-panel',
            'id="project-actions"',
            'id="project-related-posts"',
            'id="project-sources"',
        ):
            self.assertIn(marker, LAYOUT)
        self.assertIn("project.summary", LAYOUT)
        self.assertIn("project.sources", LAYOUT)

    def test_unknown_status_is_explicit_without_invented_state(self):
        for project_id in self.PROJECTS:
            if project_id != "officespire":
                self.assertNotIn("status", BY_ID[project_id])
        self.assertEqual(BY_ID["officespire"]["status"], "implemented_unverified")
        self.assertIn("公开 catalog 尚未单独记录状态", LAYOUT)
        self.assertIn("不根据版本号、页面可达性或文章日期推断", LAYOUT)

    def test_remaining_project_actions_respect_public_boundaries(self):
        self.assertEqual(BY_ID["ravenis"]["links"], {"application": "/ravenis/"})
        self.assertEqual(
            BY_ID["occult-atlas"]["links"], {"application": "/occult-atlas/"}
        )
        self.assertNotIn("links", BY_ID["gate"])
        self.assertEqual(
            BY_ID["officespire"]["links"],
            {
                "repository": "https://github.com/AplusNeutrino/OfficeSpire",
                "documentation": (
                    "https://github.com/AplusNeutrino/OfficeSpire/blob/main/README.md"
                ),
            },
        )
        self.assertNotIn("releases", BY_ID["officespire"])
        for project_id in ("ravenis", "occult-atlas", "gate", "officespire"):
            self.assertNotIn("related_posts", BY_ID[project_id])

    def test_build_cards_prefer_the_unique_detail_pages(self):
        self.assertLess(
            CARDS.index("if project.detail_url"),
            CARDS.index("elsif project.links.application"),
        )
        self.assertEqual(
            {project["detail_url"] for project in CATALOG},
            {permalink for _title, permalink in self.PROJECTS.values()},
        )

    def test_detail_styles_are_mobile_safe_and_theme_token_based(self):
        for token in (
            "var(--nv-surface-1)",
            "var(--nv-surface-2)",
            "var(--nv-text-strong)",
            "var(--nv-border)",
            "var(--nv-focus)",
        ):
            self.assertIn(token, CSS)
        self.assertIn(".nv-project-detail-grid", CSS)
        self.assertRegex(
            CSS,
            re.compile(
                r"@media \(max-width: 767\.98px\).*?"
                r"\.nv-project-detail-grid\s*\{.*?"
                r"grid-template-columns: minmax\(0, 1fr\)",
                re.DOTALL,
            ),
        )


if __name__ == "__main__":
    unittest.main()
