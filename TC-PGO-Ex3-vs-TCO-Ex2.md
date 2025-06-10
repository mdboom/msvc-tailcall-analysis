# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.611x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 204 ms: 1.44x faster   |
| docutils       | 2.11 sec | 1.58 sec: 1.34x faster |
| html5lib       | 51.3 ms  | 35.5 ms: 1.45x faster  |
| sphinx         | 843 ms   | 615 ms: 1.37x faster   |
| Geometric mean | (ref)    | 1.40x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.1 ms | 10.8 ms: 2.05x faster |
| async_generators           | 321 ms  | 199 ms: 1.62x faster  |
| async_tree_io_tg           | 563 ms  | 356 ms: 1.58x faster  |
| async_tree_none            | 248 ms  | 157 ms: 1.58x faster  |
| async_tree_none_tg         | 236 ms  | 150 ms: 1.57x faster  |
| async_tree_io              | 551 ms  | 353 ms: 1.56x faster  |
| async_tree_memoization     | 297 ms  | 196 ms: 1.51x faster  |
| async_tree_memoization_tg  | 292 ms  | 201 ms: 1.45x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 327 ms: 1.33x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms  | 325 ms: 1.32x faster  |
| asyncio_websockets         | 311 ms  | 304 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.49x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 45.7 ms: 2.16x faster |
| float          | 73.5 ms | 37.1 ms: 1.98x faster |
| pidigits       | 148 ms  | 145 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.63x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 70.7 ms: 1.74x faster |
| regex_effbot   | 1.77 ms | 1.45 ms: 1.22x faster |
| regex_v8       | 17.0 ms | 13.9 ms: 1.22x faster |
| regex_dna      | 118 ms  | 121 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.26x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 110 us: 2.48x faster   |
| pickle_pure_python   | 354 us   | 184 us: 1.93x faster   |
| tomli_loads          | 1.97 sec | 1.03 sec: 1.91x faster |
| xml_etree_process    | 63.0 ms  | 33.8 ms: 1.87x faster  |
| xml_etree_generate   | 87.5 ms  | 49.4 ms: 1.77x faster  |
| xml_etree_iterparse  | 87.5 ms  | 59.5 ms: 1.47x faster  |
| json_dumps           | 8.99 ms  | 6.19 ms: 1.45x faster  |
| json_loads           | 21.4 us  | 14.8 us: 1.45x faster  |
| xml_etree_parse      | 108 ms   | 89.4 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.69x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.2 ms | 24.7 ms: 1.10x faster |
| python_startup_no_site | 20.3 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.09x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| mako            | 11.4 ms | 5.80 ms: 1.97x faster |
| genshi_text     | 23.4 ms | 12.3 ms: 1.89x faster |
| django_template | 35.8 ms | 20.9 ms: 1.71x faster |
| genshi_xml      | 48.8 ms | 29.5 ms: 1.66x faster |
| Geometric mean  | (ref)   | 1.80x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 121 ns   | 44.1 ns: 2.76x faster  |
| scimark_lu                 | 116 ms   | 44.3 ms: 2.61x faster  |
| scimark_sor                | 133 ms   | 51.1 ms: 2.61x faster  |
| deltablue                  | 4.08 ms  | 1.64 ms: 2.48x faster  |
| unpickle_pure_python       | 271 us   | 110 us: 2.48x faster   |
| hexiom                     | 7.27 ms  | 3.00 ms: 2.43x faster  |
| scimark_monte_carlo        | 75.2 ms  | 31.5 ms: 2.39x faster  |
| spectral_norm              | 97.1 ms  | 40.9 ms: 2.37x faster  |
| generators                 | 33.5 ms  | 14.2 ms: 2.35x faster  |
| go                         | 138 ms   | 61.0 ms: 2.27x faster  |
| deepcopy_memo              | 33.0 us  | 14.7 us: 2.25x faster  |
| comprehensions             | 19.4 us  | 8.65 us: 2.24x faster  |
| nbody                      | 98.8 ms  | 45.7 ms: 2.16x faster  |
| chaos                      | 67.0 ms  | 31.3 ms: 2.14x faster  |
| scimark_sparse_mat_mult    | 4.27 ms  | 2.02 ms: 2.11x faster  |
| raytrace                   | 306 ms   | 145 ms: 2.11x faster   |
| coroutines                 | 22.1 ms  | 10.8 ms: 2.05x faster  |
| richards                   | 51.0 ms  | 25.5 ms: 2.00x faster  |
| float                      | 73.5 ms  | 37.1 ms: 1.98x faster  |
| mako                       | 11.4 ms  | 5.80 ms: 1.97x faster  |
| richards_super             | 58.0 ms  | 29.4 ms: 1.97x faster  |
| sqlglot_v2_parse           | 1.34 ms  | 695 us: 1.94x faster   |
| pyflate                    | 457 ms   | 236 ms: 1.94x faster   |
| pickle_pure_python         | 354 us   | 184 us: 1.93x faster   |
| tomli_loads                | 1.97 sec | 1.03 sec: 1.91x faster |
| scimark_fft                | 267 ms   | 140 ms: 1.91x faster   |
| crypto_pyaes               | 76.8 ms  | 40.4 ms: 1.90x faster  |
| fannkuch                   | 386 ms   | 203 ms: 1.90x faster   |
| pprint_pformat             | 1.61 sec | 853 ms: 1.89x faster   |
| genshi_text                | 23.4 ms  | 12.3 ms: 1.89x faster  |
| nqueens                    | 93.2 ms  | 49.7 ms: 1.87x faster  |
| xml_etree_process          | 63.0 ms  | 33.8 ms: 1.87x faster  |
| pprint_safe_repr           | 789 ms   | 429 ms: 1.84x faster   |
| deepcopy                   | 266 us   | 147 us: 1.82x faster   |
| sqlglot_v2_transpile       | 1.62 ms  | 894 us: 1.81x faster   |
| deepcopy_reduce            | 2.71 us  | 1.51 us: 1.79x faster  |
| xml_etree_generate         | 87.5 ms  | 49.4 ms: 1.77x faster  |
| regex_compile              | 123 ms   | 70.7 ms: 1.74x faster  |
| django_template            | 35.8 ms  | 20.9 ms: 1.71x faster  |
| bpe_tokeniser              | 4.30 sec | 2.52 sec: 1.71x faster |
| genshi_xml                 | 48.8 ms  | 29.5 ms: 1.66x faster  |
| sqlglot_v2_normalize       | 103 ms   | 62.6 ms: 1.65x faster  |
| typing_runtime_protocols   | 146 us   | 89.7 us: 1.63x faster  |
| sqlglot_v2_optimize        | 49.6 ms  | 30.5 ms: 1.63x faster  |
| async_generators           | 321 ms   | 199 ms: 1.62x faster   |
| logging_simple             | 8.63 us  | 5.42 us: 1.59x faster  |
| async_tree_io_tg           | 563 ms   | 356 ms: 1.58x faster   |
| async_tree_none            | 248 ms   | 157 ms: 1.58x faster   |
| async_tree_none_tg         | 236 ms   | 150 ms: 1.57x faster   |
| async_tree_io              | 551 ms   | 353 ms: 1.56x faster   |
| logging_format             | 9.13 us  | 5.90 us: 1.55x faster  |
| sympy_str                  | 234 ms   | 153 ms: 1.53x faster   |
| sympy_expand               | 399 ms   | 263 ms: 1.52x faster   |
| async_tree_memoization     | 297 ms   | 196 ms: 1.51x faster   |
| pycparser                  | 968 ms   | 642 ms: 1.51x faster   |
| thrift                     | 680 us   | 461 us: 1.47x faster   |
| xml_etree_iterparse        | 87.5 ms  | 59.5 ms: 1.47x faster  |
| sympy_integrate            | 17.5 ms  | 12.0 ms: 1.46x faster  |
| sympy_sum                  | 118 ms   | 80.7 ms: 1.46x faster  |
| async_tree_memoization_tg  | 292 ms   | 201 ms: 1.45x faster   |
| json_dumps                 | 8.99 ms  | 6.19 ms: 1.45x faster  |
| json_loads                 | 21.4 us  | 14.8 us: 1.45x faster  |
| html5lib                   | 51.3 ms  | 35.5 ms: 1.45x faster  |
| 2to3                       | 293 ms   | 204 ms: 1.44x faster   |
| meteor_contest             | 95.0 ms  | 66.6 ms: 1.43x faster  |
| telco                      | 6.34 ms  | 4.45 ms: 1.43x faster  |
| sphinx                     | 843 ms   | 615 ms: 1.37x faster   |
| many_optionals             | 890 us   | 659 us: 1.35x faster   |
| docutils                   | 2.11 sec | 1.58 sec: 1.34x faster |
| gc_traversal               | 2.79 ms  | 2.09 ms: 1.33x faster  |
| json                       | 3.94 ms  | 2.95 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 434 ms   | 327 ms: 1.33x faster   |
| coverage                   | 61.1 ms  | 46.2 ms: 1.32x faster  |
| async_tree_cpu_io_mixed_tg | 428 ms   | 325 ms: 1.32x faster   |
| mdp                        | 1.82 sec | 1.41 sec: 1.30x faster |
| pylint                     | 249 ms   | 193 ms: 1.29x faster   |
| dulwich_log                | 50.5 ms  | 39.1 ms: 1.29x faster  |
| subparsers                 | 50.4 ms  | 40.6 ms: 1.24x faster  |
| regex_effbot               | 1.77 ms  | 1.45 ms: 1.22x faster  |
| regex_v8                   | 17.0 ms  | 13.9 ms: 1.22x faster  |
| xml_etree_parse            | 108 ms   | 89.4 ms: 1.21x faster  |
| sqlite_synth               | 1.78 us  | 1.56 us: 1.15x faster  |
| pathlib                    | 26.8 ms  | 23.6 ms: 1.14x faster  |
| create_gc_cycles           | 1.40 ms  | 1.26 ms: 1.11x faster  |
| shortest_path              | 384 ms   | 347 ms: 1.10x faster   |
| python_startup             | 27.2 ms  | 24.7 ms: 1.10x faster  |
| k_core                     | 1.83 sec | 1.67 sec: 1.10x faster |
| connected_components       | 351 ms   | 320 ms: 1.09x faster   |
| python_startup_no_site     | 20.3 ms  | 18.7 ms: 1.09x faster  |
| asyncio_websockets         | 311 ms   | 304 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 145 ms: 1.02x faster   |
| regex_dna                  | 118 ms   | 121 ms: 1.03x slower   |
| Geometric mean             | (ref)    | 1.62x faster           |
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.611x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.50x
- 95% likely to have a speedup of 1.48x
- 99% likely to have a speedup of 1.45x

# Memory
- memory change: unknown