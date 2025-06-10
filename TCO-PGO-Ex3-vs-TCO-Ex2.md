# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.497x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 215 ms: 1.36x faster   |
| docutils       | 2.11 sec | 1.66 sec: 1.27x faster |
| html5lib       | 51.3 ms  | 37.8 ms: 1.36x faster  |
| sphinx         | 843 ms   | 641 ms: 1.31x faster   |
| Geometric mean | (ref)    | 1.33x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 12.0 ms: 1.85x faster |
| async_generators           | 321 ms  | 201 ms: 1.60x faster  |
| async_tree_io_tg           | 563 ms  | 377 ms: 1.49x faster  |
| async_tree_none_tg         | 236 ms  | 161 ms: 1.47x faster  |
| async_tree_none            | 248 ms  | 170 ms: 1.46x faster  |
| async_tree_memoization     | 297 ms  | 205 ms: 1.45x faster  |
| async_tree_io              | 551 ms  | 382 ms: 1.44x faster  |
| async_tree_memoization_tg  | 292 ms  | 208 ms: 1.41x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 330 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 330 ms: 1.30x faster  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 55.6 ms: 1.78x faster |
| float          | 73.5 ms | 42.0 ms: 1.75x faster |
| pidigits       | 148 ms  | 145 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.47x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 79.4 ms: 1.55x faster |
| regex_effbot   | 1.77 ms | 1.47 ms: 1.21x faster |
| regex_v8       | 17.0 ms | 14.2 ms: 1.19x faster |
| regex_dna      | 118 ms  | 120 ms: 1.02x slower  |
| Geometric mean | (ref)   | 1.22x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 124 us: 2.19x faster   |
| pickle_pure_python   | 354 us   | 199 us: 1.78x faster   |
| xml_etree_process    | 63.0 ms  | 36.8 ms: 1.71x faster  |
| tomli_loads          | 1.97 sec | 1.17 sec: 1.67x faster |
| xml_etree_generate   | 87.5 ms  | 53.1 ms: 1.65x faster  |
| json_loads           | 21.4 us  | 14.5 us: 1.48x faster  |
| xml_etree_iterparse  | 87.5 ms  | 61.2 ms: 1.43x faster  |
| json_dumps           | 8.99 ms  | 6.40 ms: 1.40x faster  |
| xml_etree_parse      | 108 ms   | 89.4 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.59x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 24.7 ms: 1.10x faster |
| python_startup_no_site | 20.3 ms | 18.6 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 6.25 ms: 1.83x faster |
| genshi_text     | 23.4 ms | 14.3 ms: 1.64x faster |
| django_template | 35.8 ms | 23.6 ms: 1.52x faster |
| genshi_xml      | 48.8 ms | 32.3 ms: 1.51x faster |
| Geometric mean  | (ref)   | 1.62x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 121 ns   | 49.7 ns: 2.45x faster  |
| scimark_lu                 | 116 ms   | 50.3 ms: 2.30x faster  |
| scimark_sor                | 133 ms   | 60.5 ms: 2.20x faster  |
| unpickle_pure_python       | 271 us   | 124 us: 2.19x faster   |
| deltablue                  | 4.08 ms  | 1.88 ms: 2.16x faster  |
| scimark_monte_carlo        | 75.2 ms  | 35.6 ms: 2.11x faster  |
| hexiom                     | 7.27 ms  | 3.49 ms: 2.08x faster  |
| generators                 | 33.5 ms  | 16.5 ms: 2.03x faster  |
| comprehensions             | 19.4 us  | 9.76 us: 1.99x faster  |
| spectral_norm              | 97.1 ms  | 49.4 ms: 1.96x faster  |
| go                         | 138 ms   | 70.5 ms: 1.96x faster  |
| deepcopy_memo              | 33.0 us  | 16.8 us: 1.96x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.21 ms: 1.93x faster  |
| raytrace                   | 306 ms   | 162 ms: 1.89x faster   |
| chaos                      | 67.0 ms  | 35.4 ms: 1.89x faster  |
| coroutines                 | 22.1 ms  | 12.0 ms: 1.85x faster  |
| mako                       | 11.4 ms  | 6.25 ms: 1.83x faster  |
| pickle_pure_python         | 354 us   | 199 us: 1.78x faster   |
| nbody                      | 98.8 ms  | 55.6 ms: 1.78x faster  |
| float                      | 73.5 ms  | 42.0 ms: 1.75x faster  |
| crypto_pyaes               | 76.8 ms  | 43.9 ms: 1.75x faster  |
| scimark_fft                | 267 ms   | 153 ms: 1.74x faster   |
| richards                   | 51.0 ms  | 29.4 ms: 1.74x faster  |
| pyflate                    | 457 ms   | 264 ms: 1.73x faster   |
| richards_super             | 58.0 ms  | 33.7 ms: 1.72x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 781 us: 1.72x faster   |
| fannkuch                   | 386 ms   | 225 ms: 1.72x faster   |
| xml_etree_process          | 63.0 ms  | 36.8 ms: 1.71x faster  |
| pprint_pformat             | 1.61 sec | 956 ms: 1.69x faster   |
| nqueens                    | 93.2 ms  | 55.2 ms: 1.69x faster  |
| tomli_loads                | 1.97 sec | 1.17 sec: 1.67x faster |
| pprint_safe_repr           | 789 ms   | 474 ms: 1.66x faster   |
| xml_etree_generate         | 87.5 ms  | 53.1 ms: 1.65x faster  |
| genshi_text                | 23.4 ms  | 14.3 ms: 1.64x faster  |
| sqlglot_v2_transpile       | 1.62 ms  | 993 us: 1.63x faster   |
| deepcopy_reduce            | 2.71 us  | 1.68 us: 1.62x faster  |
| async_generators           | 321 ms   | 201 ms: 1.60x faster   |
| deepcopy                   | 266 us   | 167 us: 1.59x faster   |
| bpe_tokeniser              | 4.30 sec | 2.72 sec: 1.58x faster |
| regex_compile              | 123 ms   | 79.4 ms: 1.55x faster  |
| django_template            | 35.8 ms  | 23.6 ms: 1.52x faster  |
| genshi_xml                 | 48.8 ms  | 32.3 ms: 1.51x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 32.9 ms: 1.50x faster  |
| sqlglot_v2_normalize       | 103 ms   | 69.0 ms: 1.50x faster  |
| typing_runtime_protocols   | 146 us   | 97.8 us: 1.50x faster  |
| async_tree_io_tg           | 563 ms   | 377 ms: 1.49x faster   |
| json_loads                 | 21.4 us  | 14.5 us: 1.48x faster  |
| logging_simple             | 8.63 us  | 5.87 us: 1.47x faster  |
| async_tree_none_tg         | 236 ms   | 161 ms: 1.47x faster   |
| async_tree_none            | 248 ms   | 170 ms: 1.46x faster   |
| async_tree_memoization     | 297 ms   | 205 ms: 1.45x faster   |
| async_tree_io              | 551 ms   | 382 ms: 1.44x faster   |
| xml_etree_iterparse        | 87.5 ms  | 61.2 ms: 1.43x faster  |
| logging_format             | 9.13 us  | 6.42 us: 1.42x faster  |
| sympy_expand               | 399 ms   | 283 ms: 1.41x faster   |
| async_tree_memoization_tg  | 292 ms   | 208 ms: 1.41x faster   |
| pycparser                  | 968 ms   | 689 ms: 1.40x faster   |
| json_dumps                 | 8.99 ms  | 6.40 ms: 1.40x faster  |
| thrift                     | 680 us   | 491 us: 1.39x faster   |
| sympy_sum                  | 118 ms   | 85.2 ms: 1.38x faster  |
| telco                      | 6.34 ms  | 4.59 ms: 1.38x faster  |
| sympy_integrate            | 17.5 ms  | 12.8 ms: 1.37x faster  |
| 2to3                       | 293 ms   | 215 ms: 1.36x faster   |
| html5lib                   | 51.3 ms  | 37.8 ms: 1.36x faster  |
| sympy_str                  | 234 ms   | 173 ms: 1.35x faster   |
| meteor_contest             | 95.0 ms  | 70.9 ms: 1.34x faster  |
| gc_traversal               | 2.79 ms  | 2.12 ms: 1.32x faster  |
| async_tree_cpu_io_mixed    | 434 ms   | 330 ms: 1.32x faster   |
| sphinx                     | 843 ms   | 641 ms: 1.31x faster   |
| many_optionals             | 890 us   | 685 us: 1.30x faster   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 330 ms: 1.30x faster   |
| json                       | 3.94 ms  | 3.04 ms: 1.30x faster  |
| coverage                   | 61.1 ms  | 47.5 ms: 1.29x faster  |
| mdp                        | 1.82 sec | 1.43 sec: 1.28x faster |
| docutils                   | 2.11 sec | 1.66 sec: 1.27x faster |
| dulwich_log                | 50.5 ms  | 40.3 ms: 1.25x faster  |
| pylint                     | 249 ms   | 201 ms: 1.24x faster   |
| subparsers                 | 50.4 ms  | 41.4 ms: 1.22x faster  |
| xml_etree_parse            | 108 ms   | 89.4 ms: 1.21x faster  |
| regex_effbot               | 1.77 ms  | 1.47 ms: 1.21x faster  |
| regex_v8                   | 17.0 ms  | 14.2 ms: 1.19x faster  |
| sqlite_synth               | 1.78 us  | 1.56 us: 1.14x faster  |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.12x faster  |
| pathlib                    | 26.8 ms  | 24.2 ms: 1.11x faster  |
| python_startup             | 27.2 ms  | 24.7 ms: 1.10x faster  |
| python_startup_no_site     | 20.3 ms  | 18.6 ms: 1.09x faster  |
| shortest_path              | 384 ms   | 352 ms: 1.09x faster   |
| connected_components       | 351 ms   | 325 ms: 1.08x faster   |
| k_core                     | 1.83 sec | 1.70 sec: 1.07x faster |
| pidigits                   | 148 ms   | 145 ms: 1.02x faster   |
| regex_dna                  | 118 ms   | 120 ms: 1.02x slower   |
| Geometric mean             | (ref)    | 1.51x faster           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.497x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown