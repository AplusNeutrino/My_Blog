"""Exercise diagnostic filtering; this does not certify browser font rendering."""
import ast
import json
from pathlib import Path
import unittest


class FontNetworkDiagnosticsTests(unittest.TestCase):
    def helper(self):
        source=Path('tools/check_think_build_visual.py').read_text()
        tree=ast.parse(source)
        node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='font_network_events')
        namespace={'json':json}
        exec(compile(ast.Module(body=[node],type_ignores=[]),'<font-diagnostic>','exec'),namespace)
        return namespace['font_network_events'],source

    def entry(self,method,**params):
        return {'message':json.dumps({'message':{'method':method,'params':params}})}

    def test_finished_failed_and_pending_fonts_exclude_other_requests_and_headers(self):
        helper,_=self.helper()
        entries=[]
        for request_id,kind in [('done','Font'),('fail','Font'),('pending','Font'),('private','Fetch')]:
            entries.append(self.entry('Network.requestWillBeSent',requestId=request_id,type=kind,
                                      request={'url':'https://fonts.example/'+request_id,'headers':{'secret':'never-copy'}},timestamp=1))
        entries.extend([
            self.entry('Network.responseReceived',requestId='done',type='Font',timestamp=2,
                       response={'url':'https://fonts.example/done','status':200,'headers':{'secret':'never-copy'}}),
            self.entry('Network.loadingFinished',requestId='done',timestamp=3,encodedDataLength=42),
            self.entry('Network.loadingFailed',requestId='fail',timestamp=3,errorText='net::ERR_FAILED',canceled=False),
            self.entry('Network.loadingFinished',requestId='private',timestamp=3),
        ])
        result=helper(entries)
        self.assertEqual({r['requestId']:r['state'] for r in result},{'done':'finished','fail':'failed','pending':'pending'})
        self.assertNotIn('secret',json.dumps(result))
        self.assertNotIn('private',json.dumps(result))
        self.assertEqual(result[0]['encodedDataLength'],42)
        self.assertEqual(result[1]['errorText'],'net::ERR_FAILED')

    def test_wiring_keeps_original_wait_timeout_and_failure(self):
        _,source=self.helper()
        for token in ("'goog:loggingPrefs'", "driver.get_log('performance')",'unicodeRange:f.unicodeRange',
                      "failure['fontNetwork'] = font_network_events",'fontNetworkDiagnosticError',
                      'document.fonts.ready.then(() => done(true))','driver.set_script_timeout(30)'):
            self.assertIn(token,source)
        self.assertEqual(source.count('driver.set_script_timeout('),1)
        start=source.index("failure['fontNetwork']")
        end=source.index("kind = 'think'",start)
        self.assertIn('raise',source[start:end])
