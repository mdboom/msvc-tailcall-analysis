# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.547x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TC-MostPGO-Ex          |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 209 ms: 1.48x faster   |
| docutils       | 2.31 sec | 1.74 sec: 1.32x faster |
| html5lib       | 52.5 ms  | 37.2 ms: 1.41x faster  |
| sphinx         | 933 ms   | 666 ms: 1.40x faster   |
| Geometric mean | (ref)    | 1.40x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TC-MostPGO-Ex         |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 11.8 ms: 1.90x faster |
| async_generators           | 348 ms  | 202 ms: 1.73x faster  |
| async_tree_none            | 267 ms  | 165 ms: 1.62x faster  |
| async_tree_memoization     | 313 ms  | 202 ms: 1.55x faster  |
| async_tree_io_tg           | 576 ms  | 374 ms: 1.54x faster  |
| async_tree_none_tg         | 243 ms  | 160 ms: 1.52x faster  |
| async_tree_io              | 570 ms  | 374 ms: 1.52x faster  |
| async_tree_memoization_tg  | 304 ms  | 209 ms: 1.45x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 332 ms: 1.37x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 331 ms: 1.34x faster  |
| asyncio_websockets         | 330 ms  | 315 ms: 1.05x faster  |
| Geometric mean             | (ref)   | 1.49x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 53.0 ms: 1.95x faster |
| float          | 78.0 ms | 40.4 ms: 1.93x faster |
| pidigits       | 156 ms  | 151 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.57x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 79.3 ms: 1.64x faster |
| regex_effbot   | 1.87 ms | 1.53 ms: 1.22x faster |
| regex_v8       | 17.5 ms | 15.3 ms: 1.15x faster |
| regex_dna      | 123 ms  | 125 ms: 1.01x slower  |
| Geometric mean | (ref)   | 1.23x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TC-MostPGO-Ex          |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 123 us: 2.31x faster   |
| pickle_pure_python   | 364 us   | 195 us: 1.86x faster   |
| xml_etree_process    | 66.9 ms  | 37.9 ms: 1.77x faster  |
| tomli_loads          | 2.07 sec | 1.18 sec: 1.75x faster |
| xml_etree_generate   | 92.6 ms  | 54.3 ms: 1.71x faster  |
| xml_etree_iterparse  | 94.3 ms  | 64.2 ms: 1.47x faster  |
| json_loads           | 23.3 us  | 15.8 us: 1.47x faster  |
| json_dumps           | 9.44 ms  | 6.84 ms: 1.38x faster  |
| xml_etree_parse      | 112 ms   | 92.6 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.63x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TC-MostPGO-Ex         |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.4 ms: 1.12x faster |
| python_startup_no_site | 22.0 ms | 19.9 ms: 1.11x faster |
| Geometric mean         | (ref)   | 1.11x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TC-MostPGO-Ex         |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.50 ms: 1.86x faster |
| genshi_text     | 23.9 ms | 14.1 ms: 1.70x faster |
| django_template | 38.0 ms | 22.9 ms: 1.66x faster |
| genshi_xml      | 50.4 ms | 31.3 ms: 1.61x faster |
| Geometric mean  | (ref)   | 1.70x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TC-MostPGO-Ex          |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 53.0 ns: 2.34x faster  |
| unpickle_pure_python       | 284 us   | 123 us: 2.31x faster   |
| deltablue                  | 4.22 ms  | 1.87 ms: 2.25x faster  |
| scimark_sor                | 139 ms   | 63.1 ms: 2.20x faster  |
| spectral_norm              | 102 ms   | 46.7 ms: 2.18x faster  |
| generators                 | 35.6 ms  | 16.3 ms: 2.17x faster  |
| scimark_lu                 | 119 ms   | 55.5 ms: 2.15x faster  |
| scimark_monte_carlo        | 75.8 ms  | 35.5 ms: 2.13x faster  |
| richards_super             | 67.7 ms  | 32.0 ms: 2.11x faster  |
| richards                   | 59.0 ms  | 28.1 ms: 2.10x faster  |
| comprehensions             | 20.1 us  | 9.60 us: 2.09x faster  |
| hexiom                     | 7.44 ms  | 3.58 ms: 2.08x faster  |
| go                         | 140 ms   | 68.6 ms: 2.05x faster  |
| chaos                      | 69.3 ms  | 34.2 ms: 2.03x faster  |
| deepcopy_memo              | 34.0 us  | 17.0 us: 2.00x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.25 ms: 1.97x faster  |
| nbody                      | 103 ms   | 53.0 ms: 1.95x faster  |
| raytrace                   | 313 ms   | 162 ms: 1.93x faster   |
| float                      | 78.0 ms  | 40.4 ms: 1.93x faster  |
| crypto_pyaes               | 80.1 ms  | 41.7 ms: 1.92x faster  |
| coroutines                 | 22.4 ms  | 11.8 ms: 1.90x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 742 us: 1.89x faster   |
| pickle_pure_python         | 364 us   | 195 us: 1.86x faster   |
| mako                       | 12.1 ms  | 6.50 ms: 1.86x faster  |
| scimark_fft                | 276 ms   | 151 ms: 1.83x faster   |
| pyflate                    | 477 ms   | 264 ms: 1.81x faster   |
| fannkuch                   | 418 ms   | 233 ms: 1.79x faster   |
| nqueens                    | 96.9 ms  | 54.2 ms: 1.79x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 943 us: 1.79x faster   |
| xml_etree_process          | 66.9 ms  | 37.9 ms: 1.77x faster  |
| deepcopy                   | 278 us   | 159 us: 1.75x faster   |
| tomli_loads                | 2.07 sec | 1.18 sec: 1.75x faster |
| async_generators           | 348 ms   | 202 ms: 1.73x faster   |
| pprint_pformat             | 1.66 sec | 963 ms: 1.72x faster   |
| pprint_safe_repr           | 825 ms   | 481 ms: 1.72x faster   |
| xml_etree_generate         | 92.6 ms  | 54.3 ms: 1.71x faster  |
| genshi_text                | 23.9 ms  | 14.1 ms: 1.70x faster  |
| deepcopy_reduce            | 2.86 us  | 1.69 us: 1.70x faster  |
| bpe_tokeniser              | 4.45 sec | 2.67 sec: 1.66x faster |
| django_template            | 38.0 ms  | 22.9 ms: 1.66x faster  |
| regex_compile              | 130 ms   | 79.3 ms: 1.64x faster  |
| sqlglot_v2_normalize       | 109 ms   | 66.7 ms: 1.64x faster  |
| async_tree_none            | 267 ms   | 165 ms: 1.62x faster   |
| genshi_xml                 | 50.4 ms  | 31.3 ms: 1.61x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 33.0 ms: 1.60x faster  |
| logging_simple             | 9.30 us  | 5.84 us: 1.59x faster  |
| typing_runtime_protocols   | 154 us   | 98.1 us: 1.57x faster  |
| bench_thread_pool          | 1.28 ms  | 819 us: 1.56x faster   |
| logging_format             | 9.92 us  | 6.39 us: 1.55x faster  |
| async_tree_memoization     | 313 ms   | 202 ms: 1.55x faster   |
| async_tree_io_tg           | 576 ms   | 374 ms: 1.54x faster   |
| async_tree_none_tg         | 243 ms   | 160 ms: 1.52x faster   |
| async_tree_io              | 570 ms   | 374 ms: 1.52x faster   |
| sympy_str                  | 247 ms   | 163 ms: 1.52x faster   |
| sympy_expand               | 419 ms   | 279 ms: 1.50x faster   |
| 2to3                       | 309 ms   | 209 ms: 1.48x faster   |
| pycparser                  | 1.01 sec | 688 ms: 1.47x faster   |
| pathlib                    | 37.5 ms  | 25.5 ms: 1.47x faster  |
| gc_traversal               | 3.25 ms  | 2.21 ms: 1.47x faster  |
| xml_etree_iterparse        | 94.3 ms  | 64.2 ms: 1.47x faster  |
| json_loads                 | 23.3 us  | 15.8 us: 1.47x faster  |
| thrift                     | 710 us   | 487 us: 1.46x faster   |
| async_tree_memoization_tg  | 304 ms   | 209 ms: 1.45x faster   |
| sympy_integrate            | 18.4 ms  | 12.9 ms: 1.43x faster  |
| telco                      | 6.56 ms  | 4.60 ms: 1.43x faster  |
| html5lib                   | 52.5 ms  | 37.2 ms: 1.41x faster  |
| sympy_sum                  | 123 ms   | 88.0 ms: 1.40x faster  |
| sphinx                     | 933 ms   | 666 ms: 1.40x faster   |
| json_dumps                 | 9.44 ms  | 6.84 ms: 1.38x faster  |
| coverage                   | 63.7 ms  | 46.2 ms: 1.38x faster  |
| meteor_contest             | 99.5 ms  | 72.3 ms: 1.38x faster  |
| async_tree_cpu_io_mixed    | 455 ms   | 332 ms: 1.37x faster   |
| async_tree_cpu_io_mixed_tg | 444 ms   | 331 ms: 1.34x faster   |
| pylint                     | 269 ms   | 202 ms: 1.33x faster   |
| docutils                   | 2.31 sec | 1.74 sec: 1.32x faster |
| json                       | 4.07 ms  | 3.16 ms: 1.29x faster  |
| dulwich_log                | 52.4 ms  | 41.5 ms: 1.26x faster  |
| sqlite_synth               | 1.96 us  | 1.56 us: 1.25x faster  |
| regex_effbot               | 1.87 ms  | 1.53 ms: 1.22x faster  |
| xml_etree_parse            | 112 ms   | 92.6 ms: 1.21x faster  |
| mdp                        | 1.89 sec | 1.56 sec: 1.21x faster |
| regex_v8                   | 17.5 ms  | 15.3 ms: 1.15x faster  |
| bench_mp_pool              | 101 ms   | 88.6 ms: 1.14x faster  |
| python_startup             | 29.5 ms  | 26.4 ms: 1.12x faster  |
| python_startup_no_site     | 22.0 ms  | 19.9 ms: 1.11x faster  |
| shortest_path              | 437 ms   | 399 ms: 1.10x faster   |
| k_core                     | 2.18 sec | 2.00 sec: 1.09x faster |
| connected_components       | 395 ms   | 366 ms: 1.08x faster   |
| create_gc_cycles           | 1.42 ms  | 1.35 ms: 1.05x faster  |
| asyncio_websockets         | 330 ms   | 315 ms: 1.05x faster   |
| pidigits                   | 156 ms   | 151 ms: 1.03x faster   |
| regex_dna                  | 123 ms   | 125 ms: 1.01x slower   |
| many_optionals             | 559 us   | 669 us: 1.20x slower   |
| subparsers                 | 21.5 ms  | 41.2 ms: 1.91x slower  |
| Geometric mean             | (ref)    | 1.55x faster           |

- Geometric mean (including insignificant results): 1.547x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.49x
- 95% likely to have a speedup of 1.47x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown