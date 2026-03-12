"""Pygments lexer for Splunk Search Processing Language (SPL)."""

from pygments.lexer import RegexLexer, words
from pygments.token import (
    Keyword, Name, Number, Operator, Punctuation, String, Whitespace,
)

# SPL commands (case-insensitive)
COMMANDS = (
    'abstract', 'accum', 'addcoltotals', 'addinfo', 'addtotals',
    'analyzefields', 'anomalies', 'anomalousvalue', 'anomalydetection',
    'append', 'appendcols', 'appendpipe', 'arules', 'associate',
    'autoregress', 'awssnsalert',
    'bin', 'bucket', 'bucketdir',
    'chart', 'cluster', 'cofilter', 'collect', 'concurrency',
    'contingency', 'convert', 'correlate', 'ctable',
    'datamodel', 'datamodelsimple', 'dbinspect', 'dbxquery', 'dedup',
    'delete', 'delta', 'diff',
    'entitymerge', 'erex', 'eval', 'eventcount', 'eventstats',
    'extract',
    'fieldformat', 'fields', 'fieldsummary', 'filldown', 'fillnull',
    'findtypes', 'folderize', 'foreach', 'format', 'from', 'fromjson',
    'gauge', 'gentimes', 'geom', 'geomfilter', 'geostats',
    'head', 'highlight', 'history',
    'iconify', 'ingestpreview', 'inputcsv', 'inputintelligence',
    'inputlookup', 'iplocation',
    'join',
    'kmeans', 'kv', 'kvform',
    'loadjob', 'localize', 'localop', 'lookup',
    'makecontinuous', 'makemv', 'makeresults', 'map', 'mcollect',
    'metadata', 'metasearch', 'meventcollect', 'mpreview', 'msearch',
    'mstats', 'multikv', 'multisearch', 'mvcombine', 'mvexpand',
    'nomv',
    'outlier', 'outputcsv', 'outputlookup', 'outputtext', 'overlap',
    'pivot', 'predict',
    'rangemap', 'rare', 'redistribute', 'regex', 'reltime', 'rename',
    'replace', 'require', 'rest', 'return', 'reverse', 'rex',
    'rtorder', 'run',
    'savedsearch', 'script', 'scrub', 'search', 'searchtxn',
    'selfjoin', 'sendalert', 'sendemail', 'set', 'setfields',
    'sichart', 'sirare', 'sistats', 'sitimechart', 'sitop',
    'snowevent', 'snoweventstream', 'snowincident', 'snowincidentstream',
    'sort', 'spath', 'stats', 'strcat', 'streamstats',
    'table', 'tags', 'tail', 'timechart', 'timewrap', 'tojson',
    'top', 'transaction', 'transpose', 'trendline', 'tscollect',
    'tstats', 'typeahead', 'typelearner', 'typer',
    'union', 'uniq', 'untable',
    'walklex', 'where',
    'x11', 'xmlkv', 'xmlunescape', 'xpath', 'xyseries',
)

# Clause keywords (case-insensitive)
CLAUSE_KEYWORDS = (
    'as', 'by', 'over', 'output', 'outputnew',
)

# Built-in functions: eval functions + stats/charting functions
FUNCTIONS = (
    # Bitwise
    'bit_and', 'bit_or', 'bit_not', 'bit_xor',
    'bit_shift_left', 'bit_shift_right',
    # Comparison and Conditional
    'case', 'cidrmatch', 'coalesce', 'if', 'in', 'like', 'match',
    'nullif', 'searchmatch', 'validate',
    # Conversion
    'ipmask', 'printf', 'toarray', 'tobool', 'todouble', 'toint',
    'tomv', 'tonumber', 'toobject', 'tostring',
    # Cryptographic
    'md5', 'sha1', 'sha256', 'sha512',
    # Date and Time
    'now', 'relative_time', 'strftime', 'strptime', 'time',
    # Informational
    'isarray', 'isbool', 'isdouble', 'isint', 'ismv', 'isnotnull',
    'isnull', 'isnum', 'isobject', 'isstr', 'typeof',
    # JSON
    'json', 'json_object', 'json_append', 'json_array',
    'json_array_to_mv', 'json_delete', 'json_entries', 'json_extend',
    'json_extract', 'json_extract_exact', 'json_has_key_exact',
    'json_keys', 'json_set', 'json_set_exact', 'json_valid',
    # Mathematical
    'abs', 'ceiling', 'ceil', 'exact', 'exp', 'floor', 'ln', 'log',
    'pi', 'pow', 'round', 'sigfig', 'sqrt',
    # Multivalue eval
    'commands', 'mvappend', 'mvcount', 'mvdedup', 'mvfilter',
    'mvfind', 'mvindex', 'mvjoin', 'mvmap', 'mvrange', 'mvreverse',
    'mvsort', 'mvzip', 'mv_to_json_array', 'split',
    # Statistical eval
    'avg', 'max', 'min', 'random',
    # Text
    'len', 'length', 'lower', 'ltrim', 'rtrim', 'substr', 'trim',
    'upper', 'urldecode',
    # Trig and Hyperbolic
    'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh',
    'cos', 'cosh', 'hypot', 'sin', 'sinh', 'tan', 'tanh',
    # Stats - Aggregate
    'c', 'count', 'dc', 'distinct_count', 'estdc', 'estdc_error',
    'mean', 'median', 'mode', 'range', 'stdev', 'stdevp', 'sum',
    'sumsq', 'var', 'varp',
    # Stats - Event order
    'first', 'last',
    # Stats - Multivalue
    'list', 'values',
    # Stats - Time
    'earliest', 'earliest_time', 'latest', 'latest_time',
    'per_day', 'per_hour', 'per_minute', 'per_second',
    'rate', 'rate_avg', 'rate_sum',
    # Search directives
    'term',
)

# Boolean/null constants
CONSTANTS = (
    'true', 'false', 'null',
)

# Built-in fields and variables
BUILTIN_FIELDS = (
    '_time', '_raw', '_indextime',
    'source', 'sourcetype', 'host', 'index',
    'splunk_server', 'linecount', 'eventtype',
)


class SPLLexer(RegexLexer):
    """Pygments lexer for Splunk Search Processing Language (SPL)."""

    name = 'Splunk SPL'
    url = 'https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/introduction/understanding-spl-syntax'
    aliases = ['spl', 'splunk', 'splunk-spl']
    filenames = ['*.spl']
    mimetypes = ['text/x-spl']

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Whitespace),

            # Double-quoted strings
            (r'"', String.Double, 'string-double'),

            # Backtick macro references: `macro_name` or `macro(args)`
            (r'`[^`]*`', Name.Function),

            # Macro argument substitution: $variable$
            (r'\$[a-zA-Z_]\w*\$', Name.Variable),

            # Standalone dollar sign
            (r'\$', Operator),

            # Float literals (before integers)
            (r'\d+\.\d+', Number.Float),

            # Integer literals
            (r'\d+', Number.Integer),

            # Boolean operators (case-sensitive, must be uppercase)
            (r'\b(?:AND|OR|NOT|XOR)\b', Keyword.Pseudo),

            # Boolean/null constants (case-insensitive)
            (words(CONSTANTS, prefix=r'(?i)\b', suffix=r'\b'), Keyword.Constant),

            # Clause keywords (case-insensitive)
            (words(CLAUSE_KEYWORDS, prefix=r'(?i)\b', suffix=r'\b'),
             Keyword.Pseudo),

            # Parameterized stats functions: perc<N>, exactperc<N>,
            # upperperc<N>, p<N>
            (r'(?i)\b(?:perc|exactperc|upperperc|p)\d+\b', Name.Builtin),

            # Commands (case-insensitive)
            (words(COMMANDS, prefix=r'(?i)\b', suffix=r'\b'), Keyword),

            # Built-in functions (case-insensitive)
            (words(FUNCTIONS, prefix=r'(?i)\b', suffix=r'\b'), Name.Builtin),

            # Built-in fields
            (words(BUILTIN_FIELDS, prefix=r'\b', suffix=r'\b'),
             Name.Variable.Magic),

            # Multi-character comparison operators
            (r'!=|<=|>=', Operator),

            # Single-character operators
            (r'[=<>+\-*/%@.]', Operator),

            # Punctuation
            (r'[|(),\[\]{}]', Punctuation),
            (r':', Punctuation),

            # Identifiers (field names, etc.)
            (r'[a-zA-Z_]\w*', Name),
        ],

        'string-double': [
            (r'\\[\\"|]', String.Escape),
            (r'\\', String.Double),  # unrecognized escapes pass through
            (r'[^"\\]+', String.Double),
            (r'"', String.Double, '#pop'),
        ],
    }

    def analyze_text(self, text: str) -> float:
        score = 0.0
        if '| stats ' in text or '| eval ' in text:
            score += 0.3
        if '| table ' in text or '| where ' in text:
            score += 0.2
        if 'sourcetype=' in text or 'index=' in text:
            score += 0.2
        if '| sort ' in text or '| head ' in text:
            score += 0.1
        return min(score, 1.0)
