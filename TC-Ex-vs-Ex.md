# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 231 ms: 1.34x faster   |
| docutils       | 2.31 sec | 1.77 sec: 1.30x faster |
| html5lib       | 52.5 ms  | 38.8 ms: 1.35x faster  |
| sphinx         | 933 ms   | 702 ms: 1.33x faster   |
| Geometric mean | (ref)    | 1.33x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 12.3 ms: 1.83x faster |
| async_generators           | 348 ms  | 213 ms: 1.63x faster  |
| async_tree_none            | 267 ms  | 174 ms: 1.54x faster  |
| async_tree_io_tg           | 576 ms  | 385 ms: 1.49x faster  |
| async_tree_memoization     | 313 ms  | 210 ms: 1.49x faster  |
| async_tree_io              | 570 ms  | 384 ms: 1.48x faster  |
| async_tree_none_tg         | 243 ms  | 167 ms: 1.46x faster  |
| async_tree_memoization_tg  | 304 ms  | 210 ms: 1.45x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 359 ms: 1.27x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 363 ms: 1.22x faster  |
| asyncio_websockets         | 330 ms  | 312 ms: 1.06x faster  |
| Geometric mean             | (ref)   | 1.43x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 53.1 ms: 1.95x faster |
| float          | 78.0 ms | 41.4 ms: 1.88x faster |
| pidigits       | 156 ms  | 146 ms: 1.07x faster  |
| Geometric mean | (ref)   | 1.58x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 81.9 ms: 1.58x faster |
| regex_v8       | 17.5 ms | 16.3 ms: 1.07x faster |
| regex_dna      | 123 ms  | 121 ms: 1.02x faster  |
| regex_effbot   | 1.87 ms | 1.85 ms: 1.01x faster |
| Geometric mean | (ref)   | 1.15x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 148 us: 1.92x faster   |
| tomli_loads          | 2.07 sec | 1.26 sec: 1.64x faster |
| pickle_pure_python   | 364 us   | 223 us: 1.64x faster   |
| xml_etree_process    | 66.9 ms  | 44.7 ms: 1.50x faster  |
| xml_etree_generate   | 92.6 ms  | 64.7 ms: 1.43x faster  |
| xml_etree_iterparse  | 94.3 ms  | 70.4 ms: 1.34x faster  |
| json_dumps           | 9.44 ms  | 7.79 ms: 1.21x faster  |
| xml_etree_parse      | 112 ms   | 105 ms: 1.08x faster   |
| json_loads           | 23.3 us  | 21.9 us: 1.06x faster  |
| Geometric mean       | (ref)    | 1.40x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 22.0 ms | 19.4 ms: 1.13x faster |
| python_startup         | 29.5 ms | 26.4 ms: 1.12x faster |
| Geometric mean         | (ref)   | 1.13x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TC-Ex                 |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 23.9 ms | 14.5 ms: 1.65x faster |
| genshi_xml      | 50.4 ms | 31.3 ms: 1.61x faster |
| mako            | 12.1 ms | 7.84 ms: 1.54x faster |
| django_template | 38.0 ms | 25.2 ms: 1.51x faster |
| Geometric mean  | (ref)   | 1.58x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.22 ms  | 1.91 ms: 2.21x faster  |
| generators                 | 35.6 ms  | 16.3 ms: 2.18x faster  |
| logging_silent             | 124 ns   | 61.1 ns: 2.03x faster  |
| scimark_sor                | 139 ms   | 68.6 ms: 2.02x faster  |
| go                         | 140 ms   | 70.4 ms: 1.99x faster  |
| spectral_norm              | 102 ms   | 51.1 ms: 1.99x faster  |
| nbody                      | 103 ms   | 53.1 ms: 1.95x faster  |
| scimark_monte_carlo        | 75.8 ms  | 38.9 ms: 1.95x faster  |
| unpickle_pure_python       | 284 us   | 148 us: 1.92x faster   |
| richards                   | 59.0 ms  | 30.9 ms: 1.91x faster  |
| hexiom                     | 7.44 ms  | 3.92 ms: 1.90x faster  |
| richards_super             | 67.7 ms  | 35.8 ms: 1.89x faster  |
| float                      | 78.0 ms  | 41.4 ms: 1.88x faster  |
| scimark_lu                 | 119 ms   | 64.2 ms: 1.86x faster  |
| raytrace                   | 313 ms   | 169 ms: 1.85x faster   |
| chaos                      | 69.3 ms  | 37.7 ms: 1.84x faster  |
| coroutines                 | 22.4 ms  | 12.3 ms: 1.83x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.47 ms: 1.80x faster  |
| comprehensions             | 20.1 us  | 11.3 us: 1.78x faster  |
| deepcopy_memo              | 34.0 us  | 19.3 us: 1.77x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 798 us: 1.76x faster   |
| pyflate                    | 477 ms   | 274 ms: 1.74x faster   |
| fannkuch                   | 418 ms   | 250 ms: 1.67x faster   |
| crypto_pyaes               | 80.1 ms  | 48.0 ms: 1.67x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 1.01 ms: 1.66x faster  |
| genshi_text                | 23.9 ms  | 14.5 ms: 1.65x faster  |
| tomli_loads                | 2.07 sec | 1.26 sec: 1.64x faster |
| pickle_pure_python         | 364 us   | 223 us: 1.64x faster   |
| scimark_fft                | 276 ms   | 169 ms: 1.64x faster   |
| async_generators           | 348 ms   | 213 ms: 1.63x faster   |
| nqueens                    | 96.9 ms  | 59.6 ms: 1.62x faster  |
| pprint_safe_repr           | 825 ms   | 510 ms: 1.62x faster   |
| genshi_xml                 | 50.4 ms  | 31.3 ms: 1.61x faster  |
| pprint_pformat             | 1.66 sec | 1.04 sec: 1.60x faster |
| regex_compile              | 130 ms   | 81.9 ms: 1.58x faster  |
| deepcopy                   | 278 us   | 180 us: 1.54x faster   |
| mako                       | 12.1 ms  | 7.84 ms: 1.54x faster  |
| async_tree_none            | 267 ms   | 174 ms: 1.54x faster   |
| deepcopy_reduce            | 2.86 us  | 1.90 us: 1.51x faster  |
| django_template            | 38.0 ms  | 25.2 ms: 1.51x faster  |
| xml_etree_process          | 66.9 ms  | 44.7 ms: 1.50x faster  |
| pathlib                    | 37.5 ms  | 25.1 ms: 1.49x faster  |
| async_tree_io_tg           | 576 ms   | 385 ms: 1.49x faster   |
| async_tree_memoization     | 313 ms   | 210 ms: 1.49x faster   |
| sqlglot_v2_normalize       | 109 ms   | 73.3 ms: 1.49x faster  |
| logging_simple             | 9.30 us  | 6.25 us: 1.49x faster  |
| async_tree_io              | 570 ms   | 384 ms: 1.48x faster   |
| logging_format             | 9.92 us  | 6.70 us: 1.48x faster  |
| bpe_tokeniser              | 4.45 sec | 3.01 sec: 1.48x faster |
| sqlglot_v2_optimize        | 52.8 ms  | 36.1 ms: 1.47x faster  |
| async_tree_none_tg         | 243 ms   | 167 ms: 1.46x faster   |
| bench_thread_pool          | 1.28 ms  | 876 us: 1.46x faster   |
| typing_runtime_protocols   | 154 us   | 106 us: 1.45x faster   |
| async_tree_memoization_tg  | 304 ms   | 210 ms: 1.45x faster   |
| xml_etree_generate         | 92.6 ms  | 64.7 ms: 1.43x faster  |
| pycparser                  | 1.01 sec | 713 ms: 1.42x faster   |
| sympy_str                  | 247 ms   | 177 ms: 1.40x faster   |
| sympy_expand               | 419 ms   | 304 ms: 1.38x faster   |
| sympy_integrate            | 18.4 ms  | 13.4 ms: 1.38x faster  |
| html5lib                   | 52.5 ms  | 38.8 ms: 1.35x faster  |
| sympy_sum                  | 123 ms   | 91.4 ms: 1.35x faster  |
| xml_etree_iterparse        | 94.3 ms  | 70.4 ms: 1.34x faster  |
| 2to3                       | 309 ms   | 231 ms: 1.34x faster   |
| meteor_contest             | 99.5 ms  | 74.5 ms: 1.34x faster  |
| sphinx                     | 933 ms   | 702 ms: 1.33x faster   |
| pylint                     | 269 ms   | 205 ms: 1.31x faster   |
| mdp                        | 1.89 sec | 1.44 sec: 1.31x faster |
| docutils                   | 2.31 sec | 1.77 sec: 1.30x faster |
| thrift                     | 710 us   | 551 us: 1.29x faster   |
| k_core                     | 2.18 sec | 1.71 sec: 1.28x faster |
| connected_components       | 395 ms   | 311 ms: 1.27x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 359 ms: 1.27x faster   |
| shortest_path              | 437 ms   | 347 ms: 1.26x faster   |
| telco                      | 6.56 ms  | 5.26 ms: 1.25x faster  |
| dulwich_log                | 52.4 ms  | 42.3 ms: 1.24x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 363 ms: 1.22x faster   |
| json_dumps                 | 9.44 ms  | 7.79 ms: 1.21x faster  |
| sqlite_synth               | 1.96 us  | 1.68 us: 1.17x faster  |
| coverage                   | 63.7 ms  | 55.4 ms: 1.15x faster  |
| gc_traversal               | 3.25 ms  | 2.83 ms: 1.15x faster  |
| python_startup_no_site     | 22.0 ms  | 19.4 ms: 1.13x faster  |
| python_startup             | 29.5 ms  | 26.4 ms: 1.12x faster  |
| bench_mp_pool              | 101 ms   | 93.6 ms: 1.08x faster  |
| json                       | 4.07 ms  | 3.78 ms: 1.08x faster  |
| xml_etree_parse            | 112 ms   | 105 ms: 1.08x faster   |
| regex_v8                   | 17.5 ms  | 16.3 ms: 1.07x faster  |
| pidigits                   | 156 ms   | 146 ms: 1.07x faster   |
| json_loads                 | 23.3 us  | 21.9 us: 1.06x faster  |
| create_gc_cycles           | 1.42 ms  | 1.34 ms: 1.06x faster  |
| asyncio_websockets         | 330 ms   | 312 ms: 1.06x faster   |
| regex_dna                  | 123 ms   | 121 ms: 1.02x faster   |
| regex_effbot               | 1.87 ms  | 1.85 ms: 1.01x faster  |
| many_optionals             | 559 us   | 762 us: 1.36x slower   |
| subparsers                 | 21.5 ms  | 44.5 ms: 2.07x slower  |
| Geometric mean             | (ref)    | 1.45x faster           |

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.39x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown