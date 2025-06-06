# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.344x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.55x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3             |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 251 ms: 1.16x slower   |
| docutils       | 1.63 sec   | 2.61 sec: 1.60x slower |
| html5lib       | 36.1 ms    | 57.3 ms: 1.59x slower  |
| sphinx         | 638 ms     | 1.00 sec: 1.57x slower |
| Geometric mean | (ref)      | 1.47x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | TC-PGO-Ex3            |
|----------------------------|:----------:|:---------------------:|
| async_tree_none            | 170 ms     | 249 ms: 1.47x slower  |
| async_tree_memoization_tg  | 209 ms     | 307 ms: 1.47x slower  |
| async_tree_memoization     | 205 ms     | 306 ms: 1.50x slower  |
| async_tree_none_tg         | 159 ms     | 242 ms: 1.52x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 504 ms: 1.54x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 517 ms: 1.57x slower  |
| async_tree_io              | 375 ms     | 596 ms: 1.59x slower  |
| async_tree_io_tg           | 371 ms     | 606 ms: 1.63x slower  |
| asyncio_websockets         | 317 ms     | 551 ms: 1.74x slower  |
| coroutines                 | 12.4 ms    | 22.1 ms: 1.77x slower |
| async_generators           | 206 ms     | 368 ms: 1.79x slower  |
| Geometric mean             | (ref)      | 1.59x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 219 ms: 1.50x slower  |
| nbody          | 53.3 ms    | 86.4 ms: 1.62x slower |
| float          | 40.2 ms    | 66.8 ms: 1.66x slower |
| Geometric mean | (ref)      | 1.59x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:----------:|:---------------------:|
| regex_compile  | 74.8 ms    | 125 ms: 1.67x slower  |
| regex_v8       | 14.1 ms    | 23.8 ms: 1.69x slower |
| regex_dna      | 115 ms     | 196 ms: 1.70x slower  |
| regex_effbot   | 1.40 ms    | 3.28 ms: 2.35x slower |
| Geometric mean | (ref)      | 1.83x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------|:----------:|:----------------------:|
| pickle_pure_python   | 201 us     | 306 us: 1.52x slower   |
| tomli_loads          | 1.17 sec   | 1.88 sec: 1.60x slower |
| xml_etree_process    | 36.7 ms    | 58.7 ms: 1.60x slower  |
| xml_etree_generate   | 51.5 ms    | 86.8 ms: 1.69x slower  |
| xml_etree_iterparse  | 60.4 ms    | 103 ms: 1.70x slower   |
| unpickle_pure_python | 123 us     | 217 us: 1.77x slower   |
| xml_etree_parse      | 89.0 ms    | 163 ms: 1.83x slower   |
| json_dumps           | 6.48 ms    | 12.5 ms: 1.92x slower  |
| json_loads           | 14.5 us    | 28.9 us: 2.00x slower  |
| Geometric mean       | (ref)      | 1.73x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TC-PGO-Ex3            |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 7.02 ms: 2.79x faster |
| python_startup         | 26.0 ms    | 12.7 ms: 2.04x faster |
| Geometric mean         | (ref)      | 2.39x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TC-PGO-Ex3            |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 30.6 ms: 1.31x slower |
| genshi_text     | 14.2 ms    | 21.2 ms: 1.49x slower |
| genshi_xml      | 30.7 ms    | 48.1 ms: 1.57x slower |
| mako            | 6.12 ms    | 11.6 ms: 1.89x slower |
| Geometric mean  | (ref)      | 1.55x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------------|:----------:|:----------------------:|
| python_startup_no_site     | 19.6 ms    | 7.02 ms: 2.79x faster  |
| subparsers                 | 44.9 ms    | 20.2 ms: 2.23x faster  |
| python_startup             | 26.0 ms    | 12.7 ms: 2.04x faster  |
| pathlib                    | 24.3 ms    | 14.9 ms: 1.64x faster  |
| bench_mp_pool              | 89.1 ms    | 80.9 ms: 1.10x faster  |
| logging_simple             | 5.78 us    | 5.26 us: 1.10x faster  |
| logging_format             | 6.34 us    | 5.86 us: 1.08x faster  |
| bench_thread_pool          | 851 us     | 831 us: 1.02x faster   |
| 2to3                       | 216 ms     | 251 ms: 1.16x slower   |
| many_optionals             | 761 us     | 924 us: 1.21x slower   |
| django_template            | 23.4 ms    | 30.6 ms: 1.31x slower  |
| k_core                     | 1.71 sec   | 2.27 sec: 1.33x slower |
| shortest_path              | 348 ms     | 480 ms: 1.38x slower   |
| pylint                     | 199 ms     | 275 ms: 1.39x slower   |
| connected_components       | 321 ms     | 445 ms: 1.39x slower   |
| nqueens                    | 54.0 ms    | 75.4 ms: 1.40x slower  |
| async_tree_none            | 170 ms     | 249 ms: 1.47x slower   |
| async_tree_memoization_tg  | 209 ms     | 307 ms: 1.47x slower   |
| chaos                      | 35.9 ms    | 53.3 ms: 1.49x slower  |
| typing_runtime_protocols   | 98.9 us    | 148 us: 1.49x slower   |
| genshi_text                | 14.2 ms    | 21.2 ms: 1.49x slower  |
| async_tree_memoization     | 205 ms     | 306 ms: 1.50x slower   |
| pidigits                   | 146 ms     | 219 ms: 1.50x slower   |
| async_tree_none_tg         | 159 ms     | 242 ms: 1.52x slower   |
| pickle_pure_python         | 201 us     | 306 us: 1.52x slower   |
| deepcopy_reduce            | 1.66 us    | 2.53 us: 1.52x slower  |
| deepcopy                   | 160 us     | 244 us: 1.53x slower   |
| thrift                     | 482 us     | 737 us: 1.53x slower   |
| raytrace                   | 166 ms     | 255 ms: 1.54x slower   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 504 ms: 1.54x slower   |
| pprint_safe_repr           | 478 ms     | 736 ms: 1.54x slower   |
| sympy_integrate            | 12.2 ms    | 18.9 ms: 1.55x slower  |
| pprint_pformat             | 968 ms     | 1.51 sec: 1.56x slower |
| sqlglot_v2_normalize       | 66.9 ms    | 104 ms: 1.56x slower   |
| genshi_xml                 | 30.7 ms    | 48.1 ms: 1.57x slower  |
| dulwich_log                | 39.5 ms    | 61.8 ms: 1.57x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 517 ms: 1.57x slower   |
| sphinx                     | 638 ms     | 1.00 sec: 1.57x slower |
| pyflate                    | 260 ms     | 410 ms: 1.58x slower   |
| scimark_sor                | 67.5 ms    | 107 ms: 1.58x slower   |
| html5lib                   | 36.1 ms    | 57.3 ms: 1.59x slower  |
| async_tree_io              | 375 ms     | 596 ms: 1.59x slower   |
| meteor_contest             | 69.5 ms    | 111 ms: 1.59x slower   |
| comprehensions             | 9.73 us    | 15.5 us: 1.60x slower  |
| tomli_loads                | 1.17 sec   | 1.88 sec: 1.60x slower |
| xml_etree_process          | 36.7 ms    | 58.7 ms: 1.60x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.50 ms: 1.60x slower  |
| docutils                   | 1.63 sec   | 2.61 sec: 1.60x slower |
| coverage                   | 49.5 ms    | 79.6 ms: 1.61x slower  |
| spectral_norm              | 51.1 ms    | 82.5 ms: 1.61x slower  |
| sqlglot_v2_parse           | 740 us     | 1.20 ms: 1.62x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 52.2 ms: 1.62x slower  |
| bpe_tokeniser              | 2.71 sec   | 4.39 sec: 1.62x slower |
| nbody                      | 53.3 ms    | 86.4 ms: 1.62x slower  |
| scimark_monte_carlo        | 37.0 ms    | 60.1 ms: 1.63x slower  |
| deltablue                  | 1.85 ms    | 3.01 ms: 1.63x slower  |
| telco                      | 4.54 ms    | 7.39 ms: 1.63x slower  |
| logging_silent             | 53.3 ns    | 87.1 ns: 1.63x slower  |
| async_tree_io_tg           | 371 ms     | 606 ms: 1.63x slower   |
| sympy_expand               | 269 ms     | 440 ms: 1.63x slower   |
| sympy_str                  | 158 ms     | 258 ms: 1.64x slower   |
| go                         | 68.4 ms    | 113 ms: 1.65x slower   |
| hexiom                     | 3.47 ms    | 5.74 ms: 1.65x slower  |
| float                      | 40.2 ms    | 66.8 ms: 1.66x slower  |
| regex_compile              | 74.8 ms    | 125 ms: 1.67x slower   |
| fannkuch                   | 236 ms     | 393 ms: 1.67x slower   |
| xml_etree_generate         | 51.5 ms    | 86.8 ms: 1.69x slower  |
| regex_v8                   | 14.1 ms    | 23.8 ms: 1.69x slower  |
| xml_etree_iterparse        | 60.4 ms    | 103 ms: 1.70x slower   |
| regex_dna                  | 115 ms     | 196 ms: 1.70x slower   |
| richards                   | 27.8 ms    | 47.4 ms: 1.70x slower  |
| sqlite_synth               | 1.56 us    | 2.66 us: 1.71x slower  |
| deepcopy_memo              | 17.0 us    | 29.4 us: 1.73x slower  |
| richards_super             | 32.2 ms    | 55.6 ms: 1.73x slower  |
| sympy_sum                  | 82.1 ms    | 143 ms: 1.74x slower   |
| pycparser                  | 664 ms     | 1.16 sec: 1.74x slower |
| asyncio_websockets         | 317 ms     | 551 ms: 1.74x slower   |
| crypto_pyaes               | 41.6 ms    | 72.5 ms: 1.74x slower  |
| unpickle_pure_python       | 123 us     | 217 us: 1.77x slower   |
| json                       | 2.98 ms    | 5.28 ms: 1.77x slower  |
| coroutines                 | 12.4 ms    | 22.1 ms: 1.77x slower  |
| async_generators           | 206 ms     | 368 ms: 1.79x slower   |
| xml_etree_parse            | 89.0 ms    | 163 ms: 1.83x slower   |
| scimark_sparse_mat_mult    | 2.26 ms    | 4.14 ms: 1.83x slower  |
| mako                       | 6.12 ms    | 11.6 ms: 1.89x slower  |
| mdp                        | 1.40 sec   | 2.65 sec: 1.89x slower |
| scimark_fft                | 152 ms     | 289 ms: 1.90x slower   |
| json_dumps                 | 6.48 ms    | 12.5 ms: 1.92x slower  |
| generators                 | 14.8 ms    | 28.6 ms: 1.93x slower  |
| scimark_lu                 | 54.4 ms    | 107 ms: 1.96x slower   |
| json_loads                 | 14.5 us    | 28.9 us: 2.00x slower  |
| create_gc_cycles           | 1.27 ms    | 2.54 ms: 2.00x slower  |
| regex_effbot               | 1.40 ms    | 3.28 ms: 2.35x slower  |
| gc_traversal               | 2.07 ms    | 4.97 ms: 2.40x slower  |
| Geometric mean             | (ref)      | 1.51x slower           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.344x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.57x
- 95% likely to have a slowdown of 1.56x
- 99% likely to have a slowdown of 1.55x

# Memory
- memory change: unknown