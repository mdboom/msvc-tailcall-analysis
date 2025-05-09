# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.277x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 293 ms: 1.27x slower   |
| docutils       | 1.77 sec | 2.11 sec: 1.19x slower |
| html5lib       | 38.8 ms  | 51.3 ms: 1.32x slower  |
| sphinx         | 702 ms   | 843 ms: 1.20x slower   |
| Geometric mean | (ref)    | 1.25x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 428 ms: 1.18x slower  |
| async_tree_cpu_io_mixed    | 359 ms  | 434 ms: 1.21x slower  |
| async_tree_memoization_tg  | 210 ms  | 292 ms: 1.39x slower  |
| async_tree_none_tg         | 167 ms  | 236 ms: 1.41x slower  |
| async_tree_memoization     | 210 ms  | 297 ms: 1.42x slower  |
| async_tree_none            | 174 ms  | 248 ms: 1.43x slower  |
| async_tree_io              | 384 ms  | 551 ms: 1.44x slower  |
| async_tree_io_tg           | 385 ms  | 563 ms: 1.46x slower  |
| async_generators           | 213 ms  | 321 ms: 1.50x slower  |
| coroutines                 | 12.3 ms | 22.1 ms: 1.80x slower |
| Geometric mean             | (ref)   | 1.37x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 148 ms: 1.02x slower  |
| float          | 41.4 ms | 73.5 ms: 1.77x slower |
| nbody          | 53.1 ms | 98.8 ms: 1.86x slower |
| Geometric mean | (ref)   | 1.50x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.77 ms: 1.04x faster |
| regex_dna      | 121 ms  | 118 ms: 1.03x faster  |
| regex_v8       | 16.3 ms | 17.0 ms: 1.04x slower |
| regex_compile  | 81.9 ms | 123 ms: 1.50x slower  |
| Geometric mean | (ref)   | 1.10x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 21.4 us: 1.02x faster  |
| xml_etree_parse      | 105 ms   | 108 ms: 1.03x slower   |
| json_dumps           | 7.79 ms  | 8.99 ms: 1.16x slower  |
| xml_etree_iterparse  | 70.4 ms  | 87.5 ms: 1.24x slower  |
| xml_etree_generate   | 64.7 ms  | 87.5 ms: 1.35x slower  |
| xml_etree_process    | 44.7 ms  | 63.0 ms: 1.41x slower  |
| tomli_loads          | 1.26 sec | 1.97 sec: 1.56x slower |
| pickle_pure_python   | 223 us   | 354 us: 1.59x slower   |
| unpickle_pure_python | 148 us   | 271 us: 1.83x slower   |
| Geometric mean       | (ref)    | 1.33x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TCO-Ex2               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 27.2 ms: 1.03x slower |
| python_startup_no_site | 19.4 ms | 20.3 ms: 1.05x slower |
| Geometric mean         | (ref)   | 1.04x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| django_template | 25.2 ms | 35.8 ms: 1.42x slower |
| mako            | 7.84 ms | 11.4 ms: 1.46x slower |
| genshi_xml      | 31.3 ms | 48.8 ms: 1.56x slower |
| genshi_text     | 14.5 ms | 23.4 ms: 1.62x slower |
| Geometric mean  | (ref)   | 1.51x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| regex_effbot               | 1.85 ms  | 1.77 ms: 1.04x faster  |
| regex_dna                  | 121 ms   | 118 ms: 1.03x faster   |
| json_loads                 | 21.9 us  | 21.4 us: 1.02x faster  |
| gc_traversal               | 2.83 ms  | 2.79 ms: 1.01x faster  |
| pidigits                   | 146 ms   | 148 ms: 1.02x slower   |
| python_startup             | 26.4 ms  | 27.2 ms: 1.03x slower  |
| xml_etree_parse            | 105 ms   | 108 ms: 1.03x slower   |
| regex_v8                   | 16.3 ms  | 17.0 ms: 1.04x slower  |
| json                       | 3.78 ms  | 3.94 ms: 1.04x slower  |
| bench_mp_pool              | 93.6 ms  | 97.6 ms: 1.04x slower  |
| create_gc_cycles           | 1.34 ms  | 1.40 ms: 1.04x slower  |
| python_startup_no_site     | 19.4 ms  | 20.3 ms: 1.05x slower  |
| sqlite_synth               | 1.68 us  | 1.78 us: 1.06x slower  |
| pathlib                    | 25.1 ms  | 26.8 ms: 1.07x slower  |
| k_core                     | 1.71 sec | 1.83 sec: 1.07x slower |
| coverage                   | 55.4 ms  | 61.1 ms: 1.10x slower  |
| shortest_path              | 347 ms   | 384 ms: 1.11x slower   |
| connected_components       | 311 ms   | 351 ms: 1.13x slower   |
| subparsers                 | 44.5 ms  | 50.4 ms: 1.13x slower  |
| bench_thread_pool          | 876 us   | 1.01 ms: 1.15x slower  |
| json_dumps                 | 7.79 ms  | 8.99 ms: 1.16x slower  |
| many_optionals             | 762 us   | 890 us: 1.17x slower   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 428 ms: 1.18x slower   |
| docutils                   | 1.77 sec | 2.11 sec: 1.19x slower |
| dulwich_log                | 42.3 ms  | 50.5 ms: 1.19x slower  |
| sphinx                     | 702 ms   | 843 ms: 1.20x slower   |
| telco                      | 5.26 ms  | 6.34 ms: 1.21x slower  |
| async_tree_cpu_io_mixed    | 359 ms   | 434 ms: 1.21x slower   |
| pylint                     | 205 ms   | 249 ms: 1.21x slower   |
| thrift                     | 551 us   | 680 us: 1.23x slower   |
| xml_etree_iterparse        | 70.4 ms  | 87.5 ms: 1.24x slower  |
| mdp                        | 1.44 sec | 1.82 sec: 1.26x slower |
| 2to3                       | 231 ms   | 293 ms: 1.27x slower   |
| meteor_contest             | 74.5 ms  | 95.0 ms: 1.28x slower  |
| sympy_sum                  | 91.4 ms  | 118 ms: 1.29x slower   |
| sympy_integrate            | 13.4 ms  | 17.5 ms: 1.31x slower  |
| sympy_expand               | 304 ms   | 399 ms: 1.31x slower   |
| html5lib                   | 38.8 ms  | 51.3 ms: 1.32x slower  |
| sympy_str                  | 177 ms   | 234 ms: 1.32x slower   |
| xml_etree_generate         | 64.7 ms  | 87.5 ms: 1.35x slower  |
| pycparser                  | 713 ms   | 968 ms: 1.36x slower   |
| logging_format             | 6.70 us  | 9.13 us: 1.36x slower  |
| sqlglot_v2_optimize        | 36.1 ms  | 49.6 ms: 1.37x slower  |
| logging_simple             | 6.25 us  | 8.63 us: 1.38x slower  |
| typing_runtime_protocols   | 106 us   | 146 us: 1.38x slower   |
| async_tree_memoization_tg  | 210 ms   | 292 ms: 1.39x slower   |
| xml_etree_process          | 44.7 ms  | 63.0 ms: 1.41x slower  |
| async_tree_none_tg         | 167 ms   | 236 ms: 1.41x slower   |
| sqlglot_v2_normalize       | 73.3 ms  | 103 ms: 1.41x slower   |
| async_tree_memoization     | 210 ms   | 297 ms: 1.42x slower   |
| django_template            | 25.2 ms  | 35.8 ms: 1.42x slower  |
| deepcopy_reduce            | 1.90 us  | 2.71 us: 1.43x slower  |
| async_tree_none            | 174 ms   | 248 ms: 1.43x slower   |
| bpe_tokeniser              | 3.01 sec | 4.30 sec: 1.43x slower |
| async_tree_io              | 384 ms   | 551 ms: 1.44x slower   |
| mako                       | 7.84 ms  | 11.4 ms: 1.46x slower  |
| async_tree_io_tg           | 385 ms   | 563 ms: 1.46x slower   |
| deepcopy                   | 180 us   | 266 us: 1.47x slower   |
| regex_compile              | 81.9 ms  | 123 ms: 1.50x slower   |
| async_generators           | 213 ms   | 321 ms: 1.50x slower   |
| fannkuch                   | 250 ms   | 386 ms: 1.54x slower   |
| pprint_safe_repr           | 510 ms   | 789 ms: 1.55x slower   |
| pprint_pformat             | 1.04 sec | 1.61 sec: 1.56x slower |
| genshi_xml                 | 31.3 ms  | 48.8 ms: 1.56x slower  |
| tomli_loads                | 1.26 sec | 1.97 sec: 1.56x slower |
| nqueens                    | 59.6 ms  | 93.2 ms: 1.56x slower  |
| scimark_fft                | 169 ms   | 267 ms: 1.59x slower   |
| pickle_pure_python         | 223 us   | 354 us: 1.59x slower   |
| sqlglot_v2_transpile       | 1.01 ms  | 1.62 ms: 1.59x slower  |
| crypto_pyaes               | 48.0 ms  | 76.8 ms: 1.60x slower  |
| genshi_text                | 14.5 ms  | 23.4 ms: 1.62x slower  |
| richards_super             | 35.8 ms  | 58.0 ms: 1.62x slower  |
| richards                   | 30.9 ms  | 51.0 ms: 1.65x slower  |
| pyflate                    | 274 ms   | 457 ms: 1.67x slower   |
| sqlglot_v2_parse           | 798 us   | 1.34 ms: 1.68x slower  |
| deepcopy_memo              | 19.3 us  | 33.0 us: 1.71x slower  |
| comprehensions             | 11.3 us  | 19.4 us: 1.72x slower  |
| scimark_sparse_mat_mult    | 2.47 ms  | 4.27 ms: 1.73x slower  |
| float                      | 41.4 ms  | 73.5 ms: 1.77x slower  |
| chaos                      | 37.7 ms  | 67.0 ms: 1.77x slower  |
| coroutines                 | 12.3 ms  | 22.1 ms: 1.80x slower  |
| scimark_lu                 | 64.2 ms  | 116 ms: 1.80x slower   |
| raytrace                   | 169 ms   | 306 ms: 1.81x slower   |
| unpickle_pure_python       | 148 us   | 271 us: 1.83x slower   |
| hexiom                     | 3.92 ms  | 7.27 ms: 1.86x slower  |
| nbody                      | 53.1 ms  | 98.8 ms: 1.86x slower  |
| spectral_norm              | 51.1 ms  | 97.1 ms: 1.90x slower  |
| scimark_monte_carlo        | 38.9 ms  | 75.2 ms: 1.93x slower  |
| scimark_sor                | 68.6 ms  | 133 ms: 1.94x slower   |
| go                         | 70.4 ms  | 138 ms: 1.96x slower   |
| logging_silent             | 61.1 ns  | 121 ns: 1.99x slower   |
| generators                 | 16.3 ms  | 33.5 ms: 2.05x slower  |
| deltablue                  | 1.91 ms  | 4.08 ms: 2.13x slower  |
| Geometric mean             | (ref)    | 1.38x slower           |

Benchmark hidden because not significant (1): asyncio_websockets

- Geometric mean (including insignificant results): 1.277x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.28x

# Memory
- memory change: unknown