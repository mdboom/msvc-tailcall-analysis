# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.411x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.56x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | Ex                     |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 309 ms: 1.52x slower   |
| docutils       | 1.55 sec  | 2.31 sec: 1.49x slower |
| html5lib       | 35.2 ms   | 52.5 ms: 1.49x slower  |
| sphinx         | 599 ms    | 933 ms: 1.56x slower   |
| Geometric mean | (ref)     | 1.51x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | Ex                    |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 330 ms: 1.21x faster  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 444 ms: 1.43x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 455 ms: 1.47x slower  |
| async_tree_memoization_tg  | 195 ms    | 304 ms: 1.56x slower  |
| async_tree_io              | 349 ms    | 570 ms: 1.63x slower  |
| async_tree_io_tg           | 352 ms    | 576 ms: 1.64x slower  |
| async_tree_memoization     | 190 ms    | 313 ms: 1.65x slower  |
| async_tree_none_tg         | 147 ms    | 243 ms: 1.65x slower  |
| async_tree_none            | 155 ms    | 267 ms: 1.72x slower  |
| async_generators           | 188 ms    | 348 ms: 1.85x slower  |
| coroutines                 | 11.1 ms   | 22.4 ms: 2.02x slower |
| Geometric mean             | (ref)     | 1.55x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | Ex                    |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 156 ms: 1.05x slower  |
| nbody          | 52.9 ms   | 103 ms: 1.96x slower  |
| float          | 38.5 ms   | 78.0 ms: 2.02x slower |
| Geometric mean | (ref)     | 1.61x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | Ex                    |
|----------------|:---------:|:---------------------:|
| regex_dna      | 121 ms    | 123 ms: 1.02x slower  |
| regex_effbot   | 1.65 ms   | 1.87 ms: 1.13x slower |
| regex_v8       | 13.5 ms   | 17.5 ms: 1.30x slower |
| regex_compile  | 73.4 ms   | 130 ms: 1.77x slower  |
| Geometric mean | (ref)     | 1.28x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | Ex                     |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 112 ms: 1.27x slower   |
| xml_etree_iterparse  | 60.7 ms   | 94.3 ms: 1.55x slower  |
| json_dumps           | 5.76 ms   | 9.44 ms: 1.64x slower  |
| json_loads           | 14.2 us   | 23.3 us: 1.64x slower  |
| tomli_loads          | 1.13 sec  | 2.07 sec: 1.83x slower |
| xml_etree_generate   | 48.4 ms   | 92.6 ms: 1.91x slower  |
| xml_etree_process    | 34.0 ms   | 66.9 ms: 1.97x slower  |
| pickle_pure_python   | 175 us    | 364 us: 2.08x slower   |
| unpickle_pure_python | 109 us    | 284 us: 2.61x slower   |
| Geometric mean       | (ref)     | 1.80x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | Ex                    |
|------------------------|:---------:|:---------------------:|
| python_startup_no_site | 20.0 ms   | 22.0 ms: 1.10x slower |
| python_startup         | 26.6 ms   | 29.5 ms: 1.11x slower |
| Geometric mean         | (ref)     | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | Ex                    |
|-----------------|:---------:|:---------------------:|
| genshi_xml      | 27.4 ms   | 50.4 ms: 1.84x slower |
| django_template | 19.5 ms   | 38.0 ms: 1.94x slower |
| genshi_text     | 12.0 ms   | 23.9 ms: 2.00x slower |
| mako            | 5.72 ms   | 12.1 ms: 2.11x slower |
| Geometric mean  | (ref)     | 1.97x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | Ex                     |
|----------------------------|:---------:|:----------------------:|
| asyncio_websockets         | 400 ms    | 330 ms: 1.21x faster   |
| regex_dna                  | 121 ms    | 123 ms: 1.02x slower   |
| create_gc_cycles           | 1.37 ms   | 1.42 ms: 1.03x slower  |
| pidigits                   | 148 ms    | 156 ms: 1.05x slower   |
| python_startup_no_site     | 20.0 ms   | 22.0 ms: 1.10x slower  |
| python_startup             | 26.6 ms   | 29.5 ms: 1.11x slower  |
| regex_effbot               | 1.65 ms   | 1.87 ms: 1.13x slower  |
| gc_traversal               | 2.79 ms   | 3.25 ms: 1.17x slower  |
| connected_components       | 325 ms    | 395 ms: 1.21x slower   |
| pathlib                    | 30.4 ms   | 37.5 ms: 1.23x slower  |
| xml_etree_parse            | 88.8 ms   | 112 ms: 1.27x slower   |
| shortest_path              | 345 ms    | 437 ms: 1.27x slower   |
| regex_v8                   | 13.5 ms   | 17.5 ms: 1.30x slower  |
| sqlite_synth               | 1.49 us   | 1.96 us: 1.31x slower  |
| dulwich_log                | 39.5 ms   | 52.4 ms: 1.33x slower  |
| k_core                     | 1.61 sec  | 2.18 sec: 1.36x slower |
| many_optionals             | 405 us    | 559 us: 1.38x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 444 ms: 1.43x slower   |
| json                       | 2.83 ms   | 4.07 ms: 1.44x slower  |
| meteor_contest             | 68.7 ms   | 99.5 ms: 1.45x slower  |
| mdp                        | 1.30 sec  | 1.89 sec: 1.45x slower |
| async_tree_cpu_io_mixed    | 309 ms    | 455 ms: 1.47x slower   |
| pylint                     | 182 ms    | 269 ms: 1.47x slower   |
| html5lib                   | 35.2 ms   | 52.5 ms: 1.49x slower  |
| docutils                   | 1.55 sec  | 2.31 sec: 1.49x slower |
| subparsers                 | 14.2 ms   | 21.5 ms: 1.51x slower  |
| 2to3                       | 204 ms    | 309 ms: 1.52x slower   |
| sympy_sum                  | 81.4 ms   | 123 ms: 1.52x slower   |
| xml_etree_iterparse        | 60.7 ms   | 94.3 ms: 1.55x slower  |
| coverage                   | 40.9 ms   | 63.7 ms: 1.56x slower  |
| sphinx                     | 599 ms    | 933 ms: 1.56x slower   |
| async_tree_memoization_tg  | 195 ms    | 304 ms: 1.56x slower   |
| sympy_integrate            | 11.8 ms   | 18.4 ms: 1.56x slower  |
| telco                      | 4.20 ms   | 6.56 ms: 1.56x slower  |
| pycparser                  | 637 ms    | 1.01 sec: 1.59x slower |
| sympy_expand               | 259 ms    | 419 ms: 1.62x slower   |
| sympy_str                  | 153 ms    | 247 ms: 1.62x slower   |
| async_tree_io              | 349 ms    | 570 ms: 1.63x slower   |
| async_tree_io_tg           | 352 ms    | 576 ms: 1.64x slower   |
| thrift                     | 434 us    | 710 us: 1.64x slower   |
| json_dumps                 | 5.76 ms   | 9.44 ms: 1.64x slower  |
| json_loads                 | 14.2 us   | 23.3 us: 1.64x slower  |
| async_tree_memoization     | 190 ms    | 313 ms: 1.65x slower   |
| async_tree_none_tg         | 147 ms    | 243 ms: 1.65x slower   |
| logging_format             | 5.83 us   | 9.92 us: 1.70x slower  |
| async_tree_none            | 155 ms    | 267 ms: 1.72x slower   |
| logging_simple             | 5.39 us   | 9.30 us: 1.72x slower  |
| regex_compile              | 73.4 ms   | 130 ms: 1.77x slower   |
| sqlglot_v2_optimize        | 29.8 ms   | 52.8 ms: 1.77x slower  |
| bpe_tokeniser              | 2.50 sec  | 4.45 sec: 1.78x slower |
| typing_runtime_protocols   | 86.2 us   | 154 us: 1.79x slower   |
| sqlglot_v2_normalize       | 59.9 ms   | 109 ms: 1.82x slower   |
| tomli_loads                | 1.13 sec  | 2.07 sec: 1.83x slower |
| genshi_xml                 | 27.4 ms   | 50.4 ms: 1.84x slower  |
| async_generators           | 188 ms    | 348 ms: 1.85x slower   |
| pprint_pformat             | 874 ms    | 1.66 sec: 1.90x slower |
| pprint_safe_repr           | 432 ms    | 825 ms: 1.91x slower   |
| xml_etree_generate         | 48.4 ms   | 92.6 ms: 1.91x slower  |
| deepcopy                   | 145 us    | 278 us: 1.92x slower   |
| deepcopy_reduce            | 1.49 us   | 2.86 us: 1.93x slower  |
| scimark_fft                | 143 ms    | 276 ms: 1.93x slower   |
| sqlglot_v2_transpile       | 868 us    | 1.69 ms: 1.94x slower  |
| django_template            | 19.5 ms   | 38.0 ms: 1.94x slower  |
| pyflate                    | 245 ms    | 477 ms: 1.95x slower   |
| nbody                      | 52.9 ms   | 103 ms: 1.96x slower   |
| xml_etree_process          | 34.0 ms   | 66.9 ms: 1.97x slower  |
| fannkuch                   | 209 ms    | 418 ms: 2.00x slower   |
| genshi_text                | 12.0 ms   | 23.9 ms: 2.00x slower  |
| coroutines                 | 11.1 ms   | 22.4 ms: 2.02x slower  |
| float                      | 38.5 ms   | 78.0 ms: 2.02x slower  |
| nqueens                    | 47.7 ms   | 96.9 ms: 2.03x slower  |
| crypto_pyaes               | 39.4 ms   | 80.1 ms: 2.03x slower  |
| sqlglot_v2_parse           | 686 us    | 1.41 ms: 2.05x slower  |
| pickle_pure_python         | 175 us    | 364 us: 2.08x slower   |
| mako                       | 5.72 ms   | 12.1 ms: 2.11x slower  |
| go                         | 65.1 ms   | 140 ms: 2.16x slower   |
| scimark_sparse_mat_mult    | 2.05 ms   | 4.43 ms: 2.16x slower  |
| chaos                      | 31.1 ms   | 69.3 ms: 2.23x slower  |
| generators                 | 15.8 ms   | 35.6 ms: 2.25x slower  |
| deepcopy_memo              | 15.1 us   | 34.0 us: 2.26x slower  |
| comprehensions             | 8.84 us   | 20.1 us: 2.27x slower  |
| spectral_norm              | 44.7 ms   | 102 ms: 2.27x slower   |
| raytrace                   | 137 ms    | 313 ms: 2.27x slower   |
| scimark_monte_carlo        | 32.8 ms   | 75.8 ms: 2.31x slower  |
| scimark_sor                | 59.1 ms   | 139 ms: 2.35x slower   |
| hexiom                     | 3.13 ms   | 7.44 ms: 2.38x slower  |
| scimark_lu                 | 49.1 ms   | 119 ms: 2.43x slower   |
| unpickle_pure_python       | 109 us    | 284 us: 2.61x slower   |
| deltablue                  | 1.59 ms   | 4.22 ms: 2.65x slower  |
| richards                   | 21.9 ms   | 59.0 ms: 2.69x slower  |
| richards_super             | 24.6 ms   | 67.7 ms: 2.75x slower  |
| logging_silent             | 44.5 ns   | 124 ns: 2.80x slower   |
| Geometric mean             | (ref)     | 1.71x slower           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.411x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.61x
- 95% likely to have a slowdown of 1.59x
- 99% likely to have a slowdown of 1.56x

# Memory
- memory change: unknown