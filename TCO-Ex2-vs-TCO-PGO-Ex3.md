# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.332x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 293 ms: 1.36x slower   |
| docutils       | 1.66 sec    | 2.11 sec: 1.27x slower |
| html5lib       | 37.8 ms     | 51.3 ms: 1.36x slower  |
| sphinx         | 641 ms      | 843 ms: 1.31x slower   |
| Geometric mean | (ref)       | 1.33x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------------------|:-----------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 330 ms      | 428 ms: 1.30x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 434 ms: 1.32x slower  |
| async_tree_memoization_tg  | 208 ms      | 292 ms: 1.41x slower  |
| async_tree_io              | 382 ms      | 551 ms: 1.44x slower  |
| async_tree_memoization     | 205 ms      | 297 ms: 1.45x slower  |
| async_tree_none            | 170 ms      | 248 ms: 1.46x slower  |
| async_tree_none_tg         | 161 ms      | 236 ms: 1.47x slower  |
| async_tree_io_tg           | 377 ms      | 563 ms: 1.49x slower  |
| async_generators           | 201 ms      | 321 ms: 1.60x slower  |
| coroutines                 | 12.0 ms     | 22.1 ms: 1.85x slower |
| Geometric mean             | (ref)       | 1.42x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 148 ms: 1.02x slower  |
| float          | 42.0 ms     | 73.5 ms: 1.75x slower |
| nbody          | 55.6 ms     | 98.8 ms: 1.78x slower |
| Geometric mean | (ref)       | 1.47x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 118 ms: 1.02x faster  |
| regex_v8       | 14.2 ms     | 17.0 ms: 1.19x slower |
| regex_effbot   | 1.47 ms     | 1.77 ms: 1.21x slower |
| regex_compile  | 79.4 ms     | 123 ms: 1.55x slower  |
| Geometric mean | (ref)       | 1.22x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms     | 108 ms: 1.21x slower   |
| json_dumps           | 6.40 ms     | 8.99 ms: 1.40x slower  |
| xml_etree_iterparse  | 61.2 ms     | 87.5 ms: 1.43x slower  |
| json_loads           | 14.5 us     | 21.4 us: 1.48x slower  |
| xml_etree_generate   | 53.1 ms     | 87.5 ms: 1.65x slower  |
| tomli_loads          | 1.17 sec    | 1.97 sec: 1.67x slower |
| xml_etree_process    | 36.8 ms     | 63.0 ms: 1.71x slower  |
| pickle_pure_python   | 199 us      | 354 us: 1.78x slower   |
| unpickle_pure_python | 124 us      | 271 us: 2.19x slower   |
| Geometric mean       | (ref)       | 1.59x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TCO-Ex2               |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 20.3 ms: 1.09x slower |
| python_startup         | 24.7 ms     | 27.2 ms: 1.10x slower |
| Geometric mean         | (ref)       | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TCO-Ex2               |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.3 ms     | 48.8 ms: 1.51x slower |
| django_template | 23.6 ms     | 35.8 ms: 1.52x slower |
| genshi_text     | 14.3 ms     | 23.4 ms: 1.64x slower |
| mako            | 6.25 ms     | 11.4 ms: 1.83x slower |
| Geometric mean  | (ref)       | 1.62x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------------------|:-----------:|:----------------------:|
| regex_dna                  | 120 ms      | 118 ms: 1.02x faster   |
| pidigits                   | 145 ms      | 148 ms: 1.02x slower   |
| k_core                     | 1.70 sec    | 1.83 sec: 1.07x slower |
| connected_components       | 325 ms      | 351 ms: 1.08x slower   |
| shortest_path              | 352 ms      | 384 ms: 1.09x slower   |
| python_startup_no_site     | 18.6 ms     | 20.3 ms: 1.09x slower  |
| python_startup             | 24.7 ms     | 27.2 ms: 1.10x slower  |
| pathlib                    | 24.2 ms     | 26.8 ms: 1.11x slower  |
| create_gc_cycles           | 1.25 ms     | 1.40 ms: 1.12x slower  |
| sqlite_synth               | 1.56 us     | 1.78 us: 1.14x slower  |
| regex_v8                   | 14.2 ms     | 17.0 ms: 1.19x slower  |
| regex_effbot               | 1.47 ms     | 1.77 ms: 1.21x slower  |
| xml_etree_parse            | 89.4 ms     | 108 ms: 1.21x slower   |
| subparsers                 | 41.4 ms     | 50.4 ms: 1.22x slower  |
| pylint                     | 201 ms      | 249 ms: 1.24x slower   |
| dulwich_log                | 40.3 ms     | 50.5 ms: 1.25x slower  |
| docutils                   | 1.66 sec    | 2.11 sec: 1.27x slower |
| mdp                        | 1.43 sec    | 1.82 sec: 1.28x slower |
| coverage                   | 47.5 ms     | 61.1 ms: 1.29x slower  |
| json                       | 3.04 ms     | 3.94 ms: 1.30x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 428 ms: 1.30x slower   |
| many_optionals             | 685 us      | 890 us: 1.30x slower   |
| sphinx                     | 641 ms      | 843 ms: 1.31x slower   |
| async_tree_cpu_io_mixed    | 330 ms      | 434 ms: 1.32x slower   |
| gc_traversal               | 2.12 ms     | 2.79 ms: 1.32x slower  |
| meteor_contest             | 70.9 ms     | 95.0 ms: 1.34x slower  |
| sympy_str                  | 173 ms      | 234 ms: 1.35x slower   |
| html5lib                   | 37.8 ms     | 51.3 ms: 1.36x slower  |
| 2to3                       | 215 ms      | 293 ms: 1.36x slower   |
| sympy_integrate            | 12.8 ms     | 17.5 ms: 1.37x slower  |
| telco                      | 4.59 ms     | 6.34 ms: 1.38x slower  |
| sympy_sum                  | 85.2 ms     | 118 ms: 1.38x slower   |
| thrift                     | 491 us      | 680 us: 1.39x slower   |
| json_dumps                 | 6.40 ms     | 8.99 ms: 1.40x slower  |
| pycparser                  | 689 ms      | 968 ms: 1.40x slower   |
| async_tree_memoization_tg  | 208 ms      | 292 ms: 1.41x slower   |
| sympy_expand               | 283 ms      | 399 ms: 1.41x slower   |
| logging_format             | 6.42 us     | 9.13 us: 1.42x slower  |
| xml_etree_iterparse        | 61.2 ms     | 87.5 ms: 1.43x slower  |
| async_tree_io              | 382 ms      | 551 ms: 1.44x slower   |
| async_tree_memoization     | 205 ms      | 297 ms: 1.45x slower   |
| async_tree_none            | 170 ms      | 248 ms: 1.46x slower   |
| async_tree_none_tg         | 161 ms      | 236 ms: 1.47x slower   |
| logging_simple             | 5.87 us     | 8.63 us: 1.47x slower  |
| json_loads                 | 14.5 us     | 21.4 us: 1.48x slower  |
| async_tree_io_tg           | 377 ms      | 563 ms: 1.49x slower   |
| typing_runtime_protocols   | 97.8 us     | 146 us: 1.50x slower   |
| sqlglot_v2_normalize       | 69.0 ms     | 103 ms: 1.50x slower   |
| sqlglot_v2_optimize        | 32.9 ms     | 49.6 ms: 1.50x slower  |
| genshi_xml                 | 32.3 ms     | 48.8 ms: 1.51x slower  |
| django_template            | 23.6 ms     | 35.8 ms: 1.52x slower  |
| regex_compile              | 79.4 ms     | 123 ms: 1.55x slower   |
| bpe_tokeniser              | 2.72 sec    | 4.30 sec: 1.58x slower |
| deepcopy                   | 167 us      | 266 us: 1.59x slower   |
| async_generators           | 201 ms      | 321 ms: 1.60x slower   |
| deepcopy_reduce            | 1.68 us     | 2.71 us: 1.62x slower  |
| sqlglot_v2_transpile       | 993 us      | 1.62 ms: 1.63x slower  |
| genshi_text                | 14.3 ms     | 23.4 ms: 1.64x slower  |
| xml_etree_generate         | 53.1 ms     | 87.5 ms: 1.65x slower  |
| pprint_safe_repr           | 474 ms      | 789 ms: 1.66x slower   |
| tomli_loads                | 1.17 sec    | 1.97 sec: 1.67x slower |
| nqueens                    | 55.2 ms     | 93.2 ms: 1.69x slower  |
| pprint_pformat             | 956 ms      | 1.61 sec: 1.69x slower |
| xml_etree_process          | 36.8 ms     | 63.0 ms: 1.71x slower  |
| fannkuch                   | 225 ms      | 386 ms: 1.72x slower   |
| sqlglot_v2_parse           | 781 us      | 1.34 ms: 1.72x slower  |
| richards_super             | 33.7 ms     | 58.0 ms: 1.72x slower  |
| pyflate                    | 264 ms      | 457 ms: 1.73x slower   |
| richards                   | 29.4 ms     | 51.0 ms: 1.74x slower  |
| scimark_fft                | 153 ms      | 267 ms: 1.74x slower   |
| crypto_pyaes               | 43.9 ms     | 76.8 ms: 1.75x slower  |
| float                      | 42.0 ms     | 73.5 ms: 1.75x slower  |
| nbody                      | 55.6 ms     | 98.8 ms: 1.78x slower  |
| pickle_pure_python         | 199 us      | 354 us: 1.78x slower   |
| mako                       | 6.25 ms     | 11.4 ms: 1.83x slower  |
| coroutines                 | 12.0 ms     | 22.1 ms: 1.85x slower  |
| chaos                      | 35.4 ms     | 67.0 ms: 1.89x slower  |
| raytrace                   | 162 ms      | 306 ms: 1.89x slower   |
| scimark_sparse_mat_mult    | 2.21 ms     | 4.27 ms: 1.93x slower  |
| deepcopy_memo              | 16.8 us     | 33.0 us: 1.96x slower  |
| go                         | 70.5 ms     | 138 ms: 1.96x slower   |
| spectral_norm              | 49.4 ms     | 97.1 ms: 1.96x slower  |
| comprehensions             | 9.76 us     | 19.4 us: 1.99x slower  |
| generators                 | 16.5 ms     | 33.5 ms: 2.03x slower  |
| hexiom                     | 3.49 ms     | 7.27 ms: 2.08x slower  |
| scimark_monte_carlo        | 35.6 ms     | 75.2 ms: 2.11x slower  |
| deltablue                  | 1.88 ms     | 4.08 ms: 2.16x slower  |
| unpickle_pure_python       | 124 us      | 271 us: 2.19x slower   |
| scimark_sor                | 60.5 ms     | 133 ms: 2.20x slower   |
| scimark_lu                 | 50.3 ms     | 116 ms: 2.30x slower   |
| logging_silent             | 49.7 ns     | 121 ns: 2.45x slower   |
| Geometric mean             | (ref)       | 1.51x slower           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.332x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.41x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.37x

# Memory
- memory change: unknown