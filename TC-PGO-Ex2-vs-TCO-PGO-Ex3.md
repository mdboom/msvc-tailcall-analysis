# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.007x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex2             |
|----------------|:-----------:|:----------------------:|
| docutils       | 1.66 sec    | 1.63 sec: 1.02x faster |
| html5lib       | 37.8 ms     | 36.1 ms: 1.05x faster  |
| Geometric mean | (ref)       | 1.02x faster           |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|--------------------|:-----------:|:---------------------:|
| async_tree_io      | 382 ms      | 375 ms: 1.02x faster  |
| async_tree_io_tg   | 377 ms      | 371 ms: 1.02x faster  |
| asyncio_websockets | 313 ms      | 317 ms: 1.01x slower  |
| async_generators   | 201 ms      | 206 ms: 1.02x slower  |
| coroutines         | 12.0 ms     | 12.4 ms: 1.04x slower |
| Geometric mean     | (ref)       | 1.00x slower          |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:-----------:|:---------------------:|
| float          | 42.0 ms     | 40.2 ms: 1.04x faster |
| nbody          | 55.6 ms     | 53.3 ms: 1.04x faster |
| pidigits       | 145 ms      | 146 ms: 1.01x slower  |
| Geometric mean | (ref)       | 1.03x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 79.4 ms     | 74.8 ms: 1.06x faster |
| regex_effbot   | 1.47 ms     | 1.40 ms: 1.05x faster |
| regex_dna      | 120 ms      | 115 ms: 1.04x faster  |
| Geometric mean | (ref)       | 1.04x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|----------------------|:-----------:|:---------------------:|
| xml_etree_generate   | 53.1 ms     | 51.5 ms: 1.03x faster |
| xml_etree_iterparse  | 61.2 ms     | 60.4 ms: 1.01x faster |
| unpickle_pure_python | 124 us      | 123 us: 1.01x faster  |
| json_dumps           | 6.40 ms     | 6.48 ms: 1.01x slower |
| pickle_pure_python   | 199 us      | 201 us: 1.01x slower  |
| Geometric mean       | (ref)       | 1.00x faster          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 24.7 ms     | 26.0 ms: 1.05x slower |
| python_startup_no_site | 18.6 ms     | 19.6 ms: 1.05x slower |
| Geometric mean         | (ref)       | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:-----------:|:---------------------:|
| genshi_xml     | 32.3 ms     | 30.7 ms: 1.05x faster |
| mako           | 6.25 ms     | 6.12 ms: 1.02x faster |
| Geometric mean | (ref)       | 1.02x faster          |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                | TCO-PGO-Ex3 | TC-PGO-Ex2             |
|--------------------------|:-----------:|:----------------------:|
| generators               | 16.5 ms     | 14.8 ms: 1.11x faster  |
| sympy_str                | 173 ms      | 158 ms: 1.10x faster   |
| sqlglot_v2_transpile     | 993 us      | 933 us: 1.06x faster   |
| regex_compile            | 79.4 ms     | 74.8 ms: 1.06x faster  |
| sqlglot_v2_parse         | 781 us      | 740 us: 1.06x faster   |
| richards                 | 29.4 ms     | 27.8 ms: 1.06x faster  |
| crypto_pyaes             | 43.9 ms     | 41.6 ms: 1.06x faster  |
| regex_effbot             | 1.47 ms     | 1.40 ms: 1.05x faster  |
| genshi_xml               | 32.3 ms     | 30.7 ms: 1.05x faster  |
| sympy_expand             | 283 ms      | 269 ms: 1.05x faster   |
| sympy_integrate          | 12.8 ms     | 12.2 ms: 1.05x faster  |
| html5lib                 | 37.8 ms     | 36.1 ms: 1.05x faster  |
| richards_super           | 33.7 ms     | 32.2 ms: 1.05x faster  |
| deepcopy                 | 167 us      | 160 us: 1.05x faster   |
| float                    | 42.0 ms     | 40.2 ms: 1.04x faster  |
| nbody                    | 55.6 ms     | 53.3 ms: 1.04x faster  |
| regex_dna                | 120 ms      | 115 ms: 1.04x faster   |
| pycparser                | 689 ms      | 664 ms: 1.04x faster   |
| sympy_sum                | 85.2 ms     | 82.1 ms: 1.04x faster  |
| sqlglot_v2_normalize     | 69.0 ms     | 66.9 ms: 1.03x faster  |
| xml_etree_generate       | 53.1 ms     | 51.5 ms: 1.03x faster  |
| go                       | 70.5 ms     | 68.4 ms: 1.03x faster  |
| sqlglot_v2_optimize      | 32.9 ms     | 32.2 ms: 1.02x faster  |
| nqueens                  | 55.2 ms     | 54.0 ms: 1.02x faster  |
| dulwich_log              | 40.3 ms     | 39.5 ms: 1.02x faster  |
| mako                     | 6.25 ms     | 6.12 ms: 1.02x faster  |
| mdp                      | 1.43 sec    | 1.40 sec: 1.02x faster |
| meteor_contest           | 70.9 ms     | 69.5 ms: 1.02x faster  |
| gc_traversal             | 2.12 ms     | 2.07 ms: 1.02x faster  |
| json                     | 3.04 ms     | 2.98 ms: 1.02x faster  |
| async_tree_io            | 382 ms      | 375 ms: 1.02x faster   |
| docutils                 | 1.66 sec    | 1.63 sec: 1.02x faster |
| pyflate                  | 264 ms      | 260 ms: 1.02x faster   |
| thrift                   | 491 us      | 482 us: 1.02x faster   |
| deltablue                | 1.88 ms     | 1.85 ms: 1.02x faster  |
| async_tree_io_tg         | 377 ms      | 371 ms: 1.02x faster   |
| logging_simple           | 5.87 us     | 5.78 us: 1.02x faster  |
| connected_components     | 325 ms      | 321 ms: 1.01x faster   |
| xml_etree_iterparse      | 61.2 ms     | 60.4 ms: 1.01x faster  |
| telco                    | 4.59 ms     | 4.54 ms: 1.01x faster  |
| logging_format           | 6.42 us     | 6.34 us: 1.01x faster  |
| shortest_path            | 352 ms      | 348 ms: 1.01x faster   |
| unpickle_pure_python     | 124 us      | 123 us: 1.01x faster   |
| scimark_fft              | 153 ms      | 152 ms: 1.01x faster   |
| bpe_tokeniser            | 2.72 sec    | 2.71 sec: 1.00x faster |
| pidigits                 | 145 ms      | 146 ms: 1.01x slower   |
| pprint_safe_repr         | 474 ms      | 478 ms: 1.01x slower   |
| create_gc_cycles         | 1.25 ms     | 1.27 ms: 1.01x slower  |
| typing_runtime_protocols | 97.8 us     | 98.9 us: 1.01x slower  |
| deepcopy_memo            | 16.8 us     | 17.0 us: 1.01x slower  |
| chaos                    | 35.4 ms     | 35.9 ms: 1.01x slower  |
| json_dumps               | 6.40 ms     | 6.48 ms: 1.01x slower  |
| pickle_pure_python       | 199 us      | 201 us: 1.01x slower   |
| pprint_pformat           | 956 ms      | 968 ms: 1.01x slower   |
| asyncio_websockets       | 313 ms      | 317 ms: 1.01x slower   |
| async_generators         | 201 ms      | 206 ms: 1.02x slower   |
| scimark_sparse_mat_mult  | 2.21 ms     | 2.26 ms: 1.02x slower  |
| raytrace                 | 162 ms      | 166 ms: 1.03x slower   |
| spectral_norm            | 49.4 ms     | 51.1 ms: 1.04x slower  |
| scimark_monte_carlo      | 35.6 ms     | 37.0 ms: 1.04x slower  |
| coroutines               | 12.0 ms     | 12.4 ms: 1.04x slower  |
| coverage                 | 47.5 ms     | 49.5 ms: 1.04x slower  |
| fannkuch                 | 225 ms      | 236 ms: 1.05x slower   |
| python_startup           | 24.7 ms     | 26.0 ms: 1.05x slower  |
| python_startup_no_site   | 18.6 ms     | 19.6 ms: 1.05x slower  |
| logging_silent           | 49.7 ns     | 53.3 ns: 1.07x slower  |
| scimark_lu               | 50.3 ms     | 54.4 ms: 1.08x slower  |
| subparsers               | 41.4 ms     | 44.9 ms: 1.09x slower  |
| many_optionals           | 685 us      | 761 us: 1.11x slower   |
| scimark_sor              | 60.5 ms     | 67.5 ms: 1.12x slower  |
| Geometric mean           | (ref)       | 1.01x faster           |

Benchmark hidden because not significant (22): pylint, regex_v8, deepcopy_reduce, async_tree_none_tg, django_template, async_tree_cpu_io_mixed_tg, sphinx, genshi_text, hexiom, xml_etree_parse, xml_etree_process, comprehensions, sqlite_synth, json_loads, async_tree_cpu_io_mixed, tomli_loads, async_tree_memoization, async_tree_none, k_core, 2to3, async_tree_memoization_tg, pathlib
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown