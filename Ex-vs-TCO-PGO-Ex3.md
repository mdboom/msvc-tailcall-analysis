# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.359x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | Ex                     |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 309 ms: 1.43x slower   |
| docutils       | 1.66 sec    | 2.31 sec: 1.39x slower |
| html5lib       | 37.8 ms     | 52.5 ms: 1.39x slower  |
| sphinx         | 641 ms      | 933 ms: 1.45x slower   |
| Geometric mean | (ref)       | 1.42x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | Ex                    |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 313 ms      | 330 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 444 ms: 1.35x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 455 ms: 1.38x slower  |
| async_tree_memoization_tg  | 208 ms      | 304 ms: 1.47x slower  |
| async_tree_io              | 382 ms      | 570 ms: 1.49x slower  |
| async_tree_none_tg         | 161 ms      | 243 ms: 1.51x slower  |
| async_tree_memoization     | 205 ms      | 313 ms: 1.53x slower  |
| async_tree_io_tg           | 377 ms      | 576 ms: 1.53x slower  |
| async_tree_none            | 170 ms      | 267 ms: 1.57x slower  |
| async_generators           | 201 ms      | 348 ms: 1.73x slower  |
| coroutines                 | 12.0 ms     | 22.4 ms: 1.87x slower |
| Geometric mean             | (ref)       | 1.48x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | Ex                    |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 156 ms: 1.08x slower  |
| float          | 42.0 ms     | 78.0 ms: 1.86x slower |
| nbody          | 55.6 ms     | 103 ms: 1.86x slower  |
| Geometric mean | (ref)       | 1.55x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | Ex                    |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 123 ms: 1.03x slower  |
| regex_v8       | 14.2 ms     | 17.5 ms: 1.23x slower |
| regex_effbot   | 1.47 ms     | 1.87 ms: 1.27x slower |
| regex_compile  | 79.4 ms     | 130 ms: 1.64x slower  |
| Geometric mean | (ref)       | 1.27x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | Ex                     |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms     | 112 ms: 1.26x slower   |
| json_dumps           | 6.40 ms     | 9.44 ms: 1.48x slower  |
| xml_etree_iterparse  | 61.2 ms     | 94.3 ms: 1.54x slower  |
| json_loads           | 14.5 us     | 23.3 us: 1.61x slower  |
| xml_etree_generate   | 53.1 ms     | 92.6 ms: 1.74x slower  |
| tomli_loads          | 1.17 sec    | 2.07 sec: 1.76x slower |
| xml_etree_process    | 36.8 ms     | 66.9 ms: 1.82x slower  |
| pickle_pure_python   | 199 us      | 364 us: 1.83x slower   |
| unpickle_pure_python | 124 us      | 284 us: 2.29x slower   |
| Geometric mean       | (ref)       | 1.68x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | Ex                    |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 22.0 ms: 1.18x slower |
| python_startup         | 24.7 ms     | 29.5 ms: 1.19x slower |
| Geometric mean         | (ref)       | 1.19x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | Ex                    |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.3 ms     | 50.4 ms: 1.56x slower |
| django_template | 23.6 ms     | 38.0 ms: 1.61x slower |
| genshi_text     | 14.3 ms     | 23.9 ms: 1.67x slower |
| mako            | 6.25 ms     | 12.1 ms: 1.93x slower |
| Geometric mean  | (ref)       | 1.69x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | Ex                     |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 41.4 ms     | 21.5 ms: 1.92x faster  |
| many_optionals             | 685 us      | 559 us: 1.22x faster   |
| regex_dna                  | 120 ms      | 123 ms: 1.03x slower   |
| asyncio_websockets         | 313 ms      | 330 ms: 1.06x slower   |
| pidigits                   | 145 ms      | 156 ms: 1.08x slower   |
| create_gc_cycles           | 1.25 ms     | 1.42 ms: 1.13x slower  |
| python_startup_no_site     | 18.6 ms     | 22.0 ms: 1.18x slower  |
| python_startup             | 24.7 ms     | 29.5 ms: 1.19x slower  |
| connected_components       | 325 ms      | 395 ms: 1.21x slower   |
| regex_v8                   | 14.2 ms     | 17.5 ms: 1.23x slower  |
| shortest_path              | 352 ms      | 437 ms: 1.24x slower   |
| sqlite_synth               | 1.56 us     | 1.96 us: 1.25x slower  |
| xml_etree_parse            | 89.4 ms     | 112 ms: 1.26x slower   |
| regex_effbot               | 1.47 ms     | 1.87 ms: 1.27x slower  |
| k_core                     | 1.70 sec    | 2.18 sec: 1.28x slower |
| dulwich_log                | 40.3 ms     | 52.4 ms: 1.30x slower  |
| mdp                        | 1.43 sec    | 1.89 sec: 1.32x slower |
| pylint                     | 201 ms      | 269 ms: 1.34x slower   |
| coverage                   | 47.5 ms     | 63.7 ms: 1.34x slower  |
| json                       | 3.04 ms     | 4.07 ms: 1.34x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 444 ms: 1.35x slower   |
| async_tree_cpu_io_mixed    | 330 ms      | 455 ms: 1.38x slower   |
| html5lib                   | 37.8 ms     | 52.5 ms: 1.39x slower  |
| docutils                   | 1.66 sec    | 2.31 sec: 1.39x slower |
| meteor_contest             | 70.9 ms     | 99.5 ms: 1.40x slower  |
| telco                      | 4.59 ms     | 6.56 ms: 1.43x slower  |
| sympy_str                  | 173 ms      | 247 ms: 1.43x slower   |
| 2to3                       | 215 ms      | 309 ms: 1.43x slower   |
| sympy_integrate            | 12.8 ms     | 18.4 ms: 1.44x slower  |
| thrift                     | 491 us      | 710 us: 1.45x slower   |
| sympy_sum                  | 85.2 ms     | 123 ms: 1.45x slower   |
| sphinx                     | 641 ms      | 933 ms: 1.45x slower   |
| async_tree_memoization_tg  | 208 ms      | 304 ms: 1.47x slower   |
| pycparser                  | 689 ms      | 1.01 sec: 1.47x slower |
| json_dumps                 | 6.40 ms     | 9.44 ms: 1.48x slower  |
| sympy_expand               | 283 ms      | 419 ms: 1.48x slower   |
| async_tree_io              | 382 ms      | 570 ms: 1.49x slower   |
| async_tree_none_tg         | 161 ms      | 243 ms: 1.51x slower   |
| async_tree_memoization     | 205 ms      | 313 ms: 1.53x slower   |
| async_tree_io_tg           | 377 ms      | 576 ms: 1.53x slower   |
| gc_traversal               | 2.12 ms     | 3.25 ms: 1.54x slower  |
| xml_etree_iterparse        | 61.2 ms     | 94.3 ms: 1.54x slower  |
| logging_format             | 6.42 us     | 9.92 us: 1.55x slower  |
| pathlib                    | 24.2 ms     | 37.5 ms: 1.55x slower  |
| genshi_xml                 | 32.3 ms     | 50.4 ms: 1.56x slower  |
| async_tree_none            | 170 ms      | 267 ms: 1.57x slower   |
| typing_runtime_protocols   | 97.8 us     | 154 us: 1.57x slower   |
| sqlglot_v2_normalize       | 69.0 ms     | 109 ms: 1.58x slower   |
| logging_simple             | 5.87 us     | 9.30 us: 1.58x slower  |
| sqlglot_v2_optimize        | 32.9 ms     | 52.8 ms: 1.60x slower  |
| json_loads                 | 14.5 us     | 23.3 us: 1.61x slower  |
| django_template            | 23.6 ms     | 38.0 ms: 1.61x slower  |
| bpe_tokeniser              | 2.72 sec    | 4.45 sec: 1.63x slower |
| regex_compile              | 79.4 ms     | 130 ms: 1.64x slower   |
| deepcopy                   | 167 us      | 278 us: 1.66x slower   |
| genshi_text                | 14.3 ms     | 23.9 ms: 1.67x slower  |
| sqlglot_v2_transpile       | 993 us      | 1.69 ms: 1.70x slower  |
| deepcopy_reduce            | 1.68 us     | 2.86 us: 1.71x slower  |
| async_generators           | 201 ms      | 348 ms: 1.73x slower   |
| pprint_pformat             | 956 ms      | 1.66 sec: 1.74x slower |
| pprint_safe_repr           | 474 ms      | 825 ms: 1.74x slower   |
| xml_etree_generate         | 53.1 ms     | 92.6 ms: 1.74x slower  |
| nqueens                    | 55.2 ms     | 96.9 ms: 1.76x slower  |
| tomli_loads                | 1.17 sec    | 2.07 sec: 1.76x slower |
| scimark_fft                | 153 ms      | 276 ms: 1.80x slower   |
| sqlglot_v2_parse           | 781 us      | 1.41 ms: 1.80x slower  |
| pyflate                    | 264 ms      | 477 ms: 1.81x slower   |
| xml_etree_process          | 36.8 ms     | 66.9 ms: 1.82x slower  |
| crypto_pyaes               | 43.9 ms     | 80.1 ms: 1.82x slower  |
| pickle_pure_python         | 199 us      | 364 us: 1.83x slower   |
| float                      | 42.0 ms     | 78.0 ms: 1.86x slower  |
| nbody                      | 55.6 ms     | 103 ms: 1.86x slower   |
| fannkuch                   | 225 ms      | 418 ms: 1.86x slower   |
| coroutines                 | 12.0 ms     | 22.4 ms: 1.87x slower  |
| mako                       | 6.25 ms     | 12.1 ms: 1.93x slower  |
| raytrace                   | 162 ms      | 313 ms: 1.93x slower   |
| chaos                      | 35.4 ms     | 69.3 ms: 1.96x slower  |
| go                         | 70.5 ms     | 140 ms: 1.99x slower   |
| scimark_sparse_mat_mult    | 2.21 ms     | 4.43 ms: 2.01x slower  |
| richards                   | 29.4 ms     | 59.0 ms: 2.01x slower  |
| richards_super             | 33.7 ms     | 67.7 ms: 2.01x slower  |
| deepcopy_memo              | 16.8 us     | 34.0 us: 2.02x slower  |
| spectral_norm              | 49.4 ms     | 102 ms: 2.06x slower   |
| comprehensions             | 9.76 us     | 20.1 us: 2.06x slower  |
| scimark_monte_carlo        | 35.6 ms     | 75.8 ms: 2.13x slower  |
| hexiom                     | 3.49 ms     | 7.44 ms: 2.13x slower  |
| generators                 | 16.5 ms     | 35.6 ms: 2.16x slower  |
| deltablue                  | 1.88 ms     | 4.22 ms: 2.24x slower  |
| scimark_sor                | 60.5 ms     | 139 ms: 2.29x slower   |
| unpickle_pure_python       | 124 us      | 284 us: 2.29x slower   |
| scimark_lu                 | 50.3 ms     | 119 ms: 2.38x slower   |
| logging_silent             | 49.7 ns     | 124 ns: 2.50x slower   |
| Geometric mean             | (ref)       | 1.57x slower           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.359x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.47x
- 99% likely to have a slowdown of 1.45x

# Memory
- memory change: unknown