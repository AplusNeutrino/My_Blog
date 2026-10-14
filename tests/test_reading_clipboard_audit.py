"""Audit regressions; real clipboard/visual acceptance still requires Chrome CI."""
import ast
from pathlib import Path
import unittest


class ClipboardAuditTests(unittest.TestCase):
    def test_helper_reads_real_clipboard_and_rejects_failure(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'clipboard_text')
        def require(ok, message):
            if not ok:
                raise AssertionError(message)
        namespace = {'require': require}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<helper>', 'exec'), namespace)
        class Driver:
            def execute_async_script(self, script, value):
                self.script, self.value = script, value
                return self.result
        driver = Driver()
        driver.result = {'ok': True, 'text': 'https://example.test/posts/test/'}
        self.assertEqual(namespace['clipboard_text'](driver), driver.result['text'])
        self.assertIsNone(driver.value)
        self.assertIn('navigator.clipboard.readText()', driver.script)
        namespace['clipboard_text'](driver, 'sentinel')
        self.assertEqual(driver.value, 'sentinel')
        driver.result = {'ok': False, 'error': 'NotAllowedError'}
        with self.assertRaises(AssertionError):
            namespace['clipboard_text'](driver)

    def test_scene_requires_sentinel_and_exact_url_after_real_click(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        self.assertIn("require(clipboard_text(driver) == sentinel", source)
        self.assertIn('copy.click()', source)
        self.assertIn('require(actual == driver.current_url', source)
        self.assertIn("'clipboardBytes': 'verified'", source)
        self.assertIn("'origin': base", source)


if __name__ == '__main__':
    unittest.main()
