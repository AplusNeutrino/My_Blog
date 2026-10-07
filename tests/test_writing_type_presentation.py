import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WritingTypePresentationTest(unittest.TestCase):
    def test_taxonomy_supplies_bilingual_labels_for_three_types(self):
        taxonomy = (ROOT / "_data" / "content_taxonomy.yml").read_text(encoding="utf-8")
        block = re.search(r"^types:\n(?P<body>.*?)(?=^topics:)", taxonomy, re.M | re.S)
        self.assertIsNotNone(block)
        self.assertEqual(
            [
                ("fragment", "Fragment", "片段"),
                ("note", "Note", "笔记"),
                ("essay", "Essay", "长文"),
            ],
            re.findall(
                r"^  ([a-z]+):\n    label: ([A-Za-z]+)\n    label_zh: (.+)$",
                block.group("body"),
                re.M,
            ),
        )

    def test_post_layout_uses_existing_type_without_touching_content(self):
        layout = (ROOT / "_layouts" / "post.html").read_text(encoding="utf-8")
        self.assertIn("site.data.content_taxonomy.types[page.type]", layout)
        self.assertIn("nv-post--{{ page.type | escape }}", layout)
        self.assertIn('data-writing-type="{{ page.type | escape }}"', layout)
        self.assertIn("nv_post_type.label_zh", layout)
        self.assertEqual(1, layout.count("{{ content }}"))

    def test_think_records_expose_all_three_type_classes(self):
        writing = (
            ROOT / "_includes" / "neutriverse-writing-list.html"
        ).read_text(encoding="utf-8")
        self.assertIn("nv-writing-record is-{{ item.type | escape }}", writing)
        self.assertNotIn("if nv_is_fragment %} is-fragment", writing)

    def test_shared_css_distinguishes_types_and_constrains_rich_content(self):
        css = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(
            encoding="utf-8"
        )
        for selector in (
            ".nv-writing-record.is-note",
            ".nv-writing-record.is-essay",
            ".nv-writing-record.is-fragment",
            "article.nv-post--note > header",
            "article.nv-post--essay > header",
            "article.nv-post .content pre",
            "article.nv-post .content .table-wrapper",
            "article.nv-post .content img",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, css)
        self.assertIn("max-width: 46rem", css)
        self.assertIn("overflow-x: auto", css)


if __name__ == "__main__":
    unittest.main()
