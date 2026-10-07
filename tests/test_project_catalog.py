from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
CATALOG_TEXT = (ROOT / "_data" / "neutriverse_projects.yml").read_text(encoding="utf-8")
CATALOG = json.loads(CATALOG_TEXT)
PROJECTS = CATALOG["projects"]
LAYOUT = (ROOT / "_layouts" / "neutriverse-project.html").read_text(encoding="utf-8")


class ProjectCatalogTest(unittest.TestCase):
    def test_approved_projects_have_unique_stable_ids(self):
        expected = [
            "fitzsight",
            "akasha-notes",
            "toyosatomimis-headphone",
            "ravenis",
            "occult-atlas",
            "gate",
            "officespire",
        ]
        ids = [project["id"] for project in PROJECTS]
        self.assertEqual(ids, expected)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item) for item in ids))
        self.assertNotIn("mmxproj", CATALOG_TEXT.lower())

    def test_required_fields_and_sources_are_present(self):
        for project in PROJECTS:
            with self.subTest(project=project["id"]):
                self.assertTrue(project["name"].strip())
                self.assertTrue(project["summary"].strip())
                self.assertIn("build", project["contexts"])
                self.assertIn(
                    project["visibility"],
                    {"listed", "listed_noindex", "unlisted_noindex"},
                )
                self.assertTrue(project["sources"])
                for source in project["sources"]:
                    if source["kind"] == "site":
                        self.assertTrue((ROOT / source["path"]).is_file())
                    else:
                        self.assertEqual(source["kind"], "external")
                        self.assertTrue(source["url"].startswith("https://github.com/"))

    def test_cross_context_and_visibility_boundaries_are_explicit(self):
        by_id = {project["id"]: project for project in PROJECTS}
        self.assertEqual(by_id["ravenis"]["contexts"], ["build", "observe"])
        self.assertEqual(by_id["occult-atlas"]["contexts"], ["build", "observe"])
        self.assertEqual(by_id["ravenis"]["visibility"], "listed_noindex")
        self.assertEqual(by_id["occult-atlas"]["visibility"], "listed_noindex")
        self.assertEqual(by_id["gate"]["visibility"], "unlisted_noindex")
        self.assertNotIn("links", by_id["gate"])

    def test_optional_status_is_not_invented(self):
        status_projects = [project["id"] for project in PROJECTS if "status" in project]
        self.assertEqual(status_projects, ["officespire"])
        self.assertEqual(
            PROJECTS[-1]["status"],
            "implemented_unverified",
        )

    def test_no_project_requires_a_release(self):
        self.assertTrue(all("releases" not in project for project in PROJECTS))
        self.assertIn(
            "{% if project.releases and project.releases.size > 0 %}",
            LAYOUT,
        )

    def test_links_and_related_posts_are_optional_and_guarded(self):
        self.assertIn("{% if project.links %}", LAYOUT)
        self.assertIn(
            "{% if project.related_posts and project.related_posts.size > 0 %}",
            LAYOUT,
        )
        self.assertIn("{% if project.status %}", LAYOUT)
        for project in PROJECTS:
            for post in project.get("related_posts", []):
                self.assertTrue((ROOT / post["source_path"]).is_file())
                self.assertTrue(post["url"].startswith("/posts/"))

    def test_project_template_uses_stable_id_and_has_unknown_fallback(self):
        self.assertIn("where: 'id', page.project_id", LAYOUT)
        self.assertIn("data-project-id=", LAYOUT)
        self.assertIn("Project record unavailable", LAYOUT)
        self.assertIn("'/build/' | relative_url", LAYOUT)


if __name__ == "__main__":
    unittest.main()
