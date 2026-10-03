import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = (ROOT / "_data" / "neutriverse_sections.yml").read_text(encoding="utf-8")


class NeutriverseSectionsTest(unittest.TestCase):
    def test_single_data_source_has_four_canonical_entries(self):
        expected = {
            "think": ("THINK", "我如何思考与表达", "/think/"),
            "build": ("BUILD", "我正在制作什么", "/build/"),
            "observe": ("OBSERVE", "我持续观察什么", "/observe/"),
            "about": ("ABOUT", "我是谁以及这个站如何生长", "/about/"),
        }
        self.assertEqual(DATA.count("  - id:"), 4)
        for section_id, (name, label, url) in expected.items():
            with self.subTest(section=section_id):
                block = re.search(
                    rf"  - id: {re.escape(section_id)}\n(?P<body>.*?)(?=\n  - id:|\Z)",
                    DATA,
                    re.DOTALL,
                )
                self.assertIsNotNone(block)
                body = block.group("body")
                self.assertIn(f"    name: {name}", body)
                self.assertIn(f"    label_zh: {label}", body)
                self.assertIn(f"    url: {url}", body)
                self.assertRegex(body, r"    summary: \S.+")
                self.assertIn("    links:", body)

    def test_new_canonical_pages_use_shared_layout(self):
        for section_id in ("think", "build", "observe"):
            with self.subTest(section=section_id):
                page = (ROOT / section_id / "index.md").read_text(encoding="utf-8")
                self.assertIn("layout: neutriverse-section", page)
                self.assertIn(f"permalink: /{section_id}/", page)
                self.assertIn(f"section_id: {section_id}", page)

    def test_shared_layout_and_navigation_are_data_driven(self):
        layout = (ROOT / "_layouts" / "neutriverse-section.html").read_text(encoding="utf-8")
        nav = (ROOT / "_includes" / "neutriverse-primary-nav.html").read_text(encoding="utf-8")
        links = (ROOT / "_includes" / "neutriverse-section-links.html").read_text(encoding="utf-8")
        self.assertIn("site.data.neutriverse_sections.sections", layout)
        self.assertIn("neutriverse-primary-nav.html", layout)
        self.assertIn("neutriverse-section-links.html", layout)
        self.assertIn("site.data.neutriverse_sections.sections", nav)
        self.assertIn('aria-current="page"', nav)
        self.assertIn("nv_section.links", links)

    def test_about_keeps_its_route_and_uses_shared_components(self):
        about = (ROOT / "_tabs" / "about.md").read_text(encoding="utf-8")
        self.assertIn("neutriverse-primary-nav.html current='about'", about)
        self.assertIn("neutriverse-section-links.html current='about'", about)
        self.assertNotIn("permalink:", about)

    def test_public_navigation_does_not_expose_hidden_tools_or_excluded_project(self):
        for forbidden in ("/gate/", "/navi/", "MMXProj"):
            with self.subTest(value=forbidden):
                self.assertNotIn(forbidden, DATA)

    def test_all_data_links_are_real_current_routes(self):
        urls = re.findall(r"^\s+url: (/.+)$", DATA, re.MULTILINE)
        expected = {
            "/think/",
            "/build/",
            "/observe/",
            "/about/",
            "/thoughts/",
            "/archives/",
            "/tags/",
            "/categories/",
            "/projfitzgerald/",
            "/posts/阿卡夏便笺akashanotes/",
            "/posts/丰聪耳机toyosatomimisheadphone/",
            "/ravenis/",
            "/occult-atlas/",
            "/library/",
            "/links/",
            "/about/#travel-globe-title",
        }
        self.assertEqual(set(urls), expected)

    def test_no_fake_or_disabled_function_is_rendered(self):
        sources = "\n".join(
            (ROOT / path).read_text(encoding="utf-8")
            for path in (
                "_data/neutriverse_sections.yml",
                "_includes/neutriverse-primary-nav.html",
                "_includes/neutriverse-section-links.html",
                "think/index.md",
                "build/index.md",
                "observe/index.md",
            )
        ).lower()
        for marker in ('href="#"', "coming soon", "disabled"):
            self.assertNotIn(marker, sources)

    def test_shared_stylesheet_and_theme_tokens_are_wired(self):
        hook = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
        shared = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(encoding="utf-8")
        self.assertIn("/assets/css/neutriverse-sections.css", hook)
        self.assertIn(".nv-primary-nav", shared)
        self.assertIn("outline: 2px solid var(--nv-focus)", shared)
        self.assertIn("@media (max-width: 767.98px)", shared)
        self.assertIn("@media (prefers-reduced-motion: reduce)", shared)
        for theme_file in ("NormaiNight.css", "ProsperoLight.css"):
            theme = (ROOT / "assets" / "css" / theme_file).read_text(encoding="utf-8")
            for token in ("--nv-canvas", "--nv-surface-1", "--nv-text", "--nv-accent", "--nv-focus"):
                with self.subTest(theme=theme_file, token=token):
                    self.assertIn(f"{token}:", theme)


if __name__ == "__main__":
    unittest.main()
