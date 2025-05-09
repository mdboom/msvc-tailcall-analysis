# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: not sig
- HPT reliability: 50.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): json_dumps, json_loads, pickle_pure_python, tomli_loads, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_text, genshi_xml, mako

All benchmarks:
===============

Benchmark hidden because not significant (94): 2to3, many_optionals, subparsers, async_generators, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, chaos, comprehensions, bench_mp_pool, bench_thread_pool, coroutines, coverage, crypto_pyaes, deepcopy, deepcopy_reduce, deepcopy_memo, deltablue, django_template, docutils, dulwich_log, fannkuch, float, create_gc_cycles, gc_traversal, generators, genshi_text, genshi_xml, go, hexiom, html5lib, json, json_dumps, json_loads, logging_format, logging_silent, logging_simple, mako, mdp, meteor_contest, nbody, shortest_path, connected_components, k_core, nqueens, pathlib, pickle_pure_python, pidigits, pprint_safe_repr, pprint_pformat, pycparser, pyflate, pylint, python_startup, python_startup_no_site, raytrace, regex_compile, regex_dna, regex_effbot, regex_v8, richards, richards_super, scimark_fft, scimark_lu, scimark_monte_carlo, scimark_sor, scimark_sparse_mat_mult, spectral_norm, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, sqlite_synth, sympy_expand, sympy_integrate, sympy_sum, sympy_str, telco, thrift, tomli_loads, typing_runtime_protocols, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse, xml_etree_generate, xml_etree_process

- Geometric mean (including insignificant results): not sig

# HPT report

- Reliability score: 50.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown