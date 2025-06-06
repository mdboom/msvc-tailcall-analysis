# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.285x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 251 ms: 1.09x slower   |
| docutils       | 1.77 sec | 2.61 sec: 1.47x slower |
| html5lib       | 38.8 ms  | 57.3 ms: 1.48x slower  |
| sphinx         | 702 ms   | 1.00 sec: 1.43x slower |
| Geometric mean | (ref)    | 1.36x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 504 ms: 1.39x slower  |
| async_tree_none            | 174 ms  | 249 ms: 1.43x slower  |
| async_tree_cpu_io_mixed    | 359 ms  | 517 ms: 1.44x slower  |
| async_tree_none_tg         | 167 ms  | 242 ms: 1.45x slower  |
| async_tree_memoization_tg  | 210 ms  | 307 ms: 1.46x slower  |
| async_tree_memoization     | 210 ms  | 306 ms: 1.46x slower  |
| async_tree_io              | 384 ms  | 596 ms: 1.55x slower  |
| async_tree_io_tg           | 385 ms  | 606 ms: 1.57x slower  |
| async_generators           | 213 ms  | 368 ms: 1.72x slower  |
| asyncio_websockets         | 312 ms  | 551 ms: 1.77x slower  |
| coroutines                 | 12.3 ms | 22.1 ms: 1.80x slower |
| Geometric mean             | (ref)   | 1.54x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 219 ms: 1.51x slower  |
| float          | 41.4 ms | 66.8 ms: 1.61x slower |
| nbody          | 53.1 ms | 86.4 ms: 1.63x slower |
| Geometric mean | (ref)   | 1.58x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_v8       | 16.3 ms | 23.8 ms: 1.46x slower |
| regex_compile  | 81.9 ms | 125 ms: 1.52x slower  |
| regex_dna      | 121 ms  | 196 ms: 1.63x slower  |
| regex_effbot   | 1.85 ms | 3.28 ms: 1.78x slower |
| Geometric mean | (ref)   | 1.59x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| xml_etree_process    | 44.7 ms  | 58.7 ms: 1.31x slower  |
| json_loads           | 21.9 us  | 28.9 us: 1.32x slower  |
| xml_etree_generate   | 64.7 ms  | 86.8 ms: 1.34x slower  |
| pickle_pure_python   | 223 us   | 306 us: 1.38x slower   |
| xml_etree_iterparse  | 70.4 ms  | 103 ms: 1.46x slower   |
| unpickle_pure_python | 148 us   | 217 us: 1.47x slower   |
| tomli_loads          | 1.26 sec | 1.88 sec: 1.49x slower |
| xml_etree_parse      | 105 ms   | 163 ms: 1.56x slower   |
| json_dumps           | 7.79 ms  | 12.5 ms: 1.60x slower  |
| Geometric mean       | (ref)    | 1.43x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.4 ms | 7.02 ms: 2.77x faster |
| python_startup         | 26.4 ms | 12.7 ms: 2.08x faster |
| Geometric mean         | (ref)   | 2.40x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| django_template | 25.2 ms | 30.6 ms: 1.21x slower |
| genshi_text     | 14.5 ms | 21.2 ms: 1.47x slower |
| mako            | 7.84 ms | 11.6 ms: 1.48x slower |
| genshi_xml      | 31.3 ms | 48.1 ms: 1.54x slower |
| Geometric mean  | (ref)   | 1.42x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 19.4 ms  | 7.02 ms: 2.77x faster  |
| subparsers                 | 44.5 ms  | 20.2 ms: 2.20x faster  |
| python_startup             | 26.4 ms  | 12.7 ms: 2.08x faster  |
| pathlib                    | 25.1 ms  | 14.9 ms: 1.69x faster  |
| logging_simple             | 6.25 us  | 5.26 us: 1.19x faster  |
| bench_mp_pool              | 93.6 ms  | 80.9 ms: 1.16x faster  |
| logging_format             | 6.70 us  | 5.86 us: 1.14x faster  |
| bench_thread_pool          | 876 us   | 831 us: 1.05x faster   |
| 2to3                       | 231 ms   | 251 ms: 1.09x slower   |
| django_template            | 25.2 ms  | 30.6 ms: 1.21x slower  |
| many_optionals             | 762 us   | 924 us: 1.21x slower   |
| nqueens                    | 59.6 ms  | 75.4 ms: 1.26x slower  |
| xml_etree_process          | 44.7 ms  | 58.7 ms: 1.31x slower  |
| json_loads                 | 21.9 us  | 28.9 us: 1.32x slower  |
| k_core                     | 1.71 sec | 2.27 sec: 1.33x slower |
| deepcopy_reduce            | 1.90 us  | 2.53 us: 1.34x slower  |
| thrift                     | 551 us   | 737 us: 1.34x slower   |
| xml_etree_generate         | 64.7 ms  | 86.8 ms: 1.34x slower  |
| pylint                     | 205 ms   | 275 ms: 1.34x slower   |
| deepcopy                   | 180 us   | 244 us: 1.35x slower   |
| comprehensions             | 11.3 us  | 15.5 us: 1.37x slower  |
| pickle_pure_python         | 223 us   | 306 us: 1.38x slower   |
| shortest_path              | 347 ms   | 480 ms: 1.38x slower   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 504 ms: 1.39x slower   |
| typing_runtime_protocols   | 106 us   | 148 us: 1.39x slower   |
| json                       | 3.78 ms  | 5.28 ms: 1.40x slower  |
| telco                      | 5.26 ms  | 7.39 ms: 1.41x slower  |
| sympy_integrate            | 13.4 ms  | 18.9 ms: 1.41x slower  |
| chaos                      | 37.7 ms  | 53.3 ms: 1.41x slower  |
| logging_silent             | 61.1 ns  | 87.1 ns: 1.42x slower  |
| sqlglot_v2_normalize       | 73.3 ms  | 104 ms: 1.42x slower   |
| sphinx                     | 702 ms   | 1.00 sec: 1.43x slower |
| connected_components       | 311 ms   | 445 ms: 1.43x slower   |
| async_tree_none            | 174 ms   | 249 ms: 1.43x slower   |
| coverage                   | 55.4 ms  | 79.6 ms: 1.44x slower  |
| async_tree_cpu_io_mixed    | 359 ms   | 517 ms: 1.44x slower   |
| pprint_safe_repr           | 510 ms   | 736 ms: 1.44x slower   |
| sympy_expand               | 304 ms   | 440 ms: 1.44x slower   |
| sqlglot_v2_optimize        | 36.1 ms  | 52.2 ms: 1.45x slower  |
| async_tree_none_tg         | 167 ms   | 242 ms: 1.45x slower   |
| pprint_pformat             | 1.04 sec | 1.51 sec: 1.45x slower |
| sympy_str                  | 177 ms   | 258 ms: 1.46x slower   |
| bpe_tokeniser              | 3.01 sec | 4.39 sec: 1.46x slower |
| async_tree_memoization_tg  | 210 ms   | 307 ms: 1.46x slower   |
| async_tree_memoization     | 210 ms   | 306 ms: 1.46x slower   |
| regex_v8                   | 16.3 ms  | 23.8 ms: 1.46x slower  |
| xml_etree_iterparse        | 70.4 ms  | 103 ms: 1.46x slower   |
| dulwich_log                | 42.3 ms  | 61.8 ms: 1.46x slower  |
| hexiom                     | 3.92 ms  | 5.74 ms: 1.47x slower  |
| unpickle_pure_python       | 148 us   | 217 us: 1.47x slower   |
| genshi_text                | 14.5 ms  | 21.2 ms: 1.47x slower  |
| docutils                   | 1.77 sec | 2.61 sec: 1.47x slower |
| sqlglot_v2_transpile       | 1.01 ms  | 1.50 ms: 1.48x slower  |
| html5lib                   | 38.8 ms  | 57.3 ms: 1.48x slower  |
| mako                       | 7.84 ms  | 11.6 ms: 1.48x slower  |
| meteor_contest             | 74.5 ms  | 111 ms: 1.49x slower   |
| tomli_loads                | 1.26 sec | 1.88 sec: 1.49x slower |
| pyflate                    | 274 ms   | 410 ms: 1.50x slower   |
| sqlglot_v2_parse           | 798 us   | 1.20 ms: 1.50x slower  |
| pidigits                   | 146 ms   | 219 ms: 1.51x slower   |
| raytrace                   | 169 ms   | 255 ms: 1.51x slower   |
| crypto_pyaes               | 48.0 ms  | 72.5 ms: 1.51x slower  |
| regex_compile              | 81.9 ms  | 125 ms: 1.52x slower   |
| deepcopy_memo              | 19.3 us  | 29.4 us: 1.53x slower  |
| richards                   | 30.9 ms  | 47.4 ms: 1.53x slower  |
| genshi_xml                 | 31.3 ms  | 48.1 ms: 1.54x slower  |
| scimark_monte_carlo        | 38.9 ms  | 60.1 ms: 1.54x slower  |
| scimark_sor                | 68.6 ms  | 107 ms: 1.55x slower   |
| async_tree_io              | 384 ms   | 596 ms: 1.55x slower   |
| richards_super             | 35.8 ms  | 55.6 ms: 1.55x slower  |
| xml_etree_parse            | 105 ms   | 163 ms: 1.56x slower   |
| sympy_sum                  | 91.4 ms  | 143 ms: 1.56x slower   |
| fannkuch                   | 250 ms   | 393 ms: 1.57x slower   |
| async_tree_io_tg           | 385 ms   | 606 ms: 1.57x slower   |
| deltablue                  | 1.91 ms  | 3.01 ms: 1.58x slower  |
| sqlite_synth               | 1.68 us  | 2.66 us: 1.58x slower  |
| json_dumps                 | 7.79 ms  | 12.5 ms: 1.60x slower  |
| go                         | 70.4 ms  | 113 ms: 1.60x slower   |
| float                      | 41.4 ms  | 66.8 ms: 1.61x slower  |
| spectral_norm              | 51.1 ms  | 82.5 ms: 1.62x slower  |
| pycparser                  | 713 ms   | 1.16 sec: 1.62x slower |
| regex_dna                  | 121 ms   | 196 ms: 1.63x slower   |
| nbody                      | 53.1 ms  | 86.4 ms: 1.63x slower  |
| scimark_lu                 | 64.2 ms  | 107 ms: 1.67x slower   |
| scimark_sparse_mat_mult    | 2.47 ms  | 4.14 ms: 1.68x slower  |
| scimark_fft                | 169 ms   | 289 ms: 1.72x slower   |
| async_generators           | 213 ms   | 368 ms: 1.72x slower   |
| generators                 | 16.3 ms  | 28.6 ms: 1.75x slower  |
| gc_traversal               | 2.83 ms  | 4.97 ms: 1.76x slower  |
| asyncio_websockets         | 312 ms   | 551 ms: 1.77x slower   |
| regex_effbot               | 1.85 ms  | 3.28 ms: 1.78x slower  |
| coroutines                 | 12.3 ms  | 22.1 ms: 1.80x slower  |
| mdp                        | 1.44 sec | 2.65 sec: 1.83x slower |
| create_gc_cycles           | 1.34 ms  | 2.54 ms: 1.89x slower  |
| Geometric mean             | (ref)    | 1.39x slower           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.285x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.44x

# Memory
- memory change: unknown