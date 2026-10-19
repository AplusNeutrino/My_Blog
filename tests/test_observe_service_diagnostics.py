"""Execute actual failure reducers with privacy and scope adversarial events."""
import ast
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit


class ObserveServiceDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.source = Path('tools/check_observe_history.py').read_text()
        nodes = [n for n in ast.parse(self.source).body if isinstance(n, ast.FunctionDef)
                 and n.name in ('service_route','summarize_service_events','service_failure')]
        self.ns = {'json':json,'re':re,'urlsplit':urlsplit}
        exec(compile(ast.Module(body=nodes, type_ignores=[]), '<service-diagnostic>', 'exec'), self.ns)

    @staticmethod
    def event(method, **params):
        return {'message':json.dumps({'message':{'method':method,'params':params}})}

    def test_only_exact_public_route_and_no_query_or_userinfo(self):
        route = self.ns['service_route']
        self.assertEqual(route('https://occult-atlas.onrender.com/api/astrology/now?datetime=secret#x'),
                         'https://occult-atlas.onrender.com/api/astrology/now')
        for url in ('https://other.test/api/astrology/now',
                    'https://occult-atlas.onrender.com/other',
                    'https://user:password@occult-atlas.onrender.com/api/astrology/now',
                    'http://occult-atlas.onrender.com/api/astrology/now',
                    'https://occult-atlas.onrender.com.evil.test/api/astrology/now', None):
            self.assertIsNone(route(url))

    def test_actual_failed_event_association_is_read_only_and_redacted(self):
        events = [self.event('Network.requestWillBeSent', requestId='own', request={
            'url':'https://occult-atlas.onrender.com/api/astrology/now?private=query',
            'method':'GET','headers':{'Authorization':'secret'},'postData':'private-body'}),
            self.event('Network.requestWillBeSent', requestId='foreign', request={
                'url':'https://other.test/private','method':'POST'}),
            self.event('Network.loadingFailed', requestId='foreign', errorText='net::ERR_ABORTED'),
            self.event('Network.responseReceivedExtraInfo', requestId='own', statusCode=403,
                       headers={'Set-Cookie':'private-cookie'}),
            self.event('Network.loadingFailed', requestId='own', errorText='net::ERR_FAILED',
                       corsErrorStatus={'corsError':'MissingAllowOriginHeader','failedParameter':'private-origin'})]
        console = [{'level':'SEVERE','message':'https://occult-atlas.onrender.com/api/astrology/now?secret CORS net::ERR_FAILED'},
                   {'level':'SEVERE','message':'unrelated-private-log'}]
        result = self.ns['summarize_service_events'](events, console)
        self.assertEqual(len(result['requests']), 1)
        self.assertEqual(result['requests'][0]['events'][-1]['corsError'], 'MissingAllowOriginHeader')
        self.assertEqual(result['requests'][0]['events'][0]['status'], 403)
        self.assertTrue(result['consoleFlags'][0]['corsMentioned'])
        serialized = json.dumps(result)
        for forbidden in ('private', 'secret', 'Authorization', 'headers', 'postData', 'foreign'):
            self.assertNotIn(forbidden, serialized)

    def test_missing_or_malformed_diagnostics_do_not_imply_success(self):
        result = self.ns['summarize_service_events']([{'message':'bad-json'}], [])
        self.assertTrue(result['missingRequests'])
        self.assertEqual(result['malformedEvents'], 1)
        class Driver:
            def get_log(self, kind):
                raise RuntimeError('must-not-leak-this-body')
        result = self.ns['service_failure'](Driver())
        self.assertEqual(len(result['diagnosticErrors']), 2)
        self.assertTrue(result['missingRequests'])
        self.assertNotIn('must-not-leak', json.dumps(result))

    def test_logging_does_not_relax_or_replace_original_gate(self):
        self.assertIn("options.set_capability('goog:loggingPrefs'", self.source)
        self.assertIn("row['serviceFailure'] = service_failure(driver)", self.source)
        self.assertIn("assert data['state'] != 'error'", self.source)
        self.assertIn('WebDriverWait(driver, 55)', self.source)
        self.assertIn("row['failure'] = snapshot(driver)\n                        raise", self.source)
        for forbidden in ('Network.setRequestInterception', '--disable-web-security',
                          'getResponseBody', 'requests.get(', 'urlopen('):
            self.assertNotIn(forbidden, self.source)

    def test_malformed_event_shape_and_reducer_error_cannot_mask_failure(self):
        result = self.ns['summarize_service_events']([{'message':'{"message":null}'}], [])
        self.assertEqual(result['malformedEvents'], 1)
        def fail(*args):
            raise ValueError('private-error')
        self.ns['summarize_service_events'] = fail
        class Driver:
            def get_log(self, kind):
                return []
        result = self.ns['service_failure'](Driver())
        self.assertEqual(result['diagnosticErrors'], [{'source':'reducer','type':'ValueError'}])
        self.assertTrue(result['missingRequests'])
        self.assertNotIn('private-error', json.dumps(result))
