#!/usr/bin/env python

from enum import Enum, auto
from io import StringIO

from lxml import html

out_html = html.fromstring(open('test_fixtures/Kolkka/out').read())
in_wiki_f = open('test_fixtures/Kolkka/in')

class TokenType(Enum):
    BOLD = auto()

def get_tokens(f):
    last_token = None
    cur_buf = ''
    while True:
        cur_buf += f.read(1)
        if cur_buf == '':
            break
        if cur_buf == "'":
            cur_buf += f.read(2)
            if cur_buf == "'''":
                yield TokenType.BOLD
                cur_buf = ''
        else:
            yield cur_buf
            cur_buf = ''

print(list(get_tokens(in_wiki_f)))
