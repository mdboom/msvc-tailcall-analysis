# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.634x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.50x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 204 ms: 1.46x faster   |
| docutils       | 2.17 sec | 1.55 sec: 1.40x faster |
| html5lib       | 51.3 ms  | 35.2 ms: 1.46x faster  |
| sphinx         | 872 ms   | 599 ms: 1.45x faster   |
| Geometric mean | (ref)    | 1.44x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 11.1 ms: 1.97x faster |
| async_generators           | 328 ms  | 188 ms: 1.74x faster  |
| async_tree_none            | 249 ms  | 155 ms: 1.61x faster  |
| async_tree_none_tg         | 236 ms  | 147 ms: 1.60x faster  |
| async_tree_io_tg           | 559 ms  | 352 ms: 1.59x faster  |
| async_tree_io              | 553 ms  | 349 ms: 1.58x faster  |
| async_tree_memoization     | 297 ms  | 190 ms: 1.57x faster  |
| async_tree_memoization_tg  | 291 ms  | 195 ms: 1.49x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 309 ms: 1.41x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 310 ms: 1.37x faster  |
| asyncio_websockets         | 317 ms  | 400 ms: 1.26x slower  |
| Geometric mean             | (ref)   | 1.49x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | clang-PGO             |
|----------------|:-------:|:---------------------:|
| float          | 75.4 ms | 38.5 ms: 1.96x faster |
| nbody          | 101 ms  | 52.9 ms: 1.90x faster |
| pidigits       | 152 ms  | 148 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.56x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 73.4 ms: 1.70x faster |
| regex_v8       | 17.1 ms | 13.5 ms: 1.27x faster |
| regex_effbot   | 1.81 ms | 1.65 ms: 1.10x faster |
| Geometric mean | (ref)   | 1.24x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 109 us: 2.52x faster   |
| pickle_pure_python   | 355 us   | 175 us: 2.02x faster   |
| xml_etree_process    | 64.6 ms  | 34.0 ms: 1.90x faster  |
| xml_etree_generate   | 89.5 ms  | 48.4 ms: 1.85x faster  |
| tomli_loads          | 1.99 sec | 1.13 sec: 1.76x faster |
| json_loads           | 22.3 us  | 14.2 us: 1.57x faster  |
| json_dumps           | 9.01 ms  | 5.76 ms: 1.56x faster  |
| xml_etree_iterparse  | 89.9 ms  | 60.7 ms: 1.48x faster  |
| xml_etree_parse      | 108 ms   | 88.8 ms: 1.22x faster  |
| Geometric mean       | (ref)    | 1.73x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | clang-PGO             |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 26.6 ms: 1.03x faster |
| python_startup_no_site | 20.4 ms | 20.0 ms: 1.02x faster |
| Geometric mean         | (ref)   | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 5.72 ms: 2.05x faster |
| genshi_text     | 23.2 ms | 12.0 ms: 1.94x faster |
| django_template | 36.9 ms | 19.5 ms: 1.89x faster |
| genshi_xml      | 48.8 ms | 27.4 ms: 1.78x faster |
| Geometric mean  | (ref)   | 1.91x faster          |

All benchmarks:
===============

| Benchmark                  | default  | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 44.5 ns: 2.69x faster  |
| richards_super             | 65.8 ms  | 24.6 ms: 2.67x faster  |
| richards                   | 57.8 ms  | 21.9 ms: 2.64x faster  |
| deltablue                  | 4.09 ms  | 1.59 ms: 2.57x faster  |
| unpickle_pure_python       | 274 us   | 109 us: 2.52x faster   |
| scimark_lu                 | 116 ms   | 49.1 ms: 2.37x faster  |
| hexiom                     | 7.27 ms  | 3.13 ms: 2.32x faster  |
| scimark_sor                | 135 ms   | 59.1 ms: 2.29x faster  |
| scimark_monte_carlo        | 73.9 ms  | 32.8 ms: 2.26x faster  |
| raytrace                   | 304 ms   | 137 ms: 2.21x faster   |
| comprehensions             | 19.4 us  | 8.84 us: 2.19x faster  |
| spectral_norm              | 97.7 ms  | 44.7 ms: 2.19x faster  |
| deepcopy_memo              | 32.9 us  | 15.1 us: 2.18x faster  |
| generators                 | 33.8 ms  | 15.8 ms: 2.14x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.05 ms: 2.12x faster  |
| go                         | 137 ms   | 65.1 ms: 2.10x faster  |
| chaos                      | 65.2 ms  | 31.1 ms: 2.10x faster  |
| mako                       | 11.7 ms  | 5.72 ms: 2.05x faster  |
| pickle_pure_python         | 355 us   | 175 us: 2.02x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 686 us: 1.98x faster   |
| nqueens                    | 94.3 ms  | 47.7 ms: 1.98x faster  |
| crypto_pyaes               | 77.9 ms  | 39.4 ms: 1.98x faster  |
| coroutines                 | 21.9 ms  | 11.1 ms: 1.97x faster  |
| float                      | 75.4 ms  | 38.5 ms: 1.96x faster  |
| fannkuch                   | 407 ms   | 209 ms: 1.95x faster   |
| genshi_text                | 23.2 ms  | 12.0 ms: 1.94x faster  |
| nbody                      | 101 ms   | 52.9 ms: 1.90x faster  |
| xml_etree_process          | 64.6 ms  | 34.0 ms: 1.90x faster  |
| pyflate                    | 462 ms   | 245 ms: 1.89x faster   |
| django_template            | 36.9 ms  | 19.5 ms: 1.89x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 868 us: 1.89x faster   |
| scimark_fft                | 269 ms   | 143 ms: 1.88x faster   |
| deepcopy_reduce            | 2.77 us  | 1.49 us: 1.86x faster  |
| deepcopy                   | 269 us   | 145 us: 1.86x faster   |
| xml_etree_generate         | 89.5 ms  | 48.4 ms: 1.85x faster  |
| pprint_pformat             | 1.61 sec | 874 ms: 1.84x faster   |
| pprint_safe_repr           | 788 ms   | 432 ms: 1.82x faster   |
| genshi_xml                 | 48.8 ms  | 27.4 ms: 1.78x faster  |
| sqlglot_v2_normalize       | 106 ms   | 59.9 ms: 1.77x faster  |
| tomli_loads                | 1.99 sec | 1.13 sec: 1.76x faster |
| typing_runtime_protocols   | 150 us   | 86.2 us: 1.74x faster  |
| async_generators           | 328 ms   | 188 ms: 1.74x faster   |
| bpe_tokeniser              | 4.30 sec | 2.50 sec: 1.72x faster |
| sqlglot_v2_optimize        | 51.0 ms  | 29.8 ms: 1.71x faster  |
| regex_compile              | 125 ms   | 73.4 ms: 1.70x faster  |
| logging_simple             | 8.87 us  | 5.39 us: 1.64x faster  |
| async_tree_none            | 249 ms   | 155 ms: 1.61x faster   |
| async_tree_none_tg         | 236 ms   | 147 ms: 1.60x faster   |
| thrift                     | 694 us   | 434 us: 1.60x faster   |
| logging_format             | 9.33 us  | 5.83 us: 1.60x faster  |
| async_tree_io_tg           | 559 ms   | 352 ms: 1.59x faster   |
| async_tree_io              | 553 ms   | 349 ms: 1.58x faster   |
| json_loads                 | 22.3 us  | 14.2 us: 1.57x faster  |
| async_tree_memoization     | 297 ms   | 190 ms: 1.57x faster   |
| json_dumps                 | 9.01 ms  | 5.76 ms: 1.56x faster  |
| sympy_str                  | 238 ms   | 153 ms: 1.56x faster   |
| sympy_expand               | 405 ms   | 259 ms: 1.56x faster   |
| pycparser                  | 992 ms   | 637 ms: 1.56x faster   |
| telco                      | 6.44 ms  | 4.20 ms: 1.53x faster  |
| coverage                   | 61.9 ms  | 40.9 ms: 1.51x faster  |
| sympy_integrate            | 17.8 ms  | 11.8 ms: 1.51x faster  |
| async_tree_memoization_tg  | 291 ms   | 195 ms: 1.49x faster   |
| xml_etree_iterparse        | 89.9 ms  | 60.7 ms: 1.48x faster  |
| sympy_sum                  | 119 ms   | 81.4 ms: 1.47x faster  |
| 2to3                       | 298 ms   | 204 ms: 1.46x faster   |
| subparsers                 | 20.8 ms  | 14.2 ms: 1.46x faster  |
| html5lib                   | 51.3 ms  | 35.2 ms: 1.46x faster  |
| sphinx                     | 872 ms   | 599 ms: 1.45x faster   |
| async_tree_cpu_io_mixed    | 437 ms   | 309 ms: 1.41x faster   |
| docutils                   | 2.17 sec | 1.55 sec: 1.40x faster |
| json                       | 3.96 ms  | 2.83 ms: 1.40x faster  |
| meteor_contest             | 95.9 ms  | 68.7 ms: 1.40x faster  |
| mdp                        | 1.81 sec | 1.30 sec: 1.39x faster |
| pylint                     | 253 ms   | 182 ms: 1.39x faster   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 310 ms: 1.37x faster   |
| many_optionals             | 547 us   | 405 us: 1.35x faster   |
| dulwich_log                | 51.0 ms  | 39.5 ms: 1.29x faster  |
| regex_v8                   | 17.1 ms  | 13.5 ms: 1.27x faster  |
| sqlite_synth               | 1.84 us  | 1.49 us: 1.23x faster  |
| xml_etree_parse            | 108 ms   | 88.8 ms: 1.22x faster  |
| k_core                     | 1.83 sec | 1.61 sec: 1.14x faster |
| pathlib                    | 34.4 ms  | 30.4 ms: 1.13x faster  |
| gc_traversal               | 3.15 ms  | 2.79 ms: 1.13x faster  |
| regex_effbot               | 1.81 ms  | 1.65 ms: 1.10x faster  |
| shortest_path              | 378 ms   | 345 ms: 1.10x faster   |
| connected_components       | 347 ms   | 325 ms: 1.07x faster   |
| python_startup             | 27.3 ms  | 26.6 ms: 1.03x faster  |
| pidigits                   | 152 ms   | 148 ms: 1.02x faster   |
| create_gc_cycles           | 1.40 ms  | 1.37 ms: 1.02x faster  |
| python_startup_no_site     | 20.4 ms  | 20.0 ms: 1.02x faster  |
| asyncio_websockets         | 317 ms   | 400 ms: 1.26x slower   |
| Geometric mean             | (ref)    | 1.64x faster           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.634x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.55x
- 95% likely to have a speedup of 1.54x
- 99% likely to have a speedup of 1.50x

# Memory
- memory change: unknown