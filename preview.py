#!/usr/bin/env python3
"""Terminal preview of the Splunk SPL lexer.

Usage:
    python preview.py                 # Pretty-print using Terminal256 formatter
    DEBUG=1 python preview.py         # Print each token and its type
"""

import os
import sys

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.styles import get_style_by_name

from pygments_lexer_spl import SPLLexer

SAMPLE_PATH = 'tests/examplefiles/sample.spl'
DEBUG = os.environ.get('DEBUG')

sample = open(SAMPLE_PATH).read()
lexer = SPLLexer()

if DEBUG:
    for index, tokentype, value in lexer.get_tokens_unprocessed(sample):
        print(f'{tokentype!s:<45} {value!r}')
else:
    print(highlight(sample, lexer, Terminal256Formatter(style=get_style_by_name('material'))))
