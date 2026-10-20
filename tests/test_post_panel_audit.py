"""UI-026 regressions; these do not constitute browser/visual acceptance."""
import ast
from pathlib import Path
import unittest


class PostPanelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=Path('tools/check_post_panel.py').read_text()
        tree=ast.parse(cls.source)
        function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='assert_clear')
        scope={}
        exec(compile(ast.Module(body=[function],type_ignores=[]),'<actual assert_clear>','exec'),scope)
        cls.check=staticmethod(scope['assert_clear'])

    def valid(self):
        return dict(linkCount=10,docWidth=1366,width=1366,buttonVisible=True,clearance=True,covered=[])

    def test_actual_assertion_accepts_clear_panel(self):
        self.check(self.valid())

    def test_actual_assertion_rejects_confirmed_date_covered_by_button(self):
        data=self.valid();data['covered']=[{'index':7,'char':'6'}]
        with self.assertRaises(AssertionError):
            self.check(data)

    def test_actual_assertion_rejects_old_full_height_even_between_text_rows(self):
        data=self.valid();data['clearance']=False
        with self.assertRaises(AssertionError):
            self.check(data)

    def test_actual_assertion_rejects_missing_links_hidden_button_and_overflow(self):
        for key,value in [('linkCount',0),('buttonVisible',False),('docWidth',1400)]:
            with self.subTest(key=key):
                data=self.valid();data[key]=value
                with self.assertRaises(AssertionError):self.check(data)

    def test_css_only_limits_desktop_reading_stack(self):
        css=Path('assets/css/NormaiNight.css').read_text()
        block=css[css.index('/* UI-026:'):css.index('#post-panel-stack #toc-wrapper')]
        self.assertIn('@media (min-width: 1200px)',block)
        self.assertIn('max-height: calc(100vh - 10rem)',block)
        self.assertEqual(block.count('max-height:'),1)
        for forbidden in ('display:', 'font-size:', '#back-to-top', 'position:', 'padding:'):
            self.assertNotIn(forbidden,block)
        self.assertIn('overflow-y: auto;',css[css.index('#post-panel-stack {'):css.index('/* UI-026:')])

    def test_real_input_text_ranges_and_fault_detection_are_not_removed(self):
        for token in ('document.createTreeWalker','document.createRange()','range.getClientRects()',
                      'document.elementFromPoint(x,y)','button.contains(hit)',
                      'ScrollOrigin.from_viewport','scroll_from_origin',
                      "seen==set(range(10))", "'oldHeightRejected'",'max-height:100vh!important',
                      "driver.find_element(By.ID,'back-to-top').click()",'return scrollY<=1',
                      "for width in (1366,1920)","for height in (900,640)",
                      "for theme in ('dark','light')"):
            self.assertIn(token,self.source)
        capture=self.source[self.source.index('def capture('):self.source.index('def exercise(')]
        self.assertLess(capture.index('save_screenshot'),capture.index('assert_clear'))
        self.assertIn('raise\n',self.source)
        for forbidden in ('requests.get', 'fetch(', 'Network.setBlockedURLs', 'setDocumentContent'):
            self.assertNotIn(forbidden,self.source)

    def test_production_and_live_both_upload_separate_evidence(self):
        workflow=Path('.github/workflows/pages-deploy.yml').read_text()
        self.assertEqual(workflow.count('run: python tools/check_post_panel.py'),2)
        for token in ('neutriverse-post-panel-${{ github.sha }}',
                      'neutriverse-live-post-panel-${{ github.sha }}',
                      'run: python tools/check_observe_dialog.py',
                      'run: python tools/check_think_build_visual.py'):
            self.assertIn(token,workflow)


if __name__=='__main__':unittest.main()
