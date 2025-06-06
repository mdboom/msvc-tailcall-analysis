# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.031x faster
- HPT reliability: 71.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 251 ms: 1.23x faster   |
| docutils       | 2.31 sec | 2.61 sec: 1.13x slower |
| html5lib       | 52.5 ms  | 57.3 ms: 1.09x slower  |
| sphinx         | 933 ms   | 1.00 sec: 1.08x slower |
| Geometric mean | (ref)    | 1.02x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| async_tree_none            | 267 ms  | 249 ms: 1.07x faster  |
| async_tree_memoization     | 313 ms  | 306 ms: 1.02x faster  |
| coroutines                 | 22.4 ms | 22.1 ms: 1.02x faster |
| async_tree_io              | 570 ms  | 596 ms: 1.05x slower  |
| async_tree_io_tg           | 576 ms  | 606 ms: 1.05x slower  |
| async_generators           | 348 ms  | 368 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 455 ms  | 517 ms: 1.14x slower  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 504 ms: 1.14x slower  |
| asyncio_websockets         | 330 ms  | 551 ms: 1.67x slower  |
| Geometric mean             | (ref)   | 1.08x slower          |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 86.4 ms: 1.20x faster |
| float          | 78.0 ms | 66.8 ms: 1.17x faster |
| pidigits       | 156 ms  | 219 ms: 1.40x slower  |
| Geometric mean | (ref)   | 1.00x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 125 ms: 1.04x faster  |
| regex_v8       | 17.5 ms | 23.8 ms: 1.36x slower |
| regex_dna      | 123 ms  | 196 ms: 1.59x slower  |
| regex_effbot   | 1.87 ms | 3.28 ms: 1.76x slower |
| Geometric mean | (ref)   | 1.38x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 217 us: 1.31x faster   |
| pickle_pure_python   | 364 us   | 306 us: 1.19x faster   |
| xml_etree_process    | 66.9 ms  | 58.7 ms: 1.14x faster  |
| tomli_loads          | 2.07 sec | 1.88 sec: 1.10x faster |
| xml_etree_generate   | 92.6 ms  | 86.8 ms: 1.07x faster  |
| xml_etree_iterparse  | 94.3 ms  | 103 ms: 1.09x slower   |
| json_loads           | 23.3 us  | 28.9 us: 1.24x slower  |
| json_dumps           | 9.44 ms  | 12.5 ms: 1.32x slower  |
| xml_etree_parse      | 112 ms   | 163 ms: 1.45x slower   |
| Geometric mean       | (ref)    | 1.02x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 22.0 ms | 7.02 ms: 3.14x faster |
| python_startup         | 29.5 ms | 12.7 ms: 2.32x faster |
| Geometric mean         | (ref)   | 2.70x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| django_template | 38.0 ms | 30.6 ms: 1.24x faster |
| genshi_text     | 23.9 ms | 21.2 ms: 1.13x faster |
| genshi_xml      | 50.4 ms | 48.1 ms: 1.05x faster |
| mako            | 12.1 ms | 11.6 ms: 1.04x faster |
| Geometric mean  | (ref)   | 1.11x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 22.0 ms  | 7.02 ms: 3.14x faster  |
| pathlib                    | 37.5 ms  | 14.9 ms: 2.52x faster  |
| python_startup             | 29.5 ms  | 12.7 ms: 2.32x faster  |
| logging_simple             | 9.30 us  | 5.26 us: 1.77x faster  |
| logging_format             | 9.92 us  | 5.86 us: 1.69x faster  |
| bench_thread_pool          | 1.28 ms  | 831 us: 1.53x faster   |
| logging_silent             | 124 ns   | 87.1 ns: 1.43x faster  |
| deltablue                  | 4.22 ms  | 3.01 ms: 1.40x faster  |
| unpickle_pure_python       | 284 us   | 217 us: 1.31x faster   |
| scimark_sor                | 139 ms   | 107 ms: 1.30x faster   |
| chaos                      | 69.3 ms  | 53.3 ms: 1.30x faster  |
| hexiom                     | 7.44 ms  | 5.74 ms: 1.30x faster  |
| comprehensions             | 20.1 us  | 15.5 us: 1.29x faster  |
| nqueens                    | 96.9 ms  | 75.4 ms: 1.28x faster  |
| scimark_monte_carlo        | 75.8 ms  | 60.1 ms: 1.26x faster  |
| bench_mp_pool              | 101 ms   | 80.9 ms: 1.25x faster  |
| go                         | 140 ms   | 113 ms: 1.25x faster   |
| richards                   | 59.0 ms  | 47.4 ms: 1.25x faster  |
| generators                 | 35.6 ms  | 28.6 ms: 1.24x faster  |
| django_template            | 38.0 ms  | 30.6 ms: 1.24x faster  |
| spectral_norm              | 102 ms   | 82.5 ms: 1.23x faster  |
| 2to3                       | 309 ms   | 251 ms: 1.23x faster   |
| raytrace                   | 313 ms   | 255 ms: 1.23x faster   |
| richards_super             | 67.7 ms  | 55.6 ms: 1.22x faster  |
| nbody                      | 103 ms   | 86.4 ms: 1.20x faster  |
| pickle_pure_python         | 364 us   | 306 us: 1.19x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 1.20 ms: 1.18x faster  |
| float                      | 78.0 ms  | 66.8 ms: 1.17x faster  |
| pyflate                    | 477 ms   | 410 ms: 1.17x faster   |
| deepcopy_memo              | 34.0 us  | 29.4 us: 1.16x faster  |
| deepcopy                   | 278 us   | 244 us: 1.14x faster   |
| xml_etree_process          | 66.9 ms  | 58.7 ms: 1.14x faster  |
| deepcopy_reduce            | 2.86 us  | 2.53 us: 1.13x faster  |
| genshi_text                | 23.9 ms  | 21.2 ms: 1.13x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 1.50 ms: 1.13x faster  |
| pprint_safe_repr           | 825 ms   | 736 ms: 1.12x faster   |
| scimark_lu                 | 119 ms   | 107 ms: 1.12x faster   |
| crypto_pyaes               | 80.1 ms  | 72.5 ms: 1.10x faster  |
| tomli_loads                | 2.07 sec | 1.88 sec: 1.10x faster |
| pprint_pformat             | 1.66 sec | 1.51 sec: 1.10x faster |
| async_tree_none            | 267 ms   | 249 ms: 1.07x faster   |
| scimark_sparse_mat_mult    | 4.43 ms  | 4.14 ms: 1.07x faster  |
| subparsers                 | 21.5 ms  | 20.2 ms: 1.07x faster  |
| xml_etree_generate         | 92.6 ms  | 86.8 ms: 1.07x faster  |
| fannkuch                   | 418 ms   | 393 ms: 1.06x faster   |
| genshi_xml                 | 50.4 ms  | 48.1 ms: 1.05x faster  |
| sqlglot_v2_normalize       | 109 ms   | 104 ms: 1.04x faster   |
| typing_runtime_protocols   | 154 us   | 148 us: 1.04x faster   |
| mako                       | 12.1 ms  | 11.6 ms: 1.04x faster  |
| regex_compile              | 130 ms   | 125 ms: 1.04x faster   |
| async_tree_memoization     | 313 ms   | 306 ms: 1.02x faster   |
| coroutines                 | 22.4 ms  | 22.1 ms: 1.02x faster  |
| bpe_tokeniser              | 4.45 sec | 4.39 sec: 1.01x faster |
| sqlglot_v2_optimize        | 52.8 ms  | 52.2 ms: 1.01x faster  |
| sympy_integrate            | 18.4 ms  | 18.9 ms: 1.03x slower  |
| thrift                     | 710 us   | 737 us: 1.04x slower   |
| k_core                     | 2.18 sec | 2.27 sec: 1.04x slower |
| sympy_str                  | 247 ms   | 258 ms: 1.04x slower   |
| async_tree_io              | 570 ms   | 596 ms: 1.05x slower   |
| scimark_fft                | 276 ms   | 289 ms: 1.05x slower   |
| sympy_expand               | 419 ms   | 440 ms: 1.05x slower   |
| async_tree_io_tg           | 576 ms   | 606 ms: 1.05x slower   |
| async_generators           | 348 ms   | 368 ms: 1.06x slower   |
| sphinx                     | 933 ms   | 1.00 sec: 1.08x slower |
| xml_etree_iterparse        | 94.3 ms  | 103 ms: 1.09x slower   |
| html5lib                   | 52.5 ms  | 57.3 ms: 1.09x slower  |
| shortest_path              | 437 ms   | 480 ms: 1.10x slower   |
| meteor_contest             | 99.5 ms  | 111 ms: 1.11x slower   |
| telco                      | 6.56 ms  | 7.39 ms: 1.13x slower  |
| connected_components       | 395 ms   | 445 ms: 1.13x slower   |
| docutils                   | 2.31 sec | 2.61 sec: 1.13x slower |
| async_tree_cpu_io_mixed    | 455 ms   | 517 ms: 1.14x slower   |
| async_tree_cpu_io_mixed_tg | 444 ms   | 504 ms: 1.14x slower   |
| pycparser                  | 1.01 sec | 1.16 sec: 1.14x slower |
| sympy_sum                  | 123 ms   | 143 ms: 1.16x slower   |
| dulwich_log                | 52.4 ms  | 61.8 ms: 1.18x slower  |
| json_loads                 | 23.3 us  | 28.9 us: 1.24x slower  |
| coverage                   | 63.7 ms  | 79.6 ms: 1.25x slower  |
| json                       | 4.07 ms  | 5.28 ms: 1.30x slower  |
| json_dumps                 | 9.44 ms  | 12.5 ms: 1.32x slower  |
| sqlite_synth               | 1.96 us  | 2.66 us: 1.36x slower  |
| regex_v8                   | 17.5 ms  | 23.8 ms: 1.36x slower  |
| mdp                        | 1.89 sec | 2.65 sec: 1.40x slower |
| pidigits                   | 156 ms   | 219 ms: 1.40x slower   |
| xml_etree_parse            | 112 ms   | 163 ms: 1.45x slower   |
| gc_traversal               | 3.25 ms  | 4.97 ms: 1.53x slower  |
| regex_dna                  | 123 ms   | 196 ms: 1.59x slower   |
| many_optionals             | 559 us   | 924 us: 1.65x slower   |
| asyncio_websockets         | 330 ms   | 551 ms: 1.67x slower   |
| regex_effbot               | 1.87 ms  | 3.28 ms: 1.76x slower  |
| create_gc_cycles           | 1.42 ms  | 2.54 ms: 1.79x slower  |
| Geometric mean             | (ref)    | 1.04x faster           |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization_tg, pylint
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 71.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown