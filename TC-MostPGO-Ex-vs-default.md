# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.487x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TC-MostPGO-Ex          |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 209 ms: 1.43x faster   |
| docutils       | 2.17 sec | 1.74 sec: 1.25x faster |
| html5lib       | 51.3 ms  | 37.2 ms: 1.38x faster  |
| sphinx         | 872 ms   | 666 ms: 1.31x faster   |
| Geometric mean | (ref)    | 1.34x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TC-MostPGO-Ex         |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 11.8 ms: 1.85x faster |
| async_generators           | 328 ms  | 202 ms: 1.63x faster  |
| async_tree_none            | 249 ms  | 165 ms: 1.51x faster  |
| async_tree_io_tg           | 559 ms  | 374 ms: 1.50x faster  |
| async_tree_none_tg         | 236 ms  | 160 ms: 1.48x faster  |
| async_tree_io              | 553 ms  | 374 ms: 1.48x faster  |
| async_tree_memoization     | 297 ms  | 202 ms: 1.47x faster  |
| async_tree_memoization_tg  | 291 ms  | 209 ms: 1.39x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 332 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 331 ms: 1.28x faster  |
| Geometric mean             | (ref)   | 1.43x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 53.0 ms: 1.90x faster |
| float          | 75.4 ms | 40.4 ms: 1.87x faster |
| Geometric mean | (ref)   | 1.53x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 79.3 ms: 1.57x faster |
| regex_effbot   | 1.81 ms | 1.53 ms: 1.19x faster |
| regex_v8       | 17.1 ms | 15.3 ms: 1.12x faster |
| regex_dna      | 121 ms  | 125 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.19x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TC-MostPGO-Ex          |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 123 us: 2.23x faster   |
| pickle_pure_python   | 355 us   | 195 us: 1.81x faster   |
| xml_etree_process    | 64.6 ms  | 37.9 ms: 1.70x faster  |
| tomli_loads          | 1.99 sec | 1.18 sec: 1.68x faster |
| xml_etree_generate   | 89.5 ms  | 54.3 ms: 1.65x faster  |
| json_loads           | 22.3 us  | 15.8 us: 1.41x faster  |
| xml_etree_iterparse  | 89.9 ms  | 64.2 ms: 1.40x faster  |
| json_dumps           | 9.01 ms  | 6.84 ms: 1.32x faster  |
| xml_etree_parse      | 108 ms   | 92.6 ms: 1.17x faster  |
| Geometric mean       | (ref)    | 1.57x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TC-MostPGO-Ex         |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 26.4 ms: 1.04x faster |
| python_startup_no_site | 20.4 ms | 19.9 ms: 1.03x faster |
| Geometric mean         | (ref)   | 1.03x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TC-MostPGO-Ex         |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.50 ms: 1.80x faster |
| genshi_text     | 23.2 ms | 14.1 ms: 1.65x faster |
| django_template | 36.9 ms | 22.9 ms: 1.61x faster |
| genshi_xml      | 48.8 ms | 31.3 ms: 1.56x faster |
| Geometric mean  | (ref)   | 1.65x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TC-MostPGO-Ex          |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 53.0 ns: 2.25x faster  |
| unpickle_pure_python       | 274 us   | 123 us: 2.23x faster   |
| deltablue                  | 4.09 ms  | 1.87 ms: 2.18x faster  |
| scimark_sor                | 135 ms   | 63.1 ms: 2.14x faster  |
| scimark_lu                 | 116 ms   | 55.5 ms: 2.09x faster  |
| spectral_norm              | 97.7 ms  | 46.7 ms: 2.09x faster  |
| scimark_monte_carlo        | 73.9 ms  | 35.5 ms: 2.08x faster  |
| generators                 | 33.8 ms  | 16.3 ms: 2.07x faster  |
| richards                   | 57.8 ms  | 28.1 ms: 2.05x faster  |
| richards_super             | 65.8 ms  | 32.0 ms: 2.05x faster  |
| hexiom                     | 7.27 ms  | 3.58 ms: 2.03x faster  |
| comprehensions             | 19.4 us  | 9.60 us: 2.02x faster  |
| go                         | 137 ms   | 68.6 ms: 2.00x faster  |
| deepcopy_memo              | 32.9 us  | 17.0 us: 1.93x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.25 ms: 1.93x faster  |
| chaos                      | 65.2 ms  | 34.2 ms: 1.91x faster  |
| nbody                      | 101 ms   | 53.0 ms: 1.90x faster  |
| raytrace                   | 304 ms   | 162 ms: 1.88x faster   |
| float                      | 75.4 ms  | 40.4 ms: 1.87x faster  |
| crypto_pyaes               | 77.9 ms  | 41.7 ms: 1.87x faster  |
| coroutines                 | 21.9 ms  | 11.8 ms: 1.85x faster  |
| sqlglot_v2_parse           | 1.36 ms  | 742 us: 1.83x faster   |
| pickle_pure_python         | 355 us   | 195 us: 1.81x faster   |
| mako                       | 11.7 ms  | 6.50 ms: 1.80x faster  |
| scimark_fft                | 269 ms   | 151 ms: 1.78x faster   |
| pyflate                    | 462 ms   | 264 ms: 1.75x faster   |
| fannkuch                   | 407 ms   | 233 ms: 1.75x faster   |
| nqueens                    | 94.3 ms  | 54.2 ms: 1.74x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 943 us: 1.74x faster   |
| xml_etree_process          | 64.6 ms  | 37.9 ms: 1.70x faster  |
| deepcopy                   | 269 us   | 159 us: 1.70x faster   |
| tomli_loads                | 1.99 sec | 1.18 sec: 1.68x faster |
| pprint_pformat             | 1.61 sec | 963 ms: 1.67x faster   |
| xml_etree_generate         | 89.5 ms  | 54.3 ms: 1.65x faster  |
| genshi_text                | 23.2 ms  | 14.1 ms: 1.65x faster  |
| deepcopy_reduce            | 2.77 us  | 1.69 us: 1.64x faster  |
| pprint_safe_repr           | 788 ms   | 481 ms: 1.64x faster   |
| async_generators           | 328 ms   | 202 ms: 1.63x faster   |
| bpe_tokeniser              | 4.30 sec | 2.67 sec: 1.61x faster |
| django_template            | 36.9 ms  | 22.9 ms: 1.61x faster  |
| sqlglot_v2_normalize       | 106 ms   | 66.7 ms: 1.59x faster  |
| regex_compile              | 125 ms   | 79.3 ms: 1.57x faster  |
| genshi_xml                 | 48.8 ms  | 31.3 ms: 1.56x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 33.0 ms: 1.55x faster  |
| typing_runtime_protocols   | 150 us   | 98.1 us: 1.53x faster  |
| logging_simple             | 8.87 us  | 5.84 us: 1.52x faster  |
| async_tree_none            | 249 ms   | 165 ms: 1.51x faster   |
| async_tree_io_tg           | 559 ms   | 374 ms: 1.50x faster   |
| async_tree_none_tg         | 236 ms   | 160 ms: 1.48x faster   |
| async_tree_io              | 553 ms   | 374 ms: 1.48x faster   |
| async_tree_memoization     | 297 ms   | 202 ms: 1.47x faster   |
| sympy_str                  | 238 ms   | 163 ms: 1.47x faster   |
| logging_format             | 9.33 us  | 6.39 us: 1.46x faster  |
| sympy_expand               | 405 ms   | 279 ms: 1.45x faster   |
| pycparser                  | 992 ms   | 688 ms: 1.44x faster   |
| 2to3                       | 298 ms   | 209 ms: 1.43x faster   |
| thrift                     | 694 us   | 487 us: 1.43x faster   |
| gc_traversal               | 3.15 ms  | 2.21 ms: 1.43x faster  |
| json_loads                 | 22.3 us  | 15.8 us: 1.41x faster  |
| telco                      | 6.44 ms  | 4.60 ms: 1.40x faster  |
| xml_etree_iterparse        | 89.9 ms  | 64.2 ms: 1.40x faster  |
| async_tree_memoization_tg  | 291 ms   | 209 ms: 1.39x faster   |
| sympy_integrate            | 17.8 ms  | 12.9 ms: 1.38x faster  |
| html5lib                   | 51.3 ms  | 37.2 ms: 1.38x faster  |
| sympy_sum                  | 119 ms   | 88.0 ms: 1.36x faster  |
| pathlib                    | 34.4 ms  | 25.5 ms: 1.35x faster  |
| coverage                   | 61.9 ms  | 46.2 ms: 1.34x faster  |
| meteor_contest             | 95.9 ms  | 72.3 ms: 1.33x faster  |
| json_dumps                 | 9.01 ms  | 6.84 ms: 1.32x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 332 ms: 1.32x faster   |
| sphinx                     | 872 ms   | 666 ms: 1.31x faster   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 331 ms: 1.28x faster   |
| json                       | 3.96 ms  | 3.16 ms: 1.25x faster  |
| pylint                     | 253 ms   | 202 ms: 1.25x faster   |
| docutils                   | 2.17 sec | 1.74 sec: 1.25x faster |
| dulwich_log                | 51.0 ms  | 41.5 ms: 1.23x faster  |
| bench_thread_pool          | 1.01 ms  | 819 us: 1.23x faster   |
| regex_effbot               | 1.81 ms  | 1.53 ms: 1.19x faster  |
| sqlite_synth               | 1.84 us  | 1.56 us: 1.18x faster  |
| xml_etree_parse            | 108 ms   | 92.6 ms: 1.17x faster  |
| mdp                        | 1.81 sec | 1.56 sec: 1.16x faster |
| regex_v8                   | 17.1 ms  | 15.3 ms: 1.12x faster  |
| bench_mp_pool              | 96.2 ms  | 88.6 ms: 1.09x faster  |
| create_gc_cycles           | 1.40 ms  | 1.35 ms: 1.04x faster  |
| python_startup             | 27.3 ms  | 26.4 ms: 1.04x faster  |
| python_startup_no_site     | 20.4 ms  | 19.9 ms: 1.03x faster  |
| regex_dna                  | 121 ms   | 125 ms: 1.03x slower   |
| shortest_path              | 378 ms   | 399 ms: 1.06x slower   |
| connected_components       | 347 ms   | 366 ms: 1.06x slower   |
| k_core                     | 1.83 sec | 2.00 sec: 1.09x slower |
| many_optionals             | 547 us   | 669 us: 1.22x slower   |
| subparsers                 | 20.8 ms  | 41.2 ms: 1.98x slower  |
| Geometric mean             | (ref)    | 1.49x faster           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits

- Geometric mean (including insignificant results): 1.487x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.39x

# Memory
- memory change: unknown