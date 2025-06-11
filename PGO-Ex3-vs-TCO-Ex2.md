# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.374x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | PGO-Ex3                |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 227 ms: 1.29x faster   |
| docutils       | 2.11 sec | 1.71 sec: 1.23x faster |
| html5lib       | 51.3 ms  | 40.5 ms: 1.27x faster  |
| sphinx         | 843 ms   | 670 ms: 1.26x faster   |
| Geometric mean | (ref)    | 1.26x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | PGO-Ex3               |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 13.1 ms: 1.68x faster |
| async_generators           | 321 ms  | 219 ms: 1.47x faster  |
| async_tree_io_tg           | 563 ms  | 410 ms: 1.37x faster  |
| async_tree_none_tg         | 236 ms  | 176 ms: 1.34x faster  |
| async_tree_none            | 248 ms  | 186 ms: 1.34x faster  |
| async_tree_memoization_tg  | 292 ms  | 219 ms: 1.33x faster  |
| async_tree_memoization     | 297 ms  | 223 ms: 1.33x faster  |
| async_tree_io              | 551 ms  | 417 ms: 1.32x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 340 ms: 1.28x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 344 ms: 1.24x faster  |
| Geometric mean             | (ref)   | 1.33x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| float          | 73.5 ms | 44.2 ms: 1.66x faster |
| nbody          | 98.8 ms | 78.3 ms: 1.26x faster |
| Geometric mean | (ref)   | 1.28x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 86.1 ms: 1.43x faster |
| regex_v8       | 17.0 ms | 13.8 ms: 1.23x faster |
| regex_effbot   | 1.77 ms | 1.46 ms: 1.22x faster |
| regex_dna      | 118 ms  | 116 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.21x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | PGO-Ex3                |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 147 us: 1.85x faster   |
| pickle_pure_python   | 354 us   | 217 us: 1.63x faster   |
| xml_etree_process    | 63.0 ms  | 39.7 ms: 1.59x faster  |
| xml_etree_generate   | 87.5 ms  | 56.8 ms: 1.54x faster  |
| xml_etree_iterparse  | 87.5 ms  | 62.3 ms: 1.41x faster  |
| json_loads           | 21.4 us  | 15.3 us: 1.40x faster  |
| tomli_loads          | 1.97 sec | 1.44 sec: 1.37x faster |
| json_dumps           | 8.99 ms  | 6.69 ms: 1.35x faster  |
| xml_etree_parse      | 108 ms   | 88.8 ms: 1.22x faster  |
| Geometric mean       | (ref)    | 1.47x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | PGO-Ex3               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 24.5 ms: 1.11x faster |
| python_startup_no_site | 20.3 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | PGO-Ex3               |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 6.50 ms: 1.76x faster |
| genshi_text     | 23.4 ms | 15.8 ms: 1.47x faster |
| django_template | 35.8 ms | 25.5 ms: 1.40x faster |
| genshi_xml      | 48.8 ms | 35.0 ms: 1.39x faster |
| Geometric mean  | (ref)   | 1.50x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | PGO-Ex3                |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 121 ns   | 57.0 ns: 2.13x faster  |
| scimark_lu                 | 116 ms   | 61.1 ms: 1.90x faster  |
| deltablue                  | 4.08 ms  | 2.18 ms: 1.87x faster  |
| unpickle_pure_python       | 271 us   | 147 us: 1.85x faster   |
| mako                       | 11.4 ms  | 6.50 ms: 1.76x faster  |
| comprehensions             | 19.4 us  | 11.2 us: 1.74x faster  |
| deepcopy_memo              | 33.0 us  | 19.1 us: 1.73x faster  |
| hexiom                     | 7.27 ms  | 4.28 ms: 1.70x faster  |
| coroutines                 | 22.1 ms  | 13.1 ms: 1.68x faster  |
| generators                 | 33.5 ms  | 20.0 ms: 1.67x faster  |
| spectral_norm              | 97.1 ms  | 58.1 ms: 1.67x faster  |
| scimark_monte_carlo        | 75.2 ms  | 45.3 ms: 1.66x faster  |
| float                      | 73.5 ms  | 44.2 ms: 1.66x faster  |
| go                         | 138 ms   | 84.1 ms: 1.64x faster  |
| pickle_pure_python         | 354 us   | 217 us: 1.63x faster   |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.63 ms: 1.62x faster  |
| chaos                      | 67.0 ms  | 42.2 ms: 1.59x faster  |
| xml_etree_process          | 63.0 ms  | 39.7 ms: 1.59x faster  |
| scimark_sor                | 133 ms   | 84.2 ms: 1.58x faster  |
| crypto_pyaes               | 76.8 ms  | 48.6 ms: 1.58x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 870 us: 1.55x faster   |
| xml_etree_generate         | 87.5 ms  | 56.8 ms: 1.54x faster  |
| pyflate                    | 457 ms   | 300 ms: 1.52x faster   |
| raytrace                   | 306 ms   | 201 ms: 1.52x faster   |
| nqueens                    | 93.2 ms  | 62.2 ms: 1.50x faster  |
| pprint_pformat             | 1.61 sec | 1.09 sec: 1.48x faster |
| pprint_safe_repr           | 789 ms   | 532 ms: 1.48x faster   |
| richards                   | 51.0 ms  | 34.5 ms: 1.48x faster  |
| sqlglot_v2_transpile       | 1.62 ms  | 1.09 ms: 1.48x faster  |
| genshi_text                | 23.4 ms  | 15.8 ms: 1.47x faster  |
| async_generators           | 321 ms   | 219 ms: 1.47x faster   |
| bpe_tokeniser              | 4.30 sec | 2.93 sec: 1.47x faster |
| fannkuch                   | 386 ms   | 263 ms: 1.47x faster   |
| richards_super             | 58.0 ms  | 39.9 ms: 1.45x faster  |
| deepcopy_reduce            | 2.71 us  | 1.88 us: 1.44x faster  |
| deepcopy                   | 266 us   | 185 us: 1.44x faster   |
| scimark_fft                | 267 ms   | 187 ms: 1.43x faster   |
| regex_compile              | 123 ms   | 86.1 ms: 1.43x faster  |
| xml_etree_iterparse        | 87.5 ms  | 62.3 ms: 1.41x faster  |
| django_template            | 35.8 ms  | 25.5 ms: 1.40x faster  |
| json_loads                 | 21.4 us  | 15.3 us: 1.40x faster  |
| genshi_xml                 | 48.8 ms  | 35.0 ms: 1.39x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 35.6 ms: 1.39x faster  |
| typing_runtime_protocols   | 146 us   | 106 us: 1.38x faster   |
| async_tree_io_tg           | 563 ms   | 410 ms: 1.37x faster   |
| tomli_loads                | 1.97 sec | 1.44 sec: 1.37x faster |
| sqlglot_v2_normalize       | 103 ms   | 76.3 ms: 1.36x faster  |
| gc_traversal               | 2.79 ms  | 2.07 ms: 1.35x faster  |
| json_dumps                 | 8.99 ms  | 6.69 ms: 1.35x faster  |
| async_tree_none_tg         | 236 ms   | 176 ms: 1.34x faster   |
| async_tree_none            | 248 ms   | 186 ms: 1.34x faster   |
| telco                      | 6.34 ms  | 4.75 ms: 1.33x faster  |
| async_tree_memoization_tg  | 292 ms   | 219 ms: 1.33x faster   |
| async_tree_memoization     | 297 ms   | 223 ms: 1.33x faster   |
| sympy_str                  | 234 ms   | 177 ms: 1.33x faster   |
| async_tree_io              | 551 ms   | 417 ms: 1.32x faster   |
| logging_simple             | 8.63 us  | 6.53 us: 1.32x faster  |
| sympy_expand               | 399 ms   | 305 ms: 1.31x faster   |
| thrift                     | 680 us   | 522 us: 1.30x faster   |
| pycparser                  | 968 ms   | 745 ms: 1.30x faster   |
| sympy_sum                  | 118 ms   | 90.8 ms: 1.30x faster  |
| 2to3                       | 293 ms   | 227 ms: 1.29x faster   |
| sympy_integrate            | 17.5 ms  | 13.6 ms: 1.29x faster  |
| logging_format             | 9.13 us  | 7.11 us: 1.28x faster  |
| many_optionals             | 890 us   | 695 us: 1.28x faster   |
| meteor_contest             | 95.0 ms  | 74.3 ms: 1.28x faster  |
| async_tree_cpu_io_mixed    | 434 ms   | 340 ms: 1.28x faster   |
| html5lib                   | 51.3 ms  | 40.5 ms: 1.27x faster  |
| nbody                      | 98.8 ms  | 78.3 ms: 1.26x faster  |
| sphinx                     | 843 ms   | 670 ms: 1.26x faster   |
| json                       | 3.94 ms  | 3.16 ms: 1.25x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms   | 344 ms: 1.24x faster   |
| coverage                   | 61.1 ms  | 49.2 ms: 1.24x faster  |
| docutils                   | 2.11 sec | 1.71 sec: 1.23x faster |
| regex_v8                   | 17.0 ms  | 13.8 ms: 1.23x faster  |
| subparsers                 | 50.4 ms  | 41.0 ms: 1.23x faster  |
| regex_effbot               | 1.77 ms  | 1.46 ms: 1.22x faster  |
| xml_etree_parse            | 108 ms   | 88.8 ms: 1.22x faster  |
| pylint                     | 249 ms   | 208 ms: 1.19x faster   |
| dulwich_log                | 50.5 ms  | 42.4 ms: 1.19x faster  |
| sqlite_synth               | 1.78 us  | 1.57 us: 1.14x faster  |
| mdp                        | 1.82 sec | 1.62 sec: 1.12x faster |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.12x faster  |
| python_startup             | 27.2 ms  | 24.5 ms: 1.11x faster  |
| pathlib                    | 26.8 ms  | 24.6 ms: 1.09x faster  |
| python_startup_no_site     | 20.3 ms  | 18.7 ms: 1.09x faster  |
| shortest_path              | 384 ms   | 354 ms: 1.08x faster   |
| connected_components       | 351 ms   | 324 ms: 1.08x faster   |
| k_core                     | 1.83 sec | 1.73 sec: 1.06x faster |
| regex_dna                  | 118 ms   | 116 ms: 1.01x faster   |
| Geometric mean             | (ref)    | 1.38x faster           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: unknown