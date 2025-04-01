# Results vs. base

- fork: unknown
- ref: clang-main
- machine: unknown-unknown
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.502x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | clang-main             |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 220 ms: 1.40x faster   |
| docutils       | 2.31 sec | 1.65 sec: 1.39x faster |
| html5lib       | 52.5 ms  | 39.0 ms: 1.35x faster  |
| sphinx         | 933 ms   | 653 ms: 1.43x faster   |
| Geometric mean | (ref)    | 1.39x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | clang-main            |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 330 ms  | 158 ms: 2.09x faster  |
| coroutines                 | 22.4 ms | 13.4 ms: 1.67x faster |
| async_generators           | 348 ms  | 223 ms: 1.56x faster  |
| async_tree_memoization     | 313 ms  | 216 ms: 1.45x faster  |
| async_tree_none            | 267 ms  | 185 ms: 1.44x faster  |
| async_tree_memoization_tg  | 304 ms  | 215 ms: 1.42x faster  |
| async_tree_io_tg           | 576 ms  | 407 ms: 1.41x faster  |
| async_tree_none_tg         | 243 ms  | 176 ms: 1.39x faster  |
| async_tree_io              | 570 ms  | 416 ms: 1.37x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 337 ms: 1.35x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 342 ms: 1.30x faster  |
| Geometric mean             | (ref)   | 1.48x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | clang-main            |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 44.7 ms: 1.75x faster |
| nbody          | 103 ms  | 64.2 ms: 1.61x faster |
| pidigits       | 156 ms  | 149 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.43x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | clang-main            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 82.3 ms: 1.58x faster |
| regex_effbot   | 1.87 ms | 1.39 ms: 1.34x faster |
| regex_v8       | 17.5 ms | 13.4 ms: 1.31x faster |
| regex_dna      | 123 ms  | 114 ms: 1.08x faster  |
| Geometric mean | (ref)   | 1.31x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | clang-main             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 140 us: 2.03x faster   |
| pickle_pure_python   | 364 us   | 216 us: 1.69x faster   |
| xml_etree_process    | 66.9 ms  | 40.9 ms: 1.64x faster  |
| xml_etree_generate   | 92.6 ms  | 57.2 ms: 1.62x faster  |
| json_loads           | 23.3 us  | 15.1 us: 1.54x faster  |
| xml_etree_iterparse  | 94.3 ms  | 64.1 ms: 1.47x faster  |
| tomli_loads          | 2.07 sec | 1.41 sec: 1.47x faster |
| json_dumps           | 9.44 ms  | 6.78 ms: 1.39x faster  |
| xml_etree_parse      | 112 ms   | 87.6 ms: 1.28x faster  |
| Geometric mean       | (ref)    | 1.56x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | clang-main            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 25.8 ms: 1.14x faster |
| python_startup_no_site | 22.0 ms | 20.4 ms: 1.08x faster |
| Geometric mean         | (ref)   | 1.11x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | clang-main            |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.71 ms: 1.80x faster |
| genshi_text     | 23.9 ms | 15.8 ms: 1.51x faster |
| django_template | 38.0 ms | 25.4 ms: 1.50x faster |
| genshi_xml      | 50.4 ms | 34.2 ms: 1.48x faster |
| Geometric mean  | (ref)   | 1.57x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | clang-main             |
|----------------------------|:--------:|:----------------------:|
| mdp                        | 1.89 sec | 799 ms: 2.37x faster   |
| logging_silent             | 124 ns   | 56.3 ns: 2.21x faster  |
| richards_super             | 67.7 ms  | 31.5 ms: 2.15x faster  |
| richards                   | 59.0 ms  | 27.8 ms: 2.12x faster  |
| asyncio_websockets         | 330 ms   | 158 ms: 2.09x faster   |
| unpickle_pure_python       | 284 us   | 140 us: 2.03x faster   |
| deltablue                  | 4.22 ms  | 2.12 ms: 1.99x faster  |
| generators                 | 35.6 ms  | 17.9 ms: 1.98x faster  |
| scimark_lu                 | 119 ms   | 61.6 ms: 1.94x faster  |
| spectral_norm              | 102 ms   | 55.1 ms: 1.85x faster  |
| scimark_sor                | 139 ms   | 76.7 ms: 1.81x faster  |
| hexiom                     | 7.44 ms  | 4.12 ms: 1.81x faster  |
| mako                       | 12.1 ms  | 6.71 ms: 1.80x faster  |
| deepcopy_memo              | 34.0 us  | 19.1 us: 1.78x faster  |
| comprehensions             | 20.1 us  | 11.5 us: 1.75x faster  |
| float                      | 78.0 ms  | 44.7 ms: 1.75x faster  |
| scimark_monte_carlo        | 75.8 ms  | 43.5 ms: 1.74x faster  |
| go                         | 140 ms   | 80.8 ms: 1.74x faster  |
| raytrace                   | 313 ms   | 181 ms: 1.73x faster   |
| chaos                      | 69.3 ms  | 40.2 ms: 1.73x faster  |
| crypto_pyaes               | 80.1 ms  | 47.3 ms: 1.69x faster  |
| pickle_pure_python         | 364 us   | 216 us: 1.69x faster   |
| coroutines                 | 22.4 ms  | 13.4 ms: 1.67x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 851 us: 1.65x faster   |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.69 ms: 1.65x faster  |
| pyflate                    | 477 ms   | 291 ms: 1.64x faster   |
| xml_etree_process          | 66.9 ms  | 40.9 ms: 1.64x faster  |
| xml_etree_generate         | 92.6 ms  | 57.2 ms: 1.62x faster  |
| nbody                      | 103 ms   | 64.2 ms: 1.61x faster  |
| fannkuch                   | 418 ms   | 260 ms: 1.61x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 1.05 ms: 1.60x faster  |
| pprint_safe_repr           | 825 ms   | 521 ms: 1.58x faster   |
| regex_compile              | 130 ms   | 82.3 ms: 1.58x faster  |
| gc_traversal               | 3.25 ms  | 2.08 ms: 1.56x faster  |
| async_generators           | 348 ms   | 223 ms: 1.56x faster   |
| pprint_pformat             | 1.66 sec | 1.07 sec: 1.56x faster |
| deepcopy                   | 278 us   | 180 us: 1.54x faster   |
| json_loads                 | 23.3 us  | 15.1 us: 1.54x faster  |
| nqueens                    | 96.9 ms  | 63.5 ms: 1.53x faster  |
| deepcopy_reduce            | 2.86 us  | 1.88 us: 1.52x faster  |
| bpe_tokeniser              | 4.45 sec | 2.93 sec: 1.52x faster |
| genshi_text                | 23.9 ms  | 15.8 ms: 1.51x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 35.1 ms: 1.51x faster  |
| django_template            | 38.0 ms  | 25.4 ms: 1.50x faster  |
| scimark_fft                | 276 ms   | 185 ms: 1.49x faster   |
| sqlglot_v2_normalize       | 109 ms   | 73.4 ms: 1.49x faster  |
| genshi_xml                 | 50.4 ms  | 34.2 ms: 1.48x faster  |
| bench_thread_pool          | 1.28 ms  | 864 us: 1.48x faster   |
| xml_etree_iterparse        | 94.3 ms  | 64.1 ms: 1.47x faster  |
| tomli_loads                | 2.07 sec | 1.41 sec: 1.47x faster |
| logging_simple             | 9.30 us  | 6.39 us: 1.46x faster  |
| async_tree_memoization     | 313 ms   | 216 ms: 1.45x faster   |
| logging_format             | 9.92 us  | 6.88 us: 1.44x faster  |
| async_tree_none            | 267 ms   | 185 ms: 1.44x faster   |
| typing_runtime_protocols   | 154 us   | 107 us: 1.44x faster   |
| sympy_integrate            | 18.4 ms  | 12.9 ms: 1.43x faster  |
| sphinx                     | 933 ms   | 653 ms: 1.43x faster   |
| async_tree_memoization_tg  | 304 ms   | 215 ms: 1.42x faster   |
| async_tree_io_tg           | 576 ms   | 407 ms: 1.41x faster   |
| sympy_str                  | 247 ms   | 175 ms: 1.41x faster   |
| 2to3                       | 309 ms   | 220 ms: 1.40x faster   |
| docutils                   | 2.31 sec | 1.65 sec: 1.39x faster |
| pycparser                  | 1.01 sec | 728 ms: 1.39x faster   |
| sympy_expand               | 419 ms   | 301 ms: 1.39x faster   |
| json_dumps                 | 9.44 ms  | 6.78 ms: 1.39x faster  |
| async_tree_none_tg         | 243 ms   | 176 ms: 1.39x faster   |
| sympy_sum                  | 123 ms   | 89.6 ms: 1.38x faster  |
| async_tree_io              | 570 ms   | 416 ms: 1.37x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 337 ms: 1.35x faster   |
| subparsers                 | 21.5 ms  | 15.9 ms: 1.35x faster  |
| telco                      | 6.56 ms  | 4.87 ms: 1.35x faster  |
| html5lib                   | 52.5 ms  | 39.0 ms: 1.35x faster  |
| pylint                     | 269 ms   | 200 ms: 1.35x faster   |
| regex_effbot               | 1.87 ms  | 1.39 ms: 1.34x faster  |
| json                       | 4.07 ms  | 3.09 ms: 1.32x faster  |
| coverage                   | 63.7 ms  | 48.3 ms: 1.32x faster  |
| regex_v8                   | 17.5 ms  | 13.4 ms: 1.31x faster  |
| meteor_contest             | 99.5 ms  | 76.2 ms: 1.31x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 342 ms: 1.30x faster   |
| many_optionals             | 559 us   | 432 us: 1.29x faster   |
| xml_etree_parse            | 112 ms   | 87.6 ms: 1.28x faster  |
| k_core                     | 2.18 sec | 1.71 sec: 1.27x faster |
| dulwich_log                | 52.4 ms  | 42.1 ms: 1.24x faster  |
| sqlite_synth               | 1.96 us  | 1.58 us: 1.24x faster  |
| shortest_path              | 437 ms   | 366 ms: 1.19x faster   |
| connected_components       | 395 ms   | 336 ms: 1.18x faster   |
| pathlib                    | 37.5 ms  | 32.5 ms: 1.16x faster  |
| python_startup             | 29.5 ms  | 25.8 ms: 1.14x faster  |
| bench_mp_pool              | 101 ms   | 88.9 ms: 1.14x faster  |
| create_gc_cycles           | 1.42 ms  | 1.25 ms: 1.14x faster  |
| regex_dna                  | 123 ms   | 114 ms: 1.08x faster   |
| python_startup_no_site     | 22.0 ms  | 20.4 ms: 1.08x faster  |
| pidigits                   | 156 ms   | 149 ms: 1.04x faster   |
| Geometric mean             | (ref)    | 1.50x faster           |
Ignored benchmarks (1) of Ex.json: thrift
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.502x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.42x
- 95% likely to have a speedup of 1.41x
- 99% likely to have a speedup of 1.40x

# Memory
- memory change: unknown