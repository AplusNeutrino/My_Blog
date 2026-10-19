"""Exercise actual audit helper; does not certify browser visuals."""
import ast
from pathlib import Path
import unittest


class FakeDriver:
    def __init__(self, colors):
        self.colors = iter(colors)
        self.current = None
        self.reads = 0

    def execute_script(self, script):
        if not script.startswith('return '):
            return None
        self.reads += 1
        self.current = next(self.colors, self.current)
        return self.current


class BoundedWait:
    def __init__(self, driver, timeout):
        assert timeout == 5
        self.driver = driver

    def until(self, predicate):
        for _ in range(4):
            if predicate(self.driver):
                return True
        raise TimeoutError('old color never reached')


class AtlasIconFixtureTimingTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_atlas_planet_icons.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'inject_old_backplate')
        ns = {'WebDriverWait': BoundedWait}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<icon-audit>', 'exec'), ns)
        return ns['inject_old_backplate']

    def test_waits_past_original_and_intermediate_colors(self):
        driver = FakeDriver(['rgb(255, 248, 231)', 'rgb(120, 130, 140)', 'rgb(23, 68, 90)'])
        self.assertEqual(self.helper()(driver, 'light'), 'rgb(23, 68, 90)')
        self.assertEqual(driver.reads, 4)

    def test_missing_fault_injection_still_blocks(self):
        driver = FakeDriver(['rgb(255, 248, 231)'] * 4)
        with self.assertRaises(TimeoutError):
            self.helper()(driver, 'light')
