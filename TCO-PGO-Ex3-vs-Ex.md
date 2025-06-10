# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.560x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 215 ms: 1.43x faster   |
| docutils       | 2.31 sec | 1.66 sec: 1.39x faster |
| html5lib       | 52.5 ms  | 37.8 ms: 1.39x faster  |
| sphinx         | 933 ms   | 641 ms: 1.45x faster   |
| Geometric mean | (ref)    | 1.42x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 12.0 ms: 1.87x faster |
| async_generators           | 348 ms  | 201 ms: 1.73x faster  |
| async_tree_none            | 267 ms  | 170 ms: 1.57x faster  |
| async_tree_io_tg           | 576 ms  | 377 ms: 1.53x faster  |
| async_tree_memoization     | 313 ms  | 205 ms: 1.53x faster  |
| async_tree_none_tg         | 243 ms  | 161 ms: 1.51x faster  |
| async_tree_io              | 570 ms  | 382 ms: 1.49x faster  |
| async_tree_memoization_tg  | 304 ms  | 208 ms: 1.47x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 330 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 330 ms: 1.35x faster  |
| asyncio_websockets         | 330 ms  | 313 ms: 1.06x faster  |
| Geometric mean             | (ref)   | 1.48x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 55.6 ms: 1.86x faster |
| float          | 78.0 ms | 42.0 ms: 1.86x faster |
| pidigits       | 156 ms  | 145 ms: 1.08x faster  |
| Geometric mean | (ref)   | 1.55x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 79.4 ms: 1.64x faster |
| regex_effbot   | 1.87 ms | 1.47 ms: 1.27x faster |
| regex_v8       | 17.5 ms | 14.2 ms: 1.23x faster |
| regex_dna      | 123 ms  | 120 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.27x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 124 us: 2.29x faster   |
| pickle_pure_python   | 364 us   | 199 us: 1.83x faster   |
| xml_etree_process    | 66.9 ms  | 36.8 ms: 1.82x faster  |
| tomli_loads          | 2.07 sec | 1.17 sec: 1.76x faster |
| xml_etree_generate   | 92.6 ms  | 53.1 ms: 1.74x faster  |
| json_loads           | 23.3 us  | 14.5 us: 1.61x faster  |
| xml_etree_iterparse  | 94.3 ms  | 61.2 ms: 1.54x faster  |
| json_dumps           | 9.44 ms  | 6.40 ms: 1.48x faster  |
| xml_etree_parse      | 112 ms   | 89.4 ms: 1.26x faster  |
| Geometric mean       | (ref)    | 1.68x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 24.7 ms: 1.19x faster |
| python_startup_no_site | 22.0 ms | 18.6 ms: 1.18x faster |
| Geometric mean         | (ref)   | 1.19x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.25 ms: 1.93x faster |
| genshi_text     | 23.9 ms | 14.3 ms: 1.67x faster |
| django_template | 38.0 ms | 23.6 ms: 1.61x faster |
| genshi_xml      | 50.4 ms | 32.3 ms: 1.56x faster |
| Geometric mean  | (ref)   | 1.69x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 49.7 ns: 2.50x faster  |
| scimark_lu                 | 119 ms   | 50.3 ms: 2.38x faster  |
| unpickle_pure_python       | 284 us   | 124 us: 2.29x faster   |
| scimark_sor                | 139 ms   | 60.5 ms: 2.29x faster  |
| deltablue                  | 4.22 ms  | 1.88 ms: 2.24x faster  |
| generators                 | 35.6 ms  | 16.5 ms: 2.16x faster  |
| hexiom                     | 7.44 ms  | 3.49 ms: 2.13x faster  |
| scimark_monte_carlo        | 75.8 ms  | 35.6 ms: 2.13x faster  |
| comprehensions             | 20.1 us  | 9.76 us: 2.06x faster  |
| spectral_norm              | 102 ms   | 49.4 ms: 2.06x faster  |
| deepcopy_memo              | 34.0 us  | 16.8 us: 2.02x faster  |
| richards_super             | 67.7 ms  | 33.7 ms: 2.01x faster  |
| richards                   | 59.0 ms  | 29.4 ms: 2.01x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.21 ms: 2.01x faster  |
| go                         | 140 ms   | 70.5 ms: 1.99x faster  |
| chaos                      | 69.3 ms  | 35.4 ms: 1.96x faster  |
| raytrace                   | 313 ms   | 162 ms: 1.93x faster   |
| mako                       | 12.1 ms  | 6.25 ms: 1.93x faster  |
| coroutines                 | 22.4 ms  | 12.0 ms: 1.87x faster  |
| fannkuch                   | 418 ms   | 225 ms: 1.86x faster   |
| nbody                      | 103 ms   | 55.6 ms: 1.86x faster  |
| float                      | 78.0 ms  | 42.0 ms: 1.86x faster  |
| pickle_pure_python         | 364 us   | 199 us: 1.83x faster   |
| crypto_pyaes               | 80.1 ms  | 43.9 ms: 1.82x faster  |
| xml_etree_process          | 66.9 ms  | 36.8 ms: 1.82x faster  |
| pyflate                    | 477 ms   | 264 ms: 1.81x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 781 us: 1.80x faster   |
| scimark_fft                | 276 ms   | 153 ms: 1.80x faster   |
| tomli_loads                | 2.07 sec | 1.17 sec: 1.76x faster |
| nqueens                    | 96.9 ms  | 55.2 ms: 1.76x faster  |
| xml_etree_generate         | 92.6 ms  | 53.1 ms: 1.74x faster  |
| pprint_safe_repr           | 825 ms   | 474 ms: 1.74x faster   |
| pprint_pformat             | 1.66 sec | 956 ms: 1.74x faster   |
| async_generators           | 348 ms   | 201 ms: 1.73x faster   |
| deepcopy_reduce            | 2.86 us  | 1.68 us: 1.71x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 993 us: 1.70x faster   |
| genshi_text                | 23.9 ms  | 14.3 ms: 1.67x faster  |
| deepcopy                   | 278 us   | 167 us: 1.66x faster   |
| regex_compile              | 130 ms   | 79.4 ms: 1.64x faster  |
| bpe_tokeniser              | 4.45 sec | 2.72 sec: 1.63x faster |
| django_template            | 38.0 ms  | 23.6 ms: 1.61x faster  |
| json_loads                 | 23.3 us  | 14.5 us: 1.61x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 32.9 ms: 1.60x faster  |
| logging_simple             | 9.30 us  | 5.87 us: 1.58x faster  |
| sqlglot_v2_normalize       | 109 ms   | 69.0 ms: 1.58x faster  |
| typing_runtime_protocols   | 154 us   | 97.8 us: 1.57x faster  |
| async_tree_none            | 267 ms   | 170 ms: 1.57x faster   |
| genshi_xml                 | 50.4 ms  | 32.3 ms: 1.56x faster  |
| pathlib                    | 37.5 ms  | 24.2 ms: 1.55x faster  |
| logging_format             | 9.92 us  | 6.42 us: 1.55x faster  |
| xml_etree_iterparse        | 94.3 ms  | 61.2 ms: 1.54x faster  |
| gc_traversal               | 3.25 ms  | 2.12 ms: 1.54x faster  |
| async_tree_io_tg           | 576 ms   | 377 ms: 1.53x faster   |
| async_tree_memoization     | 313 ms   | 205 ms: 1.53x faster   |
| async_tree_none_tg         | 243 ms   | 161 ms: 1.51x faster   |
| async_tree_io              | 570 ms   | 382 ms: 1.49x faster   |
| sympy_expand               | 419 ms   | 283 ms: 1.48x faster   |
| json_dumps                 | 9.44 ms  | 6.40 ms: 1.48x faster  |
| pycparser                  | 1.01 sec | 689 ms: 1.47x faster   |
| async_tree_memoization_tg  | 304 ms   | 208 ms: 1.47x faster   |
| sphinx                     | 933 ms   | 641 ms: 1.45x faster   |
| sympy_sum                  | 123 ms   | 85.2 ms: 1.45x faster  |
| thrift                     | 710 us   | 491 us: 1.45x faster   |
| sympy_integrate            | 18.4 ms  | 12.8 ms: 1.44x faster  |
| 2to3                       | 309 ms   | 215 ms: 1.43x faster   |
| sympy_str                  | 247 ms   | 173 ms: 1.43x faster   |
| telco                      | 6.56 ms  | 4.59 ms: 1.43x faster  |
| meteor_contest             | 99.5 ms  | 70.9 ms: 1.40x faster  |
| docutils                   | 2.31 sec | 1.66 sec: 1.39x faster |
| html5lib                   | 52.5 ms  | 37.8 ms: 1.39x faster  |
| async_tree_cpu_io_mixed    | 455 ms   | 330 ms: 1.38x faster   |
| async_tree_cpu_io_mixed_tg | 444 ms   | 330 ms: 1.35x faster   |
| json                       | 4.07 ms  | 3.04 ms: 1.34x faster  |
| coverage                   | 63.7 ms  | 47.5 ms: 1.34x faster  |
| pylint                     | 269 ms   | 201 ms: 1.34x faster   |
| mdp                        | 1.89 sec | 1.43 sec: 1.32x faster |
| dulwich_log                | 52.4 ms  | 40.3 ms: 1.30x faster  |
| k_core                     | 2.18 sec | 1.70 sec: 1.28x faster |
| regex_effbot               | 1.87 ms  | 1.47 ms: 1.27x faster  |
| xml_etree_parse            | 112 ms   | 89.4 ms: 1.26x faster  |
| sqlite_synth               | 1.96 us  | 1.56 us: 1.25x faster  |
| shortest_path              | 437 ms   | 352 ms: 1.24x faster   |
| regex_v8                   | 17.5 ms  | 14.2 ms: 1.23x faster  |
| connected_components       | 395 ms   | 325 ms: 1.21x faster   |
| python_startup             | 29.5 ms  | 24.7 ms: 1.19x faster  |
| python_startup_no_site     | 22.0 ms  | 18.6 ms: 1.18x faster  |
| create_gc_cycles           | 1.42 ms  | 1.25 ms: 1.13x faster  |
| pidigits                   | 156 ms   | 145 ms: 1.08x faster   |
| asyncio_websockets         | 330 ms   | 313 ms: 1.06x faster   |
| regex_dna                  | 123 ms   | 120 ms: 1.03x faster   |
| many_optionals             | 559 us   | 685 us: 1.22x slower   |
| subparsers                 | 21.5 ms  | 41.4 ms: 1.92x slower  |
| Geometric mean             | (ref)    | 1.57x faster           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.560x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.48x
- 95% likely to have a speedup of 1.47x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown