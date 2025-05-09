# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.272x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 293 ms: 1.29x slower   |
| docutils       | 1.68 sec | 2.11 sec: 1.25x slower |
| html5lib       | 40.8 ms  | 51.3 ms: 1.26x slower  |
| sphinx         | 658 ms   | 843 ms: 1.28x slower   |
| Geometric mean | (ref)    | 1.27x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 318 ms  | 311 ms: 1.02x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 428 ms: 1.25x slower  |
| async_tree_cpu_io_mixed    | 339 ms  | 434 ms: 1.28x slower  |
| async_tree_io              | 423 ms  | 551 ms: 1.30x slower  |
| async_tree_memoization     | 224 ms  | 297 ms: 1.32x slower  |
| async_tree_none            | 187 ms  | 248 ms: 1.33x slower  |
| async_tree_none_tg         | 176 ms  | 236 ms: 1.34x slower  |
| async_tree_memoization_tg  | 216 ms  | 292 ms: 1.35x slower  |
| async_tree_io_tg           | 410 ms  | 563 ms: 1.37x slower  |
| async_generators           | 226 ms  | 321 ms: 1.42x slower  |
| coroutines                 | 13.5 ms | 22.1 ms: 1.64x slower |
| Geometric mean             | (ref)   | 1.32x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| pidigits       | 152 ms  | 148 ms: 1.03x faster  |
| nbody          | 74.1 ms | 98.8 ms: 1.33x slower |
| float          | 47.8 ms | 73.5 ms: 1.54x slower |
| Geometric mean | (ref)   | 1.26x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_dna      | 112 ms  | 118 ms: 1.05x slower  |
| regex_effbot   | 1.42 ms | 1.77 ms: 1.25x slower |
| regex_v8       | 13.5 ms | 17.0 ms: 1.25x slower |
| regex_compile  | 88.2 ms | 123 ms: 1.39x slower  |
| Geometric mean | (ref)   | 1.23x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 91.2 ms  | 108 ms: 1.18x slower   |
| json_dumps           | 7.05 ms  | 8.99 ms: 1.28x slower  |
| tomli_loads          | 1.47 sec | 1.97 sec: 1.34x slower |
| xml_etree_iterparse  | 63.7 ms  | 87.5 ms: 1.37x slower  |
| json_loads           | 14.7 us  | 21.4 us: 1.46x slower  |
| xml_etree_generate   | 58.7 ms  | 87.5 ms: 1.49x slower  |
| pickle_pure_python   | 237 us   | 354 us: 1.50x slower   |
| xml_etree_process    | 41.5 ms  | 63.0 ms: 1.52x slower  |
| unpickle_pure_python | 155 us   | 271 us: 1.75x slower   |
| Geometric mean       | (ref)    | 1.42x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TCO-Ex2               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 20.3 ms: 1.02x slower |
| python_startup         | 26.1 ms | 27.2 ms: 1.05x slower |
| Geometric mean         | (ref)   | 1.03x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 36.3 ms | 48.8 ms: 1.34x slower |
| genshi_text     | 16.5 ms | 23.4 ms: 1.42x slower |
| django_template | 25.1 ms | 35.8 ms: 1.43x slower |
| mako            | 6.86 ms | 11.4 ms: 1.67x slower |
| Geometric mean  | (ref)   | 1.46x slower          |

All benchmarks:
===============

| Benchmark                  | PGO      | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| pathlib                    | 32.1 ms  | 26.8 ms: 1.20x faster  |
| pidigits                   | 152 ms   | 148 ms: 1.03x faster   |
| asyncio_websockets         | 318 ms   | 311 ms: 1.02x faster   |
| python_startup_no_site     | 19.8 ms  | 20.3 ms: 1.02x slower  |
| python_startup             | 26.1 ms  | 27.2 ms: 1.05x slower  |
| regex_dna                  | 112 ms   | 118 ms: 1.05x slower   |
| k_core                     | 1.73 sec | 1.83 sec: 1.06x slower |
| connected_components       | 329 ms   | 351 ms: 1.06x slower   |
| shortest_path              | 359 ms   | 384 ms: 1.07x slower   |
| bench_mp_pool              | 88.7 ms  | 97.6 ms: 1.10x slower  |
| mdp                        | 1.64 sec | 1.82 sec: 1.11x slower |
| create_gc_cycles           | 1.25 ms  | 1.40 ms: 1.12x slower  |
| sqlite_synth               | 1.59 us  | 1.78 us: 1.12x slower  |
| dulwich_log                | 43.4 ms  | 50.5 ms: 1.16x slower  |
| bench_thread_pool          | 864 us   | 1.01 ms: 1.17x slower  |
| xml_etree_parse            | 91.2 ms  | 108 ms: 1.18x slower   |
| meteor_contest             | 76.9 ms  | 95.0 ms: 1.24x slower  |
| pylint                     | 201 ms   | 249 ms: 1.24x slower   |
| regex_effbot               | 1.42 ms  | 1.77 ms: 1.25x slower  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 428 ms: 1.25x slower   |
| regex_v8                   | 13.5 ms  | 17.0 ms: 1.25x slower  |
| docutils                   | 1.68 sec | 2.11 sec: 1.25x slower |
| json                       | 3.14 ms  | 3.94 ms: 1.25x slower  |
| html5lib                   | 40.8 ms  | 51.3 ms: 1.26x slower  |
| json_dumps                 | 7.05 ms  | 8.99 ms: 1.28x slower  |
| async_tree_cpu_io_mixed    | 339 ms   | 434 ms: 1.28x slower   |
| sphinx                     | 658 ms   | 843 ms: 1.28x slower   |
| 2to3                       | 227 ms   | 293 ms: 1.29x slower   |
| sympy_integrate            | 13.5 ms  | 17.5 ms: 1.30x slower  |
| telco                      | 4.89 ms  | 6.34 ms: 1.30x slower  |
| logging_format             | 7.03 us  | 9.13 us: 1.30x slower  |
| sympy_sum                  | 90.5 ms  | 118 ms: 1.30x slower   |
| async_tree_io              | 423 ms   | 551 ms: 1.30x slower   |
| fannkuch                   | 296 ms   | 386 ms: 1.30x slower   |
| coverage                   | 46.8 ms  | 61.1 ms: 1.30x slower  |
| pycparser                  | 738 ms   | 968 ms: 1.31x slower   |
| logging_simple             | 6.53 us  | 8.63 us: 1.32x slower  |
| sympy_expand               | 302 ms   | 399 ms: 1.32x slower   |
| async_tree_memoization     | 224 ms   | 297 ms: 1.32x slower   |
| async_tree_none            | 187 ms   | 248 ms: 1.33x slower   |
| sympy_str                  | 176 ms   | 234 ms: 1.33x slower   |
| nbody                      | 74.1 ms  | 98.8 ms: 1.33x slower  |
| async_tree_none_tg         | 176 ms   | 236 ms: 1.34x slower   |
| tomli_loads                | 1.47 sec | 1.97 sec: 1.34x slower |
| thrift                     | 507 us   | 680 us: 1.34x slower   |
| genshi_xml                 | 36.3 ms  | 48.8 ms: 1.34x slower  |
| async_tree_memoization_tg  | 216 ms   | 292 ms: 1.35x slower   |
| gc_traversal               | 2.06 ms  | 2.79 ms: 1.36x slower  |
| xml_etree_iterparse        | 63.7 ms  | 87.5 ms: 1.37x slower  |
| async_tree_io_tg           | 410 ms   | 563 ms: 1.37x slower   |
| typing_runtime_protocols   | 106 us   | 146 us: 1.38x slower   |
| scimark_fft                | 192 ms   | 267 ms: 1.39x slower   |
| regex_compile              | 88.2 ms  | 123 ms: 1.39x slower   |
| deepcopy_reduce            | 1.94 us  | 2.71 us: 1.39x slower  |
| deepcopy                   | 190 us   | 266 us: 1.40x slower   |
| sqlglot_v2_normalize       | 73.6 ms  | 103 ms: 1.41x slower   |
| pprint_safe_repr           | 558 ms   | 789 ms: 1.41x slower   |
| sqlglot_v2_optimize        | 35.0 ms  | 49.6 ms: 1.41x slower  |
| genshi_text                | 16.5 ms  | 23.4 ms: 1.42x slower  |
| async_generators           | 226 ms   | 321 ms: 1.42x slower   |
| django_template            | 25.1 ms  | 35.8 ms: 1.43x slower  |
| pprint_pformat             | 1.13 sec | 1.61 sec: 1.43x slower |
| pyflate                    | 315 ms   | 457 ms: 1.45x slower   |
| bpe_tokeniser              | 2.96 sec | 4.30 sec: 1.45x slower |
| json_loads                 | 14.7 us  | 21.4 us: 1.46x slower  |
| scimark_sor                | 91.0 ms  | 133 ms: 1.46x slower   |
| nqueens                    | 63.6 ms  | 93.2 ms: 1.47x slower  |
| sqlglot_v2_transpile       | 1.10 ms  | 1.62 ms: 1.47x slower  |
| xml_etree_generate         | 58.7 ms  | 87.5 ms: 1.49x slower  |
| pickle_pure_python         | 237 us   | 354 us: 1.50x slower   |
| sqlglot_v2_parse           | 892 us   | 1.34 ms: 1.51x slower  |
| xml_etree_process          | 41.5 ms  | 63.0 ms: 1.52x slower  |
| chaos                      | 43.6 ms  | 67.0 ms: 1.54x slower  |
| crypto_pyaes               | 50.0 ms  | 76.8 ms: 1.54x slower  |
| float                      | 47.8 ms  | 73.5 ms: 1.54x slower  |
| go                         | 88.6 ms  | 138 ms: 1.56x slower   |
| deepcopy_memo              | 21.0 us  | 33.0 us: 1.57x slower  |
| scimark_sparse_mat_mult    | 2.72 ms  | 4.27 ms: 1.57x slower  |
| spectral_norm              | 61.5 ms  | 97.1 ms: 1.58x slower  |
| scimark_monte_carlo        | 47.1 ms  | 75.2 ms: 1.60x slower  |
| raytrace                   | 191 ms   | 306 ms: 1.61x slower   |
| coroutines                 | 13.5 ms  | 22.1 ms: 1.64x slower  |
| richards_super             | 35.1 ms  | 58.0 ms: 1.65x slower  |
| richards                   | 30.7 ms  | 51.0 ms: 1.66x slower  |
| hexiom                     | 4.38 ms  | 7.27 ms: 1.66x slower  |
| mako                       | 6.86 ms  | 11.4 ms: 1.67x slower  |
| comprehensions             | 11.3 us  | 19.4 us: 1.71x slower  |
| scimark_lu                 | 66.9 ms  | 116 ms: 1.73x slower   |
| generators                 | 19.3 ms  | 33.5 ms: 1.73x slower  |
| unpickle_pure_python       | 155 us   | 271 us: 1.75x slower   |
| deltablue                  | 2.29 ms  | 4.08 ms: 1.78x slower  |
| logging_silent             | 65.2 ns  | 121 ns: 1.86x slower   |
| many_optionals             | 438 us   | 890 us: 2.03x slower   |
| subparsers                 | 16.1 ms  | 50.4 ms: 3.13x slower  |
| Geometric mean             | (ref)    | 1.37x slower           |

- Geometric mean (including insignificant results): 1.272x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: unknown