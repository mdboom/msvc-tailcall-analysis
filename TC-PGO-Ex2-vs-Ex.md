# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.573x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.48x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 216 ms: 1.43x faster   |
| docutils       | 2.31 sec | 1.63 sec: 1.42x faster |
| html5lib       | 52.5 ms  | 36.1 ms: 1.46x faster  |
| sphinx         | 933 ms   | 638 ms: 1.46x faster   |
| Geometric mean | (ref)    | 1.44x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 12.4 ms: 1.80x faster |
| async_generators           | 348 ms  | 206 ms: 1.69x faster  |
| async_tree_none            | 267 ms  | 170 ms: 1.57x faster  |
| async_tree_io_tg           | 576 ms  | 371 ms: 1.55x faster  |
| async_tree_memoization     | 313 ms  | 205 ms: 1.53x faster  |
| async_tree_none_tg         | 243 ms  | 159 ms: 1.53x faster  |
| async_tree_io              | 570 ms  | 375 ms: 1.52x faster  |
| async_tree_memoization_tg  | 304 ms  | 209 ms: 1.46x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 329 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 328 ms: 1.35x faster  |
| asyncio_websockets         | 330 ms  | 317 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.48x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 53.3 ms: 1.94x faster |
| float          | 78.0 ms | 40.2 ms: 1.94x faster |
| pidigits       | 156 ms  | 146 ms: 1.07x faster  |
| Geometric mean | (ref)   | 1.59x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 74.8 ms: 1.73x faster |
| regex_effbot   | 1.87 ms | 1.40 ms: 1.34x faster |
| regex_v8       | 17.5 ms | 14.1 ms: 1.24x faster |
| regex_dna      | 123 ms  | 115 ms: 1.07x faster  |
| Geometric mean | (ref)   | 1.33x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 123 us: 2.32x faster   |
| xml_etree_process    | 66.9 ms  | 36.7 ms: 1.82x faster  |
| pickle_pure_python   | 364 us   | 201 us: 1.81x faster   |
| xml_etree_generate   | 92.6 ms  | 51.5 ms: 1.80x faster  |
| tomli_loads          | 2.07 sec | 1.17 sec: 1.76x faster |
| json_loads           | 23.3 us  | 14.5 us: 1.61x faster  |
| xml_etree_iterparse  | 94.3 ms  | 60.4 ms: 1.56x faster  |
| json_dumps           | 9.44 ms  | 6.48 ms: 1.46x faster  |
| xml_etree_parse      | 112 ms   | 89.0 ms: 1.26x faster  |
| Geometric mean       | (ref)    | 1.69x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TC-PGO-Ex2            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.0 ms: 1.13x faster |
| python_startup_no_site | 22.0 ms | 19.6 ms: 1.13x faster |
| Geometric mean         | (ref)   | 1.13x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.12 ms: 1.97x faster |
| genshi_text     | 23.9 ms | 14.2 ms: 1.68x faster |
| genshi_xml      | 50.4 ms | 30.7 ms: 1.64x faster |
| django_template | 38.0 ms | 23.4 ms: 1.63x faster |
| Geometric mean  | (ref)   | 1.73x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| generators                 | 35.6 ms  | 14.8 ms: 2.40x faster  |
| logging_silent             | 124 ns   | 53.3 ns: 2.33x faster  |
| unpickle_pure_python       | 284 us   | 123 us: 2.32x faster   |
| deltablue                  | 4.22 ms  | 1.85 ms: 2.28x faster  |
| scimark_lu                 | 119 ms   | 54.4 ms: 2.20x faster  |
| hexiom                     | 7.44 ms  | 3.47 ms: 2.14x faster  |
| richards                   | 59.0 ms  | 27.8 ms: 2.12x faster  |
| richards_super             | 67.7 ms  | 32.2 ms: 2.11x faster  |
| comprehensions             | 20.1 us  | 9.73 us: 2.06x faster  |
| go                         | 140 ms   | 68.4 ms: 2.06x faster  |
| scimark_sor                | 139 ms   | 67.5 ms: 2.05x faster  |
| scimark_monte_carlo        | 75.8 ms  | 37.0 ms: 2.05x faster  |
| deepcopy_memo              | 34.0 us  | 17.0 us: 2.00x faster  |
| spectral_norm              | 102 ms   | 51.1 ms: 1.99x faster  |
| mako                       | 12.1 ms  | 6.12 ms: 1.97x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.26 ms: 1.96x faster  |
| nbody                      | 103 ms   | 53.3 ms: 1.94x faster  |
| float                      | 78.0 ms  | 40.2 ms: 1.94x faster  |
| chaos                      | 69.3 ms  | 35.9 ms: 1.93x faster  |
| crypto_pyaes               | 80.1 ms  | 41.6 ms: 1.92x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 740 us: 1.90x faster   |
| raytrace                   | 313 ms   | 166 ms: 1.88x faster   |
| pyflate                    | 477 ms   | 260 ms: 1.84x faster   |
| xml_etree_process          | 66.9 ms  | 36.7 ms: 1.82x faster  |
| scimark_fft                | 276 ms   | 152 ms: 1.82x faster   |
| pickle_pure_python         | 364 us   | 201 us: 1.81x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 933 us: 1.81x faster   |
| coroutines                 | 22.4 ms  | 12.4 ms: 1.80x faster  |
| xml_etree_generate         | 92.6 ms  | 51.5 ms: 1.80x faster  |
| nqueens                    | 96.9 ms  | 54.0 ms: 1.79x faster  |
| fannkuch                   | 418 ms   | 236 ms: 1.77x faster   |
| tomli_loads                | 2.07 sec | 1.17 sec: 1.76x faster |
| deepcopy                   | 278 us   | 160 us: 1.74x faster   |
| regex_compile              | 130 ms   | 74.8 ms: 1.73x faster  |
| pprint_safe_repr           | 825 ms   | 478 ms: 1.73x faster   |
| deepcopy_reduce            | 2.86 us  | 1.66 us: 1.72x faster  |
| pprint_pformat             | 1.66 sec | 968 ms: 1.71x faster   |
| async_generators           | 348 ms   | 206 ms: 1.69x faster   |
| genshi_text                | 23.9 ms  | 14.2 ms: 1.68x faster  |
| genshi_xml                 | 50.4 ms  | 30.7 ms: 1.64x faster  |
| bpe_tokeniser              | 4.45 sec | 2.71 sec: 1.64x faster |
| sqlglot_v2_optimize        | 52.8 ms  | 32.2 ms: 1.64x faster  |
| sqlglot_v2_normalize       | 109 ms   | 66.9 ms: 1.63x faster  |
| django_template            | 38.0 ms  | 23.4 ms: 1.63x faster  |
| json_loads                 | 23.3 us  | 14.5 us: 1.61x faster  |
| logging_simple             | 9.30 us  | 5.78 us: 1.61x faster  |
| async_tree_none            | 267 ms   | 170 ms: 1.57x faster   |
| gc_traversal               | 3.25 ms  | 2.07 ms: 1.57x faster  |
| sympy_str                  | 247 ms   | 158 ms: 1.57x faster   |
| logging_format             | 9.92 us  | 6.34 us: 1.57x faster  |
| xml_etree_iterparse        | 94.3 ms  | 60.4 ms: 1.56x faster  |
| typing_runtime_protocols   | 154 us   | 98.9 us: 1.56x faster  |
| sympy_expand               | 419 ms   | 269 ms: 1.56x faster   |
| async_tree_io_tg           | 576 ms   | 371 ms: 1.55x faster   |
| pathlib                    | 37.5 ms  | 24.3 ms: 1.54x faster  |
| async_tree_memoization     | 313 ms   | 205 ms: 1.53x faster   |
| async_tree_none_tg         | 243 ms   | 159 ms: 1.53x faster   |
| pycparser                  | 1.01 sec | 664 ms: 1.53x faster   |
| async_tree_io              | 570 ms   | 375 ms: 1.52x faster   |
| sympy_integrate            | 18.4 ms  | 12.2 ms: 1.51x faster  |
| sympy_sum                  | 123 ms   | 82.1 ms: 1.50x faster  |
| bench_thread_pool          | 1.28 ms  | 851 us: 1.50x faster   |
| thrift                     | 710 us   | 482 us: 1.47x faster   |
| sphinx                     | 933 ms   | 638 ms: 1.46x faster   |
| async_tree_memoization_tg  | 304 ms   | 209 ms: 1.46x faster   |
| json_dumps                 | 9.44 ms  | 6.48 ms: 1.46x faster  |
| html5lib                   | 52.5 ms  | 36.1 ms: 1.46x faster  |
| telco                      | 6.56 ms  | 4.54 ms: 1.45x faster  |
| meteor_contest             | 99.5 ms  | 69.5 ms: 1.43x faster  |
| 2to3                       | 309 ms   | 216 ms: 1.43x faster   |
| docutils                   | 2.31 sec | 1.63 sec: 1.42x faster |
| async_tree_cpu_io_mixed    | 455 ms   | 329 ms: 1.38x faster   |
| json                       | 4.07 ms  | 2.98 ms: 1.37x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 328 ms: 1.35x faster   |
| pylint                     | 269 ms   | 199 ms: 1.35x faster   |
| mdp                        | 1.89 sec | 1.40 sec: 1.35x faster |
| regex_effbot               | 1.87 ms  | 1.40 ms: 1.34x faster  |
| dulwich_log                | 52.4 ms  | 39.5 ms: 1.33x faster  |
| coverage                   | 63.7 ms  | 49.5 ms: 1.29x faster  |
| k_core                     | 2.18 sec | 1.71 sec: 1.28x faster |
| xml_etree_parse            | 112 ms   | 89.0 ms: 1.26x faster  |
| shortest_path              | 437 ms   | 348 ms: 1.26x faster   |
| sqlite_synth               | 1.96 us  | 1.56 us: 1.26x faster  |
| regex_v8                   | 17.5 ms  | 14.1 ms: 1.24x faster  |
| connected_components       | 395 ms   | 321 ms: 1.23x faster   |
| bench_mp_pool              | 101 ms   | 89.1 ms: 1.13x faster  |
| python_startup             | 29.5 ms  | 26.0 ms: 1.13x faster  |
| python_startup_no_site     | 22.0 ms  | 19.6 ms: 1.13x faster  |
| create_gc_cycles           | 1.42 ms  | 1.27 ms: 1.12x faster  |
| pidigits                   | 156 ms   | 146 ms: 1.07x faster   |
| regex_dna                  | 123 ms   | 115 ms: 1.07x faster   |
| asyncio_websockets         | 330 ms   | 317 ms: 1.04x faster   |
| many_optionals             | 559 us   | 761 us: 1.36x slower   |
| subparsers                 | 21.5 ms  | 44.9 ms: 2.09x slower  |
| Geometric mean             | (ref)    | 1.57x faster           |

- Geometric mean (including insignificant results): 1.573x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.51x
- 99% likely to have a speedup of 1.48x

# Memory
- memory change: unknown