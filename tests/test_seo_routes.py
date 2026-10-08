import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD = (ROOT / "_includes" / "metadata-hook.html").read_text(encoding="utf-8")
GATE = (ROOT / "gate" / "index.md").read_text(encoding="utf-8")
GATE_LAYOUT = (ROOT / "_layouts" / "gate.html").read_text(encoding="utf-8")
NAVI = (ROOT / "_hidden_pages" / "navi.md").read_text(encoding="utf-8")
OCCULT_REDIRECT = (ROOT / "occult-atlas-app" / "index.html").read_text(encoding="utf-8")
ROBOTS = (ROOT / "assets" / "robots.txt").read_text(encoding="utf-8")
FITZSIGHT = (ROOT / "projfitzgerald" / "index.html").read_text(encoding="utf-8")
CHECKER = (ROOT / "tools" / "check_seo_routes.py").read_text(encoding="utf-8")
WORKFLOW = (ROOT / ".github" / "workflows" / "pages-deploy.yml").read_text(encoding="utf-8")


class SeoRoutesTest(unittest.TestCase):
    def test_page_robots_is_emitted_once_inside_shared_head(self):
        self.assertIn("{% elsif page.robots %}", HEAD)
        self.assertIn('content="{{ page.robots | escape }}"', HEAD)
        self.assertNotIn('content="noindex,nofollow"', GATE_LAYOUT)
        self.assertIn("{% elsif page.robots %}", HEAD)
        self.assertNotIn("{% if page.ravenis %}\n  <meta name=\"robots\"", HEAD)

    def test_gate_and_navi_keep_routes_but_are_explicitly_noindex(self):
        for source in (GATE, NAVI):
            self.assertIn("sitemap: false", source)
            self.assertIn("robots: noindex,nofollow", source)
        self.assertIn("permalink: /gate/", GATE)
        self.assertIn("permalink: /navi/", NAVI)

    def test_occult_compatibility_route_has_target_canonical(self):
        self.assertIn("permalink: /occult-atlas-app/", OCCULT_REDIRECT)
        self.assertIn("noindex, nofollow", OCCULT_REDIRECT)
        self.assertIn("{{ '/occult-atlas/' | absolute_url }}", OCCULT_REDIRECT)

    def test_existing_fitzsight_tool_has_a_canonical(self):
        self.assertIn("{{ '/projfitzgerald/' | absolute_url }}", FITZSIGHT)

    def test_ravenis_is_crawlable_for_page_level_noindex(self):
        self.assertNotIn("Disallow: /ravenis/", ROBOTS)
        self.assertIn("Sitemap: {{ '/sitemap.xml' | absolute_url }}", ROBOTS)

    def test_built_output_checker_is_after_build_and_before_upload(self):
        self.assertIn("baseline_routes", CHECKER)
        self.assertIn("duplicate canonical", CHECKER)
        self.assertIn("redirect loop detected", CHECKER)
        self.assertIn("broken internal page link", CHECKER)
        build = WORKFLOW.index("- name: Build site")
        validate = WORKFLOW.index("- name: Validate SEO, sitemap, redirects, and internal routes")
        upload = WORKFLOW.index("- name: Upload site artifact")
        self.assertLess(build, validate)
        self.assertLess(validate, upload)
        self.assertIn('python tools/check_seo_routes.py "_site${{ steps.pages.outputs.base_path }}"', WORKFLOW)


if __name__ == "__main__":
    unittest.main()
