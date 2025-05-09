# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.241x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | default                |
|----------------|:--------:|:----------------------:|
| 2to3           | 237 ms   | 298 ms: 1.26x slower   |
| docutils       | 1.81 sec | 2.17 sec: 1.20x slower |
| html5lib       | 40.8 ms  | 51.3 ms: 1.26x slower  |
| sphinx         | 723 ms   | 872 ms: 1.20x slower   |
| Geometric mean | (ref)    | 1.23x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | default               |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 304 ms  | 317 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 367 ms  | 424 ms: 1.16x slower  |
| async_tree_cpu_io_mixed    | 362 ms  | 437 ms: 1.20x slower  |
| async_tree_io              | 429 ms  | 553 ms: 1.29x slower  |
| async_tree_memoization     | 227 ms  | 297 ms: 1.31x slower  |
| async_tree_none            | 188 ms  | 249 ms: 1.33x slower  |
| async_tree_none_tg         | 178 ms  | 236 ms: 1.33x slower  |
| async_tree_io_tg           | 419 ms  | 559 ms: 1.33x slower  |
| async_tree_memoization_tg  | 218 ms  | 291 ms: 1.33x slower  |
| async_generators           | 224 ms  | 328 ms: 1.47x slower  |
| coroutines                 | 13.5 ms | 21.9 ms: 1.63x slower |
| Geometric mean             | (ref)   | 1.30x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | default               |
|----------------|:-------:|:---------------------:|
| pidigits       | 147 ms  | 152 ms: 1.04x slower  |
| float          | 44.8 ms | 75.4 ms: 1.68x slower |
| nbody          | 58.8 ms | 101 ms: 1.71x slower  |
| Geometric mean | (ref)   | 1.44x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | default               |
|----------------|:-------:|:---------------------:|
| regex_v8       | 16.7 ms | 17.1 ms: 1.03x slower |
| regex_dna      | 117 ms  | 121 ms: 1.03x slower  |
| regex_effbot   | 1.76 ms | 1.81 ms: 1.03x slower |
| regex_compile  | 88.0 ms | 125 ms: 1.42x slower  |
| Geometric mean | (ref)   | 1.11x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | default                |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 104 ms   | 108 ms: 1.04x slower   |
| json_loads           | 21.1 us  | 22.3 us: 1.06x slower  |
| json_dumps           | 7.94 ms  | 9.01 ms: 1.13x slower  |
| xml_etree_iterparse  | 71.5 ms  | 89.9 ms: 1.26x slower  |
| xml_etree_generate   | 66.8 ms  | 89.5 ms: 1.34x slower  |
| xml_etree_process    | 46.5 ms  | 64.6 ms: 1.39x slower  |
| tomli_loads          | 1.38 sec | 1.99 sec: 1.44x slower |
| pickle_pure_python   | 236 us   | 355 us: 1.51x slower   |
| unpickle_pure_python | 154 us   | 274 us: 1.78x slower   |
| Geometric mean       | (ref)    | 1.31x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | default               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.1 ms | 20.4 ms: 1.01x slower |
| python_startup         | 26.9 ms | 27.3 ms: 1.02x slower |
| Geometric mean         | (ref)   | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | default               |
|-----------------|:-------:|:---------------------:|
| django_template | 27.5 ms | 36.9 ms: 1.34x slower |
| genshi_xml      | 35.3 ms | 48.8 ms: 1.38x slower |
| genshi_text     | 16.2 ms | 23.2 ms: 1.43x slower |
| mako            | 7.44 ms | 11.7 ms: 1.57x slower |
| Geometric mean  | (ref)   | 1.43x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | default                |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 47.1 ms  | 20.8 ms: 2.27x faster  |
| many_optionals             | 813 us   | 547 us: 1.49x faster   |
| bench_mp_pool              | 95.0 ms  | 96.2 ms: 1.01x slower  |
| python_startup_no_site     | 20.1 ms  | 20.4 ms: 1.01x slower  |
| create_gc_cycles           | 1.38 ms  | 1.40 ms: 1.01x slower  |
| python_startup             | 26.9 ms  | 27.3 ms: 1.02x slower  |
| regex_v8                   | 16.7 ms  | 17.1 ms: 1.03x slower  |
| regex_dna                  | 117 ms   | 121 ms: 1.03x slower   |
| regex_effbot               | 1.76 ms  | 1.81 ms: 1.03x slower  |
| pidigits                   | 147 ms   | 152 ms: 1.04x slower   |
| k_core                     | 1.76 sec | 1.83 sec: 1.04x slower |
| xml_etree_parse            | 104 ms   | 108 ms: 1.04x slower   |
| asyncio_websockets         | 304 ms   | 317 ms: 1.04x slower   |
| json                       | 3.77 ms  | 3.96 ms: 1.05x slower  |
| shortest_path              | 357 ms   | 378 ms: 1.06x slower   |
| json_loads                 | 21.1 us  | 22.3 us: 1.06x slower  |
| connected_components       | 326 ms   | 347 ms: 1.06x slower   |
| sqlite_synth               | 1.68 us  | 1.84 us: 1.10x slower  |
| coverage                   | 56.4 ms  | 61.9 ms: 1.10x slower  |
| bench_thread_pool          | 906 us   | 1.01 ms: 1.11x slower  |
| json_dumps                 | 7.94 ms  | 9.01 ms: 1.13x slower  |
| gc_traversal               | 2.77 ms  | 3.15 ms: 1.14x slower  |
| mdp                        | 1.57 sec | 1.81 sec: 1.16x slower |
| async_tree_cpu_io_mixed_tg | 367 ms   | 424 ms: 1.16x slower   |
| pylint                     | 217 ms   | 253 ms: 1.16x slower   |
| dulwich_log                | 43.0 ms  | 51.0 ms: 1.19x slower  |
| docutils                   | 1.81 sec | 2.17 sec: 1.20x slower |
| async_tree_cpu_io_mixed    | 362 ms   | 437 ms: 1.20x slower   |
| sphinx                     | 723 ms   | 872 ms: 1.20x slower   |
| telco                      | 5.33 ms  | 6.44 ms: 1.21x slower  |
| meteor_contest             | 78.1 ms  | 95.9 ms: 1.23x slower  |
| thrift                     | 561 us   | 694 us: 1.24x slower   |
| sympy_sum                  | 96.6 ms  | 119 ms: 1.24x slower   |
| sympy_expand               | 324 ms   | 405 ms: 1.25x slower   |
| html5lib                   | 40.8 ms  | 51.3 ms: 1.26x slower  |
| 2to3                       | 237 ms   | 298 ms: 1.26x slower   |
| xml_etree_iterparse        | 71.5 ms  | 89.9 ms: 1.26x slower  |
| sympy_str                  | 187 ms   | 238 ms: 1.28x slower   |
| sympy_integrate            | 13.9 ms  | 17.8 ms: 1.28x slower  |
| async_tree_io              | 429 ms   | 553 ms: 1.29x slower   |
| pycparser                  | 765 ms   | 992 ms: 1.30x slower   |
| logging_format             | 7.18 us  | 9.33 us: 1.30x slower  |
| deepcopy_reduce            | 2.12 us  | 2.77 us: 1.30x slower  |
| async_tree_memoization     | 227 ms   | 297 ms: 1.31x slower   |
| async_tree_none            | 188 ms   | 249 ms: 1.33x slower   |
| logging_simple             | 6.67 us  | 8.87 us: 1.33x slower  |
| sqlglot_v2_optimize        | 38.4 ms  | 51.0 ms: 1.33x slower  |
| async_tree_none_tg         | 178 ms   | 236 ms: 1.33x slower   |
| async_tree_io_tg           | 419 ms   | 559 ms: 1.33x slower   |
| typing_runtime_protocols   | 113 us   | 150 us: 1.33x slower   |
| async_tree_memoization_tg  | 218 ms   | 291 ms: 1.33x slower   |
| xml_etree_generate         | 66.8 ms  | 89.5 ms: 1.34x slower  |
| django_template            | 27.5 ms  | 36.9 ms: 1.34x slower  |
| pathlib                    | 25.6 ms  | 34.4 ms: 1.34x slower  |
| sqlglot_v2_normalize       | 79.0 ms  | 106 ms: 1.34x slower   |
| deepcopy                   | 199 us   | 269 us: 1.35x slower   |
| bpe_tokeniser              | 3.17 sec | 4.30 sec: 1.36x slower |
| genshi_xml                 | 35.3 ms  | 48.8 ms: 1.38x slower  |
| xml_etree_process          | 46.5 ms  | 64.6 ms: 1.39x slower  |
| pprint_safe_repr           | 558 ms   | 788 ms: 1.41x slower   |
| regex_compile              | 88.0 ms  | 125 ms: 1.42x slower   |
| pprint_pformat             | 1.13 sec | 1.61 sec: 1.43x slower |
| genshi_text                | 16.2 ms  | 23.2 ms: 1.43x slower  |
| nqueens                    | 65.7 ms  | 94.3 ms: 1.44x slower  |
| tomli_loads                | 1.38 sec | 1.99 sec: 1.44x slower |
| async_generators           | 224 ms   | 328 ms: 1.47x slower   |
| sqlglot_v2_transpile       | 1.09 ms  | 1.64 ms: 1.50x slower  |
| pickle_pure_python         | 236 us   | 355 us: 1.51x slower   |
| scimark_fft                | 178 ms   | 269 ms: 1.51x slower   |
| fannkuch                   | 265 ms   | 407 ms: 1.54x slower   |
| deepcopy_memo              | 21.3 us  | 32.9 us: 1.54x slower  |
| sqlglot_v2_parse           | 876 us   | 1.36 ms: 1.55x slower  |
| pyflate                    | 295 ms   | 462 ms: 1.57x slower   |
| mako                       | 7.44 ms  | 11.7 ms: 1.57x slower  |
| chaos                      | 41.4 ms  | 65.2 ms: 1.57x slower  |
| crypto_pyaes               | 49.3 ms  | 77.9 ms: 1.58x slower  |
| comprehensions             | 12.2 us  | 19.4 us: 1.58x slower  |
| raytrace                   | 187 ms   | 304 ms: 1.63x slower   |
| coroutines                 | 13.5 ms  | 21.9 ms: 1.63x slower  |
| richards_super             | 40.4 ms  | 65.8 ms: 1.63x slower  |
| richards                   | 35.0 ms  | 57.8 ms: 1.65x slower  |
| spectral_norm              | 58.4 ms  | 97.7 ms: 1.67x slower  |
| float                      | 44.8 ms  | 75.4 ms: 1.68x slower  |
| nbody                      | 58.8 ms  | 101 ms: 1.71x slower   |
| scimark_monte_carlo        | 42.9 ms  | 73.9 ms: 1.72x slower  |
| hexiom                     | 4.17 ms  | 7.27 ms: 1.74x slower  |
| scimark_sparse_mat_mult    | 2.48 ms  | 4.34 ms: 1.75x slower  |
| go                         | 78.0 ms  | 137 ms: 1.76x slower   |
| unpickle_pure_python       | 154 us   | 274 us: 1.78x slower   |
| scimark_lu                 | 65.2 ms  | 116 ms: 1.78x slower   |
| scimark_sor                | 73.9 ms  | 135 ms: 1.83x slower   |
| generators                 | 18.1 ms  | 33.8 ms: 1.87x slower  |
| logging_silent             | 62.9 ns  | 119 ns: 1.90x slower   |
| deltablue                  | 2.09 ms  | 4.09 ms: 1.96x slower  |
| Geometric mean             | (ref)    | 1.32x slower           |

- Geometric mean (including insignificant results): 1.241x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.27x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: unknown