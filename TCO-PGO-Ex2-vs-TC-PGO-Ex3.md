# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 237 ms: 1.06x faster   |
| docutils       | 2.61 sec   | 1.81 sec: 1.44x faster |
| html5lib       | 57.3 ms    | 40.8 ms: 1.40x faster  |
| sphinx         | 1.00 sec   | 723 ms: 1.39x faster   |
| Geometric mean | (ref)      | 1.31x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 551 ms     | 304 ms: 1.81x faster  |
| async_generators           | 368 ms     | 224 ms: 1.64x faster  |
| coroutines                 | 22.1 ms    | 13.5 ms: 1.64x faster |
| async_tree_io_tg           | 606 ms     | 419 ms: 1.44x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 362 ms: 1.43x faster  |
| async_tree_memoization_tg  | 307 ms     | 218 ms: 1.41x faster  |
| async_tree_io              | 596 ms     | 429 ms: 1.39x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 367 ms: 1.37x faster  |
| async_tree_none_tg         | 242 ms     | 178 ms: 1.36x faster  |
| async_tree_memoization     | 306 ms     | 227 ms: 1.35x faster  |
| async_tree_none            | 249 ms     | 188 ms: 1.32x faster  |
| Geometric mean             | (ref)      | 1.46x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| pidigits       | 219 ms     | 147 ms: 1.50x faster  |
| float          | 66.8 ms    | 44.8 ms: 1.49x faster |
| nbody          | 86.4 ms    | 58.8 ms: 1.47x faster |
| Geometric mean | (ref)      | 1.49x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.76 ms: 1.86x faster |
| regex_dna      | 196 ms     | 117 ms: 1.67x faster  |
| regex_v8       | 23.8 ms    | 16.7 ms: 1.43x faster |
| regex_compile  | 125 ms     | 88.0 ms: 1.42x faster |
| Geometric mean | (ref)      | 1.58x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 163 ms     | 104 ms: 1.57x faster   |
| json_dumps           | 12.5 ms    | 7.94 ms: 1.57x faster  |
| xml_etree_iterparse  | 103 ms     | 71.5 ms: 1.44x faster  |
| unpickle_pure_python | 217 us     | 154 us: 1.41x faster   |
| json_loads           | 28.9 us    | 21.1 us: 1.37x faster  |
| tomli_loads          | 1.88 sec   | 1.38 sec: 1.36x faster |
| xml_etree_generate   | 86.8 ms    | 66.8 ms: 1.30x faster  |
| pickle_pure_python   | 306 us     | 236 us: 1.30x faster   |
| xml_etree_process    | 58.7 ms    | 46.5 ms: 1.26x faster  |
| Geometric mean       | (ref)      | 1.39x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 26.9 ms: 2.11x slower |
| python_startup_no_site | 7.02 ms    | 20.1 ms: 2.87x slower |
| Geometric mean         | (ref)      | 2.46x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 7.44 ms: 1.56x faster |
| genshi_xml      | 48.1 ms    | 35.3 ms: 1.36x faster |
| genshi_text     | 21.2 ms    | 16.2 ms: 1.31x faster |
| django_template | 30.6 ms    | 27.5 ms: 1.11x faster |
| Geometric mean  | (ref)      | 1.33x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------------|:----------:|:----------------------:|
| regex_effbot               | 3.28 ms    | 1.76 ms: 1.86x faster  |
| create_gc_cycles           | 2.54 ms    | 1.38 ms: 1.83x faster  |
| asyncio_websockets         | 551 ms     | 304 ms: 1.81x faster   |
| gc_traversal               | 4.97 ms    | 2.77 ms: 1.79x faster  |
| mdp                        | 2.65 sec   | 1.57 sec: 1.69x faster |
| scimark_sparse_mat_mult    | 4.14 ms    | 2.48 ms: 1.67x faster  |
| regex_dna                  | 196 ms     | 117 ms: 1.67x faster   |
| async_generators           | 368 ms     | 224 ms: 1.64x faster   |
| coroutines                 | 22.1 ms    | 13.5 ms: 1.64x faster  |
| scimark_lu                 | 107 ms     | 65.2 ms: 1.64x faster  |
| scimark_fft                | 289 ms     | 178 ms: 1.63x faster   |
| generators                 | 28.6 ms    | 18.1 ms: 1.58x faster  |
| sqlite_synth               | 2.66 us    | 1.68 us: 1.58x faster  |
| xml_etree_parse            | 163 ms     | 104 ms: 1.57x faster   |
| json_dumps                 | 12.5 ms    | 7.94 ms: 1.57x faster  |
| mako                       | 11.6 ms    | 7.44 ms: 1.56x faster  |
| pycparser                  | 1.16 sec   | 765 ms: 1.51x faster   |
| pidigits                   | 219 ms     | 147 ms: 1.50x faster   |
| float                      | 66.8 ms    | 44.8 ms: 1.49x faster  |
| fannkuch                   | 393 ms     | 265 ms: 1.49x faster   |
| sympy_sum                  | 143 ms     | 96.6 ms: 1.48x faster  |
| nbody                      | 86.4 ms    | 58.8 ms: 1.47x faster  |
| crypto_pyaes               | 72.5 ms    | 49.3 ms: 1.47x faster  |
| async_tree_io_tg           | 606 ms     | 419 ms: 1.44x faster   |
| go                         | 113 ms     | 78.0 ms: 1.44x faster  |
| deltablue                  | 3.01 ms    | 2.09 ms: 1.44x faster  |
| scimark_sor                | 107 ms     | 73.9 ms: 1.44x faster  |
| dulwich_log                | 61.8 ms    | 43.0 ms: 1.44x faster  |
| xml_etree_iterparse        | 103 ms     | 71.5 ms: 1.44x faster  |
| docutils                   | 2.61 sec   | 1.81 sec: 1.44x faster |
| regex_v8                   | 23.8 ms    | 16.7 ms: 1.43x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 362 ms: 1.43x faster   |
| regex_compile              | 125 ms     | 88.0 ms: 1.42x faster  |
| meteor_contest             | 111 ms     | 78.1 ms: 1.42x faster  |
| spectral_norm              | 82.5 ms    | 58.4 ms: 1.41x faster  |
| coverage                   | 79.6 ms    | 56.4 ms: 1.41x faster  |
| unpickle_pure_python       | 217 us     | 154 us: 1.41x faster   |
| async_tree_memoization_tg  | 307 ms     | 218 ms: 1.41x faster   |
| html5lib                   | 57.3 ms    | 40.8 ms: 1.40x faster  |
| scimark_monte_carlo        | 60.1 ms    | 42.9 ms: 1.40x faster  |
| json                       | 5.28 ms    | 3.77 ms: 1.40x faster  |
| async_tree_io              | 596 ms     | 429 ms: 1.39x faster   |
| pyflate                    | 410 ms     | 295 ms: 1.39x faster   |
| telco                      | 7.39 ms    | 5.33 ms: 1.39x faster  |
| sphinx                     | 1.00 sec   | 723 ms: 1.39x faster   |
| bpe_tokeniser              | 4.39 sec   | 3.17 sec: 1.38x faster |
| sympy_str                  | 258 ms     | 187 ms: 1.38x faster   |
| logging_silent             | 87.1 ns    | 62.9 ns: 1.38x faster  |
| deepcopy_memo              | 29.4 us    | 21.3 us: 1.38x faster  |
| richards_super             | 55.6 ms    | 40.4 ms: 1.38x faster  |
| hexiom                     | 5.74 ms    | 4.17 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 367 ms: 1.37x faster   |
| sqlglot_v2_transpile       | 1.50 ms    | 1.09 ms: 1.37x faster  |
| json_loads                 | 28.9 us    | 21.1 us: 1.37x faster  |
| connected_components       | 445 ms     | 326 ms: 1.37x faster   |
| raytrace                   | 255 ms     | 187 ms: 1.36x faster   |
| sqlglot_v2_parse           | 1.20 ms    | 876 us: 1.36x faster   |
| async_tree_none_tg         | 242 ms     | 178 ms: 1.36x faster   |
| sympy_integrate            | 18.9 ms    | 13.9 ms: 1.36x faster  |
| genshi_xml                 | 48.1 ms    | 35.3 ms: 1.36x faster  |
| sqlglot_v2_optimize        | 52.2 ms    | 38.4 ms: 1.36x faster  |
| richards                   | 47.4 ms    | 35.0 ms: 1.36x faster  |
| sympy_expand               | 440 ms     | 324 ms: 1.36x faster   |
| tomli_loads                | 1.88 sec   | 1.38 sec: 1.36x faster |
| async_tree_memoization     | 306 ms     | 227 ms: 1.35x faster   |
| shortest_path              | 480 ms     | 357 ms: 1.34x faster   |
| pprint_pformat             | 1.51 sec   | 1.13 sec: 1.33x faster |
| async_tree_none            | 249 ms     | 188 ms: 1.32x faster   |
| sqlglot_v2_normalize       | 104 ms     | 79.0 ms: 1.32x faster  |
| pprint_safe_repr           | 736 ms     | 558 ms: 1.32x faster   |
| genshi_text                | 21.2 ms    | 16.2 ms: 1.31x faster  |
| thrift                     | 737 us     | 561 us: 1.31x faster   |
| typing_runtime_protocols   | 148 us     | 113 us: 1.31x faster   |
| xml_etree_generate         | 86.8 ms    | 66.8 ms: 1.30x faster  |
| pickle_pure_python         | 306 us     | 236 us: 1.30x faster   |
| k_core                     | 2.27 sec   | 1.76 sec: 1.29x faster |
| chaos                      | 53.3 ms    | 41.4 ms: 1.29x faster  |
| comprehensions             | 15.5 us    | 12.2 us: 1.27x faster  |
| pylint                     | 275 ms     | 217 ms: 1.27x faster   |
| xml_etree_process          | 58.7 ms    | 46.5 ms: 1.26x faster  |
| deepcopy                   | 244 us     | 199 us: 1.23x faster   |
| deepcopy_reduce            | 2.53 us    | 2.12 us: 1.19x faster  |
| nqueens                    | 75.4 ms    | 65.7 ms: 1.15x faster  |
| many_optionals             | 924 us     | 813 us: 1.14x faster   |
| django_template            | 30.6 ms    | 27.5 ms: 1.11x faster  |
| 2to3                       | 251 ms     | 237 ms: 1.06x faster   |
| bench_thread_pool          | 831 us     | 906 us: 1.09x slower   |
| bench_mp_pool              | 80.9 ms    | 95.0 ms: 1.17x slower  |
| logging_format             | 5.86 us    | 7.18 us: 1.23x slower  |
| logging_simple             | 5.26 us    | 6.67 us: 1.27x slower  |
| pathlib                    | 14.9 ms    | 25.6 ms: 1.72x slower  |
| python_startup             | 12.7 ms    | 26.9 ms: 2.11x slower  |
| subparsers                 | 20.2 ms    | 47.1 ms: 2.33x slower  |
| python_startup_no_site     | 7.02 ms    | 20.1 ms: 2.87x slower  |
| Geometric mean             | (ref)      | 1.32x faster           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: unknown