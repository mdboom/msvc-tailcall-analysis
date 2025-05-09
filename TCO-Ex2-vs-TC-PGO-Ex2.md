# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.337x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-Ex2                |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 293 ms: 1.36x slower   |
| docutils       | 1.63 sec   | 2.11 sec: 1.30x slower |
| html5lib       | 36.1 ms    | 51.3 ms: 1.42x slower  |
| sphinx         | 638 ms     | 843 ms: 1.32x slower   |
| Geometric mean | (ref)      | 1.35x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | TCO-Ex2               |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 317 ms     | 311 ms: 1.02x faster  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 428 ms: 1.31x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 434 ms: 1.32x slower  |
| async_tree_memoization_tg  | 209 ms     | 292 ms: 1.40x slower  |
| async_tree_memoization     | 205 ms     | 297 ms: 1.45x slower  |
| async_tree_none            | 170 ms     | 248 ms: 1.46x slower  |
| async_tree_io              | 375 ms     | 551 ms: 1.47x slower  |
| async_tree_none_tg         | 159 ms     | 236 ms: 1.48x slower  |
| async_tree_io_tg           | 371 ms     | 563 ms: 1.52x slower  |
| async_generators           | 206 ms     | 321 ms: 1.56x slower  |
| coroutines                 | 12.4 ms    | 22.1 ms: 1.77x slower |
| Geometric mean             | (ref)      | 1.42x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 148 ms: 1.01x slower  |
| float          | 40.2 ms    | 73.5 ms: 1.83x slower |
| nbody          | 53.3 ms    | 98.8 ms: 1.86x slower |
| Geometric mean | (ref)      | 1.51x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 118 ms: 1.02x slower  |
| regex_v8       | 14.1 ms    | 17.0 ms: 1.20x slower |
| regex_effbot   | 1.40 ms    | 1.77 ms: 1.27x slower |
| regex_compile  | 74.8 ms    | 123 ms: 1.64x slower  |
| Geometric mean | (ref)      | 1.27x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TCO-Ex2                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.0 ms    | 108 ms: 1.21x slower   |
| json_dumps           | 6.48 ms    | 8.99 ms: 1.39x slower  |
| xml_etree_iterparse  | 60.4 ms    | 87.5 ms: 1.45x slower  |
| json_loads           | 14.5 us    | 21.4 us: 1.48x slower  |
| tomli_loads          | 1.17 sec   | 1.97 sec: 1.68x slower |
| xml_etree_generate   | 51.5 ms    | 87.5 ms: 1.70x slower  |
| xml_etree_process    | 36.7 ms    | 63.0 ms: 1.72x slower  |
| pickle_pure_python   | 201 us     | 354 us: 1.76x slower   |
| unpickle_pure_python | 123 us     | 271 us: 2.21x slower   |
| Geometric mean       | (ref)      | 1.60x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TCO-Ex2               |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 20.3 ms: 1.04x slower |
| python_startup         | 26.0 ms    | 27.2 ms: 1.05x slower |
| Geometric mean         | (ref)      | 1.04x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TCO-Ex2               |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 35.8 ms: 1.53x slower |
| genshi_xml      | 30.7 ms    | 48.8 ms: 1.59x slower |
| genshi_text     | 14.2 ms    | 23.4 ms: 1.64x slower |
| mako            | 6.12 ms    | 11.4 ms: 1.87x slower |
| Geometric mean  | (ref)      | 1.65x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | TCO-Ex2                |
|----------------------------|:----------:|:----------------------:|
| asyncio_websockets         | 317 ms     | 311 ms: 1.02x faster   |
| pidigits                   | 146 ms     | 148 ms: 1.01x slower   |
| regex_dna                  | 115 ms     | 118 ms: 1.02x slower   |
| python_startup_no_site     | 19.6 ms    | 20.3 ms: 1.04x slower  |
| python_startup             | 26.0 ms    | 27.2 ms: 1.05x slower  |
| k_core                     | 1.71 sec   | 1.83 sec: 1.07x slower |
| connected_components       | 321 ms     | 351 ms: 1.09x slower   |
| bench_mp_pool              | 89.1 ms    | 97.6 ms: 1.10x slower  |
| pathlib                    | 24.3 ms    | 26.8 ms: 1.10x slower  |
| shortest_path              | 348 ms     | 384 ms: 1.10x slower   |
| create_gc_cycles           | 1.27 ms    | 1.40 ms: 1.10x slower  |
| subparsers                 | 44.9 ms    | 50.4 ms: 1.12x slower  |
| sqlite_synth               | 1.56 us    | 1.78 us: 1.15x slower  |
| many_optionals             | 761 us     | 890 us: 1.17x slower   |
| bench_thread_pool          | 851 us     | 1.01 ms: 1.19x slower  |
| regex_v8                   | 14.1 ms    | 17.0 ms: 1.20x slower  |
| xml_etree_parse            | 89.0 ms    | 108 ms: 1.21x slower   |
| coverage                   | 49.5 ms    | 61.1 ms: 1.24x slower  |
| pylint                     | 199 ms     | 249 ms: 1.25x slower   |
| regex_effbot               | 1.40 ms    | 1.77 ms: 1.27x slower  |
| dulwich_log                | 39.5 ms    | 50.5 ms: 1.28x slower  |
| docutils                   | 1.63 sec   | 2.11 sec: 1.30x slower |
| mdp                        | 1.40 sec   | 1.82 sec: 1.30x slower |
| async_tree_cpu_io_mixed_tg | 328 ms     | 428 ms: 1.31x slower   |
| async_tree_cpu_io_mixed    | 329 ms     | 434 ms: 1.32x slower   |
| json                       | 2.98 ms    | 3.94 ms: 1.32x slower  |
| sphinx                     | 638 ms     | 843 ms: 1.32x slower   |
| gc_traversal               | 2.07 ms    | 2.79 ms: 1.35x slower  |
| 2to3                       | 216 ms     | 293 ms: 1.36x slower   |
| meteor_contest             | 69.5 ms    | 95.0 ms: 1.37x slower  |
| json_dumps                 | 6.48 ms    | 8.99 ms: 1.39x slower  |
| telco                      | 4.54 ms    | 6.34 ms: 1.40x slower  |
| async_tree_memoization_tg  | 209 ms     | 292 ms: 1.40x slower   |
| thrift                     | 482 us     | 680 us: 1.41x slower   |
| html5lib                   | 36.1 ms    | 51.3 ms: 1.42x slower  |
| sympy_sum                  | 82.1 ms    | 118 ms: 1.43x slower   |
| sympy_integrate            | 12.2 ms    | 17.5 ms: 1.44x slower  |
| logging_format             | 6.34 us    | 9.13 us: 1.44x slower  |
| xml_etree_iterparse        | 60.4 ms    | 87.5 ms: 1.45x slower  |
| async_tree_memoization     | 205 ms     | 297 ms: 1.45x slower   |
| pycparser                  | 664 ms     | 968 ms: 1.46x slower   |
| async_tree_none            | 170 ms     | 248 ms: 1.46x slower   |
| async_tree_io              | 375 ms     | 551 ms: 1.47x slower   |
| async_tree_none_tg         | 159 ms     | 236 ms: 1.48x slower   |
| typing_runtime_protocols   | 98.9 us    | 146 us: 1.48x slower   |
| json_loads                 | 14.5 us    | 21.4 us: 1.48x slower  |
| sympy_expand               | 269 ms     | 399 ms: 1.48x slower   |
| sympy_str                  | 158 ms     | 234 ms: 1.49x slower   |
| logging_simple             | 5.78 us    | 8.63 us: 1.49x slower  |
| async_tree_io_tg           | 371 ms     | 563 ms: 1.52x slower   |
| django_template            | 23.4 ms    | 35.8 ms: 1.53x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 49.6 ms: 1.54x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 103 ms: 1.55x slower   |
| async_generators           | 206 ms     | 321 ms: 1.56x slower   |
| genshi_xml                 | 30.7 ms    | 48.8 ms: 1.59x slower  |
| bpe_tokeniser              | 2.71 sec   | 4.30 sec: 1.59x slower |
| deepcopy_reduce            | 1.66 us    | 2.71 us: 1.63x slower  |
| fannkuch                   | 236 ms     | 386 ms: 1.64x slower   |
| regex_compile              | 74.8 ms    | 123 ms: 1.64x slower   |
| genshi_text                | 14.2 ms    | 23.4 ms: 1.64x slower  |
| pprint_safe_repr           | 478 ms     | 789 ms: 1.65x slower   |
| deepcopy                   | 160 us     | 266 us: 1.66x slower   |
| pprint_pformat             | 968 ms     | 1.61 sec: 1.67x slower |
| tomli_loads                | 1.17 sec   | 1.97 sec: 1.68x slower |
| xml_etree_generate         | 51.5 ms    | 87.5 ms: 1.70x slower  |
| xml_etree_process          | 36.7 ms    | 63.0 ms: 1.72x slower  |
| nqueens                    | 54.0 ms    | 93.2 ms: 1.72x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.62 ms: 1.73x slower  |
| pickle_pure_python         | 201 us     | 354 us: 1.76x slower   |
| scimark_fft                | 152 ms     | 267 ms: 1.76x slower   |
| pyflate                    | 260 ms     | 457 ms: 1.76x slower   |
| coroutines                 | 12.4 ms    | 22.1 ms: 1.77x slower  |
| richards_super             | 32.2 ms    | 58.0 ms: 1.80x slower  |
| sqlglot_v2_parse           | 740 us     | 1.34 ms: 1.82x slower  |
| float                      | 40.2 ms    | 73.5 ms: 1.83x slower  |
| richards                   | 27.8 ms    | 51.0 ms: 1.83x slower  |
| raytrace                   | 166 ms     | 306 ms: 1.84x slower   |
| crypto_pyaes               | 41.6 ms    | 76.8 ms: 1.84x slower  |
| nbody                      | 53.3 ms    | 98.8 ms: 1.86x slower  |
| chaos                      | 35.9 ms    | 67.0 ms: 1.87x slower  |
| mako                       | 6.12 ms    | 11.4 ms: 1.87x slower  |
| scimark_sparse_mat_mult    | 2.26 ms    | 4.27 ms: 1.89x slower  |
| spectral_norm              | 51.1 ms    | 97.1 ms: 1.90x slower  |
| deepcopy_memo              | 17.0 us    | 33.0 us: 1.94x slower  |
| scimark_sor                | 67.5 ms    | 133 ms: 1.97x slower   |
| comprehensions             | 9.73 us    | 19.4 us: 1.99x slower  |
| go                         | 68.4 ms    | 138 ms: 2.02x slower   |
| scimark_monte_carlo        | 37.0 ms    | 75.2 ms: 2.03x slower  |
| hexiom                     | 3.47 ms    | 7.27 ms: 2.09x slower  |
| scimark_lu                 | 54.4 ms    | 116 ms: 2.13x slower   |
| deltablue                  | 1.85 ms    | 4.08 ms: 2.20x slower  |
| unpickle_pure_python       | 123 us     | 271 us: 2.21x slower   |
| generators                 | 14.8 ms    | 33.5 ms: 2.26x slower  |
| logging_silent             | 53.3 ns    | 121 ns: 2.28x slower   |
| Geometric mean             | (ref)      | 1.51x slower           |

- Geometric mean (including insignificant results): 1.337x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.43x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: unknown