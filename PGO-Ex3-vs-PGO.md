# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.001x faster
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | PGO-Ex3                |
|----------------|:--------:|:----------------------:|
| docutils       | 1.68 sec | 1.71 sec: 1.02x slower |
| sphinx         | 658 ms   | 670 ms: 1.02x slower   |
| Geometric mean | (ref)    | 1.01x slower           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | PGO     | PGO-Ex3               |
|---------------------------|:-------:|:---------------------:|
| async_generators          | 226 ms  | 219 ms: 1.04x faster  |
| coroutines                | 13.5 ms | 13.1 ms: 1.03x faster |
| asyncio_websockets        | 318 ms  | 311 ms: 1.02x faster  |
| async_tree_io             | 423 ms  | 417 ms: 1.02x faster  |
| async_tree_memoization_tg | 216 ms  | 219 ms: 1.01x slower  |
| Geometric mean            | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (6): async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| float          | 47.8 ms | 44.2 ms: 1.08x faster |
| pidigits       | 152 ms  | 148 ms: 1.03x faster  |
| nbody          | 74.1 ms | 78.3 ms: 1.06x slower |
| Geometric mean | (ref)   | 1.02x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 86.1 ms: 1.02x faster |
| regex_effbot   | 1.42 ms | 1.46 ms: 1.02x slower |
| regex_dna      | 112 ms  | 116 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | PGO-Ex3                |
|----------------------|:--------:|:----------------------:|
| pickle_pure_python   | 237 us   | 217 us: 1.09x faster   |
| unpickle_pure_python | 155 us   | 147 us: 1.06x faster   |
| json_dumps           | 7.05 ms  | 6.69 ms: 1.05x faster  |
| xml_etree_process    | 41.5 ms  | 39.7 ms: 1.05x faster  |
| xml_etree_generate   | 58.7 ms  | 56.8 ms: 1.03x faster  |
| xml_etree_parse      | 91.2 ms  | 88.8 ms: 1.03x faster  |
| xml_etree_iterparse  | 63.7 ms  | 62.3 ms: 1.02x faster  |
| tomli_loads          | 1.47 sec | 1.44 sec: 1.02x faster |
| json_loads           | 14.7 us  | 15.3 us: 1.04x slower  |
| Geometric mean       | (ref)    | 1.03x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | PGO-Ex3               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.1 ms | 24.5 ms: 1.06x faster |
| python_startup_no_site | 19.8 ms | 18.7 ms: 1.06x faster |
| Geometric mean         | (ref)   | 1.06x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | PGO-Ex3               |
|-----------------|:-------:|:---------------------:|
| mako            | 6.86 ms | 6.50 ms: 1.05x faster |
| genshi_text     | 16.5 ms | 15.8 ms: 1.04x faster |
| genshi_xml      | 36.3 ms | 35.0 ms: 1.04x faster |
| django_template | 25.1 ms | 25.5 ms: 1.02x slower |
| Geometric mean  | (ref)   | 1.03x faster          |

All benchmarks:
===============

| Benchmark                 | PGO      | PGO-Ex3                |
|---------------------------|:--------:|:----------------------:|
| pathlib                   | 32.1 ms  | 24.6 ms: 1.30x faster  |
| logging_silent            | 65.2 ns  | 57.0 ns: 1.14x faster  |
| fannkuch                  | 296 ms   | 263 ms: 1.13x faster   |
| deepcopy_memo             | 21.0 us  | 19.1 us: 1.10x faster  |
| scimark_lu                | 66.9 ms  | 61.1 ms: 1.09x faster  |
| pickle_pure_python        | 237 us   | 217 us: 1.09x faster   |
| scimark_sor               | 91.0 ms  | 84.2 ms: 1.08x faster  |
| float                     | 47.8 ms  | 44.2 ms: 1.08x faster  |
| python_startup            | 26.1 ms  | 24.5 ms: 1.06x faster  |
| python_startup_no_site    | 19.8 ms  | 18.7 ms: 1.06x faster  |
| unpickle_pure_python      | 155 us   | 147 us: 1.06x faster   |
| spectral_norm             | 61.5 ms  | 58.1 ms: 1.06x faster  |
| mako                      | 6.86 ms  | 6.50 ms: 1.05x faster  |
| json_dumps                | 7.05 ms  | 6.69 ms: 1.05x faster  |
| go                        | 88.6 ms  | 84.1 ms: 1.05x faster  |
| pyflate                   | 315 ms   | 300 ms: 1.05x faster   |
| deltablue                 | 2.29 ms  | 2.18 ms: 1.05x faster  |
| pprint_safe_repr          | 558 ms   | 532 ms: 1.05x faster   |
| xml_etree_process         | 41.5 ms  | 39.7 ms: 1.05x faster  |
| scimark_monte_carlo       | 47.1 ms  | 45.3 ms: 1.04x faster  |
| genshi_text               | 16.5 ms  | 15.8 ms: 1.04x faster  |
| genshi_xml                | 36.3 ms  | 35.0 ms: 1.04x faster  |
| async_generators          | 226 ms   | 219 ms: 1.04x faster   |
| pprint_pformat            | 1.13 sec | 1.09 sec: 1.04x faster |
| scimark_sparse_mat_mult   | 2.72 ms  | 2.63 ms: 1.03x faster  |
| meteor_contest            | 76.9 ms  | 74.3 ms: 1.03x faster  |
| chaos                     | 43.6 ms  | 42.2 ms: 1.03x faster  |
| xml_etree_generate        | 58.7 ms  | 56.8 ms: 1.03x faster  |
| deepcopy_reduce           | 1.94 us  | 1.88 us: 1.03x faster  |
| telco                     | 4.89 ms  | 4.75 ms: 1.03x faster  |
| scimark_fft               | 192 ms   | 187 ms: 1.03x faster   |
| xml_etree_parse           | 91.2 ms  | 88.8 ms: 1.03x faster  |
| crypto_pyaes              | 50.0 ms  | 48.6 ms: 1.03x faster  |
| pidigits                  | 152 ms   | 148 ms: 1.03x faster   |
| coroutines                | 13.5 ms  | 13.1 ms: 1.03x faster  |
| sqlglot_v2_parse          | 892 us   | 870 us: 1.03x faster   |
| hexiom                    | 4.38 ms  | 4.28 ms: 1.02x faster  |
| deepcopy                  | 190 us   | 185 us: 1.02x faster   |
| regex_compile             | 88.2 ms  | 86.1 ms: 1.02x faster  |
| asyncio_websockets        | 318 ms   | 311 ms: 1.02x faster   |
| xml_etree_iterparse       | 63.7 ms  | 62.3 ms: 1.02x faster  |
| dulwich_log               | 43.4 ms  | 42.4 ms: 1.02x faster  |
| nqueens                   | 63.6 ms  | 62.2 ms: 1.02x faster  |
| tomli_loads               | 1.47 sec | 1.44 sec: 1.02x faster |
| connected_components      | 329 ms   | 324 ms: 1.02x faster   |
| async_tree_io             | 423 ms   | 417 ms: 1.02x faster   |
| shortest_path             | 359 ms   | 354 ms: 1.01x faster   |
| comprehensions            | 11.3 us  | 11.2 us: 1.01x faster  |
| sqlite_synth              | 1.59 us  | 1.57 us: 1.01x faster  |
| bpe_tokeniser             | 2.96 sec | 2.93 sec: 1.01x faster |
| mdp                       | 1.64 sec | 1.62 sec: 1.01x faster |
| sqlglot_v2_transpile      | 1.10 ms  | 1.09 ms: 1.01x faster  |
| sympy_expand              | 302 ms   | 305 ms: 1.01x slower   |
| logging_format            | 7.03 us  | 7.11 us: 1.01x slower  |
| async_tree_memoization_tg | 216 ms   | 219 ms: 1.01x slower   |
| sqlglot_v2_optimize       | 35.0 ms  | 35.6 ms: 1.02x slower  |
| docutils                  | 1.68 sec | 1.71 sec: 1.02x slower |
| django_template           | 25.1 ms  | 25.5 ms: 1.02x slower  |
| sphinx                    | 658 ms   | 670 ms: 1.02x slower   |
| regex_effbot              | 1.42 ms  | 1.46 ms: 1.02x slower  |
| thrift                    | 507 us   | 522 us: 1.03x slower   |
| regex_dna                 | 112 ms   | 116 ms: 1.03x slower   |
| sqlglot_v2_normalize      | 73.6 ms  | 76.3 ms: 1.04x slower  |
| generators                | 19.3 ms  | 20.0 ms: 1.04x slower  |
| pylint                    | 201 ms   | 208 ms: 1.04x slower   |
| json_loads                | 14.7 us  | 15.3 us: 1.04x slower  |
| coverage                  | 46.8 ms  | 49.2 ms: 1.05x slower  |
| raytrace                  | 191 ms   | 201 ms: 1.06x slower   |
| nbody                     | 74.1 ms  | 78.3 ms: 1.06x slower  |
| richards                  | 30.7 ms  | 34.5 ms: 1.12x slower  |
| richards_super            | 35.1 ms  | 39.9 ms: 1.14x slower  |
| many_optionals            | 438 us   | 695 us: 1.59x slower   |
| subparsers                | 16.1 ms  | 41.0 ms: 2.55x slower  |
| Geometric mean            | (ref)    | 1.00x faster           |

Benchmark hidden because not significant (19): html5lib, async_tree_none, async_tree_memoization, 2to3, async_tree_none_tg, create_gc_cycles, typing_runtime_protocols, k_core, logging_simple, async_tree_io_tg, sympy_str, sympy_sum, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, gc_traversal, json, sympy_integrate, pycparser, regex_v8
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown