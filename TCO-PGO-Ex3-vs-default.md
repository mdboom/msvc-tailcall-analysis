# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.500x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 215 ms: 1.39x faster   |
| docutils       | 2.17 sec | 1.66 sec: 1.31x faster |
| html5lib       | 51.3 ms  | 37.8 ms: 1.36x faster  |
| sphinx         | 872 ms   | 641 ms: 1.36x faster   |
| Geometric mean | (ref)    | 1.35x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 12.0 ms: 1.83x faster |
| async_generators           | 328 ms  | 201 ms: 1.63x faster  |
| async_tree_io_tg           | 559 ms  | 377 ms: 1.48x faster  |
| async_tree_none            | 249 ms  | 170 ms: 1.47x faster  |
| async_tree_none_tg         | 236 ms  | 161 ms: 1.47x faster  |
| async_tree_memoization     | 297 ms  | 205 ms: 1.45x faster  |
| async_tree_io              | 553 ms  | 382 ms: 1.45x faster  |
| async_tree_memoization_tg  | 291 ms  | 208 ms: 1.40x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 330 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 330 ms: 1.29x faster  |
| asyncio_websockets         | 317 ms  | 313 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 55.6 ms: 1.81x faster |
| float          | 75.4 ms | 42.0 ms: 1.80x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.50x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 79.4 ms: 1.57x faster |
| regex_effbot   | 1.81 ms | 1.47 ms: 1.23x faster |
| regex_v8       | 17.1 ms | 14.2 ms: 1.20x faster |
| regex_dna      | 121 ms  | 120 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.24x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 124 us: 2.21x faster   |
| pickle_pure_python   | 355 us   | 199 us: 1.78x faster   |
| xml_etree_process    | 64.6 ms  | 36.8 ms: 1.75x faster  |
| tomli_loads          | 1.99 sec | 1.17 sec: 1.70x faster |
| xml_etree_generate   | 89.5 ms  | 53.1 ms: 1.69x faster  |
| json_loads           | 22.3 us  | 14.5 us: 1.54x faster  |
| xml_etree_iterparse  | 89.9 ms  | 61.2 ms: 1.47x faster  |
| json_dumps           | 9.01 ms  | 6.40 ms: 1.41x faster  |
| xml_etree_parse      | 108 ms   | 89.4 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.62x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 24.7 ms: 1.11x faster |
| python_startup_no_site | 20.4 ms | 18.6 ms: 1.10x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.25 ms: 1.87x faster |
| genshi_text     | 23.2 ms | 14.3 ms: 1.62x faster |
| django_template | 36.9 ms | 23.6 ms: 1.57x faster |
| genshi_xml      | 48.8 ms | 32.3 ms: 1.51x faster |
| Geometric mean  | (ref)   | 1.64x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 49.7 ns: 2.41x faster  |
| scimark_lu                 | 116 ms   | 50.3 ms: 2.31x faster  |
| scimark_sor                | 135 ms   | 60.5 ms: 2.23x faster  |
| unpickle_pure_python       | 274 us   | 124 us: 2.21x faster   |
| deltablue                  | 4.09 ms  | 1.88 ms: 2.17x faster  |
| hexiom                     | 7.27 ms  | 3.49 ms: 2.08x faster  |
| scimark_monte_carlo        | 73.9 ms  | 35.6 ms: 2.07x faster  |
| generators                 | 33.8 ms  | 16.5 ms: 2.05x faster  |
| comprehensions             | 19.4 us  | 9.76 us: 1.98x faster  |
| spectral_norm              | 97.7 ms  | 49.4 ms: 1.98x faster  |
| richards                   | 57.8 ms  | 29.4 ms: 1.97x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.21 ms: 1.97x faster  |
| richards_super             | 65.8 ms  | 33.7 ms: 1.95x faster  |
| deepcopy_memo              | 32.9 us  | 16.8 us: 1.95x faster  |
| go                         | 137 ms   | 70.5 ms: 1.94x faster  |
| raytrace                   | 304 ms   | 162 ms: 1.88x faster   |
| mako                       | 11.7 ms  | 6.25 ms: 1.87x faster  |
| chaos                      | 65.2 ms  | 35.4 ms: 1.84x faster  |
| coroutines                 | 21.9 ms  | 12.0 ms: 1.83x faster  |
| fannkuch                   | 407 ms   | 225 ms: 1.81x faster   |
| nbody                      | 101 ms   | 55.6 ms: 1.81x faster  |
| float                      | 75.4 ms  | 42.0 ms: 1.80x faster  |
| pickle_pure_python         | 355 us   | 199 us: 1.78x faster   |
| crypto_pyaes               | 77.9 ms  | 43.9 ms: 1.77x faster  |
| xml_etree_process          | 64.6 ms  | 36.8 ms: 1.75x faster  |
| scimark_fft                | 269 ms   | 153 ms: 1.75x faster   |
| pyflate                    | 462 ms   | 264 ms: 1.75x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 781 us: 1.74x faster   |
| nqueens                    | 94.3 ms  | 55.2 ms: 1.71x faster  |
| tomli_loads                | 1.99 sec | 1.17 sec: 1.70x faster |
| xml_etree_generate         | 89.5 ms  | 53.1 ms: 1.69x faster  |
| pprint_pformat             | 1.61 sec | 956 ms: 1.68x faster   |
| pprint_safe_repr           | 788 ms   | 474 ms: 1.66x faster   |
| deepcopy_reduce            | 2.77 us  | 1.68 us: 1.65x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 993 us: 1.65x faster   |
| async_generators           | 328 ms   | 201 ms: 1.63x faster   |
| genshi_text                | 23.2 ms  | 14.3 ms: 1.62x faster  |
| deepcopy                   | 269 us   | 167 us: 1.61x faster   |
| bpe_tokeniser              | 4.30 sec | 2.72 sec: 1.58x faster |
| regex_compile              | 125 ms   | 79.4 ms: 1.57x faster  |
| django_template            | 36.9 ms  | 23.6 ms: 1.57x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 32.9 ms: 1.55x faster  |
| json_loads                 | 22.3 us  | 14.5 us: 1.54x faster  |
| sqlglot_v2_normalize       | 106 ms   | 69.0 ms: 1.54x faster  |
| typing_runtime_protocols   | 150 us   | 97.8 us: 1.54x faster  |
| genshi_xml                 | 48.8 ms  | 32.3 ms: 1.51x faster  |
| logging_simple             | 8.87 us  | 5.87 us: 1.51x faster  |
| gc_traversal               | 3.15 ms  | 2.12 ms: 1.49x faster  |
| async_tree_io_tg           | 559 ms   | 377 ms: 1.48x faster   |
| async_tree_none            | 249 ms   | 170 ms: 1.47x faster   |
| async_tree_none_tg         | 236 ms   | 161 ms: 1.47x faster   |
| xml_etree_iterparse        | 89.9 ms  | 61.2 ms: 1.47x faster  |
| logging_format             | 9.33 us  | 6.42 us: 1.45x faster  |
| async_tree_memoization     | 297 ms   | 205 ms: 1.45x faster   |
| async_tree_io              | 553 ms   | 382 ms: 1.45x faster   |
| pycparser                  | 992 ms   | 689 ms: 1.44x faster   |
| sympy_expand               | 405 ms   | 283 ms: 1.43x faster   |
| pathlib                    | 34.4 ms  | 24.2 ms: 1.42x faster  |
| thrift                     | 694 us   | 491 us: 1.41x faster   |
| json_dumps                 | 9.01 ms  | 6.40 ms: 1.41x faster  |
| sympy_sum                  | 119 ms   | 85.2 ms: 1.40x faster  |
| telco                      | 6.44 ms  | 4.59 ms: 1.40x faster  |
| async_tree_memoization_tg  | 291 ms   | 208 ms: 1.40x faster   |
| sympy_integrate            | 17.8 ms  | 12.8 ms: 1.39x faster  |
| 2to3                       | 298 ms   | 215 ms: 1.39x faster   |
| sympy_str                  | 238 ms   | 173 ms: 1.38x faster   |
| sphinx                     | 872 ms   | 641 ms: 1.36x faster   |
| html5lib                   | 51.3 ms  | 37.8 ms: 1.36x faster  |
| meteor_contest             | 95.9 ms  | 70.9 ms: 1.35x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 330 ms: 1.32x faster   |
| docutils                   | 2.17 sec | 1.66 sec: 1.31x faster |
| json                       | 3.96 ms  | 3.04 ms: 1.30x faster  |
| coverage                   | 61.9 ms  | 47.5 ms: 1.30x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 330 ms: 1.29x faster   |
| mdp                        | 1.81 sec | 1.43 sec: 1.27x faster |
| dulwich_log                | 51.0 ms  | 40.3 ms: 1.27x faster  |
| pylint                     | 253 ms   | 201 ms: 1.26x faster   |
| regex_effbot               | 1.81 ms  | 1.47 ms: 1.23x faster  |
| xml_etree_parse            | 108 ms   | 89.4 ms: 1.21x faster  |
| regex_v8                   | 17.1 ms  | 14.2 ms: 1.20x faster  |
| sqlite_synth               | 1.84 us  | 1.56 us: 1.18x faster  |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.12x faster  |
| python_startup             | 27.3 ms  | 24.7 ms: 1.11x faster  |
| python_startup_no_site     | 20.4 ms  | 18.6 ms: 1.10x faster  |
| shortest_path              | 378 ms   | 352 ms: 1.07x faster   |
| k_core                     | 1.83 sec | 1.70 sec: 1.07x faster |
| connected_components       | 347 ms   | 325 ms: 1.07x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| asyncio_websockets         | 317 ms   | 313 ms: 1.02x faster   |
| regex_dna                  | 121 ms   | 120 ms: 1.01x faster   |
| many_optionals             | 547 us   | 685 us: 1.25x slower   |
| subparsers                 | 20.8 ms  | 41.4 ms: 1.99x slower  |
| Geometric mean             | (ref)    | 1.51x faster           |
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.500x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.42x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown