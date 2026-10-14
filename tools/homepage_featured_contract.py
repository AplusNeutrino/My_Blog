"""Expected editorial/popular/latest fallback paths for the built homepage."""
from urllib.parse import quote


def expected_featured_paths(config, popular, visible_posts):
    public = [post for post in visible_posts if post.get('type') != 'fragment']
    normalize = lambda url: quote(url, safe='/%')
    paths = {normalize(post['url']) for post in public}
    latest = sorted(public, key=lambda post: post['date'], reverse=True)
    candidates = [*config['featured']['posts'], *popular.get('posts', []),
                  *(post['url'] for post in latest)]
    result = []
    for candidate in candidates:
        path = normalize(candidate)
        if path in paths and path not in result:
            result.append(path)
        if len(result) >= config['featured']['limit']:
            break
    return result
