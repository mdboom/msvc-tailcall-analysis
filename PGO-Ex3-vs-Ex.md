# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | PGO-Ex3                |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 227 ms: 1.36x faster   |
| docutils       | 2.31 sec | 1.71 sec: 1.35x faster |
| html5lib       | 52.5 ms  | 40.5 ms: 1.30x faster  |
| sphinx         | 933 ms   | 670 ms: 1.39x faster   |
| Geometric mean | (ref)    | 1.35x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | PGO-Ex3               |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 13.1 ms: 1.71x faster |
| async_generators           | 348 ms  | 219 ms: 1.59x faster  |
| async_tree_none            | 267 ms  | 186 ms: 1.44x faster  |
| async_tree_io_tg           | 576 ms  | 410 ms: 1.40x faster  |
| async_tree_memoization     | 313 ms  | 223 ms: 1.40x faster  |
| async_tree_memoization_tg  | 304 ms  | 219 ms: 1.39x faster  |
| async_tree_none_tg         | 243 ms  | 176 ms: 1.38x faster  |
| async_tree_io              | 570 ms  | 417 ms: 1.37x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 340 ms: 1.34x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 344 ms: 1.29x faster  |
| asyncio_websockets         | 330 ms  | 311 ms: 1.06x faster  |
| Geometric mean             | (ref)   | 1.39x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 44.2 ms: 1.76x faster |
| nbody          | 103 ms  | 78.3 ms: 1.32x faster |
| pidigits       | 156 ms  | 148 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.35x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 86.1 ms: 1.51x faster |
| regex_effbot   | 1.87 ms | 1.46 ms: 1.28x faster |
| regex_v8       | 17.5 ms | 13.8 ms: 1.27x faster |
| regex_dna      | 123 ms  | 116 ms: 1.06x faster  |
| Geometric mean | (ref)   | 1.27x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | PGO-Ex3                |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 147 us: 1.94x faster   |
| xml_etree_process    | 66.9 ms  | 39.7 ms: 1.68x faster  |
| pickle_pure_python   | 364 us   | 217 us: 1.68x faster   |
| xml_etree_generate   | 92.6 ms  | 56.8 ms: 1.63x faster  |
| json_loads           | 23.3 us  | 15.3 us: 1.52x faster  |
| xml_etree_iterparse  | 94.3 ms  | 62.3 ms: 1.52x faster  |
| tomli_loads          | 2.07 sec | 1.44 sec: 1.44x faster |
| json_dumps           | 9.44 ms  | 6.69 ms: 1.41x faster  |
| xml_etree_parse      | 112 ms   | 88.8 ms: 1.27x faster  |
| Geometric mean       | (ref)    | 1.55x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | PGO-Ex3               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 24.5 ms: 1.20x faster |
| python_startup_no_site | 22.0 ms | 18.7 ms: 1.18x faster |
| Geometric mean         | (ref)   | 1.19x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | PGO-Ex3               |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.50 ms: 1.86x faster |
| genshi_text     | 23.9 ms | 15.8 ms: 1.51x faster |
| django_template | 38.0 ms | 25.5 ms: 1.49x faster |
| genshi_xml      | 50.4 ms | 35.0 ms: 1.44x faster |
| Geometric mean  | (ref)   | 1.57x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | PGO-Ex3                |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 57.0 ns: 2.18x faster  |
| scimark_lu                 | 119 ms   | 61.1 ms: 1.96x faster  |
| unpickle_pure_python       | 284 us   | 147 us: 1.94x faster   |
| deltablue                  | 4.22 ms  | 2.18 ms: 1.93x faster  |
| mako                       | 12.1 ms  | 6.50 ms: 1.86x faster  |
| comprehensions             | 20.1 us  | 11.2 us: 1.80x faster  |
| deepcopy_memo              | 34.0 us  | 19.1 us: 1.78x faster  |
| generators                 | 35.6 ms  | 20.0 ms: 1.78x faster  |
| float                      | 78.0 ms  | 44.2 ms: 1.76x faster  |
| spectral_norm              | 102 ms   | 58.1 ms: 1.75x faster  |
| hexiom                     | 7.44 ms  | 4.28 ms: 1.74x faster  |
| richards                   | 59.0 ms  | 34.5 ms: 1.71x faster  |
| coroutines                 | 22.4 ms  | 13.1 ms: 1.71x faster  |
| richards_super             | 67.7 ms  | 39.9 ms: 1.69x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.63 ms: 1.69x faster  |
| xml_etree_process          | 66.9 ms  | 39.7 ms: 1.68x faster  |
| pickle_pure_python         | 364 us   | 217 us: 1.68x faster   |
| scimark_monte_carlo        | 75.8 ms  | 45.3 ms: 1.67x faster  |
| go                         | 140 ms   | 84.1 ms: 1.67x faster  |
| crypto_pyaes               | 80.1 ms  | 48.6 ms: 1.65x faster  |
| scimark_sor                | 139 ms   | 84.2 ms: 1.65x faster  |
| chaos                      | 69.3 ms  | 42.2 ms: 1.64x faster  |
| xml_etree_generate         | 92.6 ms  | 56.8 ms: 1.63x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 870 us: 1.62x faster   |
| pyflate                    | 477 ms   | 300 ms: 1.59x faster   |
| async_generators           | 348 ms   | 219 ms: 1.59x faster   |
| fannkuch                   | 418 ms   | 263 ms: 1.59x faster   |
| gc_traversal               | 3.25 ms  | 2.07 ms: 1.57x faster  |
| nqueens                    | 96.9 ms  | 62.2 ms: 1.56x faster  |
| raytrace                   | 313 ms   | 201 ms: 1.55x faster   |
| pprint_safe_repr           | 825 ms   | 532 ms: 1.55x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 1.09 ms: 1.54x faster  |
| pprint_pformat             | 1.66 sec | 1.09 sec: 1.53x faster |
| deepcopy_reduce            | 2.86 us  | 1.88 us: 1.52x faster  |
| pathlib                    | 37.5 ms  | 24.6 ms: 1.52x faster  |
| json_loads                 | 23.3 us  | 15.3 us: 1.52x faster  |
| bpe_tokeniser              | 4.45 sec | 2.93 sec: 1.52x faster |
| xml_etree_iterparse        | 94.3 ms  | 62.3 ms: 1.52x faster  |
| genshi_text                | 23.9 ms  | 15.8 ms: 1.51x faster  |
| regex_compile              | 130 ms   | 86.1 ms: 1.51x faster  |
| deepcopy                   | 278 us   | 185 us: 1.50x faster   |
| django_template            | 38.0 ms  | 25.5 ms: 1.49x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 35.6 ms: 1.48x faster  |
| scimark_fft                | 276 ms   | 187 ms: 1.47x faster   |
| typing_runtime_protocols   | 154 us   | 106 us: 1.45x faster   |
| tomli_loads                | 2.07 sec | 1.44 sec: 1.44x faster |
| genshi_xml                 | 50.4 ms  | 35.0 ms: 1.44x faster  |
| async_tree_none            | 267 ms   | 186 ms: 1.44x faster   |
| sqlglot_v2_normalize       | 109 ms   | 76.3 ms: 1.43x faster  |
| logging_simple             | 9.30 us  | 6.53 us: 1.42x faster  |
| json_dumps                 | 9.44 ms  | 6.69 ms: 1.41x faster  |
| async_tree_io_tg           | 576 ms   | 410 ms: 1.40x faster   |
| async_tree_memoization     | 313 ms   | 223 ms: 1.40x faster   |
| sympy_str                  | 247 ms   | 177 ms: 1.40x faster   |
| logging_format             | 9.92 us  | 7.11 us: 1.40x faster  |
| sphinx                     | 933 ms   | 670 ms: 1.39x faster   |
| async_tree_memoization_tg  | 304 ms   | 219 ms: 1.39x faster   |
| async_tree_none_tg         | 243 ms   | 176 ms: 1.38x faster   |
| telco                      | 6.56 ms  | 4.75 ms: 1.38x faster  |
| sympy_expand               | 419 ms   | 305 ms: 1.37x faster   |
| async_tree_io              | 570 ms   | 417 ms: 1.37x faster   |
| 2to3                       | 309 ms   | 227 ms: 1.36x faster   |
| pycparser                  | 1.01 sec | 745 ms: 1.36x faster   |
| thrift                     | 710 us   | 522 us: 1.36x faster   |
| sympy_sum                  | 123 ms   | 90.8 ms: 1.36x faster  |
| sympy_integrate            | 18.4 ms  | 13.6 ms: 1.35x faster  |
| docutils                   | 2.31 sec | 1.71 sec: 1.35x faster |
| meteor_contest             | 99.5 ms  | 74.3 ms: 1.34x faster  |
| async_tree_cpu_io_mixed    | 455 ms   | 340 ms: 1.34x faster   |
| nbody                      | 103 ms   | 78.3 ms: 1.32x faster  |
| html5lib                   | 52.5 ms  | 40.5 ms: 1.30x faster  |
| coverage                   | 63.7 ms  | 49.2 ms: 1.29x faster  |
| pylint                     | 269 ms   | 208 ms: 1.29x faster   |
| json                       | 4.07 ms  | 3.16 ms: 1.29x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 344 ms: 1.29x faster   |
| regex_effbot               | 1.87 ms  | 1.46 ms: 1.28x faster  |
| regex_v8                   | 17.5 ms  | 13.8 ms: 1.27x faster  |
| xml_etree_parse            | 112 ms   | 88.8 ms: 1.27x faster  |
| k_core                     | 2.18 sec | 1.73 sec: 1.26x faster |
| sqlite_synth               | 1.96 us  | 1.57 us: 1.25x faster  |
| dulwich_log                | 52.4 ms  | 42.4 ms: 1.24x faster  |
| shortest_path              | 437 ms   | 354 ms: 1.23x faster   |
| connected_components       | 395 ms   | 324 ms: 1.22x faster   |
| python_startup             | 29.5 ms  | 24.5 ms: 1.20x faster  |
| python_startup_no_site     | 22.0 ms  | 18.7 ms: 1.18x faster  |
| mdp                        | 1.89 sec | 1.62 sec: 1.16x faster |
| create_gc_cycles           | 1.42 ms  | 1.25 ms: 1.14x faster  |
| asyncio_websockets         | 330 ms   | 311 ms: 1.06x faster   |
| regex_dna                  | 123 ms   | 116 ms: 1.06x faster   |
| pidigits                   | 156 ms   | 148 ms: 1.05x faster   |
| many_optionals             | 559 us   | 695 us: 1.24x slower   |
| subparsers                 | 21.5 ms  | 41.0 ms: 1.91x slower  |
| Geometric mean             | (ref)    | 1.44x faster           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown