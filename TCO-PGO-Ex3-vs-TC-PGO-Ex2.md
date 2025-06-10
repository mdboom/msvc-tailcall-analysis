# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.007x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------|:----------:|:----------------------:|
| docutils       | 1.63 sec   | 1.66 sec: 1.02x slower |
| html5lib       | 36.1 ms    | 37.8 ms: 1.05x slower  |
| Geometric mean | (ref)      | 1.02x slower           |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|--------------------|:----------:|:---------------------:|
| coroutines         | 12.4 ms    | 12.0 ms: 1.04x faster |
| async_generators   | 206 ms     | 201 ms: 1.02x faster  |
| asyncio_websockets | 317 ms     | 313 ms: 1.01x faster  |
| async_tree_io_tg   | 371 ms     | 377 ms: 1.02x slower  |
| async_tree_io      | 375 ms     | 382 ms: 1.02x slower  |
| Geometric mean     | (ref)      | 1.00x faster          |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 145 ms: 1.01x faster  |
| nbody          | 53.3 ms    | 55.6 ms: 1.04x slower |
| float          | 40.2 ms    | 42.0 ms: 1.04x slower |
| Geometric mean | (ref)      | 1.03x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 120 ms: 1.04x slower  |
| regex_effbot   | 1.40 ms    | 1.47 ms: 1.05x slower |
| regex_compile  | 74.8 ms    | 79.4 ms: 1.06x slower |
| Geometric mean | (ref)      | 1.04x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------------|:----------:|:---------------------:|
| pickle_pure_python   | 201 us     | 199 us: 1.01x faster  |
| json_dumps           | 6.48 ms    | 6.40 ms: 1.01x faster |
| unpickle_pure_python | 123 us     | 124 us: 1.01x slower  |
| xml_etree_iterparse  | 60.4 ms    | 61.2 ms: 1.01x slower |
| xml_etree_generate   | 51.5 ms    | 53.1 ms: 1.03x slower |
| Geometric mean       | (ref)      | 1.00x slower          |

Benchmark hidden because not significant (4): tomli_loads, json_loads, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 18.6 ms: 1.05x faster |
| python_startup         | 26.0 ms    | 24.7 ms: 1.05x faster |
| Geometric mean         | (ref)      | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| mako           | 6.12 ms    | 6.25 ms: 1.02x slower |
| genshi_xml     | 30.7 ms    | 32.3 ms: 1.05x slower |
| Geometric mean | (ref)      | 1.02x slower          |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | TC-PGO-Ex2 | TCO-PGO-Ex3            |
|--------------------------|:----------:|:----------------------:|
| scimark_sor              | 67.5 ms    | 60.5 ms: 1.12x faster  |
| many_optionals           | 761 us     | 685 us: 1.11x faster   |
| subparsers               | 44.9 ms    | 41.4 ms: 1.09x faster  |
| scimark_lu               | 54.4 ms    | 50.3 ms: 1.08x faster  |
| logging_silent           | 53.3 ns    | 49.7 ns: 1.07x faster  |
| python_startup_no_site   | 19.6 ms    | 18.6 ms: 1.05x faster  |
| python_startup           | 26.0 ms    | 24.7 ms: 1.05x faster  |
| fannkuch                 | 236 ms     | 225 ms: 1.05x faster   |
| coverage                 | 49.5 ms    | 47.5 ms: 1.04x faster  |
| coroutines               | 12.4 ms    | 12.0 ms: 1.04x faster  |
| scimark_monte_carlo      | 37.0 ms    | 35.6 ms: 1.04x faster  |
| spectral_norm            | 51.1 ms    | 49.4 ms: 1.04x faster  |
| raytrace                 | 166 ms     | 162 ms: 1.03x faster   |
| scimark_sparse_mat_mult  | 2.26 ms    | 2.21 ms: 1.02x faster  |
| async_generators         | 206 ms     | 201 ms: 1.02x faster   |
| asyncio_websockets       | 317 ms     | 313 ms: 1.01x faster   |
| pprint_pformat           | 968 ms     | 956 ms: 1.01x faster   |
| pickle_pure_python       | 201 us     | 199 us: 1.01x faster   |
| json_dumps               | 6.48 ms    | 6.40 ms: 1.01x faster  |
| chaos                    | 35.9 ms    | 35.4 ms: 1.01x faster  |
| deepcopy_memo            | 17.0 us    | 16.8 us: 1.01x faster  |
| typing_runtime_protocols | 98.9 us    | 97.8 us: 1.01x faster  |
| create_gc_cycles         | 1.27 ms    | 1.25 ms: 1.01x faster  |
| pprint_safe_repr         | 478 ms     | 474 ms: 1.01x faster   |
| pidigits                 | 146 ms     | 145 ms: 1.01x faster   |
| bpe_tokeniser            | 2.71 sec   | 2.72 sec: 1.00x slower |
| scimark_fft              | 152 ms     | 153 ms: 1.01x slower   |
| unpickle_pure_python     | 123 us     | 124 us: 1.01x slower   |
| shortest_path            | 348 ms     | 352 ms: 1.01x slower   |
| logging_format           | 6.34 us    | 6.42 us: 1.01x slower  |
| telco                    | 4.54 ms    | 4.59 ms: 1.01x slower  |
| xml_etree_iterparse      | 60.4 ms    | 61.2 ms: 1.01x slower  |
| connected_components     | 321 ms     | 325 ms: 1.01x slower   |
| logging_simple           | 5.78 us    | 5.87 us: 1.02x slower  |
| async_tree_io_tg         | 371 ms     | 377 ms: 1.02x slower   |
| deltablue                | 1.85 ms    | 1.88 ms: 1.02x slower  |
| thrift                   | 482 us     | 491 us: 1.02x slower   |
| pyflate                  | 260 ms     | 264 ms: 1.02x slower   |
| docutils                 | 1.63 sec   | 1.66 sec: 1.02x slower |
| async_tree_io            | 375 ms     | 382 ms: 1.02x slower   |
| json                     | 2.98 ms    | 3.04 ms: 1.02x slower  |
| gc_traversal             | 2.07 ms    | 2.12 ms: 1.02x slower  |
| meteor_contest           | 69.5 ms    | 70.9 ms: 1.02x slower  |
| mdp                      | 1.40 sec   | 1.43 sec: 1.02x slower |
| mako                     | 6.12 ms    | 6.25 ms: 1.02x slower  |
| dulwich_log              | 39.5 ms    | 40.3 ms: 1.02x slower  |
| nqueens                  | 54.0 ms    | 55.2 ms: 1.02x slower  |
| sqlglot_v2_optimize      | 32.2 ms    | 32.9 ms: 1.02x slower  |
| go                       | 68.4 ms    | 70.5 ms: 1.03x slower  |
| xml_etree_generate       | 51.5 ms    | 53.1 ms: 1.03x slower  |
| sqlglot_v2_normalize     | 66.9 ms    | 69.0 ms: 1.03x slower  |
| sympy_sum                | 82.1 ms    | 85.2 ms: 1.04x slower  |
| pycparser                | 664 ms     | 689 ms: 1.04x slower   |
| regex_dna                | 115 ms     | 120 ms: 1.04x slower   |
| nbody                    | 53.3 ms    | 55.6 ms: 1.04x slower  |
| float                    | 40.2 ms    | 42.0 ms: 1.04x slower  |
| deepcopy                 | 160 us     | 167 us: 1.05x slower   |
| richards_super           | 32.2 ms    | 33.7 ms: 1.05x slower  |
| html5lib                 | 36.1 ms    | 37.8 ms: 1.05x slower  |
| sympy_integrate          | 12.2 ms    | 12.8 ms: 1.05x slower  |
| sympy_expand             | 269 ms     | 283 ms: 1.05x slower   |
| genshi_xml               | 30.7 ms    | 32.3 ms: 1.05x slower  |
| regex_effbot             | 1.40 ms    | 1.47 ms: 1.05x slower  |
| crypto_pyaes             | 41.6 ms    | 43.9 ms: 1.06x slower  |
| richards                 | 27.8 ms    | 29.4 ms: 1.06x slower  |
| sqlglot_v2_parse         | 740 us     | 781 us: 1.06x slower   |
| regex_compile            | 74.8 ms    | 79.4 ms: 1.06x slower  |
| sqlglot_v2_transpile     | 933 us     | 993 us: 1.06x slower   |
| sympy_str                | 158 ms     | 173 ms: 1.10x slower   |
| generators               | 14.8 ms    | 16.5 ms: 1.11x slower  |
| Geometric mean           | (ref)      | 1.01x slower           |

Benchmark hidden because not significant (22): pathlib, async_tree_memoization_tg, 2to3, k_core, async_tree_none, async_tree_memoization, tomli_loads, async_tree_cpu_io_mixed, json_loads, sqlite_synth, comprehensions, xml_etree_process, xml_etree_parse, hexiom, genshi_text, sphinx, async_tree_cpu_io_mixed_tg, django_template, async_tree_none_tg, deepcopy_reduce, regex_v8, pylint
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown