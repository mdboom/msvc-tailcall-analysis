# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.272x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 293 ms: 1.29x slower   |
| docutils       | 1.71 sec | 2.11 sec: 1.23x slower |
| html5lib       | 40.5 ms  | 51.3 ms: 1.27x slower  |
| sphinx         | 670 ms   | 843 ms: 1.26x slower   |
| Geometric mean | (ref)    | 1.26x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 344 ms  | 428 ms: 1.24x slower  |
| async_tree_cpu_io_mixed    | 340 ms  | 434 ms: 1.28x slower  |
| async_tree_io              | 417 ms  | 551 ms: 1.32x slower  |
| async_tree_memoization     | 223 ms  | 297 ms: 1.33x slower  |
| async_tree_memoization_tg  | 219 ms  | 292 ms: 1.33x slower  |
| async_tree_none            | 186 ms  | 248 ms: 1.34x slower  |
| async_tree_none_tg         | 176 ms  | 236 ms: 1.34x slower  |
| async_tree_io_tg           | 410 ms  | 563 ms: 1.37x slower  |
| async_generators           | 219 ms  | 321 ms: 1.47x slower  |
| coroutines                 | 13.1 ms | 22.1 ms: 1.68x slower |
| Geometric mean             | (ref)   | 1.33x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 98.8 ms: 1.26x slower |
| float          | 44.2 ms | 73.5 ms: 1.66x slower |
| Geometric mean | (ref)   | 1.28x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_dna      | 116 ms  | 118 ms: 1.01x slower  |
| regex_effbot   | 1.46 ms | 1.77 ms: 1.22x slower |
| regex_v8       | 13.8 ms | 17.0 ms: 1.23x slower |
| regex_compile  | 86.1 ms | 123 ms: 1.43x slower  |
| Geometric mean | (ref)   | 1.21x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 88.8 ms  | 108 ms: 1.22x slower   |
| json_dumps           | 6.69 ms  | 8.99 ms: 1.35x slower  |
| tomli_loads          | 1.44 sec | 1.97 sec: 1.37x slower |
| json_loads           | 15.3 us  | 21.4 us: 1.40x slower  |
| xml_etree_iterparse  | 62.3 ms  | 87.5 ms: 1.41x slower  |
| xml_etree_generate   | 56.8 ms  | 87.5 ms: 1.54x slower  |
| xml_etree_process    | 39.7 ms  | 63.0 ms: 1.59x slower  |
| pickle_pure_python   | 217 us   | 354 us: 1.63x slower   |
| unpickle_pure_python | 147 us   | 271 us: 1.85x slower   |
| Geometric mean       | (ref)    | 1.47x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | TCO-Ex2               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 20.3 ms: 1.09x slower |
| python_startup         | 24.5 ms | 27.2 ms: 1.11x slower |
| Geometric mean         | (ref)   | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 48.8 ms: 1.39x slower |
| django_template | 25.5 ms | 35.8 ms: 1.40x slower |
| genshi_text     | 15.8 ms | 23.4 ms: 1.47x slower |
| mako            | 6.50 ms | 11.4 ms: 1.76x slower |
| Geometric mean  | (ref)   | 1.50x slower          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| regex_dna                  | 116 ms   | 118 ms: 1.01x slower   |
| k_core                     | 1.73 sec | 1.83 sec: 1.06x slower |
| connected_components       | 324 ms   | 351 ms: 1.08x slower   |
| shortest_path              | 354 ms   | 384 ms: 1.08x slower   |
| python_startup_no_site     | 18.7 ms  | 20.3 ms: 1.09x slower  |
| pathlib                    | 24.6 ms  | 26.8 ms: 1.09x slower  |
| python_startup             | 24.5 ms  | 27.2 ms: 1.11x slower  |
| create_gc_cycles           | 1.25 ms  | 1.40 ms: 1.12x slower  |
| mdp                        | 1.62 sec | 1.82 sec: 1.12x slower |
| sqlite_synth               | 1.57 us  | 1.78 us: 1.14x slower  |
| dulwich_log                | 42.4 ms  | 50.5 ms: 1.19x slower  |
| pylint                     | 208 ms   | 249 ms: 1.19x slower   |
| xml_etree_parse            | 88.8 ms  | 108 ms: 1.22x slower   |
| regex_effbot               | 1.46 ms  | 1.77 ms: 1.22x slower  |
| subparsers                 | 41.0 ms  | 50.4 ms: 1.23x slower  |
| regex_v8                   | 13.8 ms  | 17.0 ms: 1.23x slower  |
| docutils                   | 1.71 sec | 2.11 sec: 1.23x slower |
| coverage                   | 49.2 ms  | 61.1 ms: 1.24x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms   | 428 ms: 1.24x slower   |
| json                       | 3.16 ms  | 3.94 ms: 1.25x slower  |
| sphinx                     | 670 ms   | 843 ms: 1.26x slower   |
| nbody                      | 78.3 ms  | 98.8 ms: 1.26x slower  |
| html5lib                   | 40.5 ms  | 51.3 ms: 1.27x slower  |
| async_tree_cpu_io_mixed    | 340 ms   | 434 ms: 1.28x slower   |
| meteor_contest             | 74.3 ms  | 95.0 ms: 1.28x slower  |
| many_optionals             | 695 us   | 890 us: 1.28x slower   |
| logging_format             | 7.11 us  | 9.13 us: 1.28x slower  |
| sympy_integrate            | 13.6 ms  | 17.5 ms: 1.29x slower  |
| 2to3                       | 227 ms   | 293 ms: 1.29x slower   |
| sympy_sum                  | 90.8 ms  | 118 ms: 1.30x slower   |
| pycparser                  | 745 ms   | 968 ms: 1.30x slower   |
| thrift                     | 522 us   | 680 us: 1.30x slower   |
| sympy_expand               | 305 ms   | 399 ms: 1.31x slower   |
| logging_simple             | 6.53 us  | 8.63 us: 1.32x slower  |
| async_tree_io              | 417 ms   | 551 ms: 1.32x slower   |
| sympy_str                  | 177 ms   | 234 ms: 1.33x slower   |
| async_tree_memoization     | 223 ms   | 297 ms: 1.33x slower   |
| async_tree_memoization_tg  | 219 ms   | 292 ms: 1.33x slower   |
| telco                      | 4.75 ms  | 6.34 ms: 1.33x slower  |
| async_tree_none            | 186 ms   | 248 ms: 1.34x slower   |
| async_tree_none_tg         | 176 ms   | 236 ms: 1.34x slower   |
| json_dumps                 | 6.69 ms  | 8.99 ms: 1.35x slower  |
| gc_traversal               | 2.07 ms  | 2.79 ms: 1.35x slower  |
| sqlglot_v2_normalize       | 76.3 ms  | 103 ms: 1.36x slower   |
| tomli_loads                | 1.44 sec | 1.97 sec: 1.37x slower |
| async_tree_io_tg           | 410 ms   | 563 ms: 1.37x slower   |
| typing_runtime_protocols   | 106 us   | 146 us: 1.38x slower   |
| sqlglot_v2_optimize        | 35.6 ms  | 49.6 ms: 1.39x slower  |
| genshi_xml                 | 35.0 ms  | 48.8 ms: 1.39x slower  |
| json_loads                 | 15.3 us  | 21.4 us: 1.40x slower  |
| django_template            | 25.5 ms  | 35.8 ms: 1.40x slower  |
| xml_etree_iterparse        | 62.3 ms  | 87.5 ms: 1.41x slower  |
| regex_compile              | 86.1 ms  | 123 ms: 1.43x slower   |
| scimark_fft                | 187 ms   | 267 ms: 1.43x slower   |
| deepcopy                   | 185 us   | 266 us: 1.44x slower   |
| deepcopy_reduce            | 1.88 us  | 2.71 us: 1.44x slower  |
| richards_super             | 39.9 ms  | 58.0 ms: 1.45x slower  |
| fannkuch                   | 263 ms   | 386 ms: 1.47x slower   |
| bpe_tokeniser              | 2.93 sec | 4.30 sec: 1.47x slower |
| async_generators           | 219 ms   | 321 ms: 1.47x slower   |
| genshi_text                | 15.8 ms  | 23.4 ms: 1.47x slower  |
| sqlglot_v2_transpile       | 1.09 ms  | 1.62 ms: 1.48x slower  |
| richards                   | 34.5 ms  | 51.0 ms: 1.48x slower  |
| pprint_safe_repr           | 532 ms   | 789 ms: 1.48x slower   |
| pprint_pformat             | 1.09 sec | 1.61 sec: 1.48x slower |
| nqueens                    | 62.2 ms  | 93.2 ms: 1.50x slower  |
| raytrace                   | 201 ms   | 306 ms: 1.52x slower   |
| pyflate                    | 300 ms   | 457 ms: 1.52x slower   |
| xml_etree_generate         | 56.8 ms  | 87.5 ms: 1.54x slower  |
| sqlglot_v2_parse           | 870 us   | 1.34 ms: 1.55x slower  |
| crypto_pyaes               | 48.6 ms  | 76.8 ms: 1.58x slower  |
| scimark_sor                | 84.2 ms  | 133 ms: 1.58x slower   |
| xml_etree_process          | 39.7 ms  | 63.0 ms: 1.59x slower  |
| chaos                      | 42.2 ms  | 67.0 ms: 1.59x slower  |
| scimark_sparse_mat_mult    | 2.63 ms  | 4.27 ms: 1.62x slower  |
| pickle_pure_python         | 217 us   | 354 us: 1.63x slower   |
| go                         | 84.1 ms  | 138 ms: 1.64x slower   |
| float                      | 44.2 ms  | 73.5 ms: 1.66x slower  |
| scimark_monte_carlo        | 45.3 ms  | 75.2 ms: 1.66x slower  |
| spectral_norm              | 58.1 ms  | 97.1 ms: 1.67x slower  |
| generators                 | 20.0 ms  | 33.5 ms: 1.67x slower  |
| coroutines                 | 13.1 ms  | 22.1 ms: 1.68x slower  |
| hexiom                     | 4.28 ms  | 7.27 ms: 1.70x slower  |
| deepcopy_memo              | 19.1 us  | 33.0 us: 1.73x slower  |
| comprehensions             | 11.2 us  | 19.4 us: 1.74x slower  |
| mako                       | 6.50 ms  | 11.4 ms: 1.76x slower  |
| unpickle_pure_python       | 147 us   | 271 us: 1.85x slower   |
| deltablue                  | 2.18 ms  | 4.08 ms: 1.87x slower  |
| scimark_lu                 | 61.1 ms  | 116 ms: 1.90x slower   |
| logging_silent             | 57.0 ns  | 121 ns: 2.13x slower   |
| Geometric mean             | (ref)    | 1.38x slower           |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.272x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.29x

# Memory
- memory change: unknown