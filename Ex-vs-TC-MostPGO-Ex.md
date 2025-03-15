# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.353x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | Ex                     |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 309 ms: 1.48x slower   |
| docutils       | 1.74 sec      | 2.31 sec: 1.32x slower |
| html5lib       | 37.2 ms       | 52.5 ms: 1.41x slower  |
| sphinx         | 666 ms        | 933 ms: 1.40x slower   |
| Geometric mean | (ref)         | 1.40x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | Ex                    |
|----------------------------|:-------------:|:---------------------:|
| asyncio_websockets         | 315 ms        | 330 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 444 ms: 1.34x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 455 ms: 1.37x slower  |
| async_tree_memoization_tg  | 209 ms        | 304 ms: 1.45x slower  |
| async_tree_io              | 374 ms        | 570 ms: 1.52x slower  |
| async_tree_none_tg         | 160 ms        | 243 ms: 1.52x slower  |
| async_tree_io_tg           | 374 ms        | 576 ms: 1.54x slower  |
| async_tree_memoization     | 202 ms        | 313 ms: 1.55x slower  |
| async_tree_none            | 165 ms        | 267 ms: 1.62x slower  |
| async_generators           | 202 ms        | 348 ms: 1.73x slower  |
| coroutines                 | 11.8 ms       | 22.4 ms: 1.90x slower |
| Geometric mean             | (ref)         | 1.49x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | Ex                    |
|----------------|:-------------:|:---------------------:|
| pidigits       | 151 ms        | 156 ms: 1.03x slower  |
| float          | 40.4 ms       | 78.0 ms: 1.93x slower |
| nbody          | 53.0 ms       | 103 ms: 1.95x slower  |
| Geometric mean | (ref)         | 1.57x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | Ex                    |
|----------------|:-------------:|:---------------------:|
| regex_dna      | 125 ms        | 123 ms: 1.01x faster  |
| regex_v8       | 15.3 ms       | 17.5 ms: 1.15x slower |
| regex_effbot   | 1.53 ms       | 1.87 ms: 1.22x slower |
| regex_compile  | 79.3 ms       | 130 ms: 1.64x slower  |
| Geometric mean | (ref)         | 1.23x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | Ex                     |
|----------------------|:-------------:|:----------------------:|
| xml_etree_parse      | 92.6 ms       | 112 ms: 1.21x slower   |
| json_dumps           | 6.84 ms       | 9.44 ms: 1.38x slower  |
| json_loads           | 15.8 us       | 23.3 us: 1.47x slower  |
| xml_etree_iterparse  | 64.2 ms       | 94.3 ms: 1.47x slower  |
| xml_etree_generate   | 54.3 ms       | 92.6 ms: 1.71x slower  |
| tomli_loads          | 1.18 sec      | 2.07 sec: 1.75x slower |
| xml_etree_process    | 37.9 ms       | 66.9 ms: 1.77x slower  |
| pickle_pure_python   | 195 us        | 364 us: 1.86x slower   |
| unpickle_pure_python | 123 us        | 284 us: 2.31x slower   |
| Geometric mean       | (ref)         | 1.63x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-MostPGO-Ex | Ex                    |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 19.9 ms       | 22.0 ms: 1.11x slower |
| python_startup         | 26.4 ms       | 29.5 ms: 1.12x slower |
| Geometric mean         | (ref)         | 1.11x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | Ex                    |
|-----------------|:-------------:|:---------------------:|
| genshi_xml      | 31.3 ms       | 50.4 ms: 1.61x slower |
| django_template | 22.9 ms       | 38.0 ms: 1.66x slower |
| genshi_text     | 14.1 ms       | 23.9 ms: 1.70x slower |
| mako            | 6.50 ms       | 12.1 ms: 1.86x slower |
| Geometric mean  | (ref)         | 1.70x slower          |

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | Ex                     |
|----------------------------|:-------------:|:----------------------:|
| subparsers                 | 41.2 ms       | 21.5 ms: 1.91x faster  |
| many_optionals             | 669 us        | 559 us: 1.20x faster   |
| regex_dna                  | 125 ms        | 123 ms: 1.01x faster   |
| pidigits                   | 151 ms        | 156 ms: 1.03x slower   |
| asyncio_websockets         | 315 ms        | 330 ms: 1.05x slower   |
| create_gc_cycles           | 1.35 ms       | 1.42 ms: 1.05x slower  |
| connected_components       | 366 ms        | 395 ms: 1.08x slower   |
| k_core                     | 2.00 sec      | 2.18 sec: 1.09x slower |
| shortest_path              | 399 ms        | 437 ms: 1.10x slower   |
| python_startup_no_site     | 19.9 ms       | 22.0 ms: 1.11x slower  |
| python_startup             | 26.4 ms       | 29.5 ms: 1.12x slower  |
| bench_mp_pool              | 88.6 ms       | 101 ms: 1.14x slower   |
| regex_v8                   | 15.3 ms       | 17.5 ms: 1.15x slower  |
| mdp                        | 1.56 sec      | 1.89 sec: 1.21x slower |
| xml_etree_parse            | 92.6 ms       | 112 ms: 1.21x slower   |
| regex_effbot               | 1.53 ms       | 1.87 ms: 1.22x slower  |
| sqlite_synth               | 1.56 us       | 1.96 us: 1.25x slower  |
| dulwich_log                | 41.5 ms       | 52.4 ms: 1.26x slower  |
| json                       | 3.16 ms       | 4.07 ms: 1.29x slower  |
| docutils                   | 1.74 sec      | 2.31 sec: 1.32x slower |
| pylint                     | 202 ms        | 269 ms: 1.33x slower   |
| async_tree_cpu_io_mixed_tg | 331 ms        | 444 ms: 1.34x slower   |
| async_tree_cpu_io_mixed    | 332 ms        | 455 ms: 1.37x slower   |
| meteor_contest             | 72.3 ms       | 99.5 ms: 1.38x slower  |
| coverage                   | 46.2 ms       | 63.7 ms: 1.38x slower  |
| json_dumps                 | 6.84 ms       | 9.44 ms: 1.38x slower  |
| sphinx                     | 666 ms        | 933 ms: 1.40x slower   |
| sympy_sum                  | 88.0 ms       | 123 ms: 1.40x slower   |
| html5lib                   | 37.2 ms       | 52.5 ms: 1.41x slower  |
| telco                      | 4.60 ms       | 6.56 ms: 1.43x slower  |
| sympy_integrate            | 12.9 ms       | 18.4 ms: 1.43x slower  |
| async_tree_memoization_tg  | 209 ms        | 304 ms: 1.45x slower   |
| thrift                     | 487 us        | 710 us: 1.46x slower   |
| json_loads                 | 15.8 us       | 23.3 us: 1.47x slower  |
| xml_etree_iterparse        | 64.2 ms       | 94.3 ms: 1.47x slower  |
| gc_traversal               | 2.21 ms       | 3.25 ms: 1.47x slower  |
| pathlib                    | 25.5 ms       | 37.5 ms: 1.47x slower  |
| pycparser                  | 688 ms        | 1.01 sec: 1.47x slower |
| 2to3                       | 209 ms        | 309 ms: 1.48x slower   |
| sympy_expand               | 279 ms        | 419 ms: 1.50x slower   |
| sympy_str                  | 163 ms        | 247 ms: 1.52x slower   |
| async_tree_io              | 374 ms        | 570 ms: 1.52x slower   |
| async_tree_none_tg         | 160 ms        | 243 ms: 1.52x slower   |
| async_tree_io_tg           | 374 ms        | 576 ms: 1.54x slower   |
| async_tree_memoization     | 202 ms        | 313 ms: 1.55x slower   |
| logging_format             | 6.39 us       | 9.92 us: 1.55x slower  |
| bench_thread_pool          | 819 us        | 1.28 ms: 1.56x slower  |
| typing_runtime_protocols   | 98.1 us       | 154 us: 1.57x slower   |
| logging_simple             | 5.84 us       | 9.30 us: 1.59x slower  |
| sqlglot_v2_optimize        | 33.0 ms       | 52.8 ms: 1.60x slower  |
| genshi_xml                 | 31.3 ms       | 50.4 ms: 1.61x slower  |
| async_tree_none            | 165 ms        | 267 ms: 1.62x slower   |
| sqlglot_v2_normalize       | 66.7 ms       | 109 ms: 1.64x slower   |
| regex_compile              | 79.3 ms       | 130 ms: 1.64x slower   |
| django_template            | 22.9 ms       | 38.0 ms: 1.66x slower  |
| bpe_tokeniser              | 2.67 sec      | 4.45 sec: 1.66x slower |
| deepcopy_reduce            | 1.69 us       | 2.86 us: 1.70x slower  |
| genshi_text                | 14.1 ms       | 23.9 ms: 1.70x slower  |
| xml_etree_generate         | 54.3 ms       | 92.6 ms: 1.71x slower  |
| pprint_safe_repr           | 481 ms        | 825 ms: 1.72x slower   |
| pprint_pformat             | 963 ms        | 1.66 sec: 1.72x slower |
| async_generators           | 202 ms        | 348 ms: 1.73x slower   |
| tomli_loads                | 1.18 sec      | 2.07 sec: 1.75x slower |
| deepcopy                   | 159 us        | 278 us: 1.75x slower   |
| xml_etree_process          | 37.9 ms       | 66.9 ms: 1.77x slower  |
| sqlglot_v2_transpile       | 943 us        | 1.69 ms: 1.79x slower  |
| nqueens                    | 54.2 ms       | 96.9 ms: 1.79x slower  |
| fannkuch                   | 233 ms        | 418 ms: 1.79x slower   |
| pyflate                    | 264 ms        | 477 ms: 1.81x slower   |
| scimark_fft                | 151 ms        | 276 ms: 1.83x slower   |
| mako                       | 6.50 ms       | 12.1 ms: 1.86x slower  |
| pickle_pure_python         | 195 us        | 364 us: 1.86x slower   |
| sqlglot_v2_parse           | 742 us        | 1.41 ms: 1.89x slower  |
| coroutines                 | 11.8 ms       | 22.4 ms: 1.90x slower  |
| crypto_pyaes               | 41.7 ms       | 80.1 ms: 1.92x slower  |
| float                      | 40.4 ms       | 78.0 ms: 1.93x slower  |
| raytrace                   | 162 ms        | 313 ms: 1.93x slower   |
| nbody                      | 53.0 ms       | 103 ms: 1.95x slower   |
| scimark_sparse_mat_mult    | 2.25 ms       | 4.43 ms: 1.97x slower  |
| deepcopy_memo              | 17.0 us       | 34.0 us: 2.00x slower  |
| chaos                      | 34.2 ms       | 69.3 ms: 2.03x slower  |
| go                         | 68.6 ms       | 140 ms: 2.05x slower   |
| hexiom                     | 3.58 ms       | 7.44 ms: 2.08x slower  |
| comprehensions             | 9.60 us       | 20.1 us: 2.09x slower  |
| richards                   | 28.1 ms       | 59.0 ms: 2.10x slower  |
| richards_super             | 32.0 ms       | 67.7 ms: 2.11x slower  |
| scimark_monte_carlo        | 35.5 ms       | 75.8 ms: 2.13x slower  |
| scimark_lu                 | 55.5 ms       | 119 ms: 2.15x slower   |
| generators                 | 16.3 ms       | 35.6 ms: 2.17x slower  |
| spectral_norm              | 46.7 ms       | 102 ms: 2.18x slower   |
| scimark_sor                | 63.1 ms       | 139 ms: 2.20x slower   |
| deltablue                  | 1.87 ms       | 4.22 ms: 2.25x slower  |
| unpickle_pure_python       | 123 us        | 284 us: 2.31x slower   |
| logging_silent             | 53.0 ns       | 124 ns: 2.34x slower   |
| Geometric mean             | (ref)         | 1.55x slower           |

- Geometric mean (including insignificant results): 1.353x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.45x

# Memory
- memory change: unknown