# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.306x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | Ex                     |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 309 ms: 1.34x slower   |
| docutils       | 1.77 sec | 2.31 sec: 1.30x slower |
| html5lib       | 38.8 ms  | 52.5 ms: 1.35x slower  |
| sphinx         | 702 ms   | 933 ms: 1.33x slower   |
| Geometric mean | (ref)    | 1.33x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | Ex                    |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 312 ms  | 330 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 363 ms  | 444 ms: 1.22x slower  |
| async_tree_cpu_io_mixed    | 359 ms  | 455 ms: 1.27x slower  |
| async_tree_memoization_tg  | 210 ms  | 304 ms: 1.45x slower  |
| async_tree_none_tg         | 167 ms  | 243 ms: 1.46x slower  |
| async_tree_io              | 384 ms  | 570 ms: 1.48x slower  |
| async_tree_memoization     | 210 ms  | 313 ms: 1.49x slower  |
| async_tree_io_tg           | 385 ms  | 576 ms: 1.49x slower  |
| async_tree_none            | 174 ms  | 267 ms: 1.54x slower  |
| async_generators           | 213 ms  | 348 ms: 1.63x slower  |
| coroutines                 | 12.3 ms | 22.4 ms: 1.83x slower |
| Geometric mean             | (ref)   | 1.43x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | Ex                    |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 156 ms: 1.07x slower  |
| float          | 41.4 ms | 78.0 ms: 1.88x slower |
| nbody          | 53.1 ms | 103 ms: 1.95x slower  |
| Geometric mean | (ref)   | 1.58x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | Ex                    |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.87 ms: 1.01x slower |
| regex_dna      | 121 ms  | 123 ms: 1.02x slower  |
| regex_v8       | 16.3 ms | 17.5 ms: 1.07x slower |
| regex_compile  | 81.9 ms | 130 ms: 1.58x slower  |
| Geometric mean | (ref)   | 1.15x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | Ex                     |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 23.3 us: 1.06x slower  |
| xml_etree_parse      | 105 ms   | 112 ms: 1.08x slower   |
| json_dumps           | 7.79 ms  | 9.44 ms: 1.21x slower  |
| xml_etree_iterparse  | 70.4 ms  | 94.3 ms: 1.34x slower  |
| xml_etree_generate   | 64.7 ms  | 92.6 ms: 1.43x slower  |
| xml_etree_process    | 44.7 ms  | 66.9 ms: 1.50x slower  |
| pickle_pure_python   | 223 us   | 364 us: 1.64x slower   |
| tomli_loads          | 1.26 sec | 2.07 sec: 1.64x slower |
| unpickle_pure_python | 148 us   | 284 us: 1.92x slower   |
| Geometric mean       | (ref)    | 1.40x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | Ex                    |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 29.5 ms: 1.12x slower |
| python_startup_no_site | 19.4 ms | 22.0 ms: 1.13x slower |
| Geometric mean         | (ref)   | 1.13x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | Ex                    |
|-----------------|:-------:|:---------------------:|
| django_template | 25.2 ms | 38.0 ms: 1.51x slower |
| mako            | 7.84 ms | 12.1 ms: 1.54x slower |
| genshi_xml      | 31.3 ms | 50.4 ms: 1.61x slower |
| genshi_text     | 14.5 ms | 23.9 ms: 1.65x slower |
| Geometric mean  | (ref)   | 1.58x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | Ex                     |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 44.5 ms  | 21.5 ms: 2.07x faster  |
| many_optionals             | 762 us   | 559 us: 1.36x faster   |
| regex_effbot               | 1.85 ms  | 1.87 ms: 1.01x slower  |
| regex_dna                  | 121 ms   | 123 ms: 1.02x slower   |
| asyncio_websockets         | 312 ms   | 330 ms: 1.06x slower   |
| create_gc_cycles           | 1.34 ms  | 1.42 ms: 1.06x slower  |
| json_loads                 | 21.9 us  | 23.3 us: 1.06x slower  |
| pidigits                   | 146 ms   | 156 ms: 1.07x slower   |
| regex_v8                   | 16.3 ms  | 17.5 ms: 1.07x slower  |
| xml_etree_parse            | 105 ms   | 112 ms: 1.08x slower   |
| json                       | 3.78 ms  | 4.07 ms: 1.08x slower  |
| bench_mp_pool              | 93.6 ms  | 101 ms: 1.08x slower   |
| python_startup             | 26.4 ms  | 29.5 ms: 1.12x slower  |
| python_startup_no_site     | 19.4 ms  | 22.0 ms: 1.13x slower  |
| gc_traversal               | 2.83 ms  | 3.25 ms: 1.15x slower  |
| coverage                   | 55.4 ms  | 63.7 ms: 1.15x slower  |
| sqlite_synth               | 1.68 us  | 1.96 us: 1.17x slower  |
| json_dumps                 | 7.79 ms  | 9.44 ms: 1.21x slower  |
| async_tree_cpu_io_mixed_tg | 363 ms   | 444 ms: 1.22x slower   |
| dulwich_log                | 42.3 ms  | 52.4 ms: 1.24x slower  |
| telco                      | 5.26 ms  | 6.56 ms: 1.25x slower  |
| shortest_path              | 347 ms   | 437 ms: 1.26x slower   |
| async_tree_cpu_io_mixed    | 359 ms   | 455 ms: 1.27x slower   |
| connected_components       | 311 ms   | 395 ms: 1.27x slower   |
| k_core                     | 1.71 sec | 2.18 sec: 1.28x slower |
| thrift                     | 551 us   | 710 us: 1.29x slower   |
| docutils                   | 1.77 sec | 2.31 sec: 1.30x slower |
| mdp                        | 1.44 sec | 1.89 sec: 1.31x slower |
| pylint                     | 205 ms   | 269 ms: 1.31x slower   |
| sphinx                     | 702 ms   | 933 ms: 1.33x slower   |
| meteor_contest             | 74.5 ms  | 99.5 ms: 1.34x slower  |
| 2to3                       | 231 ms   | 309 ms: 1.34x slower   |
| xml_etree_iterparse        | 70.4 ms  | 94.3 ms: 1.34x slower  |
| sympy_sum                  | 91.4 ms  | 123 ms: 1.35x slower   |
| html5lib                   | 38.8 ms  | 52.5 ms: 1.35x slower  |
| sympy_integrate            | 13.4 ms  | 18.4 ms: 1.38x slower  |
| sympy_expand               | 304 ms   | 419 ms: 1.38x slower   |
| sympy_str                  | 177 ms   | 247 ms: 1.40x slower   |
| pycparser                  | 713 ms   | 1.01 sec: 1.42x slower |
| xml_etree_generate         | 64.7 ms  | 92.6 ms: 1.43x slower  |
| async_tree_memoization_tg  | 210 ms   | 304 ms: 1.45x slower   |
| typing_runtime_protocols   | 106 us   | 154 us: 1.45x slower   |
| bench_thread_pool          | 876 us   | 1.28 ms: 1.46x slower  |
| async_tree_none_tg         | 167 ms   | 243 ms: 1.46x slower   |
| sqlglot_v2_optimize        | 36.1 ms  | 52.8 ms: 1.47x slower  |
| bpe_tokeniser              | 3.01 sec | 4.45 sec: 1.48x slower |
| logging_format             | 6.70 us  | 9.92 us: 1.48x slower  |
| async_tree_io              | 384 ms   | 570 ms: 1.48x slower   |
| logging_simple             | 6.25 us  | 9.30 us: 1.49x slower  |
| sqlglot_v2_normalize       | 73.3 ms  | 109 ms: 1.49x slower   |
| async_tree_memoization     | 210 ms   | 313 ms: 1.49x slower   |
| async_tree_io_tg           | 385 ms   | 576 ms: 1.49x slower   |
| pathlib                    | 25.1 ms  | 37.5 ms: 1.49x slower  |
| xml_etree_process          | 44.7 ms  | 66.9 ms: 1.50x slower  |
| django_template            | 25.2 ms  | 38.0 ms: 1.51x slower  |
| deepcopy_reduce            | 1.90 us  | 2.86 us: 1.51x slower  |
| async_tree_none            | 174 ms   | 267 ms: 1.54x slower   |
| mako                       | 7.84 ms  | 12.1 ms: 1.54x slower  |
| deepcopy                   | 180 us   | 278 us: 1.54x slower   |
| regex_compile              | 81.9 ms  | 130 ms: 1.58x slower   |
| pprint_pformat             | 1.04 sec | 1.66 sec: 1.60x slower |
| genshi_xml                 | 31.3 ms  | 50.4 ms: 1.61x slower  |
| pprint_safe_repr           | 510 ms   | 825 ms: 1.62x slower   |
| nqueens                    | 59.6 ms  | 96.9 ms: 1.62x slower  |
| async_generators           | 213 ms   | 348 ms: 1.63x slower   |
| scimark_fft                | 169 ms   | 276 ms: 1.64x slower   |
| pickle_pure_python         | 223 us   | 364 us: 1.64x slower   |
| tomli_loads                | 1.26 sec | 2.07 sec: 1.64x slower |
| genshi_text                | 14.5 ms  | 23.9 ms: 1.65x slower  |
| sqlglot_v2_transpile       | 1.01 ms  | 1.69 ms: 1.66x slower  |
| crypto_pyaes               | 48.0 ms  | 80.1 ms: 1.67x slower  |
| fannkuch                   | 250 ms   | 418 ms: 1.67x slower   |
| pyflate                    | 274 ms   | 477 ms: 1.74x slower   |
| sqlglot_v2_parse           | 798 us   | 1.41 ms: 1.76x slower  |
| deepcopy_memo              | 19.3 us  | 34.0 us: 1.77x slower  |
| comprehensions             | 11.3 us  | 20.1 us: 1.78x slower  |
| scimark_sparse_mat_mult    | 2.47 ms  | 4.43 ms: 1.80x slower  |
| coroutines                 | 12.3 ms  | 22.4 ms: 1.83x slower  |
| chaos                      | 37.7 ms  | 69.3 ms: 1.84x slower  |
| raytrace                   | 169 ms   | 313 ms: 1.85x slower   |
| scimark_lu                 | 64.2 ms  | 119 ms: 1.86x slower   |
| float                      | 41.4 ms  | 78.0 ms: 1.88x slower  |
| richards_super             | 35.8 ms  | 67.7 ms: 1.89x slower  |
| hexiom                     | 3.92 ms  | 7.44 ms: 1.90x slower  |
| richards                   | 30.9 ms  | 59.0 ms: 1.91x slower  |
| unpickle_pure_python       | 148 us   | 284 us: 1.92x slower   |
| scimark_monte_carlo        | 38.9 ms  | 75.8 ms: 1.95x slower  |
| nbody                      | 53.1 ms  | 103 ms: 1.95x slower   |
| spectral_norm              | 51.1 ms  | 102 ms: 1.99x slower   |
| go                         | 70.4 ms  | 140 ms: 1.99x slower   |
| scimark_sor                | 68.6 ms  | 139 ms: 2.02x slower   |
| logging_silent             | 61.1 ns  | 124 ns: 2.03x slower   |
| generators                 | 16.3 ms  | 35.6 ms: 2.18x slower  |
| deltablue                  | 1.91 ms  | 4.22 ms: 2.21x slower  |
| Geometric mean             | (ref)    | 1.45x slower           |

- Geometric mean (including insignificant results): 1.306x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.41x
- 95% likely to have a slowdown of 1.39x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: unknown