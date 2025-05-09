# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.338x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | default                |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 298 ms: 1.38x slower   |
| docutils       | 1.63 sec   | 2.17 sec: 1.33x slower |
| html5lib       | 36.1 ms    | 51.3 ms: 1.42x slower  |
| sphinx         | 638 ms     | 872 ms: 1.37x slower   |
| Geometric mean | (ref)      | 1.38x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | default               |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 328 ms     | 424 ms: 1.30x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 437 ms: 1.33x slower  |
| async_tree_memoization_tg  | 209 ms     | 291 ms: 1.39x slower  |
| async_tree_memoization     | 205 ms     | 297 ms: 1.45x slower  |
| async_tree_none            | 170 ms     | 249 ms: 1.47x slower  |
| async_tree_io              | 375 ms     | 553 ms: 1.47x slower  |
| async_tree_none_tg         | 159 ms     | 236 ms: 1.48x slower  |
| async_tree_io_tg           | 371 ms     | 559 ms: 1.51x slower  |
| async_generators           | 206 ms     | 328 ms: 1.59x slower  |
| coroutines                 | 12.4 ms    | 21.9 ms: 1.76x slower |
| Geometric mean             | (ref)      | 1.42x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | default               |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 152 ms: 1.04x slower  |
| float          | 40.2 ms    | 75.4 ms: 1.88x slower |
| nbody          | 53.3 ms    | 101 ms: 1.89x slower  |
| Geometric mean | (ref)      | 1.55x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | default               |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 121 ms: 1.05x slower  |
| regex_v8       | 14.1 ms    | 17.1 ms: 1.21x slower |
| regex_effbot   | 1.40 ms    | 1.81 ms: 1.30x slower |
| regex_compile  | 74.8 ms    | 125 ms: 1.67x slower  |
| Geometric mean | (ref)      | 1.29x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | default                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.0 ms    | 108 ms: 1.21x slower   |
| json_dumps           | 6.48 ms    | 9.01 ms: 1.39x slower  |
| xml_etree_iterparse  | 60.4 ms    | 89.9 ms: 1.49x slower  |
| json_loads           | 14.5 us    | 22.3 us: 1.55x slower  |
| tomli_loads          | 1.17 sec   | 1.99 sec: 1.70x slower |
| xml_etree_generate   | 51.5 ms    | 89.5 ms: 1.74x slower  |
| xml_etree_process    | 36.7 ms    | 64.6 ms: 1.76x slower  |
| pickle_pure_python   | 201 us     | 355 us: 1.76x slower   |
| unpickle_pure_python | 123 us     | 274 us: 2.23x slower   |
| Geometric mean       | (ref)      | 1.63x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | default               |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 20.4 ms: 1.04x slower |
| python_startup         | 26.0 ms    | 27.3 ms: 1.05x slower |
| Geometric mean         | (ref)      | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | default               |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 36.9 ms: 1.58x slower |
| genshi_xml      | 30.7 ms    | 48.8 ms: 1.59x slower |
| genshi_text     | 14.2 ms    | 23.2 ms: 1.63x slower |
| mako            | 6.12 ms    | 11.7 ms: 1.91x slower |
| Geometric mean  | (ref)      | 1.67x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | default                |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 44.9 ms    | 20.8 ms: 2.16x faster  |
| many_optionals             | 761 us     | 547 us: 1.39x faster   |
| python_startup_no_site     | 19.6 ms    | 20.4 ms: 1.04x slower  |
| pidigits                   | 146 ms     | 152 ms: 1.04x slower   |
| regex_dna                  | 115 ms     | 121 ms: 1.05x slower   |
| python_startup             | 26.0 ms    | 27.3 ms: 1.05x slower  |
| k_core                     | 1.71 sec   | 1.83 sec: 1.07x slower |
| connected_components       | 321 ms     | 347 ms: 1.08x slower   |
| bench_mp_pool              | 89.1 ms    | 96.2 ms: 1.08x slower  |
| shortest_path              | 348 ms     | 378 ms: 1.09x slower   |
| create_gc_cycles           | 1.27 ms    | 1.40 ms: 1.11x slower  |
| bench_thread_pool          | 851 us     | 1.01 ms: 1.18x slower  |
| sqlite_synth               | 1.56 us    | 1.84 us: 1.18x slower  |
| regex_v8                   | 14.1 ms    | 17.1 ms: 1.21x slower  |
| xml_etree_parse            | 89.0 ms    | 108 ms: 1.21x slower   |
| coverage                   | 49.5 ms    | 61.9 ms: 1.25x slower  |
| pylint                     | 199 ms     | 253 ms: 1.27x slower   |
| dulwich_log                | 39.5 ms    | 51.0 ms: 1.29x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 424 ms: 1.30x slower   |
| mdp                        | 1.40 sec   | 1.81 sec: 1.30x slower |
| regex_effbot               | 1.40 ms    | 1.81 ms: 1.30x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 437 ms: 1.33x slower   |
| json                       | 2.98 ms    | 3.96 ms: 1.33x slower  |
| docutils                   | 1.63 sec   | 2.17 sec: 1.33x slower |
| sphinx                     | 638 ms     | 872 ms: 1.37x slower   |
| 2to3                       | 216 ms     | 298 ms: 1.38x slower   |
| meteor_contest             | 69.5 ms    | 95.9 ms: 1.38x slower  |
| json_dumps                 | 6.48 ms    | 9.01 ms: 1.39x slower  |
| async_tree_memoization_tg  | 209 ms     | 291 ms: 1.39x slower   |
| pathlib                    | 24.3 ms    | 34.4 ms: 1.41x slower  |
| telco                      | 4.54 ms    | 6.44 ms: 1.42x slower  |
| html5lib                   | 36.1 ms    | 51.3 ms: 1.42x slower  |
| thrift                     | 482 us     | 694 us: 1.44x slower   |
| async_tree_memoization     | 205 ms     | 297 ms: 1.45x slower   |
| sympy_sum                  | 82.1 ms    | 119 ms: 1.45x slower   |
| sympy_integrate            | 12.2 ms    | 17.8 ms: 1.46x slower  |
| async_tree_none            | 170 ms     | 249 ms: 1.47x slower   |
| logging_format             | 6.34 us    | 9.33 us: 1.47x slower  |
| async_tree_io              | 375 ms     | 553 ms: 1.47x slower   |
| async_tree_none_tg         | 159 ms     | 236 ms: 1.48x slower   |
| xml_etree_iterparse        | 60.4 ms    | 89.9 ms: 1.49x slower  |
| pycparser                  | 664 ms     | 992 ms: 1.49x slower   |
| sympy_expand               | 269 ms     | 405 ms: 1.50x slower   |
| async_tree_io_tg           | 371 ms     | 559 ms: 1.51x slower   |
| sympy_str                  | 158 ms     | 238 ms: 1.51x slower   |
| gc_traversal               | 2.07 ms    | 3.15 ms: 1.52x slower  |
| typing_runtime_protocols   | 98.9 us    | 150 us: 1.52x slower   |
| logging_simple             | 5.78 us    | 8.87 us: 1.53x slower  |
| json_loads                 | 14.5 us    | 22.3 us: 1.55x slower  |
| django_template            | 23.4 ms    | 36.9 ms: 1.58x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 51.0 ms: 1.58x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 106 ms: 1.59x slower   |
| bpe_tokeniser              | 2.71 sec   | 4.30 sec: 1.59x slower |
| genshi_xml                 | 30.7 ms    | 48.8 ms: 1.59x slower  |
| async_generators           | 206 ms     | 328 ms: 1.59x slower   |
| genshi_text                | 14.2 ms    | 23.2 ms: 1.63x slower  |
| pprint_safe_repr           | 478 ms     | 788 ms: 1.65x slower   |
| pprint_pformat             | 968 ms     | 1.61 sec: 1.66x slower |
| regex_compile              | 74.8 ms    | 125 ms: 1.67x slower   |
| deepcopy_reduce            | 1.66 us    | 2.77 us: 1.67x slower  |
| deepcopy                   | 160 us     | 269 us: 1.69x slower   |
| tomli_loads                | 1.17 sec   | 1.99 sec: 1.70x slower |
| fannkuch                   | 236 ms     | 407 ms: 1.73x slower   |
| xml_etree_generate         | 51.5 ms    | 89.5 ms: 1.74x slower  |
| nqueens                    | 54.0 ms    | 94.3 ms: 1.75x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.64 ms: 1.76x slower  |
| xml_etree_process          | 36.7 ms    | 64.6 ms: 1.76x slower  |
| pickle_pure_python         | 201 us     | 355 us: 1.76x slower   |
| coroutines                 | 12.4 ms    | 21.9 ms: 1.76x slower  |
| scimark_fft                | 152 ms     | 269 ms: 1.77x slower   |
| pyflate                    | 260 ms     | 462 ms: 1.78x slower   |
| chaos                      | 35.9 ms    | 65.2 ms: 1.82x slower  |
| raytrace                   | 166 ms     | 304 ms: 1.83x slower   |
| sqlglot_v2_parse           | 740 us     | 1.36 ms: 1.84x slower  |
| crypto_pyaes               | 41.6 ms    | 77.9 ms: 1.87x slower  |
| float                      | 40.2 ms    | 75.4 ms: 1.88x slower  |
| nbody                      | 53.3 ms    | 101 ms: 1.89x slower   |
| mako                       | 6.12 ms    | 11.7 ms: 1.91x slower  |
| spectral_norm              | 51.1 ms    | 97.7 ms: 1.91x slower  |
| scimark_sparse_mat_mult    | 2.26 ms    | 4.34 ms: 1.92x slower  |
| deepcopy_memo              | 17.0 us    | 32.9 us: 1.93x slower  |
| comprehensions             | 9.73 us    | 19.4 us: 1.99x slower  |
| scimark_monte_carlo        | 37.0 ms    | 73.9 ms: 2.00x slower  |
| scimark_sor                | 67.5 ms    | 135 ms: 2.00x slower   |
| go                         | 68.4 ms    | 137 ms: 2.00x slower   |
| richards_super             | 32.2 ms    | 65.8 ms: 2.05x slower  |
| richards                   | 27.8 ms    | 57.8 ms: 2.08x slower  |
| hexiom                     | 3.47 ms    | 7.27 ms: 2.09x slower  |
| scimark_lu                 | 54.4 ms    | 116 ms: 2.14x slower   |
| deltablue                  | 1.85 ms    | 4.09 ms: 2.21x slower  |
| unpickle_pure_python       | 123 us     | 274 us: 2.23x slower   |
| logging_silent             | 53.3 ns    | 119 ns: 2.24x slower   |
| generators                 | 14.8 ms    | 33.8 ms: 2.28x slower  |
| Geometric mean             | (ref)      | 1.51x slower           |

Benchmark hidden because not significant (1): asyncio_websockets

- Geometric mean (including insignificant results): 1.338x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: unknown