# pygments-lexer-spl

[![PyPI
Package](https://img.shields.io/pypi/v/pygments-lexer-spl.svg)](https://pypi.org/project/pygments-lexer-spl/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pygments-lexer-spl?color=blue)](https://pypistats.org/packages/pygments-lexer-spl)

A Pygments lexer plugin for the Splunk Search Processing Language (SPL). Pygments is the default syntax highlighter for Sphinx (and therefore Read the Docs). This package adds
Splunk SPL support to Pygments.

## Installation

Install the package directly:

```sh
pip install pygments-lexer-spl
```

Or add it to your project's dependencies:

```toml
# pyproject.toml
[project]
dependencies = [
    "pygments-lexer-spl",
]
```

## Usage

Once installed, the lexer is automatically available to Pygments via the plugin
entry point. You can use it with any Pygments-compatible tool.

### Command line (pygmentize)

```bash
pygmentize -l spl example.spl
pygmentize -l splunk example.spl
```

### Python API

```python
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments_lexer_spl import SPLLexer

code = open('example.spl').read()
print(highlight(code, SPLLexer(), TerminalFormatter()))
```

### Terminal preview

```bash
python preview.py
DEBUG=1 python preview.py   # Print each token and its type
```

### Visual preview server

```bash
pip install 'pygments-lexer-spl[server]'
python server.py
# Then open http://localhost:8080
```

### MkDocs

Install `pygments-lexer-spl` alongside MkDocs. The lexer is picked up
automatically via the Pygments plugin entry point, so no extra configuration is
required. Use the `spl` language identifier in fenced code blocks:

````markdown
```spl
index=main sourcetype=access_combined
| stats count BY host
```
````

### Sphinx

Install `pygments-lexer-spl` in the same environment as Sphinx. The lexer
registers itself automatically, so it is available in `code-block` directives
without any additional configuration:

```rst
.. code-block:: spl

   index=main sourcetype=access_combined
   | stats count BY host
```

### Flask

Use Pygments directly to render highlighted HTML and serve it from a Flask
route:

```python
from flask import Flask
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_lexer_spl import SPLLexer

app = Flask(__name__)
formatter = HtmlFormatter()

@app.route("/highlight")
def highlight_code():
    code = open("example.spl").read()
    highlighted = highlight(code, SPLLexer(), formatter)
    css = f"<style>{formatter.get_style_defs('.highlight')}</style>"
    return css + highlighted
```

### Django

Add Pygments to your Django project and call it from a view or template tag:

```python
# views.py
from django.utils.safestring import mark_safe
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_lexer_spl import SPLLexer

formatter = HtmlFormatter()

def highlight_code(request):
    from django.shortcuts import render
    code = open("example.spl").read()
    highlighted = highlight(code, SPLLexer(), formatter)
    css = formatter.get_style_defs(".highlight")
    return render(request, "highlight.html", {
        "css": mark_safe(css),
        "code": mark_safe(highlighted),
    })
```

```html
{# highlight.html #}
<style>{{ css }}</style>
{{ code }}
```

### Colors

The lexer tells Pygments how to identify tokens. Pygments wraps each token in a
`span` tag with a `class` related to that token type. If you want to change how
the tokens are highlighted, change themes or add custom CSS.

## Supported aliases

| Alias        | Description                |
|--------------|----------------------------|
| `spl`        | Primary alias              |
| `splunk`     | Alternative alias          |
| `splunk-spl` | Fully qualified alias      |

## Development

Install dependencies:

```sh
pip install -e ".[dev,server]"
```

Run the test suite:

```sh
pytest
```

Start the visual preview server (available at http://localhost:8080):

```sh
python server.py
```

Run the terminal preview script:

```sh
python preview.py
```

Enable debug mode to print each token and its value:

```sh
DEBUG=1 python preview.py
```

## License

MIT
