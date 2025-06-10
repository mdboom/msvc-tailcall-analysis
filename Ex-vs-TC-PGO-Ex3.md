# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.404x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | Ex                     |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 309 ms: 1.51x slower   |
| docutils       | 1.58 sec   | 2.31 sec: 1.46x slower |
| html5lib       | 35.5 ms    | 52.5 ms: 1.48x slower  |
| sphinx         | 615 ms     | 933 ms: 1.52x slower   |
| Geometric mean | (ref)      | 1.49x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | Ex                    |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 304 ms     | 330 ms: 1.08x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 444 ms: 1.37x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 455 ms: 1.39x slower  |
| async_tree_memoization_tg  | 201 ms     | 304 ms: 1.52x slower  |
| async_tree_memoization     | 196 ms     | 313 ms: 1.59x slower  |
| async_tree_io              | 353 ms     | 570 ms: 1.61x slower  |
| async_tree_io_tg           | 356 ms     | 576 ms: 1.62x slower  |
| async_tree_none_tg         | 150 ms     | 243 ms: 1.62x slower  |
| async_tree_none            | 157 ms     | 267 ms: 1.70x slower  |
| async_generators           | 199 ms     | 348 ms: 1.75x slower  |
| coroutines                 | 10.8 ms    | 22.4 ms: 2.08x slower |
| Geometric mean             | (ref)      | 1.56x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | Ex                    |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 156 ms: 1.08x slower  |
| float          | 37.1 ms    | 78.0 ms: 2.10x slower |
| nbody          | 45.7 ms    | 103 ms: 2.26x slower  |
| Geometric mean | (ref)      | 1.72x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | Ex                    |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 123 ms: 1.02x slower  |
| regex_v8       | 13.9 ms    | 17.5 ms: 1.26x slower |
| regex_effbot   | 1.45 ms    | 1.87 ms: 1.28x slower |
| regex_compile  | 70.7 ms    | 130 ms: 1.84x slower  |
| Geometric mean | (ref)      | 1.32x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | Ex                     |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 112 ms: 1.26x slower   |
| json_dumps           | 6.19 ms    | 9.44 ms: 1.52x slower  |
| json_loads           | 14.8 us    | 23.3 us: 1.58x slower  |
| xml_etree_iterparse  | 59.5 ms    | 94.3 ms: 1.58x slower  |
| xml_etree_generate   | 49.4 ms    | 92.6 ms: 1.87x slower  |
| xml_etree_process    | 33.8 ms    | 66.9 ms: 1.98x slower  |
| pickle_pure_python   | 184 us     | 364 us: 1.98x slower   |
| tomli_loads          | 1.03 sec   | 2.07 sec: 2.01x slower |
| unpickle_pure_python | 110 us     | 284 us: 2.59x slower   |
| Geometric mean       | (ref)      | 1.78x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | Ex                    |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 22.0 ms: 1.18x slower |
| python_startup         | 24.7 ms    | 29.5 ms: 1.19x slower |
| Geometric mean         | (ref)      | 1.18x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | Ex                    |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 50.4 ms: 1.71x slower |
| django_template | 20.9 ms    | 38.0 ms: 1.81x slower |
| genshi_text     | 12.3 ms    | 23.9 ms: 1.94x slower |
| mako            | 5.80 ms    | 12.1 ms: 2.08x slower |
| Geometric mean  | (ref)      | 1.88x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | Ex                     |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 40.6 ms    | 21.5 ms: 1.89x faster  |
| many_optionals             | 659 us     | 559 us: 1.18x faster   |
| regex_dna                  | 121 ms     | 123 ms: 1.02x slower   |
| pidigits                   | 145 ms     | 156 ms: 1.08x slower   |
| asyncio_websockets         | 304 ms     | 330 ms: 1.08x slower   |
| create_gc_cycles           | 1.26 ms    | 1.42 ms: 1.12x slower  |
| python_startup_no_site     | 18.7 ms    | 22.0 ms: 1.18x slower  |
| python_startup             | 24.7 ms    | 29.5 ms: 1.19x slower  |
| connected_components       | 320 ms     | 395 ms: 1.23x slower   |
| sqlite_synth               | 1.56 us    | 1.96 us: 1.26x slower  |
| regex_v8                   | 13.9 ms    | 17.5 ms: 1.26x slower  |
| xml_etree_parse            | 89.4 ms    | 112 ms: 1.26x slower   |
| shortest_path              | 347 ms     | 437 ms: 1.26x slower   |
| regex_effbot               | 1.45 ms    | 1.87 ms: 1.28x slower  |
| k_core                     | 1.67 sec   | 2.18 sec: 1.31x slower |
| dulwich_log                | 39.1 ms    | 52.4 ms: 1.34x slower  |
| mdp                        | 1.41 sec   | 1.89 sec: 1.34x slower |
| async_tree_cpu_io_mixed_tg | 325 ms     | 444 ms: 1.37x slower   |
| coverage                   | 46.2 ms    | 63.7 ms: 1.38x slower  |
| json                       | 2.95 ms    | 4.07 ms: 1.38x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 455 ms: 1.39x slower   |
| pylint                     | 193 ms     | 269 ms: 1.40x slower   |
| docutils                   | 1.58 sec   | 2.31 sec: 1.46x slower |
| telco                      | 4.45 ms    | 6.56 ms: 1.48x slower  |
| html5lib                   | 35.5 ms    | 52.5 ms: 1.48x slower  |
| meteor_contest             | 66.6 ms    | 99.5 ms: 1.49x slower  |
| 2to3                       | 204 ms     | 309 ms: 1.51x slower   |
| async_tree_memoization_tg  | 201 ms     | 304 ms: 1.52x slower   |
| sphinx                     | 615 ms     | 933 ms: 1.52x slower   |
| json_dumps                 | 6.19 ms    | 9.44 ms: 1.52x slower  |
| sympy_sum                  | 80.7 ms    | 123 ms: 1.53x slower   |
| sympy_integrate            | 12.0 ms    | 18.4 ms: 1.54x slower  |
| thrift                     | 461 us     | 710 us: 1.54x slower   |
| gc_traversal               | 2.09 ms    | 3.25 ms: 1.55x slower  |
| json_loads                 | 14.8 us    | 23.3 us: 1.58x slower  |
| pycparser                  | 642 ms     | 1.01 sec: 1.58x slower |
| xml_etree_iterparse        | 59.5 ms    | 94.3 ms: 1.58x slower  |
| pathlib                    | 23.6 ms    | 37.5 ms: 1.59x slower  |
| sympy_expand               | 263 ms     | 419 ms: 1.59x slower   |
| async_tree_memoization     | 196 ms     | 313 ms: 1.59x slower   |
| async_tree_io              | 353 ms     | 570 ms: 1.61x slower   |
| sympy_str                  | 153 ms     | 247 ms: 1.61x slower   |
| async_tree_io_tg           | 356 ms     | 576 ms: 1.62x slower   |
| async_tree_none_tg         | 150 ms     | 243 ms: 1.62x slower   |
| logging_format             | 5.90 us    | 9.92 us: 1.68x slower  |
| async_tree_none            | 157 ms     | 267 ms: 1.70x slower   |
| genshi_xml                 | 29.5 ms    | 50.4 ms: 1.71x slower  |
| typing_runtime_protocols   | 89.7 us    | 154 us: 1.72x slower   |
| logging_simple             | 5.42 us    | 9.30 us: 1.72x slower  |
| sqlglot_v2_optimize        | 30.5 ms    | 52.8 ms: 1.73x slower  |
| sqlglot_v2_normalize       | 62.6 ms    | 109 ms: 1.74x slower   |
| async_generators           | 199 ms     | 348 ms: 1.75x slower   |
| bpe_tokeniser              | 2.52 sec   | 4.45 sec: 1.76x slower |
| django_template            | 20.9 ms    | 38.0 ms: 1.81x slower  |
| regex_compile              | 70.7 ms    | 130 ms: 1.84x slower   |
| xml_etree_generate         | 49.4 ms    | 92.6 ms: 1.87x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.69 ms: 1.89x slower  |
| deepcopy_reduce            | 1.51 us    | 2.86 us: 1.89x slower  |
| deepcopy                   | 147 us     | 278 us: 1.90x slower   |
| pprint_safe_repr           | 429 ms     | 825 ms: 1.92x slower   |
| genshi_text                | 12.3 ms    | 23.9 ms: 1.94x slower  |
| pprint_pformat             | 853 ms     | 1.66 sec: 1.95x slower |
| nqueens                    | 49.7 ms    | 96.9 ms: 1.95x slower  |
| scimark_fft                | 140 ms     | 276 ms: 1.97x slower   |
| xml_etree_process          | 33.8 ms    | 66.9 ms: 1.98x slower  |
| crypto_pyaes               | 40.4 ms    | 80.1 ms: 1.98x slower  |
| pickle_pure_python         | 184 us     | 364 us: 1.98x slower   |
| tomli_loads                | 1.03 sec   | 2.07 sec: 2.01x slower |
| pyflate                    | 236 ms     | 477 ms: 2.02x slower   |
| sqlglot_v2_parse           | 695 us     | 1.41 ms: 2.02x slower  |
| fannkuch                   | 203 ms     | 418 ms: 2.06x slower   |
| coroutines                 | 10.8 ms    | 22.4 ms: 2.08x slower  |
| mako                       | 5.80 ms    | 12.1 ms: 2.08x slower  |
| float                      | 37.1 ms    | 78.0 ms: 2.10x slower  |
| raytrace                   | 145 ms     | 313 ms: 2.16x slower   |
| scimark_sparse_mat_mult    | 2.02 ms    | 4.43 ms: 2.19x slower  |
| chaos                      | 31.3 ms    | 69.3 ms: 2.22x slower  |
| nbody                      | 45.7 ms    | 103 ms: 2.26x slower   |
| richards_super             | 29.4 ms    | 67.7 ms: 2.30x slower  |
| go                         | 61.0 ms    | 140 ms: 2.30x slower   |
| richards                   | 25.5 ms    | 59.0 ms: 2.32x slower  |
| deepcopy_memo              | 14.7 us    | 34.0 us: 2.32x slower  |
| comprehensions             | 8.65 us    | 20.1 us: 2.32x slower  |
| scimark_monte_carlo        | 31.5 ms    | 75.8 ms: 2.41x slower  |
| spectral_norm              | 40.9 ms    | 102 ms: 2.49x slower   |
| hexiom                     | 3.00 ms    | 7.44 ms: 2.49x slower  |
| generators                 | 14.2 ms    | 35.6 ms: 2.50x slower  |
| deltablue                  | 1.64 ms    | 4.22 ms: 2.57x slower  |
| unpickle_pure_python       | 110 us     | 284 us: 2.59x slower   |
| scimark_lu                 | 44.3 ms    | 119 ms: 2.69x slower   |
| scimark_sor                | 51.1 ms    | 139 ms: 2.71x slower   |
| logging_silent             | 44.1 ns    | 124 ns: 2.82x slower   |
| Geometric mean             | (ref)      | 1.69x slower           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.404x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.58x
- 95% likely to have a slowdown of 1.56x
- 99% likely to have a slowdown of 1.53x

# Memory
- memory change: unknown