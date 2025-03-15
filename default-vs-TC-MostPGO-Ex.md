# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.327x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | default                |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 298 ms: 1.43x slower   |
| docutils       | 1.74 sec      | 2.17 sec: 1.25x slower |
| html5lib       | 37.2 ms       | 51.3 ms: 1.38x slower  |
| sphinx         | 666 ms        | 872 ms: 1.31x slower   |
| Geometric mean | (ref)         | 1.34x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | default               |
|----------------------------|:-------------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 331 ms        | 424 ms: 1.28x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 437 ms: 1.32x slower  |
| async_tree_memoization_tg  | 209 ms        | 291 ms: 1.39x slower  |
| async_tree_memoization     | 202 ms        | 297 ms: 1.47x slower  |
| async_tree_io              | 374 ms        | 553 ms: 1.48x slower  |
| async_tree_none_tg         | 160 ms        | 236 ms: 1.48x slower  |
| async_tree_io_tg           | 374 ms        | 559 ms: 1.50x slower  |
| async_tree_none            | 165 ms        | 249 ms: 1.51x slower  |
| async_generators           | 202 ms        | 328 ms: 1.63x slower  |
| coroutines                 | 11.8 ms       | 21.9 ms: 1.85x slower |
| Geometric mean             | (ref)         | 1.43x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | default               |
|----------------|:-------------:|:---------------------:|
| float          | 40.4 ms       | 75.4 ms: 1.87x slower |
| nbody          | 53.0 ms       | 101 ms: 1.90x slower  |
| Geometric mean | (ref)         | 1.53x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | default               |
|----------------|:-------------:|:---------------------:|
| regex_dna      | 125 ms        | 121 ms: 1.03x faster  |
| regex_v8       | 15.3 ms       | 17.1 ms: 1.12x slower |
| regex_effbot   | 1.53 ms       | 1.81 ms: 1.19x slower |
| regex_compile  | 79.3 ms       | 125 ms: 1.57x slower  |
| Geometric mean | (ref)         | 1.19x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | default                |
|----------------------|:-------------:|:----------------------:|
| xml_etree_parse      | 92.6 ms       | 108 ms: 1.17x slower   |
| json_dumps           | 6.84 ms       | 9.01 ms: 1.32x slower  |
| xml_etree_iterparse  | 64.2 ms       | 89.9 ms: 1.40x slower  |
| json_loads           | 15.8 us       | 22.3 us: 1.41x slower  |
| xml_etree_generate   | 54.3 ms       | 89.5 ms: 1.65x slower  |
| tomli_loads          | 1.18 sec      | 1.99 sec: 1.68x slower |
| xml_etree_process    | 37.9 ms       | 64.6 ms: 1.70x slower  |
| pickle_pure_python   | 195 us        | 355 us: 1.81x slower   |
| unpickle_pure_python | 123 us        | 274 us: 2.23x slower   |
| Geometric mean       | (ref)         | 1.57x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-MostPGO-Ex | default               |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 19.9 ms       | 20.4 ms: 1.03x slower |
| python_startup         | 26.4 ms       | 27.3 ms: 1.04x slower |
| Geometric mean         | (ref)         | 1.03x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | default               |
|-----------------|:-------------:|:---------------------:|
| genshi_xml      | 31.3 ms       | 48.8 ms: 1.56x slower |
| django_template | 22.9 ms       | 36.9 ms: 1.61x slower |
| genshi_text     | 14.1 ms       | 23.2 ms: 1.65x slower |
| mako            | 6.50 ms       | 11.7 ms: 1.80x slower |
| Geometric mean  | (ref)         | 1.65x slower          |

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | default                |
|----------------------------|:-------------:|:----------------------:|
| subparsers                 | 41.2 ms       | 20.8 ms: 1.98x faster  |
| many_optionals             | 669 us        | 547 us: 1.22x faster   |
| k_core                     | 2.00 sec      | 1.83 sec: 1.09x faster |
| connected_components       | 366 ms        | 347 ms: 1.06x faster   |
| shortest_path              | 399 ms        | 378 ms: 1.06x faster   |
| regex_dna                  | 125 ms        | 121 ms: 1.03x faster   |
| python_startup_no_site     | 19.9 ms       | 20.4 ms: 1.03x slower  |
| python_startup             | 26.4 ms       | 27.3 ms: 1.04x slower  |
| create_gc_cycles           | 1.35 ms       | 1.40 ms: 1.04x slower  |
| bench_mp_pool              | 88.6 ms       | 96.2 ms: 1.09x slower  |
| regex_v8                   | 15.3 ms       | 17.1 ms: 1.12x slower  |
| mdp                        | 1.56 sec      | 1.81 sec: 1.16x slower |
| xml_etree_parse            | 92.6 ms       | 108 ms: 1.17x slower   |
| sqlite_synth               | 1.56 us       | 1.84 us: 1.18x slower  |
| regex_effbot               | 1.53 ms       | 1.81 ms: 1.19x slower  |
| bench_thread_pool          | 819 us        | 1.01 ms: 1.23x slower  |
| dulwich_log                | 41.5 ms       | 51.0 ms: 1.23x slower  |
| docutils                   | 1.74 sec      | 2.17 sec: 1.25x slower |
| pylint                     | 202 ms        | 253 ms: 1.25x slower   |
| json                       | 3.16 ms       | 3.96 ms: 1.25x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 424 ms: 1.28x slower   |
| sphinx                     | 666 ms        | 872 ms: 1.31x slower   |
| async_tree_cpu_io_mixed    | 332 ms        | 437 ms: 1.32x slower   |
| json_dumps                 | 6.84 ms       | 9.01 ms: 1.32x slower  |
| meteor_contest             | 72.3 ms       | 95.9 ms: 1.33x slower  |
| coverage                   | 46.2 ms       | 61.9 ms: 1.34x slower  |
| pathlib                    | 25.5 ms       | 34.4 ms: 1.35x slower  |
| sympy_sum                  | 88.0 ms       | 119 ms: 1.36x slower   |
| html5lib                   | 37.2 ms       | 51.3 ms: 1.38x slower  |
| sympy_integrate            | 12.9 ms       | 17.8 ms: 1.38x slower  |
| async_tree_memoization_tg  | 209 ms        | 291 ms: 1.39x slower   |
| xml_etree_iterparse        | 64.2 ms       | 89.9 ms: 1.40x slower  |
| telco                      | 4.60 ms       | 6.44 ms: 1.40x slower  |
| json_loads                 | 15.8 us       | 22.3 us: 1.41x slower  |
| gc_traversal               | 2.21 ms       | 3.15 ms: 1.43x slower  |
| thrift                     | 487 us        | 694 us: 1.43x slower   |
| 2to3                       | 209 ms        | 298 ms: 1.43x slower   |
| pycparser                  | 688 ms        | 992 ms: 1.44x slower   |
| sympy_expand               | 279 ms        | 405 ms: 1.45x slower   |
| logging_format             | 6.39 us       | 9.33 us: 1.46x slower  |
| sympy_str                  | 163 ms        | 238 ms: 1.47x slower   |
| async_tree_memoization     | 202 ms        | 297 ms: 1.47x slower   |
| async_tree_io              | 374 ms        | 553 ms: 1.48x slower   |
| async_tree_none_tg         | 160 ms        | 236 ms: 1.48x slower   |
| async_tree_io_tg           | 374 ms        | 559 ms: 1.50x slower   |
| async_tree_none            | 165 ms        | 249 ms: 1.51x slower   |
| logging_simple             | 5.84 us       | 8.87 us: 1.52x slower  |
| typing_runtime_protocols   | 98.1 us       | 150 us: 1.53x slower   |
| sqlglot_v2_optimize        | 33.0 ms       | 51.0 ms: 1.55x slower  |
| genshi_xml                 | 31.3 ms       | 48.8 ms: 1.56x slower  |
| regex_compile              | 79.3 ms       | 125 ms: 1.57x slower   |
| sqlglot_v2_normalize       | 66.7 ms       | 106 ms: 1.59x slower   |
| django_template            | 22.9 ms       | 36.9 ms: 1.61x slower  |
| bpe_tokeniser              | 2.67 sec      | 4.30 sec: 1.61x slower |
| async_generators           | 202 ms        | 328 ms: 1.63x slower   |
| pprint_safe_repr           | 481 ms        | 788 ms: 1.64x slower   |
| deepcopy_reduce            | 1.69 us       | 2.77 us: 1.64x slower  |
| genshi_text                | 14.1 ms       | 23.2 ms: 1.65x slower  |
| xml_etree_generate         | 54.3 ms       | 89.5 ms: 1.65x slower  |
| pprint_pformat             | 963 ms        | 1.61 sec: 1.67x slower |
| tomli_loads                | 1.18 sec      | 1.99 sec: 1.68x slower |
| deepcopy                   | 159 us        | 269 us: 1.70x slower   |
| xml_etree_process          | 37.9 ms       | 64.6 ms: 1.70x slower  |
| sqlglot_v2_transpile       | 943 us        | 1.64 ms: 1.74x slower  |
| nqueens                    | 54.2 ms       | 94.3 ms: 1.74x slower  |
| fannkuch                   | 233 ms        | 407 ms: 1.75x slower   |
| pyflate                    | 264 ms        | 462 ms: 1.75x slower   |
| scimark_fft                | 151 ms        | 269 ms: 1.78x slower   |
| mako                       | 6.50 ms       | 11.7 ms: 1.80x slower  |
| pickle_pure_python         | 195 us        | 355 us: 1.81x slower   |
| sqlglot_v2_parse           | 742 us        | 1.36 ms: 1.83x slower  |
| coroutines                 | 11.8 ms       | 21.9 ms: 1.85x slower  |
| crypto_pyaes               | 41.7 ms       | 77.9 ms: 1.87x slower  |
| float                      | 40.4 ms       | 75.4 ms: 1.87x slower  |
| raytrace                   | 162 ms        | 304 ms: 1.88x slower   |
| nbody                      | 53.0 ms       | 101 ms: 1.90x slower   |
| chaos                      | 34.2 ms       | 65.2 ms: 1.91x slower  |
| scimark_sparse_mat_mult    | 2.25 ms       | 4.34 ms: 1.93x slower  |
| deepcopy_memo              | 17.0 us       | 32.9 us: 1.93x slower  |
| go                         | 68.6 ms       | 137 ms: 2.00x slower   |
| comprehensions             | 9.60 us       | 19.4 us: 2.02x slower  |
| hexiom                     | 3.58 ms       | 7.27 ms: 2.03x slower  |
| richards_super             | 32.0 ms       | 65.8 ms: 2.05x slower  |
| richards                   | 28.1 ms       | 57.8 ms: 2.05x slower  |
| generators                 | 16.3 ms       | 33.8 ms: 2.07x slower  |
| scimark_monte_carlo        | 35.5 ms       | 73.9 ms: 2.08x slower  |
| spectral_norm              | 46.7 ms       | 97.7 ms: 2.09x slower  |
| scimark_lu                 | 55.5 ms       | 116 ms: 2.09x slower   |
| scimark_sor                | 63.1 ms       | 135 ms: 2.14x slower   |
| deltablue                  | 1.87 ms       | 4.09 ms: 2.18x slower  |
| unpickle_pure_python       | 123 us        | 274 us: 2.23x slower   |
| logging_silent             | 53.0 ns       | 119 ns: 2.25x slower   |
| Geometric mean             | (ref)         | 1.49x slower           |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets

- Geometric mean (including insignificant results): 1.327x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.39x

# Memory
- memory change: unknown