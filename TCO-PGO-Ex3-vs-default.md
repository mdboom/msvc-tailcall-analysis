# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.498x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 212 ms: 1.41x faster   |
| docutils       | 2.17 sec | 1.67 sec: 1.30x faster |
| html5lib       | 51.3 ms  | 37.9 ms: 1.35x faster  |
| sphinx         | 872 ms   | 645 ms: 1.35x faster   |
| Geometric mean | (ref)    | 1.35x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 11.9 ms: 1.84x faster |
| async_generators           | 328 ms  | 202 ms: 1.62x faster  |
| async_tree_none_tg         | 236 ms  | 159 ms: 1.49x faster  |
| async_tree_io_tg           | 559 ms  | 377 ms: 1.48x faster  |
| async_tree_none            | 249 ms  | 170 ms: 1.47x faster  |
| async_tree_memoization     | 297 ms  | 206 ms: 1.45x faster  |
| async_tree_io              | 553 ms  | 384 ms: 1.44x faster  |
| async_tree_memoization_tg  | 291 ms  | 208 ms: 1.40x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 330 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 329 ms: 1.29x faster  |
| asyncio_websockets         | 317 ms  | 301 ms: 1.06x faster  |
| Geometric mean             | (ref)   | 1.43x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 55.2 ms: 1.82x faster |
| float          | 75.4 ms | 41.9 ms: 1.80x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.51x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 78.1 ms: 1.60x faster |
| regex_v8       | 17.1 ms | 13.2 ms: 1.29x faster |
| regex_effbot   | 1.81 ms | 1.46 ms: 1.24x faster |
| Geometric mean | (ref)   | 1.27x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 127 us: 2.15x faster   |
| pickle_pure_python   | 355 us   | 199 us: 1.78x faster   |
| xml_etree_process    | 64.6 ms  | 37.0 ms: 1.74x faster  |
| tomli_loads          | 1.99 sec | 1.18 sec: 1.69x faster |
| xml_etree_generate   | 89.5 ms  | 53.6 ms: 1.67x faster  |
| json_loads           | 22.3 us  | 14.7 us: 1.52x faster  |
| xml_etree_iterparse  | 89.9 ms  | 61.2 ms: 1.47x faster  |
| json_dumps           | 9.01 ms  | 6.55 ms: 1.38x faster  |
| xml_etree_parse      | 108 ms   | 89.3 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.60x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 24.7 ms: 1.11x faster |
| python_startup_no_site | 20.4 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.28 ms: 1.86x faster |
| genshi_text     | 23.2 ms | 14.3 ms: 1.62x faster |
| django_template | 36.9 ms | 22.9 ms: 1.61x faster |
| genshi_xml      | 48.8 ms | 32.8 ms: 1.49x faster |
| Geometric mean  | (ref)   | 1.64x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 49.4 ns: 2.42x faster  |
| scimark_lu                 | 116 ms   | 50.9 ms: 2.28x faster  |
| scimark_sor                | 135 ms   | 61.1 ms: 2.21x faster  |
| deltablue                  | 4.09 ms  | 1.88 ms: 2.17x faster  |
| unpickle_pure_python       | 274 us   | 127 us: 2.15x faster   |
| hexiom                     | 7.27 ms  | 3.54 ms: 2.06x faster  |
| scimark_monte_carlo        | 73.9 ms  | 36.0 ms: 2.06x faster  |
| generators                 | 33.8 ms  | 16.5 ms: 2.05x faster  |
| richards                   | 57.8 ms  | 28.7 ms: 2.01x faster  |
| richards_super             | 65.8 ms  | 33.1 ms: 1.99x faster  |
| deepcopy_memo              | 32.9 us  | 16.6 us: 1.98x faster  |
| spectral_norm              | 97.7 ms  | 49.4 ms: 1.98x faster  |
| comprehensions             | 19.4 us  | 9.87 us: 1.96x faster  |
| go                         | 137 ms   | 70.9 ms: 1.93x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.27 ms: 1.92x faster  |
| raytrace                   | 304 ms   | 160 ms: 1.89x faster   |
| mako                       | 11.7 ms  | 6.28 ms: 1.86x faster  |
| coroutines                 | 21.9 ms  | 11.9 ms: 1.84x faster  |
| fannkuch                   | 407 ms   | 223 ms: 1.83x faster   |
| nbody                      | 101 ms   | 55.2 ms: 1.82x faster  |
| float                      | 75.4 ms  | 41.9 ms: 1.80x faster  |
| pickle_pure_python         | 355 us   | 199 us: 1.78x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 766 us: 1.77x faster   |
| chaos                      | 65.2 ms  | 36.9 ms: 1.77x faster  |
| xml_etree_process          | 64.6 ms  | 37.0 ms: 1.74x faster  |
| scimark_fft                | 269 ms   | 154 ms: 1.74x faster   |
| nqueens                    | 94.3 ms  | 54.4 ms: 1.74x faster  |
| pyflate                    | 462 ms   | 268 ms: 1.72x faster   |
| tomli_loads                | 1.99 sec | 1.18 sec: 1.69x faster |
| sqlglot_v2_transpile       | 1.64 ms  | 970 us: 1.69x faster   |
| pprint_safe_repr           | 788 ms   | 470 ms: 1.68x faster   |
| xml_etree_generate         | 89.5 ms  | 53.6 ms: 1.67x faster  |
| pprint_pformat             | 1.61 sec | 967 ms: 1.67x faster   |
| crypto_pyaes               | 77.9 ms  | 47.4 ms: 1.64x faster  |
| deepcopy_reduce            | 2.77 us  | 1.70 us: 1.63x faster  |
| genshi_text                | 23.2 ms  | 14.3 ms: 1.62x faster  |
| async_generators           | 328 ms   | 202 ms: 1.62x faster   |
| deepcopy                   | 269 us   | 167 us: 1.61x faster   |
| django_template            | 36.9 ms  | 22.9 ms: 1.61x faster  |
| regex_compile              | 125 ms   | 78.1 ms: 1.60x faster  |
| bpe_tokeniser              | 4.30 sec | 2.72 sec: 1.58x faster |
| sqlglot_v2_optimize        | 51.0 ms  | 33.0 ms: 1.54x faster  |
| sqlglot_v2_normalize       | 106 ms   | 69.3 ms: 1.53x faster  |
| typing_runtime_protocols   | 150 us   | 98.8 us: 1.52x faster  |
| json_loads                 | 22.3 us  | 14.7 us: 1.52x faster  |
| gc_traversal               | 3.15 ms  | 2.11 ms: 1.50x faster  |
| async_tree_none_tg         | 236 ms   | 159 ms: 1.49x faster   |
| genshi_xml                 | 48.8 ms  | 32.8 ms: 1.49x faster  |
| logging_simple             | 8.87 us  | 5.97 us: 1.48x faster  |
| async_tree_io_tg           | 559 ms   | 377 ms: 1.48x faster   |
| xml_etree_iterparse        | 89.9 ms  | 61.2 ms: 1.47x faster  |
| async_tree_none            | 249 ms   | 170 ms: 1.47x faster   |
| sympy_str                  | 238 ms   | 164 ms: 1.45x faster   |
| pycparser                  | 992 ms   | 686 ms: 1.45x faster   |
| async_tree_memoization     | 297 ms   | 206 ms: 1.45x faster   |
| async_tree_io              | 553 ms   | 384 ms: 1.44x faster   |
| thrift                     | 694 us   | 482 us: 1.44x faster   |
| logging_format             | 9.33 us  | 6.50 us: 1.44x faster  |
| sympy_expand               | 405 ms   | 282 ms: 1.44x faster   |
| pathlib                    | 34.4 ms  | 24.1 ms: 1.43x faster  |
| 2to3                       | 298 ms   | 212 ms: 1.41x faster   |
| telco                      | 6.44 ms  | 4.57 ms: 1.41x faster  |
| async_tree_memoization_tg  | 291 ms   | 208 ms: 1.40x faster   |
| sympy_integrate            | 17.8 ms  | 12.8 ms: 1.39x faster  |
| sympy_sum                  | 119 ms   | 86.3 ms: 1.38x faster  |
| json_dumps                 | 9.01 ms  | 6.55 ms: 1.38x faster  |
| meteor_contest             | 95.9 ms  | 70.2 ms: 1.37x faster  |
| html5lib                   | 51.3 ms  | 37.9 ms: 1.35x faster  |
| sphinx                     | 872 ms   | 645 ms: 1.35x faster   |
| json                       | 3.96 ms  | 2.97 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 330 ms: 1.32x faster   |
| docutils                   | 2.17 sec | 1.67 sec: 1.30x faster |
| regex_v8                   | 17.1 ms  | 13.2 ms: 1.29x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 329 ms: 1.29x faster   |
| coverage                   | 61.9 ms  | 48.2 ms: 1.28x faster  |
| pylint                     | 253 ms   | 198 ms: 1.27x faster   |
| dulwich_log                | 51.0 ms  | 40.2 ms: 1.27x faster  |
| regex_effbot               | 1.81 ms  | 1.46 ms: 1.24x faster  |
| xml_etree_parse            | 108 ms   | 89.3 ms: 1.21x faster  |
| sqlite_synth               | 1.84 us  | 1.56 us: 1.18x faster  |
| mdp                        | 1.81 sec | 1.62 sec: 1.12x faster |
| python_startup             | 27.3 ms  | 24.7 ms: 1.11x faster  |
| create_gc_cycles           | 1.40 ms  | 1.27 ms: 1.10x faster  |
| python_startup_no_site     | 20.4 ms  | 18.7 ms: 1.09x faster  |
| shortest_path              | 378 ms   | 353 ms: 1.07x faster   |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| connected_components       | 347 ms   | 326 ms: 1.06x faster   |
| asyncio_websockets         | 317 ms   | 301 ms: 1.06x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| many_optionals             | 547 us   | 665 us: 1.22x slower   |
| subparsers                 | 20.8 ms  | 40.7 ms: 1.96x slower  |
| Geometric mean             | (ref)    | 1.51x faster           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.498x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.43x
- 99% likely to have a speedup of 1.41x

# Memory
- memory change: unknown