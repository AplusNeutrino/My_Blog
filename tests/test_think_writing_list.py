import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ThinkWritingListTest(unittest.TestCase):
    def test_list_uses_authoritative_sources_and_excludes_hidden_posts(self):
        include = (ROOT / "_includes" / "neutriverse-writing-list.html").read_text(encoding="utf-8")
        self.assertIn("site.posts | where_exp: 'item', 'item.hidden != true'", include)
        self.assertIn("site.tabs | where: 'layout', 'thoughts' | first", include)
        self.assertIn("nv_visible_posts | concat: nv_fragments | sort: 'date' | reverse", include)
        self.assertIn("data-writing-type", include)
        self.assertIn("data-writing-topic", include)
        self.assertNotIn("item.categories", include)

    def test_list_has_real_empty_state_and_fragment_source_links(self):
        include = (ROOT / "_includes" / "neutriverse-writing-list.html").read_text(encoding="utf-8")
        thoughts = (ROOT / "_layouts" / "thoughts.html").read_text(encoding="utf-8")
        self.assertIn("还没有公开写作记录", include)
        self.assertIn("查看片段原页", include)
        self.assertIn("item.id | default: '' | strip", include)
        self.assertIn("#{{ nv_fragment_id | escape }}", include)
        self.assertIn("fragment.id | default: '' | strip", thoughts)
        self.assertIn('id="{{ fragment_id | escape }}"', thoughts)

    def test_current_public_inventory_contract(self):
        baseline = json.loads(
            (ROOT / "docs" / "neutriverse-restructure-baseline.json").read_text(encoding="utf-8")
        )
        public_posts = [post for post in baseline["posts"] if not post["hidden"]]
        self.assertEqual(39, len(public_posts))
        self.assertEqual(5, len(baseline["fragments"]))
        self.assertEqual(44, len(public_posts) + len(baseline["fragments"]))

    def test_progressive_filters_keep_the_server_rendered_fallback(self):
        include = (ROOT / "_includes" / "neutriverse-writing-list.html").read_text(encoding="utf-8")
        layout = (ROOT / "_layouts" / "neutriverse-section.html").read_text(encoding="utf-8")
        script = (
            ROOT / "assets" / "js" / "neutriverse-writing-filters.js"
        ).read_text(encoding="utf-8")

        self.assertIn('data-writing-controls hidden', include)
        self.assertIn('data-writing-page-size="12"', include)
        self.assertIn("JavaScript 未启用，以下显示全部公开写作记录", include)
        self.assertIn("data-writing-filter-empty", include)
        self.assertIn("neutriverse-writing-filters.js", layout)
        for parameter in ("type", "topic", "sort", "page"):
            with self.subTest(parameter=parameter):
                self.assertIn("'" + parameter + "'", script)
        self.assertIn("window.addEventListener('popstate'", script)
        self.assertIn("window.history[historyMode + 'State']", script)
        self.assertNotIn("document.write", script)

    def test_filter_contract_uses_only_three_types_and_four_topics(self):
        script = (
            ROOT / "assets" / "js" / "neutriverse-writing-filters.js"
        ).read_text(encoding="utf-8")
        self.assertIn("['all', 'note', 'essay', 'fragment']", script)
        self.assertIn(
            "['all', 'computation', 'humanity', 'otaku', 'arts']",
            script,
        )
        self.assertIn("['newest', 'oldest']", script)

    def test_shared_layout_and_styles_wire_the_ledger(self):
        layout = (ROOT / "_layouts" / "neutriverse-section.html").read_text(encoding="utf-8")
        css = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(encoding="utf-8")
        self.assertIn("page.section_id == 'think'", layout)
        self.assertIn("neutriverse-writing-list.html", layout)
        for selector in (
            ".nv-writing-ledger",
            ".nv-writing-record",
            ".nv-writing-taxonomy",
            ".nv-writing-empty",
            ".nv-writing-controls",
            ".nv-writing-pagination",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
        self.assertRegex(css, r"\.nv-writing-record h3 a:focus-visible")

    def test_custom_filters_keep_native_state_and_accessible_options(self):
        include = (ROOT / "_includes" / "neutriverse-writing-list.html").read_text(encoding="utf-8")
        filter_include = (ROOT / "_includes" / "neutriverse-filter-select.html").read_text(encoding="utf-8")
        script = (ROOT / "assets" / "js" / "neutriverse-writing-filters.js").read_text(encoding="utf-8")
        for target in ("nv-writing-type", "nv-writing-topic", "nv-writing-series", "nv-writing-sort"):
            with self.subTest(target=target):
                self.assertIn(f"id='{target}'", include)
        self.assertIn('role="listbox"', filter_include)
        self.assertIn('role="option"', filter_include)
        self.assertIn("class=\"nv-writing-native-select\" hidden", include)
        self.assertIn("const syncFilterDetails", script)
        self.assertIn("select.value = option.dataset.value", script)
        self.assertIn("updateFromControls()", script)
        self.assertIn("closeFilterDetails(details, true)", script)
        self.assertIn("event.key === 'Escape'", script)


if __name__ == "__main__":
    unittest.main()
