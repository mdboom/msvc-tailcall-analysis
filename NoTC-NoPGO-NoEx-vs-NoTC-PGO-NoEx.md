# Results vs. base

- fork: unknown
- ref: NoTC-NoPGO-NoEx
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.273x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx        |
|----------------|:-------------:|:----------------------:|
| 2to3           | 227 ms        | 298 ms: 1.31x slower   |
| docutils       | 1.68 sec      | 2.17 sec: 1.29x slower |
| html5lib       | 40.8 ms       | 51.3 ms: 1.26x slower  |
| sphinx         | 658 ms        | 872 ms: 1.32x slower   |
| Geometric mean | (ref)         | 1.30x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx       |
|----------------------------|:-------------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 343 ms        | 424 ms: 1.24x slower  |
| async_tree_cpu_io_mixed    | 339 ms        | 437 ms: 1.29x slower  |
| async_tree_io              | 423 ms        | 553 ms: 1.31x slower  |
| async_tree_memoization     | 224 ms        | 297 ms: 1.33x slower  |
| async_tree_none            | 187 ms        | 249 ms: 1.34x slower  |
| async_tree_none_tg         | 176 ms        | 236 ms: 1.34x slower  |
| async_tree_memoization_tg  | 216 ms        | 291 ms: 1.35x slower  |
| async_tree_io_tg           | 410 ms        | 559 ms: 1.36x slower  |
| async_generators           | 226 ms        | 328 ms: 1.45x slower  |
| coroutines                 | 13.5 ms       | 21.9 ms: 1.62x slower |
| Geometric mean             | (ref)         | 1.32x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx       |
|----------------|:-------------:|:---------------------:|
| nbody          | 74.1 ms       | 101 ms: 1.36x slower  |
| float          | 47.8 ms       | 75.4 ms: 1.58x slower |
| Geometric mean | (ref)         | 1.29x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx       |
|----------------|:-------------:|:---------------------:|
| regex_dna      | 112 ms        | 121 ms: 1.07x slower  |
| regex_v8       | 13.5 ms       | 17.1 ms: 1.26x slower |
| regex_effbot   | 1.42 ms       | 1.81 ms: 1.28x slower |
| regex_compile  | 88.2 ms       | 125 ms: 1.41x slower  |
| Geometric mean | (ref)         | 1.25x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx        |
|----------------------|:-------------:|:----------------------:|
| xml_etree_parse      | 91.2 ms       | 108 ms: 1.18x slower   |
| json_dumps           | 7.05 ms       | 9.01 ms: 1.28x slower  |
| tomli_loads          | 1.47 sec      | 1.99 sec: 1.36x slower |
| xml_etree_iterparse  | 63.7 ms       | 89.9 ms: 1.41x slower  |
| pickle_pure_python   | 237 us        | 355 us: 1.50x slower   |
| json_loads           | 14.7 us       | 22.3 us: 1.52x slower  |
| xml_etree_generate   | 58.7 ms       | 89.5 ms: 1.52x slower  |
| xml_etree_process    | 41.5 ms       | 64.6 ms: 1.55x slower  |
| unpickle_pure_python | 155 us        | 274 us: 1.76x slower   |
| Geometric mean       | (ref)         | 1.45x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx       |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 19.8 ms       | 20.4 ms: 1.03x slower |
| python_startup         | 26.1 ms       | 27.3 ms: 1.05x slower |
| Geometric mean         | (ref)         | 1.04x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx       |
|-----------------|:-------------:|:---------------------:|
| genshi_xml      | 36.3 ms       | 48.8 ms: 1.34x slower |
| genshi_text     | 16.5 ms       | 23.2 ms: 1.40x slower |
| django_template | 25.1 ms       | 36.9 ms: 1.47x slower |
| mako            | 6.86 ms       | 11.7 ms: 1.71x slower |
| Geometric mean  | (ref)         | 1.47x slower          |

All benchmarks:
===============

| Benchmark                  | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx        |
|----------------------------|:-------------:|:----------------------:|
| python_startup_no_site     | 19.8 ms       | 20.4 ms: 1.03x slower  |
| python_startup             | 26.1 ms       | 27.3 ms: 1.05x slower  |
| shortest_path              | 359 ms        | 378 ms: 1.05x slower   |
| connected_components       | 329 ms        | 347 ms: 1.05x slower   |
| k_core                     | 1.73 sec      | 1.83 sec: 1.06x slower |
| pathlib                    | 32.1 ms       | 34.4 ms: 1.07x slower  |
| regex_dna                  | 112 ms        | 121 ms: 1.07x slower   |
| bench_mp_pool              | 88.7 ms       | 96.2 ms: 1.08x slower  |
| mdp                        | 1.64 sec      | 1.81 sec: 1.11x slower |
| create_gc_cycles           | 1.25 ms       | 1.40 ms: 1.12x slower  |
| sqlite_synth               | 1.59 us       | 1.84 us: 1.16x slower  |
| bench_thread_pool          | 864 us        | 1.01 ms: 1.16x slower  |
| dulwich_log                | 43.4 ms       | 51.0 ms: 1.18x slower  |
| xml_etree_parse            | 91.2 ms       | 108 ms: 1.18x slower   |
| async_tree_cpu_io_mixed_tg | 343 ms        | 424 ms: 1.24x slower   |
| meteor_contest             | 76.9 ms       | 95.9 ms: 1.25x slower  |
| many_optionals             | 438 us        | 547 us: 1.25x slower   |
| pylint                     | 201 ms        | 253 ms: 1.26x slower   |
| html5lib                   | 40.8 ms       | 51.3 ms: 1.26x slower  |
| json                       | 3.14 ms       | 3.96 ms: 1.26x slower  |
| regex_v8                   | 13.5 ms       | 17.1 ms: 1.26x slower  |
| regex_effbot               | 1.42 ms       | 1.81 ms: 1.28x slower  |
| json_dumps                 | 7.05 ms       | 9.01 ms: 1.28x slower  |
| async_tree_cpu_io_mixed    | 339 ms        | 437 ms: 1.29x slower   |
| docutils                   | 1.68 sec      | 2.17 sec: 1.29x slower |
| subparsers                 | 16.1 ms       | 20.8 ms: 1.29x slower  |
| async_tree_io              | 423 ms        | 553 ms: 1.31x slower   |
| 2to3                       | 227 ms        | 298 ms: 1.31x slower   |
| sympy_integrate            | 13.5 ms       | 17.8 ms: 1.32x slower  |
| telco                      | 4.89 ms       | 6.44 ms: 1.32x slower  |
| sympy_sum                  | 90.5 ms       | 119 ms: 1.32x slower   |
| coverage                   | 46.8 ms       | 61.9 ms: 1.32x slower  |
| sphinx                     | 658 ms        | 872 ms: 1.32x slower   |
| async_tree_memoization     | 224 ms        | 297 ms: 1.33x slower   |
| logging_format             | 7.03 us       | 9.33 us: 1.33x slower  |
| async_tree_none            | 187 ms        | 249 ms: 1.34x slower   |
| sympy_expand               | 302 ms        | 405 ms: 1.34x slower   |
| async_tree_none_tg         | 176 ms        | 236 ms: 1.34x slower   |
| genshi_xml                 | 36.3 ms       | 48.8 ms: 1.34x slower  |
| pycparser                  | 738 ms        | 992 ms: 1.34x slower   |
| async_tree_memoization_tg  | 216 ms        | 291 ms: 1.35x slower   |
| sympy_str                  | 176 ms        | 238 ms: 1.35x slower   |
| nbody                      | 74.1 ms       | 101 ms: 1.36x slower   |
| tomli_loads                | 1.47 sec      | 1.99 sec: 1.36x slower |
| logging_simple             | 6.53 us       | 8.87 us: 1.36x slower  |
| async_tree_io_tg           | 410 ms        | 559 ms: 1.36x slower   |
| thrift                     | 507 us        | 694 us: 1.37x slower   |
| fannkuch                   | 296 ms        | 407 ms: 1.38x slower   |
| scimark_fft                | 192 ms        | 269 ms: 1.40x slower   |
| genshi_text                | 16.5 ms       | 23.2 ms: 1.40x slower  |
| xml_etree_iterparse        | 63.7 ms       | 89.9 ms: 1.41x slower  |
| pprint_safe_repr           | 558 ms        | 788 ms: 1.41x slower   |
| regex_compile              | 88.2 ms       | 125 ms: 1.41x slower   |
| typing_runtime_protocols   | 106 us        | 150 us: 1.42x slower   |
| deepcopy                   | 190 us        | 269 us: 1.42x slower   |
| deepcopy_reduce            | 1.94 us       | 2.77 us: 1.43x slower  |
| pprint_pformat             | 1.13 sec      | 1.61 sec: 1.43x slower |
| sqlglot_v2_normalize       | 73.6 ms       | 106 ms: 1.44x slower   |
| async_generators           | 226 ms        | 328 ms: 1.45x slower   |
| bpe_tokeniser              | 2.96 sec      | 4.30 sec: 1.45x slower |
| sqlglot_v2_optimize        | 35.0 ms       | 51.0 ms: 1.46x slower  |
| pyflate                    | 315 ms        | 462 ms: 1.46x slower   |
| django_template            | 25.1 ms       | 36.9 ms: 1.47x slower  |
| nqueens                    | 63.6 ms       | 94.3 ms: 1.48x slower  |
| scimark_sor                | 91.0 ms       | 135 ms: 1.48x slower   |
| sqlglot_v2_transpile       | 1.10 ms       | 1.64 ms: 1.49x slower  |
| chaos                      | 43.6 ms       | 65.2 ms: 1.50x slower  |
| pickle_pure_python         | 237 us        | 355 us: 1.50x slower   |
| json_loads                 | 14.7 us       | 22.3 us: 1.52x slower  |
| sqlglot_v2_parse           | 892 us        | 1.36 ms: 1.52x slower  |
| xml_etree_generate         | 58.7 ms       | 89.5 ms: 1.52x slower  |
| gc_traversal               | 2.06 ms       | 3.15 ms: 1.53x slower  |
| go                         | 88.6 ms       | 137 ms: 1.55x slower   |
| xml_etree_process          | 41.5 ms       | 64.6 ms: 1.55x slower  |
| crypto_pyaes               | 50.0 ms       | 77.9 ms: 1.56x slower  |
| deepcopy_memo              | 21.0 us       | 32.9 us: 1.56x slower  |
| scimark_monte_carlo        | 47.1 ms       | 73.9 ms: 1.57x slower  |
| float                      | 47.8 ms       | 75.4 ms: 1.58x slower  |
| spectral_norm              | 61.5 ms       | 97.7 ms: 1.59x slower  |
| raytrace                   | 191 ms        | 304 ms: 1.59x slower   |
| scimark_sparse_mat_mult    | 2.72 ms       | 4.34 ms: 1.60x slower  |
| coroutines                 | 13.5 ms       | 21.9 ms: 1.62x slower  |
| hexiom                     | 4.38 ms       | 7.27 ms: 1.66x slower  |
| mako                       | 6.86 ms       | 11.7 ms: 1.71x slower  |
| comprehensions             | 11.3 us       | 19.4 us: 1.71x slower  |
| scimark_lu                 | 66.9 ms       | 116 ms: 1.74x slower   |
| generators                 | 19.3 ms       | 33.8 ms: 1.75x slower  |
| unpickle_pure_python       | 155 us        | 274 us: 1.76x slower   |
| deltablue                  | 2.29 ms       | 4.09 ms: 1.78x slower  |
| logging_silent             | 65.2 ns       | 119 ns: 1.83x slower   |
| richards_super             | 35.1 ms       | 65.8 ms: 1.87x slower  |
| richards                   | 30.7 ms       | 57.8 ms: 1.88x slower  |
| Geometric mean             | (ref)         | 1.37x slower           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits

- Geometric mean (including insignificant results): 1.273x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.32x

# Memory
- memory change: unknown