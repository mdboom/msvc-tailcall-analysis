# Results vs. base

- fork: unknown
- ref: clang-main
- machine: unknown-unknown
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | clang-main             |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 220 ms: 1.36x faster   |
| docutils       | 2.17 sec | 1.65 sec: 1.31x faster |
| html5lib       | 51.3 ms  | 39.0 ms: 1.31x faster  |
| sphinx         | 872 ms   | 653 ms: 1.33x faster   |
| Geometric mean | (ref)    | 1.33x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | clang-main            |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 317 ms  | 158 ms: 2.01x faster  |
| coroutines                 | 21.9 ms | 13.4 ms: 1.63x faster |
| async_generators           | 328 ms  | 223 ms: 1.47x faster  |
| async_tree_memoization     | 297 ms  | 216 ms: 1.38x faster  |
| async_tree_io_tg           | 559 ms  | 407 ms: 1.37x faster  |
| async_tree_memoization_tg  | 291 ms  | 215 ms: 1.35x faster  |
| async_tree_none_tg         | 236 ms  | 176 ms: 1.35x faster  |
| async_tree_none            | 249 ms  | 185 ms: 1.35x faster  |
| async_tree_io              | 553 ms  | 416 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 337 ms: 1.30x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 342 ms: 1.24x faster  |
| Geometric mean             | (ref)   | 1.42x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | clang-main            |
|----------------|:-------:|:---------------------:|
| float          | 75.4 ms | 44.7 ms: 1.69x faster |
| nbody          | 101 ms  | 64.2 ms: 1.57x faster |
| pidigits       | 152 ms  | 149 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.39x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | clang-main            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 82.3 ms: 1.51x faster |
| regex_effbot   | 1.81 ms | 1.39 ms: 1.30x faster |
| regex_v8       | 17.1 ms | 13.4 ms: 1.28x faster |
| regex_dna      | 121 ms  | 114 ms: 1.06x faster  |
| Geometric mean | (ref)   | 1.28x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | clang-main             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 140 us: 1.96x faster   |
| pickle_pure_python   | 355 us   | 216 us: 1.64x faster   |
| xml_etree_process    | 64.6 ms  | 40.9 ms: 1.58x faster  |
| xml_etree_generate   | 89.5 ms  | 57.2 ms: 1.56x faster  |
| json_loads           | 22.3 us  | 15.1 us: 1.48x faster  |
| tomli_loads          | 1.99 sec | 1.41 sec: 1.41x faster |
| xml_etree_iterparse  | 89.9 ms  | 64.1 ms: 1.40x faster  |
| json_dumps           | 9.01 ms  | 6.78 ms: 1.33x faster  |
| xml_etree_parse      | 108 ms   | 87.6 ms: 1.23x faster  |
| Geometric mean       | (ref)    | 1.50x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | default | clang-main            |
|----------------|:-------:|:---------------------:|
| python_startup | 27.3 ms | 25.8 ms: 1.06x faster |
| Geometric mean | (ref)   | 1.03x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | default | clang-main            |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 6.71 ms: 1.74x faster |
| genshi_text     | 23.2 ms | 15.8 ms: 1.47x faster |
| django_template | 36.9 ms | 25.4 ms: 1.45x faster |
| genshi_xml      | 48.8 ms | 34.2 ms: 1.43x faster |
| Geometric mean  | (ref)   | 1.52x faster          |

All benchmarks:
===============

| Benchmark                  | default  | clang-main             |
|----------------------------|:--------:|:----------------------:|
| mdp                        | 1.81 sec | 799 ms: 2.27x faster   |
| logging_silent             | 119 ns   | 56.3 ns: 2.12x faster  |
| richards_super             | 65.8 ms  | 31.5 ms: 2.09x faster  |
| richards                   | 57.8 ms  | 27.8 ms: 2.08x faster  |
| asyncio_websockets         | 317 ms   | 158 ms: 2.01x faster   |
| unpickle_pure_python       | 274 us   | 140 us: 1.96x faster   |
| deltablue                  | 4.09 ms  | 2.12 ms: 1.93x faster  |
| scimark_lu                 | 116 ms   | 61.6 ms: 1.89x faster  |
| generators                 | 33.8 ms  | 17.9 ms: 1.88x faster  |
| spectral_norm              | 97.7 ms  | 55.1 ms: 1.77x faster  |
| hexiom                     | 7.27 ms  | 4.12 ms: 1.77x faster  |
| scimark_sor                | 135 ms   | 76.7 ms: 1.76x faster  |
| mako                       | 11.7 ms  | 6.71 ms: 1.74x faster  |
| deepcopy_memo              | 32.9 us  | 19.1 us: 1.72x faster  |
| scimark_monte_carlo        | 73.9 ms  | 43.5 ms: 1.70x faster  |
| go                         | 137 ms   | 80.8 ms: 1.69x faster  |
| float                      | 75.4 ms  | 44.7 ms: 1.69x faster  |
| comprehensions             | 19.4 us  | 11.5 us: 1.69x faster  |
| raytrace                   | 304 ms   | 181 ms: 1.68x faster   |
| crypto_pyaes               | 77.9 ms  | 47.3 ms: 1.65x faster  |
| pickle_pure_python         | 355 us   | 216 us: 1.64x faster   |
| coroutines                 | 21.9 ms  | 13.4 ms: 1.63x faster  |
| chaos                      | 65.2 ms  | 40.2 ms: 1.62x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.69 ms: 1.62x faster  |
| sqlglot_v2_parse           | 1.36 ms  | 851 us: 1.60x faster   |
| pyflate                    | 462 ms   | 291 ms: 1.59x faster   |
| xml_etree_process          | 64.6 ms  | 40.9 ms: 1.58x faster  |
| nbody                      | 101 ms   | 64.2 ms: 1.57x faster  |
| fannkuch                   | 407 ms   | 260 ms: 1.57x faster   |
| xml_etree_generate         | 89.5 ms  | 57.2 ms: 1.56x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 1.05 ms: 1.56x faster  |
| gc_traversal               | 3.15 ms  | 2.08 ms: 1.52x faster  |
| regex_compile              | 125 ms   | 82.3 ms: 1.51x faster  |
| pprint_safe_repr           | 788 ms   | 521 ms: 1.51x faster   |
| pprint_pformat             | 1.61 sec | 1.07 sec: 1.51x faster |
| deepcopy                   | 269 us   | 180 us: 1.49x faster   |
| nqueens                    | 94.3 ms  | 63.5 ms: 1.49x faster  |
| json_loads                 | 22.3 us  | 15.1 us: 1.48x faster  |
| deepcopy_reduce            | 2.77 us  | 1.88 us: 1.47x faster  |
| bpe_tokeniser              | 4.30 sec | 2.93 sec: 1.47x faster |
| async_generators           | 328 ms   | 223 ms: 1.47x faster   |
| genshi_text                | 23.2 ms  | 15.8 ms: 1.47x faster  |
| scimark_fft                | 269 ms   | 185 ms: 1.45x faster   |
| sqlglot_v2_optimize        | 51.0 ms  | 35.1 ms: 1.45x faster  |
| django_template            | 36.9 ms  | 25.4 ms: 1.45x faster  |
| sqlglot_v2_normalize       | 106 ms   | 73.4 ms: 1.45x faster  |
| genshi_xml                 | 48.8 ms  | 34.2 ms: 1.43x faster  |
| tomli_loads                | 1.99 sec | 1.41 sec: 1.41x faster |
| typing_runtime_protocols   | 150 us   | 107 us: 1.40x faster   |
| xml_etree_iterparse        | 89.9 ms  | 64.1 ms: 1.40x faster  |
| logging_simple             | 8.87 us  | 6.39 us: 1.39x faster  |
| sympy_integrate            | 17.8 ms  | 12.9 ms: 1.38x faster  |
| async_tree_memoization     | 297 ms   | 216 ms: 1.38x faster   |
| async_tree_io_tg           | 559 ms   | 407 ms: 1.37x faster   |
| pycparser                  | 992 ms   | 728 ms: 1.36x faster   |
| sympy_str                  | 238 ms   | 175 ms: 1.36x faster   |
| logging_format             | 9.33 us  | 6.88 us: 1.36x faster  |
| 2to3                       | 298 ms   | 220 ms: 1.36x faster   |
| async_tree_memoization_tg  | 291 ms   | 215 ms: 1.35x faster   |
| sympy_expand               | 405 ms   | 301 ms: 1.35x faster   |
| async_tree_none_tg         | 236 ms   | 176 ms: 1.35x faster   |
| async_tree_none            | 249 ms   | 185 ms: 1.35x faster   |
| sphinx                     | 872 ms   | 653 ms: 1.33x faster   |
| sympy_sum                  | 119 ms   | 89.6 ms: 1.33x faster  |
| json_dumps                 | 9.01 ms  | 6.78 ms: 1.33x faster  |
| async_tree_io              | 553 ms   | 416 ms: 1.33x faster   |
| telco                      | 6.44 ms  | 4.87 ms: 1.32x faster  |
| html5lib                   | 51.3 ms  | 39.0 ms: 1.31x faster  |
| docutils                   | 2.17 sec | 1.65 sec: 1.31x faster |
| subparsers                 | 20.8 ms  | 15.9 ms: 1.31x faster  |
| regex_effbot               | 1.81 ms  | 1.39 ms: 1.30x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 337 ms: 1.30x faster   |
| json                       | 3.96 ms  | 3.09 ms: 1.28x faster  |
| coverage                   | 61.9 ms  | 48.3 ms: 1.28x faster  |
| regex_v8                   | 17.1 ms  | 13.4 ms: 1.28x faster  |
| many_optionals             | 547 us   | 432 us: 1.27x faster   |
| pylint                     | 253 ms   | 200 ms: 1.26x faster   |
| meteor_contest             | 95.9 ms  | 76.2 ms: 1.26x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 342 ms: 1.24x faster   |
| xml_etree_parse            | 108 ms   | 87.6 ms: 1.23x faster  |
| dulwich_log                | 51.0 ms  | 42.1 ms: 1.21x faster  |
| sqlite_synth               | 1.84 us  | 1.58 us: 1.17x faster  |
| bench_thread_pool          | 1.01 ms  | 864 us: 1.16x faster   |
| create_gc_cycles           | 1.40 ms  | 1.25 ms: 1.13x faster  |
| bench_mp_pool              | 96.2 ms  | 88.9 ms: 1.08x faster  |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| pathlib                    | 34.4 ms  | 32.5 ms: 1.06x faster  |
| regex_dna                  | 121 ms   | 114 ms: 1.06x faster   |
| python_startup             | 27.3 ms  | 25.8 ms: 1.06x faster  |
| shortest_path              | 378 ms   | 366 ms: 1.03x faster   |
| connected_components       | 347 ms   | 336 ms: 1.03x faster   |
| pidigits                   | 152 ms   | 149 ms: 1.02x faster   |
| Geometric mean             | (ref)    | 1.44x faster           |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (1) of default.json: thrift
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown