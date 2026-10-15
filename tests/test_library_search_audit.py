"""Audit contract checks; visual/search acceptance still requires real Chrome."""
import ast
from pathlib import Path
import unittest


class LibrarySearchAuditTests(unittest.TestCase):
    def test_real_input_refresh_empty_and_clear_are_required(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        node=next(n for n in ast.parse(source).body
                  if isinstance(n,ast.FunctionDef) and n.name=='library_search_controls')
        helper=ast.get_source_segment(source,node)
        for text in ['field.send_keys(value)','driver.refresh()',
                     "capture('results')","capture('empty')","capture('cleared')",
                     "expected_id in",'Library empty message missing',
                     'Library clear did not restore root URL']:
            self.assertIn(text,helper)
        self.assertNotIn('.value =',helper)
        self.assertNotIn('dispatchEvent',helper)

    def test_query_comes_from_existing_public_card(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        self.assertIn("query = first.find_element(By.CSS_SELECTOR, '.pgl-card-title').text",source)
        self.assertIn("expected_id = first.get_attribute('data-pgl-id')",source)
