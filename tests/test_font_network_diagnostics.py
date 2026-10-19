"""Exercise diagnostic filtering; this does not certify browser font rendering."""
import ast
import base64
import json
import re
from pathlib import Path
import unittest
from urllib.parse import urlsplit


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

    def sources_helper(self):
        source = Path('tools/check_think_build_visual.py').read_text()
        node = next(n for n in ast.parse(source).body
                    if isinstance(n, ast.FunctionDef) and n.name == 'font_face_sources')
        namespace = {'json': json, 'base64': base64, 're': re, 'urlsplit': urlsplit}
        exec(compile(ast.Module(body=[node], type_ignores=[]), '<font-sources>', 'exec'), namespace)
        return namespace['font_face_sources'], source

    def stylesheet(self, request_id='css', url='https://fonts.googleapis.com/css2?family=Noto+Sans+SC'):
        return self.entry('Network.responseReceived', requestId=request_id, type='Stylesheet',
                          response={'url': url})

    def test_actual_parser_links_variable_weights_unicode_sources_and_cache_metadata(self):
        helper, _ = self.sources_helper()
        css = '''@font-face {font-family:'Noto Sans SC';font-style:normal;
          font-weight:100 900;src:url(https://fonts.gstatic.com/s/font.woff2) format('woff2');
          unicode-range:U+7722, U+7726;}
        @font-face {font-family:'Noto Sans SC';font-style:normal;font-weight:400;
          src:url(https://fonts.gstatic.com/s/other.woff2);unicode-range:U+4E00;}
        @font-face {font-family:'Other';font-weight:400;
          src:url(https://fonts.gstatic.com/s/other.woff2);unicode-range:U+7722,U+7726;}'''
        class Driver:
            calls = []
            def execute_cdp_cmd(self, command, params):
                self.calls.append((command, params))
                return {'body': base64.b64encode(css.encode()).decode(), 'base64Encoded': True}
        driver = Driver()
        faces = [{'family':'Noto Sans SC','style':'normal','weight':str(w),
                  'unicodeRange':'u+7722,u+7726','status':'loading'} for w in (400, 500, 600)]
        faces.append({**faces[0], 'status':'loaded'})
        network = [{'url':'https://fonts.gstatic.com/s/font.woff2','state':'finished',
                    'requestServedFromCache':True}]
        resource = [{'name':network[0]['url'],'transferSize':0}]
        result = helper(driver, [self.stylesheet()], faces, resource, network)
        self.assertEqual(len(result['loadingFaces']), 3)
        for row in result['loadingFaces']:
            self.assertEqual(row['matchCount'], 1)
            self.assertEqual(row['candidates'][0]['network'], network)
            self.assertEqual(row['candidates'][0]['resources'], resource)
        self.assertEqual(driver.calls, [('Network.getResponseBody', {'requestId':'css'})])
        self.assertIn('do not establish root cause', result['interpretation'])

    def test_body_allowlist_missing_body_and_ambiguity_are_not_silenced(self):
        helper, _ = self.sources_helper()
        class Driver:
            calls = []
            def execute_cdp_cmd(self, command, params):
                self.calls.append(params['requestId'])
                if params['requestId'] == 'evicted':
                    raise RuntimeError('sensitive error detail must not be copied')
                return {'body': "@font-face {font-family:X;src:url(https://fonts.gstatic.com/x);}" * 2}
        driver = Driver()
        entries = [self.stylesheet('private', 'https://example.test/private.css'),
                   self.stylesheet('spoof', 'https://fonts.googleapis.com.evil.test/css2'),
                   self.stylesheet('auth', 'https://user:secret@fonts.googleapis.com/css2'),
                   self.stylesheet('other', 'https://fonts.googleapis.com/not-css'),
                   self.stylesheet('css'), self.stylesheet('css'), self.stylesheet('evicted')]
        faces = [{'family':'X','weight':'400','style':'normal', 'unicodeRange':'U+0-10FFFF','status':'loading'},
                 {'family':'Missing','weight':'400','style':'normal','unicodeRange':'U+0-10FFFF','status':'loading'}]
        result = helper(driver, entries, faces, [], [])
        self.assertEqual(driver.calls, ['css', 'evicted'])
        self.assertEqual([r['matchCount'] for r in result['loadingFaces']], [2, 0])
        self.assertEqual(result['stylesheets'][1]['bodyReadError'], 'RuntimeError')
        self.assertFalse(result['stylesheets'][1]['bodyRead'])
        self.assertNotIn('sensitive', json.dumps(result))
        self.assertNotIn('secret', json.dumps(result))

    def test_served_from_cache_event_preserved_without_copying_unrelated_request(self):
        helper, _ = self.helper()
        events = [self.entry('Network.requestServedFromCache', requestId='font'),
                  self.entry('Network.requestServedFromCache', requestId='private'),
                  self.entry('Network.requestWillBeSent',requestId='font',type='Font',
                             request={'url':'https://fonts.gstatic.com/f.woff2'}),
                  self.entry('Network.responseReceived',requestId='font',type='Font',loaderId='nav',
                             response={'url':'https://fonts.gstatic.com/f.woff2','status':200,
                                       'fromServiceWorker':False,'fromDiskCache':False})]
        result = helper(events)
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0]['requestServedFromCache'])
        self.assertFalse(result[0]['fromDiskCache'])
        self.assertEqual(result[0]['loaderId'], 'nav')

    def test_sources_diagnostic_only_runs_after_original_failure_without_network_or_dom_writes(self):
        _, source = self.sources_helper()
        function = ast.get_source_segment(source, next(n for n in ast.parse(source).body
            if isinstance(n, ast.FunctionDef) and n.name == 'font_face_sources'))
        self.assertNotIn('execute_script', function)
        self.assertNotIn('execute_async_script', function)
        commands = re.findall(r"execute_cdp_cmd\('([^']+)'", function)
        self.assertEqual(commands, ['Network.getResponseBody'])
        failure = source[source.index('except Exception:\n                            driver.save_screenshot'):]
        self.assertIn("failure['fontFaceSources'] = font_face_sources(", failure)
        self.assertLess(failure.index("failure['fontFaceSources']"), failure.index('\n                            raise'))
