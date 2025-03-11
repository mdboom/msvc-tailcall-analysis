# Results vs. base

- fork: unknown
- ref: NoTC-NoPGO-NoEx
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.278x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------|:-----------:|:----------------------:|
| 2to3           | 231 ms      | 298 ms: 1.29x slower   |
| docutils       | 1.77 sec    | 2.17 sec: 1.23x slower |
| html5lib       | 38.8 ms     | 51.3 ms: 1.32x slower  |
| sphinx         | 702 ms      | 872 ms: 1.24x slower   |
| Geometric mean | (ref)       | 1.27x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 312 ms      | 317 ms: 1.02x slower  |
| async_tree_cpu_io_mixed_tg | 363 ms      | 424 ms: 1.17x slower  |
| async_tree_cpu_io_mixed    | 359 ms      | 437 ms: 1.21x slower  |
| async_tree_memoization_tg  | 210 ms      | 291 ms: 1.38x slower  |
| async_tree_none_tg         | 167 ms      | 236 ms: 1.41x slower  |
| async_tree_memoization     | 210 ms      | 297 ms: 1.42x slower  |
| async_tree_none            | 174 ms      | 249 ms: 1.44x slower  |
| async_tree_io              | 384 ms      | 553 ms: 1.44x slower  |
| async_tree_io_tg           | 385 ms      | 559 ms: 1.45x slower  |
| async_generators           | 213 ms      | 328 ms: 1.54x slower  |
| coroutines                 | 12.3 ms     | 21.9 ms: 1.79x slower |
| Geometric mean             | (ref)       | 1.37x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------|:-----------:|:---------------------:|
| pidigits       | 146 ms      | 152 ms: 1.04x slower  |
| float          | 41.4 ms     | 75.4 ms: 1.82x slower |
| nbody          | 53.1 ms     | 101 ms: 1.89x slower  |
| Geometric mean | (ref)       | 1.53x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.85 ms     | 1.81 ms: 1.02x faster |
| regex_v8       | 16.3 ms     | 17.1 ms: 1.05x slower |
| regex_compile  | 81.9 ms     | 125 ms: 1.52x slower  |
| Geometric mean | (ref)       | 1.12x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.9 us     | 22.3 us: 1.02x slower  |
| xml_etree_parse      | 105 ms      | 108 ms: 1.03x slower   |
| json_dumps           | 7.79 ms     | 9.01 ms: 1.16x slower  |
| xml_etree_iterparse  | 70.4 ms     | 89.9 ms: 1.28x slower  |
| xml_etree_generate   | 64.7 ms     | 89.5 ms: 1.38x slower  |
| xml_etree_process    | 44.7 ms     | 64.6 ms: 1.44x slower  |
| tomli_loads          | 1.26 sec    | 1.99 sec: 1.58x slower |
| pickle_pure_python   | 223 us      | 355 us: 1.59x slower   |
| unpickle_pure_python | 148 us      | 274 us: 1.85x slower   |
| Geometric mean       | (ref)       | 1.35x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.4 ms     | 27.3 ms: 1.04x slower |
| python_startup_no_site | 19.4 ms     | 20.4 ms: 1.05x slower |
| Geometric mean         | (ref)       | 1.04x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-NoPGO-Ex | NoTC-NoPGO-NoEx       |
|-----------------|:-----------:|:---------------------:|
| django_template | 25.2 ms     | 36.9 ms: 1.46x slower |
| mako            | 7.84 ms     | 11.7 ms: 1.49x slower |
| genshi_xml      | 31.3 ms     | 48.8 ms: 1.56x slower |
| genshi_text     | 14.5 ms     | 23.2 ms: 1.60x slower |
| Geometric mean  | (ref)       | 1.53x slower          |

All benchmarks:
===============

| Benchmark                  | TC-NoPGO-Ex | NoTC-NoPGO-NoEx        |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 44.5 ms     | 20.8 ms: 2.14x faster  |
| many_optionals             | 762 us      | 547 us: 1.39x faster   |
| regex_effbot               | 1.85 ms     | 1.81 ms: 1.02x faster  |
| asyncio_websockets         | 312 ms      | 317 ms: 1.02x slower   |
| json_loads                 | 21.9 us     | 22.3 us: 1.02x slower  |
| bench_mp_pool              | 93.6 ms     | 96.2 ms: 1.03x slower  |
| xml_etree_parse            | 105 ms      | 108 ms: 1.03x slower   |
| python_startup             | 26.4 ms     | 27.3 ms: 1.04x slower  |
| pidigits                   | 146 ms      | 152 ms: 1.04x slower   |
| json                       | 3.78 ms     | 3.96 ms: 1.05x slower  |
| create_gc_cycles           | 1.34 ms     | 1.40 ms: 1.05x slower  |
| regex_v8                   | 16.3 ms     | 17.1 ms: 1.05x slower  |
| python_startup_no_site     | 19.4 ms     | 20.4 ms: 1.05x slower  |
| k_core                     | 1.71 sec    | 1.83 sec: 1.07x slower |
| shortest_path              | 347 ms      | 378 ms: 1.09x slower   |
| sqlite_synth               | 1.68 us     | 1.84 us: 1.10x slower  |
| gc_traversal               | 2.83 ms     | 3.15 ms: 1.11x slower  |
| connected_components       | 311 ms      | 347 ms: 1.11x slower   |
| coverage                   | 55.4 ms     | 61.9 ms: 1.12x slower  |
| bench_thread_pool          | 876 us      | 1.01 ms: 1.15x slower  |
| json_dumps                 | 7.79 ms     | 9.01 ms: 1.16x slower  |
| async_tree_cpu_io_mixed_tg | 363 ms      | 424 ms: 1.17x slower   |
| dulwich_log                | 42.3 ms     | 51.0 ms: 1.21x slower  |
| async_tree_cpu_io_mixed    | 359 ms      | 437 ms: 1.21x slower   |
| telco                      | 5.26 ms     | 6.44 ms: 1.22x slower  |
| docutils                   | 1.77 sec    | 2.17 sec: 1.23x slower |
| pylint                     | 205 ms      | 253 ms: 1.23x slower   |
| sphinx                     | 702 ms      | 872 ms: 1.24x slower   |
| mdp                        | 1.44 sec    | 1.81 sec: 1.26x slower |
| thrift                     | 551 us      | 694 us: 1.26x slower   |
| xml_etree_iterparse        | 70.4 ms     | 89.9 ms: 1.28x slower  |
| meteor_contest             | 74.5 ms     | 95.9 ms: 1.29x slower  |
| 2to3                       | 231 ms      | 298 ms: 1.29x slower   |
| sympy_sum                  | 91.4 ms     | 119 ms: 1.31x slower   |
| html5lib                   | 38.8 ms     | 51.3 ms: 1.32x slower  |
| sympy_integrate            | 13.4 ms     | 17.8 ms: 1.33x slower  |
| sympy_expand               | 304 ms      | 405 ms: 1.33x slower   |
| sympy_str                  | 177 ms      | 238 ms: 1.35x slower   |
| pathlib                    | 25.1 ms     | 34.4 ms: 1.37x slower  |
| xml_etree_generate         | 64.7 ms     | 89.5 ms: 1.38x slower  |
| async_tree_memoization_tg  | 210 ms      | 291 ms: 1.38x slower   |
| pycparser                  | 713 ms      | 992 ms: 1.39x slower   |
| logging_format             | 6.70 us     | 9.33 us: 1.39x slower  |
| sqlglot_v2_optimize        | 36.1 ms     | 51.0 ms: 1.41x slower  |
| async_tree_none_tg         | 167 ms      | 236 ms: 1.41x slower   |
| async_tree_memoization     | 210 ms      | 297 ms: 1.42x slower   |
| logging_simple             | 6.25 us     | 8.87 us: 1.42x slower  |
| typing_runtime_protocols   | 106 us      | 150 us: 1.42x slower   |
| bpe_tokeniser              | 3.01 sec    | 4.30 sec: 1.43x slower |
| async_tree_none            | 174 ms      | 249 ms: 1.44x slower   |
| async_tree_io              | 384 ms      | 553 ms: 1.44x slower   |
| xml_etree_process          | 44.7 ms     | 64.6 ms: 1.44x slower  |
| sqlglot_v2_normalize       | 73.3 ms     | 106 ms: 1.45x slower   |
| async_tree_io_tg           | 385 ms      | 559 ms: 1.45x slower   |
| deepcopy_reduce            | 1.90 us     | 2.77 us: 1.46x slower  |
| django_template            | 25.2 ms     | 36.9 ms: 1.46x slower  |
| mako                       | 7.84 ms     | 11.7 ms: 1.49x slower  |
| deepcopy                   | 180 us      | 269 us: 1.49x slower   |
| regex_compile              | 81.9 ms     | 125 ms: 1.52x slower   |
| async_generators           | 213 ms      | 328 ms: 1.54x slower   |
| pprint_safe_repr           | 510 ms      | 788 ms: 1.54x slower   |
| pprint_pformat             | 1.04 sec    | 1.61 sec: 1.55x slower |
| genshi_xml                 | 31.3 ms     | 48.8 ms: 1.56x slower  |
| tomli_loads                | 1.26 sec    | 1.99 sec: 1.58x slower |
| nqueens                    | 59.6 ms     | 94.3 ms: 1.58x slower  |
| scimark_fft                | 169 ms      | 269 ms: 1.59x slower   |
| pickle_pure_python         | 223 us      | 355 us: 1.59x slower   |
| genshi_text                | 14.5 ms     | 23.2 ms: 1.60x slower  |
| sqlglot_v2_transpile       | 1.01 ms     | 1.64 ms: 1.62x slower  |
| crypto_pyaes               | 48.0 ms     | 77.9 ms: 1.62x slower  |
| fannkuch                   | 250 ms      | 407 ms: 1.63x slower   |
| pyflate                    | 274 ms      | 462 ms: 1.69x slower   |
| sqlglot_v2_parse           | 798 us      | 1.36 ms: 1.70x slower  |
| deepcopy_memo              | 19.3 us     | 32.9 us: 1.71x slower  |
| comprehensions             | 11.3 us     | 19.4 us: 1.71x slower  |
| chaos                      | 37.7 ms     | 65.2 ms: 1.73x slower  |
| scimark_sparse_mat_mult    | 2.47 ms     | 4.34 ms: 1.76x slower  |
| coroutines                 | 12.3 ms     | 21.9 ms: 1.79x slower  |
| raytrace                   | 169 ms      | 304 ms: 1.79x slower   |
| scimark_lu                 | 64.2 ms     | 116 ms: 1.81x slower   |
| float                      | 41.4 ms     | 75.4 ms: 1.82x slower  |
| richards_super             | 35.8 ms     | 65.8 ms: 1.84x slower  |
| unpickle_pure_python       | 148 us      | 274 us: 1.85x slower   |
| hexiom                     | 3.92 ms     | 7.27 ms: 1.86x slower  |
| richards                   | 30.9 ms     | 57.8 ms: 1.87x slower  |
| nbody                      | 53.1 ms     | 101 ms: 1.89x slower   |
| scimark_monte_carlo        | 38.9 ms     | 73.9 ms: 1.90x slower  |
| spectral_norm              | 51.1 ms     | 97.7 ms: 1.91x slower  |
| go                         | 70.4 ms     | 137 ms: 1.94x slower   |
| logging_silent             | 61.1 ns     | 119 ns: 1.95x slower   |
| scimark_sor                | 68.6 ms     | 135 ms: 1.97x slower   |
| generators                 | 16.3 ms     | 33.8 ms: 2.07x slower  |
| deltablue                  | 1.91 ms     | 4.09 ms: 2.14x slower  |
| Geometric mean             | (ref)       | 1.39x slower           |

Benchmark hidden because not significant (1): regex_dna

- Geometric mean (including insignificant results): 1.278x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.35x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: unknown