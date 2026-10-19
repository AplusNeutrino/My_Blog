#!/usr/bin/env python3
"""Parse the actual compressed like scripts, not just their source templates."""
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current = None
        self.likes = []

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.current = ''

    def handle_data(self, data):
        if self.current is not None:
            self.current += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            if '__neutriverseLikesReady' in self.current:
                self.likes.append(self.current)
            self.current = None


def validate(text, expected):
    parser = Scripts()
    parser.feed(text)
    if len(parser.likes) != expected:
        raise AssertionError(f'Expected {expected} like scripts, found {len(parser.likes)}')
    for index, script in enumerate(parser.likes):
        result = subprocess.run(['node', '--check'], input=script, text=True,
                                capture_output=True)
        if result.returncode:
            raise AssertionError(f'Compressed like script {index + 1}: {result.stderr}')


def main():
    site = Path(sys.argv[1])
    validate((site / 'thoughts/index.html').read_text(encoding='utf-8'), 5)
    posts = sorted(site.glob('posts/*/index.html'))
    for path in posts:
        text = path.read_text(encoding='utf-8')
        if 'data-post-like' in text:
            validate(text, 1)
            print(f'Like scripts parse after production compression: Thoughts x5 and {path}')
            return
    raise AssertionError('No built public article with likes found')


if __name__ == '__main__':
    main()
