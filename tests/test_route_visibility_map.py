import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "docs" / "neutriverse-route-visibility-map.md"
BASELINE_PATH = ROOT / "docs" / "neutriverse-restructure-baseline.json"


class RouteVisibilityMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = MAP_PATH.read_text(encoding="utf-8")
        cls.baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))

    def test_all_baseline_page_sources_are_mapped(self):
        for page in self.baseline["pages"]:
            with self.subTest(path=page["path"]):
                self.assertIn(f"`{page['path']}`", self.text)
                self.assertIn(f"`{page['source_url_candidate']}`", self.text)

    def test_four_public_entries_and_chinese_explanations_are_fixed(self):
        expected = {
            "THINK": ("我如何思考与表达", "/think/"),
            "BUILD": ("我正在制作什么", "/build/"),
            "OBSERVE": ("我持续观察什么", "/observe/"),
            "ABOUT": ("我是谁以及这个站如何生长", "/about/"),
        }
        for name, (description, route) in expected.items():
            with self.subTest(entry=name):
                self.assertIn(f"| {name} | {description} | `{route}`", self.text)

    def test_q3_observe_contract_is_explicit(self):
        self.assertIn("Q3 明确要求 Ravenis 与 Occult Atlas 在 OBSERVE 可发现，同时保留 `noindex`", self.text)
        self.assertIn("OBSERVE 公开目录项，同时是 BUILD 项目关联的实际使用入口", self.text)
        self.assertIn("T33 应消除 Disallow 与页面 noindex 的语义冲突但不得改为 index", self.text)

    def test_q4_special_modules_are_explicit(self):
        for value in (
            "Prospero Great Library",
            "友链",
            "旅行地球",
            "Gate",
            "NAVI",
            "维持原 URL 和隐蔽发现",
        ):
            with self.subTest(value=value):
                self.assertIn(value, self.text)

    def test_visibility_dimensions_are_not_collapsed(self):
        for value in (
            "可直达",
            "公开发现",
            "隐蔽发现",
            "`noindex`",
            "`sitemap: false`",
            "`robots.txt Disallow`",
            "`hidden: true` / `hidden_pages`",
        ):
            with self.subTest(value=value):
                self.assertIn(value, self.text)

    def test_build_scope_is_complete_and_mmxproj_excluded(self):
        for project in (
            "FitzSight",
            "Akasha Notes",
            "Toyosatomimi's Headphone",
            "Ravenis",
            "Occult Atlas",
            "Gate",
            "OfficeSpire",
        ):
            with self.subTest(project=project):
                self.assertIn(f"| {project} |", self.text)
        self.assertIn("`MMXProj` 明确排除", self.text)

    def test_protected_routes_and_compatibility_routes_are_present(self):
        for route in (
            "/posts/:title/",
            "/categories/:name/",
            "/tags/:name/",
            "/tags/bus/",
            "/tags/changelog/",
            "/feed.xml",
            "/sitemap.xml",
            "/robots.txt",
        ):
            with self.subTest(route=route):
                self.assertIn(f"`{route}`", self.text)


if __name__ == "__main__":
    unittest.main()
