"""Helper contracts only; real lazy-load/visual acceptance requires Chrome."""
import ast
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


class LibraryCoverAuditTests(unittest.TestCase):
    def run_helper(self, rows):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'library_visible_covers')
        def require(ok, message):
            if not ok:
                raise AssertionError(message)
        namespace = {'require': require, 'json': json}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<helper>', 'exec'), namespace)
        class Driver:
            def execute_script(self, script):
                self.script = script
                return rows
            def save_screenshot(self, path):
                self.screenshot = path
            def execute_async_script(self, script):
                self.decode_script = script
                return {'ok': True}
        driver = Driver()
        class Wait:
            def until(self, callback):
                if not callback(driver):
                    raise TimeoutError('native load did not finish')
        with TemporaryDirectory() as folder:
            try:
                return namespace['library_visible_covers'](driver, Wait(), Path(folder), 390, 'dark')
            finally:
                if rows:
                    evidence=json.loads((Path(folder)/'covers-390-dark-library.json').read_text())
                    self.assertEqual(evidence['images'],rows)
                    self.assertTrue(driver.screenshot.endswith('.png'))
                    self.assertNotIn('setAttribute',driver.script)
                    if all(row['complete'] for row in rows):
                        self.assertIn('e.decode()',driver.decode_script)
                        self.assertIn('requestAnimationFrame',driver.decode_script)

    def test_loaded_visible_images_pass(self):
        self.assertEqual(self.run_helper([{'complete':True,'naturalWidth':100,'naturalHeight':150}]),
                         {'visibleImages':1,'loaded':True})

    def test_broken_image_fails_but_records_evidence(self):
        with self.assertRaises(AssertionError):
            self.run_helper([{'complete':True,'naturalWidth':0,'naturalHeight':0}])

    def test_loading_timeout_fails_but_records_evidence(self):
        with self.assertRaises(TimeoutError):
            self.run_helper([{'complete':False,'naturalWidth':0,'naturalHeight':0}])

    def test_empty_view_is_not_success(self):
        with self.assertRaises(AssertionError):
            self.run_helper([])
