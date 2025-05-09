# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.509x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 216 ms: 1.36x faster   |
| docutils       | 2.11 sec | 1.63 sec: 1.30x faster |
| html5lib       | 51.3 ms  | 36.1 ms: 1.42x faster  |
| sphinx         | 843 ms   | 638 ms: 1.32x faster   |
| Geometric mean | (ref)    | 1.35x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 12.4 ms: 1.77x faster |
| async_generators           | 321 ms  | 206 ms: 1.56x faster  |
| async_tree_io_tg           | 563 ms  | 371 ms: 1.52x faster  |
| async_tree_none_tg         | 236 ms  | 159 ms: 1.48x faster  |
| async_tree_io              | 551 ms  | 375 ms: 1.47x faster  |
| async_tree_none            | 248 ms  | 170 ms: 1.46x faster  |
| async_tree_memoization     | 297 ms  | 205 ms: 1.45x faster  |
| async_tree_memoization_tg  | 292 ms  | 209 ms: 1.40x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 329 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 328 ms: 1.31x faster  |
| asyncio_websockets         | 311 ms  | 317 ms: 1.02x slower  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 53.3 ms: 1.86x faster |
| float          | 73.5 ms | 40.2 ms: 1.83x faster |
| pidigits       | 148 ms  | 146 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.51x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 74.8 ms: 1.64x faster |
| regex_effbot   | 1.77 ms | 1.40 ms: 1.27x faster |
| regex_v8       | 17.0 ms | 14.1 ms: 1.20x faster |
| regex_dna      | 118 ms  | 115 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.27x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 123 us: 2.21x faster   |
| pickle_pure_python   | 354 us   | 201 us: 1.76x faster   |
| xml_etree_process    | 63.0 ms  | 36.7 ms: 1.72x faster  |
| xml_etree_generate   | 87.5 ms  | 51.5 ms: 1.70x faster  |
| tomli_loads          | 1.97 sec | 1.17 sec: 1.68x faster |
| json_loads           | 21.4 us  | 14.5 us: 1.48x faster  |
| xml_etree_iterparse  | 87.5 ms  | 60.4 ms: 1.45x faster  |
| json_dumps           | 8.99 ms  | 6.48 ms: 1.39x faster  |
| xml_etree_parse      | 108 ms   | 89.0 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.60x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TC-PGO-Ex2            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 26.0 ms: 1.05x faster |
| python_startup_no_site | 20.3 ms | 19.6 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.04x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 6.12 ms: 1.87x faster |
| genshi_text     | 23.4 ms | 14.2 ms: 1.64x faster |
| genshi_xml      | 48.8 ms | 30.7 ms: 1.59x faster |
| django_template | 35.8 ms | 23.4 ms: 1.53x faster |
| Geometric mean  | (ref)   | 1.65x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 121 ns   | 53.3 ns: 2.28x faster  |
| generators                 | 33.5 ms  | 14.8 ms: 2.26x faster  |
| unpickle_pure_python       | 271 us   | 123 us: 2.21x faster   |
| deltablue                  | 4.08 ms  | 1.85 ms: 2.20x faster  |
| scimark_lu                 | 116 ms   | 54.4 ms: 2.13x faster  |
| hexiom                     | 7.27 ms  | 3.47 ms: 2.09x faster  |
| scimark_monte_carlo        | 75.2 ms  | 37.0 ms: 2.03x faster  |
| go                         | 138 ms   | 68.4 ms: 2.02x faster  |
| comprehensions             | 19.4 us  | 9.73 us: 1.99x faster  |
| scimark_sor                | 133 ms   | 67.5 ms: 1.97x faster  |
| deepcopy_memo              | 33.0 us  | 17.0 us: 1.94x faster  |
| spectral_norm              | 97.1 ms  | 51.1 ms: 1.90x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.26 ms: 1.89x faster  |
| mako                       | 11.4 ms  | 6.12 ms: 1.87x faster  |
| chaos                      | 67.0 ms  | 35.9 ms: 1.87x faster  |
| nbody                      | 98.8 ms  | 53.3 ms: 1.86x faster  |
| crypto_pyaes               | 76.8 ms  | 41.6 ms: 1.84x faster  |
| raytrace                   | 306 ms   | 166 ms: 1.84x faster   |
| richards                   | 51.0 ms  | 27.8 ms: 1.83x faster  |
| float                      | 73.5 ms  | 40.2 ms: 1.83x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 740 us: 1.82x faster   |
| richards_super             | 58.0 ms  | 32.2 ms: 1.80x faster  |
| coroutines                 | 22.1 ms  | 12.4 ms: 1.77x faster  |
| pyflate                    | 457 ms   | 260 ms: 1.76x faster   |
| scimark_fft                | 267 ms   | 152 ms: 1.76x faster   |
| pickle_pure_python         | 354 us   | 201 us: 1.76x faster   |
| sqlglot_v2_transpile       | 1.62 ms  | 933 us: 1.73x faster   |
| nqueens                    | 93.2 ms  | 54.0 ms: 1.72x faster  |
| xml_etree_process          | 63.0 ms  | 36.7 ms: 1.72x faster  |
| xml_etree_generate         | 87.5 ms  | 51.5 ms: 1.70x faster  |
| tomli_loads                | 1.97 sec | 1.17 sec: 1.68x faster |
| pprint_pformat             | 1.61 sec | 968 ms: 1.67x faster   |
| deepcopy                   | 266 us   | 160 us: 1.66x faster   |
| pprint_safe_repr           | 789 ms   | 478 ms: 1.65x faster   |
| genshi_text                | 23.4 ms  | 14.2 ms: 1.64x faster  |
| regex_compile              | 123 ms   | 74.8 ms: 1.64x faster  |
| fannkuch                   | 386 ms   | 236 ms: 1.64x faster   |
| deepcopy_reduce            | 2.71 us  | 1.66 us: 1.63x faster  |
| bpe_tokeniser              | 4.30 sec | 2.71 sec: 1.59x faster |
| genshi_xml                 | 48.8 ms  | 30.7 ms: 1.59x faster  |
| async_generators           | 321 ms   | 206 ms: 1.56x faster   |
| sqlglot_v2_normalize       | 103 ms   | 66.9 ms: 1.55x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 32.2 ms: 1.54x faster  |
| django_template            | 35.8 ms  | 23.4 ms: 1.53x faster  |
| async_tree_io_tg           | 563 ms   | 371 ms: 1.52x faster   |
| logging_simple             | 8.63 us  | 5.78 us: 1.49x faster  |
| sympy_str                  | 234 ms   | 158 ms: 1.49x faster   |
| sympy_expand               | 399 ms   | 269 ms: 1.48x faster   |
| json_loads                 | 21.4 us  | 14.5 us: 1.48x faster  |
| typing_runtime_protocols   | 146 us   | 98.9 us: 1.48x faster  |
| async_tree_none_tg         | 236 ms   | 159 ms: 1.48x faster   |
| async_tree_io              | 551 ms   | 375 ms: 1.47x faster   |
| async_tree_none            | 248 ms   | 170 ms: 1.46x faster   |
| pycparser                  | 968 ms   | 664 ms: 1.46x faster   |
| async_tree_memoization     | 297 ms   | 205 ms: 1.45x faster   |
| xml_etree_iterparse        | 87.5 ms  | 60.4 ms: 1.45x faster  |
| logging_format             | 9.13 us  | 6.34 us: 1.44x faster  |
| sympy_integrate            | 17.5 ms  | 12.2 ms: 1.44x faster  |
| sympy_sum                  | 118 ms   | 82.1 ms: 1.43x faster  |
| html5lib                   | 51.3 ms  | 36.1 ms: 1.42x faster  |
| thrift                     | 680 us   | 482 us: 1.41x faster   |
| async_tree_memoization_tg  | 292 ms   | 209 ms: 1.40x faster   |
| telco                      | 6.34 ms  | 4.54 ms: 1.40x faster  |
| json_dumps                 | 8.99 ms  | 6.48 ms: 1.39x faster  |
| meteor_contest             | 95.0 ms  | 69.5 ms: 1.37x faster  |
| 2to3                       | 293 ms   | 216 ms: 1.36x faster   |
| gc_traversal               | 2.79 ms  | 2.07 ms: 1.35x faster  |
| sphinx                     | 843 ms   | 638 ms: 1.32x faster   |
| json                       | 3.94 ms  | 2.98 ms: 1.32x faster  |
| async_tree_cpu_io_mixed    | 434 ms   | 329 ms: 1.32x faster   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 328 ms: 1.31x faster   |
| mdp                        | 1.82 sec | 1.40 sec: 1.30x faster |
| docutils                   | 2.11 sec | 1.63 sec: 1.30x faster |
| dulwich_log                | 50.5 ms  | 39.5 ms: 1.28x faster  |
| regex_effbot               | 1.77 ms  | 1.40 ms: 1.27x faster  |
| pylint                     | 249 ms   | 199 ms: 1.25x faster   |
| coverage                   | 61.1 ms  | 49.5 ms: 1.24x faster  |
| xml_etree_parse            | 108 ms   | 89.0 ms: 1.21x faster  |
| regex_v8                   | 17.0 ms  | 14.1 ms: 1.20x faster  |
| bench_thread_pool          | 1.01 ms  | 851 us: 1.19x faster   |
| many_optionals             | 890 us   | 761 us: 1.17x faster   |
| sqlite_synth               | 1.78 us  | 1.56 us: 1.15x faster  |
| subparsers                 | 50.4 ms  | 44.9 ms: 1.12x faster  |
| create_gc_cycles           | 1.40 ms  | 1.27 ms: 1.10x faster  |
| shortest_path              | 384 ms   | 348 ms: 1.10x faster   |
| pathlib                    | 26.8 ms  | 24.3 ms: 1.10x faster  |
| bench_mp_pool              | 97.6 ms  | 89.1 ms: 1.10x faster  |
| connected_components       | 351 ms   | 321 ms: 1.09x faster   |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| python_startup             | 27.2 ms  | 26.0 ms: 1.05x faster  |
| python_startup_no_site     | 20.3 ms  | 19.6 ms: 1.04x faster  |
| regex_dna                  | 118 ms   | 115 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 146 ms: 1.01x faster   |
| asyncio_websockets         | 311 ms   | 317 ms: 1.02x slower   |
| Geometric mean             | (ref)    | 1.51x faster           |

- Geometric mean (including insignificant results): 1.509x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.44x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown