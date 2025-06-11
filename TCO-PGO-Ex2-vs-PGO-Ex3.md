# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.042x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TCO-PGO-Ex2            |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 237 ms: 1.05x slower   |
| docutils       | 1.71 sec | 1.81 sec: 1.06x slower |
| html5lib       | 40.5 ms  | 40.8 ms: 1.01x slower  |
| sphinx         | 670 ms   | 723 ms: 1.08x slower   |
| Geometric mean | (ref)    | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TCO-PGO-Ex2           |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 311 ms  | 304 ms: 1.02x faster  |
| async_tree_none_tg         | 176 ms  | 178 ms: 1.01x slower  |
| async_tree_none            | 186 ms  | 188 ms: 1.01x slower  |
| async_tree_memoization     | 223 ms  | 227 ms: 1.02x slower  |
| async_tree_io_tg           | 410 ms  | 419 ms: 1.02x slower  |
| async_generators           | 219 ms  | 224 ms: 1.02x slower  |
| coroutines                 | 13.1 ms | 13.5 ms: 1.02x slower |
| async_tree_io              | 417 ms  | 429 ms: 1.03x slower  |
| async_tree_cpu_io_mixed    | 340 ms  | 362 ms: 1.07x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 367 ms: 1.07x slower  |
| Geometric mean             | (ref)   | 1.02x slower          |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 58.8 ms: 1.33x faster |
| pidigits       | 148 ms  | 147 ms: 1.01x faster  |
| float          | 44.2 ms | 44.8 ms: 1.01x slower |
| Geometric mean | (ref)   | 1.10x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| regex_dna      | 116 ms  | 117 ms: 1.01x slower  |
| regex_compile  | 86.1 ms | 88.0 ms: 1.02x slower |
| regex_v8       | 13.8 ms | 16.7 ms: 1.21x slower |
| regex_effbot   | 1.46 ms | 1.76 ms: 1.21x slower |
| Geometric mean | (ref)   | 1.11x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TCO-PGO-Ex2            |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.44 sec | 1.38 sec: 1.04x faster |
| unpickle_pure_python | 147 us   | 154 us: 1.05x slower   |
| pickle_pure_python   | 217 us   | 236 us: 1.08x slower   |
| xml_etree_iterparse  | 62.3 ms  | 71.5 ms: 1.15x slower  |
| xml_etree_parse      | 88.8 ms  | 104 ms: 1.17x slower   |
| xml_etree_process    | 39.7 ms  | 46.5 ms: 1.17x slower  |
| xml_etree_generate   | 56.8 ms  | 66.8 ms: 1.18x slower  |
| json_dumps           | 6.69 ms  | 7.94 ms: 1.19x slower  |
| json_loads           | 15.3 us  | 21.1 us: 1.38x slower  |
| Geometric mean       | (ref)    | 1.14x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | TCO-PGO-Ex2           |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 20.1 ms: 1.08x slower |
| python_startup         | 24.5 ms | 26.9 ms: 1.10x slower |
| Geometric mean         | (ref)   | 1.09x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TCO-PGO-Ex2           |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 35.3 ms: 1.01x slower |
| genshi_text     | 15.8 ms | 16.2 ms: 1.02x slower |
| django_template | 25.5 ms | 27.5 ms: 1.08x slower |
| mako            | 6.50 ms | 7.44 ms: 1.14x slower |
| Geometric mean  | (ref)   | 1.06x slower          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TCO-PGO-Ex2            |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 78.3 ms  | 58.8 ms: 1.33x faster  |
| scimark_sor                | 84.2 ms  | 73.9 ms: 1.14x faster  |
| generators                 | 20.0 ms  | 18.1 ms: 1.11x faster  |
| go                         | 84.1 ms  | 78.0 ms: 1.08x faster  |
| raytrace                   | 201 ms   | 187 ms: 1.08x faster   |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.48 ms: 1.06x faster  |
| scimark_monte_carlo        | 45.3 ms  | 42.9 ms: 1.06x faster  |
| scimark_fft                | 187 ms   | 178 ms: 1.05x faster   |
| deltablue                  | 2.18 ms  | 2.09 ms: 1.05x faster  |
| tomli_loads                | 1.44 sec | 1.38 sec: 1.04x faster |
| mdp                        | 1.62 sec | 1.57 sec: 1.03x faster |
| hexiom                     | 4.28 ms  | 4.17 ms: 1.03x faster  |
| asyncio_websockets         | 311 ms   | 304 ms: 1.02x faster   |
| chaos                      | 42.2 ms  | 41.4 ms: 1.02x faster  |
| pyflate                    | 300 ms   | 295 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 147 ms: 1.01x faster   |
| fannkuch                   | 263 ms   | 265 ms: 1.01x slower   |
| sqlglot_v2_parse           | 870 us   | 876 us: 1.01x slower   |
| shortest_path              | 354 ms   | 357 ms: 1.01x slower   |
| genshi_xml                 | 35.0 ms  | 35.3 ms: 1.01x slower  |
| async_tree_none_tg         | 176 ms   | 178 ms: 1.01x slower   |
| html5lib                   | 40.5 ms  | 40.8 ms: 1.01x slower  |
| logging_format             | 7.11 us  | 7.18 us: 1.01x slower  |
| richards_super             | 39.9 ms  | 40.4 ms: 1.01x slower  |
| regex_dna                  | 116 ms   | 117 ms: 1.01x slower   |
| float                      | 44.2 ms  | 44.8 ms: 1.01x slower  |
| richards                   | 34.5 ms  | 35.0 ms: 1.01x slower  |
| async_tree_none            | 186 ms   | 188 ms: 1.01x slower   |
| crypto_pyaes               | 48.6 ms  | 49.3 ms: 1.01x slower  |
| dulwich_log                | 42.4 ms  | 43.0 ms: 1.01x slower  |
| async_tree_memoization     | 223 ms   | 227 ms: 1.02x slower   |
| sympy_integrate            | 13.6 ms  | 13.9 ms: 1.02x slower  |
| genshi_text                | 15.8 ms  | 16.2 ms: 1.02x slower  |
| logging_simple             | 6.53 us  | 6.67 us: 1.02x slower  |
| async_tree_io_tg           | 410 ms   | 419 ms: 1.02x slower   |
| regex_compile              | 86.1 ms  | 88.0 ms: 1.02x slower  |
| async_generators           | 219 ms   | 224 ms: 1.02x slower   |
| coroutines                 | 13.1 ms  | 13.5 ms: 1.02x slower  |
| pycparser                  | 745 ms   | 765 ms: 1.03x slower   |
| async_tree_io              | 417 ms   | 429 ms: 1.03x slower   |
| sqlglot_v2_normalize       | 76.3 ms  | 79.0 ms: 1.03x slower  |
| pathlib                    | 24.6 ms  | 25.6 ms: 1.04x slower  |
| pprint_pformat             | 1.09 sec | 1.13 sec: 1.04x slower |
| pylint                     | 208 ms   | 217 ms: 1.04x slower   |
| 2to3                       | 227 ms   | 237 ms: 1.05x slower   |
| unpickle_pure_python       | 147 us   | 154 us: 1.05x slower   |
| pprint_safe_repr           | 532 ms   | 558 ms: 1.05x slower   |
| meteor_contest             | 74.3 ms  | 78.1 ms: 1.05x slower  |
| sympy_str                  | 177 ms   | 187 ms: 1.06x slower   |
| nqueens                    | 62.2 ms  | 65.7 ms: 1.06x slower  |
| sympy_expand               | 305 ms   | 324 ms: 1.06x slower   |
| sympy_sum                  | 90.8 ms  | 96.6 ms: 1.06x slower  |
| docutils                   | 1.71 sec | 1.81 sec: 1.06x slower |
| typing_runtime_protocols   | 106 us   | 113 us: 1.06x slower   |
| async_tree_cpu_io_mixed    | 340 ms   | 362 ms: 1.07x slower   |
| async_tree_cpu_io_mixed_tg | 344 ms   | 367 ms: 1.07x slower   |
| scimark_lu                 | 61.1 ms  | 65.2 ms: 1.07x slower  |
| sqlite_synth               | 1.57 us  | 1.68 us: 1.07x slower  |
| deepcopy                   | 185 us   | 199 us: 1.07x slower   |
| thrift                     | 522 us   | 561 us: 1.07x slower   |
| django_template            | 25.5 ms  | 27.5 ms: 1.08x slower  |
| python_startup_no_site     | 18.7 ms  | 20.1 ms: 1.08x slower  |
| sqlglot_v2_optimize        | 35.6 ms  | 38.4 ms: 1.08x slower  |
| sphinx                     | 670 ms   | 723 ms: 1.08x slower   |
| bpe_tokeniser              | 2.93 sec | 3.17 sec: 1.08x slower |
| pickle_pure_python         | 217 us   | 236 us: 1.08x slower   |
| comprehensions             | 11.2 us  | 12.2 us: 1.09x slower  |
| python_startup             | 24.5 ms  | 26.9 ms: 1.10x slower  |
| logging_silent             | 57.0 ns  | 62.9 ns: 1.10x slower  |
| create_gc_cycles           | 1.25 ms  | 1.38 ms: 1.11x slower  |
| deepcopy_memo              | 19.1 us  | 21.3 us: 1.11x slower  |
| telco                      | 4.75 ms  | 5.33 ms: 1.12x slower  |
| deepcopy_reduce            | 1.88 us  | 2.12 us: 1.13x slower  |
| mako                       | 6.50 ms  | 7.44 ms: 1.14x slower  |
| coverage                   | 49.2 ms  | 56.4 ms: 1.15x slower  |
| subparsers                 | 41.0 ms  | 47.1 ms: 1.15x slower  |
| xml_etree_iterparse        | 62.3 ms  | 71.5 ms: 1.15x slower  |
| xml_etree_parse            | 88.8 ms  | 104 ms: 1.17x slower   |
| many_optionals             | 695 us   | 813 us: 1.17x slower   |
| xml_etree_process          | 39.7 ms  | 46.5 ms: 1.17x slower  |
| xml_etree_generate         | 56.8 ms  | 66.8 ms: 1.18x slower  |
| json_dumps                 | 6.69 ms  | 7.94 ms: 1.19x slower  |
| json                       | 3.16 ms  | 3.77 ms: 1.19x slower  |
| regex_v8                   | 13.8 ms  | 16.7 ms: 1.21x slower  |
| regex_effbot               | 1.46 ms  | 1.76 ms: 1.21x slower  |
| gc_traversal               | 2.07 ms  | 2.77 ms: 1.34x slower  |
| json_loads                 | 15.3 us  | 21.1 us: 1.38x slower  |
| Geometric mean             | (ref)    | 1.05x slower           |

Benchmark hidden because not significant (5): async_tree_memoization_tg, sqlglot_v2_transpile, spectral_norm, connected_components, k_core
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown