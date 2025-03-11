# Results vs. base

- fork: unknown
- ref: NoTC-NoPGO-NoEx
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------|:-------------:|:----------------------:|
| 2to3           | 309 ms        | 298 ms: 1.03x faster   |
| docutils       | 2.31 sec      | 2.17 sec: 1.06x faster |
| html5lib       | 52.5 ms       | 51.3 ms: 1.02x faster  |
| sphinx         | 933 ms        | 872 ms: 1.07x faster   |
| Geometric mean | (ref)         | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------------------|:-------------:|:---------------------:|
| async_tree_none            | 267 ms        | 249 ms: 1.07x faster  |
| async_generators           | 348 ms        | 328 ms: 1.06x faster  |
| async_tree_memoization     | 313 ms        | 297 ms: 1.05x faster  |
| async_tree_memoization_tg  | 304 ms        | 291 ms: 1.05x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms        | 424 ms: 1.05x faster  |
| async_tree_cpu_io_mixed    | 455 ms        | 437 ms: 1.04x faster  |
| asyncio_websockets         | 330 ms        | 317 ms: 1.04x faster  |
| async_tree_io_tg           | 576 ms        | 559 ms: 1.03x faster  |
| async_tree_io              | 570 ms        | 553 ms: 1.03x faster  |
| async_tree_none_tg         | 243 ms        | 236 ms: 1.03x faster  |
| coroutines                 | 22.4 ms       | 21.9 ms: 1.02x faster |
| Geometric mean             | (ref)         | 1.04x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------|:-------------:|:---------------------:|
| float          | 78.0 ms       | 75.4 ms: 1.03x faster |
| nbody          | 103 ms        | 101 ms: 1.03x faster  |
| pidigits       | 156 ms        | 152 ms: 1.03x faster  |
| Geometric mean | (ref)         | 1.03x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------|:-------------:|:---------------------:|
| regex_compile  | 130 ms        | 125 ms: 1.04x faster  |
| regex_effbot   | 1.87 ms       | 1.81 ms: 1.03x faster |
| regex_v8       | 17.5 ms       | 17.1 ms: 1.02x faster |
| regex_dna      | 123 ms        | 121 ms: 1.02x faster  |
| Geometric mean | (ref)         | 1.03x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------------|:-------------:|:----------------------:|
| xml_etree_iterparse  | 94.3 ms       | 89.9 ms: 1.05x faster  |
| json_dumps           | 9.44 ms       | 9.01 ms: 1.05x faster  |
| json_loads           | 23.3 us       | 22.3 us: 1.04x faster  |
| xml_etree_parse      | 112 ms        | 108 ms: 1.04x faster   |
| tomli_loads          | 2.07 sec      | 1.99 sec: 1.04x faster |
| unpickle_pure_python | 284 us        | 274 us: 1.04x faster   |
| xml_etree_process    | 66.9 ms       | 64.6 ms: 1.04x faster  |
| xml_etree_generate   | 92.6 ms       | 89.5 ms: 1.03x faster  |
| pickle_pure_python   | 364 us        | 355 us: 1.03x faster   |
| Geometric mean       | (ref)         | 1.04x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 22.0 ms       | 20.4 ms: 1.08x faster |
| python_startup         | 29.5 ms       | 27.3 ms: 1.08x faster |
| Geometric mean         | (ref)         | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|-----------------|:-------------:|:---------------------:|
| genshi_xml      | 50.4 ms       | 48.8 ms: 1.03x faster |
| genshi_text     | 23.9 ms       | 23.2 ms: 1.03x faster |
| mako            | 12.1 ms       | 11.7 ms: 1.03x faster |
| django_template | 38.0 ms       | 36.9 ms: 1.03x faster |
| Geometric mean  | (ref)         | 1.03x faster          |

All benchmarks:
===============

| Benchmark                  | NoTC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------------------|:-------------:|:----------------------:|
| bench_thread_pool          | 1.28 ms       | 1.01 ms: 1.27x faster  |
| k_core                     | 2.18 sec      | 1.83 sec: 1.19x faster |
| shortest_path              | 437 ms        | 378 ms: 1.16x faster   |
| connected_components       | 395 ms        | 347 ms: 1.14x faster   |
| pathlib                    | 37.5 ms       | 34.4 ms: 1.09x faster  |
| python_startup_no_site     | 22.0 ms       | 20.4 ms: 1.08x faster  |
| python_startup             | 29.5 ms       | 27.3 ms: 1.08x faster  |
| async_tree_none            | 267 ms        | 249 ms: 1.07x faster   |
| sphinx                     | 933 ms        | 872 ms: 1.07x faster   |
| pylint                     | 269 ms        | 253 ms: 1.06x faster   |
| docutils                   | 2.31 sec      | 2.17 sec: 1.06x faster |
| logging_format             | 9.92 us       | 9.33 us: 1.06x faster  |
| chaos                      | 69.3 ms       | 65.2 ms: 1.06x faster  |
| sqlite_synth               | 1.96 us       | 1.84 us: 1.06x faster  |
| async_generators           | 348 ms        | 328 ms: 1.06x faster   |
| async_tree_memoization     | 313 ms        | 297 ms: 1.05x faster   |
| generators                 | 35.6 ms       | 33.8 ms: 1.05x faster  |
| bench_mp_pool              | 101 ms        | 96.2 ms: 1.05x faster  |
| xml_etree_iterparse        | 94.3 ms       | 89.9 ms: 1.05x faster  |
| logging_simple             | 9.30 us       | 8.87 us: 1.05x faster  |
| json_dumps                 | 9.44 ms       | 9.01 ms: 1.05x faster  |
| pprint_safe_repr           | 825 ms        | 788 ms: 1.05x faster   |
| async_tree_memoization_tg  | 304 ms        | 291 ms: 1.05x faster   |
| async_tree_cpu_io_mixed_tg | 444 ms        | 424 ms: 1.05x faster   |
| json_loads                 | 23.3 us       | 22.3 us: 1.04x faster  |
| async_tree_cpu_io_mixed    | 455 ms        | 437 ms: 1.04x faster   |
| mdp                        | 1.89 sec      | 1.81 sec: 1.04x faster |
| regex_compile              | 130 ms        | 125 ms: 1.04x faster   |
| spectral_norm              | 102 ms        | 97.7 ms: 1.04x faster  |
| xml_etree_parse            | 112 ms        | 108 ms: 1.04x faster   |
| logging_silent             | 124 ns        | 119 ns: 1.04x faster   |
| asyncio_websockets         | 330 ms        | 317 ms: 1.04x faster   |
| tomli_loads                | 2.07 sec      | 1.99 sec: 1.04x faster |
| comprehensions             | 20.1 us       | 19.4 us: 1.04x faster  |
| sympy_str                  | 247 ms        | 238 ms: 1.04x faster   |
| meteor_contest             | 99.5 ms       | 95.9 ms: 1.04x faster  |
| unpickle_pure_python       | 284 us        | 274 us: 1.04x faster   |
| sqlglot_v2_optimize        | 52.8 ms       | 51.0 ms: 1.04x faster  |
| subparsers                 | 21.5 ms       | 20.8 ms: 1.04x faster  |
| xml_etree_process          | 66.9 ms       | 64.6 ms: 1.04x faster  |
| sympy_integrate            | 18.4 ms       | 17.8 ms: 1.04x faster  |
| 2to3                       | 309 ms        | 298 ms: 1.03x faster   |
| sympy_expand               | 419 ms        | 405 ms: 1.03x faster   |
| xml_etree_generate         | 92.6 ms       | 89.5 ms: 1.03x faster  |
| sqlglot_v2_parse           | 1.41 ms       | 1.36 ms: 1.03x faster  |
| deepcopy_memo              | 34.0 us       | 32.9 us: 1.03x faster  |
| float                      | 78.0 ms       | 75.4 ms: 1.03x faster  |
| sympy_sum                  | 123 ms        | 119 ms: 1.03x faster   |
| deepcopy_reduce            | 2.86 us       | 2.77 us: 1.03x faster  |
| pyflate                    | 477 ms        | 462 ms: 1.03x faster   |
| genshi_xml                 | 50.4 ms       | 48.8 ms: 1.03x faster  |
| bpe_tokeniser              | 4.45 sec      | 4.30 sec: 1.03x faster |
| deltablue                  | 4.22 ms       | 4.09 ms: 1.03x faster  |
| genshi_text                | 23.9 ms       | 23.2 ms: 1.03x faster  |
| deepcopy                   | 278 us        | 269 us: 1.03x faster   |
| mako                       | 12.1 ms       | 11.7 ms: 1.03x faster  |
| gc_traversal               | 3.25 ms       | 3.15 ms: 1.03x faster  |
| async_tree_io_tg           | 576 ms        | 559 ms: 1.03x faster   |
| async_tree_io              | 570 ms        | 553 ms: 1.03x faster   |
| pprint_pformat             | 1.66 sec      | 1.61 sec: 1.03x faster |
| async_tree_none_tg         | 243 ms        | 236 ms: 1.03x faster   |
| django_template            | 38.0 ms       | 36.9 ms: 1.03x faster  |
| raytrace                   | 313 ms        | 304 ms: 1.03x faster   |
| richards_super             | 67.7 ms       | 65.8 ms: 1.03x faster  |
| sqlglot_v2_transpile       | 1.69 ms       | 1.64 ms: 1.03x faster  |
| nbody                      | 103 ms        | 101 ms: 1.03x faster   |
| json                       | 4.07 ms       | 3.96 ms: 1.03x faster  |
| coverage                   | 63.7 ms       | 61.9 ms: 1.03x faster  |
| scimark_lu                 | 119 ms        | 116 ms: 1.03x faster   |
| crypto_pyaes               | 80.1 ms       | 77.9 ms: 1.03x faster  |
| regex_effbot               | 1.87 ms       | 1.81 ms: 1.03x faster  |
| pickle_pure_python         | 364 us        | 355 us: 1.03x faster   |
| sqlglot_v2_normalize       | 109 ms        | 106 ms: 1.03x faster   |
| nqueens                    | 96.9 ms       | 94.3 ms: 1.03x faster  |
| scimark_fft                | 276 ms        | 269 ms: 1.03x faster   |
| pidigits                   | 156 ms        | 152 ms: 1.03x faster   |
| scimark_sor                | 139 ms        | 135 ms: 1.03x faster   |
| dulwich_log                | 52.4 ms       | 51.0 ms: 1.03x faster  |
| fannkuch                   | 418 ms        | 407 ms: 1.03x faster   |
| go                         | 140 ms        | 137 ms: 1.03x faster   |
| scimark_monte_carlo        | 75.8 ms       | 73.9 ms: 1.03x faster  |
| typing_runtime_protocols   | 154 us        | 150 us: 1.02x faster   |
| regex_v8                   | 17.5 ms       | 17.1 ms: 1.02x faster  |
| coroutines                 | 22.4 ms       | 21.9 ms: 1.02x faster  |
| hexiom                     | 7.44 ms       | 7.27 ms: 1.02x faster  |
| html5lib                   | 52.5 ms       | 51.3 ms: 1.02x faster  |
| thrift                     | 710 us        | 694 us: 1.02x faster   |
| pycparser                  | 1.01 sec      | 992 ms: 1.02x faster   |
| many_optionals             | 559 us        | 547 us: 1.02x faster   |
| richards                   | 59.0 ms       | 57.8 ms: 1.02x faster  |
| scimark_sparse_mat_mult    | 4.43 ms       | 4.34 ms: 1.02x faster  |
| regex_dna                  | 123 ms        | 121 ms: 1.02x faster   |
| telco                      | 6.56 ms       | 6.44 ms: 1.02x faster  |
| create_gc_cycles           | 1.42 ms       | 1.40 ms: 1.01x faster  |
| Geometric mean             | (ref)         | 1.04x faster           |

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown