# Results vs. base

- fork: unknown
- ref: clang
- machine: unknown-unknown
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.738x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.59x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | clang                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 207 ms: 1.49x faster   |
| docutils       | 2.31 sec | 1.56 sec: 1.48x faster |
| html5lib       | 52.5 ms  | 34.9 ms: 1.50x faster  |
| sphinx         | 933 ms   | 603 ms: 1.55x faster   |
| Geometric mean | (ref)    | 1.51x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | clang                 |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 10.7 ms: 2.09x faster |
| asyncio_websockets         | 330 ms  | 159 ms: 2.07x faster  |
| async_generators           | 348 ms  | 187 ms: 1.86x faster  |
| async_tree_none            | 267 ms  | 159 ms: 1.68x faster  |
| async_tree_memoization     | 313 ms  | 187 ms: 1.67x faster  |
| async_tree_io_tg           | 576 ms  | 351 ms: 1.64x faster  |
| async_tree_none_tg         | 243 ms  | 150 ms: 1.62x faster  |
| async_tree_io              | 570 ms  | 353 ms: 1.62x faster  |
| async_tree_memoization_tg  | 304 ms  | 197 ms: 1.55x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 313 ms: 1.45x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 316 ms: 1.40x faster  |
| Geometric mean             | (ref)   | 1.68x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | clang                 |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 36.9 ms: 2.11x faster |
| nbody          | 103 ms  | 49.1 ms: 2.11x faster |
| pidigits       | 156 ms  | 145 ms: 1.08x faster  |
| Geometric mean | (ref)   | 1.69x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | clang                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 69.8 ms: 1.86x faster |
| regex_v8       | 17.5 ms | 13.0 ms: 1.35x faster |
| regex_effbot   | 1.87 ms | 1.54 ms: 1.21x faster |
| regex_dna      | 123 ms  | 117 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.34x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | clang                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 107 us: 2.65x faster   |
| pickle_pure_python   | 364 us   | 173 us: 2.10x faster   |
| xml_etree_process    | 66.9 ms  | 34.0 ms: 1.97x faster  |
| tomli_loads          | 2.07 sec | 1.09 sec: 1.90x faster |
| xml_etree_generate   | 92.6 ms  | 49.1 ms: 1.88x faster  |
| json_dumps           | 9.44 ms  | 5.66 ms: 1.67x faster  |
| json_loads           | 23.3 us  | 14.1 us: 1.66x faster  |
| xml_etree_iterparse  | 94.3 ms  | 61.5 ms: 1.53x faster  |
| xml_etree_parse      | 112 ms   | 89.4 ms: 1.26x faster  |
| Geometric mean       | (ref)    | 1.81x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | clang                 |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.4 ms: 1.11x faster |
| python_startup_no_site | 22.0 ms | 20.9 ms: 1.05x faster |
| Geometric mean         | (ref)   | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | clang                 |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 5.83 ms: 2.07x faster |
| genshi_text     | 23.9 ms | 11.9 ms: 2.01x faster |
| django_template | 38.0 ms | 21.3 ms: 1.78x faster |
| genshi_xml      | 50.4 ms | 29.0 ms: 1.74x faster |
| Geometric mean  | (ref)   | 1.89x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | clang                  |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 41.1 ns: 3.02x faster  |
| scimark_sor                | 139 ms   | 49.3 ms: 2.81x faster  |
| mdp                        | 1.89 sec | 682 ms: 2.77x faster   |
| scimark_lu                 | 119 ms   | 43.5 ms: 2.75x faster  |
| unpickle_pure_python       | 284 us   | 107 us: 2.65x faster   |
| scimark_monte_carlo        | 75.8 ms  | 28.6 ms: 2.65x faster  |
| deltablue                  | 4.22 ms  | 1.64 ms: 2.57x faster  |
| hexiom                     | 7.44 ms  | 2.98 ms: 2.49x faster  |
| deepcopy_memo              | 34.0 us  | 14.0 us: 2.43x faster  |
| generators                 | 35.6 ms  | 14.8 ms: 2.41x faster  |
| spectral_norm              | 102 ms   | 42.8 ms: 2.37x faster  |
| comprehensions             | 20.1 us  | 8.64 us: 2.33x faster  |
| go                         | 140 ms   | 61.5 ms: 2.28x faster  |
| richards                   | 59.0 ms  | 26.3 ms: 2.25x faster  |
| richards_super             | 67.7 ms  | 30.2 ms: 2.24x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 1.99 ms: 2.23x faster  |
| chaos                      | 69.3 ms  | 31.4 ms: 2.21x faster  |
| raytrace                   | 313 ms   | 142 ms: 2.20x faster   |
| float                      | 78.0 ms  | 36.9 ms: 2.11x faster  |
| nbody                      | 103 ms   | 49.1 ms: 2.11x faster  |
| pickle_pure_python         | 364 us   | 173 us: 2.10x faster   |
| coroutines                 | 22.4 ms  | 10.7 ms: 2.09x faster  |
| asyncio_websockets         | 330 ms   | 159 ms: 2.07x faster   |
| mako                       | 12.1 ms  | 5.83 ms: 2.07x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 682 us: 2.06x faster   |
| pyflate                    | 477 ms   | 234 ms: 2.04x faster   |
| fannkuch                   | 418 ms   | 207 ms: 2.02x faster   |
| genshi_text                | 23.9 ms  | 11.9 ms: 2.01x faster  |
| crypto_pyaes               | 80.1 ms  | 39.9 ms: 2.00x faster  |
| pprint_safe_repr           | 825 ms   | 415 ms: 1.99x faster   |
| pprint_pformat             | 1.66 sec | 835 ms: 1.99x faster   |
| scimark_fft                | 276 ms   | 139 ms: 1.98x faster   |
| xml_etree_process          | 66.9 ms  | 34.0 ms: 1.97x faster  |
| nqueens                    | 96.9 ms  | 49.8 ms: 1.94x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 873 us: 1.93x faster   |
| deepcopy                   | 278 us   | 144 us: 1.93x faster   |
| tomli_loads                | 2.07 sec | 1.09 sec: 1.90x faster |
| deepcopy_reduce            | 2.86 us  | 1.52 us: 1.89x faster  |
| xml_etree_generate         | 92.6 ms  | 49.1 ms: 1.88x faster  |
| regex_compile              | 130 ms   | 69.8 ms: 1.86x faster  |
| async_generators           | 348 ms   | 187 ms: 1.86x faster   |
| django_template            | 38.0 ms  | 21.3 ms: 1.78x faster  |
| typing_runtime_protocols   | 154 us   | 87.6 us: 1.76x faster  |
| bpe_tokeniser              | 4.45 sec | 2.55 sec: 1.75x faster |
| genshi_xml                 | 50.4 ms  | 29.0 ms: 1.74x faster  |
| sqlglot_v2_normalize       | 109 ms   | 64.2 ms: 1.70x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 31.1 ms: 1.70x faster  |
| async_tree_none            | 267 ms   | 159 ms: 1.68x faster   |
| logging_simple             | 9.30 us  | 5.55 us: 1.68x faster  |
| async_tree_memoization     | 313 ms   | 187 ms: 1.67x faster   |
| json_dumps                 | 9.44 ms  | 5.66 ms: 1.67x faster  |
| logging_format             | 9.92 us  | 5.96 us: 1.67x faster  |
| sympy_str                  | 247 ms   | 149 ms: 1.66x faster   |
| json_loads                 | 23.3 us  | 14.1 us: 1.66x faster  |
| sympy_integrate            | 18.4 ms  | 11.2 ms: 1.64x faster  |
| async_tree_io_tg           | 576 ms   | 351 ms: 1.64x faster   |
| sympy_expand               | 419 ms   | 256 ms: 1.64x faster   |
| async_tree_none_tg         | 243 ms   | 150 ms: 1.62x faster   |
| async_tree_io              | 570 ms   | 353 ms: 1.62x faster   |
| coverage                   | 63.7 ms  | 39.8 ms: 1.60x faster  |
| pycparser                  | 1.01 sec | 647 ms: 1.57x faster   |
| sympy_sum                  | 123 ms   | 79.2 ms: 1.56x faster  |
| bench_thread_pool          | 1.28 ms  | 823 us: 1.55x faster   |
| sphinx                     | 933 ms   | 603 ms: 1.55x faster   |
| async_tree_memoization_tg  | 304 ms   | 197 ms: 1.55x faster   |
| telco                      | 6.56 ms  | 4.25 ms: 1.54x faster  |
| xml_etree_iterparse        | 94.3 ms  | 61.5 ms: 1.53x faster  |
| html5lib                   | 52.5 ms  | 34.9 ms: 1.50x faster  |
| 2to3                       | 309 ms   | 207 ms: 1.49x faster   |
| meteor_contest             | 99.5 ms  | 66.8 ms: 1.49x faster  |
| docutils                   | 2.31 sec | 1.56 sec: 1.48x faster |
| async_tree_cpu_io_mixed    | 455 ms   | 313 ms: 1.45x faster   |
| json                       | 4.07 ms  | 2.81 ms: 1.45x faster  |
| pylint                     | 269 ms   | 188 ms: 1.43x faster   |
| subparsers                 | 21.5 ms  | 15.3 ms: 1.41x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 316 ms: 1.40x faster   |
| dulwich_log                | 52.4 ms  | 38.0 ms: 1.38x faster  |
| many_optionals             | 559 us   | 409 us: 1.37x faster   |
| regex_v8                   | 17.5 ms  | 13.0 ms: 1.35x faster  |
| k_core                     | 2.18 sec | 1.66 sec: 1.32x faster |
| sqlite_synth               | 1.96 us  | 1.51 us: 1.29x faster  |
| xml_etree_parse            | 112 ms   | 89.4 ms: 1.26x faster  |
| shortest_path              | 437 ms   | 351 ms: 1.25x faster   |
| pathlib                    | 37.5 ms  | 30.7 ms: 1.22x faster  |
| regex_effbot               | 1.87 ms  | 1.54 ms: 1.21x faster  |
| connected_components       | 395 ms   | 329 ms: 1.20x faster   |
| gc_traversal               | 3.25 ms  | 2.76 ms: 1.18x faster  |
| bench_mp_pool              | 101 ms   | 88.6 ms: 1.14x faster  |
| python_startup             | 29.5 ms  | 26.4 ms: 1.11x faster  |
| pidigits                   | 156 ms   | 145 ms: 1.08x faster   |
| python_startup_no_site     | 22.0 ms  | 20.9 ms: 1.05x faster  |
| regex_dna                  | 123 ms   | 117 ms: 1.05x faster   |
| create_gc_cycles           | 1.42 ms  | 1.36 ms: 1.04x faster  |
| Geometric mean             | (ref)    | 1.74x faster           |
Ignored benchmarks (1) of Ex.json: thrift

- Geometric mean (including insignificant results): 1.738x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.63x
- 95% likely to have a speedup of 1.62x
- 99% likely to have a speedup of 1.59x

# Memory
- memory change: unknown