# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.512x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 216 ms: 1.38x faster   |
| docutils       | 2.17 sec | 1.63 sec: 1.33x faster |
| html5lib       | 51.3 ms  | 36.1 ms: 1.42x faster  |
| sphinx         | 872 ms   | 638 ms: 1.37x faster   |
| Geometric mean | (ref)    | 1.38x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 12.4 ms: 1.76x faster |
| async_generators           | 328 ms  | 206 ms: 1.59x faster  |
| async_tree_io_tg           | 559 ms  | 371 ms: 1.51x faster  |
| async_tree_none_tg         | 236 ms  | 159 ms: 1.48x faster  |
| async_tree_io              | 553 ms  | 375 ms: 1.47x faster  |
| async_tree_none            | 249 ms  | 170 ms: 1.47x faster  |
| async_tree_memoization     | 297 ms  | 205 ms: 1.45x faster  |
| async_tree_memoization_tg  | 291 ms  | 209 ms: 1.39x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 329 ms: 1.33x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 328 ms: 1.30x faster  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 53.3 ms: 1.89x faster |
| float          | 75.4 ms | 40.2 ms: 1.88x faster |
| pidigits       | 152 ms  | 146 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.55x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 74.8 ms: 1.67x faster |
| regex_effbot   | 1.81 ms | 1.40 ms: 1.30x faster |
| regex_v8       | 17.1 ms | 14.1 ms: 1.21x faster |
| regex_dna      | 121 ms  | 115 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.29x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 123 us: 2.23x faster   |
| pickle_pure_python   | 355 us   | 201 us: 1.76x faster   |
| xml_etree_process    | 64.6 ms  | 36.7 ms: 1.76x faster  |
| xml_etree_generate   | 89.5 ms  | 51.5 ms: 1.74x faster  |
| tomli_loads          | 1.99 sec | 1.17 sec: 1.70x faster |
| json_loads           | 22.3 us  | 14.5 us: 1.55x faster  |
| xml_etree_iterparse  | 89.9 ms  | 60.4 ms: 1.49x faster  |
| json_dumps           | 9.01 ms  | 6.48 ms: 1.39x faster  |
| xml_etree_parse      | 108 ms   | 89.0 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.63x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TC-PGO-Ex2            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 26.0 ms: 1.05x faster |
| python_startup_no_site | 20.4 ms | 19.6 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.12 ms: 1.91x faster |
| genshi_text     | 23.2 ms | 14.2 ms: 1.63x faster |
| genshi_xml      | 48.8 ms | 30.7 ms: 1.59x faster |
| django_template | 36.9 ms | 23.4 ms: 1.58x faster |
| Geometric mean  | (ref)   | 1.67x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| generators                 | 33.8 ms  | 14.8 ms: 2.28x faster  |
| logging_silent             | 119 ns   | 53.3 ns: 2.24x faster  |
| unpickle_pure_python       | 274 us   | 123 us: 2.23x faster   |
| deltablue                  | 4.09 ms  | 1.85 ms: 2.21x faster  |
| scimark_lu                 | 116 ms   | 54.4 ms: 2.14x faster  |
| hexiom                     | 7.27 ms  | 3.47 ms: 2.09x faster  |
| richards                   | 57.8 ms  | 27.8 ms: 2.08x faster  |
| richards_super             | 65.8 ms  | 32.2 ms: 2.05x faster  |
| go                         | 137 ms   | 68.4 ms: 2.00x faster  |
| scimark_sor                | 135 ms   | 67.5 ms: 2.00x faster  |
| scimark_monte_carlo        | 73.9 ms  | 37.0 ms: 2.00x faster  |
| comprehensions             | 19.4 us  | 9.73 us: 1.99x faster  |
| deepcopy_memo              | 32.9 us  | 17.0 us: 1.93x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.26 ms: 1.92x faster  |
| spectral_norm              | 97.7 ms  | 51.1 ms: 1.91x faster  |
| mako                       | 11.7 ms  | 6.12 ms: 1.91x faster  |
| nbody                      | 101 ms   | 53.3 ms: 1.89x faster  |
| float                      | 75.4 ms  | 40.2 ms: 1.88x faster  |
| crypto_pyaes               | 77.9 ms  | 41.6 ms: 1.87x faster  |
| sqlglot_v2_parse           | 1.36 ms  | 740 us: 1.84x faster   |
| raytrace                   | 304 ms   | 166 ms: 1.83x faster   |
| chaos                      | 65.2 ms  | 35.9 ms: 1.82x faster  |
| pyflate                    | 462 ms   | 260 ms: 1.78x faster   |
| scimark_fft                | 269 ms   | 152 ms: 1.77x faster   |
| coroutines                 | 21.9 ms  | 12.4 ms: 1.76x faster  |
| pickle_pure_python         | 355 us   | 201 us: 1.76x faster   |
| xml_etree_process          | 64.6 ms  | 36.7 ms: 1.76x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 933 us: 1.76x faster   |
| nqueens                    | 94.3 ms  | 54.0 ms: 1.75x faster  |
| xml_etree_generate         | 89.5 ms  | 51.5 ms: 1.74x faster  |
| fannkuch                   | 407 ms   | 236 ms: 1.73x faster   |
| tomli_loads                | 1.99 sec | 1.17 sec: 1.70x faster |
| deepcopy                   | 269 us   | 160 us: 1.69x faster   |
| deepcopy_reduce            | 2.77 us  | 1.66 us: 1.67x faster  |
| regex_compile              | 125 ms   | 74.8 ms: 1.67x faster  |
| pprint_pformat             | 1.61 sec | 968 ms: 1.66x faster   |
| pprint_safe_repr           | 788 ms   | 478 ms: 1.65x faster   |
| genshi_text                | 23.2 ms  | 14.2 ms: 1.63x faster  |
| async_generators           | 328 ms   | 206 ms: 1.59x faster   |
| genshi_xml                 | 48.8 ms  | 30.7 ms: 1.59x faster  |
| bpe_tokeniser              | 4.30 sec | 2.71 sec: 1.59x faster |
| sqlglot_v2_normalize       | 106 ms   | 66.9 ms: 1.59x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 32.2 ms: 1.58x faster  |
| django_template            | 36.9 ms  | 23.4 ms: 1.58x faster  |
| json_loads                 | 22.3 us  | 14.5 us: 1.55x faster  |
| logging_simple             | 8.87 us  | 5.78 us: 1.53x faster  |
| typing_runtime_protocols   | 150 us   | 98.9 us: 1.52x faster  |
| gc_traversal               | 3.15 ms  | 2.07 ms: 1.52x faster  |
| sympy_str                  | 238 ms   | 158 ms: 1.51x faster   |
| async_tree_io_tg           | 559 ms   | 371 ms: 1.51x faster   |
| sympy_expand               | 405 ms   | 269 ms: 1.50x faster   |
| pycparser                  | 992 ms   | 664 ms: 1.49x faster   |
| xml_etree_iterparse        | 89.9 ms  | 60.4 ms: 1.49x faster  |
| async_tree_none_tg         | 236 ms   | 159 ms: 1.48x faster   |
| async_tree_io              | 553 ms   | 375 ms: 1.47x faster   |
| logging_format             | 9.33 us  | 6.34 us: 1.47x faster  |
| async_tree_none            | 249 ms   | 170 ms: 1.47x faster   |
| sympy_integrate            | 17.8 ms  | 12.2 ms: 1.46x faster  |
| sympy_sum                  | 119 ms   | 82.1 ms: 1.45x faster  |
| async_tree_memoization     | 297 ms   | 205 ms: 1.45x faster   |
| thrift                     | 694 us   | 482 us: 1.44x faster   |
| html5lib                   | 51.3 ms  | 36.1 ms: 1.42x faster  |
| telco                      | 6.44 ms  | 4.54 ms: 1.42x faster  |
| pathlib                    | 34.4 ms  | 24.3 ms: 1.41x faster  |
| async_tree_memoization_tg  | 291 ms   | 209 ms: 1.39x faster   |
| json_dumps                 | 9.01 ms  | 6.48 ms: 1.39x faster  |
| meteor_contest             | 95.9 ms  | 69.5 ms: 1.38x faster  |
| 2to3                       | 298 ms   | 216 ms: 1.38x faster   |
| sphinx                     | 872 ms   | 638 ms: 1.37x faster   |
| docutils                   | 2.17 sec | 1.63 sec: 1.33x faster |
| json                       | 3.96 ms  | 2.98 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 329 ms: 1.33x faster   |
| regex_effbot               | 1.81 ms  | 1.40 ms: 1.30x faster  |
| mdp                        | 1.81 sec | 1.40 sec: 1.30x faster |
| async_tree_cpu_io_mixed_tg | 424 ms   | 328 ms: 1.30x faster   |
| dulwich_log                | 51.0 ms  | 39.5 ms: 1.29x faster  |
| pylint                     | 253 ms   | 199 ms: 1.27x faster   |
| coverage                   | 61.9 ms  | 49.5 ms: 1.25x faster  |
| xml_etree_parse            | 108 ms   | 89.0 ms: 1.21x faster  |
| regex_v8                   | 17.1 ms  | 14.1 ms: 1.21x faster  |
| sqlite_synth               | 1.84 us  | 1.56 us: 1.18x faster  |
| bench_thread_pool          | 1.01 ms  | 851 us: 1.18x faster   |
| create_gc_cycles           | 1.40 ms  | 1.27 ms: 1.11x faster  |
| shortest_path              | 378 ms   | 348 ms: 1.09x faster   |
| bench_mp_pool              | 96.2 ms  | 89.1 ms: 1.08x faster  |
| connected_components       | 347 ms   | 321 ms: 1.08x faster   |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| python_startup             | 27.3 ms  | 26.0 ms: 1.05x faster  |
| regex_dna                  | 121 ms   | 115 ms: 1.05x faster   |
| pidigits                   | 152 ms   | 146 ms: 1.04x faster   |
| python_startup_no_site     | 20.4 ms  | 19.6 ms: 1.04x faster  |
| many_optionals             | 547 us   | 761 us: 1.39x slower   |
| subparsers                 | 20.8 ms  | 44.9 ms: 2.16x slower  |
| Geometric mean             | (ref)    | 1.51x faster           |

Benchmark hidden because not significant (1): asyncio_websockets

- Geometric mean (including insignificant results): 1.512x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.46x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown