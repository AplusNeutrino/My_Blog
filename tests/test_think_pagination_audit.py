"""Wiring checks only; actual screenshots and pointer flows run in Chrome CI."""
import ast
from pathlib import Path
import unittest


class ThinkPaginationAuditTests(unittest.TestCase):
    def test_lossless_scoped_artifacts_keep_complete_archives(self):
        import yaml
        workflow = yaml.safe_load(Path('.github/workflows/pages-deploy.yml').read_text())
        for job, full, scoped in (
            ('build', 'neutriverse-think-build-', 'neutriverse-think-pagination-'),
            ('verify-live-ui', 'neutriverse-live-ui-', 'neutriverse-live-think-pagination-'),
        ):
            steps = workflow['jobs'][job]['steps']
            uploads = [s for s in steps if s.get('uses') == 'actions/upload-artifact@v4']
            self.assertTrue(any(s['with']['name'].startswith(full) for s in uploads))
            scope = next(s for s in uploads if s['with']['name'].startswith(scoped))
            self.assertEqual(scope['if'], 'always()')
            self.assertEqual(scope['with']['retention-days'], 14)
            for pattern in ('public-sweep-think-page-*.png', 'public-sweep-think-page-*.json',
                            'public-top-think-page-*.png', 'think-pagination-*.json',
                            'think-pagination-*.png', 'audit.json'):
                self.assertIn(pattern, scope['with']['path'])

    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'think_pagination_controls')
        return source, ast.get_source_segment(source, node)

    def test_all_pages_exact_public_inventory_and_native_sweeps(self):
        source, helper = self.helper()
        for token in ('range(1, 5)', 'len(expected) == 44', 'len(set(seen)) == 44',
                      'expected[(number-1)*12:number*12]', 'public_page_sweep(',
                      'data-writing-page-current', 'data-writing-page-total', 'aria-current'):
            self.assertIn(token, helper)
        self.assertIn("result['paginationInventory'] = think_pagination_controls(", source)
        self.assertNotIn('captureBeyondViewport', helper)

    def test_refresh_previous_real_click_and_failure_evidence(self):
        _, helper = self.helper()
        for token in ('driver.refresh()', 'driver.current_url == original', 'expected[36:44]',
                      'expected[24:36]', 'e.click()', 'elementFromPoint', 'think-pagination-failure-',
                      'finally:', 'visibleHrefs', 'raise', 'settle(driver, wait, theme)'):
            self.assertIn(token, helper)
        self.assertNotIn('dispatchEvent', helper)
