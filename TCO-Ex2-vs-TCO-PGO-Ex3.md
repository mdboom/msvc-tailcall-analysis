# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.331x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 293 ms: 1.38x slower   |
| docutils       | 1.67 sec    | 2.11 sec: 1.27x slower |
| html5lib       | 37.9 ms     | 51.3 ms: 1.35x slower  |
| sphinx         | 645 ms      | 843 ms: 1.31x slower   |
| Geometric mean | (ref)       | 1.33x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 301 ms      | 311 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 428 ms: 1.30x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 434 ms: 1.31x slower  |
| async_tree_memoization_tg  | 208 ms      | 292 ms: 1.40x slower  |
| async_tree_io              | 384 ms      | 551 ms: 1.44x slower  |
| async_tree_memoization     | 206 ms      | 297 ms: 1.44x slower  |
| async_tree_none            | 170 ms      | 248 ms: 1.46x slower  |
| async_tree_none_tg         | 159 ms      | 236 ms: 1.48x slower  |
| async_tree_io_tg           | 377 ms      | 563 ms: 1.49x slower  |
| async_generators           | 202 ms      | 321 ms: 1.59x slower  |
| coroutines                 | 11.9 ms     | 22.1 ms: 1.85x slower |
| Geometric mean             | (ref)       | 1.42x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 148 ms: 1.02x slower  |
| float          | 41.9 ms     | 73.5 ms: 1.75x slower |
| nbody          | 55.2 ms     | 98.8 ms: 1.79x slower |
| Geometric mean | (ref)       | 1.47x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 118 ms: 1.03x faster  |
| regex_effbot   | 1.46 ms     | 1.77 ms: 1.21x slower |
| regex_v8       | 13.2 ms     | 17.0 ms: 1.28x slower |
| regex_compile  | 78.1 ms     | 123 ms: 1.57x slower  |
| Geometric mean | (ref)       | 1.24x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.3 ms     | 108 ms: 1.21x slower   |
| json_dumps           | 6.55 ms     | 8.99 ms: 1.37x slower  |
| xml_etree_iterparse  | 61.2 ms     | 87.5 ms: 1.43x slower  |
| json_loads           | 14.7 us     | 21.4 us: 1.45x slower  |
| xml_etree_generate   | 53.6 ms     | 87.5 ms: 1.63x slower  |
| tomli_loads          | 1.18 sec    | 1.97 sec: 1.67x slower |
| xml_etree_process    | 37.0 ms     | 63.0 ms: 1.70x slower  |
| pickle_pure_python   | 199 us      | 354 us: 1.78x slower   |
| unpickle_pure_python | 127 us      | 271 us: 2.13x slower   |
| Geometric mean       | (ref)       | 1.58x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TCO-Ex2               |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 20.3 ms: 1.09x slower |
| python_startup         | 24.7 ms     | 27.2 ms: 1.10x slower |
| Geometric mean         | (ref)       | 1.09x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TCO-Ex2               |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 48.8 ms: 1.49x slower |
| django_template | 22.9 ms     | 35.8 ms: 1.57x slower |
| genshi_text     | 14.3 ms     | 23.4 ms: 1.64x slower |
| mako            | 6.28 ms     | 11.4 ms: 1.82x slower |
| Geometric mean  | (ref)       | 1.62x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TCO-Ex2                |
|----------------------------|:-----------:|:----------------------:|
| regex_dna                  | 120 ms      | 118 ms: 1.03x faster   |
| pidigits                   | 145 ms      | 148 ms: 1.02x slower   |
| asyncio_websockets         | 301 ms      | 311 ms: 1.04x slower   |
| k_core                     | 1.71 sec    | 1.83 sec: 1.07x slower |
| connected_components       | 326 ms      | 351 ms: 1.08x slower   |
| python_startup_no_site     | 18.7 ms     | 20.3 ms: 1.09x slower  |
| shortest_path              | 353 ms      | 384 ms: 1.09x slower   |
| create_gc_cycles           | 1.27 ms     | 1.40 ms: 1.10x slower  |
| python_startup             | 24.7 ms     | 27.2 ms: 1.10x slower  |
| pathlib                    | 24.1 ms     | 26.8 ms: 1.11x slower  |
| mdp                        | 1.62 sec    | 1.82 sec: 1.13x slower |
| sqlite_synth               | 1.56 us     | 1.78 us: 1.14x slower  |
| xml_etree_parse            | 89.3 ms     | 108 ms: 1.21x slower   |
| regex_effbot               | 1.46 ms     | 1.77 ms: 1.21x slower  |
| subparsers                 | 40.7 ms     | 50.4 ms: 1.24x slower  |
| pylint                     | 198 ms      | 249 ms: 1.25x slower   |
| dulwich_log                | 40.2 ms     | 50.5 ms: 1.26x slower  |
| docutils                   | 1.67 sec    | 2.11 sec: 1.27x slower |
| coverage                   | 48.2 ms     | 61.1 ms: 1.27x slower  |
| regex_v8                   | 13.2 ms     | 17.0 ms: 1.28x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 428 ms: 1.30x slower   |
| sphinx                     | 645 ms      | 843 ms: 1.31x slower   |
| async_tree_cpu_io_mixed    | 330 ms      | 434 ms: 1.31x slower   |
| json                       | 2.97 ms     | 3.94 ms: 1.32x slower  |
| gc_traversal               | 2.11 ms     | 2.79 ms: 1.33x slower  |
| many_optionals             | 665 us      | 890 us: 1.34x slower   |
| html5lib                   | 37.9 ms     | 51.3 ms: 1.35x slower  |
| meteor_contest             | 70.2 ms     | 95.0 ms: 1.35x slower  |
| sympy_sum                  | 86.3 ms     | 118 ms: 1.36x slower   |
| sympy_integrate            | 12.8 ms     | 17.5 ms: 1.36x slower  |
| json_dumps                 | 6.55 ms     | 8.99 ms: 1.37x slower  |
| 2to3                       | 212 ms      | 293 ms: 1.38x slower   |
| telco                      | 4.57 ms     | 6.34 ms: 1.39x slower  |
| async_tree_memoization_tg  | 208 ms      | 292 ms: 1.40x slower   |
| logging_format             | 6.50 us     | 9.13 us: 1.41x slower  |
| thrift                     | 482 us      | 680 us: 1.41x slower   |
| pycparser                  | 686 ms      | 968 ms: 1.41x slower   |
| sympy_expand               | 282 ms      | 399 ms: 1.42x slower   |
| sympy_str                  | 164 ms      | 234 ms: 1.43x slower   |
| xml_etree_iterparse        | 61.2 ms     | 87.5 ms: 1.43x slower  |
| async_tree_io              | 384 ms      | 551 ms: 1.44x slower   |
| async_tree_memoization     | 206 ms      | 297 ms: 1.44x slower   |
| logging_simple             | 5.97 us     | 8.63 us: 1.44x slower  |
| json_loads                 | 14.7 us     | 21.4 us: 1.45x slower  |
| async_tree_none            | 170 ms      | 248 ms: 1.46x slower   |
| async_tree_none_tg         | 159 ms      | 236 ms: 1.48x slower   |
| typing_runtime_protocols   | 98.8 us     | 146 us: 1.48x slower   |
| genshi_xml                 | 32.8 ms     | 48.8 ms: 1.49x slower  |
| sqlglot_v2_normalize       | 69.3 ms     | 103 ms: 1.49x slower   |
| async_tree_io_tg           | 377 ms      | 563 ms: 1.49x slower   |
| sqlglot_v2_optimize        | 33.0 ms     | 49.6 ms: 1.50x slower  |
| django_template            | 22.9 ms     | 35.8 ms: 1.57x slower  |
| regex_compile              | 78.1 ms     | 123 ms: 1.57x slower   |
| bpe_tokeniser              | 2.72 sec    | 4.30 sec: 1.58x slower |
| async_generators           | 202 ms      | 321 ms: 1.59x slower   |
| deepcopy_reduce            | 1.70 us     | 2.71 us: 1.59x slower  |
| deepcopy                   | 167 us      | 266 us: 1.59x slower   |
| crypto_pyaes               | 47.4 ms     | 76.8 ms: 1.62x slower  |
| xml_etree_generate         | 53.6 ms     | 87.5 ms: 1.63x slower  |
| genshi_text                | 14.3 ms     | 23.4 ms: 1.64x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.62 ms: 1.67x slower  |
| pprint_pformat             | 967 ms      | 1.61 sec: 1.67x slower |
| tomli_loads                | 1.18 sec    | 1.97 sec: 1.67x slower |
| pprint_safe_repr           | 470 ms      | 789 ms: 1.68x slower   |
| xml_etree_process          | 37.0 ms     | 63.0 ms: 1.70x slower  |
| pyflate                    | 268 ms      | 457 ms: 1.70x slower   |
| nqueens                    | 54.4 ms     | 93.2 ms: 1.71x slower  |
| fannkuch                   | 223 ms      | 386 ms: 1.73x slower   |
| scimark_fft                | 154 ms      | 267 ms: 1.74x slower   |
| float                      | 41.9 ms     | 73.5 ms: 1.75x slower  |
| richards_super             | 33.1 ms     | 58.0 ms: 1.75x slower  |
| sqlglot_v2_parse           | 766 us      | 1.34 ms: 1.75x slower  |
| richards                   | 28.7 ms     | 51.0 ms: 1.77x slower  |
| pickle_pure_python         | 199 us      | 354 us: 1.78x slower   |
| nbody                      | 55.2 ms     | 98.8 ms: 1.79x slower  |
| chaos                      | 36.9 ms     | 67.0 ms: 1.82x slower  |
| mako                       | 6.28 ms     | 11.4 ms: 1.82x slower  |
| coroutines                 | 11.9 ms     | 22.1 ms: 1.85x slower  |
| scimark_sparse_mat_mult    | 2.27 ms     | 4.27 ms: 1.89x slower  |
| raytrace                   | 160 ms      | 306 ms: 1.91x slower   |
| go                         | 70.9 ms     | 138 ms: 1.95x slower   |
| spectral_norm              | 49.4 ms     | 97.1 ms: 1.97x slower  |
| comprehensions             | 9.87 us     | 19.4 us: 1.97x slower  |
| deepcopy_memo              | 16.6 us     | 33.0 us: 1.99x slower  |
| generators                 | 16.5 ms     | 33.5 ms: 2.03x slower  |
| hexiom                     | 3.54 ms     | 7.27 ms: 2.06x slower  |
| scimark_monte_carlo        | 36.0 ms     | 75.2 ms: 2.09x slower  |
| unpickle_pure_python       | 127 us      | 271 us: 2.13x slower   |
| deltablue                  | 1.88 ms     | 4.08 ms: 2.17x slower  |
| scimark_sor                | 61.1 ms     | 133 ms: 2.18x slower   |
| scimark_lu                 | 50.9 ms     | 116 ms: 2.27x slower   |
| logging_silent             | 49.4 ns     | 121 ns: 2.46x slower   |
| Geometric mean             | (ref)       | 1.50x slower           |
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.331x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.42x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: unknown