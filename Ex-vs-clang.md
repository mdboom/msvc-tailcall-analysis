# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.424x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.59x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang    | Ex                     |
|----------------|:--------:|:----------------------:|
| 2to3           | 207 ms   | 309 ms: 1.49x slower   |
| docutils       | 1.56 sec | 2.31 sec: 1.48x slower |
| html5lib       | 34.9 ms  | 52.5 ms: 1.50x slower  |
| sphinx         | 603 ms   | 933 ms: 1.55x slower   |
| Geometric mean | (ref)    | 1.51x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang   | Ex                    |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 316 ms  | 444 ms: 1.40x slower  |
| async_tree_cpu_io_mixed    | 313 ms  | 455 ms: 1.45x slower  |
| async_tree_memoization_tg  | 197 ms  | 304 ms: 1.55x slower  |
| async_tree_io              | 353 ms  | 570 ms: 1.62x slower  |
| async_tree_none_tg         | 150 ms  | 243 ms: 1.62x slower  |
| async_tree_io_tg           | 351 ms  | 576 ms: 1.64x slower  |
| async_tree_memoization     | 187 ms  | 313 ms: 1.67x slower  |
| async_tree_none            | 159 ms  | 267 ms: 1.68x slower  |
| async_generators           | 187 ms  | 348 ms: 1.86x slower  |
| asyncio_websockets         | 159 ms  | 330 ms: 2.07x slower  |
| coroutines                 | 10.7 ms | 22.4 ms: 2.09x slower |
| Geometric mean             | (ref)   | 1.68x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang   | Ex                    |
|----------------|:-------:|:---------------------:|
| pidigits       | 145 ms  | 156 ms: 1.08x slower  |
| nbody          | 49.1 ms | 103 ms: 2.11x slower  |
| float          | 36.9 ms | 78.0 ms: 2.11x slower |
| Geometric mean | (ref)   | 1.69x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang   | Ex                    |
|----------------|:-------:|:---------------------:|
| regex_dna      | 117 ms  | 123 ms: 1.05x slower  |
| regex_effbot   | 1.54 ms | 1.87 ms: 1.21x slower |
| regex_v8       | 13.0 ms | 17.5 ms: 1.35x slower |
| regex_compile  | 69.8 ms | 130 ms: 1.86x slower  |
| Geometric mean | (ref)   | 1.34x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang    | Ex                     |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 89.4 ms  | 112 ms: 1.26x slower   |
| xml_etree_iterparse  | 61.5 ms  | 94.3 ms: 1.53x slower  |
| json_loads           | 14.1 us  | 23.3 us: 1.66x slower  |
| json_dumps           | 5.66 ms  | 9.44 ms: 1.67x slower  |
| xml_etree_generate   | 49.1 ms  | 92.6 ms: 1.88x slower  |
| tomli_loads          | 1.09 sec | 2.07 sec: 1.90x slower |
| xml_etree_process    | 34.0 ms  | 66.9 ms: 1.97x slower  |
| pickle_pure_python   | 173 us   | 364 us: 2.10x slower   |
| unpickle_pure_python | 107 us   | 284 us: 2.65x slower   |
| Geometric mean       | (ref)    | 1.81x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang   | Ex                    |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.9 ms | 22.0 ms: 1.05x slower |
| python_startup         | 26.4 ms | 29.5 ms: 1.11x slower |
| Geometric mean         | (ref)   | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang   | Ex                    |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 29.0 ms | 50.4 ms: 1.74x slower |
| django_template | 21.3 ms | 38.0 ms: 1.78x slower |
| genshi_text     | 11.9 ms | 23.9 ms: 2.01x slower |
| mako            | 5.83 ms | 12.1 ms: 2.07x slower |
| Geometric mean  | (ref)   | 1.89x slower          |

All benchmarks:
===============

| Benchmark                  | clang    | Ex                     |
|----------------------------|:--------:|:----------------------:|
| create_gc_cycles           | 1.36 ms  | 1.42 ms: 1.04x slower  |
| regex_dna                  | 117 ms   | 123 ms: 1.05x slower   |
| python_startup_no_site     | 20.9 ms  | 22.0 ms: 1.05x slower  |
| pidigits                   | 145 ms   | 156 ms: 1.08x slower   |
| python_startup             | 26.4 ms  | 29.5 ms: 1.11x slower  |
| bench_mp_pool              | 88.6 ms  | 101 ms: 1.14x slower   |
| gc_traversal               | 2.76 ms  | 3.25 ms: 1.18x slower  |
| connected_components       | 329 ms   | 395 ms: 1.20x slower   |
| regex_effbot               | 1.54 ms  | 1.87 ms: 1.21x slower  |
| pathlib                    | 30.7 ms  | 37.5 ms: 1.22x slower  |
| shortest_path              | 351 ms   | 437 ms: 1.25x slower   |
| xml_etree_parse            | 89.4 ms  | 112 ms: 1.26x slower   |
| sqlite_synth               | 1.51 us  | 1.96 us: 1.29x slower  |
| k_core                     | 1.66 sec | 2.18 sec: 1.32x slower |
| regex_v8                   | 13.0 ms  | 17.5 ms: 1.35x slower  |
| many_optionals             | 409 us   | 559 us: 1.37x slower   |
| dulwich_log                | 38.0 ms  | 52.4 ms: 1.38x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms   | 444 ms: 1.40x slower   |
| subparsers                 | 15.3 ms  | 21.5 ms: 1.41x slower  |
| pylint                     | 188 ms   | 269 ms: 1.43x slower   |
| json                       | 2.81 ms  | 4.07 ms: 1.45x slower  |
| async_tree_cpu_io_mixed    | 313 ms   | 455 ms: 1.45x slower   |
| docutils                   | 1.56 sec | 2.31 sec: 1.48x slower |
| meteor_contest             | 66.8 ms  | 99.5 ms: 1.49x slower  |
| 2to3                       | 207 ms   | 309 ms: 1.49x slower   |
| html5lib                   | 34.9 ms  | 52.5 ms: 1.50x slower  |
| xml_etree_iterparse        | 61.5 ms  | 94.3 ms: 1.53x slower  |
| telco                      | 4.25 ms  | 6.56 ms: 1.54x slower  |
| async_tree_memoization_tg  | 197 ms   | 304 ms: 1.55x slower   |
| sphinx                     | 603 ms   | 933 ms: 1.55x slower   |
| bench_thread_pool          | 823 us   | 1.28 ms: 1.55x slower  |
| sympy_sum                  | 79.2 ms  | 123 ms: 1.56x slower   |
| pycparser                  | 647 ms   | 1.01 sec: 1.57x slower |
| coverage                   | 39.8 ms  | 63.7 ms: 1.60x slower  |
| async_tree_io              | 353 ms   | 570 ms: 1.62x slower   |
| async_tree_none_tg         | 150 ms   | 243 ms: 1.62x slower   |
| sympy_expand               | 256 ms   | 419 ms: 1.64x slower   |
| async_tree_io_tg           | 351 ms   | 576 ms: 1.64x slower   |
| sympy_integrate            | 11.2 ms  | 18.4 ms: 1.64x slower  |
| json_loads                 | 14.1 us  | 23.3 us: 1.66x slower  |
| sympy_str                  | 149 ms   | 247 ms: 1.66x slower   |
| logging_format             | 5.96 us  | 9.92 us: 1.67x slower  |
| json_dumps                 | 5.66 ms  | 9.44 ms: 1.67x slower  |
| async_tree_memoization     | 187 ms   | 313 ms: 1.67x slower   |
| logging_simple             | 5.55 us  | 9.30 us: 1.68x slower  |
| async_tree_none            | 159 ms   | 267 ms: 1.68x slower   |
| sqlglot_v2_optimize        | 31.1 ms  | 52.8 ms: 1.70x slower  |
| sqlglot_v2_normalize       | 64.2 ms  | 109 ms: 1.70x slower   |
| genshi_xml                 | 29.0 ms  | 50.4 ms: 1.74x slower  |
| bpe_tokeniser              | 2.55 sec | 4.45 sec: 1.75x slower |
| typing_runtime_protocols   | 87.6 us  | 154 us: 1.76x slower   |
| django_template            | 21.3 ms  | 38.0 ms: 1.78x slower  |
| async_generators           | 187 ms   | 348 ms: 1.86x slower   |
| regex_compile              | 69.8 ms  | 130 ms: 1.86x slower   |
| xml_etree_generate         | 49.1 ms  | 92.6 ms: 1.88x slower  |
| deepcopy_reduce            | 1.52 us  | 2.86 us: 1.89x slower  |
| tomli_loads                | 1.09 sec | 2.07 sec: 1.90x slower |
| deepcopy                   | 144 us   | 278 us: 1.93x slower   |
| sqlglot_v2_transpile       | 873 us   | 1.69 ms: 1.93x slower  |
| nqueens                    | 49.8 ms  | 96.9 ms: 1.94x slower  |
| xml_etree_process          | 34.0 ms  | 66.9 ms: 1.97x slower  |
| scimark_fft                | 139 ms   | 276 ms: 1.98x slower   |
| pprint_pformat             | 835 ms   | 1.66 sec: 1.99x slower |
| pprint_safe_repr           | 415 ms   | 825 ms: 1.99x slower   |
| crypto_pyaes               | 39.9 ms  | 80.1 ms: 2.00x slower  |
| genshi_text                | 11.9 ms  | 23.9 ms: 2.01x slower  |
| fannkuch                   | 207 ms   | 418 ms: 2.02x slower   |
| pyflate                    | 234 ms   | 477 ms: 2.04x slower   |
| sqlglot_v2_parse           | 682 us   | 1.41 ms: 2.06x slower  |
| mako                       | 5.83 ms  | 12.1 ms: 2.07x slower  |
| asyncio_websockets         | 159 ms   | 330 ms: 2.07x slower   |
| coroutines                 | 10.7 ms  | 22.4 ms: 2.09x slower  |
| pickle_pure_python         | 173 us   | 364 us: 2.10x slower   |
| nbody                      | 49.1 ms  | 103 ms: 2.11x slower   |
| float                      | 36.9 ms  | 78.0 ms: 2.11x slower  |
| raytrace                   | 142 ms   | 313 ms: 2.20x slower   |
| chaos                      | 31.4 ms  | 69.3 ms: 2.21x slower  |
| scimark_sparse_mat_mult    | 1.99 ms  | 4.43 ms: 2.23x slower  |
| richards_super             | 30.2 ms  | 67.7 ms: 2.24x slower  |
| richards                   | 26.3 ms  | 59.0 ms: 2.25x slower  |
| go                         | 61.5 ms  | 140 ms: 2.28x slower   |
| comprehensions             | 8.64 us  | 20.1 us: 2.33x slower  |
| spectral_norm              | 42.8 ms  | 102 ms: 2.37x slower   |
| generators                 | 14.8 ms  | 35.6 ms: 2.41x slower  |
| deepcopy_memo              | 14.0 us  | 34.0 us: 2.43x slower  |
| hexiom                     | 2.98 ms  | 7.44 ms: 2.49x slower  |
| deltablue                  | 1.64 ms  | 4.22 ms: 2.57x slower  |
| scimark_monte_carlo        | 28.6 ms  | 75.8 ms: 2.65x slower  |
| unpickle_pure_python       | 107 us   | 284 us: 2.65x slower   |
| scimark_lu                 | 43.5 ms  | 119 ms: 2.75x slower   |
| mdp                        | 682 ms   | 1.89 sec: 2.77x slower |
| scimark_sor                | 49.3 ms  | 139 ms: 2.81x slower   |
| logging_silent             | 41.1 ns  | 124 ns: 3.02x slower   |
| Geometric mean             | (ref)    | 1.74x slower           |
Ignored benchmarks (1) of Ex.json: thrift

- Geometric mean (including insignificant results): 1.424x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.63x
- 95% likely to have a slowdown of 1.62x
- 99% likely to have a slowdown of 1.59x

# Memory
- memory change: unknown