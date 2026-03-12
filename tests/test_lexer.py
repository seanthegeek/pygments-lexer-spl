import pytest
from pygments.lexers import find_lexer_class_by_name, get_lexer_for_filename, get_lexer_for_mimetype
from pygments.token import Error

from pygments_lexer_spl import SPLLexer

DEMO_FILE   = 'tests/examplefiles/demo.spl'
SAMPLE_FILE = 'tests/examplefiles/sample.spl'


class TestSPLLexer:
    def setup_method(self):
        self.lexer = SPLLexer()

    def test_finds_by_alias(self):
        assert find_lexer_class_by_name('spl') is SPLLexer

    def test_finds_by_alias_splunk(self):
        assert find_lexer_class_by_name('splunk') is SPLLexer

    def test_finds_by_alias_splunk_spl(self):
        assert find_lexer_class_by_name('splunk-spl') is SPLLexer

    def test_guesses_by_filename(self):
        assert get_lexer_for_filename('example.spl').__class__ is SPLLexer

    def test_guesses_by_mimetype(self):
        assert get_lexer_for_mimetype('text/x-spl').__class__ is SPLLexer

    def test_demo_preserves_input(self):
        demo = _load_demo()
        output = ''.join(v for _, v in self.lexer.get_tokens(demo))
        assert output == demo, 'Lexer output does not reconstruct the demo input'

    def test_sample_preserves_input(self):
        sample = _load_sample()
        output = ''.join(v for _, v in self.lexer.get_tokens(sample))
        assert output == sample, 'Lexer output does not reconstruct the sample input'

    def test_no_error_tokens_in_demo(self):
        demo = _load_demo()
        errors = _collect_errors(self.lexer, demo)
        assert not errors, f"Demo produced error tokens:\n{_format_errors(errors)}"

    def test_no_error_tokens_in_sample(self):
        sample = _load_sample()
        errors = _collect_errors(self.lexer, sample)
        assert not errors, f"Visual sample produced error tokens:\n{_format_errors(errors)}"


def _load_demo():
    return open(DEMO_FILE).read()


def _load_sample():
    return open(SAMPLE_FILE).read()


def _collect_errors(lexer, text):
    return [(t, v) for t, v in lexer.get_tokens(text) if t == Error]


def _format_errors(errors):
    return '\n'.join(f'  {v!r}' for _, v in errors)
