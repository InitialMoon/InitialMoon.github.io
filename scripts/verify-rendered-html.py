#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys

pages = [
    Path('public/index.html'),
    Path('public/zh/index.html'),
    Path('public/projects/anfluid/index.html'),
    Path('public/zh/projects/anfluid/index.html'),
    Path('public/publications/anfluid/index.html'),
    Path('public/zh/publications/anfluid/index.html'),
]

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._current_href = None
        self._current_text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self._current_href = dict(attrs).get('href', '')
            self._current_text = []

    def handle_data(self, data):
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self._current_href is not None:
            text = ' '.join(''.join(self._current_text).split())
            self.links.append((text, self._current_href))
            self._current_href = None
            self._current_text = []

failed = False
for page in pages:
    if not page.exists():
        print(f'MISSING {page}')
        failed = True
        continue
    html = page.read_text(errors='replace')
    if '__hdeferred' in html:
        print(f'FAIL {page}: contains unresolved Hugo deferred placeholder')
        failed = True
    if '/css/_entry' not in html:
        print(f'FAIL {page}: missing HugoBlox Tailwind CSS link')
        failed = True

    parser = LinkParser()
    parser.feed(html)
    for text, href in parser.links:
        if text in {'English', '中文 (简体)'} and href.startswith('https://initialmoon.github.io'):
            print(f'FAIL {page}: language switcher uses absolute production URL {href}')
            failed = True

if failed:
    sys.exit(1)
print('Rendered HTML verification passed')
