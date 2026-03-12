# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-12

### Added

- Initial release of the `pygments-lexer-spl` package
- `SPLLexer` lexer with aliases `spl`, `splunk`, `splunk-spl`,
  filename extension `.spl`, and MIME type `text/x-spl`
- Auto-detection heuristics based on common SPL patterns (`| stats`, `| eval`,
  `sourcetype=`, `index=`)

#### Commands

- 157 SPL commands including aliases (`bucket`/`bin`, `ctable`/`contingency`,
  `kv`/`extract`, `script`/`run`, `msearch`/`mpreview`)

#### Functions

- Bitwise functions: `bit_and`, `bit_or`, `bit_not`, `bit_xor`,
  `bit_shift_left`, `bit_shift_right`
- Comparison and conditional functions: `case`, `cidrmatch`, `coalesce`, `if`,
  `in`, `like`, `match`, `nullif`, `searchmatch`, `validate`
- Conversion functions: `ipmask`, `printf`, `toarray`, `tobool`, `todouble`,
  `toint`, `tomv`, `tonumber`, `toobject`, `tostring`
- Cryptographic functions: `md5`, `sha1`, `sha256`, `sha512`
- Date and time functions: `now`, `relative_time`, `strftime`, `strptime`, `time`
- Informational functions: `isarray`, `isbool`, `isdouble`, `isint`, `ismv`,
  `isnotnull`, `isnull`, `isnum`, `isobject`, `isstr`, `typeof`
- JSON functions: `json`, `json_object`, `json_append`, `json_array`,
  `json_array_to_mv`, `json_delete`, `json_entries`, `json_extend`,
  `json_extract`, `json_extract_exact`, `json_has_key_exact`, `json_keys`,
  `json_set`, `json_set_exact`, `json_valid`
- Mathematical functions: `abs`, `ceiling`/`ceil`, `exact`, `exp`, `floor`,
  `ln`, `log`, `pi`, `pow`, `round`, `sigfig`, `sqrt`, `sum`
- Multivalue eval functions: `commands`, `mvappend`, `mvcount`, `mvdedup`,
  `mvfilter`, `mvfind`, `mvindex`, `mvjoin`, `mvmap`, `mvrange`, `mvreverse`,
  `mvsort`, `mvzip`, `mv_to_json_array`, `split`
- Statistical eval functions: `avg`, `max`, `min`, `random`
- Text functions: `len`/`length`, `lower`, `ltrim`, `replace`, `rtrim`,
  `spath`, `substr`, `trim`, `upper`, `urldecode`
- Trigonometric and hyperbolic functions: `acos`, `acosh`, `asin`, `asinh`,
  `atan`, `atan2`, `atanh`, `cos`, `cosh`, `hypot`, `sin`, `sinh`, `tan`, `tanh`
- Aggregate stats functions: `avg`, `c`/`count`, `dc`/`distinct_count`,
  `estdc`, `estdc_error`, `max`, `mean`, `median`, `min`, `mode`, `range`,
  `stdev`, `stdevp`, `sum`, `sumsq`, `var`, `varp`,
  `perc<N>`/`p<N>`, `exactperc<N>`, `upperperc<N>`
- Event order functions: `first`, `last`
- Multivalue stats functions: `list`, `values`
- Time stats functions: `earliest`, `earliest_time`, `latest`, `latest_time`,
  `per_day`, `per_hour`, `per_minute`, `per_second`, `rate`, `rate_avg`,
  `rate_sum`

[0.1.0]: https://github.com/seanthegeek/pygments-lexer-spl/releases/tag/v0.1.0
