"""Static audit contracts only; real Chrome screenshots remain required."""
import ast
from pathlib import Path
import unittest


class LibrarySortLayoutAuditTests(unittest.TestCase):
    def test_real_controls_reload_keyboard_and_strict_geometry(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_sort_layout_controls')
        helper = ast.get_source_segment(source, node)
        for text in ('select_by_value(key)', 'button.click()', 'driver.refresh()',
                     'button.send_keys(Keys.ENTER)', "capture('rating')", "capture('year')",
                     "capture('list')", "capture('reloaded')", 'ids() == title_ids',
                     "card['status'] == 'in_progress'", 'sorted(values, reverse=True)',
                     "geometry['page'] <= geometry['viewport']+1", "c['scroll'] <= c['client']+1",
                     'save_screenshot', 'write_text(json.dumps(geometry'):
            self.assertIn(text, helper)
        self.assertIn('sort_layout = library_sort_layout_controls(', source)
        self.assertIn("'sortLayout':sort_layout", source)
        self.assertNotIn('dispatchEvent', helper)
        self.assertNotIn('localStorage.setItem', helper)
