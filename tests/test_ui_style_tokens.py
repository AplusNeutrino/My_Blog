"""Catch invalid shared style references before they silently fall back in browsers."""
import re
import unittest
from pathlib import Path


class UIStyleTokenTest(unittest.TestCase):
    def test_shared_neutriverse_tokens_have_definitions(self):
        root = Path(__file__).resolve().parents[1]
        css = '\n'.join(p.read_text() for p in (root / 'assets/css').glob('*.css'))
        css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
        definitions = set(re.findall(r'(--nv-[\w-]+)\s*:', css))
        required = set(re.findall(r'var\(\s*(--nv-[\w-]+)\s*\)', css))
        self.assertEqual(required - definitions, set(), 'undefined UI style tokens')
