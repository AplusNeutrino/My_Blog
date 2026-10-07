import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SIDEBAR = (ROOT / "_includes" / "sidebar.html").read_text(encoding="utf-8")
SECTIONS = (ROOT / "_data" / "neutriverse_sections.yml").read_text(encoding="utf-8")
STYLES = (ROOT / "assets" / "css" / "neutriverse-sections.css").read_text(encoding="utf-8")
SCRIPT = (ROOT / "assets" / "js" / "neutriverse-navigation.js").read_text(encoding="utf-8")


class NeutriverseSidebarTest(unittest.TestCase):
    def test_four_primary_entrances_render_from_the_shared_source(self):
        self.assertIn("site.data.neutriverse_sections.sections", SIDEBAR)
        self.assertIn("{{ entry.name }}", SIDEBAR)
        self.assertIn("{{ entry.label_zh }}", SIDEBAR)
        self.assertNotRegex(SIDEBAR, r"for tab in site\.tabs")

    def test_home_and_section_active_states_are_accessible(self):
        self.assertIn("nv_current = 'home'", SIDEBAR)
        self.assertIn('aria-current="page"', SIDEBAR)
        self.assertIn("entry.id == nv_current", SIDEBAR)
        self.assertIn("返回首页", SIDEBAR)

    def test_route_ownership_covers_existing_public_surfaces(self):
        for route in (
            "/posts/", "/thoughts/", "/tags/", "/archives/", "/categories/",
            "/build/", "/projfitzgerald/", "/ravenis/", "/occult-atlas/",
            "/about/", "/library/", "/links/",
        ):
            with self.subTest(route=route):
                self.assertIn(route, SECTIONS)

    def test_secondary_utilities_preserve_search_archive_feed_and_social(self):
        self.assertIn("data-nv-search-trigger", SIDEBAR)
        self.assertIn("'/tags/'", SIDEBAR)
        self.assertIn("'/archives/'", SIDEBAR)
        self.assertIn("'/feed.xml'", SIDEBAR)
        self.assertIn("site.twitter.username", SIDEBAR)
        self.assertIn("site.github.username", SIDEBAR)
        self.assertIn("nativeTrigger.click()", SCRIPT)
        self.assertIn("searchInput?.focus()", SCRIPT)

    def test_hidden_tools_and_excluded_project_are_not_in_public_sidebar(self):
        for forbidden in ("/gate/", "/navi/", "MMXProj"):
            with self.subTest(value=forbidden):
                self.assertNotIn(forbidden, SIDEBAR)
                self.assertNotIn(forbidden, SECTIONS)

    def test_navigation_styles_have_desktop_hierarchy_and_focus(self):
        self.assertIn("#sidebar .nv-sidebar-primary .nav-link", STYLES)
        self.assertIn("#sidebar .nv-sidebar-utility-group", STYLES)
        self.assertIn("@media (min-width: 850px)", STYLES)
        self.assertRegex(STYLES, r"outline:\s*2px solid var\(--nv-focus\)")
        self.assertNotIn("transition: all", STYLES)

    def test_sidebar_uses_links_for_navigation_and_button_for_search(self):
        self.assertRegex(SIDEBAR, r"<button[^>]+data-nv-search-trigger")
        self.assertRegex(SIDEBAR, r"<a\s+href=\"\{\{ entry\.url")
        self.assertNotIn('href="#"', SIDEBAR)

    def test_navigation_asset_is_loaded(self):
        hook = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
        self.assertIn("/assets/js/neutriverse-navigation.js", hook)
        self.assertIn("defer", hook)

    def test_theme_does_not_hide_secondary_writing_routes(self):
        # The old tab suppression also matched the new Tags/Archive utilities.
        # Markup presence alone cannot prove an entrance is actually reachable.
        for theme in ("NormaiNight.css", "ProsperoLight.css"):
            css = (ROOT / "assets" / "css" / theme).read_text(encoding="utf-8")
            for route in ("tags", "archives"):
                with self.subTest(theme=theme, route=route):
                    self.assertNotRegex(
                        css,
                        rf'[^{{}}]*:has\([^{{}}]*href[^{{}}]*/{route}/[^{{}}]*\{{[^{{}}]*display:\s*none',
                    )

    def test_essential_navigation_labels_meet_minimum_size(self):
        for selector in (
            "#sidebar .nv-sidebar-copy small",
            "#sidebar .nv-sidebar-utilities .nav-link",
        ):
            block = re.search(re.escape(selector) + r"\s*\{([^}]+)\}", STYLES).group(1)
            size = re.search(r"font-size:\s*([\d.]+)rem", block).group(1)
            self.assertGreaterEqual(float(size), 0.75)

    def test_utility_buttons_fill_their_grid_cell_without_label_wrap(self):
        cell = re.findall(
            r"#sidebar \.nv-sidebar-utilities \.nav-item\s*\{([^}]+)\}", STYLES
        )[-1]
        self.assertIn("padding: 0", cell)
        self.assertIn("margin: 0", cell)
        block = re.search(
            r"#sidebar \.nv-sidebar-utilities \.nav-link\s*\{([^}]+)\}", STYLES
        ).group(1)
        self.assertIn("width: 100%", block)
        self.assertIn("white-space: nowrap", block)


if __name__ == "__main__":
    unittest.main()
