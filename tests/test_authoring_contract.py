import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "check_authoring.py"
GUIDE = (ROOT / "docs" / "neutriverse-authoring-guide.md").read_text(encoding="utf-8")
POST_TEMPLATE = (ROOT / "docs" / "templates" / "neutriverse-post.md").read_text(encoding="utf-8")
FRAGMENT_TEMPLATE = (ROOT / "docs" / "templates" / "neutriverse-fragment.yml").read_text(encoding="utf-8")
PROJECT_TEMPLATE = json.loads((ROOT / "docs" / "templates" / "neutriverse-project.json").read_text(encoding="utf-8"))
WORKFLOW = (ROOT / ".github" / "workflows" / "pages-deploy.yml").read_text(encoding="utf-8")

SPEC = importlib.util.spec_from_file_location("check_authoring", SCRIPT)
authoring = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(authoring)


class AuthoringContractTest(unittest.TestCase):
    def test_current_authoring_sources_pass_with_expected_counts(self):
        result = subprocess.run(
            ["python", str(SCRIPT)], cwd=ROOT, check=False, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            json.loads(result.stdout),
            {"posts": 44, "fragments": 5, "projects": 7, "passed": True, "errors": 0},
        )

    def test_guide_routes_each_content_kind_to_one_authoritative_source(self):
        for value in (
            "_posts/",
            "_tabs/thoughts.md",
            "_data/neutriverse_projects.yml",
            "type: note",
            "type: essay",
            "固定为 `fragment`",
            "Project Log 是文章与项目的次级关系，不是第四种 Type",
        ):
            self.assertIn(value, GUIDE)
        self.assertIn("categories` 是 ADR 0001 定义的只读兼容层", GUIDE)
        self.assertIn("新文章不强制填写", GUIDE)

    def test_templates_require_explicit_values_and_do_not_invent_project_state(self):
        self.assertIn('type: "<note-or-essay>"', POST_TEMPLATE)
        self.assertIn('topic: "<computation-humanity-otaku-or-arts>"', POST_TEMPLATE)
        self.assertIn('"<canonical string tag>"', POST_TEMPLATE)
        self.assertIn("# categories:", POST_TEMPLATE)
        self.assertIn("type: fragment", FRAGMENT_TEMPLATE)
        self.assertIn('tags: ["<canonical string tag>"]', FRAGMENT_TEMPLATE)
        self.assertEqual(PROJECT_TEMPLATE["contexts"], ["build"])
        for optional in ("status", "links", "related_posts", "releases"):
            self.assertNotIn(optional, PROJECT_TEMPLATE)
        self.assertIn("<", json.dumps(PROJECT_TEMPLATE))

    def test_unquoted_yaml_implicit_tag_is_rejected_but_quoted_tag_is_string(self):
        values, errors = authoring.validate_string_list("tags: [8086, Addressing Modes]", "tags", True)
        self.assertEqual(values, ["Addressing Modes"])
        self.assertTrue(any("must be quoted" in item for item in errors))
        values, errors = authoring.validate_string_list('tags: ["8086", Addressing Modes]', "tags", True)
        self.assertEqual(values, ["8086", "Addressing Modes"])
        self.assertEqual(errors, [])

    def test_post_validator_rejects_fragment_type_and_unknown_series(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "2026-10-11-test.md"
            path.write_text(
                "---\ntitle: Test\ndate: 2026-10-11\ntype: fragment\ntopic: computation\n"
                "series: Invented Series\ntags: [Test]\n---\nBody\n",
                encoding="utf-8",
            )
            errors = authoring.validate_post(path, {"Database Systems"})
        self.assertTrue(any("type must be note or essay" in item for item in errors))
        self.assertTrue(any("series is not defined" in item for item in errors))

    def test_project_validator_reports_malformed_related_posts_without_crashing(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "_data").mkdir()
            (root / "build" / "example").mkdir(parents=True)
            (root / "build" / "example" / "index.md").write_text(
                "---\nproject_id: example\npermalink: /build/example/\n---\n",
                encoding="utf-8",
            )
            catalog = {
                "schema_version": 1,
                "projects": [
                    {
                        "id": "example",
                        "name": "Example",
                        "summary": "Example summary",
                        "contexts": ["build"],
                        "visibility": "listed",
                        "sources": [{"kind": "site", "path": "build/example/index.md"}],
                        "related_posts": {},
                        "detail_url": "/build/example/",
                    }
                ],
            }
            (root / "_data" / "neutriverse_projects.yml").write_text(
                json.dumps(catalog), encoding="utf-8"
            )
            count, errors = authoring.validate_projects(root)
        self.assertEqual(count, 1)
        self.assertTrue(any("related_posts must be omitted" in item for item in errors))

    def test_workflow_runs_authoring_gate_before_jekyll(self):
        regression = WORKFLOW.index("- name: Run regression tests")
        authoring_gate = WORKFLOW.index("- name: Validate authoring sources")
        build = WORKFLOW.index("- name: Build site")
        self.assertLess(regression, authoring_gate)
        self.assertLess(authoring_gate, build)
        self.assertIn("python tools/check_authoring.py", WORKFLOW)


if __name__ == "__main__":
    unittest.main()
