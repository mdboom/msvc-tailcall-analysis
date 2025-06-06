# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.248x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 251 ms: 1.06x slower   |
| docutils       | 1.81 sec    | 2.61 sec: 1.44x slower |
| html5lib       | 40.8 ms     | 57.3 ms: 1.40x slower  |
| sphinx         | 723 ms      | 1.00 sec: 1.39x slower |
| Geometric mean | (ref)       | 1.31x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------------------|:-----------:|:---------------------:|
| async_tree_none            | 188 ms      | 249 ms: 1.32x slower  |
| async_tree_memoization     | 227 ms      | 306 ms: 1.35x slower  |
| async_tree_none_tg         | 178 ms      | 242 ms: 1.36x slower  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 504 ms: 1.37x slower  |
| async_tree_io              | 429 ms      | 596 ms: 1.39x slower  |
| async_tree_memoization_tg  | 218 ms      | 307 ms: 1.41x slower  |
| async_tree_cpu_io_mixed    | 362 ms      | 517 ms: 1.43x slower  |
| async_tree_io_tg           | 419 ms      | 606 ms: 1.44x slower  |
| coroutines                 | 13.5 ms     | 22.1 ms: 1.64x slower |
| async_generators           | 224 ms      | 368 ms: 1.64x slower  |
| asyncio_websockets         | 304 ms      | 551 ms: 1.81x slower  |
| Geometric mean             | (ref)       | 1.46x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| nbody          | 58.8 ms     | 86.4 ms: 1.47x slower |
| float          | 44.8 ms     | 66.8 ms: 1.49x slower |
| pidigits       | 147 ms      | 219 ms: 1.50x slower  |
| Geometric mean | (ref)       | 1.49x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 88.0 ms     | 125 ms: 1.42x slower  |
| regex_v8       | 16.7 ms     | 23.8 ms: 1.43x slower |
| regex_dna      | 117 ms      | 196 ms: 1.67x slower  |
| regex_effbot   | 1.76 ms     | 3.28 ms: 1.86x slower |
| Geometric mean | (ref)       | 1.58x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------|:-----------:|:----------------------:|
| xml_etree_process    | 46.5 ms     | 58.7 ms: 1.26x slower  |
| pickle_pure_python   | 236 us      | 306 us: 1.30x slower   |
| xml_etree_generate   | 66.8 ms     | 86.8 ms: 1.30x slower  |
| tomli_loads          | 1.38 sec    | 1.88 sec: 1.36x slower |
| json_loads           | 21.1 us     | 28.9 us: 1.37x slower  |
| unpickle_pure_python | 154 us      | 217 us: 1.41x slower   |
| xml_etree_iterparse  | 71.5 ms     | 103 ms: 1.44x slower   |
| json_dumps           | 7.94 ms     | 12.5 ms: 1.57x slower  |
| xml_etree_parse      | 104 ms      | 163 ms: 1.57x slower   |
| Geometric mean       | (ref)       | 1.39x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 20.1 ms     | 7.02 ms: 2.87x faster |
| python_startup         | 26.9 ms     | 12.7 ms: 2.11x faster |
| Geometric mean         | (ref)       | 2.46x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|-----------------|:-----------:|:---------------------:|
| django_template | 27.5 ms     | 30.6 ms: 1.11x slower |
| genshi_text     | 16.2 ms     | 21.2 ms: 1.31x slower |
| genshi_xml      | 35.3 ms     | 48.1 ms: 1.36x slower |
| mako            | 7.44 ms     | 11.6 ms: 1.56x slower |
| Geometric mean  | (ref)       | 1.33x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------------|:-----------:|:----------------------:|
| python_startup_no_site     | 20.1 ms     | 7.02 ms: 2.87x faster  |
| subparsers                 | 47.1 ms     | 20.2 ms: 2.33x faster  |
| python_startup             | 26.9 ms     | 12.7 ms: 2.11x faster  |
| pathlib                    | 25.6 ms     | 14.9 ms: 1.72x faster  |
| logging_simple             | 6.67 us     | 5.26 us: 1.27x faster  |
| logging_format             | 7.18 us     | 5.86 us: 1.23x faster  |
| bench_mp_pool              | 95.0 ms     | 80.9 ms: 1.17x faster  |
| bench_thread_pool          | 906 us      | 831 us: 1.09x faster   |
| 2to3                       | 237 ms      | 251 ms: 1.06x slower   |
| django_template            | 27.5 ms     | 30.6 ms: 1.11x slower  |
| many_optionals             | 813 us      | 924 us: 1.14x slower   |
| nqueens                    | 65.7 ms     | 75.4 ms: 1.15x slower  |
| deepcopy_reduce            | 2.12 us     | 2.53 us: 1.19x slower  |
| deepcopy                   | 199 us      | 244 us: 1.23x slower   |
| xml_etree_process          | 46.5 ms     | 58.7 ms: 1.26x slower  |
| pylint                     | 217 ms      | 275 ms: 1.27x slower   |
| comprehensions             | 12.2 us     | 15.5 us: 1.27x slower  |
| chaos                      | 41.4 ms     | 53.3 ms: 1.29x slower  |
| k_core                     | 1.76 sec    | 2.27 sec: 1.29x slower |
| pickle_pure_python         | 236 us      | 306 us: 1.30x slower   |
| xml_etree_generate         | 66.8 ms     | 86.8 ms: 1.30x slower  |
| typing_runtime_protocols   | 113 us      | 148 us: 1.31x slower   |
| thrift                     | 561 us      | 737 us: 1.31x slower   |
| genshi_text                | 16.2 ms     | 21.2 ms: 1.31x slower  |
| pprint_safe_repr           | 558 ms      | 736 ms: 1.32x slower   |
| sqlglot_v2_normalize       | 79.0 ms     | 104 ms: 1.32x slower   |
| async_tree_none            | 188 ms      | 249 ms: 1.32x slower   |
| pprint_pformat             | 1.13 sec    | 1.51 sec: 1.33x slower |
| shortest_path              | 357 ms      | 480 ms: 1.34x slower   |
| async_tree_memoization     | 227 ms      | 306 ms: 1.35x slower   |
| tomli_loads                | 1.38 sec    | 1.88 sec: 1.36x slower |
| sympy_expand               | 324 ms      | 440 ms: 1.36x slower   |
| richards                   | 35.0 ms     | 47.4 ms: 1.36x slower  |
| sqlglot_v2_optimize        | 38.4 ms     | 52.2 ms: 1.36x slower  |
| genshi_xml                 | 35.3 ms     | 48.1 ms: 1.36x slower  |
| sympy_integrate            | 13.9 ms     | 18.9 ms: 1.36x slower  |
| async_tree_none_tg         | 178 ms      | 242 ms: 1.36x slower   |
| sqlglot_v2_parse           | 876 us      | 1.20 ms: 1.36x slower  |
| raytrace                   | 187 ms      | 255 ms: 1.36x slower   |
| connected_components       | 326 ms      | 445 ms: 1.37x slower   |
| json_loads                 | 21.1 us     | 28.9 us: 1.37x slower  |
| sqlglot_v2_transpile       | 1.09 ms     | 1.50 ms: 1.37x slower  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 504 ms: 1.37x slower   |
| hexiom                     | 4.17 ms     | 5.74 ms: 1.38x slower  |
| richards_super             | 40.4 ms     | 55.6 ms: 1.38x slower  |
| deepcopy_memo              | 21.3 us     | 29.4 us: 1.38x slower  |
| logging_silent             | 62.9 ns     | 87.1 ns: 1.38x slower  |
| sympy_str                  | 187 ms      | 258 ms: 1.38x slower   |
| bpe_tokeniser              | 3.17 sec    | 4.39 sec: 1.38x slower |
| sphinx                     | 723 ms      | 1.00 sec: 1.39x slower |
| telco                      | 5.33 ms     | 7.39 ms: 1.39x slower  |
| pyflate                    | 295 ms      | 410 ms: 1.39x slower   |
| async_tree_io              | 429 ms      | 596 ms: 1.39x slower   |
| json                       | 3.77 ms     | 5.28 ms: 1.40x slower  |
| scimark_monte_carlo        | 42.9 ms     | 60.1 ms: 1.40x slower  |
| html5lib                   | 40.8 ms     | 57.3 ms: 1.40x slower  |
| async_tree_memoization_tg  | 218 ms      | 307 ms: 1.41x slower   |
| unpickle_pure_python       | 154 us      | 217 us: 1.41x slower   |
| coverage                   | 56.4 ms     | 79.6 ms: 1.41x slower  |
| spectral_norm              | 58.4 ms     | 82.5 ms: 1.41x slower  |
| meteor_contest             | 78.1 ms     | 111 ms: 1.42x slower   |
| regex_compile              | 88.0 ms     | 125 ms: 1.42x slower   |
| async_tree_cpu_io_mixed    | 362 ms      | 517 ms: 1.43x slower   |
| regex_v8                   | 16.7 ms     | 23.8 ms: 1.43x slower  |
| docutils                   | 1.81 sec    | 2.61 sec: 1.44x slower |
| xml_etree_iterparse        | 71.5 ms     | 103 ms: 1.44x slower   |
| dulwich_log                | 43.0 ms     | 61.8 ms: 1.44x slower  |
| scimark_sor                | 73.9 ms     | 107 ms: 1.44x slower   |
| deltablue                  | 2.09 ms     | 3.01 ms: 1.44x slower  |
| go                         | 78.0 ms     | 113 ms: 1.44x slower   |
| async_tree_io_tg           | 419 ms      | 606 ms: 1.44x slower   |
| crypto_pyaes               | 49.3 ms     | 72.5 ms: 1.47x slower  |
| nbody                      | 58.8 ms     | 86.4 ms: 1.47x slower  |
| sympy_sum                  | 96.6 ms     | 143 ms: 1.48x slower   |
| fannkuch                   | 265 ms      | 393 ms: 1.49x slower   |
| float                      | 44.8 ms     | 66.8 ms: 1.49x slower  |
| pidigits                   | 147 ms      | 219 ms: 1.50x slower   |
| pycparser                  | 765 ms      | 1.16 sec: 1.51x slower |
| mako                       | 7.44 ms     | 11.6 ms: 1.56x slower  |
| json_dumps                 | 7.94 ms     | 12.5 ms: 1.57x slower  |
| xml_etree_parse            | 104 ms      | 163 ms: 1.57x slower   |
| sqlite_synth               | 1.68 us     | 2.66 us: 1.58x slower  |
| generators                 | 18.1 ms     | 28.6 ms: 1.58x slower  |
| scimark_fft                | 178 ms      | 289 ms: 1.63x slower   |
| scimark_lu                 | 65.2 ms     | 107 ms: 1.64x slower   |
| coroutines                 | 13.5 ms     | 22.1 ms: 1.64x slower  |
| async_generators           | 224 ms      | 368 ms: 1.64x slower   |
| regex_dna                  | 117 ms      | 196 ms: 1.67x slower   |
| scimark_sparse_mat_mult    | 2.48 ms     | 4.14 ms: 1.67x slower  |
| mdp                        | 1.57 sec    | 2.65 sec: 1.69x slower |
| gc_traversal               | 2.77 ms     | 4.97 ms: 1.79x slower  |
| asyncio_websockets         | 304 ms      | 551 ms: 1.81x slower   |
| create_gc_cycles           | 1.38 ms     | 2.54 ms: 1.83x slower  |
| regex_effbot               | 1.76 ms     | 3.28 ms: 1.86x slower  |
| Geometric mean             | (ref)       | 1.32x slower           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.248x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.36x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: unknown