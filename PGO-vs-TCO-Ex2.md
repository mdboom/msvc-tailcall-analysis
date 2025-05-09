# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.374x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | PGO                    |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 227 ms: 1.29x faster   |
| docutils       | 2.11 sec | 1.68 sec: 1.25x faster |
| html5lib       | 51.3 ms  | 40.8 ms: 1.26x faster  |
| sphinx         | 843 ms   | 658 ms: 1.28x faster   |
| Geometric mean | (ref)    | 1.27x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | PGO                   |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 13.5 ms: 1.64x faster |
| async_generators           | 321 ms  | 226 ms: 1.42x faster  |
| async_tree_io_tg           | 563 ms  | 410 ms: 1.37x faster  |
| async_tree_memoization_tg  | 292 ms  | 216 ms: 1.35x faster  |
| async_tree_none_tg         | 236 ms  | 176 ms: 1.34x faster  |
| async_tree_none            | 248 ms  | 187 ms: 1.33x faster  |
| async_tree_memoization     | 297 ms  | 224 ms: 1.32x faster  |
| async_tree_io              | 551 ms  | 423 ms: 1.30x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 339 ms: 1.28x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 343 ms: 1.25x faster  |
| asyncio_websockets         | 311 ms  | 318 ms: 1.02x slower  |
| Geometric mean             | (ref)   | 1.32x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | PGO                   |
|----------------|:-------:|:---------------------:|
| float          | 73.5 ms | 47.8 ms: 1.54x faster |
| nbody          | 98.8 ms | 74.1 ms: 1.33x faster |
| pidigits       | 148 ms  | 152 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.26x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | PGO                   |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 88.2 ms: 1.39x faster |
| regex_v8       | 17.0 ms | 13.5 ms: 1.25x faster |
| regex_effbot   | 1.77 ms | 1.42 ms: 1.25x faster |
| regex_dna      | 118 ms  | 112 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.23x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | PGO                    |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 155 us: 1.75x faster   |
| xml_etree_process    | 63.0 ms  | 41.5 ms: 1.52x faster  |
| pickle_pure_python   | 354 us   | 237 us: 1.50x faster   |
| xml_etree_generate   | 87.5 ms  | 58.7 ms: 1.49x faster  |
| json_loads           | 21.4 us  | 14.7 us: 1.46x faster  |
| xml_etree_iterparse  | 87.5 ms  | 63.7 ms: 1.37x faster  |
| tomli_loads          | 1.97 sec | 1.47 sec: 1.34x faster |
| json_dumps           | 8.99 ms  | 7.05 ms: 1.28x faster  |
| xml_etree_parse      | 108 ms   | 91.2 ms: 1.18x faster  |
| Geometric mean       | (ref)    | 1.42x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | PGO                   |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 26.1 ms: 1.05x faster |
| python_startup_no_site | 20.3 ms | 19.8 ms: 1.02x faster |
| Geometric mean         | (ref)   | 1.03x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | PGO                   |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 6.86 ms: 1.67x faster |
| django_template | 35.8 ms | 25.1 ms: 1.43x faster |
| genshi_text     | 23.4 ms | 16.5 ms: 1.42x faster |
| genshi_xml      | 48.8 ms | 36.3 ms: 1.34x faster |
| Geometric mean  | (ref)   | 1.46x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | PGO                    |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 50.4 ms  | 16.1 ms: 3.13x faster  |
| many_optionals             | 890 us   | 438 us: 2.03x faster   |
| logging_silent             | 121 ns   | 65.2 ns: 1.86x faster  |
| deltablue                  | 4.08 ms  | 2.29 ms: 1.78x faster  |
| unpickle_pure_python       | 271 us   | 155 us: 1.75x faster   |
| generators                 | 33.5 ms  | 19.3 ms: 1.73x faster  |
| scimark_lu                 | 116 ms   | 66.9 ms: 1.73x faster  |
| comprehensions             | 19.4 us  | 11.3 us: 1.71x faster  |
| mako                       | 11.4 ms  | 6.86 ms: 1.67x faster  |
| hexiom                     | 7.27 ms  | 4.38 ms: 1.66x faster  |
| richards                   | 51.0 ms  | 30.7 ms: 1.66x faster  |
| richards_super             | 58.0 ms  | 35.1 ms: 1.65x faster  |
| coroutines                 | 22.1 ms  | 13.5 ms: 1.64x faster  |
| raytrace                   | 306 ms   | 191 ms: 1.61x faster   |
| scimark_monte_carlo        | 75.2 ms  | 47.1 ms: 1.60x faster  |
| spectral_norm              | 97.1 ms  | 61.5 ms: 1.58x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.72 ms: 1.57x faster  |
| deepcopy_memo              | 33.0 us  | 21.0 us: 1.57x faster  |
| go                         | 138 ms   | 88.6 ms: 1.56x faster  |
| float                      | 73.5 ms  | 47.8 ms: 1.54x faster  |
| crypto_pyaes               | 76.8 ms  | 50.0 ms: 1.54x faster  |
| chaos                      | 67.0 ms  | 43.6 ms: 1.54x faster  |
| xml_etree_process          | 63.0 ms  | 41.5 ms: 1.52x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 892 us: 1.51x faster   |
| pickle_pure_python         | 354 us   | 237 us: 1.50x faster   |
| xml_etree_generate         | 87.5 ms  | 58.7 ms: 1.49x faster  |
| sqlglot_v2_transpile       | 1.62 ms  | 1.10 ms: 1.47x faster  |
| nqueens                    | 93.2 ms  | 63.6 ms: 1.47x faster  |
| scimark_sor                | 133 ms   | 91.0 ms: 1.46x faster  |
| json_loads                 | 21.4 us  | 14.7 us: 1.46x faster  |
| bpe_tokeniser              | 4.30 sec | 2.96 sec: 1.45x faster |
| pyflate                    | 457 ms   | 315 ms: 1.45x faster   |
| pprint_pformat             | 1.61 sec | 1.13 sec: 1.43x faster |
| django_template            | 35.8 ms  | 25.1 ms: 1.43x faster  |
| async_generators           | 321 ms   | 226 ms: 1.42x faster   |
| genshi_text                | 23.4 ms  | 16.5 ms: 1.42x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 35.0 ms: 1.41x faster  |
| pprint_safe_repr           | 789 ms   | 558 ms: 1.41x faster   |
| sqlglot_v2_normalize       | 103 ms   | 73.6 ms: 1.41x faster  |
| deepcopy                   | 266 us   | 190 us: 1.40x faster   |
| deepcopy_reduce            | 2.71 us  | 1.94 us: 1.39x faster  |
| regex_compile              | 123 ms   | 88.2 ms: 1.39x faster  |
| scimark_fft                | 267 ms   | 192 ms: 1.39x faster   |
| typing_runtime_protocols   | 146 us   | 106 us: 1.38x faster   |
| async_tree_io_tg           | 563 ms   | 410 ms: 1.37x faster   |
| xml_etree_iterparse        | 87.5 ms  | 63.7 ms: 1.37x faster  |
| gc_traversal               | 2.79 ms  | 2.06 ms: 1.36x faster  |
| async_tree_memoization_tg  | 292 ms   | 216 ms: 1.35x faster   |
| genshi_xml                 | 48.8 ms  | 36.3 ms: 1.34x faster  |
| thrift                     | 680 us   | 507 us: 1.34x faster   |
| tomli_loads                | 1.97 sec | 1.47 sec: 1.34x faster |
| async_tree_none_tg         | 236 ms   | 176 ms: 1.34x faster   |
| nbody                      | 98.8 ms  | 74.1 ms: 1.33x faster  |
| sympy_str                  | 234 ms   | 176 ms: 1.33x faster   |
| async_tree_none            | 248 ms   | 187 ms: 1.33x faster   |
| async_tree_memoization     | 297 ms   | 224 ms: 1.32x faster   |
| sympy_expand               | 399 ms   | 302 ms: 1.32x faster   |
| logging_simple             | 8.63 us  | 6.53 us: 1.32x faster  |
| pycparser                  | 968 ms   | 738 ms: 1.31x faster   |
| coverage                   | 61.1 ms  | 46.8 ms: 1.30x faster  |
| fannkuch                   | 386 ms   | 296 ms: 1.30x faster   |
| async_tree_io              | 551 ms   | 423 ms: 1.30x faster   |
| sympy_sum                  | 118 ms   | 90.5 ms: 1.30x faster  |
| logging_format             | 9.13 us  | 7.03 us: 1.30x faster  |
| telco                      | 6.34 ms  | 4.89 ms: 1.30x faster  |
| sympy_integrate            | 17.5 ms  | 13.5 ms: 1.30x faster  |
| 2to3                       | 293 ms   | 227 ms: 1.29x faster   |
| sphinx                     | 843 ms   | 658 ms: 1.28x faster   |
| async_tree_cpu_io_mixed    | 434 ms   | 339 ms: 1.28x faster   |
| json_dumps                 | 8.99 ms  | 7.05 ms: 1.28x faster  |
| html5lib                   | 51.3 ms  | 40.8 ms: 1.26x faster  |
| json                       | 3.94 ms  | 3.14 ms: 1.25x faster  |
| docutils                   | 2.11 sec | 1.68 sec: 1.25x faster |
| regex_v8                   | 17.0 ms  | 13.5 ms: 1.25x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms   | 343 ms: 1.25x faster   |
| regex_effbot               | 1.77 ms  | 1.42 ms: 1.25x faster  |
| pylint                     | 249 ms   | 201 ms: 1.24x faster   |
| meteor_contest             | 95.0 ms  | 76.9 ms: 1.24x faster  |
| xml_etree_parse            | 108 ms   | 91.2 ms: 1.18x faster  |
| bench_thread_pool          | 1.01 ms  | 864 us: 1.17x faster   |
| dulwich_log                | 50.5 ms  | 43.4 ms: 1.16x faster  |
| sqlite_synth               | 1.78 us  | 1.59 us: 1.12x faster  |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.12x faster  |
| mdp                        | 1.82 sec | 1.64 sec: 1.11x faster |
| bench_mp_pool              | 97.6 ms  | 88.7 ms: 1.10x faster  |
| shortest_path              | 384 ms   | 359 ms: 1.07x faster   |
| connected_components       | 351 ms   | 329 ms: 1.06x faster   |
| k_core                     | 1.83 sec | 1.73 sec: 1.06x faster |
| regex_dna                  | 118 ms   | 112 ms: 1.05x faster   |
| python_startup             | 27.2 ms  | 26.1 ms: 1.05x faster  |
| python_startup_no_site     | 20.3 ms  | 19.8 ms: 1.02x faster  |
| asyncio_websockets         | 311 ms   | 318 ms: 1.02x slower   |
| pidigits                   | 148 ms   | 152 ms: 1.03x slower   |
| pathlib                    | 26.8 ms  | 32.1 ms: 1.20x slower  |
| Geometric mean             | (ref)    | 1.37x faster           |

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: unknown