# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.364x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | Ex                     |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 309 ms: 1.43x slower   |
| docutils       | 1.63 sec   | 2.31 sec: 1.42x slower |
| html5lib       | 36.1 ms    | 52.5 ms: 1.46x slower  |
| sphinx         | 638 ms     | 933 ms: 1.46x slower   |
| Geometric mean | (ref)      | 1.44x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | Ex                    |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 317 ms     | 330 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 444 ms: 1.35x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 455 ms: 1.38x slower  |
| async_tree_memoization_tg  | 209 ms     | 304 ms: 1.46x slower  |
| async_tree_io              | 375 ms     | 570 ms: 1.52x slower  |
| async_tree_none_tg         | 159 ms     | 243 ms: 1.53x slower  |
| async_tree_memoization     | 205 ms     | 313 ms: 1.53x slower  |
| async_tree_io_tg           | 371 ms     | 576 ms: 1.55x slower  |
| async_tree_none            | 170 ms     | 267 ms: 1.57x slower  |
| async_generators           | 206 ms     | 348 ms: 1.69x slower  |
| coroutines                 | 12.4 ms    | 22.4 ms: 1.80x slower |
| Geometric mean             | (ref)      | 1.48x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | Ex                    |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 156 ms: 1.07x slower  |
| float          | 40.2 ms    | 78.0 ms: 1.94x slower |
| nbody          | 53.3 ms    | 103 ms: 1.94x slower  |
| Geometric mean | (ref)      | 1.59x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | Ex                    |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 123 ms: 1.07x slower  |
| regex_v8       | 14.1 ms    | 17.5 ms: 1.24x slower |
| regex_effbot   | 1.40 ms    | 1.87 ms: 1.34x slower |
| regex_compile  | 74.8 ms    | 130 ms: 1.73x slower  |
| Geometric mean | (ref)      | 1.33x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | Ex                     |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.0 ms    | 112 ms: 1.26x slower   |
| json_dumps           | 6.48 ms    | 9.44 ms: 1.46x slower  |
| xml_etree_iterparse  | 60.4 ms    | 94.3 ms: 1.56x slower  |
| json_loads           | 14.5 us    | 23.3 us: 1.61x slower  |
| tomli_loads          | 1.17 sec   | 2.07 sec: 1.76x slower |
| xml_etree_generate   | 51.5 ms    | 92.6 ms: 1.80x slower  |
| pickle_pure_python   | 201 us     | 364 us: 1.81x slower   |
| xml_etree_process    | 36.7 ms    | 66.9 ms: 1.82x slower  |
| unpickle_pure_python | 123 us     | 284 us: 2.32x slower   |
| Geometric mean       | (ref)      | 1.69x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | Ex                    |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 22.0 ms: 1.13x slower |
| python_startup         | 26.0 ms    | 29.5 ms: 1.13x slower |
| Geometric mean         | (ref)      | 1.13x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | Ex                    |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 38.0 ms: 1.63x slower |
| genshi_xml      | 30.7 ms    | 50.4 ms: 1.64x slower |
| genshi_text     | 14.2 ms    | 23.9 ms: 1.68x slower |
| mako            | 6.12 ms    | 12.1 ms: 1.97x slower |
| Geometric mean  | (ref)      | 1.73x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | Ex                     |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 44.9 ms    | 21.5 ms: 2.09x faster  |
| many_optionals             | 761 us     | 559 us: 1.36x faster   |
| asyncio_websockets         | 317 ms     | 330 ms: 1.04x slower   |
| regex_dna                  | 115 ms     | 123 ms: 1.07x slower   |
| pidigits                   | 146 ms     | 156 ms: 1.07x slower   |
| create_gc_cycles           | 1.27 ms    | 1.42 ms: 1.12x slower  |
| python_startup_no_site     | 19.6 ms    | 22.0 ms: 1.13x slower  |
| python_startup             | 26.0 ms    | 29.5 ms: 1.13x slower  |
| bench_mp_pool              | 89.1 ms    | 101 ms: 1.13x slower   |
| connected_components       | 321 ms     | 395 ms: 1.23x slower   |
| regex_v8                   | 14.1 ms    | 17.5 ms: 1.24x slower  |
| sqlite_synth               | 1.56 us    | 1.96 us: 1.26x slower  |
| shortest_path              | 348 ms     | 437 ms: 1.26x slower   |
| xml_etree_parse            | 89.0 ms    | 112 ms: 1.26x slower   |
| k_core                     | 1.71 sec   | 2.18 sec: 1.28x slower |
| coverage                   | 49.5 ms    | 63.7 ms: 1.29x slower  |
| dulwich_log                | 39.5 ms    | 52.4 ms: 1.33x slower  |
| regex_effbot               | 1.40 ms    | 1.87 ms: 1.34x slower  |
| mdp                        | 1.40 sec   | 1.89 sec: 1.35x slower |
| pylint                     | 199 ms     | 269 ms: 1.35x slower   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 444 ms: 1.35x slower   |
| json                       | 2.98 ms    | 4.07 ms: 1.37x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 455 ms: 1.38x slower   |
| docutils                   | 1.63 sec   | 2.31 sec: 1.42x slower |
| 2to3                       | 216 ms     | 309 ms: 1.43x slower   |
| meteor_contest             | 69.5 ms    | 99.5 ms: 1.43x slower  |
| telco                      | 4.54 ms    | 6.56 ms: 1.45x slower  |
| html5lib                   | 36.1 ms    | 52.5 ms: 1.46x slower  |
| json_dumps                 | 6.48 ms    | 9.44 ms: 1.46x slower  |
| async_tree_memoization_tg  | 209 ms     | 304 ms: 1.46x slower   |
| sphinx                     | 638 ms     | 933 ms: 1.46x slower   |
| thrift                     | 482 us     | 710 us: 1.47x slower   |
| bench_thread_pool          | 851 us     | 1.28 ms: 1.50x slower  |
| sympy_sum                  | 82.1 ms    | 123 ms: 1.50x slower   |
| sympy_integrate            | 12.2 ms    | 18.4 ms: 1.51x slower  |
| async_tree_io              | 375 ms     | 570 ms: 1.52x slower   |
| pycparser                  | 664 ms     | 1.01 sec: 1.53x slower |
| async_tree_none_tg         | 159 ms     | 243 ms: 1.53x slower   |
| async_tree_memoization     | 205 ms     | 313 ms: 1.53x slower   |
| pathlib                    | 24.3 ms    | 37.5 ms: 1.54x slower  |
| async_tree_io_tg           | 371 ms     | 576 ms: 1.55x slower   |
| sympy_expand               | 269 ms     | 419 ms: 1.56x slower   |
| typing_runtime_protocols   | 98.9 us    | 154 us: 1.56x slower   |
| xml_etree_iterparse        | 60.4 ms    | 94.3 ms: 1.56x slower  |
| logging_format             | 6.34 us    | 9.92 us: 1.57x slower  |
| sympy_str                  | 158 ms     | 247 ms: 1.57x slower   |
| gc_traversal               | 2.07 ms    | 3.25 ms: 1.57x slower  |
| async_tree_none            | 170 ms     | 267 ms: 1.57x slower   |
| logging_simple             | 5.78 us    | 9.30 us: 1.61x slower  |
| json_loads                 | 14.5 us    | 23.3 us: 1.61x slower  |
| django_template            | 23.4 ms    | 38.0 ms: 1.63x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 109 ms: 1.63x slower   |
| sqlglot_v2_optimize        | 32.2 ms    | 52.8 ms: 1.64x slower  |
| bpe_tokeniser              | 2.71 sec   | 4.45 sec: 1.64x slower |
| genshi_xml                 | 30.7 ms    | 50.4 ms: 1.64x slower  |
| genshi_text                | 14.2 ms    | 23.9 ms: 1.68x slower  |
| async_generators           | 206 ms     | 348 ms: 1.69x slower   |
| pprint_pformat             | 968 ms     | 1.66 sec: 1.71x slower |
| deepcopy_reduce            | 1.66 us    | 2.86 us: 1.72x slower  |
| pprint_safe_repr           | 478 ms     | 825 ms: 1.73x slower   |
| regex_compile              | 74.8 ms    | 130 ms: 1.73x slower   |
| deepcopy                   | 160 us     | 278 us: 1.74x slower   |
| tomli_loads                | 1.17 sec   | 2.07 sec: 1.76x slower |
| fannkuch                   | 236 ms     | 418 ms: 1.77x slower   |
| nqueens                    | 54.0 ms    | 96.9 ms: 1.79x slower  |
| xml_etree_generate         | 51.5 ms    | 92.6 ms: 1.80x slower  |
| coroutines                 | 12.4 ms    | 22.4 ms: 1.80x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.69 ms: 1.81x slower  |
| pickle_pure_python         | 201 us     | 364 us: 1.81x slower   |
| scimark_fft                | 152 ms     | 276 ms: 1.82x slower   |
| xml_etree_process          | 36.7 ms    | 66.9 ms: 1.82x slower  |
| pyflate                    | 260 ms     | 477 ms: 1.84x slower   |
| raytrace                   | 166 ms     | 313 ms: 1.88x slower   |
| sqlglot_v2_parse           | 740 us     | 1.41 ms: 1.90x slower  |
| crypto_pyaes               | 41.6 ms    | 80.1 ms: 1.92x slower  |
| chaos                      | 35.9 ms    | 69.3 ms: 1.93x slower  |
| float                      | 40.2 ms    | 78.0 ms: 1.94x slower  |
| nbody                      | 53.3 ms    | 103 ms: 1.94x slower   |
| scimark_sparse_mat_mult    | 2.26 ms    | 4.43 ms: 1.96x slower  |
| mako                       | 6.12 ms    | 12.1 ms: 1.97x slower  |
| spectral_norm              | 51.1 ms    | 102 ms: 1.99x slower   |
| deepcopy_memo              | 17.0 us    | 34.0 us: 2.00x slower  |
| scimark_monte_carlo        | 37.0 ms    | 75.8 ms: 2.05x slower  |
| scimark_sor                | 67.5 ms    | 139 ms: 2.05x slower   |
| go                         | 68.4 ms    | 140 ms: 2.06x slower   |
| comprehensions             | 9.73 us    | 20.1 us: 2.06x slower  |
| richards_super             | 32.2 ms    | 67.7 ms: 2.11x slower  |
| richards                   | 27.8 ms    | 59.0 ms: 2.12x slower  |
| hexiom                     | 3.47 ms    | 7.44 ms: 2.14x slower  |
| scimark_lu                 | 54.4 ms    | 119 ms: 2.20x slower   |
| deltablue                  | 1.85 ms    | 4.22 ms: 2.28x slower  |
| unpickle_pure_python       | 123 us     | 284 us: 2.32x slower   |
| logging_silent             | 53.3 ns    | 124 ns: 2.33x slower   |
| generators                 | 14.8 ms    | 35.6 ms: 2.40x slower  |
| Geometric mean             | (ref)      | 1.57x slower           |

- Geometric mean (including insignificant results): 1.364x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.52x
- 95% likely to have a slowdown of 1.51x
- 99% likely to have a slowdown of 1.48x

# Memory
- memory change: unknown