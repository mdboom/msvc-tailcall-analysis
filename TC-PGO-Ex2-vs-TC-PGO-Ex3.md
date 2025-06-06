# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.526x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.55x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2             |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 216 ms: 1.16x faster   |
| docutils       | 2.61 sec   | 1.63 sec: 1.60x faster |
| html5lib       | 57.3 ms    | 36.1 ms: 1.59x faster  |
| sphinx         | 1.00 sec   | 638 ms: 1.57x faster   |
| Geometric mean | (ref)      | 1.47x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TC-PGO-Ex2            |
|----------------------------|:----------:|:---------------------:|
| async_generators           | 368 ms     | 206 ms: 1.79x faster  |
| coroutines                 | 22.1 ms    | 12.4 ms: 1.77x faster |
| asyncio_websockets         | 551 ms     | 317 ms: 1.74x faster  |
| async_tree_io_tg           | 606 ms     | 371 ms: 1.63x faster  |
| async_tree_io              | 596 ms     | 375 ms: 1.59x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 329 ms: 1.57x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 328 ms: 1.54x faster  |
| async_tree_none_tg         | 242 ms     | 159 ms: 1.52x faster  |
| async_tree_memoization     | 306 ms     | 205 ms: 1.50x faster  |
| async_tree_memoization_tg  | 307 ms     | 209 ms: 1.47x faster  |
| async_tree_none            | 249 ms     | 170 ms: 1.47x faster  |
| Geometric mean             | (ref)      | 1.59x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:----------:|:---------------------:|
| float          | 66.8 ms    | 40.2 ms: 1.66x faster |
| nbody          | 86.4 ms    | 53.3 ms: 1.62x faster |
| pidigits       | 219 ms     | 146 ms: 1.50x faster  |
| Geometric mean | (ref)      | 1.59x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.40 ms: 2.35x faster |
| regex_dna      | 196 ms     | 115 ms: 1.70x faster  |
| regex_v8       | 23.8 ms    | 14.1 ms: 1.69x faster |
| regex_compile  | 125 ms     | 74.8 ms: 1.67x faster |
| Geometric mean | (ref)      | 1.83x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TC-PGO-Ex2             |
|----------------------|:----------:|:----------------------:|
| json_loads           | 28.9 us    | 14.5 us: 2.00x faster  |
| json_dumps           | 12.5 ms    | 6.48 ms: 1.92x faster  |
| xml_etree_parse      | 163 ms     | 89.0 ms: 1.83x faster  |
| unpickle_pure_python | 217 us     | 123 us: 1.77x faster   |
| xml_etree_iterparse  | 103 ms     | 60.4 ms: 1.70x faster  |
| xml_etree_generate   | 86.8 ms    | 51.5 ms: 1.69x faster  |
| xml_etree_process    | 58.7 ms    | 36.7 ms: 1.60x faster  |
| tomli_loads          | 1.88 sec   | 1.17 sec: 1.60x faster |
| pickle_pure_python   | 306 us     | 201 us: 1.52x faster   |
| Geometric mean       | (ref)      | 1.73x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TC-PGO-Ex2            |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 26.0 ms: 2.04x slower |
| python_startup_no_site | 7.02 ms    | 19.6 ms: 2.79x slower |
| Geometric mean         | (ref)      | 2.39x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TC-PGO-Ex2            |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 6.12 ms: 1.89x faster |
| genshi_xml      | 48.1 ms    | 30.7 ms: 1.57x faster |
| genshi_text     | 21.2 ms    | 14.2 ms: 1.49x faster |
| django_template | 30.6 ms    | 23.4 ms: 1.31x faster |
| Geometric mean  | (ref)      | 1.55x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TC-PGO-Ex2             |
|----------------------------|:----------:|:----------------------:|
| gc_traversal               | 4.97 ms    | 2.07 ms: 2.40x faster  |
| regex_effbot               | 3.28 ms    | 1.40 ms: 2.35x faster  |
| create_gc_cycles           | 2.54 ms    | 1.27 ms: 2.00x faster  |
| json_loads                 | 28.9 us    | 14.5 us: 2.00x faster  |
| scimark_lu                 | 107 ms     | 54.4 ms: 1.96x faster  |
| generators                 | 28.6 ms    | 14.8 ms: 1.93x faster  |
| json_dumps                 | 12.5 ms    | 6.48 ms: 1.92x faster  |
| scimark_fft                | 289 ms     | 152 ms: 1.90x faster   |
| mdp                        | 2.65 sec   | 1.40 sec: 1.89x faster |
| mako                       | 11.6 ms    | 6.12 ms: 1.89x faster  |
| scimark_sparse_mat_mult    | 4.14 ms    | 2.26 ms: 1.83x faster  |
| xml_etree_parse            | 163 ms     | 89.0 ms: 1.83x faster  |
| async_generators           | 368 ms     | 206 ms: 1.79x faster   |
| coroutines                 | 22.1 ms    | 12.4 ms: 1.77x faster  |
| json                       | 5.28 ms    | 2.98 ms: 1.77x faster  |
| unpickle_pure_python       | 217 us     | 123 us: 1.77x faster   |
| crypto_pyaes               | 72.5 ms    | 41.6 ms: 1.74x faster  |
| asyncio_websockets         | 551 ms     | 317 ms: 1.74x faster   |
| pycparser                  | 1.16 sec   | 664 ms: 1.74x faster   |
| sympy_sum                  | 143 ms     | 82.1 ms: 1.74x faster  |
| richards_super             | 55.6 ms    | 32.2 ms: 1.73x faster  |
| deepcopy_memo              | 29.4 us    | 17.0 us: 1.73x faster  |
| sqlite_synth               | 2.66 us    | 1.56 us: 1.71x faster  |
| richards                   | 47.4 ms    | 27.8 ms: 1.70x faster  |
| regex_dna                  | 196 ms     | 115 ms: 1.70x faster   |
| xml_etree_iterparse        | 103 ms     | 60.4 ms: 1.70x faster  |
| regex_v8                   | 23.8 ms    | 14.1 ms: 1.69x faster  |
| xml_etree_generate         | 86.8 ms    | 51.5 ms: 1.69x faster  |
| fannkuch                   | 393 ms     | 236 ms: 1.67x faster   |
| regex_compile              | 125 ms     | 74.8 ms: 1.67x faster  |
| float                      | 66.8 ms    | 40.2 ms: 1.66x faster  |
| hexiom                     | 5.74 ms    | 3.47 ms: 1.65x faster  |
| go                         | 113 ms     | 68.4 ms: 1.65x faster  |
| sympy_str                  | 258 ms     | 158 ms: 1.64x faster   |
| sympy_expand               | 440 ms     | 269 ms: 1.63x faster   |
| async_tree_io_tg           | 606 ms     | 371 ms: 1.63x faster   |
| logging_silent             | 87.1 ns    | 53.3 ns: 1.63x faster  |
| telco                      | 7.39 ms    | 4.54 ms: 1.63x faster  |
| deltablue                  | 3.01 ms    | 1.85 ms: 1.63x faster  |
| scimark_monte_carlo        | 60.1 ms    | 37.0 ms: 1.63x faster  |
| nbody                      | 86.4 ms    | 53.3 ms: 1.62x faster  |
| bpe_tokeniser              | 4.39 sec   | 2.71 sec: 1.62x faster |
| sqlglot_v2_optimize        | 52.2 ms    | 32.2 ms: 1.62x faster  |
| sqlglot_v2_parse           | 1.20 ms    | 740 us: 1.62x faster   |
| spectral_norm              | 82.5 ms    | 51.1 ms: 1.61x faster  |
| coverage                   | 79.6 ms    | 49.5 ms: 1.61x faster  |
| docutils                   | 2.61 sec   | 1.63 sec: 1.60x faster |
| sqlglot_v2_transpile       | 1.50 ms    | 933 us: 1.60x faster   |
| xml_etree_process          | 58.7 ms    | 36.7 ms: 1.60x faster  |
| tomli_loads                | 1.88 sec   | 1.17 sec: 1.60x faster |
| comprehensions             | 15.5 us    | 9.73 us: 1.60x faster  |
| meteor_contest             | 111 ms     | 69.5 ms: 1.59x faster  |
| async_tree_io              | 596 ms     | 375 ms: 1.59x faster   |
| html5lib                   | 57.3 ms    | 36.1 ms: 1.59x faster  |
| scimark_sor                | 107 ms     | 67.5 ms: 1.58x faster  |
| pyflate                    | 410 ms     | 260 ms: 1.58x faster   |
| sphinx                     | 1.00 sec   | 638 ms: 1.57x faster   |
| async_tree_cpu_io_mixed    | 517 ms     | 329 ms: 1.57x faster   |
| dulwich_log                | 61.8 ms    | 39.5 ms: 1.57x faster  |
| genshi_xml                 | 48.1 ms    | 30.7 ms: 1.57x faster  |
| sqlglot_v2_normalize       | 104 ms     | 66.9 ms: 1.56x faster  |
| pprint_pformat             | 1.51 sec   | 968 ms: 1.56x faster   |
| sympy_integrate            | 18.9 ms    | 12.2 ms: 1.55x faster  |
| pprint_safe_repr           | 736 ms     | 478 ms: 1.54x faster   |
| async_tree_cpu_io_mixed_tg | 504 ms     | 328 ms: 1.54x faster   |
| raytrace                   | 255 ms     | 166 ms: 1.54x faster   |
| thrift                     | 737 us     | 482 us: 1.53x faster   |
| deepcopy                   | 244 us     | 160 us: 1.53x faster   |
| deepcopy_reduce            | 2.53 us    | 1.66 us: 1.52x faster  |
| pickle_pure_python         | 306 us     | 201 us: 1.52x faster   |
| async_tree_none_tg         | 242 ms     | 159 ms: 1.52x faster   |
| pidigits                   | 219 ms     | 146 ms: 1.50x faster   |
| async_tree_memoization     | 306 ms     | 205 ms: 1.50x faster   |
| genshi_text                | 21.2 ms    | 14.2 ms: 1.49x faster  |
| typing_runtime_protocols   | 148 us     | 98.9 us: 1.49x faster  |
| chaos                      | 53.3 ms    | 35.9 ms: 1.49x faster  |
| async_tree_memoization_tg  | 307 ms     | 209 ms: 1.47x faster   |
| async_tree_none            | 249 ms     | 170 ms: 1.47x faster   |
| nqueens                    | 75.4 ms    | 54.0 ms: 1.40x faster  |
| connected_components       | 445 ms     | 321 ms: 1.39x faster   |
| pylint                     | 275 ms     | 199 ms: 1.39x faster   |
| shortest_path              | 480 ms     | 348 ms: 1.38x faster   |
| k_core                     | 2.27 sec   | 1.71 sec: 1.33x faster |
| django_template            | 30.6 ms    | 23.4 ms: 1.31x faster  |
| many_optionals             | 924 us     | 761 us: 1.21x faster   |
| 2to3                       | 251 ms     | 216 ms: 1.16x faster   |
| bench_thread_pool          | 831 us     | 851 us: 1.02x slower   |
| logging_format             | 5.86 us    | 6.34 us: 1.08x slower  |
| logging_simple             | 5.26 us    | 5.78 us: 1.10x slower  |
| bench_mp_pool              | 80.9 ms    | 89.1 ms: 1.10x slower  |
| pathlib                    | 14.9 ms    | 24.3 ms: 1.64x slower  |
| python_startup             | 12.7 ms    | 26.0 ms: 2.04x slower  |
| subparsers                 | 20.2 ms    | 44.9 ms: 2.23x slower  |
| python_startup_no_site     | 7.02 ms    | 19.6 ms: 2.79x slower  |
| Geometric mean             | (ref)      | 1.51x faster           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.526x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.57x
- 95% likely to have a speedup of 1.56x
- 99% likely to have a speedup of 1.55x

# Memory
- memory change: unknown