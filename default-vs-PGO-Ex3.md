# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.273x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | default                |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 298 ms: 1.32x slower   |
| docutils       | 1.71 sec | 2.17 sec: 1.27x slower |
| html5lib       | 40.5 ms  | 51.3 ms: 1.27x slower  |
| sphinx         | 670 ms   | 872 ms: 1.30x slower   |
| Geometric mean | (ref)    | 1.29x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | default               |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 311 ms  | 317 ms: 1.02x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 424 ms: 1.23x slower  |
| async_tree_cpu_io_mixed    | 340 ms  | 437 ms: 1.28x slower  |
| async_tree_io              | 417 ms  | 553 ms: 1.33x slower  |
| async_tree_memoization_tg  | 219 ms  | 291 ms: 1.33x slower  |
| async_tree_memoization     | 223 ms  | 297 ms: 1.33x slower  |
| async_tree_none_tg         | 176 ms  | 236 ms: 1.34x slower  |
| async_tree_none            | 186 ms  | 249 ms: 1.34x slower  |
| async_tree_io_tg           | 410 ms  | 559 ms: 1.36x slower  |
| async_generators           | 219 ms  | 328 ms: 1.50x slower  |
| coroutines                 | 13.1 ms | 21.9 ms: 1.67x slower |
| Geometric mean             | (ref)   | 1.33x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | default               |
|----------------|:-------:|:---------------------:|
| pidigits       | 148 ms  | 152 ms: 1.03x slower  |
| nbody          | 78.3 ms | 101 ms: 1.28x slower  |
| float          | 44.2 ms | 75.4 ms: 1.70x slower |
| Geometric mean | (ref)   | 1.31x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | default               |
|----------------|:-------:|:---------------------:|
| regex_dna      | 116 ms  | 121 ms: 1.04x slower  |
| regex_v8       | 13.8 ms | 17.1 ms: 1.24x slower |
| regex_effbot   | 1.46 ms | 1.81 ms: 1.25x slower |
| regex_compile  | 86.1 ms | 125 ms: 1.45x slower  |
| Geometric mean | (ref)   | 1.24x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | default                |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 88.8 ms  | 108 ms: 1.22x slower   |
| json_dumps           | 6.69 ms  | 9.01 ms: 1.35x slower  |
| tomli_loads          | 1.44 sec | 1.99 sec: 1.39x slower |
| xml_etree_iterparse  | 62.3 ms  | 89.9 ms: 1.44x slower  |
| json_loads           | 15.3 us  | 22.3 us: 1.46x slower  |
| xml_etree_generate   | 56.8 ms  | 89.5 ms: 1.57x slower  |
| xml_etree_process    | 39.7 ms  | 64.6 ms: 1.63x slower  |
| pickle_pure_python   | 217 us   | 355 us: 1.63x slower   |
| unpickle_pure_python | 147 us   | 274 us: 1.87x slower   |
| Geometric mean       | (ref)    | 1.50x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | default               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 20.4 ms: 1.09x slower |
| python_startup         | 24.5 ms | 27.3 ms: 1.12x slower |
| Geometric mean         | (ref)   | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | default               |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 48.8 ms: 1.40x slower |
| django_template | 25.5 ms | 36.9 ms: 1.45x slower |
| genshi_text     | 15.8 ms | 23.2 ms: 1.46x slower |
| mako            | 6.50 ms | 11.7 ms: 1.80x slower |
| Geometric mean  | (ref)   | 1.52x slower          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | default                |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 41.0 ms  | 20.8 ms: 1.98x faster  |
| many_optionals             | 695 us   | 547 us: 1.27x faster   |
| asyncio_websockets         | 311 ms   | 317 ms: 1.02x slower   |
| pidigits                   | 148 ms   | 152 ms: 1.03x slower   |
| regex_dna                  | 116 ms   | 121 ms: 1.04x slower   |
| k_core                     | 1.73 sec | 1.83 sec: 1.06x slower |
| shortest_path              | 354 ms   | 378 ms: 1.07x slower   |
| connected_components       | 324 ms   | 347 ms: 1.07x slower   |
| python_startup_no_site     | 18.7 ms  | 20.4 ms: 1.09x slower  |
| python_startup             | 24.5 ms  | 27.3 ms: 1.12x slower  |
| mdp                        | 1.62 sec | 1.81 sec: 1.12x slower |
| create_gc_cycles           | 1.25 ms  | 1.40 ms: 1.12x slower  |
| sqlite_synth               | 1.57 us  | 1.84 us: 1.17x slower  |
| dulwich_log                | 42.4 ms  | 51.0 ms: 1.20x slower  |
| pylint                     | 208 ms   | 253 ms: 1.21x slower   |
| xml_etree_parse            | 88.8 ms  | 108 ms: 1.22x slower   |
| async_tree_cpu_io_mixed_tg | 344 ms   | 424 ms: 1.23x slower   |
| regex_v8                   | 13.8 ms  | 17.1 ms: 1.24x slower  |
| regex_effbot               | 1.46 ms  | 1.81 ms: 1.25x slower  |
| json                       | 3.16 ms  | 3.96 ms: 1.25x slower  |
| coverage                   | 49.2 ms  | 61.9 ms: 1.26x slower  |
| html5lib                   | 40.5 ms  | 51.3 ms: 1.27x slower  |
| docutils                   | 1.71 sec | 2.17 sec: 1.27x slower |
| async_tree_cpu_io_mixed    | 340 ms   | 437 ms: 1.28x slower   |
| nbody                      | 78.3 ms  | 101 ms: 1.28x slower   |
| meteor_contest             | 74.3 ms  | 95.9 ms: 1.29x slower  |
| sphinx                     | 670 ms   | 872 ms: 1.30x slower   |
| sympy_integrate            | 13.6 ms  | 17.8 ms: 1.31x slower  |
| logging_format             | 7.11 us  | 9.33 us: 1.31x slower  |
| sympy_sum                  | 90.8 ms  | 119 ms: 1.31x slower   |
| 2to3                       | 227 ms   | 298 ms: 1.32x slower   |
| sympy_expand               | 305 ms   | 405 ms: 1.33x slower   |
| async_tree_io              | 417 ms   | 553 ms: 1.33x slower   |
| thrift                     | 522 us   | 694 us: 1.33x slower   |
| async_tree_memoization_tg  | 219 ms   | 291 ms: 1.33x slower   |
| pycparser                  | 745 ms   | 992 ms: 1.33x slower   |
| async_tree_memoization     | 223 ms   | 297 ms: 1.33x slower   |
| async_tree_none_tg         | 176 ms   | 236 ms: 1.34x slower   |
| async_tree_none            | 186 ms   | 249 ms: 1.34x slower   |
| json_dumps                 | 6.69 ms  | 9.01 ms: 1.35x slower  |
| sympy_str                  | 177 ms   | 238 ms: 1.35x slower   |
| telco                      | 4.75 ms  | 6.44 ms: 1.35x slower  |
| logging_simple             | 6.53 us  | 8.87 us: 1.36x slower  |
| async_tree_io_tg           | 410 ms   | 559 ms: 1.36x slower   |
| tomli_loads                | 1.44 sec | 1.99 sec: 1.39x slower |
| sqlglot_v2_normalize       | 76.3 ms  | 106 ms: 1.39x slower   |
| pathlib                    | 24.6 ms  | 34.4 ms: 1.40x slower  |
| genshi_xml                 | 35.0 ms  | 48.8 ms: 1.40x slower  |
| typing_runtime_protocols   | 106 us   | 150 us: 1.42x slower   |
| sqlglot_v2_optimize        | 35.6 ms  | 51.0 ms: 1.43x slower  |
| scimark_fft                | 187 ms   | 269 ms: 1.44x slower   |
| xml_etree_iterparse        | 62.3 ms  | 89.9 ms: 1.44x slower  |
| django_template            | 25.5 ms  | 36.9 ms: 1.45x slower  |
| regex_compile              | 86.1 ms  | 125 ms: 1.45x slower   |
| deepcopy                   | 185 us   | 269 us: 1.45x slower   |
| json_loads                 | 15.3 us  | 22.3 us: 1.46x slower  |
| genshi_text                | 15.8 ms  | 23.2 ms: 1.46x slower  |
| bpe_tokeniser              | 2.93 sec | 4.30 sec: 1.47x slower |
| deepcopy_reduce            | 1.88 us  | 2.77 us: 1.47x slower  |
| pprint_safe_repr           | 532 ms   | 788 ms: 1.48x slower   |
| pprint_pformat             | 1.09 sec | 1.61 sec: 1.48x slower |
| sqlglot_v2_transpile       | 1.09 ms  | 1.64 ms: 1.50x slower  |
| async_generators           | 219 ms   | 328 ms: 1.50x slower   |
| raytrace                   | 201 ms   | 304 ms: 1.51x slower   |
| nqueens                    | 62.2 ms  | 94.3 ms: 1.52x slower  |
| gc_traversal               | 2.07 ms  | 3.15 ms: 1.52x slower  |
| pyflate                    | 300 ms   | 462 ms: 1.54x slower   |
| chaos                      | 42.2 ms  | 65.2 ms: 1.55x slower  |
| fannkuch                   | 263 ms   | 407 ms: 1.55x slower   |
| sqlglot_v2_parse           | 870 us   | 1.36 ms: 1.56x slower  |
| xml_etree_generate         | 56.8 ms  | 89.5 ms: 1.57x slower  |
| crypto_pyaes               | 48.6 ms  | 77.9 ms: 1.60x slower  |
| scimark_sor                | 84.2 ms  | 135 ms: 1.60x slower   |
| xml_etree_process          | 39.7 ms  | 64.6 ms: 1.63x slower  |
| go                         | 84.1 ms  | 137 ms: 1.63x slower   |
| pickle_pure_python         | 217 us   | 355 us: 1.63x slower   |
| scimark_monte_carlo        | 45.3 ms  | 73.9 ms: 1.63x slower  |
| richards_super             | 39.9 ms  | 65.8 ms: 1.65x slower  |
| scimark_sparse_mat_mult    | 2.63 ms  | 4.34 ms: 1.65x slower  |
| coroutines                 | 13.1 ms  | 21.9 ms: 1.67x slower  |
| richards                   | 34.5 ms  | 57.8 ms: 1.67x slower  |
| spectral_norm              | 58.1 ms  | 97.7 ms: 1.68x slower  |
| generators                 | 20.0 ms  | 33.8 ms: 1.69x slower  |
| hexiom                     | 4.28 ms  | 7.27 ms: 1.70x slower  |
| float                      | 44.2 ms  | 75.4 ms: 1.70x slower  |
| deepcopy_memo              | 19.1 us  | 32.9 us: 1.72x slower  |
| comprehensions             | 11.2 us  | 19.4 us: 1.73x slower  |
| mako                       | 6.50 ms  | 11.7 ms: 1.80x slower  |
| unpickle_pure_python       | 147 us   | 274 us: 1.87x slower   |
| deltablue                  | 2.18 ms  | 4.09 ms: 1.87x slower  |
| scimark_lu                 | 61.1 ms  | 116 ms: 1.90x slower   |
| logging_silent             | 57.0 ns  | 119 ns: 2.09x slower   |
| Geometric mean             | (ref)    | 1.38x slower           |
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.273x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: unknown