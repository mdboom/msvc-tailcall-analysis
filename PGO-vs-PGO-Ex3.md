# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.000x slower
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | PGO                    |
|----------------|:--------:|:----------------------:|
| docutils       | 1.71 sec | 1.68 sec: 1.02x faster |
| sphinx         | 670 ms   | 658 ms: 1.02x faster   |
| Geometric mean | (ref)    | 1.01x faster           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | PGO-Ex3 | PGO                   |
|---------------------------|:-------:|:---------------------:|
| async_tree_memoization_tg | 219 ms  | 216 ms: 1.01x faster  |
| async_tree_io             | 417 ms  | 423 ms: 1.02x slower  |
| asyncio_websockets        | 311 ms  | 318 ms: 1.02x slower  |
| coroutines                | 13.1 ms | 13.5 ms: 1.03x slower |
| async_generators          | 219 ms  | 226 ms: 1.04x slower  |
| Geometric mean            | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | PGO                   |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 74.1 ms: 1.06x faster |
| pidigits       | 148 ms  | 152 ms: 1.03x slower  |
| float          | 44.2 ms | 47.8 ms: 1.08x slower |
| Geometric mean | (ref)   | 1.02x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | PGO                   |
|----------------|:-------:|:---------------------:|
| regex_dna      | 116 ms  | 112 ms: 1.03x faster  |
| regex_effbot   | 1.46 ms | 1.42 ms: 1.02x faster |
| regex_compile  | 86.1 ms | 88.2 ms: 1.02x slower |
| Geometric mean | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | PGO                    |
|----------------------|:--------:|:----------------------:|
| json_loads           | 15.3 us  | 14.7 us: 1.04x faster  |
| tomli_loads          | 1.44 sec | 1.47 sec: 1.02x slower |
| xml_etree_iterparse  | 62.3 ms  | 63.7 ms: 1.02x slower  |
| xml_etree_parse      | 88.8 ms  | 91.2 ms: 1.03x slower  |
| xml_etree_generate   | 56.8 ms  | 58.7 ms: 1.03x slower  |
| xml_etree_process    | 39.7 ms  | 41.5 ms: 1.05x slower  |
| json_dumps           | 6.69 ms  | 7.05 ms: 1.05x slower  |
| unpickle_pure_python | 147 us   | 155 us: 1.06x slower   |
| pickle_pure_python   | 217 us   | 237 us: 1.09x slower   |
| Geometric mean       | (ref)    | 1.03x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | PGO                   |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 19.8 ms: 1.06x slower |
| python_startup         | 24.5 ms | 26.1 ms: 1.06x slower |
| Geometric mean         | (ref)   | 1.06x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | PGO                   |
|-----------------|:-------:|:---------------------:|
| django_template | 25.5 ms | 25.1 ms: 1.02x faster |
| genshi_xml      | 35.0 ms | 36.3 ms: 1.04x slower |
| genshi_text     | 15.8 ms | 16.5 ms: 1.04x slower |
| mako            | 6.50 ms | 6.86 ms: 1.05x slower |
| Geometric mean  | (ref)   | 1.03x slower          |

All benchmarks:
===============

| Benchmark                 | PGO-Ex3  | PGO                    |
|---------------------------|:--------:|:----------------------:|
| subparsers                | 41.0 ms  | 16.1 ms: 2.55x faster  |
| many_optionals            | 695 us   | 438 us: 1.59x faster   |
| richards_super            | 39.9 ms  | 35.1 ms: 1.14x faster  |
| richards                  | 34.5 ms  | 30.7 ms: 1.12x faster  |
| nbody                     | 78.3 ms  | 74.1 ms: 1.06x faster  |
| raytrace                  | 201 ms   | 191 ms: 1.06x faster   |
| coverage                  | 49.2 ms  | 46.8 ms: 1.05x faster  |
| json_loads                | 15.3 us  | 14.7 us: 1.04x faster  |
| pylint                    | 208 ms   | 201 ms: 1.04x faster   |
| generators                | 20.0 ms  | 19.3 ms: 1.04x faster  |
| sqlglot_v2_normalize      | 76.3 ms  | 73.6 ms: 1.04x faster  |
| regex_dna                 | 116 ms   | 112 ms: 1.03x faster   |
| thrift                    | 522 us   | 507 us: 1.03x faster   |
| regex_effbot              | 1.46 ms  | 1.42 ms: 1.02x faster  |
| sphinx                    | 670 ms   | 658 ms: 1.02x faster   |
| django_template           | 25.5 ms  | 25.1 ms: 1.02x faster  |
| docutils                  | 1.71 sec | 1.68 sec: 1.02x faster |
| sqlglot_v2_optimize       | 35.6 ms  | 35.0 ms: 1.02x faster  |
| async_tree_memoization_tg | 219 ms   | 216 ms: 1.01x faster   |
| logging_format            | 7.11 us  | 7.03 us: 1.01x faster  |
| sympy_expand              | 305 ms   | 302 ms: 1.01x faster   |
| sqlglot_v2_transpile      | 1.09 ms  | 1.10 ms: 1.01x slower  |
| mdp                       | 1.62 sec | 1.64 sec: 1.01x slower |
| bpe_tokeniser             | 2.93 sec | 2.96 sec: 1.01x slower |
| sqlite_synth              | 1.57 us  | 1.59 us: 1.01x slower  |
| comprehensions            | 11.2 us  | 11.3 us: 1.01x slower  |
| shortest_path             | 354 ms   | 359 ms: 1.01x slower   |
| async_tree_io             | 417 ms   | 423 ms: 1.02x slower   |
| connected_components      | 324 ms   | 329 ms: 1.02x slower   |
| tomli_loads               | 1.44 sec | 1.47 sec: 1.02x slower |
| nqueens                   | 62.2 ms  | 63.6 ms: 1.02x slower  |
| dulwich_log               | 42.4 ms  | 43.4 ms: 1.02x slower  |
| xml_etree_iterparse       | 62.3 ms  | 63.7 ms: 1.02x slower  |
| asyncio_websockets        | 311 ms   | 318 ms: 1.02x slower   |
| regex_compile             | 86.1 ms  | 88.2 ms: 1.02x slower  |
| deepcopy                  | 185 us   | 190 us: 1.02x slower   |
| hexiom                    | 4.28 ms  | 4.38 ms: 1.02x slower  |
| sqlglot_v2_parse          | 870 us   | 892 us: 1.03x slower   |
| coroutines                | 13.1 ms  | 13.5 ms: 1.03x slower  |
| pidigits                  | 148 ms   | 152 ms: 1.03x slower   |
| crypto_pyaes              | 48.6 ms  | 50.0 ms: 1.03x slower  |
| xml_etree_parse           | 88.8 ms  | 91.2 ms: 1.03x slower  |
| scimark_fft               | 187 ms   | 192 ms: 1.03x slower   |
| telco                     | 4.75 ms  | 4.89 ms: 1.03x slower  |
| deepcopy_reduce           | 1.88 us  | 1.94 us: 1.03x slower  |
| xml_etree_generate        | 56.8 ms  | 58.7 ms: 1.03x slower  |
| chaos                     | 42.2 ms  | 43.6 ms: 1.03x slower  |
| meteor_contest            | 74.3 ms  | 76.9 ms: 1.03x slower  |
| scimark_sparse_mat_mult   | 2.63 ms  | 2.72 ms: 1.03x slower  |
| pprint_pformat            | 1.09 sec | 1.13 sec: 1.04x slower |
| async_generators          | 219 ms   | 226 ms: 1.04x slower   |
| genshi_xml                | 35.0 ms  | 36.3 ms: 1.04x slower  |
| genshi_text               | 15.8 ms  | 16.5 ms: 1.04x slower  |
| scimark_monte_carlo       | 45.3 ms  | 47.1 ms: 1.04x slower  |
| xml_etree_process         | 39.7 ms  | 41.5 ms: 1.05x slower  |
| pprint_safe_repr          | 532 ms   | 558 ms: 1.05x slower   |
| deltablue                 | 2.18 ms  | 2.29 ms: 1.05x slower  |
| pyflate                   | 300 ms   | 315 ms: 1.05x slower   |
| go                        | 84.1 ms  | 88.6 ms: 1.05x slower  |
| json_dumps                | 6.69 ms  | 7.05 ms: 1.05x slower  |
| mako                      | 6.50 ms  | 6.86 ms: 1.05x slower  |
| spectral_norm             | 58.1 ms  | 61.5 ms: 1.06x slower  |
| unpickle_pure_python      | 147 us   | 155 us: 1.06x slower   |
| python_startup_no_site    | 18.7 ms  | 19.8 ms: 1.06x slower  |
| python_startup            | 24.5 ms  | 26.1 ms: 1.06x slower  |
| float                     | 44.2 ms  | 47.8 ms: 1.08x slower  |
| scimark_sor               | 84.2 ms  | 91.0 ms: 1.08x slower  |
| pickle_pure_python        | 217 us   | 237 us: 1.09x slower   |
| scimark_lu                | 61.1 ms  | 66.9 ms: 1.09x slower  |
| deepcopy_memo             | 19.1 us  | 21.0 us: 1.10x slower  |
| fannkuch                  | 263 ms   | 296 ms: 1.13x slower   |
| logging_silent            | 57.0 ns  | 65.2 ns: 1.14x slower  |
| pathlib                   | 24.6 ms  | 32.1 ms: 1.30x slower  |
| Geometric mean            | (ref)    | 1.00x slower           |

Benchmark hidden because not significant (19): regex_v8, pycparser, sympy_integrate, json, gc_traversal, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, sympy_sum, sympy_str, async_tree_io_tg, logging_simple, k_core, typing_runtime_protocols, create_gc_cycles, async_tree_none_tg, 2to3, async_tree_memoization, async_tree_none, html5lib
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 99.49% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown