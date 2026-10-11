import json
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "docs" / "neutriverse-restructure-baseline.json"
ACCEPTANCE = (ROOT / "docs" / "neutriverse-restructure-acceptance.md").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "pages-deploy.yml").read_text(encoding="utf-8")


class RestructureAcceptanceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        cls.temporary = tempfile.TemporaryDirectory()
        cls.current_path = Path(cls.temporary.name) / "current.json"
        cls.result = subprocess.run(
            [
                "python",
                str(ROOT / "tools" / "content_restructure_baseline.py"),
                "--output",
                str(cls.current_path),
                "--check-against",
                str(BASELINE_PATH),
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        cls.current = json.loads(cls.current_path.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def test_all_protected_content_and_visibility_match_t01(self):
        self.assertEqual(self.result.returncode, 0, self.result.stderr)
        self.assertEqual(
            self.current["protection_check"],
            {"baseline": str(BASELINE_PATH), "passed": True, "errors": []},
        )
        self.assertEqual(self.current["counts"]["posts"], 44)
        self.assertEqual(self.current["counts"]["fragments"], 5)
        self.assertEqual(self.current["counts"]["hidden_posts"], 5)
        self.assertEqual(self.current["counts"]["types"], {"essay": 5, "fragment": 5, "note": 39})
        self.assertEqual(
            self.current["counts"]["topics"],
            {"arts": 1, "computation": 38, "humanity": 6, "otaku": 4},
        )

    def test_only_the_two_t05_tag_edits_change_original_post_files(self):
        old = {item["path"]: item for item in self.baseline["posts"]}
        new = {item["path"]: item for item in self.current["posts"]}
        self.assertEqual(set(new), set(old))
        raw_changes = {path for path in old if old[path]["raw_sha256"] != new[path]["raw_sha256"]}
        expected = {
            "_posts/2025-05-07-计组-06.md": (
                ["Bus", "I/O", "DMA", "Interrupts"],
                ["System Bus", "I/O", "DMA", "Interrupts"],
            ),
            "_posts/2026-05-24-neutriverse-site-changelog.md": (
                ["Neutriverse", "Changelog", "Jekyll"],
                ["Neutriverse", "Jekyll"],
            ),
        }
        self.assertEqual(raw_changes, set(expected))
        stable_fields = (
            "title",
            "body_sha256_lf",
            "body_bytes_utf8_lf",
            "protected_url_metadata",
            "source_url_candidate",
            "type",
            "topic",
            "series",
            "categories",
            "hidden",
            "published",
            "sitemap",
            "robots",
        )
        for path in old:
            for field in stable_fields:
                self.assertEqual(old[path].get(field), new[path].get(field), f"{path}: {field}")
        for path, (old_tags, new_tags) in expected.items():
            self.assertEqual(old[path]["tags"], old_tags)
            self.assertEqual(new[path]["tags"], new_tags)

    def test_original_fragments_are_exactly_preserved(self):
        stable_fields = ("source", "source_index", "date", "text_sha256", "type", "topic", "tags", "hidden")
        old = [{field: item.get(field) for field in stable_fields} for item in self.baseline["fragments"]]
        new = [{field: item.get(field) for field in stable_fields} for item in self.current["fragments"]]
        self.assertEqual(new, old)

    def test_production_workflow_runs_frozen_baseline_before_build(self):
        install = WORKFLOW.index("python -m pip install boto3 PyYAML selenium")
        regression = WORKFLOW.index("- name: Run regression tests")
        baseline = WORKFLOW.index("- name: Validate protected restructure baseline")
        authoring = WORKFLOW.index("- name: Validate authoring sources")
        build = WORKFLOW.index("- name: Build site")
        self.assertLess(install, regression)
        self.assertLess(regression, baseline)
        self.assertLess(baseline, authoring)
        self.assertLess(authoring, build)
        self.assertIn("--check-against docs/neutriverse-restructure-baseline.json", WORKFLOW)
        self.assertIn('${{ runner.temp }}/neutriverse-current.json', WORKFLOW)

    def test_acceptance_document_separates_source_build_and_online_evidence(self):
        for value in (
            "T01 protected baseline",
            "T33 的 production-build 门禁",
            "T36 authoring source 校验",
            "不声称已经完成线上端到端浏览",
            "_posts/2025-05-07-计组-06.md",
            "_posts/2026-05-24-neutriverse-site-changelog.md",
        ):
            self.assertIn(value, ACCEPTANCE)


if __name__ == "__main__":
    unittest.main()
