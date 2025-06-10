# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.333x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | default                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 298 ms: 1.39x slower   |
| docutils       | 1.66 sec    | 2.17 sec: 1.31x slower |
| html5lib       | 37.8 ms     | 51.3 ms: 1.36x slower  |
| sphinx         | 641 ms      | 872 ms: 1.36x slower   |
| Geometric mean | (ref)       | 1.35x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | default               |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 313 ms      | 317 ms: 1.02x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 424 ms: 1.29x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 437 ms: 1.32x slower  |
| async_tree_memoization_tg  | 208 ms      | 291 ms: 1.40x slower  |
| async_tree_io              | 382 ms      | 553 ms: 1.45x slower  |
| async_tree_memoization     | 205 ms      | 297 ms: 1.45x slower  |
| async_tree_none_tg         | 161 ms      | 236 ms: 1.47x slower  |
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower  |
| async_tree_io_tg           | 377 ms      | 559 ms: 1.48x slower  |
| async_generators           | 201 ms      | 328 ms: 1.63x slower  |
| coroutines                 | 12.0 ms     | 21.9 ms: 1.83x slower |
| Geometric mean             | (ref)       | 1.42x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | default               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 152 ms: 1.05x slower  |
| float          | 42.0 ms     | 75.4 ms: 1.80x slower |
| nbody          | 55.6 ms     | 101 ms: 1.81x slower  |
| Geometric mean | (ref)       | 1.50x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | default               |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 121 ms: 1.01x slower  |
| regex_v8       | 14.2 ms     | 17.1 ms: 1.20x slower |
| regex_effbot   | 1.47 ms     | 1.81 ms: 1.23x slower |
| regex_compile  | 79.4 ms     | 125 ms: 1.57x slower  |
| Geometric mean | (ref)       | 1.24x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | default                |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms     | 108 ms: 1.21x slower   |
| json_dumps           | 6.40 ms     | 9.01 ms: 1.41x slower  |
| xml_etree_iterparse  | 61.2 ms     | 89.9 ms: 1.47x slower  |
| json_loads           | 14.5 us     | 22.3 us: 1.54x slower  |
| xml_etree_generate   | 53.1 ms     | 89.5 ms: 1.69x slower  |
| tomli_loads          | 1.17 sec    | 1.99 sec: 1.70x slower |
| xml_etree_process    | 36.8 ms     | 64.6 ms: 1.75x slower  |
| pickle_pure_python   | 199 us      | 355 us: 1.78x slower   |
| unpickle_pure_python | 124 us      | 274 us: 2.21x slower   |
| Geometric mean       | (ref)       | 1.62x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | default               |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 20.4 ms: 1.10x slower |
| python_startup         | 24.7 ms     | 27.3 ms: 1.11x slower |
| Geometric mean         | (ref)       | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | default               |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.3 ms     | 48.8 ms: 1.51x slower |
| django_template | 23.6 ms     | 36.9 ms: 1.57x slower |
| genshi_text     | 14.3 ms     | 23.2 ms: 1.62x slower |
| mako            | 6.25 ms     | 11.7 ms: 1.87x slower |
| Geometric mean  | (ref)       | 1.64x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | default                |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 41.4 ms     | 20.8 ms: 1.99x faster  |
| many_optionals             | 685 us      | 547 us: 1.25x faster   |
| regex_dna                  | 120 ms      | 121 ms: 1.01x slower   |
| asyncio_websockets         | 313 ms      | 317 ms: 1.02x slower   |
| pidigits                   | 145 ms      | 152 ms: 1.05x slower   |
| connected_components       | 325 ms      | 347 ms: 1.07x slower   |
| k_core                     | 1.70 sec    | 1.83 sec: 1.07x slower |
| shortest_path              | 352 ms      | 378 ms: 1.07x slower   |
| python_startup_no_site     | 18.6 ms     | 20.4 ms: 1.10x slower  |
| python_startup             | 24.7 ms     | 27.3 ms: 1.11x slower  |
| create_gc_cycles           | 1.25 ms     | 1.40 ms: 1.12x slower  |
| sqlite_synth               | 1.56 us     | 1.84 us: 1.18x slower  |
| regex_v8                   | 14.2 ms     | 17.1 ms: 1.20x slower  |
| xml_etree_parse            | 89.4 ms     | 108 ms: 1.21x slower   |
| regex_effbot               | 1.47 ms     | 1.81 ms: 1.23x slower  |
| pylint                     | 201 ms      | 253 ms: 1.26x slower   |
| dulwich_log                | 40.3 ms     | 51.0 ms: 1.27x slower  |
| mdp                        | 1.43 sec    | 1.81 sec: 1.27x slower |
| async_tree_cpu_io_mixed_tg | 330 ms      | 424 ms: 1.29x slower   |
| coverage                   | 47.5 ms     | 61.9 ms: 1.30x slower  |
| json                       | 3.04 ms     | 3.96 ms: 1.30x slower  |
| docutils                   | 1.66 sec    | 2.17 sec: 1.31x slower |
| async_tree_cpu_io_mixed    | 330 ms      | 437 ms: 1.32x slower   |
| meteor_contest             | 70.9 ms     | 95.9 ms: 1.35x slower  |
| html5lib                   | 37.8 ms     | 51.3 ms: 1.36x slower  |
| sphinx                     | 641 ms      | 872 ms: 1.36x slower   |
| sympy_str                  | 173 ms      | 238 ms: 1.38x slower   |
| 2to3                       | 215 ms      | 298 ms: 1.39x slower   |
| sympy_integrate            | 12.8 ms     | 17.8 ms: 1.39x slower  |
| async_tree_memoization_tg  | 208 ms      | 291 ms: 1.40x slower   |
| telco                      | 4.59 ms     | 6.44 ms: 1.40x slower  |
| sympy_sum                  | 85.2 ms     | 119 ms: 1.40x slower   |
| json_dumps                 | 6.40 ms     | 9.01 ms: 1.41x slower  |
| thrift                     | 491 us      | 694 us: 1.41x slower   |
| pathlib                    | 24.2 ms     | 34.4 ms: 1.42x slower  |
| sympy_expand               | 283 ms      | 405 ms: 1.43x slower   |
| pycparser                  | 689 ms      | 992 ms: 1.44x slower   |
| async_tree_io              | 382 ms      | 553 ms: 1.45x slower   |
| async_tree_memoization     | 205 ms      | 297 ms: 1.45x slower   |
| logging_format             | 6.42 us     | 9.33 us: 1.45x slower  |
| xml_etree_iterparse        | 61.2 ms     | 89.9 ms: 1.47x slower  |
| async_tree_none_tg         | 161 ms      | 236 ms: 1.47x slower   |
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower   |
| async_tree_io_tg           | 377 ms      | 559 ms: 1.48x slower   |
| gc_traversal               | 2.12 ms     | 3.15 ms: 1.49x slower  |
| logging_simple             | 5.87 us     | 8.87 us: 1.51x slower  |
| genshi_xml                 | 32.3 ms     | 48.8 ms: 1.51x slower  |
| typing_runtime_protocols   | 97.8 us     | 150 us: 1.54x slower   |
| sqlglot_v2_normalize       | 69.0 ms     | 106 ms: 1.54x slower   |
| json_loads                 | 14.5 us     | 22.3 us: 1.54x slower  |
| sqlglot_v2_optimize        | 32.9 ms     | 51.0 ms: 1.55x slower  |
| django_template            | 23.6 ms     | 36.9 ms: 1.57x slower  |
| regex_compile              | 79.4 ms     | 125 ms: 1.57x slower   |
| bpe_tokeniser              | 2.72 sec    | 4.30 sec: 1.58x slower |
| deepcopy                   | 167 us      | 269 us: 1.61x slower   |
| genshi_text                | 14.3 ms     | 23.2 ms: 1.62x slower  |
| async_generators           | 201 ms      | 328 ms: 1.63x slower   |
| sqlglot_v2_transpile       | 993 us      | 1.64 ms: 1.65x slower  |
| deepcopy_reduce            | 1.68 us     | 2.77 us: 1.65x slower  |
| pprint_safe_repr           | 474 ms      | 788 ms: 1.66x slower   |
| pprint_pformat             | 956 ms      | 1.61 sec: 1.68x slower |
| xml_etree_generate         | 53.1 ms     | 89.5 ms: 1.69x slower  |
| tomli_loads                | 1.17 sec    | 1.99 sec: 1.70x slower |
| nqueens                    | 55.2 ms     | 94.3 ms: 1.71x slower  |
| sqlglot_v2_parse           | 781 us      | 1.36 ms: 1.74x slower  |
| pyflate                    | 264 ms      | 462 ms: 1.75x slower   |
| scimark_fft                | 153 ms      | 269 ms: 1.75x slower   |
| xml_etree_process          | 36.8 ms     | 64.6 ms: 1.75x slower  |
| crypto_pyaes               | 43.9 ms     | 77.9 ms: 1.77x slower  |
| pickle_pure_python         | 199 us      | 355 us: 1.78x slower   |
| float                      | 42.0 ms     | 75.4 ms: 1.80x slower  |
| nbody                      | 55.6 ms     | 101 ms: 1.81x slower   |
| fannkuch                   | 225 ms      | 407 ms: 1.81x slower   |
| coroutines                 | 12.0 ms     | 21.9 ms: 1.83x slower  |
| chaos                      | 35.4 ms     | 65.2 ms: 1.84x slower  |
| mako                       | 6.25 ms     | 11.7 ms: 1.87x slower  |
| raytrace                   | 162 ms      | 304 ms: 1.88x slower   |
| go                         | 70.5 ms     | 137 ms: 1.94x slower   |
| deepcopy_memo              | 16.8 us     | 32.9 us: 1.95x slower  |
| richards_super             | 33.7 ms     | 65.8 ms: 1.95x slower  |
| scimark_sparse_mat_mult    | 2.21 ms     | 4.34 ms: 1.97x slower  |
| richards                   | 29.4 ms     | 57.8 ms: 1.97x slower  |
| spectral_norm              | 49.4 ms     | 97.7 ms: 1.98x slower  |
| comprehensions             | 9.76 us     | 19.4 us: 1.98x slower  |
| generators                 | 16.5 ms     | 33.8 ms: 2.05x slower  |
| scimark_monte_carlo        | 35.6 ms     | 73.9 ms: 2.07x slower  |
| hexiom                     | 3.49 ms     | 7.27 ms: 2.08x slower  |
| deltablue                  | 1.88 ms     | 4.09 ms: 2.17x slower  |
| unpickle_pure_python       | 124 us      | 274 us: 2.21x slower   |
| scimark_sor                | 60.5 ms     | 135 ms: 2.23x slower   |
| scimark_lu                 | 50.3 ms     | 116 ms: 2.31x slower   |
| logging_silent             | 49.7 ns     | 119 ns: 2.41x slower   |
| Geometric mean             | (ref)       | 1.51x slower           |
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.333x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: unknown