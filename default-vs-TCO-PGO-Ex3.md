# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.332x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | default                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 298 ms: 1.41x slower   |
| docutils       | 1.67 sec    | 2.17 sec: 1.30x slower |
| html5lib       | 37.9 ms     | 51.3 ms: 1.35x slower  |
| sphinx         | 645 ms      | 872 ms: 1.35x slower   |
| Geometric mean | (ref)       | 1.35x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | default               |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 301 ms      | 317 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 424 ms: 1.29x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 437 ms: 1.32x slower  |
| async_tree_memoization_tg  | 208 ms      | 291 ms: 1.40x slower  |
| async_tree_io              | 384 ms      | 553 ms: 1.44x slower  |
| async_tree_memoization     | 206 ms      | 297 ms: 1.45x slower  |
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower  |
| async_tree_io_tg           | 377 ms      | 559 ms: 1.48x slower  |
| async_tree_none_tg         | 159 ms      | 236 ms: 1.49x slower  |
| async_generators           | 202 ms      | 328 ms: 1.62x slower  |
| coroutines                 | 11.9 ms     | 21.9 ms: 1.84x slower |
| Geometric mean             | (ref)       | 1.43x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | default               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 152 ms: 1.05x slower  |
| float          | 41.9 ms     | 75.4 ms: 1.80x slower |
| nbody          | 55.2 ms     | 101 ms: 1.82x slower  |
| Geometric mean | (ref)       | 1.51x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | default               |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.46 ms     | 1.81 ms: 1.24x slower |
| regex_v8       | 13.2 ms     | 17.1 ms: 1.29x slower |
| regex_compile  | 78.1 ms     | 125 ms: 1.60x slower  |
| Geometric mean | (ref)       | 1.27x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | default                |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.3 ms     | 108 ms: 1.21x slower   |
| json_dumps           | 6.55 ms     | 9.01 ms: 1.38x slower  |
| xml_etree_iterparse  | 61.2 ms     | 89.9 ms: 1.47x slower  |
| json_loads           | 14.7 us     | 22.3 us: 1.52x slower  |
| xml_etree_generate   | 53.6 ms     | 89.5 ms: 1.67x slower  |
| tomli_loads          | 1.18 sec    | 1.99 sec: 1.69x slower |
| xml_etree_process    | 37.0 ms     | 64.6 ms: 1.74x slower  |
| pickle_pure_python   | 199 us      | 355 us: 1.78x slower   |
| unpickle_pure_python | 127 us      | 274 us: 2.15x slower   |
| Geometric mean       | (ref)       | 1.60x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | default               |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 20.4 ms: 1.09x slower |
| python_startup         | 24.7 ms     | 27.3 ms: 1.11x slower |
| Geometric mean         | (ref)       | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | default               |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 48.8 ms: 1.49x slower |
| django_template | 22.9 ms     | 36.9 ms: 1.61x slower |
| genshi_text     | 14.3 ms     | 23.2 ms: 1.62x slower |
| mako            | 6.28 ms     | 11.7 ms: 1.86x slower |
| Geometric mean  | (ref)       | 1.64x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | default                |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 40.7 ms     | 20.8 ms: 1.96x faster  |
| many_optionals             | 665 us      | 547 us: 1.22x faster   |
| pidigits                   | 145 ms      | 152 ms: 1.05x slower   |
| asyncio_websockets         | 301 ms      | 317 ms: 1.06x slower   |
| connected_components       | 326 ms      | 347 ms: 1.06x slower   |
| k_core                     | 1.71 sec    | 1.83 sec: 1.07x slower |
| shortest_path              | 353 ms      | 378 ms: 1.07x slower   |
| python_startup_no_site     | 18.7 ms     | 20.4 ms: 1.09x slower  |
| create_gc_cycles           | 1.27 ms     | 1.40 ms: 1.10x slower  |
| python_startup             | 24.7 ms     | 27.3 ms: 1.11x slower  |
| mdp                        | 1.62 sec    | 1.81 sec: 1.12x slower |
| sqlite_synth               | 1.56 us     | 1.84 us: 1.18x slower  |
| xml_etree_parse            | 89.3 ms     | 108 ms: 1.21x slower   |
| regex_effbot               | 1.46 ms     | 1.81 ms: 1.24x slower  |
| dulwich_log                | 40.2 ms     | 51.0 ms: 1.27x slower  |
| pylint                     | 198 ms      | 253 ms: 1.27x slower   |
| coverage                   | 48.2 ms     | 61.9 ms: 1.28x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 424 ms: 1.29x slower   |
| regex_v8                   | 13.2 ms     | 17.1 ms: 1.29x slower  |
| docutils                   | 1.67 sec    | 2.17 sec: 1.30x slower |
| async_tree_cpu_io_mixed    | 330 ms      | 437 ms: 1.32x slower   |
| json                       | 2.97 ms     | 3.96 ms: 1.33x slower  |
| sphinx                     | 645 ms      | 872 ms: 1.35x slower   |
| html5lib                   | 37.9 ms     | 51.3 ms: 1.35x slower  |
| meteor_contest             | 70.2 ms     | 95.9 ms: 1.37x slower  |
| json_dumps                 | 6.55 ms     | 9.01 ms: 1.38x slower  |
| sympy_sum                  | 86.3 ms     | 119 ms: 1.38x slower   |
| sympy_integrate            | 12.8 ms     | 17.8 ms: 1.39x slower  |
| async_tree_memoization_tg  | 208 ms      | 291 ms: 1.40x slower   |
| telco                      | 4.57 ms     | 6.44 ms: 1.41x slower  |
| 2to3                       | 212 ms      | 298 ms: 1.41x slower   |
| pathlib                    | 24.1 ms     | 34.4 ms: 1.43x slower  |
| sympy_expand               | 282 ms      | 405 ms: 1.44x slower   |
| logging_format             | 6.50 us     | 9.33 us: 1.44x slower  |
| thrift                     | 482 us      | 694 us: 1.44x slower   |
| async_tree_io              | 384 ms      | 553 ms: 1.44x slower   |
| async_tree_memoization     | 206 ms      | 297 ms: 1.45x slower   |
| pycparser                  | 686 ms      | 992 ms: 1.45x slower   |
| sympy_str                  | 164 ms      | 238 ms: 1.45x slower   |
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower   |
| xml_etree_iterparse        | 61.2 ms     | 89.9 ms: 1.47x slower  |
| async_tree_io_tg           | 377 ms      | 559 ms: 1.48x slower   |
| logging_simple             | 5.97 us     | 8.87 us: 1.48x slower  |
| genshi_xml                 | 32.8 ms     | 48.8 ms: 1.49x slower  |
| async_tree_none_tg         | 159 ms      | 236 ms: 1.49x slower   |
| gc_traversal               | 2.11 ms     | 3.15 ms: 1.50x slower  |
| json_loads                 | 14.7 us     | 22.3 us: 1.52x slower  |
| typing_runtime_protocols   | 98.8 us     | 150 us: 1.52x slower   |
| sqlglot_v2_normalize       | 69.3 ms     | 106 ms: 1.53x slower   |
| sqlglot_v2_optimize        | 33.0 ms     | 51.0 ms: 1.54x slower  |
| bpe_tokeniser              | 2.72 sec    | 4.30 sec: 1.58x slower |
| regex_compile              | 78.1 ms     | 125 ms: 1.60x slower   |
| django_template            | 22.9 ms     | 36.9 ms: 1.61x slower  |
| deepcopy                   | 167 us      | 269 us: 1.61x slower   |
| async_generators           | 202 ms      | 328 ms: 1.62x slower   |
| genshi_text                | 14.3 ms     | 23.2 ms: 1.62x slower  |
| deepcopy_reduce            | 1.70 us     | 2.77 us: 1.63x slower  |
| crypto_pyaes               | 47.4 ms     | 77.9 ms: 1.64x slower  |
| pprint_pformat             | 967 ms      | 1.61 sec: 1.67x slower |
| xml_etree_generate         | 53.6 ms     | 89.5 ms: 1.67x slower  |
| pprint_safe_repr           | 470 ms      | 788 ms: 1.68x slower   |
| sqlglot_v2_transpile       | 970 us      | 1.64 ms: 1.69x slower  |
| tomli_loads                | 1.18 sec    | 1.99 sec: 1.69x slower |
| pyflate                    | 268 ms      | 462 ms: 1.72x slower   |
| nqueens                    | 54.4 ms     | 94.3 ms: 1.74x slower  |
| scimark_fft                | 154 ms      | 269 ms: 1.74x slower   |
| xml_etree_process          | 37.0 ms     | 64.6 ms: 1.74x slower  |
| chaos                      | 36.9 ms     | 65.2 ms: 1.77x slower  |
| sqlglot_v2_parse           | 766 us      | 1.36 ms: 1.77x slower  |
| pickle_pure_python         | 199 us      | 355 us: 1.78x slower   |
| float                      | 41.9 ms     | 75.4 ms: 1.80x slower  |
| nbody                      | 55.2 ms     | 101 ms: 1.82x slower   |
| fannkuch                   | 223 ms      | 407 ms: 1.83x slower   |
| coroutines                 | 11.9 ms     | 21.9 ms: 1.84x slower  |
| mako                       | 6.28 ms     | 11.7 ms: 1.86x slower  |
| raytrace                   | 160 ms      | 304 ms: 1.89x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 4.34 ms: 1.92x slower  |
| go                         | 70.9 ms     | 137 ms: 1.93x slower   |
| comprehensions             | 9.87 us     | 19.4 us: 1.96x slower  |
| spectral_norm              | 49.4 ms     | 97.7 ms: 1.98x slower  |
| deepcopy_memo              | 16.6 us     | 32.9 us: 1.98x slower  |
| richards_super             | 33.1 ms     | 65.8 ms: 1.99x slower  |
| richards                   | 28.7 ms     | 57.8 ms: 2.01x slower  |
| generators                 | 16.5 ms     | 33.8 ms: 2.05x slower  |
| scimark_monte_carlo        | 36.0 ms     | 73.9 ms: 2.06x slower  |
| hexiom                     | 3.54 ms     | 7.27 ms: 2.06x slower  |
| unpickle_pure_python       | 127 us      | 274 us: 2.15x slower   |
| deltablue                  | 1.88 ms     | 4.09 ms: 2.17x slower  |
| scimark_sor                | 61.1 ms     | 135 ms: 2.21x slower   |
| scimark_lu                 | 50.9 ms     | 116 ms: 2.28x slower   |
| logging_silent             | 49.4 ns     | 119 ns: 2.42x slower   |
| Geometric mean             | (ref)       | 1.51x slower           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.332x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: unknown