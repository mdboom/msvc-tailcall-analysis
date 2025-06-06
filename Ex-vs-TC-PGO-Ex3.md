# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.030x slower
- HPT reliability: 71.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | Ex                     |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 309 ms: 1.23x slower   |
| docutils       | 2.61 sec   | 2.31 sec: 1.13x faster |
| html5lib       | 57.3 ms    | 52.5 ms: 1.09x faster  |
| sphinx         | 1.00 sec   | 933 ms: 1.08x faster   |
| Geometric mean | (ref)      | 1.02x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | Ex                    |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 551 ms     | 330 ms: 1.67x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 444 ms: 1.14x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 455 ms: 1.14x faster  |
| async_generators           | 368 ms     | 348 ms: 1.06x faster  |
| async_tree_io_tg           | 606 ms     | 576 ms: 1.05x faster  |
| async_tree_io              | 596 ms     | 570 ms: 1.05x faster  |
| coroutines                 | 22.1 ms    | 22.4 ms: 1.02x slower |
| async_tree_memoization     | 306 ms     | 313 ms: 1.02x slower  |
| async_tree_none            | 249 ms     | 267 ms: 1.07x slower  |
| Geometric mean             | (ref)      | 1.08x faster          |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | Ex                    |
|----------------|:----------:|:---------------------:|
| pidigits       | 219 ms     | 156 ms: 1.40x faster  |
| float          | 66.8 ms    | 78.0 ms: 1.17x slower |
| nbody          | 86.4 ms    | 103 ms: 1.20x slower  |
| Geometric mean | (ref)      | 1.00x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | Ex                    |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.87 ms: 1.76x faster |
| regex_dna      | 196 ms     | 123 ms: 1.59x faster  |
| regex_v8       | 23.8 ms    | 17.5 ms: 1.36x faster |
| regex_compile  | 125 ms     | 130 ms: 1.04x slower  |
| Geometric mean | (ref)      | 1.38x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | Ex                     |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 163 ms     | 112 ms: 1.45x faster   |
| json_dumps           | 12.5 ms    | 9.44 ms: 1.32x faster  |
| json_loads           | 28.9 us    | 23.3 us: 1.24x faster  |
| xml_etree_iterparse  | 103 ms     | 94.3 ms: 1.09x faster  |
| xml_etree_generate   | 86.8 ms    | 92.6 ms: 1.07x slower  |
| tomli_loads          | 1.88 sec   | 2.07 sec: 1.10x slower |
| xml_etree_process    | 58.7 ms    | 66.9 ms: 1.14x slower  |
| pickle_pure_python   | 306 us     | 364 us: 1.19x slower   |
| unpickle_pure_python | 217 us     | 284 us: 1.31x slower   |
| Geometric mean       | (ref)      | 1.02x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | Ex                    |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 29.5 ms: 2.32x slower |
| python_startup_no_site | 7.02 ms    | 22.0 ms: 3.14x slower |
| Geometric mean         | (ref)      | 2.70x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | Ex                    |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 12.1 ms: 1.04x slower |
| genshi_xml      | 48.1 ms    | 50.4 ms: 1.05x slower |
| genshi_text     | 21.2 ms    | 23.9 ms: 1.13x slower |
| django_template | 30.6 ms    | 38.0 ms: 1.24x slower |
| Geometric mean  | (ref)      | 1.11x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | Ex                     |
|----------------------------|:----------:|:----------------------:|
| create_gc_cycles           | 2.54 ms    | 1.42 ms: 1.79x faster  |
| regex_effbot               | 3.28 ms    | 1.87 ms: 1.76x faster  |
| asyncio_websockets         | 551 ms     | 330 ms: 1.67x faster   |
| many_optionals             | 924 us     | 559 us: 1.65x faster   |
| regex_dna                  | 196 ms     | 123 ms: 1.59x faster   |
| gc_traversal               | 4.97 ms    | 3.25 ms: 1.53x faster  |
| xml_etree_parse            | 163 ms     | 112 ms: 1.45x faster   |
| pidigits                   | 219 ms     | 156 ms: 1.40x faster   |
| mdp                        | 2.65 sec   | 1.89 sec: 1.40x faster |
| regex_v8                   | 23.8 ms    | 17.5 ms: 1.36x faster  |
| sqlite_synth               | 2.66 us    | 1.96 us: 1.36x faster  |
| json_dumps                 | 12.5 ms    | 9.44 ms: 1.32x faster  |
| json                       | 5.28 ms    | 4.07 ms: 1.30x faster  |
| coverage                   | 79.6 ms    | 63.7 ms: 1.25x faster  |
| json_loads                 | 28.9 us    | 23.3 us: 1.24x faster  |
| dulwich_log                | 61.8 ms    | 52.4 ms: 1.18x faster  |
| sympy_sum                  | 143 ms     | 123 ms: 1.16x faster   |
| pycparser                  | 1.16 sec   | 1.01 sec: 1.14x faster |
| async_tree_cpu_io_mixed_tg | 504 ms     | 444 ms: 1.14x faster   |
| async_tree_cpu_io_mixed    | 517 ms     | 455 ms: 1.14x faster   |
| docutils                   | 2.61 sec   | 2.31 sec: 1.13x faster |
| connected_components       | 445 ms     | 395 ms: 1.13x faster   |
| telco                      | 7.39 ms    | 6.56 ms: 1.13x faster  |
| meteor_contest             | 111 ms     | 99.5 ms: 1.11x faster  |
| shortest_path              | 480 ms     | 437 ms: 1.10x faster   |
| html5lib                   | 57.3 ms    | 52.5 ms: 1.09x faster  |
| xml_etree_iterparse        | 103 ms     | 94.3 ms: 1.09x faster  |
| sphinx                     | 1.00 sec   | 933 ms: 1.08x faster   |
| async_generators           | 368 ms     | 348 ms: 1.06x faster   |
| async_tree_io_tg           | 606 ms     | 576 ms: 1.05x faster   |
| sympy_expand               | 440 ms     | 419 ms: 1.05x faster   |
| scimark_fft                | 289 ms     | 276 ms: 1.05x faster   |
| async_tree_io              | 596 ms     | 570 ms: 1.05x faster   |
| sympy_str                  | 258 ms     | 247 ms: 1.04x faster   |
| k_core                     | 2.27 sec   | 2.18 sec: 1.04x faster |
| thrift                     | 737 us     | 710 us: 1.04x faster   |
| sympy_integrate            | 18.9 ms    | 18.4 ms: 1.03x faster  |
| sqlglot_v2_optimize        | 52.2 ms    | 52.8 ms: 1.01x slower  |
| bpe_tokeniser              | 4.39 sec   | 4.45 sec: 1.01x slower |
| coroutines                 | 22.1 ms    | 22.4 ms: 1.02x slower  |
| async_tree_memoization     | 306 ms     | 313 ms: 1.02x slower   |
| regex_compile              | 125 ms     | 130 ms: 1.04x slower   |
| mako                       | 11.6 ms    | 12.1 ms: 1.04x slower  |
| typing_runtime_protocols   | 148 us     | 154 us: 1.04x slower   |
| sqlglot_v2_normalize       | 104 ms     | 109 ms: 1.04x slower   |
| genshi_xml                 | 48.1 ms    | 50.4 ms: 1.05x slower  |
| fannkuch                   | 393 ms     | 418 ms: 1.06x slower   |
| xml_etree_generate         | 86.8 ms    | 92.6 ms: 1.07x slower  |
| subparsers                 | 20.2 ms    | 21.5 ms: 1.07x slower  |
| scimark_sparse_mat_mult    | 4.14 ms    | 4.43 ms: 1.07x slower  |
| async_tree_none            | 249 ms     | 267 ms: 1.07x slower   |
| pprint_pformat             | 1.51 sec   | 1.66 sec: 1.10x slower |
| tomli_loads                | 1.88 sec   | 2.07 sec: 1.10x slower |
| crypto_pyaes               | 72.5 ms    | 80.1 ms: 1.10x slower  |
| scimark_lu                 | 107 ms     | 119 ms: 1.12x slower   |
| pprint_safe_repr           | 736 ms     | 825 ms: 1.12x slower   |
| sqlglot_v2_transpile       | 1.50 ms    | 1.69 ms: 1.13x slower  |
| genshi_text                | 21.2 ms    | 23.9 ms: 1.13x slower  |
| deepcopy_reduce            | 2.53 us    | 2.86 us: 1.13x slower  |
| xml_etree_process          | 58.7 ms    | 66.9 ms: 1.14x slower  |
| deepcopy                   | 244 us     | 278 us: 1.14x slower   |
| deepcopy_memo              | 29.4 us    | 34.0 us: 1.16x slower  |
| pyflate                    | 410 ms     | 477 ms: 1.17x slower   |
| float                      | 66.8 ms    | 78.0 ms: 1.17x slower  |
| sqlglot_v2_parse           | 1.20 ms    | 1.41 ms: 1.18x slower  |
| pickle_pure_python         | 306 us     | 364 us: 1.19x slower   |
| nbody                      | 86.4 ms    | 103 ms: 1.20x slower   |
| richards_super             | 55.6 ms    | 67.7 ms: 1.22x slower  |
| raytrace                   | 255 ms     | 313 ms: 1.23x slower   |
| 2to3                       | 251 ms     | 309 ms: 1.23x slower   |
| spectral_norm              | 82.5 ms    | 102 ms: 1.23x slower   |
| django_template            | 30.6 ms    | 38.0 ms: 1.24x slower  |
| generators                 | 28.6 ms    | 35.6 ms: 1.24x slower  |
| richards                   | 47.4 ms    | 59.0 ms: 1.25x slower  |
| go                         | 113 ms     | 140 ms: 1.25x slower   |
| bench_mp_pool              | 80.9 ms    | 101 ms: 1.25x slower   |
| scimark_monte_carlo        | 60.1 ms    | 75.8 ms: 1.26x slower  |
| nqueens                    | 75.4 ms    | 96.9 ms: 1.28x slower  |
| comprehensions             | 15.5 us    | 20.1 us: 1.29x slower  |
| hexiom                     | 5.74 ms    | 7.44 ms: 1.30x slower  |
| chaos                      | 53.3 ms    | 69.3 ms: 1.30x slower  |
| scimark_sor                | 107 ms     | 139 ms: 1.30x slower   |
| unpickle_pure_python       | 217 us     | 284 us: 1.31x slower   |
| deltablue                  | 3.01 ms    | 4.22 ms: 1.40x slower  |
| logging_silent             | 87.1 ns    | 124 ns: 1.43x slower   |
| bench_thread_pool          | 831 us     | 1.28 ms: 1.53x slower  |
| logging_format             | 5.86 us    | 9.92 us: 1.69x slower  |
| logging_simple             | 5.26 us    | 9.30 us: 1.77x slower  |
| python_startup             | 12.7 ms    | 29.5 ms: 2.32x slower  |
| pathlib                    | 14.9 ms    | 37.5 ms: 2.52x slower  |
| python_startup_no_site     | 7.02 ms    | 22.0 ms: 3.14x slower  |
| Geometric mean             | (ref)      | 1.04x slower           |

Benchmark hidden because not significant (3): pylint, async_tree_memoization_tg, async_tree_none_tg
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 71.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown