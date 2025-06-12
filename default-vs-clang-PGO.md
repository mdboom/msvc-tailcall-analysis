# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.388x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.50x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | default                |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 298 ms: 1.46x slower   |
| docutils       | 1.55 sec  | 2.17 sec: 1.40x slower |
| html5lib       | 35.2 ms   | 51.3 ms: 1.46x slower  |
| sphinx         | 599 ms    | 872 ms: 1.45x slower   |
| Geometric mean | (ref)     | 1.44x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | default               |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 317 ms: 1.26x faster  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 424 ms: 1.37x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 437 ms: 1.41x slower  |
| async_tree_memoization_tg  | 195 ms    | 291 ms: 1.49x slower  |
| async_tree_memoization     | 190 ms    | 297 ms: 1.57x slower  |
| async_tree_io              | 349 ms    | 553 ms: 1.58x slower  |
| async_tree_io_tg           | 352 ms    | 559 ms: 1.59x slower  |
| async_tree_none_tg         | 147 ms    | 236 ms: 1.60x slower  |
| async_tree_none            | 155 ms    | 249 ms: 1.61x slower  |
| async_generators           | 188 ms    | 328 ms: 1.74x slower  |
| coroutines                 | 11.1 ms   | 21.9 ms: 1.97x slower |
| Geometric mean             | (ref)     | 1.49x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | default               |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 152 ms: 1.02x slower  |
| nbody          | 52.9 ms   | 101 ms: 1.90x slower  |
| float          | 38.5 ms   | 75.4 ms: 1.96x slower |
| Geometric mean | (ref)     | 1.56x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | default               |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.81 ms: 1.10x slower |
| regex_v8       | 13.5 ms   | 17.1 ms: 1.27x slower |
| regex_compile  | 73.4 ms   | 125 ms: 1.70x slower  |
| Geometric mean | (ref)     | 1.24x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | default                |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 108 ms: 1.22x slower   |
| xml_etree_iterparse  | 60.7 ms   | 89.9 ms: 1.48x slower  |
| json_dumps           | 5.76 ms   | 9.01 ms: 1.56x slower  |
| json_loads           | 14.2 us   | 22.3 us: 1.57x slower  |
| tomli_loads          | 1.13 sec  | 1.99 sec: 1.76x slower |
| xml_etree_generate   | 48.4 ms   | 89.5 ms: 1.85x slower  |
| xml_etree_process    | 34.0 ms   | 64.6 ms: 1.90x slower  |
| pickle_pure_python   | 175 us    | 355 us: 2.02x slower   |
| unpickle_pure_python | 109 us    | 274 us: 2.52x slower   |
| Geometric mean       | (ref)     | 1.73x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | default               |
|------------------------|:---------:|:---------------------:|
| python_startup_no_site | 20.0 ms   | 20.4 ms: 1.02x slower |
| python_startup         | 26.6 ms   | 27.3 ms: 1.03x slower |
| Geometric mean         | (ref)     | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | default               |
|-----------------|:---------:|:---------------------:|
| genshi_xml      | 27.4 ms   | 48.8 ms: 1.78x slower |
| django_template | 19.5 ms   | 36.9 ms: 1.89x slower |
| genshi_text     | 12.0 ms   | 23.2 ms: 1.94x slower |
| mako            | 5.72 ms   | 11.7 ms: 2.05x slower |
| Geometric mean  | (ref)     | 1.91x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | default                |
|----------------------------|:---------:|:----------------------:|
| asyncio_websockets         | 400 ms    | 317 ms: 1.26x faster   |
| python_startup_no_site     | 20.0 ms   | 20.4 ms: 1.02x slower  |
| create_gc_cycles           | 1.37 ms   | 1.40 ms: 1.02x slower  |
| pidigits                   | 148 ms    | 152 ms: 1.02x slower   |
| python_startup             | 26.6 ms   | 27.3 ms: 1.03x slower  |
| connected_components       | 325 ms    | 347 ms: 1.07x slower   |
| shortest_path              | 345 ms    | 378 ms: 1.10x slower   |
| regex_effbot               | 1.65 ms   | 1.81 ms: 1.10x slower  |
| gc_traversal               | 2.79 ms   | 3.15 ms: 1.13x slower  |
| pathlib                    | 30.4 ms   | 34.4 ms: 1.13x slower  |
| k_core                     | 1.61 sec  | 1.83 sec: 1.14x slower |
| xml_etree_parse            | 88.8 ms   | 108 ms: 1.22x slower   |
| sqlite_synth               | 1.49 us   | 1.84 us: 1.23x slower  |
| regex_v8                   | 13.5 ms   | 17.1 ms: 1.27x slower  |
| dulwich_log                | 39.5 ms   | 51.0 ms: 1.29x slower  |
| many_optionals             | 405 us    | 547 us: 1.35x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 424 ms: 1.37x slower   |
| pylint                     | 182 ms    | 253 ms: 1.39x slower   |
| mdp                        | 1.30 sec  | 1.81 sec: 1.39x slower |
| meteor_contest             | 68.7 ms   | 95.9 ms: 1.40x slower  |
| json                       | 2.83 ms   | 3.96 ms: 1.40x slower  |
| docutils                   | 1.55 sec  | 2.17 sec: 1.40x slower |
| async_tree_cpu_io_mixed    | 309 ms    | 437 ms: 1.41x slower   |
| sphinx                     | 599 ms    | 872 ms: 1.45x slower   |
| html5lib                   | 35.2 ms   | 51.3 ms: 1.46x slower  |
| subparsers                 | 14.2 ms   | 20.8 ms: 1.46x slower  |
| 2to3                       | 204 ms    | 298 ms: 1.46x slower   |
| sympy_sum                  | 81.4 ms   | 119 ms: 1.47x slower   |
| xml_etree_iterparse        | 60.7 ms   | 89.9 ms: 1.48x slower  |
| async_tree_memoization_tg  | 195 ms    | 291 ms: 1.49x slower   |
| sympy_integrate            | 11.8 ms   | 17.8 ms: 1.51x slower  |
| coverage                   | 40.9 ms   | 61.9 ms: 1.51x slower  |
| telco                      | 4.20 ms   | 6.44 ms: 1.53x slower  |
| pycparser                  | 637 ms    | 992 ms: 1.56x slower   |
| sympy_expand               | 259 ms    | 405 ms: 1.56x slower   |
| sympy_str                  | 153 ms    | 238 ms: 1.56x slower   |
| json_dumps                 | 5.76 ms   | 9.01 ms: 1.56x slower  |
| async_tree_memoization     | 190 ms    | 297 ms: 1.57x slower   |
| json_loads                 | 14.2 us   | 22.3 us: 1.57x slower  |
| async_tree_io              | 349 ms    | 553 ms: 1.58x slower   |
| async_tree_io_tg           | 352 ms    | 559 ms: 1.59x slower   |
| logging_format             | 5.83 us   | 9.33 us: 1.60x slower  |
| thrift                     | 434 us    | 694 us: 1.60x slower   |
| async_tree_none_tg         | 147 ms    | 236 ms: 1.60x slower   |
| async_tree_none            | 155 ms    | 249 ms: 1.61x slower   |
| logging_simple             | 5.39 us   | 8.87 us: 1.64x slower  |
| regex_compile              | 73.4 ms   | 125 ms: 1.70x slower   |
| sqlglot_v2_optimize        | 29.8 ms   | 51.0 ms: 1.71x slower  |
| bpe_tokeniser              | 2.50 sec  | 4.30 sec: 1.72x slower |
| async_generators           | 188 ms    | 328 ms: 1.74x slower   |
| typing_runtime_protocols   | 86.2 us   | 150 us: 1.74x slower   |
| tomli_loads                | 1.13 sec  | 1.99 sec: 1.76x slower |
| sqlglot_v2_normalize       | 59.9 ms   | 106 ms: 1.77x slower   |
| genshi_xml                 | 27.4 ms   | 48.8 ms: 1.78x slower  |
| pprint_safe_repr           | 432 ms    | 788 ms: 1.82x slower   |
| pprint_pformat             | 874 ms    | 1.61 sec: 1.84x slower |
| xml_etree_generate         | 48.4 ms   | 89.5 ms: 1.85x slower  |
| deepcopy                   | 145 us    | 269 us: 1.86x slower   |
| deepcopy_reduce            | 1.49 us   | 2.77 us: 1.86x slower  |
| scimark_fft                | 143 ms    | 269 ms: 1.88x slower   |
| sqlglot_v2_transpile       | 868 us    | 1.64 ms: 1.89x slower  |
| django_template            | 19.5 ms   | 36.9 ms: 1.89x slower  |
| pyflate                    | 245 ms    | 462 ms: 1.89x slower   |
| xml_etree_process          | 34.0 ms   | 64.6 ms: 1.90x slower  |
| nbody                      | 52.9 ms   | 101 ms: 1.90x slower   |
| genshi_text                | 12.0 ms   | 23.2 ms: 1.94x slower  |
| fannkuch                   | 209 ms    | 407 ms: 1.95x slower   |
| float                      | 38.5 ms   | 75.4 ms: 1.96x slower  |
| coroutines                 | 11.1 ms   | 21.9 ms: 1.97x slower  |
| crypto_pyaes               | 39.4 ms   | 77.9 ms: 1.98x slower  |
| nqueens                    | 47.7 ms   | 94.3 ms: 1.98x slower  |
| sqlglot_v2_parse           | 686 us    | 1.36 ms: 1.98x slower  |
| pickle_pure_python         | 175 us    | 355 us: 2.02x slower   |
| mako                       | 5.72 ms   | 11.7 ms: 2.05x slower  |
| chaos                      | 31.1 ms   | 65.2 ms: 2.10x slower  |
| go                         | 65.1 ms   | 137 ms: 2.10x slower   |
| scimark_sparse_mat_mult    | 2.05 ms   | 4.34 ms: 2.12x slower  |
| generators                 | 15.8 ms   | 33.8 ms: 2.14x slower  |
| deepcopy_memo              | 15.1 us   | 32.9 us: 2.18x slower  |
| spectral_norm              | 44.7 ms   | 97.7 ms: 2.19x slower  |
| comprehensions             | 8.84 us   | 19.4 us: 2.19x slower  |
| raytrace                   | 137 ms    | 304 ms: 2.21x slower   |
| scimark_monte_carlo        | 32.8 ms   | 73.9 ms: 2.26x slower  |
| scimark_sor                | 59.1 ms   | 135 ms: 2.29x slower   |
| hexiom                     | 3.13 ms   | 7.27 ms: 2.32x slower  |
| scimark_lu                 | 49.1 ms   | 116 ms: 2.37x slower   |
| unpickle_pure_python       | 109 us    | 274 us: 2.52x slower   |
| deltablue                  | 1.59 ms   | 4.09 ms: 2.57x slower  |
| richards                   | 21.9 ms   | 57.8 ms: 2.64x slower  |
| richards_super             | 24.6 ms   | 65.8 ms: 2.67x slower  |
| logging_silent             | 44.5 ns   | 119 ns: 2.69x slower   |
| Geometric mean             | (ref)     | 1.64x slower           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.388x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.55x
- 95% likely to have a slowdown of 1.54x
- 99% likely to have a slowdown of 1.50x

# Memory
- memory change: unknown