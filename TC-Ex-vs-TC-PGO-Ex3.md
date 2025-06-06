# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.400x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                  |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 231 ms: 1.09x faster   |
| docutils       | 2.61 sec   | 1.77 sec: 1.47x faster |
| html5lib       | 57.3 ms    | 38.8 ms: 1.48x faster  |
| sphinx         | 1.00 sec   | 702 ms: 1.43x faster   |
| Geometric mean | (ref)      | 1.36x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TC-Ex                 |
|----------------------------|:----------:|:---------------------:|
| coroutines                 | 22.1 ms    | 12.3 ms: 1.80x faster |
| asyncio_websockets         | 551 ms     | 312 ms: 1.77x faster  |
| async_generators           | 368 ms     | 213 ms: 1.72x faster  |
| async_tree_io_tg           | 606 ms     | 385 ms: 1.57x faster  |
| async_tree_io              | 596 ms     | 384 ms: 1.55x faster  |
| async_tree_memoization     | 306 ms     | 210 ms: 1.46x faster  |
| async_tree_memoization_tg  | 307 ms     | 210 ms: 1.46x faster  |
| async_tree_none_tg         | 242 ms     | 167 ms: 1.45x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 359 ms: 1.44x faster  |
| async_tree_none            | 249 ms     | 174 ms: 1.43x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 363 ms: 1.39x faster  |
| Geometric mean             | (ref)      | 1.54x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| nbody          | 86.4 ms    | 53.1 ms: 1.63x faster |
| float          | 66.8 ms    | 41.4 ms: 1.61x faster |
| pidigits       | 219 ms     | 146 ms: 1.51x faster  |
| Geometric mean | (ref)      | 1.58x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.85 ms: 1.78x faster |
| regex_dna      | 196 ms     | 121 ms: 1.63x faster  |
| regex_compile  | 125 ms     | 81.9 ms: 1.52x faster |
| regex_v8       | 23.8 ms    | 16.3 ms: 1.46x faster |
| Geometric mean | (ref)      | 1.59x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TC-Ex                  |
|----------------------|:----------:|:----------------------:|
| json_dumps           | 12.5 ms    | 7.79 ms: 1.60x faster  |
| xml_etree_parse      | 163 ms     | 105 ms: 1.56x faster   |
| tomli_loads          | 1.88 sec   | 1.26 sec: 1.49x faster |
| unpickle_pure_python | 217 us     | 148 us: 1.47x faster   |
| xml_etree_iterparse  | 103 ms     | 70.4 ms: 1.46x faster  |
| pickle_pure_python   | 306 us     | 223 us: 1.38x faster   |
| xml_etree_generate   | 86.8 ms    | 64.7 ms: 1.34x faster  |
| json_loads           | 28.9 us    | 21.9 us: 1.32x faster  |
| xml_etree_process    | 58.7 ms    | 44.7 ms: 1.31x faster  |
| Geometric mean       | (ref)      | 1.43x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TC-Ex                 |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 26.4 ms: 2.08x slower |
| python_startup_no_site | 7.02 ms    | 19.4 ms: 2.77x slower |
| Geometric mean         | (ref)      | 2.40x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TC-Ex                 |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 48.1 ms    | 31.3 ms: 1.54x faster |
| mako            | 11.6 ms    | 7.84 ms: 1.48x faster |
| genshi_text     | 21.2 ms    | 14.5 ms: 1.47x faster |
| django_template | 30.6 ms    | 25.2 ms: 1.21x faster |
| Geometric mean  | (ref)      | 1.42x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TC-Ex                  |
|----------------------------|:----------:|:----------------------:|
| create_gc_cycles           | 2.54 ms    | 1.34 ms: 1.89x faster  |
| mdp                        | 2.65 sec   | 1.44 sec: 1.83x faster |
| coroutines                 | 22.1 ms    | 12.3 ms: 1.80x faster  |
| regex_effbot               | 3.28 ms    | 1.85 ms: 1.78x faster  |
| asyncio_websockets         | 551 ms     | 312 ms: 1.77x faster   |
| gc_traversal               | 4.97 ms    | 2.83 ms: 1.76x faster  |
| generators                 | 28.6 ms    | 16.3 ms: 1.75x faster  |
| async_generators           | 368 ms     | 213 ms: 1.72x faster   |
| scimark_fft                | 289 ms     | 169 ms: 1.72x faster   |
| scimark_sparse_mat_mult    | 4.14 ms    | 2.47 ms: 1.68x faster  |
| scimark_lu                 | 107 ms     | 64.2 ms: 1.67x faster  |
| nbody                      | 86.4 ms    | 53.1 ms: 1.63x faster  |
| regex_dna                  | 196 ms     | 121 ms: 1.63x faster   |
| pycparser                  | 1.16 sec   | 713 ms: 1.62x faster   |
| spectral_norm              | 82.5 ms    | 51.1 ms: 1.62x faster  |
| float                      | 66.8 ms    | 41.4 ms: 1.61x faster  |
| go                         | 113 ms     | 70.4 ms: 1.60x faster  |
| json_dumps                 | 12.5 ms    | 7.79 ms: 1.60x faster  |
| sqlite_synth               | 2.66 us    | 1.68 us: 1.58x faster  |
| deltablue                  | 3.01 ms    | 1.91 ms: 1.58x faster  |
| async_tree_io_tg           | 606 ms     | 385 ms: 1.57x faster   |
| fannkuch                   | 393 ms     | 250 ms: 1.57x faster   |
| sympy_sum                  | 143 ms     | 91.4 ms: 1.56x faster  |
| xml_etree_parse            | 163 ms     | 105 ms: 1.56x faster   |
| richards_super             | 55.6 ms    | 35.8 ms: 1.55x faster  |
| async_tree_io              | 596 ms     | 384 ms: 1.55x faster   |
| scimark_sor                | 107 ms     | 68.6 ms: 1.55x faster  |
| scimark_monte_carlo        | 60.1 ms    | 38.9 ms: 1.54x faster  |
| genshi_xml                 | 48.1 ms    | 31.3 ms: 1.54x faster  |
| richards                   | 47.4 ms    | 30.9 ms: 1.53x faster  |
| deepcopy_memo              | 29.4 us    | 19.3 us: 1.53x faster  |
| regex_compile              | 125 ms     | 81.9 ms: 1.52x faster  |
| crypto_pyaes               | 72.5 ms    | 48.0 ms: 1.51x faster  |
| raytrace                   | 255 ms     | 169 ms: 1.51x faster   |
| pidigits                   | 219 ms     | 146 ms: 1.51x faster   |
| sqlglot_v2_parse           | 1.20 ms    | 798 us: 1.50x faster   |
| pyflate                    | 410 ms     | 274 ms: 1.50x faster   |
| tomli_loads                | 1.88 sec   | 1.26 sec: 1.49x faster |
| meteor_contest             | 111 ms     | 74.5 ms: 1.49x faster  |
| mako                       | 11.6 ms    | 7.84 ms: 1.48x faster  |
| html5lib                   | 57.3 ms    | 38.8 ms: 1.48x faster  |
| sqlglot_v2_transpile       | 1.50 ms    | 1.01 ms: 1.48x faster  |
| docutils                   | 2.61 sec   | 1.77 sec: 1.47x faster |
| genshi_text                | 21.2 ms    | 14.5 ms: 1.47x faster  |
| unpickle_pure_python       | 217 us     | 148 us: 1.47x faster   |
| hexiom                     | 5.74 ms    | 3.92 ms: 1.47x faster  |
| dulwich_log                | 61.8 ms    | 42.3 ms: 1.46x faster  |
| xml_etree_iterparse        | 103 ms     | 70.4 ms: 1.46x faster  |
| regex_v8                   | 23.8 ms    | 16.3 ms: 1.46x faster  |
| async_tree_memoization     | 306 ms     | 210 ms: 1.46x faster   |
| async_tree_memoization_tg  | 307 ms     | 210 ms: 1.46x faster   |
| bpe_tokeniser              | 4.39 sec   | 3.01 sec: 1.46x faster |
| sympy_str                  | 258 ms     | 177 ms: 1.46x faster   |
| pprint_pformat             | 1.51 sec   | 1.04 sec: 1.45x faster |
| async_tree_none_tg         | 242 ms     | 167 ms: 1.45x faster   |
| sqlglot_v2_optimize        | 52.2 ms    | 36.1 ms: 1.45x faster  |
| sympy_expand               | 440 ms     | 304 ms: 1.44x faster   |
| pprint_safe_repr           | 736 ms     | 510 ms: 1.44x faster   |
| async_tree_cpu_io_mixed    | 517 ms     | 359 ms: 1.44x faster   |
| coverage                   | 79.6 ms    | 55.4 ms: 1.44x faster  |
| async_tree_none            | 249 ms     | 174 ms: 1.43x faster   |
| connected_components       | 445 ms     | 311 ms: 1.43x faster   |
| sphinx                     | 1.00 sec   | 702 ms: 1.43x faster   |
| sqlglot_v2_normalize       | 104 ms     | 73.3 ms: 1.42x faster  |
| logging_silent             | 87.1 ns    | 61.1 ns: 1.42x faster  |
| chaos                      | 53.3 ms    | 37.7 ms: 1.41x faster  |
| sympy_integrate            | 18.9 ms    | 13.4 ms: 1.41x faster  |
| telco                      | 7.39 ms    | 5.26 ms: 1.41x faster  |
| json                       | 5.28 ms    | 3.78 ms: 1.40x faster  |
| typing_runtime_protocols   | 148 us     | 106 us: 1.39x faster   |
| async_tree_cpu_io_mixed_tg | 504 ms     | 363 ms: 1.39x faster   |
| shortest_path              | 480 ms     | 347 ms: 1.38x faster   |
| pickle_pure_python         | 306 us     | 223 us: 1.38x faster   |
| comprehensions             | 15.5 us    | 11.3 us: 1.37x faster  |
| deepcopy                   | 244 us     | 180 us: 1.35x faster   |
| pylint                     | 275 ms     | 205 ms: 1.34x faster   |
| xml_etree_generate         | 86.8 ms    | 64.7 ms: 1.34x faster  |
| thrift                     | 737 us     | 551 us: 1.34x faster   |
| deepcopy_reduce            | 2.53 us    | 1.90 us: 1.34x faster  |
| k_core                     | 2.27 sec   | 1.71 sec: 1.33x faster |
| json_loads                 | 28.9 us    | 21.9 us: 1.32x faster  |
| xml_etree_process          | 58.7 ms    | 44.7 ms: 1.31x faster  |
| nqueens                    | 75.4 ms    | 59.6 ms: 1.26x faster  |
| many_optionals             | 924 us     | 762 us: 1.21x faster   |
| django_template            | 30.6 ms    | 25.2 ms: 1.21x faster  |
| 2to3                       | 251 ms     | 231 ms: 1.09x faster   |
| bench_thread_pool          | 831 us     | 876 us: 1.05x slower   |
| logging_format             | 5.86 us    | 6.70 us: 1.14x slower  |
| bench_mp_pool              | 80.9 ms    | 93.6 ms: 1.16x slower  |
| logging_simple             | 5.26 us    | 6.25 us: 1.19x slower  |
| pathlib                    | 14.9 ms    | 25.1 ms: 1.69x slower  |
| python_startup             | 12.7 ms    | 26.4 ms: 2.08x slower  |
| subparsers                 | 20.2 ms    | 44.5 ms: 2.20x slower  |
| python_startup_no_site     | 7.02 ms    | 19.4 ms: 2.77x slower  |
| Geometric mean             | (ref)      | 1.39x faster           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.400x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.45x
- 95% likely to have a speedup of 1.45x
- 99% likely to have a speedup of 1.44x

# Memory
- memory change: unknown