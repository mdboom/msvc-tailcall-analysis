# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.559x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 212 ms: 1.46x faster   |
| docutils       | 2.31 sec | 1.67 sec: 1.38x faster |
| html5lib       | 52.5 ms  | 37.9 ms: 1.38x faster  |
| sphinx         | 933 ms   | 645 ms: 1.45x faster   |
| Geometric mean | (ref)    | 1.42x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 11.9 ms: 1.88x faster |
| async_generators           | 348 ms  | 202 ms: 1.72x faster  |
| async_tree_none            | 267 ms  | 170 ms: 1.57x faster  |
| async_tree_none_tg         | 243 ms  | 159 ms: 1.53x faster  |
| async_tree_io_tg           | 576 ms  | 377 ms: 1.53x faster  |
| async_tree_memoization     | 313 ms  | 206 ms: 1.52x faster  |
| async_tree_io              | 570 ms  | 384 ms: 1.48x faster  |
| async_tree_memoization_tg  | 304 ms  | 208 ms: 1.46x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 330 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 329 ms: 1.35x faster  |
| asyncio_websockets         | 330 ms  | 301 ms: 1.10x faster  |
| Geometric mean             | (ref)   | 1.49x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 55.2 ms: 1.87x faster |
| float          | 78.0 ms | 41.9 ms: 1.86x faster |
| pidigits       | 156 ms  | 145 ms: 1.08x faster  |
| Geometric mean | (ref)   | 1.55x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 78.1 ms: 1.66x faster |
| regex_v8       | 17.5 ms | 13.2 ms: 1.32x faster |
| regex_effbot   | 1.87 ms | 1.46 ms: 1.28x faster |
| regex_dna      | 123 ms  | 120 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.30x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 127 us: 2.23x faster   |
| pickle_pure_python   | 364 us   | 199 us: 1.83x faster   |
| xml_etree_process    | 66.9 ms  | 37.0 ms: 1.81x faster  |
| tomli_loads          | 2.07 sec | 1.18 sec: 1.76x faster |
| xml_etree_generate   | 92.6 ms  | 53.6 ms: 1.73x faster  |
| json_loads           | 23.3 us  | 14.7 us: 1.58x faster  |
| xml_etree_iterparse  | 94.3 ms  | 61.2 ms: 1.54x faster  |
| json_dumps           | 9.44 ms  | 6.55 ms: 1.44x faster  |
| xml_etree_parse      | 112 ms   | 89.3 ms: 1.26x faster  |
| Geometric mean       | (ref)    | 1.67x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 24.7 ms: 1.19x faster |
| python_startup_no_site | 22.0 ms | 18.7 ms: 1.18x faster |
| Geometric mean         | (ref)   | 1.18x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.28 ms: 1.92x faster |
| genshi_text     | 23.9 ms | 14.3 ms: 1.67x faster |
| django_template | 38.0 ms | 22.9 ms: 1.66x faster |
| genshi_xml      | 50.4 ms | 32.8 ms: 1.54x faster |
| Geometric mean  | (ref)   | 1.69x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 49.4 ns: 2.51x faster  |
| scimark_lu                 | 119 ms   | 50.9 ms: 2.35x faster  |
| scimark_sor                | 139 ms   | 61.1 ms: 2.27x faster  |
| deltablue                  | 4.22 ms  | 1.88 ms: 2.25x faster  |
| unpickle_pure_python       | 284 us   | 127 us: 2.23x faster   |
| generators                 | 35.6 ms  | 16.5 ms: 2.16x faster  |
| scimark_monte_carlo        | 75.8 ms  | 36.0 ms: 2.11x faster  |
| hexiom                     | 7.44 ms  | 3.54 ms: 2.10x faster  |
| spectral_norm              | 102 ms   | 49.4 ms: 2.06x faster  |
| richards                   | 59.0 ms  | 28.7 ms: 2.05x faster  |
| deepcopy_memo              | 34.0 us  | 16.6 us: 2.05x faster  |
| richards_super             | 67.7 ms  | 33.1 ms: 2.05x faster  |
| comprehensions             | 20.1 us  | 9.87 us: 2.04x faster  |
| go                         | 140 ms   | 70.9 ms: 1.98x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.27 ms: 1.96x faster  |
| raytrace                   | 313 ms   | 160 ms: 1.95x faster   |
| mako                       | 12.1 ms  | 6.28 ms: 1.92x faster  |
| coroutines                 | 22.4 ms  | 11.9 ms: 1.88x faster  |
| chaos                      | 69.3 ms  | 36.9 ms: 1.88x faster  |
| fannkuch                   | 418 ms   | 223 ms: 1.88x faster   |
| nbody                      | 103 ms   | 55.2 ms: 1.87x faster  |
| float                      | 78.0 ms  | 41.9 ms: 1.86x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 766 us: 1.84x faster   |
| pickle_pure_python         | 364 us   | 199 us: 1.83x faster   |
| xml_etree_process          | 66.9 ms  | 37.0 ms: 1.81x faster  |
| scimark_fft                | 276 ms   | 154 ms: 1.79x faster   |
| nqueens                    | 96.9 ms  | 54.4 ms: 1.78x faster  |
| pyflate                    | 477 ms   | 268 ms: 1.78x faster   |
| tomli_loads                | 2.07 sec | 1.18 sec: 1.76x faster |
| pprint_safe_repr           | 825 ms   | 470 ms: 1.76x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 970 us: 1.74x faster   |
| xml_etree_generate         | 92.6 ms  | 53.6 ms: 1.73x faster  |
| async_generators           | 348 ms   | 202 ms: 1.72x faster   |
| pprint_pformat             | 1.66 sec | 967 ms: 1.72x faster   |
| crypto_pyaes               | 80.1 ms  | 47.4 ms: 1.69x faster  |
| deepcopy_reduce            | 2.86 us  | 1.70 us: 1.69x faster  |
| genshi_text                | 23.9 ms  | 14.3 ms: 1.67x faster  |
| deepcopy                   | 278 us   | 167 us: 1.67x faster   |
| django_template            | 38.0 ms  | 22.9 ms: 1.66x faster  |
| regex_compile              | 130 ms   | 78.1 ms: 1.66x faster  |
| bpe_tokeniser              | 4.45 sec | 2.72 sec: 1.64x faster |
| sqlglot_v2_optimize        | 52.8 ms  | 33.0 ms: 1.60x faster  |
| json_loads                 | 23.3 us  | 14.7 us: 1.58x faster  |
| sqlglot_v2_normalize       | 109 ms   | 69.3 ms: 1.57x faster  |
| async_tree_none            | 267 ms   | 170 ms: 1.57x faster   |
| typing_runtime_protocols   | 154 us   | 98.8 us: 1.56x faster  |
| pathlib                    | 37.5 ms  | 24.1 ms: 1.56x faster  |
| logging_simple             | 9.30 us  | 5.97 us: 1.56x faster  |
| gc_traversal               | 3.25 ms  | 2.11 ms: 1.54x faster  |
| xml_etree_iterparse        | 94.3 ms  | 61.2 ms: 1.54x faster  |
| genshi_xml                 | 50.4 ms  | 32.8 ms: 1.54x faster  |
| async_tree_none_tg         | 243 ms   | 159 ms: 1.53x faster   |
| async_tree_io_tg           | 576 ms   | 377 ms: 1.53x faster   |
| logging_format             | 9.92 us  | 6.50 us: 1.53x faster  |
| async_tree_memoization     | 313 ms   | 206 ms: 1.52x faster   |
| sympy_str                  | 247 ms   | 164 ms: 1.51x faster   |
| sympy_expand               | 419 ms   | 282 ms: 1.49x faster   |
| async_tree_io              | 570 ms   | 384 ms: 1.48x faster   |
| pycparser                  | 1.01 sec | 686 ms: 1.48x faster   |
| thrift                     | 710 us   | 482 us: 1.47x faster   |
| async_tree_memoization_tg  | 304 ms   | 208 ms: 1.46x faster   |
| 2to3                       | 309 ms   | 212 ms: 1.46x faster   |
| sphinx                     | 933 ms   | 645 ms: 1.45x faster   |
| json_dumps                 | 9.44 ms  | 6.55 ms: 1.44x faster  |
| telco                      | 6.56 ms  | 4.57 ms: 1.44x faster  |
| sympy_integrate            | 18.4 ms  | 12.8 ms: 1.43x faster  |
| sympy_sum                  | 123 ms   | 86.3 ms: 1.43x faster  |
| meteor_contest             | 99.5 ms  | 70.2 ms: 1.42x faster  |
| docutils                   | 2.31 sec | 1.67 sec: 1.38x faster |
| html5lib                   | 52.5 ms  | 37.9 ms: 1.38x faster  |
| async_tree_cpu_io_mixed    | 455 ms   | 330 ms: 1.38x faster   |
| json                       | 4.07 ms  | 2.97 ms: 1.37x faster  |
| pylint                     | 269 ms   | 198 ms: 1.35x faster   |
| async_tree_cpu_io_mixed_tg | 444 ms   | 329 ms: 1.35x faster   |
| regex_v8                   | 17.5 ms  | 13.2 ms: 1.32x faster  |
| coverage                   | 63.7 ms  | 48.2 ms: 1.32x faster  |
| dulwich_log                | 52.4 ms  | 40.2 ms: 1.30x faster  |
| regex_effbot               | 1.87 ms  | 1.46 ms: 1.28x faster  |
| k_core                     | 2.18 sec | 1.71 sec: 1.28x faster |
| xml_etree_parse            | 112 ms   | 89.3 ms: 1.26x faster  |
| sqlite_synth               | 1.96 us  | 1.56 us: 1.25x faster  |
| shortest_path              | 437 ms   | 353 ms: 1.24x faster   |
| connected_components       | 395 ms   | 326 ms: 1.21x faster   |
| python_startup             | 29.5 ms  | 24.7 ms: 1.19x faster  |
| python_startup_no_site     | 22.0 ms  | 18.7 ms: 1.18x faster  |
| mdp                        | 1.89 sec | 1.62 sec: 1.17x faster |
| create_gc_cycles           | 1.42 ms  | 1.27 ms: 1.12x faster  |
| asyncio_websockets         | 330 ms   | 301 ms: 1.10x faster   |
| pidigits                   | 156 ms   | 145 ms: 1.08x faster   |
| regex_dna                  | 123 ms   | 120 ms: 1.02x faster   |
| many_optionals             | 559 us   | 665 us: 1.19x slower   |
| subparsers                 | 21.5 ms  | 40.7 ms: 1.89x slower  |
| Geometric mean             | (ref)    | 1.57x faster           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.559x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.49x
- 95% likely to have a speedup of 1.48x
- 99% likely to have a speedup of 1.46x

# Memory
- memory change: unknown