# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.386x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.49x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TCO-Ex2                |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 293 ms: 1.44x slower   |
| docutils       | 1.55 sec  | 2.11 sec: 1.36x slower |
| html5lib       | 35.2 ms   | 51.3 ms: 1.45x slower  |
| sphinx         | 599 ms    | 843 ms: 1.41x slower   |
| Geometric mean | (ref)     | 1.42x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TCO-Ex2               |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 311 ms: 1.28x faster  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 428 ms: 1.38x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 434 ms: 1.41x slower  |
| async_tree_memoization_tg  | 195 ms    | 292 ms: 1.49x slower  |
| async_tree_memoization     | 190 ms    | 297 ms: 1.57x slower  |
| async_tree_io              | 349 ms    | 551 ms: 1.58x slower  |
| async_tree_none_tg         | 147 ms    | 236 ms: 1.60x slower  |
| async_tree_io_tg           | 352 ms    | 563 ms: 1.60x slower  |
| async_tree_none            | 155 ms    | 248 ms: 1.60x slower  |
| async_generators           | 188 ms    | 321 ms: 1.70x slower  |
| coroutines                 | 11.1 ms   | 22.1 ms: 1.99x slower |
| Geometric mean             | (ref)     | 1.48x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TCO-Ex2               |
|----------------|:---------:|:---------------------:|
| nbody          | 52.9 ms   | 98.8 ms: 1.87x slower |
| float          | 38.5 ms   | 73.5 ms: 1.91x slower |
| Geometric mean | (ref)     | 1.53x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TCO-Ex2               |
|----------------|:---------:|:---------------------:|
| regex_dna      | 121 ms    | 118 ms: 1.03x faster  |
| regex_effbot   | 1.65 ms   | 1.77 ms: 1.08x slower |
| regex_v8       | 13.5 ms   | 17.0 ms: 1.25x slower |
| regex_compile  | 73.4 ms   | 123 ms: 1.67x slower  |
| Geometric mean | (ref)     | 1.22x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TCO-Ex2                |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 108 ms: 1.22x slower   |
| xml_etree_iterparse  | 60.7 ms   | 87.5 ms: 1.44x slower  |
| json_loads           | 14.2 us   | 21.4 us: 1.51x slower  |
| json_dumps           | 5.76 ms   | 8.99 ms: 1.56x slower  |
| tomli_loads          | 1.13 sec  | 1.97 sec: 1.74x slower |
| xml_etree_generate   | 48.4 ms   | 87.5 ms: 1.81x slower  |
| xml_etree_process    | 34.0 ms   | 63.0 ms: 1.85x slower  |
| pickle_pure_python   | 175 us    | 354 us: 2.02x slower   |
| unpickle_pure_python | 109 us    | 271 us: 2.49x slower   |
| Geometric mean       | (ref)     | 1.70x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | TCO-Ex2               |
|------------------------|:---------:|:---------------------:|
| python_startup_no_site | 20.0 ms   | 20.3 ms: 1.02x slower |
| python_startup         | 26.6 ms   | 27.2 ms: 1.02x slower |
| Geometric mean         | (ref)     | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TCO-Ex2               |
|-----------------|:---------:|:---------------------:|
| genshi_xml      | 27.4 ms   | 48.8 ms: 1.78x slower |
| django_template | 19.5 ms   | 35.8 ms: 1.83x slower |
| genshi_text     | 12.0 ms   | 23.4 ms: 1.95x slower |
| mako            | 5.72 ms   | 11.4 ms: 2.00x slower |
| Geometric mean  | (ref)     | 1.89x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TCO-Ex2                |
|----------------------------|:---------:|:----------------------:|
| asyncio_websockets         | 400 ms    | 311 ms: 1.28x faster   |
| pathlib                    | 30.4 ms   | 26.8 ms: 1.13x faster  |
| regex_dna                  | 121 ms    | 118 ms: 1.03x faster   |
| python_startup_no_site     | 20.0 ms   | 20.3 ms: 1.02x slower  |
| create_gc_cycles           | 1.37 ms   | 1.40 ms: 1.02x slower  |
| python_startup             | 26.6 ms   | 27.2 ms: 1.02x slower  |
| regex_effbot               | 1.65 ms   | 1.77 ms: 1.08x slower  |
| connected_components       | 325 ms    | 351 ms: 1.08x slower   |
| shortest_path              | 345 ms    | 384 ms: 1.11x slower   |
| k_core                     | 1.61 sec  | 1.83 sec: 1.14x slower |
| sqlite_synth               | 1.49 us   | 1.78 us: 1.19x slower  |
| xml_etree_parse            | 88.8 ms   | 108 ms: 1.22x slower   |
| regex_v8                   | 13.5 ms   | 17.0 ms: 1.25x slower  |
| dulwich_log                | 39.5 ms   | 50.5 ms: 1.28x slower  |
| docutils                   | 1.55 sec  | 2.11 sec: 1.36x slower |
| pylint                     | 182 ms    | 249 ms: 1.36x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 428 ms: 1.38x slower   |
| meteor_contest             | 68.7 ms   | 95.0 ms: 1.38x slower  |
| json                       | 2.83 ms   | 3.94 ms: 1.39x slower  |
| mdp                        | 1.30 sec  | 1.82 sec: 1.40x slower |
| async_tree_cpu_io_mixed    | 309 ms    | 434 ms: 1.41x slower   |
| sphinx                     | 599 ms    | 843 ms: 1.41x slower   |
| 2to3                       | 204 ms    | 293 ms: 1.44x slower   |
| xml_etree_iterparse        | 60.7 ms   | 87.5 ms: 1.44x slower  |
| sympy_sum                  | 81.4 ms   | 118 ms: 1.45x slower   |
| html5lib                   | 35.2 ms   | 51.3 ms: 1.45x slower  |
| sympy_integrate            | 11.8 ms   | 17.5 ms: 1.49x slower  |
| coverage                   | 40.9 ms   | 61.1 ms: 1.49x slower  |
| async_tree_memoization_tg  | 195 ms    | 292 ms: 1.49x slower   |
| json_loads                 | 14.2 us   | 21.4 us: 1.51x slower  |
| telco                      | 4.20 ms   | 6.34 ms: 1.51x slower  |
| pycparser                  | 637 ms    | 968 ms: 1.52x slower   |
| sympy_str                  | 153 ms    | 234 ms: 1.54x slower   |
| sympy_expand               | 259 ms    | 399 ms: 1.54x slower   |
| json_dumps                 | 5.76 ms   | 8.99 ms: 1.56x slower  |
| logging_format             | 5.83 us   | 9.13 us: 1.57x slower  |
| async_tree_memoization     | 190 ms    | 297 ms: 1.57x slower   |
| thrift                     | 434 us    | 680 us: 1.57x slower   |
| async_tree_io              | 349 ms    | 551 ms: 1.58x slower   |
| async_tree_none_tg         | 147 ms    | 236 ms: 1.60x slower   |
| async_tree_io_tg           | 352 ms    | 563 ms: 1.60x slower   |
| async_tree_none            | 155 ms    | 248 ms: 1.60x slower   |
| logging_simple             | 5.39 us   | 8.63 us: 1.60x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 49.6 ms: 1.66x slower  |
| regex_compile              | 73.4 ms   | 123 ms: 1.67x slower   |
| typing_runtime_protocols   | 86.2 us   | 146 us: 1.70x slower   |
| async_generators           | 188 ms    | 321 ms: 1.70x slower   |
| bpe_tokeniser              | 2.50 sec  | 4.30 sec: 1.72x slower |
| sqlglot_v2_normalize       | 59.9 ms   | 103 ms: 1.73x slower   |
| tomli_loads                | 1.13 sec  | 1.97 sec: 1.74x slower |
| genshi_xml                 | 27.4 ms   | 48.8 ms: 1.78x slower  |
| xml_etree_generate         | 48.4 ms   | 87.5 ms: 1.81x slower  |
| deepcopy_reduce            | 1.49 us   | 2.71 us: 1.82x slower  |
| pprint_safe_repr           | 432 ms    | 789 ms: 1.83x slower   |
| django_template            | 19.5 ms   | 35.8 ms: 1.83x slower  |
| deepcopy                   | 145 us    | 266 us: 1.84x slower   |
| fannkuch                   | 209 ms    | 386 ms: 1.84x slower   |
| pprint_pformat             | 874 ms    | 1.61 sec: 1.85x slower |
| xml_etree_process          | 34.0 ms   | 63.0 ms: 1.85x slower  |
| sqlglot_v2_transpile       | 868 us    | 1.62 ms: 1.86x slower  |
| nbody                      | 52.9 ms   | 98.8 ms: 1.87x slower  |
| pyflate                    | 245 ms    | 457 ms: 1.87x slower   |
| scimark_fft                | 143 ms    | 267 ms: 1.87x slower   |
| float                      | 38.5 ms   | 73.5 ms: 1.91x slower  |
| crypto_pyaes               | 39.4 ms   | 76.8 ms: 1.95x slower  |
| genshi_text                | 12.0 ms   | 23.4 ms: 1.95x slower  |
| nqueens                    | 47.7 ms   | 93.2 ms: 1.95x slower  |
| sqlglot_v2_parse           | 686 us    | 1.34 ms: 1.96x slower  |
| coroutines                 | 11.1 ms   | 22.1 ms: 1.99x slower  |
| mako                       | 5.72 ms   | 11.4 ms: 2.00x slower  |
| pickle_pure_python         | 175 us    | 354 us: 2.02x slower   |
| scimark_sparse_mat_mult    | 2.05 ms   | 4.27 ms: 2.08x slower  |
| generators                 | 15.8 ms   | 33.5 ms: 2.12x slower  |
| go                         | 65.1 ms   | 138 ms: 2.12x slower   |
| chaos                      | 31.1 ms   | 67.0 ms: 2.16x slower  |
| spectral_norm              | 44.7 ms   | 97.1 ms: 2.17x slower  |
| deepcopy_memo              | 15.1 us   | 33.0 us: 2.19x slower  |
| many_optionals             | 405 us    | 890 us: 2.20x slower   |
| comprehensions             | 8.84 us   | 19.4 us: 2.20x slower  |
| raytrace                   | 137 ms    | 306 ms: 2.23x slower   |
| scimark_sor                | 59.1 ms   | 133 ms: 2.26x slower   |
| scimark_monte_carlo        | 32.8 ms   | 75.2 ms: 2.29x slower  |
| hexiom                     | 3.13 ms   | 7.27 ms: 2.32x slower  |
| richards                   | 21.9 ms   | 51.0 ms: 2.33x slower  |
| richards_super             | 24.6 ms   | 58.0 ms: 2.36x slower  |
| scimark_lu                 | 49.1 ms   | 116 ms: 2.36x slower   |
| unpickle_pure_python       | 109 us    | 271 us: 2.49x slower   |
| deltablue                  | 1.59 ms   | 4.08 ms: 2.56x slower  |
| logging_silent             | 44.5 ns   | 121 ns: 2.73x slower   |
| subparsers                 | 14.2 ms   | 50.4 ms: 3.53x slower  |
| Geometric mean             | (ref)     | 1.64x slower           |

Benchmark hidden because not significant (2): pidigits, gc_traversal
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.386x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.54x
- 95% likely to have a slowdown of 1.52x
- 99% likely to have a slowdown of 1.49x

# Memory
- memory change: unknown