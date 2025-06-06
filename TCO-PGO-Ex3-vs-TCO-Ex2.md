# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.496x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 212 ms: 1.38x faster   |
| docutils       | 2.11 sec | 1.67 sec: 1.27x faster |
| html5lib       | 51.3 ms  | 37.9 ms: 1.35x faster  |
| sphinx         | 843 ms   | 645 ms: 1.31x faster   |
| Geometric mean | (ref)    | 1.33x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 11.9 ms: 1.85x faster |
| async_generators           | 321 ms  | 202 ms: 1.59x faster  |
| async_tree_io_tg           | 563 ms  | 377 ms: 1.49x faster  |
| async_tree_none_tg         | 236 ms  | 159 ms: 1.48x faster  |
| async_tree_none            | 248 ms  | 170 ms: 1.46x faster  |
| async_tree_memoization     | 297 ms  | 206 ms: 1.44x faster  |
| async_tree_io              | 551 ms  | 384 ms: 1.44x faster  |
| async_tree_memoization_tg  | 292 ms  | 208 ms: 1.40x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 330 ms: 1.31x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 329 ms: 1.30x faster  |
| asyncio_websockets         | 311 ms  | 301 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 55.2 ms: 1.79x faster |
| float          | 73.5 ms | 41.9 ms: 1.75x faster |
| pidigits       | 148 ms  | 145 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.47x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 78.1 ms: 1.57x faster |
| regex_v8       | 17.0 ms | 13.2 ms: 1.28x faster |
| regex_effbot   | 1.77 ms | 1.46 ms: 1.21x faster |
| regex_dna      | 118 ms  | 120 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.24x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 127 us: 2.13x faster   |
| pickle_pure_python   | 354 us   | 199 us: 1.78x faster   |
| xml_etree_process    | 63.0 ms  | 37.0 ms: 1.70x faster  |
| tomli_loads          | 1.97 sec | 1.18 sec: 1.67x faster |
| xml_etree_generate   | 87.5 ms  | 53.6 ms: 1.63x faster  |
| json_loads           | 21.4 us  | 14.7 us: 1.45x faster  |
| xml_etree_iterparse  | 87.5 ms  | 61.2 ms: 1.43x faster  |
| json_dumps           | 8.99 ms  | 6.55 ms: 1.37x faster  |
| xml_etree_parse      | 108 ms   | 89.3 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.58x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 24.7 ms: 1.10x faster |
| python_startup_no_site | 20.3 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.09x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 6.28 ms: 1.82x faster |
| genshi_text     | 23.4 ms | 14.3 ms: 1.64x faster |
| django_template | 35.8 ms | 22.9 ms: 1.57x faster |
| genshi_xml      | 48.8 ms | 32.8 ms: 1.49x faster |
| Geometric mean  | (ref)   | 1.62x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 121 ns   | 49.4 ns: 2.46x faster  |
| scimark_lu                 | 116 ms   | 50.9 ms: 2.27x faster  |
| scimark_sor                | 133 ms   | 61.1 ms: 2.18x faster  |
| deltablue                  | 4.08 ms  | 1.88 ms: 2.17x faster  |
| unpickle_pure_python       | 271 us   | 127 us: 2.13x faster   |
| scimark_monte_carlo        | 75.2 ms  | 36.0 ms: 2.09x faster  |
| hexiom                     | 7.27 ms  | 3.54 ms: 2.06x faster  |
| generators                 | 33.5 ms  | 16.5 ms: 2.03x faster  |
| deepcopy_memo              | 33.0 us  | 16.6 us: 1.99x faster  |
| comprehensions             | 19.4 us  | 9.87 us: 1.97x faster  |
| spectral_norm              | 97.1 ms  | 49.4 ms: 1.97x faster  |
| go                         | 138 ms   | 70.9 ms: 1.95x faster  |
| raytrace                   | 306 ms   | 160 ms: 1.91x faster   |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.27 ms: 1.89x faster  |
| coroutines                 | 22.1 ms  | 11.9 ms: 1.85x faster  |
| mako                       | 11.4 ms  | 6.28 ms: 1.82x faster  |
| chaos                      | 67.0 ms  | 36.9 ms: 1.82x faster  |
| nbody                      | 98.8 ms  | 55.2 ms: 1.79x faster  |
| pickle_pure_python         | 354 us   | 199 us: 1.78x faster   |
| richards                   | 51.0 ms  | 28.7 ms: 1.77x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 766 us: 1.75x faster   |
| richards_super             | 58.0 ms  | 33.1 ms: 1.75x faster  |
| float                      | 73.5 ms  | 41.9 ms: 1.75x faster  |
| scimark_fft                | 267 ms   | 154 ms: 1.74x faster   |
| fannkuch                   | 386 ms   | 223 ms: 1.73x faster   |
| nqueens                    | 93.2 ms  | 54.4 ms: 1.71x faster  |
| pyflate                    | 457 ms   | 268 ms: 1.70x faster   |
| xml_etree_process          | 63.0 ms  | 37.0 ms: 1.70x faster  |
| pprint_safe_repr           | 789 ms   | 470 ms: 1.68x faster   |
| tomli_loads                | 1.97 sec | 1.18 sec: 1.67x faster |
| pprint_pformat             | 1.61 sec | 967 ms: 1.67x faster   |
| sqlglot_v2_transpile       | 1.62 ms  | 970 us: 1.67x faster   |
| genshi_text                | 23.4 ms  | 14.3 ms: 1.64x faster  |
| xml_etree_generate         | 87.5 ms  | 53.6 ms: 1.63x faster  |
| crypto_pyaes               | 76.8 ms  | 47.4 ms: 1.62x faster  |
| deepcopy                   | 266 us   | 167 us: 1.59x faster   |
| deepcopy_reduce            | 2.71 us  | 1.70 us: 1.59x faster  |
| async_generators           | 321 ms   | 202 ms: 1.59x faster   |
| bpe_tokeniser              | 4.30 sec | 2.72 sec: 1.58x faster |
| regex_compile              | 123 ms   | 78.1 ms: 1.57x faster  |
| django_template            | 35.8 ms  | 22.9 ms: 1.57x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 33.0 ms: 1.50x faster  |
| async_tree_io_tg           | 563 ms   | 377 ms: 1.49x faster   |
| sqlglot_v2_normalize       | 103 ms   | 69.3 ms: 1.49x faster  |
| genshi_xml                 | 48.8 ms  | 32.8 ms: 1.49x faster  |
| typing_runtime_protocols   | 146 us   | 98.8 us: 1.48x faster  |
| async_tree_none_tg         | 236 ms   | 159 ms: 1.48x faster   |
| async_tree_none            | 248 ms   | 170 ms: 1.46x faster   |
| json_loads                 | 21.4 us  | 14.7 us: 1.45x faster  |
| logging_simple             | 8.63 us  | 5.97 us: 1.44x faster  |
| async_tree_memoization     | 297 ms   | 206 ms: 1.44x faster   |
| async_tree_io              | 551 ms   | 384 ms: 1.44x faster   |
| xml_etree_iterparse        | 87.5 ms  | 61.2 ms: 1.43x faster  |
| sympy_str                  | 234 ms   | 164 ms: 1.43x faster   |
| sympy_expand               | 399 ms   | 282 ms: 1.42x faster   |
| pycparser                  | 968 ms   | 686 ms: 1.41x faster   |
| thrift                     | 680 us   | 482 us: 1.41x faster   |
| logging_format             | 9.13 us  | 6.50 us: 1.41x faster  |
| async_tree_memoization_tg  | 292 ms   | 208 ms: 1.40x faster   |
| telco                      | 6.34 ms  | 4.57 ms: 1.39x faster  |
| 2to3                       | 293 ms   | 212 ms: 1.38x faster   |
| json_dumps                 | 8.99 ms  | 6.55 ms: 1.37x faster  |
| sympy_integrate            | 17.5 ms  | 12.8 ms: 1.36x faster  |
| sympy_sum                  | 118 ms   | 86.3 ms: 1.36x faster  |
| meteor_contest             | 95.0 ms  | 70.2 ms: 1.35x faster  |
| html5lib                   | 51.3 ms  | 37.9 ms: 1.35x faster  |
| many_optionals             | 890 us   | 665 us: 1.34x faster   |
| gc_traversal               | 2.79 ms  | 2.11 ms: 1.33x faster  |
| json                       | 3.94 ms  | 2.97 ms: 1.32x faster  |
| async_tree_cpu_io_mixed    | 434 ms   | 330 ms: 1.31x faster   |
| sphinx                     | 843 ms   | 645 ms: 1.31x faster   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 329 ms: 1.30x faster   |
| regex_v8                   | 17.0 ms  | 13.2 ms: 1.28x faster  |
| coverage                   | 61.1 ms  | 48.2 ms: 1.27x faster  |
| docutils                   | 2.11 sec | 1.67 sec: 1.27x faster |
| dulwich_log                | 50.5 ms  | 40.2 ms: 1.26x faster  |
| pylint                     | 249 ms   | 198 ms: 1.25x faster   |
| subparsers                 | 50.4 ms  | 40.7 ms: 1.24x faster  |
| regex_effbot               | 1.77 ms  | 1.46 ms: 1.21x faster  |
| xml_etree_parse            | 108 ms   | 89.3 ms: 1.21x faster  |
| sqlite_synth               | 1.78 us  | 1.56 us: 1.14x faster  |
| mdp                        | 1.82 sec | 1.62 sec: 1.13x faster |
| pathlib                    | 26.8 ms  | 24.1 ms: 1.11x faster  |
| python_startup             | 27.2 ms  | 24.7 ms: 1.10x faster  |
| create_gc_cycles           | 1.40 ms  | 1.27 ms: 1.10x faster  |
| shortest_path              | 384 ms   | 353 ms: 1.09x faster   |
| python_startup_no_site     | 20.3 ms  | 18.7 ms: 1.09x faster  |
| connected_components       | 351 ms   | 326 ms: 1.08x faster   |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| asyncio_websockets         | 311 ms   | 301 ms: 1.04x faster   |
| pidigits                   | 148 ms   | 145 ms: 1.02x faster   |
| regex_dna                  | 118 ms   | 120 ms: 1.03x slower   |
| Geometric mean             | (ref)    | 1.50x faster           |
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.496x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.42x
- 95% likely to have a speedup of 1.41x
- 99% likely to have a speedup of 1.38x

# Memory
- memory change: unknown