# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.376x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | PGO-Ex3                |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 227 ms: 1.32x faster   |
| docutils       | 2.17 sec | 1.71 sec: 1.27x faster |
| html5lib       | 51.3 ms  | 40.5 ms: 1.27x faster  |
| sphinx         | 872 ms   | 670 ms: 1.30x faster   |
| Geometric mean | (ref)    | 1.29x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | PGO-Ex3               |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 13.1 ms: 1.67x faster |
| async_generators           | 328 ms  | 219 ms: 1.50x faster  |
| async_tree_io_tg           | 559 ms  | 410 ms: 1.36x faster  |
| async_tree_none            | 249 ms  | 186 ms: 1.34x faster  |
| async_tree_none_tg         | 236 ms  | 176 ms: 1.34x faster  |
| async_tree_memoization     | 297 ms  | 223 ms: 1.33x faster  |
| async_tree_memoization_tg  | 291 ms  | 219 ms: 1.33x faster  |
| async_tree_io              | 553 ms  | 417 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 340 ms: 1.28x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 344 ms: 1.23x faster  |
| asyncio_websockets         | 317 ms  | 311 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.33x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| float          | 75.4 ms | 44.2 ms: 1.70x faster |
| nbody          | 101 ms  | 78.3 ms: 1.28x faster |
| pidigits       | 152 ms  | 148 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.31x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 86.1 ms: 1.45x faster |
| regex_effbot   | 1.81 ms | 1.46 ms: 1.25x faster |
| regex_v8       | 17.1 ms | 13.8 ms: 1.24x faster |
| regex_dna      | 121 ms  | 116 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.24x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | PGO-Ex3                |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 147 us: 1.87x faster   |
| pickle_pure_python   | 355 us   | 217 us: 1.63x faster   |
| xml_etree_process    | 64.6 ms  | 39.7 ms: 1.63x faster  |
| xml_etree_generate   | 89.5 ms  | 56.8 ms: 1.57x faster  |
| json_loads           | 22.3 us  | 15.3 us: 1.46x faster  |
| xml_etree_iterparse  | 89.9 ms  | 62.3 ms: 1.44x faster  |
| tomli_loads          | 1.99 sec | 1.44 sec: 1.39x faster |
| json_dumps           | 9.01 ms  | 6.69 ms: 1.35x faster  |
| xml_etree_parse      | 108 ms   | 88.8 ms: 1.22x faster  |
| Geometric mean       | (ref)    | 1.50x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | PGO-Ex3               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 24.5 ms: 1.12x faster |
| python_startup_no_site | 20.4 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | PGO-Ex3               |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.50 ms: 1.80x faster |
| genshi_text     | 23.2 ms | 15.8 ms: 1.46x faster |
| django_template | 36.9 ms | 25.5 ms: 1.45x faster |
| genshi_xml      | 48.8 ms | 35.0 ms: 1.40x faster |
| Geometric mean  | (ref)   | 1.52x faster          |

All benchmarks:
===============

| Benchmark                  | default  | PGO-Ex3                |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 57.0 ns: 2.09x faster  |
| scimark_lu                 | 116 ms   | 61.1 ms: 1.90x faster  |
| deltablue                  | 4.09 ms  | 2.18 ms: 1.87x faster  |
| unpickle_pure_python       | 274 us   | 147 us: 1.87x faster   |
| mako                       | 11.7 ms  | 6.50 ms: 1.80x faster  |
| comprehensions             | 19.4 us  | 11.2 us: 1.73x faster  |
| deepcopy_memo              | 32.9 us  | 19.1 us: 1.72x faster  |
| float                      | 75.4 ms  | 44.2 ms: 1.70x faster  |
| hexiom                     | 7.27 ms  | 4.28 ms: 1.70x faster  |
| generators                 | 33.8 ms  | 20.0 ms: 1.69x faster  |
| spectral_norm              | 97.7 ms  | 58.1 ms: 1.68x faster  |
| richards                   | 57.8 ms  | 34.5 ms: 1.67x faster  |
| coroutines                 | 21.9 ms  | 13.1 ms: 1.67x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.63 ms: 1.65x faster  |
| richards_super             | 65.8 ms  | 39.9 ms: 1.65x faster  |
| scimark_monte_carlo        | 73.9 ms  | 45.3 ms: 1.63x faster  |
| pickle_pure_python         | 355 us   | 217 us: 1.63x faster   |
| go                         | 137 ms   | 84.1 ms: 1.63x faster  |
| xml_etree_process          | 64.6 ms  | 39.7 ms: 1.63x faster  |
| scimark_sor                | 135 ms   | 84.2 ms: 1.60x faster  |
| crypto_pyaes               | 77.9 ms  | 48.6 ms: 1.60x faster  |
| xml_etree_generate         | 89.5 ms  | 56.8 ms: 1.57x faster  |
| sqlglot_v2_parse           | 1.36 ms  | 870 us: 1.56x faster   |
| fannkuch                   | 407 ms   | 263 ms: 1.55x faster   |
| chaos                      | 65.2 ms  | 42.2 ms: 1.55x faster  |
| pyflate                    | 462 ms   | 300 ms: 1.54x faster   |
| gc_traversal               | 3.15 ms  | 2.07 ms: 1.52x faster  |
| nqueens                    | 94.3 ms  | 62.2 ms: 1.52x faster  |
| raytrace                   | 304 ms   | 201 ms: 1.51x faster   |
| async_generators           | 328 ms   | 219 ms: 1.50x faster   |
| sqlglot_v2_transpile       | 1.64 ms  | 1.09 ms: 1.50x faster  |
| pprint_pformat             | 1.61 sec | 1.09 sec: 1.48x faster |
| pprint_safe_repr           | 788 ms   | 532 ms: 1.48x faster   |
| deepcopy_reduce            | 2.77 us  | 1.88 us: 1.47x faster  |
| bpe_tokeniser              | 4.30 sec | 2.93 sec: 1.47x faster |
| genshi_text                | 23.2 ms  | 15.8 ms: 1.46x faster  |
| json_loads                 | 22.3 us  | 15.3 us: 1.46x faster  |
| deepcopy                   | 269 us   | 185 us: 1.45x faster   |
| regex_compile              | 125 ms   | 86.1 ms: 1.45x faster  |
| django_template            | 36.9 ms  | 25.5 ms: 1.45x faster  |
| xml_etree_iterparse        | 89.9 ms  | 62.3 ms: 1.44x faster  |
| scimark_fft                | 269 ms   | 187 ms: 1.44x faster   |
| sqlglot_v2_optimize        | 51.0 ms  | 35.6 ms: 1.43x faster  |
| typing_runtime_protocols   | 150 us   | 106 us: 1.42x faster   |
| genshi_xml                 | 48.8 ms  | 35.0 ms: 1.40x faster  |
| pathlib                    | 34.4 ms  | 24.6 ms: 1.40x faster  |
| sqlglot_v2_normalize       | 106 ms   | 76.3 ms: 1.39x faster  |
| tomli_loads                | 1.99 sec | 1.44 sec: 1.39x faster |
| async_tree_io_tg           | 559 ms   | 410 ms: 1.36x faster   |
| logging_simple             | 8.87 us  | 6.53 us: 1.36x faster  |
| telco                      | 6.44 ms  | 4.75 ms: 1.35x faster  |
| sympy_str                  | 238 ms   | 177 ms: 1.35x faster   |
| json_dumps                 | 9.01 ms  | 6.69 ms: 1.35x faster  |
| async_tree_none            | 249 ms   | 186 ms: 1.34x faster   |
| async_tree_none_tg         | 236 ms   | 176 ms: 1.34x faster   |
| async_tree_memoization     | 297 ms   | 223 ms: 1.33x faster   |
| pycparser                  | 992 ms   | 745 ms: 1.33x faster   |
| async_tree_memoization_tg  | 291 ms   | 219 ms: 1.33x faster   |
| thrift                     | 694 us   | 522 us: 1.33x faster   |
| async_tree_io              | 553 ms   | 417 ms: 1.33x faster   |
| sympy_expand               | 405 ms   | 305 ms: 1.33x faster   |
| 2to3                       | 298 ms   | 227 ms: 1.32x faster   |
| sympy_sum                  | 119 ms   | 90.8 ms: 1.31x faster  |
| logging_format             | 9.33 us  | 7.11 us: 1.31x faster  |
| sympy_integrate            | 17.8 ms  | 13.6 ms: 1.31x faster  |
| sphinx                     | 872 ms   | 670 ms: 1.30x faster   |
| meteor_contest             | 95.9 ms  | 74.3 ms: 1.29x faster  |
| nbody                      | 101 ms   | 78.3 ms: 1.28x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 340 ms: 1.28x faster   |
| docutils                   | 2.17 sec | 1.71 sec: 1.27x faster |
| html5lib                   | 51.3 ms  | 40.5 ms: 1.27x faster  |
| coverage                   | 61.9 ms  | 49.2 ms: 1.26x faster  |
| json                       | 3.96 ms  | 3.16 ms: 1.25x faster  |
| regex_effbot               | 1.81 ms  | 1.46 ms: 1.25x faster  |
| regex_v8                   | 17.1 ms  | 13.8 ms: 1.24x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 344 ms: 1.23x faster   |
| xml_etree_parse            | 108 ms   | 88.8 ms: 1.22x faster  |
| pylint                     | 253 ms   | 208 ms: 1.21x faster   |
| dulwich_log                | 51.0 ms  | 42.4 ms: 1.20x faster  |
| sqlite_synth               | 1.84 us  | 1.57 us: 1.17x faster  |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.12x faster  |
| mdp                        | 1.81 sec | 1.62 sec: 1.12x faster |
| python_startup             | 27.3 ms  | 24.5 ms: 1.12x faster  |
| python_startup_no_site     | 20.4 ms  | 18.7 ms: 1.09x faster  |
| connected_components       | 347 ms   | 324 ms: 1.07x faster   |
| shortest_path              | 378 ms   | 354 ms: 1.07x faster   |
| k_core                     | 1.83 sec | 1.73 sec: 1.06x faster |
| regex_dna                  | 121 ms   | 116 ms: 1.04x faster   |
| pidigits                   | 152 ms   | 148 ms: 1.03x faster   |
| asyncio_websockets         | 317 ms   | 311 ms: 1.02x faster   |
| many_optionals             | 547 us   | 695 us: 1.27x slower   |
| subparsers                 | 20.8 ms  | 41.0 ms: 1.98x slower  |
| Geometric mean             | (ref)    | 1.38x faster           |
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.376x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: unknown