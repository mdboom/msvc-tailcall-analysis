# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.301x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | Ex                     |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 309 ms: 1.36x slower   |
| docutils       | 1.71 sec | 2.31 sec: 1.35x slower |
| html5lib       | 40.5 ms  | 52.5 ms: 1.30x slower  |
| sphinx         | 670 ms   | 933 ms: 1.39x slower   |
| Geometric mean | (ref)    | 1.35x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | Ex                    |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 311 ms  | 330 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 444 ms: 1.29x slower  |
| async_tree_cpu_io_mixed    | 340 ms  | 455 ms: 1.34x slower  |
| async_tree_io              | 417 ms  | 570 ms: 1.37x slower  |
| async_tree_none_tg         | 176 ms  | 243 ms: 1.38x slower  |
| async_tree_memoization_tg  | 219 ms  | 304 ms: 1.39x slower  |
| async_tree_memoization     | 223 ms  | 313 ms: 1.40x slower  |
| async_tree_io_tg           | 410 ms  | 576 ms: 1.40x slower  |
| async_tree_none            | 186 ms  | 267 ms: 1.44x slower  |
| async_generators           | 219 ms  | 348 ms: 1.59x slower  |
| coroutines                 | 13.1 ms | 22.4 ms: 1.71x slower |
| Geometric mean             | (ref)   | 1.39x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | Ex                    |
|----------------|:-------:|:---------------------:|
| pidigits       | 148 ms  | 156 ms: 1.05x slower  |
| nbody          | 78.3 ms | 103 ms: 1.32x slower  |
| float          | 44.2 ms | 78.0 ms: 1.76x slower |
| Geometric mean | (ref)   | 1.35x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | Ex                    |
|----------------|:-------:|:---------------------:|
| regex_dna      | 116 ms  | 123 ms: 1.06x slower  |
| regex_v8       | 13.8 ms | 17.5 ms: 1.27x slower |
| regex_effbot   | 1.46 ms | 1.87 ms: 1.28x slower |
| regex_compile  | 86.1 ms | 130 ms: 1.51x slower  |
| Geometric mean | (ref)   | 1.27x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | Ex                     |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 88.8 ms  | 112 ms: 1.27x slower   |
| json_dumps           | 6.69 ms  | 9.44 ms: 1.41x slower  |
| tomli_loads          | 1.44 sec | 2.07 sec: 1.44x slower |
| xml_etree_iterparse  | 62.3 ms  | 94.3 ms: 1.52x slower  |
| json_loads           | 15.3 us  | 23.3 us: 1.52x slower  |
| xml_etree_generate   | 56.8 ms  | 92.6 ms: 1.63x slower  |
| pickle_pure_python   | 217 us   | 364 us: 1.68x slower   |
| xml_etree_process    | 39.7 ms  | 66.9 ms: 1.68x slower  |
| unpickle_pure_python | 147 us   | 284 us: 1.94x slower   |
| Geometric mean       | (ref)    | 1.55x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | Ex                    |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 22.0 ms: 1.18x slower |
| python_startup         | 24.5 ms | 29.5 ms: 1.20x slower |
| Geometric mean         | (ref)   | 1.19x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | Ex                    |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 50.4 ms: 1.44x slower |
| django_template | 25.5 ms | 38.0 ms: 1.49x slower |
| genshi_text     | 15.8 ms | 23.9 ms: 1.51x slower |
| mako            | 6.50 ms | 12.1 ms: 1.86x slower |
| Geometric mean  | (ref)   | 1.57x slower          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | Ex                     |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 41.0 ms  | 21.5 ms: 1.91x faster  |
| many_optionals             | 695 us   | 559 us: 1.24x faster   |
| pidigits                   | 148 ms   | 156 ms: 1.05x slower   |
| regex_dna                  | 116 ms   | 123 ms: 1.06x slower   |
| asyncio_websockets         | 311 ms   | 330 ms: 1.06x slower   |
| create_gc_cycles           | 1.25 ms  | 1.42 ms: 1.14x slower  |
| mdp                        | 1.62 sec | 1.89 sec: 1.16x slower |
| python_startup_no_site     | 18.7 ms  | 22.0 ms: 1.18x slower  |
| python_startup             | 24.5 ms  | 29.5 ms: 1.20x slower  |
| connected_components       | 324 ms   | 395 ms: 1.22x slower   |
| shortest_path              | 354 ms   | 437 ms: 1.23x slower   |
| dulwich_log                | 42.4 ms  | 52.4 ms: 1.24x slower  |
| sqlite_synth               | 1.57 us  | 1.96 us: 1.25x slower  |
| k_core                     | 1.73 sec | 2.18 sec: 1.26x slower |
| xml_etree_parse            | 88.8 ms  | 112 ms: 1.27x slower   |
| regex_v8                   | 13.8 ms  | 17.5 ms: 1.27x slower  |
| regex_effbot               | 1.46 ms  | 1.87 ms: 1.28x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms   | 444 ms: 1.29x slower   |
| json                       | 3.16 ms  | 4.07 ms: 1.29x slower  |
| pylint                     | 208 ms   | 269 ms: 1.29x slower   |
| coverage                   | 49.2 ms  | 63.7 ms: 1.29x slower  |
| html5lib                   | 40.5 ms  | 52.5 ms: 1.30x slower  |
| nbody                      | 78.3 ms  | 103 ms: 1.32x slower   |
| async_tree_cpu_io_mixed    | 340 ms   | 455 ms: 1.34x slower   |
| meteor_contest             | 74.3 ms  | 99.5 ms: 1.34x slower  |
| docutils                   | 1.71 sec | 2.31 sec: 1.35x slower |
| sympy_integrate            | 13.6 ms  | 18.4 ms: 1.35x slower  |
| sympy_sum                  | 90.8 ms  | 123 ms: 1.36x slower   |
| thrift                     | 522 us   | 710 us: 1.36x slower   |
| pycparser                  | 745 ms   | 1.01 sec: 1.36x slower |
| 2to3                       | 227 ms   | 309 ms: 1.36x slower   |
| async_tree_io              | 417 ms   | 570 ms: 1.37x slower   |
| sympy_expand               | 305 ms   | 419 ms: 1.37x slower   |
| telco                      | 4.75 ms  | 6.56 ms: 1.38x slower  |
| async_tree_none_tg         | 176 ms   | 243 ms: 1.38x slower   |
| async_tree_memoization_tg  | 219 ms   | 304 ms: 1.39x slower   |
| sphinx                     | 670 ms   | 933 ms: 1.39x slower   |
| logging_format             | 7.11 us  | 9.92 us: 1.40x slower  |
| sympy_str                  | 177 ms   | 247 ms: 1.40x slower   |
| async_tree_memoization     | 223 ms   | 313 ms: 1.40x slower   |
| async_tree_io_tg           | 410 ms   | 576 ms: 1.40x slower   |
| json_dumps                 | 6.69 ms  | 9.44 ms: 1.41x slower  |
| logging_simple             | 6.53 us  | 9.30 us: 1.42x slower  |
| sqlglot_v2_normalize       | 76.3 ms  | 109 ms: 1.43x slower   |
| async_tree_none            | 186 ms   | 267 ms: 1.44x slower   |
| genshi_xml                 | 35.0 ms  | 50.4 ms: 1.44x slower  |
| tomli_loads                | 1.44 sec | 2.07 sec: 1.44x slower |
| typing_runtime_protocols   | 106 us   | 154 us: 1.45x slower   |
| scimark_fft                | 187 ms   | 276 ms: 1.47x slower   |
| sqlglot_v2_optimize        | 35.6 ms  | 52.8 ms: 1.48x slower  |
| django_template            | 25.5 ms  | 38.0 ms: 1.49x slower  |
| deepcopy                   | 185 us   | 278 us: 1.50x slower   |
| regex_compile              | 86.1 ms  | 130 ms: 1.51x slower   |
| genshi_text                | 15.8 ms  | 23.9 ms: 1.51x slower  |
| xml_etree_iterparse        | 62.3 ms  | 94.3 ms: 1.52x slower  |
| bpe_tokeniser              | 2.93 sec | 4.45 sec: 1.52x slower |
| json_loads                 | 15.3 us  | 23.3 us: 1.52x slower  |
| pathlib                    | 24.6 ms  | 37.5 ms: 1.52x slower  |
| deepcopy_reduce            | 1.88 us  | 2.86 us: 1.52x slower  |
| pprint_pformat             | 1.09 sec | 1.66 sec: 1.53x slower |
| sqlglot_v2_transpile       | 1.09 ms  | 1.69 ms: 1.54x slower  |
| pprint_safe_repr           | 532 ms   | 825 ms: 1.55x slower   |
| raytrace                   | 201 ms   | 313 ms: 1.55x slower   |
| nqueens                    | 62.2 ms  | 96.9 ms: 1.56x slower  |
| gc_traversal               | 2.07 ms  | 3.25 ms: 1.57x slower  |
| fannkuch                   | 263 ms   | 418 ms: 1.59x slower   |
| async_generators           | 219 ms   | 348 ms: 1.59x slower   |
| pyflate                    | 300 ms   | 477 ms: 1.59x slower   |
| sqlglot_v2_parse           | 870 us   | 1.41 ms: 1.62x slower  |
| xml_etree_generate         | 56.8 ms  | 92.6 ms: 1.63x slower  |
| chaos                      | 42.2 ms  | 69.3 ms: 1.64x slower  |
| scimark_sor                | 84.2 ms  | 139 ms: 1.65x slower   |
| crypto_pyaes               | 48.6 ms  | 80.1 ms: 1.65x slower  |
| go                         | 84.1 ms  | 140 ms: 1.67x slower   |
| scimark_monte_carlo        | 45.3 ms  | 75.8 ms: 1.67x slower  |
| pickle_pure_python         | 217 us   | 364 us: 1.68x slower   |
| xml_etree_process          | 39.7 ms  | 66.9 ms: 1.68x slower  |
| scimark_sparse_mat_mult    | 2.63 ms  | 4.43 ms: 1.69x slower  |
| richards_super             | 39.9 ms  | 67.7 ms: 1.69x slower  |
| coroutines                 | 13.1 ms  | 22.4 ms: 1.71x slower  |
| richards                   | 34.5 ms  | 59.0 ms: 1.71x slower  |
| hexiom                     | 4.28 ms  | 7.44 ms: 1.74x slower  |
| spectral_norm              | 58.1 ms  | 102 ms: 1.75x slower   |
| float                      | 44.2 ms  | 78.0 ms: 1.76x slower  |
| generators                 | 20.0 ms  | 35.6 ms: 1.78x slower  |
| deepcopy_memo              | 19.1 us  | 34.0 us: 1.78x slower  |
| comprehensions             | 11.2 us  | 20.1 us: 1.80x slower  |
| mako                       | 6.50 ms  | 12.1 ms: 1.86x slower  |
| deltablue                  | 2.18 ms  | 4.22 ms: 1.93x slower  |
| unpickle_pure_python       | 147 us   | 284 us: 1.94x slower   |
| scimark_lu                 | 61.1 ms  | 119 ms: 1.96x slower   |
| logging_silent             | 57.0 ns  | 124 ns: 2.18x slower   |
| Geometric mean             | (ref)    | 1.44x slower           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.301x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.38x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: unknown