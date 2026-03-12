# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## Commands

```sh
pip install -e ".[dev,server]"  # Install dependencies
pytest                           # Run the test suite (default task)
python server.py                 # Start visual preview server at http://localhost:8080
python preview.py                # Terminal preview using github-dark style
DEBUG=1 python preview.py        # Print each token and its type
```

To check for error tokens via the preview server:

```sh
curl -s http://localhost:8080 | grep 'class="err"'
```

## Architecture

This is a Pygments lexer plugin package for Splunk Search Processing Language (SPL). Pygments is
the default syntax highlighter used by Sphinx/Read the Docs.

### Key files

- [pygments_lexer_spl/_lexer.py](pygments_lexer_spl/_lexer.py) — The lexer implementation (`SPLLexer(RegexLexer)`)
- [pygments_lexer_spl/__init__.py](pygments_lexer_spl/__init__.py) — Entry point that re-exports the lexer class; this is what consumers import
- [tests/test_lexer.py](tests/test_lexer.py) — pytest test suite
- [tests/examplefiles/demo.spl](tests/examplefiles/demo.spl) — Short demo snippet used in tests
- [tests/examplefiles/sample.spl](tests/examplefiles/sample.spl) — Comprehensive sample used for visual testing and error-token checks

__Lexer structure:__ The lexer uses module-level tuples for keyword classification,
passed to `words()` inline in the `tokens` dict. The `'root'` state matches tokens
in priority order. Sub-states handle strings and any other paired constructs.

## Splunk SPL references

Use *ONLY* official documentation, *NOT* from memory, training, or inference.

### Splunk Documentation

__MANDATORY: Before writing or modifying the lexer, you MUST fetch and read every
URL in this list.__ This is not background reading — it is a required prerequisite
step. Fetch each page, extract the keywords or function names, and verify them
against the lexer before declaring any work complete.

Do not use the quick-reference or overview pages as a substitute for the individual detail pages. The quick-reference pages omit aliases (e.g. `ceil` for `ceiling`, `average` for `avg`, `c` for `count`), secondary functions, and command-specific keywords that only appear on the detail pages. Every page in this list exists because it contains information not fully captured elsewhere.

- Understanding SPL syntax <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/introduction/understanding-spl-syntax>
- How to use this manual <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/introduction/how-to-use-this-manual>
- Splunk Quick Reference Guide <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/quick-reference/splunk-quick-reference-guide>
- Command quick reference <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/quick-reference/command-quick-reference>
- Commands by category <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/quick-reference/commands-by-category>
- Command types <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/quick-reference/command-types>
- Evaluation functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/evaluation-functions>
- Bitwise functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/bitwise-functions>
- Comparison and Conditional functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/comparison-and-conditional-functions>
- Conversion functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/conversion-functions>
- Cryptographic functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/cryptographic-functions>
- Date and Time functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/date-and-time-functions>
- Informational functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/informational-functions>
- JSON functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/json-functions>
- Mathematical functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/mathematical-functions>
- Multivalue eval functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/multivalue-eval-functions>
- Statistical eval functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions>
- Text functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/text-functions>
- Trig and Hyperbolic functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/evaluation-functions/trig-and-hyperbolic-functions>
- Statistical and charting functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/statistical-and-charting-functions/statistical-and-charting-functions>
- Aggregate functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/statistical-and-charting-functions/aggregate-functions>
- Event order functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/statistical-and-charting-functions/event-order-functions>
- Multivalue stats and chart functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/statistical-and-charting-functions/multivalue-stats-and-chart-functions>
- Time functions <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/statistical-and-charting-functions/time-functions>
- Date and time format variables <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/time-format-variables-and-modifiers/date-and-time-format-variables>
- Time modifiers <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers>
- abstract <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/abstract>
- accum <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/accum>
- addcoltotals <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/addcoltotals>
- addinfo <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/addinfo>
- addtotals <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/addtotals>
- analyzefields <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/analyzefields>
- anomalies <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/anomalies>
- anomalousvalue <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/anomalousvalue>
- anomalydetection <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/anomalydetection>
- append <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/append>
- appendcols <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/appendcols>
- appendpipe <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/appendpipe>
- arules <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/arules>
- associate <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/associate>
- autoregress <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/autoregress>
- awssnsalert <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/awssnsalert>
- bin <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/bin>
- bucket <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/bucket>
- bucketdir <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/bucketdir>
- chart <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/chart>
- cluster <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/cluster>
- cofilter <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/cofilter>
- collect <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/collect>
- concurrency <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/concurrency>
- contingency <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/contingency>
- convert <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/convert>
- correlate <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/correlate>
- ctable <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/ctable>
- datamodel <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/datamodel>
- datamodelsimple <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/datamodelsimple>
- dbinspect <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/dbinspect>
- dbxquery <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/dbxquery>
- dedup <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/dedup>
- delete <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/delete>
- delta <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/delta>
- diff <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/diff>
- entitymerge <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/entitymerge>
- erex <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/erex>
- eval <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/eval>
- eventcount <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/eventcount>
- eventstats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/eventstats>
- extract <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/extract>
- fieldformat <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/fieldformat>
- fields <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/fields>
- fieldsummary <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/fieldsummary>
- filldown <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/filldown>
- fillnull <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/fillnull>
- findtypes <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/findtypes>
- folderize <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/folderize>
- foreach <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/foreach>
- format <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/format>
- from <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/from>
- fromjson <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/fromjson>
- gauge <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/gauge>
- gentimes <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/gentimes>
- geom <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/geom>
- geomfilter <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/geomfilter>
- geostats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/geostats>
- head <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/head>
- highlight <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/highlight>
- history <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/history>
- iconify <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/iconify>
- ingestpreview <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/ingestpreview>
- inputcsv <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/inputcsv>
- inputintelligence <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/inputintelligence>
- inputlookup <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/inputlookup>
- iplocation <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/iplocation>
- join <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/join>
- kmeans <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/kmeans>
- kvform <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/kvform>
- loadjob <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/loadjob>
- localize <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/localize>
- localop <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/localop>
- lookup <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/lookup>
- makecontinuous <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/makecontinuous>
- makemv <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/makemv>
- makeresults <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/makeresults>
- map <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/map>
- mcollect <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/mcollect>
- metadata <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/metadata>
- metasearch <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/metasearch>
- meventcollect <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/meventcollect>
- mpreview <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/mpreview>
- msearch <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/msearch>
- mstats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/mstats>
- multikv <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/multikv>
- multisearch <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/multisearch>
- mvcombine <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/mvcombine>
- mvexpand <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/mvexpand>
- nomv <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/nomv>
- outlier <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/outlier>
- outputs <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/outputcsv>
- outputlookup <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/outputlookup>
- outputtext <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/outputtext>
- overlap <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/overlap>
- pivot <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/pivot>
- predict <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/predict>
- rangemap <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rangemap>
- rare <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rare>
- regex <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/regex>
- reltime <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/reltime>
- rename <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rename>
- replace <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/replace>
- require <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/require>
- rest <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rest>
- return <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/return>
- reverse <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/reverse>
- rex <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rex>
- rtorder <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/rtorder>
- run <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/run>
- savedsearch <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/savedsearch>
- script <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/script>
- scrub <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/scrub>
- search <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/search>
- searchtxn <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/searchtxn>
- selfjoin <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/selfjoin>
- sendalert <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sendalert>
- sendemail <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sendemail>
- set <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/set>
- setfields <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/setfields>
- sichart <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sichart>
- sirare <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sirare>
- sistats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sistats>
- sitimechart <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sitimechart>
- sitop <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sitop>
- snowincident <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/snowincident>
- snowincidentstream <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/snowincidentstream>
- snowevent <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/snowevent>
- snoweventstream <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/snoweventstream>
- sort <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/sort>
- spath <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/spath>
- stats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/stats>
- strcat <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/strcat>
- streamstats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/streamstats>
- table <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/table>
- tags <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/tags>
- tail <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/tail>
- timechart <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/timechart>
- timewrap <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/timewrap>
- tojson <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/tojson>
- top <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/top>
- transaction <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/transaction>
- transpose <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/transpose>
- trendline <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/trendline>
- tscollect <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/tscollect>
- tstats <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/tstats>
- typeahead <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/typeahead>
- typelearner <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/typelearner>
- typer <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/typer>
- union <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/union>
- uniq <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/uniq>
- untable <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/untable>
- walklex <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/walklex>
- where <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/where>
- x11 <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/x11>
- xmlkv <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/xmlkv>
- xmlunescape <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/xmlunescape>
- xpath <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/xpath>
- xyseries <https://docs.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.2/search-commands/xyseries>

## Pygments references

- Lexer development guide: <https://pygments.org/docs/lexerdevelopment/>
- Existing lexers for reference: <https://github.com/pygments/pygments/tree/master/pygments/lexers>
- JSON/data lexer (simple example): <https://github.com/pygments/pygments/blob/master/pygments/lexers/data.py>
- SQL lexer (keyword-heavy analog): <https://github.com/pygments/pygments/blob/master/pygments/lexers/sql.py>
- Token types: <https://pygments.org/docs/tokens/>

## Fetching documentation

Always use `help.splunk.com` URLs — direct `docs.splunk.com` URLs return 403.

### Parsing the HTML

__Always save to a file first__ — piping curl output directly into Python via `|` results in empty stdin. Save with `-o`, then open the file in Python.

Pages contain a large navigation sidebar that repeats command and function names before the article body. Skip past it by searching for a marker that only appears in the article content (e.g. the second occurrence of a section heading, or a phrase like `"Splunk Enterprise › Search ›"`).

Recommended extraction pattern:

```python
import re
with open('/tmp/page.html', 'r', errors='replace') as f:
    html = f.read()
text = re.sub(r'<[^>]+>', ' ', html)   # strip tags
text = re.sub(r'&#?\w+;', ' ', text)   # strip HTML entities
text = re.sub(r'\s+', ' ', text)        # normalise whitespace

# Skip the nav — find content after the breadcrumb marker
idx = text.find('Splunk Enterprise › Search ›')
if idx < 0:
    idx = 0
print(text[idx:idx+10000])
```

Alternatively, find the __second__ occurrence of a known section heading (the first is in the nav, the second is the article):

```python
marker = 'Aggregate functions'
idx = text.find(marker)
idx = text.find(marker, idx + 1)  # skip nav occurrence
print(text[idx:idx+8000])
```

## SPL lexer gotchas

These mistakes are easy to make and will cause error tokens or incorrect highlighting.

### Characters that need explicit lexer rules

The following characters appear in real SPL but are not word characters (`\w`) and have no obvious operator meaning, so they produce error tokens if no rule matches them:

| Character | Where it appears | Rule needed |
| --------- | ---------------- | ----------- |
| `@` | Time snap modifier: `-24h@h`, `@d`, `@w0` | `Operator` |
| `:` | Field values with colons: `sourcetype=cisco:asa` | `Punctuation` |
| `{}` | spath array paths: `results{}`, `data{0}` | `Punctuation` |
| `$word$` | Macro argument substitution: `$host$` | `Name::Variable` |
| `$` | Standalone (e.g. `return $threshold`) | `Operator` |

### The dot operator and IP addresses

Do __not__ write `rule %r/\.(?!\w)/` for the dot operator. The negative lookahead `(?!\w)` prevents it from matching dots before digits, so IP addresses like `10.0.0.*` produce error tokens on every `.`. Use a plain `rule %r/\./` instead.

### Documentation placeholders are not syntax

Splunk documentation uses `<<UPPERCASE>>` patterns (e.g. `<<field-name>>`, `<<search-string>>`) and `<lowercase>` angle-bracket patterns to indicate where the user should substitute their own values. __None of these are real SPL syntax.__ Do not add lexer rules for them and do not include them in the visual sample.

## Verification workflow (MANDATORY — do this BEFORE adding anything)

Before writing or modifying the lexer, fetch __every URL in the Splunk documentation list__ above. Do not begin implementation until all pages have been read. "I read the quick-reference page" is not sufficient.

Before adding ANY individual keyword, function, or syntax element:

1. __Fetch the relevant documentation page__ using the WebFetch tool or curl (see Fetching documentation above).
2. __Extract and confirm__ the element exists in the fetched content. Do not rely on training data, memory, or assumptions about what "should" exist.
3. __Only add__ elements that appear in the fetched content. __Only remove__ elements confirmed absent.

### What NOT to do

- __Do NOT add functions, keywords, or syntax from training data or memory.__ Every addition must be traced to a specific URL from the reference list in this file.
- __Do NOT use preview/beta features__ unless explicitly asked. Only add GA (generally available) features.
- __Do NOT fabricate or modify reference URLs.__ Use ONLY the exact URLs listed in this file. If a URL doesn't work, say so — do not guess an alternative.
- __Do NOT assume a function exists because a similar one does.__

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

### Iterative testing workflow

1. Run `pytest -v` — this directly inspects every `Token.Error` in the lexer output and is the authoritative check.
2. Optionally start `python server.py` for a visual review of token coloring (useful for spotting wrong token *types*, not error tokens).
3. Fix any errors in `pygments_lexer_spl/_lexer.py`.
4. Repeat until `pytest` passes with zero error tokens.

## Self-verification

After making changes, verify correctness by __re-fetching the source documentation__ and confirming every added element appears in the fetched HTML. Do not verify by re-reading your own changes — verify against the external source.

### Constraints (applies to all work)

- __No hallucinated syntax.__ Every keyword, function, operator, and language construct in the lexer must come from the official documentation listed above. for patterns. Don't invent novel approaches.
- __`pytest` is the ground truth for error tokens.__ The test suite calls `lexer.get_tokens(text)` directly and asserts that no token has type `Token.Error`. This is more reliable than scraping HTML.
- __Iterate until clean.__ Do not declare the task complete until both `pytest` passes AND the Error token count is zero for both demo and visual sample.

## Changelog

The changelog ([CHANGELOG.md](CHANGELOG.md)) follows the
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format and
[Semantic Versioning](https://semver.org/spec/v2.0.0.html). When updating the
changelog:

- Use `## [version] - YYYY-MM-DD` for release headings
- Use `### Added`, `### Changed`, `### Removed` as second-level section headings
- Use `#### Category name` as optional third-level headings within a section
- Ensure blank lines surround all headings to satisfy markdownlint
