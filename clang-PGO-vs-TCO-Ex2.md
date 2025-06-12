# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.631x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.49x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 204 ms: 1.44x faster   |
| docutils       | 2.11 sec | 1.55 sec: 1.36x faster |
| html5lib       | 51.3 ms  | 35.2 ms: 1.45x faster  |
| sphinx         | 843 ms   | 599 ms: 1.41x faster   |
| Geometric mean | (ref)    | 1.42x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 11.1 ms: 1.99x faster |
| async_generators           | 321 ms  | 188 ms: 1.70x faster  |
| async_tree_none            | 248 ms  | 155 ms: 1.60x faster  |
| async_tree_io_tg           | 563 ms  | 352 ms: 1.60x faster  |
| async_tree_none_tg         | 236 ms  | 147 ms: 1.60x faster  |
| async_tree_io              | 551 ms  | 349 ms: 1.58x faster  |
| async_tree_memoization     | 297 ms  | 190 ms: 1.57x faster  |
| async_tree_memoization_tg  | 292 ms  | 195 ms: 1.49x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 309 ms: 1.41x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 310 ms: 1.38x faster  |
| asyncio_websockets         | 311 ms  | 400 ms: 1.28x slower  |
| Geometric mean             | (ref)   | 1.48x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | clang-PGO             |
|----------------|:-------:|:---------------------:|
| float          | 73.5 ms | 38.5 ms: 1.91x faster |
| nbody          | 98.8 ms | 52.9 ms: 1.87x faster |
| Geometric mean | (ref)   | 1.53x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 73.4 ms: 1.67x faster |
| regex_v8       | 17.0 ms | 13.5 ms: 1.25x faster |
| regex_effbot   | 1.77 ms | 1.65 ms: 1.08x faster |
| regex_dna      | 118 ms  | 121 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.22x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 109 us: 2.49x faster   |
| pickle_pure_python   | 354 us   | 175 us: 2.02x faster   |
| xml_etree_process    | 63.0 ms  | 34.0 ms: 1.85x faster  |
| xml_etree_generate   | 87.5 ms  | 48.4 ms: 1.81x faster  |
| tomli_loads          | 1.97 sec | 1.13 sec: 1.74x faster |
| json_dumps           | 8.99 ms  | 5.76 ms: 1.56x faster  |
| json_loads           | 21.4 us  | 14.2 us: 1.51x faster  |
| xml_etree_iterparse  | 87.5 ms  | 60.7 ms: 1.44x faster  |
| xml_etree_parse      | 108 ms   | 88.8 ms: 1.22x faster  |
| Geometric mean       | (ref)    | 1.70x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | clang-PGO             |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 26.6 ms: 1.02x faster |
| python_startup_no_site | 20.3 ms | 20.0 ms: 1.02x faster |
| Geometric mean         | (ref)   | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 5.72 ms: 2.00x faster |
| genshi_text     | 23.4 ms | 12.0 ms: 1.95x faster |
| django_template | 35.8 ms | 19.5 ms: 1.83x faster |
| genshi_xml      | 48.8 ms | 27.4 ms: 1.78x faster |
| Geometric mean  | (ref)   | 1.89x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 50.4 ms  | 14.2 ms: 3.53x faster  |
| logging_silent             | 121 ns   | 44.5 ns: 2.73x faster  |
| deltablue                  | 4.08 ms  | 1.59 ms: 2.56x faster  |
| unpickle_pure_python       | 271 us   | 109 us: 2.49x faster   |
| scimark_lu                 | 116 ms   | 49.1 ms: 2.36x faster  |
| richards_super             | 58.0 ms  | 24.6 ms: 2.36x faster  |
| richards                   | 51.0 ms  | 21.9 ms: 2.33x faster  |
| hexiom                     | 7.27 ms  | 3.13 ms: 2.32x faster  |
| scimark_monte_carlo        | 75.2 ms  | 32.8 ms: 2.29x faster  |
| scimark_sor                | 133 ms   | 59.1 ms: 2.26x faster  |
| raytrace                   | 306 ms   | 137 ms: 2.23x faster   |
| comprehensions             | 19.4 us  | 8.84 us: 2.20x faster  |
| many_optionals             | 890 us   | 405 us: 2.20x faster   |
| deepcopy_memo              | 33.0 us  | 15.1 us: 2.19x faster  |
| spectral_norm              | 97.1 ms  | 44.7 ms: 2.17x faster  |
| chaos                      | 67.0 ms  | 31.1 ms: 2.16x faster  |
| go                         | 138 ms   | 65.1 ms: 2.12x faster  |
| generators                 | 33.5 ms  | 15.8 ms: 2.12x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.05 ms: 2.08x faster  |
| pickle_pure_python         | 354 us   | 175 us: 2.02x faster   |
| mako                       | 11.4 ms  | 5.72 ms: 2.00x faster  |
| coroutines                 | 22.1 ms  | 11.1 ms: 1.99x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 686 us: 1.96x faster   |
| nqueens                    | 93.2 ms  | 47.7 ms: 1.95x faster  |
| genshi_text                | 23.4 ms  | 12.0 ms: 1.95x faster  |
| crypto_pyaes               | 76.8 ms  | 39.4 ms: 1.95x faster  |
| float                      | 73.5 ms  | 38.5 ms: 1.91x faster  |
| scimark_fft                | 267 ms   | 143 ms: 1.87x faster   |
| pyflate                    | 457 ms   | 245 ms: 1.87x faster   |
| nbody                      | 98.8 ms  | 52.9 ms: 1.87x faster  |
| sqlglot_v2_transpile       | 1.62 ms  | 868 us: 1.86x faster   |
| xml_etree_process          | 63.0 ms  | 34.0 ms: 1.85x faster  |
| pprint_pformat             | 1.61 sec | 874 ms: 1.85x faster   |
| fannkuch                   | 386 ms   | 209 ms: 1.84x faster   |
| deepcopy                   | 266 us   | 145 us: 1.84x faster   |
| django_template            | 35.8 ms  | 19.5 ms: 1.83x faster  |
| pprint_safe_repr           | 789 ms   | 432 ms: 1.83x faster   |
| deepcopy_reduce            | 2.71 us  | 1.49 us: 1.82x faster  |
| xml_etree_generate         | 87.5 ms  | 48.4 ms: 1.81x faster  |
| genshi_xml                 | 48.8 ms  | 27.4 ms: 1.78x faster  |
| tomli_loads                | 1.97 sec | 1.13 sec: 1.74x faster |
| sqlglot_v2_normalize       | 103 ms   | 59.9 ms: 1.73x faster  |
| bpe_tokeniser              | 4.30 sec | 2.50 sec: 1.72x faster |
| async_generators           | 321 ms   | 188 ms: 1.70x faster   |
| typing_runtime_protocols   | 146 us   | 86.2 us: 1.70x faster  |
| regex_compile              | 123 ms   | 73.4 ms: 1.67x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 29.8 ms: 1.66x faster  |
| logging_simple             | 8.63 us  | 5.39 us: 1.60x faster  |
| async_tree_none            | 248 ms   | 155 ms: 1.60x faster   |
| async_tree_io_tg           | 563 ms   | 352 ms: 1.60x faster   |
| async_tree_none_tg         | 236 ms   | 147 ms: 1.60x faster   |
| async_tree_io              | 551 ms   | 349 ms: 1.58x faster   |
| thrift                     | 680 us   | 434 us: 1.57x faster   |
| async_tree_memoization     | 297 ms   | 190 ms: 1.57x faster   |
| logging_format             | 9.13 us  | 5.83 us: 1.57x faster  |
| json_dumps                 | 8.99 ms  | 5.76 ms: 1.56x faster  |
| sympy_expand               | 399 ms   | 259 ms: 1.54x faster   |
| sympy_str                  | 234 ms   | 153 ms: 1.54x faster   |
| pycparser                  | 968 ms   | 637 ms: 1.52x faster   |
| telco                      | 6.34 ms  | 4.20 ms: 1.51x faster  |
| json_loads                 | 21.4 us  | 14.2 us: 1.51x faster  |
| async_tree_memoization_tg  | 292 ms   | 195 ms: 1.49x faster   |
| coverage                   | 61.1 ms  | 40.9 ms: 1.49x faster  |
| sympy_integrate            | 17.5 ms  | 11.8 ms: 1.49x faster  |
| html5lib                   | 51.3 ms  | 35.2 ms: 1.45x faster  |
| sympy_sum                  | 118 ms   | 81.4 ms: 1.45x faster  |
| xml_etree_iterparse        | 87.5 ms  | 60.7 ms: 1.44x faster  |
| 2to3                       | 293 ms   | 204 ms: 1.44x faster   |
| sphinx                     | 843 ms   | 599 ms: 1.41x faster   |
| async_tree_cpu_io_mixed    | 434 ms   | 309 ms: 1.41x faster   |
| mdp                        | 1.82 sec | 1.30 sec: 1.40x faster |
| json                       | 3.94 ms  | 2.83 ms: 1.39x faster  |
| meteor_contest             | 95.0 ms  | 68.7 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms   | 310 ms: 1.38x faster   |
| pylint                     | 249 ms   | 182 ms: 1.36x faster   |
| docutils                   | 2.11 sec | 1.55 sec: 1.36x faster |
| dulwich_log                | 50.5 ms  | 39.5 ms: 1.28x faster  |
| regex_v8                   | 17.0 ms  | 13.5 ms: 1.25x faster  |
| xml_etree_parse            | 108 ms   | 88.8 ms: 1.22x faster  |
| sqlite_synth               | 1.78 us  | 1.49 us: 1.19x faster  |
| k_core                     | 1.83 sec | 1.61 sec: 1.14x faster |
| shortest_path              | 384 ms   | 345 ms: 1.11x faster   |
| connected_components       | 351 ms   | 325 ms: 1.08x faster   |
| regex_effbot               | 1.77 ms  | 1.65 ms: 1.08x faster  |
| python_startup             | 27.2 ms  | 26.6 ms: 1.02x faster  |
| create_gc_cycles           | 1.40 ms  | 1.37 ms: 1.02x faster  |
| python_startup_no_site     | 20.3 ms  | 20.0 ms: 1.02x faster  |
| regex_dna                  | 118 ms   | 121 ms: 1.03x slower   |
| pathlib                    | 26.8 ms  | 30.4 ms: 1.13x slower  |
| asyncio_websockets         | 311 ms   | 400 ms: 1.28x slower   |
| Geometric mean             | (ref)    | 1.64x faster           |

Benchmark hidden because not significant (2): gc_traversal, pidigits
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.631x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.54x
- 95% likely to have a speedup of 1.52x
- 99% likely to have a speedup of 1.49x

# Memory
- memory change: unknown