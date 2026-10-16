"""Audit wiring tests, not a substitute for actual browser/screenshots."""
import ast
from pathlib import Path
import unittest


class LibrarySteamCoverAuditTests(unittest.TestCase):
    def helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
                    and n.name == 'library_steam_cover_controls')
        return source, ast.get_source_segment(source, node)

    def test_native_cover_scroll_decode_without_loader_override(self):
        source, helper = self.helper()
        for text in ('scrollIntoView', 'e.decode()', 'e.naturalWidth', 'e.naturalHeight',
                     "observed['width'] > 0", "c['before']['top'] >= c['before']['height']",
                     'save_screenshot', 'steam-covers-{state}-{width}-{theme}-library.json'):
            self.assertIn(text, helper)
        for forbidden in ('.src =', '.loading =', 'dispatchEvent', '.focus()', 'except'):
            self.assertNotIn(forbidden, helper)
        self.assertIn('steam_covers = library_steam_cover_controls(', source)
        self.assertIn("'steamCovers':steam_covers", source)

    def test_real_steam_data_and_empty_reload_recovery(self):
        _, helper = self.helper()
        for text in ("select_by_value('playtime')", "select_by_value('steam')",
                     "values == sorted(values, reverse=True)", "ranks == sorted(ranks)",
                     "driver.current_url == ordered_url", "driver.current_url == filtered_url",
                     "'#pgl-grid .pgl-empty'", "click('#pgl-clear-filters')", "click('#pgl-back')",
                     "'pending-no-data'", "steam_status in ('ok', 'stale')"):
            self.assertIn(text, helper)

    def test_all_five_states_and_client_viewport_gate_retained(self):
        _, helper = self.helper()
        for state in ('stats', 'playtime', 'last', 'reloaded', 'source'):
            self.assertIn(f"capture('{state}'", helper)
        self.assertIn("geometry['clientViewport']+1", helper)
        self.assertIn("len(set(ordered)) == len(ordered)", helper)
        self.assertIn("len(ids()) == min(page_size,len(expected_steam))", helper)
