# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TCO-PGO-Ex2            |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 237 ms: 1.23x faster   |
| docutils       | 2.11 sec | 1.81 sec: 1.16x faster |
| html5lib       | 51.3 ms  | 40.8 ms: 1.26x faster  |
| sphinx         | 843 ms   | 723 ms: 1.17x faster   |
| Geometric mean | (ref)    | 1.20x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TCO-PGO-Ex2           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 13.5 ms: 1.64x faster |
| async_generators           | 321 ms  | 224 ms: 1.44x faster  |
| async_tree_io_tg           | 563 ms  | 419 ms: 1.34x faster  |
| async_tree_memoization_tg  | 292 ms  | 218 ms: 1.34x faster  |
| async_tree_none_tg         | 236 ms  | 178 ms: 1.33x faster  |
| async_tree_none            | 248 ms  | 188 ms: 1.32x faster  |
| async_tree_memoization     | 297 ms  | 227 ms: 1.31x faster  |
| async_tree_io              | 551 ms  | 429 ms: 1.28x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 362 ms: 1.20x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 367 ms: 1.16x faster  |
| asyncio_websockets         | 311 ms  | 304 ms: 1.03x faster  |
| Geometric mean             | (ref)   | 1.30x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 58.8 ms: 1.68x faster |
| float          | 73.5 ms | 44.8 ms: 1.64x faster |
| pidigits       | 148 ms  | 147 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.41x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 88.0 ms: 1.40x faster |
| regex_effbot   | 1.77 ms | 1.76 ms: 1.01x faster |
| Geometric mean | (ref)   | 1.09x faster          |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TCO-PGO-Ex2            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 154 us: 1.76x faster   |
| pickle_pure_python   | 354 us   | 236 us: 1.50x faster   |
| tomli_loads          | 1.97 sec | 1.38 sec: 1.42x faster |
| xml_etree_process    | 63.0 ms  | 46.5 ms: 1.35x faster  |
| xml_etree_generate   | 87.5 ms  | 66.8 ms: 1.31x faster  |
| xml_etree_iterparse  | 87.5 ms  | 71.5 ms: 1.22x faster  |
| json_dumps           | 8.99 ms  | 7.94 ms: 1.13x faster  |
| xml_etree_parse      | 108 ms   | 104 ms: 1.04x faster   |
| json_loads           | 21.4 us  | 21.1 us: 1.02x faster  |
| Geometric mean       | (ref)    | 1.29x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TCO-Ex2 | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| python_startup | 27.2 ms | 26.9 ms: 1.01x faster |
| Geometric mean | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TCO-PGO-Ex2           |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 7.44 ms: 1.54x faster |
| genshi_text     | 23.4 ms | 16.2 ms: 1.44x faster |
| genshi_xml      | 48.8 ms | 35.3 ms: 1.38x faster |
| django_template | 35.8 ms | 27.5 ms: 1.30x faster |
| Geometric mean  | (ref)   | 1.42x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TCO-PGO-Ex2            |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.08 ms  | 2.09 ms: 1.95x faster  |
| logging_silent             | 121 ns   | 62.9 ns: 1.93x faster  |
| generators                 | 33.5 ms  | 18.1 ms: 1.85x faster  |
| scimark_sor                | 133 ms   | 73.9 ms: 1.80x faster  |
| scimark_lu                 | 116 ms   | 65.2 ms: 1.77x faster  |
| go                         | 138 ms   | 78.0 ms: 1.77x faster  |
| unpickle_pure_python       | 271 us   | 154 us: 1.76x faster   |
| scimark_monte_carlo        | 75.2 ms  | 42.9 ms: 1.75x faster  |
| hexiom                     | 7.27 ms  | 4.17 ms: 1.74x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.48 ms: 1.72x faster  |
| nbody                      | 98.8 ms  | 58.8 ms: 1.68x faster  |
| spectral_norm              | 97.1 ms  | 58.4 ms: 1.66x faster  |
| float                      | 73.5 ms  | 44.8 ms: 1.64x faster  |
| coroutines                 | 22.1 ms  | 13.5 ms: 1.64x faster  |
| raytrace                   | 306 ms   | 187 ms: 1.64x faster   |
| chaos                      | 67.0 ms  | 41.4 ms: 1.62x faster  |
| comprehensions             | 19.4 us  | 12.2 us: 1.59x faster  |
| crypto_pyaes               | 76.8 ms  | 49.3 ms: 1.56x faster  |
| deepcopy_memo              | 33.0 us  | 21.3 us: 1.55x faster  |
| pyflate                    | 457 ms   | 295 ms: 1.55x faster   |
| mako                       | 11.4 ms  | 7.44 ms: 1.54x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 876 us: 1.53x faster   |
| scimark_fft                | 267 ms   | 178 ms: 1.50x faster   |
| pickle_pure_python         | 354 us   | 236 us: 1.50x faster   |
| sqlglot_v2_transpile       | 1.62 ms  | 1.09 ms: 1.48x faster  |
| richards                   | 51.0 ms  | 35.0 ms: 1.46x faster  |
| fannkuch                   | 386 ms   | 265 ms: 1.46x faster   |
| genshi_text                | 23.4 ms  | 16.2 ms: 1.44x faster  |
| richards_super             | 58.0 ms  | 40.4 ms: 1.44x faster  |
| async_generators           | 321 ms   | 224 ms: 1.44x faster   |
| pprint_pformat             | 1.61 sec | 1.13 sec: 1.43x faster |
| tomli_loads                | 1.97 sec | 1.38 sec: 1.42x faster |
| nqueens                    | 93.2 ms  | 65.7 ms: 1.42x faster  |
| pprint_safe_repr           | 789 ms   | 558 ms: 1.41x faster   |
| regex_compile              | 123 ms   | 88.0 ms: 1.40x faster  |
| genshi_xml                 | 48.8 ms  | 35.3 ms: 1.38x faster  |
| bpe_tokeniser              | 4.30 sec | 3.17 sec: 1.36x faster |
| xml_etree_process          | 63.0 ms  | 46.5 ms: 1.35x faster  |
| async_tree_io_tg           | 563 ms   | 419 ms: 1.34x faster   |
| async_tree_memoization_tg  | 292 ms   | 218 ms: 1.34x faster   |
| deepcopy                   | 266 us   | 199 us: 1.34x faster   |
| async_tree_none_tg         | 236 ms   | 178 ms: 1.33x faster   |
| async_tree_none            | 248 ms   | 188 ms: 1.32x faster   |
| xml_etree_generate         | 87.5 ms  | 66.8 ms: 1.31x faster  |
| sqlglot_v2_normalize       | 103 ms   | 79.0 ms: 1.31x faster  |
| async_tree_memoization     | 297 ms   | 227 ms: 1.31x faster   |
| django_template            | 35.8 ms  | 27.5 ms: 1.30x faster  |
| typing_runtime_protocols   | 146 us   | 113 us: 1.30x faster   |
| logging_simple             | 8.63 us  | 6.67 us: 1.29x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 38.4 ms: 1.29x faster  |
| async_tree_io              | 551 ms   | 429 ms: 1.28x faster   |
| deepcopy_reduce            | 2.71 us  | 2.12 us: 1.27x faster  |
| logging_format             | 9.13 us  | 7.18 us: 1.27x faster  |
| pycparser                  | 968 ms   | 765 ms: 1.27x faster   |
| sympy_integrate            | 17.5 ms  | 13.9 ms: 1.26x faster  |
| sympy_str                  | 234 ms   | 187 ms: 1.26x faster   |
| html5lib                   | 51.3 ms  | 40.8 ms: 1.26x faster  |
| 2to3                       | 293 ms   | 237 ms: 1.23x faster   |
| sympy_expand               | 399 ms   | 324 ms: 1.23x faster   |
| xml_etree_iterparse        | 87.5 ms  | 71.5 ms: 1.22x faster  |
| sympy_sum                  | 118 ms   | 96.6 ms: 1.22x faster  |
| meteor_contest             | 95.0 ms  | 78.1 ms: 1.22x faster  |
| thrift                     | 680 us   | 561 us: 1.21x faster   |
| async_tree_cpu_io_mixed    | 434 ms   | 362 ms: 1.20x faster   |
| telco                      | 6.34 ms  | 5.33 ms: 1.19x faster  |
| dulwich_log                | 50.5 ms  | 43.0 ms: 1.17x faster  |
| sphinx                     | 843 ms   | 723 ms: 1.17x faster   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 367 ms: 1.16x faster   |
| docutils                   | 2.11 sec | 1.81 sec: 1.16x faster |
| mdp                        | 1.82 sec | 1.57 sec: 1.16x faster |
| pylint                     | 249 ms   | 217 ms: 1.15x faster   |
| json_dumps                 | 8.99 ms  | 7.94 ms: 1.13x faster  |
| bench_thread_pool          | 1.01 ms  | 906 us: 1.12x faster   |
| many_optionals             | 890 us   | 813 us: 1.09x faster   |
| coverage                   | 61.1 ms  | 56.4 ms: 1.08x faster  |
| connected_components       | 351 ms   | 326 ms: 1.08x faster   |
| shortest_path              | 384 ms   | 357 ms: 1.07x faster   |
| subparsers                 | 50.4 ms  | 47.1 ms: 1.07x faster  |
| sqlite_synth               | 1.78 us  | 1.68 us: 1.06x faster  |
| pathlib                    | 26.8 ms  | 25.6 ms: 1.05x faster  |
| json                       | 3.94 ms  | 3.77 ms: 1.04x faster  |
| xml_etree_parse            | 108 ms   | 104 ms: 1.04x faster   |
| k_core                     | 1.83 sec | 1.76 sec: 1.04x faster |
| bench_mp_pool              | 97.6 ms  | 95.0 ms: 1.03x faster  |
| asyncio_websockets         | 311 ms   | 304 ms: 1.03x faster   |
| json_loads                 | 21.4 us  | 21.1 us: 1.02x faster  |
| python_startup             | 27.2 ms  | 26.9 ms: 1.01x faster  |
| pidigits                   | 148 ms   | 147 ms: 1.01x faster   |
| create_gc_cycles           | 1.40 ms  | 1.38 ms: 1.01x faster  |
| regex_effbot               | 1.77 ms  | 1.76 ms: 1.01x faster  |
| gc_traversal               | 2.79 ms  | 2.77 ms: 1.01x faster  |
| Geometric mean             | (ref)    | 1.31x faster           |

Benchmark hidden because not significant (3): regex_v8, python_startup_no_site, regex_dna

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown