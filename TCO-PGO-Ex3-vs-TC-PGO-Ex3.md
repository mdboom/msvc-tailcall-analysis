# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.513x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 212 ms: 1.19x faster   |
| docutils       | 2.61 sec   | 1.67 sec: 1.56x faster |
| html5lib       | 57.3 ms    | 37.9 ms: 1.51x faster  |
| sphinx         | 1.00 sec   | 645 ms: 1.55x faster   |
| Geometric mean | (ref)      | 1.45x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------------------|:----------:|:---------------------:|
| coroutines                 | 22.1 ms    | 11.9 ms: 1.85x faster |
| asyncio_websockets         | 551 ms     | 301 ms: 1.83x faster  |
| async_generators           | 368 ms     | 202 ms: 1.82x faster  |
| async_tree_io_tg           | 606 ms     | 377 ms: 1.61x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 330 ms: 1.56x faster  |
| async_tree_io              | 596 ms     | 384 ms: 1.55x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 329 ms: 1.53x faster  |
| async_tree_none_tg         | 242 ms     | 159 ms: 1.52x faster  |
| async_tree_memoization     | 306 ms     | 206 ms: 1.49x faster  |
| async_tree_memoization_tg  | 307 ms     | 208 ms: 1.47x faster  |
| async_tree_none            | 249 ms     | 170 ms: 1.47x faster  |
| Geometric mean             | (ref)      | 1.60x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| float          | 66.8 ms    | 41.9 ms: 1.59x faster |
| nbody          | 86.4 ms    | 55.2 ms: 1.57x faster |
| pidigits       | 219 ms     | 145 ms: 1.51x faster  |
| Geometric mean | (ref)      | 1.56x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.46 ms: 2.24x faster |
| regex_v8       | 23.8 ms    | 13.2 ms: 1.80x faster |
| regex_dna      | 196 ms     | 120 ms: 1.63x faster  |
| regex_compile  | 125 ms     | 78.1 ms: 1.60x faster |
| Geometric mean | (ref)      | 1.80x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------------|:----------:|:----------------------:|
| json_loads           | 28.9 us    | 14.7 us: 1.96x faster  |
| json_dumps           | 12.5 ms    | 6.55 ms: 1.90x faster  |
| xml_etree_parse      | 163 ms     | 89.3 ms: 1.82x faster  |
| unpickle_pure_python | 217 us     | 127 us: 1.71x faster   |
| xml_etree_iterparse  | 103 ms     | 61.2 ms: 1.68x faster  |
| xml_etree_generate   | 86.8 ms    | 53.6 ms: 1.62x faster  |
| tomli_loads          | 1.88 sec   | 1.18 sec: 1.60x faster |
| xml_etree_process    | 58.7 ms    | 37.0 ms: 1.59x faster  |
| pickle_pure_python   | 306 us     | 199 us: 1.54x faster   |
| Geometric mean       | (ref)      | 1.71x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 24.7 ms: 1.94x slower |
| python_startup_no_site | 7.02 ms    | 18.7 ms: 2.67x slower |
| Geometric mean         | (ref)      | 2.28x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 6.28 ms: 1.85x faster |
| genshi_text     | 21.2 ms    | 14.3 ms: 1.49x faster |
| genshi_xml      | 48.1 ms    | 32.8 ms: 1.47x faster |
| django_template | 30.6 ms    | 22.9 ms: 1.34x faster |
| Geometric mean  | (ref)      | 1.52x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------------------|:----------:|:----------------------:|
| gc_traversal               | 4.97 ms    | 2.11 ms: 2.36x faster  |
| regex_effbot               | 3.28 ms    | 1.46 ms: 2.24x faster  |
| scimark_lu                 | 107 ms     | 50.9 ms: 2.10x faster  |
| create_gc_cycles           | 2.54 ms    | 1.27 ms: 1.99x faster  |
| json_loads                 | 28.9 us    | 14.7 us: 1.96x faster  |
| json_dumps                 | 12.5 ms    | 6.55 ms: 1.90x faster  |
| scimark_fft                | 289 ms     | 154 ms: 1.88x faster   |
| coroutines                 | 22.1 ms    | 11.9 ms: 1.85x faster  |
| mako                       | 11.6 ms    | 6.28 ms: 1.85x faster  |
| asyncio_websockets         | 551 ms     | 301 ms: 1.83x faster   |
| scimark_sparse_mat_mult    | 4.14 ms    | 2.27 ms: 1.83x faster  |
| xml_etree_parse            | 163 ms     | 89.3 ms: 1.82x faster  |
| async_generators           | 368 ms     | 202 ms: 1.82x faster   |
| regex_v8                   | 23.8 ms    | 13.2 ms: 1.80x faster  |
| json                       | 5.28 ms    | 2.97 ms: 1.78x faster  |
| deepcopy_memo              | 29.4 us    | 16.6 us: 1.77x faster  |
| fannkuch                   | 393 ms     | 223 ms: 1.77x faster   |
| logging_silent             | 87.1 ns    | 49.4 ns: 1.76x faster  |
| scimark_sor                | 107 ms     | 61.1 ms: 1.74x faster  |
| generators                 | 28.6 ms    | 16.5 ms: 1.73x faster  |
| unpickle_pure_python       | 217 us     | 127 us: 1.71x faster   |
| sqlite_synth               | 2.66 us    | 1.56 us: 1.70x faster  |
| pycparser                  | 1.16 sec   | 686 ms: 1.68x faster   |
| richards_super             | 55.6 ms    | 33.1 ms: 1.68x faster  |
| xml_etree_iterparse        | 103 ms     | 61.2 ms: 1.68x faster  |
| scimark_monte_carlo        | 60.1 ms    | 36.0 ms: 1.67x faster  |
| spectral_norm              | 82.5 ms    | 49.4 ms: 1.67x faster  |
| sympy_sum                  | 143 ms     | 86.3 ms: 1.65x faster  |
| coverage                   | 79.6 ms    | 48.2 ms: 1.65x faster  |
| richards                   | 47.4 ms    | 28.7 ms: 1.65x faster  |
| mdp                        | 2.65 sec   | 1.62 sec: 1.63x faster |
| regex_dna                  | 196 ms     | 120 ms: 1.63x faster   |
| hexiom                     | 5.74 ms    | 3.54 ms: 1.62x faster  |
| xml_etree_generate         | 86.8 ms    | 53.6 ms: 1.62x faster  |
| telco                      | 7.39 ms    | 4.57 ms: 1.62x faster  |
| bpe_tokeniser              | 4.39 sec   | 2.72 sec: 1.61x faster |
| async_tree_io_tg           | 606 ms     | 377 ms: 1.61x faster   |
| deltablue                  | 3.01 ms    | 1.88 ms: 1.60x faster  |
| tomli_loads                | 1.88 sec   | 1.18 sec: 1.60x faster |
| regex_compile              | 125 ms     | 78.1 ms: 1.60x faster  |
| float                      | 66.8 ms    | 41.9 ms: 1.59x faster  |
| go                         | 113 ms     | 70.9 ms: 1.59x faster  |
| raytrace                   | 255 ms     | 160 ms: 1.59x faster   |
| xml_etree_process          | 58.7 ms    | 37.0 ms: 1.59x faster  |
| sqlglot_v2_optimize        | 52.2 ms    | 33.0 ms: 1.58x faster  |
| meteor_contest             | 111 ms     | 70.2 ms: 1.58x faster  |
| comprehensions             | 15.5 us    | 9.87 us: 1.57x faster  |
| sympy_str                  | 258 ms     | 164 ms: 1.57x faster   |
| nbody                      | 86.4 ms    | 55.2 ms: 1.57x faster  |
| pprint_safe_repr           | 736 ms     | 470 ms: 1.56x faster   |
| docutils                   | 2.61 sec   | 1.67 sec: 1.56x faster |
| async_tree_cpu_io_mixed    | 517 ms     | 330 ms: 1.56x faster   |
| sqlglot_v2_parse           | 1.20 ms    | 766 us: 1.56x faster   |
| sympy_expand               | 440 ms     | 282 ms: 1.56x faster   |
| pprint_pformat             | 1.51 sec   | 967 ms: 1.56x faster   |
| sphinx                     | 1.00 sec   | 645 ms: 1.55x faster   |
| async_tree_io              | 596 ms     | 384 ms: 1.55x faster   |
| sqlglot_v2_transpile       | 1.50 ms    | 970 us: 1.54x faster   |
| dulwich_log                | 61.8 ms    | 40.2 ms: 1.54x faster  |
| pickle_pure_python         | 306 us     | 199 us: 1.54x faster   |
| async_tree_cpu_io_mixed_tg | 504 ms     | 329 ms: 1.53x faster   |
| crypto_pyaes               | 72.5 ms    | 47.4 ms: 1.53x faster  |
| thrift                     | 737 us     | 482 us: 1.53x faster   |
| pyflate                    | 410 ms     | 268 ms: 1.53x faster   |
| async_tree_none_tg         | 242 ms     | 159 ms: 1.52x faster   |
| pidigits                   | 219 ms     | 145 ms: 1.51x faster   |
| html5lib                   | 57.3 ms    | 37.9 ms: 1.51x faster  |
| sqlglot_v2_normalize       | 104 ms     | 69.3 ms: 1.51x faster  |
| typing_runtime_protocols   | 148 us     | 98.8 us: 1.49x faster  |
| deepcopy_reduce            | 2.53 us    | 1.70 us: 1.49x faster  |
| async_tree_memoization     | 306 ms     | 206 ms: 1.49x faster   |
| genshi_text                | 21.2 ms    | 14.3 ms: 1.49x faster  |
| async_tree_memoization_tg  | 307 ms     | 208 ms: 1.47x faster   |
| sympy_integrate            | 18.9 ms    | 12.8 ms: 1.47x faster  |
| genshi_xml                 | 48.1 ms    | 32.8 ms: 1.47x faster  |
| async_tree_none            | 249 ms     | 170 ms: 1.47x faster   |
| deepcopy                   | 244 us     | 167 us: 1.46x faster   |
| chaos                      | 53.3 ms    | 36.9 ms: 1.45x faster  |
| many_optionals             | 924 us     | 665 us: 1.39x faster   |
| nqueens                    | 75.4 ms    | 54.4 ms: 1.39x faster  |
| pylint                     | 275 ms     | 198 ms: 1.39x faster   |
| connected_components       | 445 ms     | 326 ms: 1.37x faster   |
| shortest_path              | 480 ms     | 353 ms: 1.36x faster   |
| django_template            | 30.6 ms    | 22.9 ms: 1.34x faster  |
| k_core                     | 2.27 sec   | 1.71 sec: 1.33x faster |
| 2to3                       | 251 ms     | 212 ms: 1.19x faster   |
| logging_format             | 5.86 us    | 6.50 us: 1.11x slower  |
| logging_simple             | 5.26 us    | 5.97 us: 1.14x slower  |
| pathlib                    | 14.9 ms    | 24.1 ms: 1.62x slower  |
| python_startup             | 12.7 ms    | 24.7 ms: 1.94x slower  |
| subparsers                 | 20.2 ms    | 40.7 ms: 2.02x slower  |
| python_startup_no_site     | 7.02 ms    | 18.7 ms: 2.67x slower  |
| Geometric mean             | (ref)      | 1.51x faster           |
Ignored benchmarks (4) of TC-PGO-Ex3.json: bench_mp_pool, bench_thread_pool, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.513x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.55x
- 95% likely to have a speedup of 1.54x
- 99% likely to have a speedup of 1.53x

# Memory
- memory change: unknown