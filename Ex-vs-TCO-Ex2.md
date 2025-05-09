# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.040x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | Ex                     |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 309 ms: 1.05x slower   |
| docutils       | 2.11 sec | 2.31 sec: 1.09x slower |
| html5lib       | 51.3 ms  | 52.5 ms: 1.02x slower  |
| sphinx         | 843 ms   | 933 ms: 1.11x slower   |
| Geometric mean | (ref)    | 1.07x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | Ex                    |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 22.4 ms: 1.02x slower |
| async_tree_io_tg           | 563 ms  | 576 ms: 1.02x slower  |
| async_tree_io              | 551 ms  | 570 ms: 1.03x slower  |
| async_tree_none_tg         | 236 ms  | 243 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 444 ms: 1.04x slower  |
| async_tree_memoization_tg  | 292 ms  | 304 ms: 1.04x slower  |
| async_tree_cpu_io_mixed    | 434 ms  | 455 ms: 1.05x slower  |
| async_tree_memoization     | 297 ms  | 313 ms: 1.05x slower  |
| asyncio_websockets         | 311 ms  | 330 ms: 1.06x slower  |
| async_tree_none            | 248 ms  | 267 ms: 1.08x slower  |
| async_generators           | 321 ms  | 348 ms: 1.08x slower  |
| Geometric mean             | (ref)   | 1.05x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | Ex                    |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 103 ms: 1.05x slower  |
| pidigits       | 148 ms  | 156 ms: 1.05x slower  |
| float          | 73.5 ms | 78.0 ms: 1.06x slower |
| Geometric mean | (ref)   | 1.05x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | Ex                    |
|----------------|:-------:|:---------------------:|
| regex_v8       | 17.0 ms | 17.5 ms: 1.03x slower |
| regex_dna      | 118 ms  | 123 ms: 1.05x slower  |
| regex_effbot   | 1.77 ms | 1.87 ms: 1.05x slower |
| regex_compile  | 123 ms  | 130 ms: 1.06x slower  |
| Geometric mean | (ref)   | 1.05x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | Ex                     |
|----------------------|:--------:|:----------------------:|
| pickle_pure_python   | 354 us   | 364 us: 1.03x slower   |
| xml_etree_parse      | 108 ms   | 112 ms: 1.04x slower   |
| unpickle_pure_python | 271 us   | 284 us: 1.05x slower   |
| json_dumps           | 8.99 ms  | 9.44 ms: 1.05x slower  |
| tomli_loads          | 1.97 sec | 2.07 sec: 1.05x slower |
| xml_etree_generate   | 87.5 ms  | 92.6 ms: 1.06x slower  |
| xml_etree_process    | 63.0 ms  | 66.9 ms: 1.06x slower  |
| xml_etree_iterparse  | 87.5 ms  | 94.3 ms: 1.08x slower  |
| json_loads           | 21.4 us  | 23.3 us: 1.09x slower  |
| Geometric mean       | (ref)    | 1.06x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | Ex                    |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 29.5 ms: 1.08x slower |
| python_startup_no_site | 20.3 ms | 22.0 ms: 1.08x slower |
| Geometric mean         | (ref)   | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | Ex                    |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 23.4 ms | 23.9 ms: 1.02x slower |
| genshi_xml      | 48.8 ms | 50.4 ms: 1.03x slower |
| mako            | 11.4 ms | 12.1 ms: 1.06x slower |
| django_template | 35.8 ms | 38.0 ms: 1.06x slower |
| Geometric mean  | (ref)   | 1.04x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | Ex                     |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 50.4 ms  | 21.5 ms: 2.34x faster  |
| many_optionals             | 890 us   | 559 us: 1.59x faster   |
| scimark_monte_carlo        | 75.2 ms  | 75.8 ms: 1.01x slower  |
| create_gc_cycles           | 1.40 ms  | 1.42 ms: 1.01x slower  |
| coroutines                 | 22.1 ms  | 22.4 ms: 1.02x slower  |
| go                         | 138 ms   | 140 ms: 1.02x slower   |
| raytrace                   | 306 ms   | 313 ms: 1.02x slower   |
| logging_silent             | 121 ns   | 124 ns: 1.02x slower   |
| async_tree_io_tg           | 563 ms   | 576 ms: 1.02x slower   |
| hexiom                     | 7.27 ms  | 7.44 ms: 1.02x slower  |
| genshi_text                | 23.4 ms  | 23.9 ms: 1.02x slower  |
| html5lib                   | 51.3 ms  | 52.5 ms: 1.02x slower  |
| pprint_pformat             | 1.61 sec | 1.66 sec: 1.03x slower |
| pickle_pure_python         | 354 us   | 364 us: 1.03x slower   |
| deepcopy_memo              | 33.0 us  | 34.0 us: 1.03x slower  |
| scimark_lu                 | 116 ms   | 119 ms: 1.03x slower   |
| scimark_fft                | 267 ms   | 276 ms: 1.03x slower   |
| regex_v8                   | 17.0 ms  | 17.5 ms: 1.03x slower  |
| bpe_tokeniser              | 4.30 sec | 4.45 sec: 1.03x slower |
| async_tree_io              | 551 ms   | 570 ms: 1.03x slower   |
| async_tree_none_tg         | 236 ms   | 243 ms: 1.03x slower   |
| genshi_xml                 | 48.8 ms  | 50.4 ms: 1.03x slower  |
| telco                      | 6.34 ms  | 6.56 ms: 1.03x slower  |
| chaos                      | 67.0 ms  | 69.3 ms: 1.03x slower  |
| json                       | 3.94 ms  | 4.07 ms: 1.03x slower  |
| deltablue                  | 4.08 ms  | 4.22 ms: 1.04x slower  |
| comprehensions             | 19.4 us  | 20.1 us: 1.04x slower  |
| bench_mp_pool              | 97.6 ms  | 101 ms: 1.04x slower   |
| mdp                        | 1.82 sec | 1.89 sec: 1.04x slower |
| async_tree_cpu_io_mixed_tg | 428 ms   | 444 ms: 1.04x slower   |
| dulwich_log                | 50.5 ms  | 52.4 ms: 1.04x slower  |
| scimark_sparse_mat_mult    | 4.27 ms  | 4.43 ms: 1.04x slower  |
| nqueens                    | 93.2 ms  | 96.9 ms: 1.04x slower  |
| scimark_sor                | 133 ms   | 139 ms: 1.04x slower   |
| xml_etree_parse            | 108 ms   | 112 ms: 1.04x slower   |
| coverage                   | 61.1 ms  | 63.7 ms: 1.04x slower  |
| crypto_pyaes               | 76.8 ms  | 80.1 ms: 1.04x slower  |
| async_tree_memoization_tg  | 292 ms   | 304 ms: 1.04x slower   |
| sqlglot_v2_transpile       | 1.62 ms  | 1.69 ms: 1.04x slower  |
| thrift                     | 680 us   | 710 us: 1.04x slower   |
| pyflate                    | 457 ms   | 477 ms: 1.04x slower   |
| deepcopy                   | 266 us   | 278 us: 1.05x slower   |
| sqlglot_v2_parse           | 1.34 ms  | 1.41 ms: 1.05x slower  |
| pprint_safe_repr           | 789 ms   | 825 ms: 1.05x slower   |
| meteor_contest             | 95.0 ms  | 99.5 ms: 1.05x slower  |
| unpickle_pure_python       | 271 us   | 284 us: 1.05x slower   |
| nbody                      | 98.8 ms  | 103 ms: 1.05x slower   |
| spectral_norm              | 97.1 ms  | 102 ms: 1.05x slower   |
| pycparser                  | 968 ms   | 1.01 sec: 1.05x slower |
| regex_dna                  | 118 ms   | 123 ms: 1.05x slower   |
| sympy_expand               | 399 ms   | 419 ms: 1.05x slower   |
| async_tree_cpu_io_mixed    | 434 ms   | 455 ms: 1.05x slower   |
| sympy_sum                  | 118 ms   | 123 ms: 1.05x slower   |
| json_dumps                 | 8.99 ms  | 9.44 ms: 1.05x slower  |
| sympy_integrate            | 17.5 ms  | 18.4 ms: 1.05x slower  |
| typing_runtime_protocols   | 146 us   | 154 us: 1.05x slower   |
| regex_effbot               | 1.77 ms  | 1.87 ms: 1.05x slower  |
| tomli_loads                | 1.97 sec | 2.07 sec: 1.05x slower |
| async_tree_memoization     | 297 ms   | 313 ms: 1.05x slower   |
| 2to3                       | 293 ms   | 309 ms: 1.05x slower   |
| pidigits                   | 148 ms   | 156 ms: 1.05x slower   |
| sympy_str                  | 234 ms   | 247 ms: 1.05x slower   |
| sqlglot_v2_normalize       | 103 ms   | 109 ms: 1.06x slower   |
| mako                       | 11.4 ms  | 12.1 ms: 1.06x slower  |
| regex_compile              | 123 ms   | 130 ms: 1.06x slower   |
| xml_etree_generate         | 87.5 ms  | 92.6 ms: 1.06x slower  |
| deepcopy_reduce            | 2.71 us  | 2.86 us: 1.06x slower  |
| asyncio_websockets         | 311 ms   | 330 ms: 1.06x slower   |
| django_template            | 35.8 ms  | 38.0 ms: 1.06x slower  |
| float                      | 73.5 ms  | 78.0 ms: 1.06x slower  |
| xml_etree_process          | 63.0 ms  | 66.9 ms: 1.06x slower  |
| generators                 | 33.5 ms  | 35.6 ms: 1.06x slower  |
| sqlglot_v2_optimize        | 49.6 ms  | 52.8 ms: 1.07x slower  |
| async_tree_none            | 248 ms   | 267 ms: 1.08x slower   |
| logging_simple             | 8.63 us  | 9.30 us: 1.08x slower  |
| xml_etree_iterparse        | 87.5 ms  | 94.3 ms: 1.08x slower  |
| pylint                     | 249 ms   | 269 ms: 1.08x slower   |
| python_startup             | 27.2 ms  | 29.5 ms: 1.08x slower  |
| python_startup_no_site     | 20.3 ms  | 22.0 ms: 1.08x slower  |
| async_generators           | 321 ms   | 348 ms: 1.08x slower   |
| fannkuch                   | 386 ms   | 418 ms: 1.08x slower   |
| logging_format             | 9.13 us  | 9.92 us: 1.09x slower  |
| json_loads                 | 21.4 us  | 23.3 us: 1.09x slower  |
| docutils                   | 2.11 sec | 2.31 sec: 1.09x slower |
| sqlite_synth               | 1.78 us  | 1.96 us: 1.10x slower  |
| sphinx                     | 843 ms   | 933 ms: 1.11x slower   |
| connected_components       | 351 ms   | 395 ms: 1.13x slower   |
| shortest_path              | 384 ms   | 437 ms: 1.14x slower   |
| richards                   | 51.0 ms  | 59.0 ms: 1.16x slower  |
| gc_traversal               | 2.79 ms  | 3.25 ms: 1.16x slower  |
| richards_super             | 58.0 ms  | 67.7 ms: 1.17x slower  |
| k_core                     | 1.83 sec | 2.18 sec: 1.19x slower |
| bench_thread_pool          | 1.01 ms  | 1.28 ms: 1.26x slower  |
| pathlib                    | 26.8 ms  | 37.5 ms: 1.40x slower  |
| Geometric mean             | (ref)    | 1.04x slower           |

- Geometric mean (including insignificant results): 1.040x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown