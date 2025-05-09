# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 293 ms: 1.05x faster   |
| docutils       | 2.31 sec | 2.11 sec: 1.09x faster |
| html5lib       | 52.5 ms  | 51.3 ms: 1.02x faster  |
| sphinx         | 933 ms   | 843 ms: 1.11x faster   |
| Geometric mean | (ref)    | 1.07x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| async_generators           | 348 ms  | 321 ms: 1.08x faster  |
| async_tree_none            | 267 ms  | 248 ms: 1.08x faster  |
| asyncio_websockets         | 330 ms  | 311 ms: 1.06x faster  |
| async_tree_memoization     | 313 ms  | 297 ms: 1.05x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 434 ms: 1.05x faster  |
| async_tree_memoization_tg  | 304 ms  | 292 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 428 ms: 1.04x faster  |
| async_tree_none_tg         | 243 ms  | 236 ms: 1.03x faster  |
| async_tree_io              | 570 ms  | 551 ms: 1.03x faster  |
| async_tree_io_tg           | 576 ms  | 563 ms: 1.02x faster  |
| coroutines                 | 22.4 ms | 22.1 ms: 1.02x faster |
| Geometric mean             | (ref)   | 1.05x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 73.5 ms: 1.06x faster |
| pidigits       | 156 ms  | 148 ms: 1.05x faster  |
| nbody          | 103 ms  | 98.8 ms: 1.05x faster |
| Geometric mean | (ref)   | 1.05x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 123 ms: 1.06x faster  |
| regex_effbot   | 1.87 ms | 1.77 ms: 1.05x faster |
| regex_dna      | 123 ms  | 118 ms: 1.05x faster  |
| regex_v8       | 17.5 ms | 17.0 ms: 1.03x faster |
| Geometric mean | (ref)   | 1.05x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| json_loads           | 23.3 us  | 21.4 us: 1.09x faster  |
| xml_etree_iterparse  | 94.3 ms  | 87.5 ms: 1.08x faster  |
| xml_etree_process    | 66.9 ms  | 63.0 ms: 1.06x faster  |
| xml_etree_generate   | 92.6 ms  | 87.5 ms: 1.06x faster  |
| tomli_loads          | 2.07 sec | 1.97 sec: 1.05x faster |
| json_dumps           | 9.44 ms  | 8.99 ms: 1.05x faster  |
| unpickle_pure_python | 284 us   | 271 us: 1.05x faster   |
| xml_etree_parse      | 112 ms   | 108 ms: 1.04x faster   |
| pickle_pure_python   | 364 us   | 354 us: 1.03x faster   |
| Geometric mean       | (ref)    | 1.06x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TCO-Ex2               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 22.0 ms | 20.3 ms: 1.08x faster |
| python_startup         | 29.5 ms | 27.2 ms: 1.08x faster |
| Geometric mean         | (ref)   | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| django_template | 38.0 ms | 35.8 ms: 1.06x faster |
| mako            | 12.1 ms | 11.4 ms: 1.06x faster |
| genshi_xml      | 50.4 ms | 48.8 ms: 1.03x faster |
| genshi_text     | 23.9 ms | 23.4 ms: 1.02x faster |
| Geometric mean  | (ref)   | 1.04x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| pathlib                    | 37.5 ms  | 26.8 ms: 1.40x faster  |
| bench_thread_pool          | 1.28 ms  | 1.01 ms: 1.26x faster  |
| k_core                     | 2.18 sec | 1.83 sec: 1.19x faster |
| richards_super             | 67.7 ms  | 58.0 ms: 1.17x faster  |
| gc_traversal               | 3.25 ms  | 2.79 ms: 1.16x faster  |
| richards                   | 59.0 ms  | 51.0 ms: 1.16x faster  |
| shortest_path              | 437 ms   | 384 ms: 1.14x faster   |
| connected_components       | 395 ms   | 351 ms: 1.13x faster   |
| sphinx                     | 933 ms   | 843 ms: 1.11x faster   |
| sqlite_synth               | 1.96 us  | 1.78 us: 1.10x faster  |
| docutils                   | 2.31 sec | 2.11 sec: 1.09x faster |
| json_loads                 | 23.3 us  | 21.4 us: 1.09x faster  |
| logging_format             | 9.92 us  | 9.13 us: 1.09x faster  |
| fannkuch                   | 418 ms   | 386 ms: 1.08x faster   |
| async_generators           | 348 ms   | 321 ms: 1.08x faster   |
| python_startup_no_site     | 22.0 ms  | 20.3 ms: 1.08x faster  |
| python_startup             | 29.5 ms  | 27.2 ms: 1.08x faster  |
| pylint                     | 269 ms   | 249 ms: 1.08x faster   |
| xml_etree_iterparse        | 94.3 ms  | 87.5 ms: 1.08x faster  |
| logging_simple             | 9.30 us  | 8.63 us: 1.08x faster  |
| async_tree_none            | 267 ms   | 248 ms: 1.08x faster   |
| sqlglot_v2_optimize        | 52.8 ms  | 49.6 ms: 1.07x faster  |
| generators                 | 35.6 ms  | 33.5 ms: 1.06x faster  |
| xml_etree_process          | 66.9 ms  | 63.0 ms: 1.06x faster  |
| float                      | 78.0 ms  | 73.5 ms: 1.06x faster  |
| django_template            | 38.0 ms  | 35.8 ms: 1.06x faster  |
| asyncio_websockets         | 330 ms   | 311 ms: 1.06x faster   |
| deepcopy_reduce            | 2.86 us  | 2.71 us: 1.06x faster  |
| xml_etree_generate         | 92.6 ms  | 87.5 ms: 1.06x faster  |
| regex_compile              | 130 ms   | 123 ms: 1.06x faster   |
| mako                       | 12.1 ms  | 11.4 ms: 1.06x faster  |
| sqlglot_v2_normalize       | 109 ms   | 103 ms: 1.06x faster   |
| sympy_str                  | 247 ms   | 234 ms: 1.05x faster   |
| pidigits                   | 156 ms   | 148 ms: 1.05x faster   |
| 2to3                       | 309 ms   | 293 ms: 1.05x faster   |
| async_tree_memoization     | 313 ms   | 297 ms: 1.05x faster   |
| tomli_loads                | 2.07 sec | 1.97 sec: 1.05x faster |
| regex_effbot               | 1.87 ms  | 1.77 ms: 1.05x faster  |
| typing_runtime_protocols   | 154 us   | 146 us: 1.05x faster   |
| sympy_integrate            | 18.4 ms  | 17.5 ms: 1.05x faster  |
| json_dumps                 | 9.44 ms  | 8.99 ms: 1.05x faster  |
| sympy_sum                  | 123 ms   | 118 ms: 1.05x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 434 ms: 1.05x faster   |
| sympy_expand               | 419 ms   | 399 ms: 1.05x faster   |
| regex_dna                  | 123 ms   | 118 ms: 1.05x faster   |
| pycparser                  | 1.01 sec | 968 ms: 1.05x faster   |
| spectral_norm              | 102 ms   | 97.1 ms: 1.05x faster  |
| nbody                      | 103 ms   | 98.8 ms: 1.05x faster  |
| unpickle_pure_python       | 284 us   | 271 us: 1.05x faster   |
| meteor_contest             | 99.5 ms  | 95.0 ms: 1.05x faster  |
| pprint_safe_repr           | 825 ms   | 789 ms: 1.05x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 1.34 ms: 1.05x faster  |
| deepcopy                   | 278 us   | 266 us: 1.05x faster   |
| pyflate                    | 477 ms   | 457 ms: 1.04x faster   |
| thrift                     | 710 us   | 680 us: 1.04x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 1.62 ms: 1.04x faster  |
| async_tree_memoization_tg  | 304 ms   | 292 ms: 1.04x faster   |
| crypto_pyaes               | 80.1 ms  | 76.8 ms: 1.04x faster  |
| coverage                   | 63.7 ms  | 61.1 ms: 1.04x faster  |
| xml_etree_parse            | 112 ms   | 108 ms: 1.04x faster   |
| scimark_sor                | 139 ms   | 133 ms: 1.04x faster   |
| nqueens                    | 96.9 ms  | 93.2 ms: 1.04x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 4.27 ms: 1.04x faster  |
| dulwich_log                | 52.4 ms  | 50.5 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 428 ms: 1.04x faster   |
| mdp                        | 1.89 sec | 1.82 sec: 1.04x faster |
| bench_mp_pool              | 101 ms   | 97.6 ms: 1.04x faster  |
| comprehensions             | 20.1 us  | 19.4 us: 1.04x faster  |
| deltablue                  | 4.22 ms  | 4.08 ms: 1.04x faster  |
| json                       | 4.07 ms  | 3.94 ms: 1.03x faster  |
| chaos                      | 69.3 ms  | 67.0 ms: 1.03x faster  |
| telco                      | 6.56 ms  | 6.34 ms: 1.03x faster  |
| genshi_xml                 | 50.4 ms  | 48.8 ms: 1.03x faster  |
| async_tree_none_tg         | 243 ms   | 236 ms: 1.03x faster   |
| async_tree_io              | 570 ms   | 551 ms: 1.03x faster   |
| bpe_tokeniser              | 4.45 sec | 4.30 sec: 1.03x faster |
| regex_v8                   | 17.5 ms  | 17.0 ms: 1.03x faster  |
| scimark_fft                | 276 ms   | 267 ms: 1.03x faster   |
| scimark_lu                 | 119 ms   | 116 ms: 1.03x faster   |
| deepcopy_memo              | 34.0 us  | 33.0 us: 1.03x faster  |
| pickle_pure_python         | 364 us   | 354 us: 1.03x faster   |
| pprint_pformat             | 1.66 sec | 1.61 sec: 1.03x faster |
| html5lib                   | 52.5 ms  | 51.3 ms: 1.02x faster  |
| genshi_text                | 23.9 ms  | 23.4 ms: 1.02x faster  |
| hexiom                     | 7.44 ms  | 7.27 ms: 1.02x faster  |
| async_tree_io_tg           | 576 ms   | 563 ms: 1.02x faster   |
| logging_silent             | 124 ns   | 121 ns: 1.02x faster   |
| raytrace                   | 313 ms   | 306 ms: 1.02x faster   |
| go                         | 140 ms   | 138 ms: 1.02x faster   |
| coroutines                 | 22.4 ms  | 22.1 ms: 1.02x faster  |
| create_gc_cycles           | 1.42 ms  | 1.40 ms: 1.01x faster  |
| scimark_monte_carlo        | 75.8 ms  | 75.2 ms: 1.01x faster  |
| many_optionals             | 559 us   | 890 us: 1.59x slower   |
| subparsers                 | 21.5 ms  | 50.4 ms: 2.34x slower  |
| Geometric mean             | (ref)    | 1.04x faster           |

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown