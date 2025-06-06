# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.358x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | Ex                     |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 309 ms: 1.46x slower   |
| docutils       | 1.67 sec    | 2.31 sec: 1.38x slower |
| html5lib       | 37.9 ms     | 52.5 ms: 1.38x slower  |
| sphinx         | 645 ms      | 933 ms: 1.45x slower   |
| Geometric mean | (ref)       | 1.42x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | Ex                    |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 301 ms      | 330 ms: 1.10x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 444 ms: 1.35x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 455 ms: 1.38x slower  |
| async_tree_memoization_tg  | 208 ms      | 304 ms: 1.46x slower  |
| async_tree_io              | 384 ms      | 570 ms: 1.48x slower  |
| async_tree_memoization     | 206 ms      | 313 ms: 1.52x slower  |
| async_tree_io_tg           | 377 ms      | 576 ms: 1.53x slower  |
| async_tree_none_tg         | 159 ms      | 243 ms: 1.53x slower  |
| async_tree_none            | 170 ms      | 267 ms: 1.57x slower  |
| async_generators           | 202 ms      | 348 ms: 1.72x slower  |
| coroutines                 | 11.9 ms     | 22.4 ms: 1.88x slower |
| Geometric mean             | (ref)       | 1.49x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | Ex                    |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 156 ms: 1.08x slower  |
| float          | 41.9 ms     | 78.0 ms: 1.86x slower |
| nbody          | 55.2 ms     | 103 ms: 1.87x slower  |
| Geometric mean | (ref)       | 1.55x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | Ex                    |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 123 ms: 1.02x slower  |
| regex_effbot   | 1.46 ms     | 1.87 ms: 1.28x slower |
| regex_v8       | 13.2 ms     | 17.5 ms: 1.32x slower |
| regex_compile  | 78.1 ms     | 130 ms: 1.66x slower  |
| Geometric mean | (ref)       | 1.30x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | Ex                     |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.3 ms     | 112 ms: 1.26x slower   |
| json_dumps           | 6.55 ms     | 9.44 ms: 1.44x slower  |
| xml_etree_iterparse  | 61.2 ms     | 94.3 ms: 1.54x slower  |
| json_loads           | 14.7 us     | 23.3 us: 1.58x slower  |
| xml_etree_generate   | 53.6 ms     | 92.6 ms: 1.73x slower  |
| tomli_loads          | 1.18 sec    | 2.07 sec: 1.76x slower |
| xml_etree_process    | 37.0 ms     | 66.9 ms: 1.81x slower  |
| pickle_pure_python   | 199 us      | 364 us: 1.83x slower   |
| unpickle_pure_python | 127 us      | 284 us: 2.23x slower   |
| Geometric mean       | (ref)       | 1.67x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | Ex                    |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 22.0 ms: 1.18x slower |
| python_startup         | 24.7 ms     | 29.5 ms: 1.19x slower |
| Geometric mean         | (ref)       | 1.18x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | Ex                    |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 50.4 ms: 1.54x slower |
| django_template | 22.9 ms     | 38.0 ms: 1.66x slower |
| genshi_text     | 14.3 ms     | 23.9 ms: 1.67x slower |
| mako            | 6.28 ms     | 12.1 ms: 1.92x slower |
| Geometric mean  | (ref)       | 1.69x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | Ex                     |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 40.7 ms     | 21.5 ms: 1.89x faster  |
| many_optionals             | 665 us      | 559 us: 1.19x faster   |
| regex_dna                  | 120 ms      | 123 ms: 1.02x slower   |
| pidigits                   | 145 ms      | 156 ms: 1.08x slower   |
| asyncio_websockets         | 301 ms      | 330 ms: 1.10x slower   |
| create_gc_cycles           | 1.27 ms     | 1.42 ms: 1.12x slower  |
| mdp                        | 1.62 sec    | 1.89 sec: 1.17x slower |
| python_startup_no_site     | 18.7 ms     | 22.0 ms: 1.18x slower  |
| python_startup             | 24.7 ms     | 29.5 ms: 1.19x slower  |
| connected_components       | 326 ms      | 395 ms: 1.21x slower   |
| shortest_path              | 353 ms      | 437 ms: 1.24x slower   |
| sqlite_synth               | 1.56 us     | 1.96 us: 1.25x slower  |
| xml_etree_parse            | 89.3 ms     | 112 ms: 1.26x slower   |
| k_core                     | 1.71 sec    | 2.18 sec: 1.28x slower |
| regex_effbot               | 1.46 ms     | 1.87 ms: 1.28x slower  |
| dulwich_log                | 40.2 ms     | 52.4 ms: 1.30x slower  |
| coverage                   | 48.2 ms     | 63.7 ms: 1.32x slower  |
| regex_v8                   | 13.2 ms     | 17.5 ms: 1.32x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 444 ms: 1.35x slower   |
| pylint                     | 198 ms      | 269 ms: 1.35x slower   |
| json                       | 2.97 ms     | 4.07 ms: 1.37x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 455 ms: 1.38x slower   |
| html5lib                   | 37.9 ms     | 52.5 ms: 1.38x slower  |
| docutils                   | 1.67 sec    | 2.31 sec: 1.38x slower |
| meteor_contest             | 70.2 ms     | 99.5 ms: 1.42x slower  |
| sympy_sum                  | 86.3 ms     | 123 ms: 1.43x slower   |
| sympy_integrate            | 12.8 ms     | 18.4 ms: 1.43x slower  |
| telco                      | 4.57 ms     | 6.56 ms: 1.44x slower  |
| json_dumps                 | 6.55 ms     | 9.44 ms: 1.44x slower  |
| sphinx                     | 645 ms      | 933 ms: 1.45x slower   |
| 2to3                       | 212 ms      | 309 ms: 1.46x slower   |
| async_tree_memoization_tg  | 208 ms      | 304 ms: 1.46x slower   |
| thrift                     | 482 us      | 710 us: 1.47x slower   |
| pycparser                  | 686 ms      | 1.01 sec: 1.48x slower |
| async_tree_io              | 384 ms      | 570 ms: 1.48x slower   |
| sympy_expand               | 282 ms      | 419 ms: 1.49x slower   |
| sympy_str                  | 164 ms      | 247 ms: 1.51x slower   |
| async_tree_memoization     | 206 ms      | 313 ms: 1.52x slower   |
| logging_format             | 6.50 us     | 9.92 us: 1.53x slower  |
| async_tree_io_tg           | 377 ms      | 576 ms: 1.53x slower   |
| async_tree_none_tg         | 159 ms      | 243 ms: 1.53x slower   |
| genshi_xml                 | 32.8 ms     | 50.4 ms: 1.54x slower  |
| xml_etree_iterparse        | 61.2 ms     | 94.3 ms: 1.54x slower  |
| gc_traversal               | 2.11 ms     | 3.25 ms: 1.54x slower  |
| logging_simple             | 5.97 us     | 9.30 us: 1.56x slower  |
| pathlib                    | 24.1 ms     | 37.5 ms: 1.56x slower  |
| typing_runtime_protocols   | 98.8 us     | 154 us: 1.56x slower   |
| async_tree_none            | 170 ms      | 267 ms: 1.57x slower   |
| sqlglot_v2_normalize       | 69.3 ms     | 109 ms: 1.57x slower   |
| json_loads                 | 14.7 us     | 23.3 us: 1.58x slower  |
| sqlglot_v2_optimize        | 33.0 ms     | 52.8 ms: 1.60x slower  |
| bpe_tokeniser              | 2.72 sec    | 4.45 sec: 1.64x slower |
| regex_compile              | 78.1 ms     | 130 ms: 1.66x slower   |
| django_template            | 22.9 ms     | 38.0 ms: 1.66x slower  |
| deepcopy                   | 167 us      | 278 us: 1.67x slower   |
| genshi_text                | 14.3 ms     | 23.9 ms: 1.67x slower  |
| deepcopy_reduce            | 1.70 us     | 2.86 us: 1.69x slower  |
| crypto_pyaes               | 47.4 ms     | 80.1 ms: 1.69x slower  |
| pprint_pformat             | 967 ms      | 1.66 sec: 1.72x slower |
| async_generators           | 202 ms      | 348 ms: 1.72x slower   |
| xml_etree_generate         | 53.6 ms     | 92.6 ms: 1.73x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.69 ms: 1.74x slower  |
| pprint_safe_repr           | 470 ms      | 825 ms: 1.76x slower   |
| tomli_loads                | 1.18 sec    | 2.07 sec: 1.76x slower |
| pyflate                    | 268 ms      | 477 ms: 1.78x slower   |
| nqueens                    | 54.4 ms     | 96.9 ms: 1.78x slower  |
| scimark_fft                | 154 ms      | 276 ms: 1.79x slower   |
| xml_etree_process          | 37.0 ms     | 66.9 ms: 1.81x slower  |
| pickle_pure_python         | 199 us      | 364 us: 1.83x slower   |
| sqlglot_v2_parse           | 766 us      | 1.41 ms: 1.84x slower  |
| float                      | 41.9 ms     | 78.0 ms: 1.86x slower  |
| nbody                      | 55.2 ms     | 103 ms: 1.87x slower   |
| fannkuch                   | 223 ms      | 418 ms: 1.88x slower   |
| chaos                      | 36.9 ms     | 69.3 ms: 1.88x slower  |
| coroutines                 | 11.9 ms     | 22.4 ms: 1.88x slower  |
| mako                       | 6.28 ms     | 12.1 ms: 1.92x slower  |
| raytrace                   | 160 ms      | 313 ms: 1.95x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 4.43 ms: 1.96x slower  |
| go                         | 70.9 ms     | 140 ms: 1.98x slower   |
| comprehensions             | 9.87 us     | 20.1 us: 2.04x slower  |
| richards_super             | 33.1 ms     | 67.7 ms: 2.05x slower  |
| deepcopy_memo              | 16.6 us     | 34.0 us: 2.05x slower  |
| richards                   | 28.7 ms     | 59.0 ms: 2.05x slower  |
| spectral_norm              | 49.4 ms     | 102 ms: 2.06x slower   |
| hexiom                     | 3.54 ms     | 7.44 ms: 2.10x slower  |
| scimark_monte_carlo        | 36.0 ms     | 75.8 ms: 2.11x slower  |
| generators                 | 16.5 ms     | 35.6 ms: 2.16x slower  |
| unpickle_pure_python       | 127 us      | 284 us: 2.23x slower   |
| deltablue                  | 1.88 ms     | 4.22 ms: 2.25x slower  |
| scimark_sor                | 61.1 ms     | 139 ms: 2.27x slower   |
| scimark_lu                 | 50.9 ms     | 119 ms: 2.35x slower   |
| logging_silent             | 49.4 ns     | 124 ns: 2.51x slower   |
| Geometric mean             | (ref)       | 1.57x slower           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.358x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.48x
- 99% likely to have a slowdown of 1.46x

# Memory
- memory change: unknown