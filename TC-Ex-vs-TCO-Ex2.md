# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.384x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 231 ms: 1.27x faster   |
| docutils       | 2.11 sec | 1.77 sec: 1.19x faster |
| html5lib       | 51.3 ms  | 38.8 ms: 1.32x faster  |
| sphinx         | 843 ms   | 702 ms: 1.20x faster   |
| Geometric mean | (ref)    | 1.25x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 12.3 ms: 1.80x faster |
| async_generators           | 321 ms  | 213 ms: 1.50x faster  |
| async_tree_io_tg           | 563 ms  | 385 ms: 1.46x faster  |
| async_tree_io              | 551 ms  | 384 ms: 1.44x faster  |
| async_tree_none            | 248 ms  | 174 ms: 1.43x faster  |
| async_tree_memoization     | 297 ms  | 210 ms: 1.42x faster  |
| async_tree_none_tg         | 236 ms  | 167 ms: 1.41x faster  |
| async_tree_memoization_tg  | 292 ms  | 210 ms: 1.39x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 359 ms: 1.21x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 363 ms: 1.18x faster  |
| Geometric mean             | (ref)   | 1.37x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 53.1 ms: 1.86x faster |
| float          | 73.5 ms | 41.4 ms: 1.77x faster |
| pidigits       | 148 ms  | 146 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.50x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 81.9 ms: 1.50x faster |
| regex_v8       | 17.0 ms | 16.3 ms: 1.04x faster |
| regex_dna      | 118 ms  | 121 ms: 1.03x slower  |
| regex_effbot   | 1.77 ms | 1.85 ms: 1.04x slower |
| Geometric mean | (ref)   | 1.10x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 148 us: 1.83x faster   |
| pickle_pure_python   | 354 us   | 223 us: 1.59x faster   |
| tomli_loads          | 1.97 sec | 1.26 sec: 1.56x faster |
| xml_etree_process    | 63.0 ms  | 44.7 ms: 1.41x faster  |
| xml_etree_generate   | 87.5 ms  | 64.7 ms: 1.35x faster  |
| xml_etree_iterparse  | 87.5 ms  | 70.4 ms: 1.24x faster  |
| json_dumps           | 8.99 ms  | 7.79 ms: 1.16x faster  |
| xml_etree_parse      | 108 ms   | 105 ms: 1.03x faster   |
| json_loads           | 21.4 us  | 21.9 us: 1.02x slower  |
| Geometric mean       | (ref)    | 1.33x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.3 ms | 19.4 ms: 1.05x faster |
| python_startup         | 27.2 ms | 26.4 ms: 1.03x faster |
| Geometric mean         | (ref)   | 1.04x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TC-Ex                 |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 23.4 ms | 14.5 ms: 1.62x faster |
| genshi_xml      | 48.8 ms | 31.3 ms: 1.56x faster |
| mako            | 11.4 ms | 7.84 ms: 1.46x faster |
| django_template | 35.8 ms | 25.2 ms: 1.42x faster |
| Geometric mean  | (ref)   | 1.51x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.08 ms  | 1.91 ms: 2.13x faster  |
| generators                 | 33.5 ms  | 16.3 ms: 2.05x faster  |
| logging_silent             | 121 ns   | 61.1 ns: 1.99x faster  |
| go                         | 138 ms   | 70.4 ms: 1.96x faster  |
| scimark_sor                | 133 ms   | 68.6 ms: 1.94x faster  |
| scimark_monte_carlo        | 75.2 ms  | 38.9 ms: 1.93x faster  |
| spectral_norm              | 97.1 ms  | 51.1 ms: 1.90x faster  |
| nbody                      | 98.8 ms  | 53.1 ms: 1.86x faster  |
| hexiom                     | 7.27 ms  | 3.92 ms: 1.86x faster  |
| unpickle_pure_python       | 271 us   | 148 us: 1.83x faster   |
| raytrace                   | 306 ms   | 169 ms: 1.81x faster   |
| scimark_lu                 | 116 ms   | 64.2 ms: 1.80x faster  |
| coroutines                 | 22.1 ms  | 12.3 ms: 1.80x faster  |
| chaos                      | 67.0 ms  | 37.7 ms: 1.77x faster  |
| float                      | 73.5 ms  | 41.4 ms: 1.77x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.47 ms: 1.73x faster  |
| comprehensions             | 19.4 us  | 11.3 us: 1.72x faster  |
| deepcopy_memo              | 33.0 us  | 19.3 us: 1.71x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 798 us: 1.68x faster   |
| pyflate                    | 457 ms   | 274 ms: 1.67x faster   |
| richards                   | 51.0 ms  | 30.9 ms: 1.65x faster  |
| richards_super             | 58.0 ms  | 35.8 ms: 1.62x faster  |
| genshi_text                | 23.4 ms  | 14.5 ms: 1.62x faster  |
| crypto_pyaes               | 76.8 ms  | 48.0 ms: 1.60x faster  |
| sqlglot_v2_transpile       | 1.62 ms  | 1.01 ms: 1.59x faster  |
| pickle_pure_python         | 354 us   | 223 us: 1.59x faster   |
| scimark_fft                | 267 ms   | 169 ms: 1.59x faster   |
| nqueens                    | 93.2 ms  | 59.6 ms: 1.56x faster  |
| tomli_loads                | 1.97 sec | 1.26 sec: 1.56x faster |
| genshi_xml                 | 48.8 ms  | 31.3 ms: 1.56x faster  |
| pprint_pformat             | 1.61 sec | 1.04 sec: 1.56x faster |
| pprint_safe_repr           | 789 ms   | 510 ms: 1.55x faster   |
| fannkuch                   | 386 ms   | 250 ms: 1.54x faster   |
| async_generators           | 321 ms   | 213 ms: 1.50x faster   |
| regex_compile              | 123 ms   | 81.9 ms: 1.50x faster  |
| deepcopy                   | 266 us   | 180 us: 1.47x faster   |
| async_tree_io_tg           | 563 ms   | 385 ms: 1.46x faster   |
| mako                       | 11.4 ms  | 7.84 ms: 1.46x faster  |
| async_tree_io              | 551 ms   | 384 ms: 1.44x faster   |
| bpe_tokeniser              | 4.30 sec | 3.01 sec: 1.43x faster |
| async_tree_none            | 248 ms   | 174 ms: 1.43x faster   |
| deepcopy_reduce            | 2.71 us  | 1.90 us: 1.43x faster  |
| django_template            | 35.8 ms  | 25.2 ms: 1.42x faster  |
| async_tree_memoization     | 297 ms   | 210 ms: 1.42x faster   |
| sqlglot_v2_normalize       | 103 ms   | 73.3 ms: 1.41x faster  |
| async_tree_none_tg         | 236 ms   | 167 ms: 1.41x faster   |
| xml_etree_process          | 63.0 ms  | 44.7 ms: 1.41x faster  |
| async_tree_memoization_tg  | 292 ms   | 210 ms: 1.39x faster   |
| typing_runtime_protocols   | 146 us   | 106 us: 1.38x faster   |
| logging_simple             | 8.63 us  | 6.25 us: 1.38x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 36.1 ms: 1.37x faster  |
| logging_format             | 9.13 us  | 6.70 us: 1.36x faster  |
| pycparser                  | 968 ms   | 713 ms: 1.36x faster   |
| xml_etree_generate         | 87.5 ms  | 64.7 ms: 1.35x faster  |
| sympy_str                  | 234 ms   | 177 ms: 1.32x faster   |
| html5lib                   | 51.3 ms  | 38.8 ms: 1.32x faster  |
| sympy_expand               | 399 ms   | 304 ms: 1.31x faster   |
| sympy_integrate            | 17.5 ms  | 13.4 ms: 1.31x faster  |
| sympy_sum                  | 118 ms   | 91.4 ms: 1.29x faster  |
| meteor_contest             | 95.0 ms  | 74.5 ms: 1.28x faster  |
| 2to3                       | 293 ms   | 231 ms: 1.27x faster   |
| mdp                        | 1.82 sec | 1.44 sec: 1.26x faster |
| xml_etree_iterparse        | 87.5 ms  | 70.4 ms: 1.24x faster  |
| thrift                     | 680 us   | 551 us: 1.23x faster   |
| pylint                     | 249 ms   | 205 ms: 1.21x faster   |
| async_tree_cpu_io_mixed    | 434 ms   | 359 ms: 1.21x faster   |
| telco                      | 6.34 ms  | 5.26 ms: 1.21x faster  |
| sphinx                     | 843 ms   | 702 ms: 1.20x faster   |
| dulwich_log                | 50.5 ms  | 42.3 ms: 1.19x faster  |
| docutils                   | 2.11 sec | 1.77 sec: 1.19x faster |
| async_tree_cpu_io_mixed_tg | 428 ms   | 363 ms: 1.18x faster   |
| many_optionals             | 890 us   | 762 us: 1.17x faster   |
| json_dumps                 | 8.99 ms  | 7.79 ms: 1.16x faster  |
| bench_thread_pool          | 1.01 ms  | 876 us: 1.15x faster   |
| subparsers                 | 50.4 ms  | 44.5 ms: 1.13x faster  |
| connected_components       | 351 ms   | 311 ms: 1.13x faster   |
| shortest_path              | 384 ms   | 347 ms: 1.11x faster   |
| coverage                   | 61.1 ms  | 55.4 ms: 1.10x faster  |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| pathlib                    | 26.8 ms  | 25.1 ms: 1.07x faster  |
| sqlite_synth               | 1.78 us  | 1.68 us: 1.06x faster  |
| python_startup_no_site     | 20.3 ms  | 19.4 ms: 1.05x faster  |
| create_gc_cycles           | 1.40 ms  | 1.34 ms: 1.04x faster  |
| bench_mp_pool              | 97.6 ms  | 93.6 ms: 1.04x faster  |
| json                       | 3.94 ms  | 3.78 ms: 1.04x faster  |
| regex_v8                   | 17.0 ms  | 16.3 ms: 1.04x faster  |
| xml_etree_parse            | 108 ms   | 105 ms: 1.03x faster   |
| python_startup             | 27.2 ms  | 26.4 ms: 1.03x faster  |
| pidigits                   | 148 ms   | 146 ms: 1.02x faster   |
| gc_traversal               | 2.79 ms  | 2.83 ms: 1.01x slower  |
| json_loads                 | 21.4 us  | 21.9 us: 1.02x slower  |
| regex_dna                  | 118 ms   | 121 ms: 1.03x slower   |
| regex_effbot               | 1.77 ms  | 1.85 ms: 1.04x slower  |
| Geometric mean             | (ref)    | 1.38x faster           |

Benchmark hidden because not significant (1): asyncio_websockets

- Geometric mean (including insignificant results): 1.384x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: unknown