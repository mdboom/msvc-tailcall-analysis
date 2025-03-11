# Results vs. base

- fork: unknown
- ref: NoTC-NoPGO-Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.039x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex          |
|----------------|:---------------:|:----------------------:|
| 2to3           | 298 ms          | 309 ms: 1.03x slower   |
| docutils       | 2.17 sec        | 2.31 sec: 1.06x slower |
| html5lib       | 51.3 ms         | 52.5 ms: 1.02x slower  |
| sphinx         | 872 ms          | 933 ms: 1.07x slower   |
| Geometric mean | (ref)           | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex         |
|----------------------------|:---------------:|:---------------------:|
| coroutines                 | 21.9 ms         | 22.4 ms: 1.02x slower |
| async_tree_none_tg         | 236 ms          | 243 ms: 1.03x slower  |
| async_tree_io              | 553 ms          | 570 ms: 1.03x slower  |
| async_tree_io_tg           | 559 ms          | 576 ms: 1.03x slower  |
| asyncio_websockets         | 317 ms          | 330 ms: 1.04x slower  |
| async_tree_cpu_io_mixed    | 437 ms          | 455 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 424 ms          | 444 ms: 1.05x slower  |
| async_tree_memoization_tg  | 291 ms          | 304 ms: 1.05x slower  |
| async_tree_memoization     | 297 ms          | 313 ms: 1.05x slower  |
| async_generators           | 328 ms          | 348 ms: 1.06x slower  |
| async_tree_none            | 249 ms          | 267 ms: 1.07x slower  |
| Geometric mean             | (ref)           | 1.04x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex         |
|----------------|:---------------:|:---------------------:|
| pidigits       | 152 ms          | 156 ms: 1.03x slower  |
| nbody          | 101 ms          | 103 ms: 1.03x slower  |
| float          | 75.4 ms         | 78.0 ms: 1.03x slower |
| Geometric mean | (ref)           | 1.03x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex         |
|----------------|:---------------:|:---------------------:|
| regex_dna      | 121 ms          | 123 ms: 1.02x slower  |
| regex_v8       | 17.1 ms         | 17.5 ms: 1.02x slower |
| regex_effbot   | 1.81 ms         | 1.87 ms: 1.03x slower |
| regex_compile  | 125 ms          | 130 ms: 1.04x slower  |
| Geometric mean | (ref)           | 1.03x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex          |
|----------------------|:---------------:|:----------------------:|
| pickle_pure_python   | 355 us          | 364 us: 1.03x slower   |
| xml_etree_generate   | 89.5 ms         | 92.6 ms: 1.03x slower  |
| xml_etree_process    | 64.6 ms         | 66.9 ms: 1.04x slower  |
| unpickle_pure_python | 274 us          | 284 us: 1.04x slower   |
| tomli_loads          | 1.99 sec        | 2.07 sec: 1.04x slower |
| xml_etree_parse      | 108 ms          | 112 ms: 1.04x slower   |
| json_loads           | 22.3 us         | 23.3 us: 1.04x slower  |
| json_dumps           | 9.01 ms         | 9.44 ms: 1.05x slower  |
| xml_etree_iterparse  | 89.9 ms         | 94.3 ms: 1.05x slower  |
| Geometric mean       | (ref)           | 1.04x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex         |
|------------------------|:---------------:|:---------------------:|
| python_startup         | 27.3 ms         | 29.5 ms: 1.08x slower |
| python_startup_no_site | 20.4 ms         | 22.0 ms: 1.08x slower |
| Geometric mean         | (ref)           | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex         |
|-----------------|:---------------:|:---------------------:|
| django_template | 36.9 ms         | 38.0 ms: 1.03x slower |
| mako            | 11.7 ms         | 12.1 ms: 1.03x slower |
| genshi_text     | 23.2 ms         | 23.9 ms: 1.03x slower |
| genshi_xml      | 48.8 ms         | 50.4 ms: 1.03x slower |
| Geometric mean  | (ref)           | 1.03x slower          |

All benchmarks:
===============

| Benchmark                  | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex          |
|----------------------------|:---------------:|:----------------------:|
| create_gc_cycles           | 1.40 ms         | 1.42 ms: 1.01x slower  |
| telco                      | 6.44 ms         | 6.56 ms: 1.02x slower  |
| regex_dna                  | 121 ms          | 123 ms: 1.02x slower   |
| scimark_sparse_mat_mult    | 4.34 ms         | 4.43 ms: 1.02x slower  |
| richards                   | 57.8 ms         | 59.0 ms: 1.02x slower  |
| many_optionals             | 547 us          | 559 us: 1.02x slower   |
| pycparser                  | 992 ms          | 1.01 sec: 1.02x slower |
| thrift                     | 694 us          | 710 us: 1.02x slower   |
| html5lib                   | 51.3 ms         | 52.5 ms: 1.02x slower  |
| hexiom                     | 7.27 ms         | 7.44 ms: 1.02x slower  |
| coroutines                 | 21.9 ms         | 22.4 ms: 1.02x slower  |
| regex_v8                   | 17.1 ms         | 17.5 ms: 1.02x slower  |
| typing_runtime_protocols   | 150 us          | 154 us: 1.02x slower   |
| scimark_monte_carlo        | 73.9 ms         | 75.8 ms: 1.03x slower  |
| go                         | 137 ms          | 140 ms: 1.03x slower   |
| fannkuch                   | 407 ms          | 418 ms: 1.03x slower   |
| dulwich_log                | 51.0 ms         | 52.4 ms: 1.03x slower  |
| scimark_sor                | 135 ms          | 139 ms: 1.03x slower   |
| pidigits                   | 152 ms          | 156 ms: 1.03x slower   |
| scimark_fft                | 269 ms          | 276 ms: 1.03x slower   |
| nqueens                    | 94.3 ms         | 96.9 ms: 1.03x slower  |
| sqlglot_v2_normalize       | 106 ms          | 109 ms: 1.03x slower   |
| pickle_pure_python         | 355 us          | 364 us: 1.03x slower   |
| regex_effbot               | 1.81 ms         | 1.87 ms: 1.03x slower  |
| crypto_pyaes               | 77.9 ms         | 80.1 ms: 1.03x slower  |
| scimark_lu                 | 116 ms          | 119 ms: 1.03x slower   |
| coverage                   | 61.9 ms         | 63.7 ms: 1.03x slower  |
| json                       | 3.96 ms         | 4.07 ms: 1.03x slower  |
| nbody                      | 101 ms          | 103 ms: 1.03x slower   |
| sqlglot_v2_transpile       | 1.64 ms         | 1.69 ms: 1.03x slower  |
| richards_super             | 65.8 ms         | 67.7 ms: 1.03x slower  |
| raytrace                   | 304 ms          | 313 ms: 1.03x slower   |
| django_template            | 36.9 ms         | 38.0 ms: 1.03x slower  |
| async_tree_none_tg         | 236 ms          | 243 ms: 1.03x slower   |
| pprint_pformat             | 1.61 sec        | 1.66 sec: 1.03x slower |
| async_tree_io              | 553 ms          | 570 ms: 1.03x slower   |
| async_tree_io_tg           | 559 ms          | 576 ms: 1.03x slower   |
| gc_traversal               | 3.15 ms         | 3.25 ms: 1.03x slower  |
| mako                       | 11.7 ms         | 12.1 ms: 1.03x slower  |
| deepcopy                   | 269 us          | 278 us: 1.03x slower   |
| genshi_text                | 23.2 ms         | 23.9 ms: 1.03x slower  |
| deltablue                  | 4.09 ms         | 4.22 ms: 1.03x slower  |
| bpe_tokeniser              | 4.30 sec        | 4.45 sec: 1.03x slower |
| genshi_xml                 | 48.8 ms         | 50.4 ms: 1.03x slower  |
| pyflate                    | 462 ms          | 477 ms: 1.03x slower   |
| deepcopy_reduce            | 2.77 us         | 2.86 us: 1.03x slower  |
| sympy_sum                  | 119 ms          | 123 ms: 1.03x slower   |
| float                      | 75.4 ms         | 78.0 ms: 1.03x slower  |
| deepcopy_memo              | 32.9 us         | 34.0 us: 1.03x slower  |
| sqlglot_v2_parse           | 1.36 ms         | 1.41 ms: 1.03x slower  |
| xml_etree_generate         | 89.5 ms         | 92.6 ms: 1.03x slower  |
| sympy_expand               | 405 ms          | 419 ms: 1.03x slower   |
| 2to3                       | 298 ms          | 309 ms: 1.03x slower   |
| sympy_integrate            | 17.8 ms         | 18.4 ms: 1.04x slower  |
| xml_etree_process          | 64.6 ms         | 66.9 ms: 1.04x slower  |
| subparsers                 | 20.8 ms         | 21.5 ms: 1.04x slower  |
| sqlglot_v2_optimize        | 51.0 ms         | 52.8 ms: 1.04x slower  |
| unpickle_pure_python       | 274 us          | 284 us: 1.04x slower   |
| meteor_contest             | 95.9 ms         | 99.5 ms: 1.04x slower  |
| sympy_str                  | 238 ms          | 247 ms: 1.04x slower   |
| comprehensions             | 19.4 us         | 20.1 us: 1.04x slower  |
| tomli_loads                | 1.99 sec        | 2.07 sec: 1.04x slower |
| asyncio_websockets         | 317 ms          | 330 ms: 1.04x slower   |
| logging_silent             | 119 ns          | 124 ns: 1.04x slower   |
| xml_etree_parse            | 108 ms          | 112 ms: 1.04x slower   |
| spectral_norm              | 97.7 ms         | 102 ms: 1.04x slower   |
| regex_compile              | 125 ms          | 130 ms: 1.04x slower   |
| mdp                        | 1.81 sec        | 1.89 sec: 1.04x slower |
| async_tree_cpu_io_mixed    | 437 ms          | 455 ms: 1.04x slower   |
| json_loads                 | 22.3 us         | 23.3 us: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 424 ms          | 444 ms: 1.05x slower   |
| async_tree_memoization_tg  | 291 ms          | 304 ms: 1.05x slower   |
| pprint_safe_repr           | 788 ms          | 825 ms: 1.05x slower   |
| json_dumps                 | 9.01 ms         | 9.44 ms: 1.05x slower  |
| logging_simple             | 8.87 us         | 9.30 us: 1.05x slower  |
| xml_etree_iterparse        | 89.9 ms         | 94.3 ms: 1.05x slower  |
| bench_mp_pool              | 96.2 ms         | 101 ms: 1.05x slower   |
| generators                 | 33.8 ms         | 35.6 ms: 1.05x slower  |
| async_tree_memoization     | 297 ms          | 313 ms: 1.05x slower   |
| async_generators           | 328 ms          | 348 ms: 1.06x slower   |
| sqlite_synth               | 1.84 us         | 1.96 us: 1.06x slower  |
| chaos                      | 65.2 ms         | 69.3 ms: 1.06x slower  |
| logging_format             | 9.33 us         | 9.92 us: 1.06x slower  |
| docutils                   | 2.17 sec        | 2.31 sec: 1.06x slower |
| pylint                     | 253 ms          | 269 ms: 1.06x slower   |
| sphinx                     | 872 ms          | 933 ms: 1.07x slower   |
| async_tree_none            | 249 ms          | 267 ms: 1.07x slower   |
| python_startup             | 27.3 ms         | 29.5 ms: 1.08x slower  |
| python_startup_no_site     | 20.4 ms         | 22.0 ms: 1.08x slower  |
| pathlib                    | 34.4 ms         | 37.5 ms: 1.09x slower  |
| connected_components       | 347 ms          | 395 ms: 1.14x slower   |
| shortest_path              | 378 ms          | 437 ms: 1.16x slower   |
| k_core                     | 1.83 sec        | 2.18 sec: 1.19x slower |
| bench_thread_pool          | 1.01 ms         | 1.28 ms: 1.27x slower  |
| Geometric mean             | (ref)           | 1.04x slower           |

- Geometric mean (including insignificant results): 1.039x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown