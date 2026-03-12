#!/usr/bin/env python3
"""Visual preview server for the Splunk SPL lexer.

Requires: pip install flask   (or: pip install 'pygments-lexer-spl[server]')

Usage:
    python server.py          # Serve on http://localhost:8080
"""

from flask import Flask, Response
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.styles import get_style_by_name

from pygments_lexer_spl import SPLLexer

app = Flask(__name__)

DEMO_PATH   = 'tests/examplefiles/demo.spl'
SAMPLE_PATH = 'tests/examplefiles/sample.spl'


@app.get('/')
def index():
    lexer     = SPLLexer()
    formatter = HtmlFormatter(style=get_style_by_name('material'))
    theme_css = formatter.get_style_defs('.highlight')

    demo   = open(DEMO_PATH).read()
    sample = open(SAMPLE_PATH).read()

    highlighted_demo   = highlight(demo,   lexer, HtmlFormatter(style=get_style_by_name('material')))
    highlighted_sample = highlight(sample, lexer, HtmlFormatter(style=get_style_by_name('material')))

    body = f"""<!DOCTYPE html>
<html>
<head>
  <title>Pygments Lexer Preview: spl</title>
  <style>{theme_css} body {{ font-family: sans-serif; margin: 2em; }}</style>
</head>
<body>
  <h1>Splunk SPL Lexer Preview</h1>
  <h2>Demo</h2>
  {highlighted_demo}
  <h2>Visual Sample</h2>
  {highlighted_sample}
</body>
</html>"""

    return Response(body, mimetype='text/html')


if __name__ == '__main__':
    print('Preview at http://localhost:8080')
    app.run(port=8080, debug=True)
