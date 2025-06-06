# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.011x slower
- HPT reliability: 96.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 251 ms: 1.17x faster   |
| docutils       | 2.11 sec | 2.61 sec: 1.24x slower |
| html5lib       | 51.3 ms  | 57.3 ms: 1.12x slower  |
| sphinx         | 843 ms   | 1.00 sec: 1.19x slower |
| Geometric mean | (ref)    | 1.09x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TC-PGO-Ex3           |
|----------------------------|:-------:|:--------------------:|
| async_tree_none_tg         | 236 ms  | 242 ms: 1.03x slower |
| async_tree_memoization     | 297 ms  | 306 ms: 1.03x slower |
| async_tree_memoization_tg  | 292 ms  | 307 ms: 1.05x slower |
| async_tree_io_tg           | 563 ms  | 606 ms: 1.08x slower |
| async_tree_io              | 551 ms  | 596 ms: 1.08x slower |
| async_generators           | 321 ms  | 368 ms: 1.15x slower |
| async_tree_cpu_io_mixed_tg | 428 ms  | 504 ms: 1.18x slower |
| async_tree_cpu_io_mixed    | 434 ms  | 517 ms: 1.19x slower |
| asyncio_websockets         | 311 ms  | 551 ms: 1.77x slower |
| Geometric mean             | (ref)   | 1.13x slower         |

Benchmark hidden because not significant (2): coroutines, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 86.4 ms: 1.14x faster |
| float          | 73.5 ms | 66.8 ms: 1.10x faster |
| pidigits       | 148 ms  | 219 ms: 1.48x slower  |
| Geometric mean | (ref)   | 1.06x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 125 ms: 1.02x slower  |
| regex_v8       | 17.0 ms | 23.8 ms: 1.40x slower |
| regex_dna      | 118 ms  | 196 ms: 1.67x slower  |
| regex_effbot   | 1.77 ms | 3.28 ms: 1.85x slower |
| Geometric mean | (ref)   | 1.45x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 217 us: 1.25x faster   |
| pickle_pure_python   | 354 us   | 306 us: 1.16x faster   |
| xml_etree_process    | 63.0 ms  | 58.7 ms: 1.07x faster  |
| tomli_loads          | 1.97 sec | 1.88 sec: 1.05x faster |
| xml_etree_generate   | 87.5 ms  | 86.8 ms: 1.01x faster  |
| xml_etree_iterparse  | 87.5 ms  | 103 ms: 1.17x slower   |
| json_loads           | 21.4 us  | 28.9 us: 1.35x slower  |
| json_dumps           | 8.99 ms  | 12.5 ms: 1.38x slower  |
| xml_etree_parse      | 108 ms   | 163 ms: 1.51x slower   |
| Geometric mean       | (ref)    | 1.08x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.3 ms | 7.02 ms: 2.90x faster |
| python_startup         | 27.2 ms | 12.7 ms: 2.14x faster |
| Geometric mean         | (ref)   | 2.49x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| django_template | 35.8 ms | 30.6 ms: 1.17x faster |
| genshi_text     | 23.4 ms | 21.2 ms: 1.10x faster |
| genshi_xml      | 48.8 ms | 48.1 ms: 1.01x faster |
| mako            | 11.4 ms | 11.6 ms: 1.01x slower |
| Geometric mean  | (ref)   | 1.07x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 20.3 ms  | 7.02 ms: 2.90x faster  |
| subparsers                 | 50.4 ms  | 20.2 ms: 2.50x faster  |
| python_startup             | 27.2 ms  | 12.7 ms: 2.14x faster  |
| pathlib                    | 26.8 ms  | 14.9 ms: 1.80x faster  |
| logging_simple             | 8.63 us  | 5.26 us: 1.64x faster  |
| logging_format             | 9.13 us  | 5.86 us: 1.56x faster  |
| logging_silent             | 121 ns   | 87.1 ns: 1.40x faster  |
| deltablue                  | 4.08 ms  | 3.01 ms: 1.35x faster  |
| hexiom                     | 7.27 ms  | 5.74 ms: 1.27x faster  |
| chaos                      | 67.0 ms  | 53.3 ms: 1.26x faster  |
| scimark_sor                | 133 ms   | 107 ms: 1.25x faster   |
| unpickle_pure_python       | 271 us   | 217 us: 1.25x faster   |
| scimark_monte_carlo        | 75.2 ms  | 60.1 ms: 1.25x faster  |
| comprehensions             | 19.4 us  | 15.5 us: 1.25x faster  |
| nqueens                    | 93.2 ms  | 75.4 ms: 1.24x faster  |
| go                         | 138 ms   | 113 ms: 1.23x faster   |
| bench_thread_pool          | 1.01 ms  | 831 us: 1.22x faster   |
| bench_mp_pool              | 97.6 ms  | 80.9 ms: 1.21x faster  |
| raytrace                   | 306 ms   | 255 ms: 1.20x faster   |
| spectral_norm              | 97.1 ms  | 82.5 ms: 1.18x faster  |
| django_template            | 35.8 ms  | 30.6 ms: 1.17x faster  |
| generators                 | 33.5 ms  | 28.6 ms: 1.17x faster  |
| 2to3                       | 293 ms   | 251 ms: 1.17x faster   |
| pickle_pure_python         | 354 us   | 306 us: 1.16x faster   |
| nbody                      | 98.8 ms  | 86.4 ms: 1.14x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 1.20 ms: 1.12x faster  |
| deepcopy_memo              | 33.0 us  | 29.4 us: 1.12x faster  |
| pyflate                    | 457 ms   | 410 ms: 1.12x faster   |
| genshi_text                | 23.4 ms  | 21.2 ms: 1.10x faster  |
| float                      | 73.5 ms  | 66.8 ms: 1.10x faster  |
| deepcopy                   | 266 us   | 244 us: 1.09x faster   |
| scimark_lu                 | 116 ms   | 107 ms: 1.08x faster   |
| sqlglot_v2_transpile       | 1.62 ms  | 1.50 ms: 1.08x faster  |
| richards                   | 51.0 ms  | 47.4 ms: 1.08x faster  |
| pprint_safe_repr           | 789 ms   | 736 ms: 1.07x faster   |
| xml_etree_process          | 63.0 ms  | 58.7 ms: 1.07x faster  |
| pprint_pformat             | 1.61 sec | 1.51 sec: 1.07x faster |
| deepcopy_reduce            | 2.71 us  | 2.53 us: 1.07x faster  |
| crypto_pyaes               | 76.8 ms  | 72.5 ms: 1.06x faster  |
| tomli_loads                | 1.97 sec | 1.88 sec: 1.05x faster |
| richards_super             | 58.0 ms  | 55.6 ms: 1.04x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 4.14 ms: 1.03x faster  |
| genshi_xml                 | 48.8 ms  | 48.1 ms: 1.01x faster  |
| xml_etree_generate         | 87.5 ms  | 86.8 ms: 1.01x faster  |
| typing_runtime_protocols   | 146 us   | 148 us: 1.01x slower   |
| sqlglot_v2_normalize       | 103 ms   | 104 ms: 1.01x slower   |
| mako                       | 11.4 ms  | 11.6 ms: 1.01x slower  |
| regex_compile              | 123 ms   | 125 ms: 1.02x slower   |
| bpe_tokeniser              | 4.30 sec | 4.39 sec: 1.02x slower |
| fannkuch                   | 386 ms   | 393 ms: 1.02x slower   |
| async_tree_none_tg         | 236 ms   | 242 ms: 1.03x slower   |
| async_tree_memoization     | 297 ms   | 306 ms: 1.03x slower   |
| many_optionals             | 890 us   | 924 us: 1.04x slower   |
| sqlglot_v2_optimize        | 49.6 ms  | 52.2 ms: 1.05x slower  |
| async_tree_memoization_tg  | 292 ms   | 307 ms: 1.05x slower   |
| async_tree_io_tg           | 563 ms   | 606 ms: 1.08x slower   |
| sympy_integrate            | 17.5 ms  | 18.9 ms: 1.08x slower  |
| async_tree_io              | 551 ms   | 596 ms: 1.08x slower   |
| scimark_fft                | 267 ms   | 289 ms: 1.08x slower   |
| thrift                     | 680 us   | 737 us: 1.08x slower   |
| sympy_expand               | 399 ms   | 440 ms: 1.10x slower   |
| sympy_str                  | 234 ms   | 258 ms: 1.10x slower   |
| pylint                     | 249 ms   | 275 ms: 1.11x slower   |
| html5lib                   | 51.3 ms  | 57.3 ms: 1.12x slower  |
| async_generators           | 321 ms   | 368 ms: 1.15x slower   |
| meteor_contest             | 95.0 ms  | 111 ms: 1.16x slower   |
| telco                      | 6.34 ms  | 7.39 ms: 1.17x slower  |
| xml_etree_iterparse        | 87.5 ms  | 103 ms: 1.17x slower   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 504 ms: 1.18x slower   |
| sphinx                     | 843 ms   | 1.00 sec: 1.19x slower |
| async_tree_cpu_io_mixed    | 434 ms   | 517 ms: 1.19x slower   |
| pycparser                  | 968 ms   | 1.16 sec: 1.19x slower |
| sympy_sum                  | 118 ms   | 143 ms: 1.21x slower   |
| dulwich_log                | 50.5 ms  | 61.8 ms: 1.22x slower  |
| docutils                   | 2.11 sec | 2.61 sec: 1.24x slower |
| k_core                     | 1.83 sec | 2.27 sec: 1.24x slower |
| shortest_path              | 384 ms   | 480 ms: 1.25x slower   |
| connected_components       | 351 ms   | 445 ms: 1.27x slower   |
| coverage                   | 61.1 ms  | 79.6 ms: 1.30x slower  |
| json                       | 3.94 ms  | 5.28 ms: 1.34x slower  |
| json_loads                 | 21.4 us  | 28.9 us: 1.35x slower  |
| json_dumps                 | 8.99 ms  | 12.5 ms: 1.38x slower  |
| regex_v8                   | 17.0 ms  | 23.8 ms: 1.40x slower  |
| mdp                        | 1.82 sec | 2.65 sec: 1.45x slower |
| pidigits                   | 148 ms   | 219 ms: 1.48x slower   |
| sqlite_synth               | 1.78 us  | 2.66 us: 1.49x slower  |
| xml_etree_parse            | 108 ms   | 163 ms: 1.51x slower   |
| regex_dna                  | 118 ms   | 196 ms: 1.67x slower   |
| asyncio_websockets         | 311 ms   | 551 ms: 1.77x slower   |
| gc_traversal               | 2.79 ms  | 4.97 ms: 1.78x slower  |
| create_gc_cycles           | 1.40 ms  | 2.54 ms: 1.81x slower  |
| regex_effbot               | 1.77 ms  | 3.28 ms: 1.85x slower  |
| Geometric mean             | (ref)    | 1.00x slower           |

Benchmark hidden because not significant (2): coroutines, async_tree_none
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 96.44% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown