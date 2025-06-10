# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.379x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2                |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 293 ms: 1.44x slower   |
| docutils       | 1.58 sec   | 2.11 sec: 1.34x slower |
| html5lib       | 35.5 ms    | 51.3 ms: 1.45x slower  |
| sphinx         | 615 ms     | 843 ms: 1.37x slower   |
| Geometric mean | (ref)      | 1.40x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-Ex2               |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 304 ms     | 311 ms: 1.02x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 428 ms: 1.32x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 434 ms: 1.33x slower  |
| async_tree_memoization_tg  | 201 ms     | 292 ms: 1.45x slower  |
| async_tree_memoization     | 196 ms     | 297 ms: 1.51x slower  |
| async_tree_io              | 353 ms     | 551 ms: 1.56x slower  |
| async_tree_none_tg         | 150 ms     | 236 ms: 1.57x slower  |
| async_tree_none            | 157 ms     | 248 ms: 1.58x slower  |
| async_tree_io_tg           | 356 ms     | 563 ms: 1.58x slower  |
| async_generators           | 199 ms     | 321 ms: 1.62x slower  |
| coroutines                 | 10.8 ms    | 22.1 ms: 2.05x slower |
| Geometric mean             | (ref)      | 1.49x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 148 ms: 1.02x slower  |
| float          | 37.1 ms    | 73.5 ms: 1.98x slower |
| nbody          | 45.7 ms    | 98.8 ms: 2.16x slower |
| Geometric mean | (ref)      | 1.63x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 118 ms: 1.03x faster  |
| regex_v8       | 13.9 ms    | 17.0 ms: 1.22x slower |
| regex_effbot   | 1.45 ms    | 1.77 ms: 1.22x slower |
| regex_compile  | 70.7 ms    | 123 ms: 1.74x slower  |
| Geometric mean | (ref)      | 1.26x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-Ex2                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 108 ms: 1.21x slower   |
| json_loads           | 14.8 us    | 21.4 us: 1.45x slower  |
| json_dumps           | 6.19 ms    | 8.99 ms: 1.45x slower  |
| xml_etree_iterparse  | 59.5 ms    | 87.5 ms: 1.47x slower  |
| xml_etree_generate   | 49.4 ms    | 87.5 ms: 1.77x slower  |
| xml_etree_process    | 33.8 ms    | 63.0 ms: 1.87x slower  |
| tomli_loads          | 1.03 sec   | 1.97 sec: 1.91x slower |
| pickle_pure_python   | 184 us     | 354 us: 1.93x slower   |
| unpickle_pure_python | 110 us     | 271 us: 2.48x slower   |
| Geometric mean       | (ref)      | 1.69x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TCO-Ex2               |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 20.3 ms: 1.09x slower |
| python_startup         | 24.7 ms    | 27.2 ms: 1.10x slower |
| Geometric mean         | (ref)      | 1.09x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-Ex2               |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 48.8 ms: 1.66x slower |
| django_template | 20.9 ms    | 35.8 ms: 1.71x slower |
| genshi_text     | 12.3 ms    | 23.4 ms: 1.89x slower |
| mako            | 5.80 ms    | 11.4 ms: 1.97x slower |
| Geometric mean  | (ref)      | 1.80x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-Ex2                |
|----------------------------|:----------:|:----------------------:|
| regex_dna                  | 121 ms     | 118 ms: 1.03x faster   |
| pidigits                   | 145 ms     | 148 ms: 1.02x slower   |
| asyncio_websockets         | 304 ms     | 311 ms: 1.02x slower   |
| python_startup_no_site     | 18.7 ms    | 20.3 ms: 1.09x slower  |
| connected_components       | 320 ms     | 351 ms: 1.09x slower   |
| k_core                     | 1.67 sec   | 1.83 sec: 1.10x slower |
| python_startup             | 24.7 ms    | 27.2 ms: 1.10x slower  |
| shortest_path              | 347 ms     | 384 ms: 1.10x slower   |
| create_gc_cycles           | 1.26 ms    | 1.40 ms: 1.11x slower  |
| pathlib                    | 23.6 ms    | 26.8 ms: 1.14x slower  |
| sqlite_synth               | 1.56 us    | 1.78 us: 1.15x slower  |
| xml_etree_parse            | 89.4 ms    | 108 ms: 1.21x slower   |
| regex_v8                   | 13.9 ms    | 17.0 ms: 1.22x slower  |
| regex_effbot               | 1.45 ms    | 1.77 ms: 1.22x slower  |
| subparsers                 | 40.6 ms    | 50.4 ms: 1.24x slower  |
| dulwich_log                | 39.1 ms    | 50.5 ms: 1.29x slower  |
| pylint                     | 193 ms     | 249 ms: 1.29x slower   |
| mdp                        | 1.41 sec   | 1.82 sec: 1.30x slower |
| async_tree_cpu_io_mixed_tg | 325 ms     | 428 ms: 1.32x slower   |
| coverage                   | 46.2 ms    | 61.1 ms: 1.32x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 434 ms: 1.33x slower   |
| json                       | 2.95 ms    | 3.94 ms: 1.33x slower  |
| gc_traversal               | 2.09 ms    | 2.79 ms: 1.33x slower  |
| docutils                   | 1.58 sec   | 2.11 sec: 1.34x slower |
| many_optionals             | 659 us     | 890 us: 1.35x slower   |
| sphinx                     | 615 ms     | 843 ms: 1.37x slower   |
| telco                      | 4.45 ms    | 6.34 ms: 1.43x slower  |
| meteor_contest             | 66.6 ms    | 95.0 ms: 1.43x slower  |
| 2to3                       | 204 ms     | 293 ms: 1.44x slower   |
| html5lib                   | 35.5 ms    | 51.3 ms: 1.45x slower  |
| json_loads                 | 14.8 us    | 21.4 us: 1.45x slower  |
| json_dumps                 | 6.19 ms    | 8.99 ms: 1.45x slower  |
| async_tree_memoization_tg  | 201 ms     | 292 ms: 1.45x slower   |
| sympy_sum                  | 80.7 ms    | 118 ms: 1.46x slower   |
| sympy_integrate            | 12.0 ms    | 17.5 ms: 1.46x slower  |
| xml_etree_iterparse        | 59.5 ms    | 87.5 ms: 1.47x slower  |
| thrift                     | 461 us     | 680 us: 1.47x slower   |
| pycparser                  | 642 ms     | 968 ms: 1.51x slower   |
| async_tree_memoization     | 196 ms     | 297 ms: 1.51x slower   |
| sympy_expand               | 263 ms     | 399 ms: 1.52x slower   |
| sympy_str                  | 153 ms     | 234 ms: 1.53x slower   |
| logging_format             | 5.90 us    | 9.13 us: 1.55x slower  |
| async_tree_io              | 353 ms     | 551 ms: 1.56x slower   |
| async_tree_none_tg         | 150 ms     | 236 ms: 1.57x slower   |
| async_tree_none            | 157 ms     | 248 ms: 1.58x slower   |
| async_tree_io_tg           | 356 ms     | 563 ms: 1.58x slower   |
| logging_simple             | 5.42 us    | 8.63 us: 1.59x slower  |
| async_generators           | 199 ms     | 321 ms: 1.62x slower   |
| sqlglot_v2_optimize        | 30.5 ms    | 49.6 ms: 1.63x slower  |
| typing_runtime_protocols   | 89.7 us    | 146 us: 1.63x slower   |
| sqlglot_v2_normalize       | 62.6 ms    | 103 ms: 1.65x slower   |
| genshi_xml                 | 29.5 ms    | 48.8 ms: 1.66x slower  |
| bpe_tokeniser              | 2.52 sec   | 4.30 sec: 1.71x slower |
| django_template            | 20.9 ms    | 35.8 ms: 1.71x slower  |
| regex_compile              | 70.7 ms    | 123 ms: 1.74x slower   |
| xml_etree_generate         | 49.4 ms    | 87.5 ms: 1.77x slower  |
| deepcopy_reduce            | 1.51 us    | 2.71 us: 1.79x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.62 ms: 1.81x slower  |
| deepcopy                   | 147 us     | 266 us: 1.82x slower   |
| pprint_safe_repr           | 429 ms     | 789 ms: 1.84x slower   |
| xml_etree_process          | 33.8 ms    | 63.0 ms: 1.87x slower  |
| nqueens                    | 49.7 ms    | 93.2 ms: 1.87x slower  |
| genshi_text                | 12.3 ms    | 23.4 ms: 1.89x slower  |
| pprint_pformat             | 853 ms     | 1.61 sec: 1.89x slower |
| fannkuch                   | 203 ms     | 386 ms: 1.90x slower   |
| crypto_pyaes               | 40.4 ms    | 76.8 ms: 1.90x slower  |
| scimark_fft                | 140 ms     | 267 ms: 1.91x slower   |
| tomli_loads                | 1.03 sec   | 1.97 sec: 1.91x slower |
| pickle_pure_python         | 184 us     | 354 us: 1.93x slower   |
| pyflate                    | 236 ms     | 457 ms: 1.94x slower   |
| sqlglot_v2_parse           | 695 us     | 1.34 ms: 1.94x slower  |
| richards_super             | 29.4 ms    | 58.0 ms: 1.97x slower  |
| mako                       | 5.80 ms    | 11.4 ms: 1.97x slower  |
| float                      | 37.1 ms    | 73.5 ms: 1.98x slower  |
| richards                   | 25.5 ms    | 51.0 ms: 2.00x slower  |
| coroutines                 | 10.8 ms    | 22.1 ms: 2.05x slower  |
| raytrace                   | 145 ms     | 306 ms: 2.11x slower   |
| scimark_sparse_mat_mult    | 2.02 ms    | 4.27 ms: 2.11x slower  |
| chaos                      | 31.3 ms    | 67.0 ms: 2.14x slower  |
| nbody                      | 45.7 ms    | 98.8 ms: 2.16x slower  |
| comprehensions             | 8.65 us    | 19.4 us: 2.24x slower  |
| deepcopy_memo              | 14.7 us    | 33.0 us: 2.25x slower  |
| go                         | 61.0 ms    | 138 ms: 2.27x slower   |
| generators                 | 14.2 ms    | 33.5 ms: 2.35x slower  |
| spectral_norm              | 40.9 ms    | 97.1 ms: 2.37x slower  |
| scimark_monte_carlo        | 31.5 ms    | 75.2 ms: 2.39x slower  |
| hexiom                     | 3.00 ms    | 7.27 ms: 2.43x slower  |
| unpickle_pure_python       | 110 us     | 271 us: 2.48x slower   |
| deltablue                  | 1.64 ms    | 4.08 ms: 2.48x slower  |
| scimark_sor                | 51.1 ms    | 133 ms: 2.61x slower   |
| scimark_lu                 | 44.3 ms    | 116 ms: 2.61x slower   |
| logging_silent             | 44.1 ns    | 121 ns: 2.76x slower   |
| Geometric mean             | (ref)      | 1.62x slower           |
Ignored benchmarks (2) of TCO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.379x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.48x
- 99% likely to have a slowdown of 1.45x

# Memory
- memory change: unknown