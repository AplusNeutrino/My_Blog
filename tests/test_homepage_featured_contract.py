import unittest
from tools.homepage_featured_contract import expected_featured_paths


class FeaturedContractTest(unittest.TestCase):
    def test_popular_updates_preserve_editorial_prefix_and_exact_order(self):
        config = {'featured': {'posts': ['/a'], 'limit': 3}}
        posts = [{'url': '/' + x, 'date': str(i), 'type': 'note'}
                 for i, x in enumerate('abcd')]
        self.assertEqual(expected_featured_paths(config, {'posts': ['/b', '/c']}, posts),
                         ['/a', '/b', '/c'])
        self.assertEqual(expected_featured_paths(config, {'posts': ['/d', '/b']}, posts),
                         ['/a', '/d', '/b'])

    def test_missing_hidden_fragments_and_duplicates_do_not_enter(self):
        config = {'featured': {'posts': ['/hidden', '/a'], 'limit': 3}}
        posts = [{'url': '/a', 'date': '1', 'type': 'essay'},
                 {'url': '/b', 'date': '2', 'type': 'note'},
                 {'url': '/c', 'date': '3', 'type': 'note'},
                 {'url': '/thoughts/#f', 'date': '4', 'type': 'fragment'}]
        self.assertEqual(expected_featured_paths(config,
                         {'posts': ['/a', '/missing', '/thoughts/#f']}, posts),
                         ['/a', '/c', '/b'])

    def test_encoded_public_paths_match_source_paths(self):
        config = {'featured': {'posts': ['/posts/%E4%B8%AD/'], 'limit': 1}}
        self.assertEqual(expected_featured_paths(config, {},
                         [{'url': '/posts/中/', 'date': '1', 'type': 'note'}]),
                         ['/posts/%E4%B8%AD/'])
