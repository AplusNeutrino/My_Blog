import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ThinkFragmentsTest(unittest.TestCase):
    def test_fragment_source_declares_unique_stable_ids(self):
        source = (ROOT / "_tabs" / "thoughts.md").read_text(encoding="utf-8")
        source = source.split("---", 2)[1]
        pairs = re.findall(
            r'^  - text: .+\n    id: (fragment-[a-z0-9-]+)\n    date: (\d{4}-\d{2}-\d{2})$',
            source,
            re.MULTILINE,
        )
        self.assertEqual(
            [
                ("fragment-2024-09-12", "2024-09-12"),
                ("fragment-2024-10-30", "2024-10-30"),
                ("fragment-2025-03-23", "2025-03-23"),
                ("fragment-2025-11-12", "2025-11-12"),
                ("fragment-2026-05-02", "2026-05-02"),
            ],
            pairs,
        )
        self.assertEqual(len(pairs), len({fragment_id for fragment_id, _ in pairs}))

    def test_thoughts_and_think_share_the_same_id_field(self):
        thoughts_layout = (ROOT / "_layouts" / "thoughts.html").read_text(encoding="utf-8")
        writing_list = (
            ROOT / "_includes" / "neutriverse-writing-list.html"
        ).read_text(encoding="utf-8")
        source = (ROOT / "_tabs" / "thoughts.md").read_text(encoding="utf-8")
        source = source.split("---", 2)[1]

        self.assertIn("fragment.id | default: '' | strip", thoughts_layout)
        self.assertIn('id="{{ fragment_id | escape }}"', thoughts_layout)
        self.assertIn("item.id | default: '' | strip", writing_list)
        self.assertIn("#{{ nv_fragment_id | escape }}", writing_list)
        self.assertIn("nv_fragment_page.fragments", writing_list)

        texts = re.findall(r'^  - text: "(.*)"$', source, re.MULTILINE)
        self.assertEqual(5, len(texts))
        for text in texts:
            with self.subTest(text=text):
                self.assertNotIn(text, thoughts_layout)
                self.assertNotIn(text, writing_list)


if __name__ == "__main__":
    unittest.main()
