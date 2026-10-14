import unittest
from pathlib import Path


class SidebarHeightTests(unittest.TestCase):
    def test_sidebar_groups_keep_intrinsic_height(self):
        css = Path('assets/css/neutriverse-sections.css').read_text()
        self.assertIn('#sidebar {\n  overflow-y: auto;', css)
        self.assertIn('#sidebar .profile-wrapper,\n#sidebar .nv-sidebar-navigation,\n#sidebar .sidebar-bottom {\n  flex-shrink: 0;', css)


if __name__ == '__main__':
    unittest.main()
