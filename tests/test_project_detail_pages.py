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
CSS = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(
    encoding="utf-8"
)


class ProjectDetailPagesTest(unittest.TestCase):
    FIRST_GROUP = {
        "fitzsight": ("FitzSight", "/build/fitzsight/"),
        "akasha-notes": ("Akasha Notes", "/build/akasha-notes/"),
        "toyosatomimis-headphone": (
            "Toyosatomimi's Headphone",
            "/build/toyosatomimis-headphone/",
        ),
    }

    def test_first_group_has_canonical_data_driven_pages(self):
        for project_id, (title, permalink) in self.FIRST_GROUP.items():
            with self.subTest(project=project_id):
                page = (
                    ROOT / "build" / project_id / "index.md"
                ).read_text(encoding="utf-8")
                self.assertIn("layout: neutriverse-project", page)
                self.assertIn(f"permalink: {permalink}", page)
                self.assertIn(f"project_id: {project_id}", page)
                self.assertIn(title, page)
                self.assertEqual(BY_ID[project_id]["detail_url"], permalink)

    def test_remaining_projects_are_left_for_t24(self):
        remaining = {"ravenis", "occult-atlas", "gate", "officespire"}
        self.assertTrue(all("detail_url" not in BY_ID[item] for item in remaining))
        self.assertTrue(
            all(not (ROOT / "build" / item / "index.md").exists() for item in remaining)
        )

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
        for project_id in self.FIRST_GROUP:
            self.assertNotIn("status", BY_ID[project_id])
        self.assertIn("公开 catalog 尚未单独记录状态", LAYOUT)
        self.assertIn("不根据版本号、页面可达性或文章日期推断", LAYOUT)

    def test_real_actions_and_related_posts_remain_separate(self):
        self.assertEqual(
            BY_ID["fitzsight"]["links"],
            {
                "application": "/projfitzgerald/",
                "repository": "https://github.com/AplusNeutrino/FitzSight",
            },
        )
        for project_id in ("akasha-notes", "toyosatomimis-headphone"):
            project = BY_ID[project_id]
            self.assertTrue(project["links"]["repository"].startswith("https://github.com/"))
            self.assertEqual(len(project["related_posts"]), 1)
            self.assertTrue(project["related_posts"][0]["url"].startswith("/posts/"))
        self.assertIn('data-project-action="application"', LAYOUT)
        self.assertIn('data-project-action="repository"', LAYOUT)

    def test_build_cards_prefer_detail_without_replacing_old_routes(self):
        self.assertLess(
            CARDS.index("if project.detail_url"),
            CARDS.index("elsif project.links.application"),
        )
        for project_id, (_title, permalink) in self.FIRST_GROUP.items():
            self.assertEqual(BY_ID[project_id]["detail_url"], permalink)

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
