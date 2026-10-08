import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = (ROOT / "_tabs" / "about.md").read_text(encoding="utf-8")
DATA = (ROOT / "_data" / "neutriverse_about.yml").read_text(encoding="utf-8")
PROFILE = (ROOT / "_includes" / "neutriverse-about-profile.html").read_text(
    encoding="utf-8"
)


class AboutDataModelTest(unittest.TestCase):
    def test_about_page_uses_one_content_source(self):
        self.assertEqual(ABOUT.count("neutriverse-about-profile.html"), 1)
        self.assertIn("site.data.neutriverse_about", PROFILE)
        for legacy in (
            "about_info_text",
            "about_now_summary",
            "signal_items",
            "status_items",
            "roadmap_items",
            "reading_stack_items",
            "visual_stack_items",
        ):
            self.assertNotIn(legacy, ABOUT)

    def test_migrated_snapshot_is_explicitly_historical(self):
        for marker in (
            'as_of: "2026-08-17"',
            "as_of_label: 更新于 2026-08-17",
            "notice: 历史快照 · 非实时状态",
            'data-as-of="{{ snapshot.as_of }}"',
            'datetime="{{ snapshot.as_of }}"',
            "{{ snapshot.notice }}",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, DATA + PROFILE)

    def test_content_is_limited_to_the_preexisting_about_material(self):
        migrated_values = (
            "本站是 Neutrino 的个人文字站。",
            "主要用于存储笔记、读后感和记忆碎片。",
            "欢迎所有的你。",
            "全力备战软考系统分析师中。",
            "正在品鉴《无敌号》。",
            "软考备战中",
            "软考好多东西",
            "继续写游戏REPO",
            "VB一个竞赛小玩具",
            "保持健身",
            "入职环境调节",
            "构筑稳定生活流",
            "实现时/财自由",
            "《迷雾之子》",
            "《大师与玛格丽特》",
            "《阿特拉斯耸耸肩》",
            "《无限近似于青色的蓝》",
            "《诺瓦利斯作品选集》",
            "《纽约提喻法》",
            "《Amadeus》",
            "《挽救计划》",
            "《全金属外壳》",
            "《斯巴达克斯》",
        )
        for value in migrated_values:
            with self.subTest(value=value):
                self.assertEqual(DATA.count(value), 1)
                self.assertNotIn(value, ABOUT)
        self.assertIn("source: _tabs/about.md before T27", DATA)

    def test_profile_renders_structured_lists_without_copying_values(self):
        for expression in (
            "about.identity.lines",
            "snapshot.summary",
            "snapshot.signals",
            "snapshot.status",
            "snapshot.roadmap",
            "about.stacks[stack_key]",
            "stack.items | sort: 'added'",
        ):
            self.assertIn(expression, PROFILE)
        self.assertIn("data-about-profile", PROFILE)
        self.assertIn('role="note"', PROFILE)

    def test_related_about_surfaces_and_travel_implementation_stay_in_place(self):
        sections = (ROOT / "_data" / "neutriverse_sections.yml").read_text(
            encoding="utf-8"
        )
        for route in ("/library/", "/links/", "/about/#about-relations-title"):
            self.assertIn(route, sections)
        for marker in (
            "travel_globe_enabled = false",
            "site.data.travel_regions",
            "site.data.travel_boundary_sources",
            "assets/js/travel-globe.js",
        ):
            self.assertIn(marker, ABOUT)


if __name__ == "__main__":
    unittest.main()
