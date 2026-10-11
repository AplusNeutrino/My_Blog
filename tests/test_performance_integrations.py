import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PerformanceIntegrationContracts(unittest.TestCase):
    def test_pgl_preserves_ssr_and_defers_catalog(self):
        include = (ROOT / "_includes/pgl/library.html").read_text(encoding="utf-8")
        source = (ROOT / "assets/pgl/pgl.js").read_text(encoding="utf-8")
        self.assertIn("{% include pgl/stats.html %}", include)
        self.assertIn("function loadLibraryData()", source)
        self.assertIn("requestIdleCallback", source)
        self.assertIn("state.view !== 'index'", source)
        self.assertIn("pointerdown", source)
        self.assertIn("focusin", source)
        self.assertEqual(source.count("loadJson(root.dataset.libraryUrl)"), 1)

    def test_twikoo_is_lazy_and_has_visible_failure(self):
        source = (ROOT / "_includes/comments/twikoo.html").read_text(encoding="utf-8")
        self.assertNotIn('<script src="https://cdn.jsdelivr.net/npm/twikoo', source)
        self.assertIn("script.async = true", source)
        self.assertIn("IntersectionObserver", source)
        self.assertIn("rootMargin: '480px 0px'", source)
        self.assertIn("data-twikoo-status", source)
        self.assertIn("评论服务暂时不可用", source)
        for key in ("envId:", "path:", "lang:"):
            self.assertIn(key, source)

    def test_existing_like_and_ravenis_fallbacks_remain(self):
        likes = (ROOT / "_includes/post-like.html").read_text(encoding="utf-8")
        ravenis = (ROOT / "assets/js/ravenis.js").read_text(encoding="utf-8")
        self.assertIn("localStorage.getItem", likes)
        self.assertIn("localStorage.setItem", likes)
        self.assertIn("data-like-endpoint", likes)
        self.assertEqual(ravenis.count("fetchSearchIndex()"), 2)
        self.assertIn("fetchJSON('manifest.json')", ravenis)

    def test_production_workflow_runs_new_gate_after_build(self):
        workflow = (ROOT / ".github/workflows/pages-deploy.yml").read_text(encoding="utf-8")
        build = workflow.index("- name: Build site")
        gate = workflow.index("- name: Validate resource scope and integration fallbacks")
        upload = workflow.index("- name: Upload site artifact")
        self.assertLess(build, gate)
        self.assertLess(gate, upload)
        self.assertIn('python tools/check_performance_integrations.py "_site${{ steps.pages.outputs.base_path }}"', workflow)

    def test_built_post_probe_uses_rendered_markers_not_a_guessed_slug(self):
        checker = (ROOT / "tools/check_performance_integrations.py").read_text(encoding="utf-8")
        self.assertIn('site.rglob("*.html")', checker)
        self.assertIn('"data-post-like" not in candidate', checker)
        self.assertNotIn('/posts/dbms-01/', checker)


if __name__ == "__main__":
    unittest.main()
