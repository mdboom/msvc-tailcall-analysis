# Results vs. base

- fork: unknown
- ref: NoTC-PGO-NoEx
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.376x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx          |
|----------------|:---------------:|:----------------------:|
| 2to3           | 298 ms          | 227 ms: 1.31x faster   |
| docutils       | 2.17 sec        | 1.68 sec: 1.29x faster |
| html5lib       | 51.3 ms         | 40.8 ms: 1.26x faster  |
| sphinx         | 872 ms          | 658 ms: 1.32x faster   |
| Geometric mean | (ref)           | 1.30x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx         |
|----------------------------|:---------------:|:---------------------:|
| coroutines                 | 21.9 ms         | 13.5 ms: 1.62x faster |
| async_generators           | 328 ms          | 226 ms: 1.45x faster  |
| async_tree_io_tg           | 559 ms          | 410 ms: 1.36x faster  |
| async_tree_memoization_tg  | 291 ms          | 216 ms: 1.35x faster  |
| async_tree_none_tg         | 236 ms          | 176 ms: 1.34x faster  |
| async_tree_none            | 249 ms          | 187 ms: 1.34x faster  |
| async_tree_memoization     | 297 ms          | 224 ms: 1.33x faster  |
| async_tree_io              | 553 ms          | 423 ms: 1.31x faster  |
| async_tree_cpu_io_mixed    | 437 ms          | 339 ms: 1.29x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms          | 343 ms: 1.24x faster  |
| Geometric mean             | (ref)           | 1.32x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx         |
|----------------|:---------------:|:---------------------:|
| float          | 75.4 ms         | 47.8 ms: 1.58x faster |
| nbody          | 101 ms          | 74.1 ms: 1.36x faster |
| Geometric mean | (ref)           | 1.29x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx         |
|----------------|:---------------:|:---------------------:|
| regex_compile  | 125 ms          | 88.2 ms: 1.41x faster |
| regex_effbot   | 1.81 ms         | 1.42 ms: 1.28x faster |
| regex_v8       | 17.1 ms         | 13.5 ms: 1.26x faster |
| regex_dna      | 121 ms          | 112 ms: 1.07x faster  |
| Geometric mean | (ref)           | 1.25x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx          |
|----------------------|:---------------:|:----------------------:|
| unpickle_pure_python | 274 us          | 155 us: 1.76x faster   |
| xml_etree_process    | 64.6 ms         | 41.5 ms: 1.55x faster  |
| xml_etree_generate   | 89.5 ms         | 58.7 ms: 1.52x faster  |
| json_loads           | 22.3 us         | 14.7 us: 1.52x faster  |
| pickle_pure_python   | 355 us          | 237 us: 1.50x faster   |
| xml_etree_iterparse  | 89.9 ms         | 63.7 ms: 1.41x faster  |
| tomli_loads          | 1.99 sec        | 1.47 sec: 1.36x faster |
| json_dumps           | 9.01 ms         | 7.05 ms: 1.28x faster  |
| xml_etree_parse      | 108 ms          | 91.2 ms: 1.18x faster  |
| Geometric mean       | (ref)           | 1.45x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx         |
|------------------------|:---------------:|:---------------------:|
| python_startup         | 27.3 ms         | 26.1 ms: 1.05x faster |
| python_startup_no_site | 20.4 ms         | 19.8 ms: 1.03x faster |
| Geometric mean         | (ref)           | 1.04x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx         |
|-----------------|:---------------:|:---------------------:|
| mako            | 11.7 ms         | 6.86 ms: 1.71x faster |
| django_template | 36.9 ms         | 25.1 ms: 1.47x faster |
| genshi_text     | 23.2 ms         | 16.5 ms: 1.40x faster |
| genshi_xml      | 48.8 ms         | 36.3 ms: 1.34x faster |
| Geometric mean  | (ref)           | 1.47x faster          |

All benchmarks:
===============

| Benchmark                  | NoTC-NoPGO-NoEx | NoTC-PGO-NoEx          |
|----------------------------|:---------------:|:----------------------:|
| richards                   | 57.8 ms         | 30.7 ms: 1.88x faster  |
| richards_super             | 65.8 ms         | 35.1 ms: 1.87x faster  |
| logging_silent             | 119 ns          | 65.2 ns: 1.83x faster  |
| deltablue                  | 4.09 ms         | 2.29 ms: 1.78x faster  |
| unpickle_pure_python       | 274 us          | 155 us: 1.76x faster   |
| generators                 | 33.8 ms         | 19.3 ms: 1.75x faster  |
| scimark_lu                 | 116 ms          | 66.9 ms: 1.74x faster  |
| comprehensions             | 19.4 us         | 11.3 us: 1.71x faster  |
| mako                       | 11.7 ms         | 6.86 ms: 1.71x faster  |
| hexiom                     | 7.27 ms         | 4.38 ms: 1.66x faster  |
| coroutines                 | 21.9 ms         | 13.5 ms: 1.62x faster  |
| scimark_sparse_mat_mult    | 4.34 ms         | 2.72 ms: 1.60x faster  |
| raytrace                   | 304 ms          | 191 ms: 1.59x faster   |
| spectral_norm              | 97.7 ms         | 61.5 ms: 1.59x faster  |
| float                      | 75.4 ms         | 47.8 ms: 1.58x faster  |
| scimark_monte_carlo        | 73.9 ms         | 47.1 ms: 1.57x faster  |
| deepcopy_memo              | 32.9 us         | 21.0 us: 1.56x faster  |
| crypto_pyaes               | 77.9 ms         | 50.0 ms: 1.56x faster  |
| xml_etree_process          | 64.6 ms         | 41.5 ms: 1.55x faster  |
| go                         | 137 ms          | 88.6 ms: 1.55x faster  |
| gc_traversal               | 3.15 ms         | 2.06 ms: 1.53x faster  |
| xml_etree_generate         | 89.5 ms         | 58.7 ms: 1.52x faster  |
| sqlglot_v2_parse           | 1.36 ms         | 892 us: 1.52x faster   |
| json_loads                 | 22.3 us         | 14.7 us: 1.52x faster  |
| pickle_pure_python         | 355 us          | 237 us: 1.50x faster   |
| chaos                      | 65.2 ms         | 43.6 ms: 1.50x faster  |
| sqlglot_v2_transpile       | 1.64 ms         | 1.10 ms: 1.49x faster  |
| scimark_sor                | 135 ms          | 91.0 ms: 1.48x faster  |
| nqueens                    | 94.3 ms         | 63.6 ms: 1.48x faster  |
| django_template            | 36.9 ms         | 25.1 ms: 1.47x faster  |
| pyflate                    | 462 ms          | 315 ms: 1.46x faster   |
| sqlglot_v2_optimize        | 51.0 ms         | 35.0 ms: 1.46x faster  |
| bpe_tokeniser              | 4.30 sec        | 2.96 sec: 1.45x faster |
| async_generators           | 328 ms          | 226 ms: 1.45x faster   |
| sqlglot_v2_normalize       | 106 ms          | 73.6 ms: 1.44x faster  |
| pprint_pformat             | 1.61 sec        | 1.13 sec: 1.43x faster |
| deepcopy_reduce            | 2.77 us         | 1.94 us: 1.43x faster  |
| deepcopy                   | 269 us          | 190 us: 1.42x faster   |
| typing_runtime_protocols   | 150 us          | 106 us: 1.42x faster   |
| regex_compile              | 125 ms          | 88.2 ms: 1.41x faster  |
| pprint_safe_repr           | 788 ms          | 558 ms: 1.41x faster   |
| xml_etree_iterparse        | 89.9 ms         | 63.7 ms: 1.41x faster  |
| genshi_text                | 23.2 ms         | 16.5 ms: 1.40x faster  |
| scimark_fft                | 269 ms          | 192 ms: 1.40x faster   |
| fannkuch                   | 407 ms          | 296 ms: 1.38x faster   |
| thrift                     | 694 us          | 507 us: 1.37x faster   |
| async_tree_io_tg           | 559 ms          | 410 ms: 1.36x faster   |
| logging_simple             | 8.87 us         | 6.53 us: 1.36x faster  |
| tomli_loads                | 1.99 sec        | 1.47 sec: 1.36x faster |
| nbody                      | 101 ms          | 74.1 ms: 1.36x faster  |
| sympy_str                  | 238 ms          | 176 ms: 1.35x faster   |
| async_tree_memoization_tg  | 291 ms          | 216 ms: 1.35x faster   |
| pycparser                  | 992 ms          | 738 ms: 1.34x faster   |
| genshi_xml                 | 48.8 ms         | 36.3 ms: 1.34x faster  |
| async_tree_none_tg         | 236 ms          | 176 ms: 1.34x faster   |
| sympy_expand               | 405 ms          | 302 ms: 1.34x faster   |
| async_tree_none            | 249 ms          | 187 ms: 1.34x faster   |
| logging_format             | 9.33 us         | 7.03 us: 1.33x faster  |
| async_tree_memoization     | 297 ms          | 224 ms: 1.33x faster   |
| sphinx                     | 872 ms          | 658 ms: 1.32x faster   |
| coverage                   | 61.9 ms         | 46.8 ms: 1.32x faster  |
| sympy_sum                  | 119 ms          | 90.5 ms: 1.32x faster  |
| telco                      | 6.44 ms         | 4.89 ms: 1.32x faster  |
| sympy_integrate            | 17.8 ms         | 13.5 ms: 1.32x faster  |
| 2to3                       | 298 ms          | 227 ms: 1.31x faster   |
| async_tree_io              | 553 ms          | 423 ms: 1.31x faster   |
| subparsers                 | 20.8 ms         | 16.1 ms: 1.29x faster  |
| docutils                   | 2.17 sec        | 1.68 sec: 1.29x faster |
| async_tree_cpu_io_mixed    | 437 ms          | 339 ms: 1.29x faster   |
| json_dumps                 | 9.01 ms         | 7.05 ms: 1.28x faster  |
| regex_effbot               | 1.81 ms         | 1.42 ms: 1.28x faster  |
| regex_v8                   | 17.1 ms         | 13.5 ms: 1.26x faster  |
| json                       | 3.96 ms         | 3.14 ms: 1.26x faster  |
| html5lib                   | 51.3 ms         | 40.8 ms: 1.26x faster  |
| pylint                     | 253 ms          | 201 ms: 1.26x faster   |
| many_optionals             | 547 us          | 438 us: 1.25x faster   |
| meteor_contest             | 95.9 ms         | 76.9 ms: 1.25x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms          | 343 ms: 1.24x faster   |
| xml_etree_parse            | 108 ms          | 91.2 ms: 1.18x faster  |
| dulwich_log                | 51.0 ms         | 43.4 ms: 1.18x faster  |
| bench_thread_pool          | 1.01 ms         | 864 us: 1.16x faster   |
| sqlite_synth               | 1.84 us         | 1.59 us: 1.16x faster  |
| create_gc_cycles           | 1.40 ms         | 1.25 ms: 1.12x faster  |
| mdp                        | 1.81 sec        | 1.64 sec: 1.11x faster |
| bench_mp_pool              | 96.2 ms         | 88.7 ms: 1.08x faster  |
| regex_dna                  | 121 ms          | 112 ms: 1.07x faster   |
| pathlib                    | 34.4 ms         | 32.1 ms: 1.07x faster  |
| k_core                     | 1.83 sec        | 1.73 sec: 1.06x faster |
| connected_components       | 347 ms          | 329 ms: 1.05x faster   |
| shortest_path              | 378 ms          | 359 ms: 1.05x faster   |
| python_startup             | 27.3 ms         | 26.1 ms: 1.05x faster  |
| python_startup_no_site     | 20.4 ms         | 19.8 ms: 1.03x faster  |
| Geometric mean             | (ref)           | 1.37x faster           |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets

- Geometric mean (including insignificant results): 1.376x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown