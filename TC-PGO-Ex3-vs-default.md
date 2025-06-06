# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.009x slower
- HPT reliability: 91.34%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 251 ms: 1.19x faster   |
| docutils       | 2.17 sec | 2.61 sec: 1.20x slower |
| html5lib       | 51.3 ms  | 57.3 ms: 1.12x slower  |
| sphinx         | 872 ms   | 1.00 sec: 1.15x slower |
| Geometric mean | (ref)    | 1.07x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 22.1 ms: 1.01x slower |
| async_tree_none_tg         | 236 ms  | 242 ms: 1.02x slower  |
| async_tree_memoization     | 297 ms  | 306 ms: 1.03x slower  |
| async_tree_memoization_tg  | 291 ms  | 307 ms: 1.06x slower  |
| async_tree_io              | 553 ms  | 596 ms: 1.08x slower  |
| async_tree_io_tg           | 559 ms  | 606 ms: 1.08x slower  |
| async_generators           | 328 ms  | 368 ms: 1.12x slower  |
| async_tree_cpu_io_mixed    | 437 ms  | 517 ms: 1.18x slower  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 504 ms: 1.19x slower  |
| asyncio_websockets         | 317 ms  | 551 ms: 1.74x slower  |
| Geometric mean             | (ref)   | 1.12x slower          |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 86.4 ms: 1.16x faster |
| float          | 75.4 ms | 66.8 ms: 1.13x faster |
| pidigits       | 152 ms  | 219 ms: 1.44x slower  |
| Geometric mean | (ref)   | 1.03x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_v8       | 17.1 ms | 23.8 ms: 1.39x slower |
| regex_dna      | 121 ms  | 196 ms: 1.62x slower  |
| regex_effbot   | 1.81 ms | 3.28 ms: 1.81x slower |
| Geometric mean | (ref)   | 1.42x slower          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 217 us: 1.26x faster   |
| pickle_pure_python   | 355 us   | 306 us: 1.16x faster   |
| xml_etree_process    | 64.6 ms  | 58.7 ms: 1.10x faster  |
| tomli_loads          | 1.99 sec | 1.88 sec: 1.06x faster |
| xml_etree_generate   | 89.5 ms  | 86.8 ms: 1.03x faster  |
| xml_etree_iterparse  | 89.9 ms  | 103 ms: 1.14x slower   |
| json_loads           | 22.3 us  | 28.9 us: 1.29x slower  |
| json_dumps           | 9.01 ms  | 12.5 ms: 1.38x slower  |
| xml_etree_parse      | 108 ms   | 163 ms: 1.51x slower   |
| Geometric mean       | (ref)    | 1.06x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.4 ms | 7.02 ms: 2.90x faster |
| python_startup         | 27.3 ms | 12.7 ms: 2.15x faster |
| Geometric mean         | (ref)   | 2.50x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| django_template | 36.9 ms | 30.6 ms: 1.21x faster |
| genshi_text     | 23.2 ms | 21.2 ms: 1.09x faster |
| genshi_xml      | 48.8 ms | 48.1 ms: 1.01x faster |
| mako            | 11.7 ms | 11.6 ms: 1.01x faster |
| Geometric mean  | (ref)   | 1.08x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 20.4 ms  | 7.02 ms: 2.90x faster  |
| pathlib                    | 34.4 ms  | 14.9 ms: 2.31x faster  |
| python_startup             | 27.3 ms  | 12.7 ms: 2.15x faster  |
| logging_simple             | 8.87 us  | 5.26 us: 1.69x faster  |
| logging_format             | 9.33 us  | 5.86 us: 1.59x faster  |
| logging_silent             | 119 ns   | 87.1 ns: 1.37x faster  |
| deltablue                  | 4.09 ms  | 3.01 ms: 1.36x faster  |
| scimark_sor                | 135 ms   | 107 ms: 1.27x faster   |
| hexiom                     | 7.27 ms  | 5.74 ms: 1.27x faster  |
| unpickle_pure_python       | 274 us   | 217 us: 1.26x faster   |
| nqueens                    | 94.3 ms  | 75.4 ms: 1.25x faster  |
| comprehensions             | 19.4 us  | 15.5 us: 1.25x faster  |
| scimark_monte_carlo        | 73.9 ms  | 60.1 ms: 1.23x faster  |
| chaos                      | 65.2 ms  | 53.3 ms: 1.22x faster  |
| richards                   | 57.8 ms  | 47.4 ms: 1.22x faster  |
| go                         | 137 ms   | 113 ms: 1.22x faster   |
| bench_thread_pool          | 1.01 ms  | 831 us: 1.21x faster   |
| django_template            | 36.9 ms  | 30.6 ms: 1.21x faster  |
| raytrace                   | 304 ms   | 255 ms: 1.19x faster   |
| bench_mp_pool              | 96.2 ms  | 80.9 ms: 1.19x faster  |
| 2to3                       | 298 ms   | 251 ms: 1.19x faster   |
| spectral_norm              | 97.7 ms  | 82.5 ms: 1.18x faster  |
| generators                 | 33.8 ms  | 28.6 ms: 1.18x faster  |
| richards_super             | 65.8 ms  | 55.6 ms: 1.18x faster  |
| nbody                      | 101 ms   | 86.4 ms: 1.16x faster  |
| pickle_pure_python         | 355 us   | 306 us: 1.16x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 1.20 ms: 1.14x faster  |
| float                      | 75.4 ms  | 66.8 ms: 1.13x faster  |
| pyflate                    | 462 ms   | 410 ms: 1.13x faster   |
| deepcopy_memo              | 32.9 us  | 29.4 us: 1.12x faster  |
| deepcopy                   | 269 us   | 244 us: 1.10x faster   |
| xml_etree_process          | 64.6 ms  | 58.7 ms: 1.10x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 1.50 ms: 1.09x faster  |
| deepcopy_reduce            | 2.77 us  | 2.53 us: 1.09x faster  |
| genshi_text                | 23.2 ms  | 21.2 ms: 1.09x faster  |
| scimark_lu                 | 116 ms   | 107 ms: 1.09x faster   |
| crypto_pyaes               | 77.9 ms  | 72.5 ms: 1.07x faster  |
| pprint_safe_repr           | 788 ms   | 736 ms: 1.07x faster   |
| pprint_pformat             | 1.61 sec | 1.51 sec: 1.07x faster |
| tomli_loads                | 1.99 sec | 1.88 sec: 1.06x faster |
| scimark_sparse_mat_mult    | 4.34 ms  | 4.14 ms: 1.05x faster  |
| fannkuch                   | 407 ms   | 393 ms: 1.04x faster   |
| xml_etree_generate         | 89.5 ms  | 86.8 ms: 1.03x faster  |
| subparsers                 | 20.8 ms  | 20.2 ms: 1.03x faster  |
| typing_runtime_protocols   | 150 us   | 148 us: 1.02x faster   |
| sqlglot_v2_normalize       | 106 ms   | 104 ms: 1.02x faster   |
| genshi_xml                 | 48.8 ms  | 48.1 ms: 1.01x faster  |
| mako                       | 11.7 ms  | 11.6 ms: 1.01x faster  |
| coroutines                 | 21.9 ms  | 22.1 ms: 1.01x slower  |
| bpe_tokeniser              | 4.30 sec | 4.39 sec: 1.02x slower |
| sqlglot_v2_optimize        | 51.0 ms  | 52.2 ms: 1.02x slower  |
| async_tree_none_tg         | 236 ms   | 242 ms: 1.02x slower   |
| async_tree_memoization     | 297 ms   | 306 ms: 1.03x slower   |
| async_tree_memoization_tg  | 291 ms   | 307 ms: 1.06x slower   |
| thrift                     | 694 us   | 737 us: 1.06x slower   |
| sympy_integrate            | 17.8 ms  | 18.9 ms: 1.06x slower  |
| scimark_fft                | 269 ms   | 289 ms: 1.08x slower   |
| async_tree_io              | 553 ms   | 596 ms: 1.08x slower   |
| sympy_str                  | 238 ms   | 258 ms: 1.08x slower   |
| async_tree_io_tg           | 559 ms   | 606 ms: 1.08x slower   |
| sympy_expand               | 405 ms   | 440 ms: 1.09x slower   |
| pylint                     | 253 ms   | 275 ms: 1.09x slower   |
| html5lib                   | 51.3 ms  | 57.3 ms: 1.12x slower  |
| async_generators           | 328 ms   | 368 ms: 1.12x slower   |
| xml_etree_iterparse        | 89.9 ms  | 103 ms: 1.14x slower   |
| telco                      | 6.44 ms  | 7.39 ms: 1.15x slower  |
| sphinx                     | 872 ms   | 1.00 sec: 1.15x slower |
| meteor_contest             | 95.9 ms  | 111 ms: 1.15x slower   |
| pycparser                  | 992 ms   | 1.16 sec: 1.16x slower |
| async_tree_cpu_io_mixed    | 437 ms   | 517 ms: 1.18x slower   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 504 ms: 1.19x slower   |
| sympy_sum                  | 119 ms   | 143 ms: 1.19x slower   |
| docutils                   | 2.17 sec | 2.61 sec: 1.20x slower |
| dulwich_log                | 51.0 ms  | 61.8 ms: 1.21x slower  |
| k_core                     | 1.83 sec | 2.27 sec: 1.24x slower |
| shortest_path              | 378 ms   | 480 ms: 1.27x slower   |
| connected_components       | 347 ms   | 445 ms: 1.28x slower   |
| coverage                   | 61.9 ms  | 79.6 ms: 1.29x slower  |
| json_loads                 | 22.3 us  | 28.9 us: 1.29x slower  |
| json                       | 3.96 ms  | 5.28 ms: 1.33x slower  |
| json_dumps                 | 9.01 ms  | 12.5 ms: 1.38x slower  |
| regex_v8                   | 17.1 ms  | 23.8 ms: 1.39x slower  |
| sqlite_synth               | 1.84 us  | 2.66 us: 1.44x slower  |
| pidigits                   | 152 ms   | 219 ms: 1.44x slower   |
| mdp                        | 1.81 sec | 2.65 sec: 1.46x slower |
| xml_etree_parse            | 108 ms   | 163 ms: 1.51x slower   |
| gc_traversal               | 3.15 ms  | 4.97 ms: 1.58x slower  |
| regex_dna                  | 121 ms   | 196 ms: 1.62x slower   |
| many_optionals             | 547 us   | 924 us: 1.69x slower   |
| asyncio_websockets         | 317 ms   | 551 ms: 1.74x slower   |
| regex_effbot               | 1.81 ms  | 3.28 ms: 1.81x slower  |
| create_gc_cycles           | 1.40 ms  | 2.54 ms: 1.81x slower  |
| Geometric mean             | (ref)    | 1.00x slower           |

Benchmark hidden because not significant (2): async_tree_none, regex_compile
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 91.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown