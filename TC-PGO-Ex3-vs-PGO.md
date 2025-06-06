# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.280x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 251 ms: 1.11x slower   |
| docutils       | 1.68 sec | 2.61 sec: 1.55x slower |
| html5lib       | 40.8 ms  | 57.3 ms: 1.40x slower  |
| sphinx         | 658 ms   | 1.00 sec: 1.52x slower |
| Geometric mean | (ref)    | 1.38x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| async_tree_none            | 187 ms  | 249 ms: 1.34x slower  |
| async_tree_memoization     | 224 ms  | 306 ms: 1.37x slower  |
| async_tree_none_tg         | 176 ms  | 242 ms: 1.37x slower  |
| async_tree_io              | 423 ms  | 596 ms: 1.41x slower  |
| async_tree_memoization_tg  | 216 ms  | 307 ms: 1.42x slower  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 504 ms: 1.47x slower  |
| async_tree_io_tg           | 410 ms  | 606 ms: 1.48x slower  |
| async_tree_cpu_io_mixed    | 339 ms  | 517 ms: 1.52x slower  |
| async_generators           | 226 ms  | 368 ms: 1.62x slower  |
| coroutines                 | 13.5 ms | 22.1 ms: 1.64x slower |
| asyncio_websockets         | 318 ms  | 551 ms: 1.73x slower  |
| Geometric mean             | (ref)   | 1.48x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 86.4 ms: 1.17x slower |
| float          | 47.8 ms | 66.8 ms: 1.40x slower |
| pidigits       | 152 ms  | 219 ms: 1.44x slower  |
| Geometric mean | (ref)   | 1.33x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 125 ms: 1.42x slower  |
| regex_dna      | 112 ms  | 196 ms: 1.75x slower  |
| regex_v8       | 13.5 ms | 23.8 ms: 1.76x slower |
| regex_effbot   | 1.42 ms | 3.28 ms: 2.30x slower |
| Geometric mean | (ref)   | 1.78x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.47 sec | 1.88 sec: 1.28x slower |
| pickle_pure_python   | 237 us   | 306 us: 1.29x slower   |
| unpickle_pure_python | 155 us   | 217 us: 1.40x slower   |
| xml_etree_process    | 41.5 ms  | 58.7 ms: 1.41x slower  |
| xml_etree_generate   | 58.7 ms  | 86.8 ms: 1.48x slower  |
| xml_etree_iterparse  | 63.7 ms  | 103 ms: 1.61x slower   |
| json_dumps           | 7.05 ms  | 12.5 ms: 1.77x slower  |
| xml_etree_parse      | 91.2 ms  | 163 ms: 1.78x slower   |
| json_loads           | 14.7 us  | 28.9 us: 1.96x slower  |
| Geometric mean       | (ref)    | 1.54x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 7.02 ms: 2.83x faster |
| python_startup         | 26.1 ms | 12.7 ms: 2.05x faster |
| Geometric mean         | (ref)   | 2.41x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| django_template | 25.1 ms | 30.6 ms: 1.22x slower |
| genshi_text     | 16.5 ms | 21.2 ms: 1.29x slower |
| genshi_xml      | 36.3 ms | 48.1 ms: 1.32x slower |
| mako            | 6.86 ms | 11.6 ms: 1.69x slower |
| Geometric mean  | (ref)   | 1.37x slower          |

All benchmarks:
===============

| Benchmark                  | PGO      | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 19.8 ms  | 7.02 ms: 2.83x faster  |
| pathlib                    | 32.1 ms  | 14.9 ms: 2.16x faster  |
| python_startup             | 26.1 ms  | 12.7 ms: 2.05x faster  |
| logging_simple             | 6.53 us  | 5.26 us: 1.24x faster  |
| logging_format             | 7.03 us  | 5.86 us: 1.20x faster  |
| bench_mp_pool              | 88.7 ms  | 80.9 ms: 1.10x faster  |
| bench_thread_pool          | 864 us   | 831 us: 1.04x faster   |
| 2to3                       | 227 ms   | 251 ms: 1.11x slower   |
| nbody                      | 74.1 ms  | 86.4 ms: 1.17x slower  |
| scimark_sor                | 91.0 ms  | 107 ms: 1.17x slower   |
| nqueens                    | 63.6 ms  | 75.4 ms: 1.19x slower  |
| django_template            | 25.1 ms  | 30.6 ms: 1.22x slower  |
| chaos                      | 43.6 ms  | 53.3 ms: 1.22x slower  |
| subparsers                 | 16.1 ms  | 20.2 ms: 1.25x slower  |
| go                         | 88.6 ms  | 113 ms: 1.27x slower   |
| scimark_monte_carlo        | 47.1 ms  | 60.1 ms: 1.28x slower  |
| tomli_loads                | 1.47 sec | 1.88 sec: 1.28x slower |
| deepcopy                   | 190 us   | 244 us: 1.29x slower   |
| genshi_text                | 16.5 ms  | 21.2 ms: 1.29x slower  |
| pickle_pure_python         | 237 us   | 306 us: 1.29x slower   |
| pyflate                    | 315 ms   | 410 ms: 1.30x slower   |
| deepcopy_reduce            | 1.94 us  | 2.53 us: 1.31x slower  |
| hexiom                     | 4.38 ms  | 5.74 ms: 1.31x slower  |
| k_core                     | 1.73 sec | 2.27 sec: 1.31x slower |
| deltablue                  | 2.29 ms  | 3.01 ms: 1.31x slower  |
| pprint_safe_repr           | 558 ms   | 736 ms: 1.32x slower   |
| genshi_xml                 | 36.3 ms  | 48.1 ms: 1.32x slower  |
| fannkuch                   | 296 ms   | 393 ms: 1.33x slower   |
| shortest_path              | 359 ms   | 480 ms: 1.33x slower   |
| logging_silent             | 65.2 ns  | 87.1 ns: 1.34x slower  |
| async_tree_none            | 187 ms   | 249 ms: 1.34x slower   |
| pprint_pformat             | 1.13 sec | 1.51 sec: 1.34x slower |
| raytrace                   | 191 ms   | 255 ms: 1.34x slower   |
| sqlglot_v2_parse           | 892 us   | 1.20 ms: 1.34x slower  |
| spectral_norm              | 61.5 ms  | 82.5 ms: 1.34x slower  |
| connected_components       | 329 ms   | 445 ms: 1.35x slower   |
| sqlglot_v2_transpile       | 1.10 ms  | 1.50 ms: 1.36x slower  |
| async_tree_memoization     | 224 ms   | 306 ms: 1.37x slower   |
| pylint                     | 201 ms   | 275 ms: 1.37x slower   |
| comprehensions             | 11.3 us  | 15.5 us: 1.37x slower  |
| async_tree_none_tg         | 176 ms   | 242 ms: 1.37x slower   |
| typing_runtime_protocols   | 106 us   | 148 us: 1.39x slower   |
| unpickle_pure_python       | 155 us   | 217 us: 1.40x slower   |
| deepcopy_memo              | 21.0 us  | 29.4 us: 1.40x slower  |
| sympy_integrate            | 13.5 ms  | 18.9 ms: 1.40x slower  |
| float                      | 47.8 ms  | 66.8 ms: 1.40x slower  |
| html5lib                   | 40.8 ms  | 57.3 ms: 1.40x slower  |
| async_tree_io              | 423 ms   | 596 ms: 1.41x slower   |
| xml_etree_process          | 41.5 ms  | 58.7 ms: 1.41x slower  |
| regex_compile              | 88.2 ms  | 125 ms: 1.42x slower   |
| sqlglot_v2_normalize       | 73.6 ms  | 104 ms: 1.42x slower   |
| async_tree_memoization_tg  | 216 ms   | 307 ms: 1.42x slower   |
| dulwich_log                | 43.4 ms  | 61.8 ms: 1.43x slower  |
| pidigits                   | 152 ms   | 219 ms: 1.44x slower   |
| meteor_contest             | 76.9 ms  | 111 ms: 1.44x slower   |
| crypto_pyaes               | 50.0 ms  | 72.5 ms: 1.45x slower  |
| thrift                     | 507 us   | 737 us: 1.45x slower   |
| sympy_expand               | 302 ms   | 440 ms: 1.46x slower   |
| sympy_str                  | 176 ms   | 258 ms: 1.47x slower   |
| async_tree_cpu_io_mixed_tg | 343 ms   | 504 ms: 1.47x slower   |
| async_tree_io_tg           | 410 ms   | 606 ms: 1.48x slower   |
| xml_etree_generate         | 58.7 ms  | 86.8 ms: 1.48x slower  |
| generators                 | 19.3 ms  | 28.6 ms: 1.48x slower  |
| bpe_tokeniser              | 2.96 sec | 4.39 sec: 1.48x slower |
| sqlglot_v2_optimize        | 35.0 ms  | 52.2 ms: 1.49x slower  |
| scimark_fft                | 192 ms   | 289 ms: 1.50x slower   |
| telco                      | 4.89 ms  | 7.39 ms: 1.51x slower  |
| scimark_sparse_mat_mult    | 2.72 ms  | 4.14 ms: 1.52x slower  |
| sphinx                     | 658 ms   | 1.00 sec: 1.52x slower |
| async_tree_cpu_io_mixed    | 339 ms   | 517 ms: 1.52x slower   |
| richards                   | 30.7 ms  | 47.4 ms: 1.54x slower  |
| docutils                   | 1.68 sec | 2.61 sec: 1.55x slower |
| pycparser                  | 738 ms   | 1.16 sec: 1.56x slower |
| sympy_sum                  | 90.5 ms  | 143 ms: 1.58x slower   |
| richards_super             | 35.1 ms  | 55.6 ms: 1.58x slower  |
| scimark_lu                 | 66.9 ms  | 107 ms: 1.60x slower   |
| xml_etree_iterparse        | 63.7 ms  | 103 ms: 1.61x slower   |
| mdp                        | 1.64 sec | 2.65 sec: 1.61x slower |
| async_generators           | 226 ms   | 368 ms: 1.62x slower   |
| coroutines                 | 13.5 ms  | 22.1 ms: 1.64x slower  |
| sqlite_synth               | 1.59 us  | 2.66 us: 1.67x slower  |
| json                       | 3.14 ms  | 5.28 ms: 1.68x slower  |
| mako                       | 6.86 ms  | 11.6 ms: 1.69x slower  |
| coverage                   | 46.8 ms  | 79.6 ms: 1.70x slower  |
| asyncio_websockets         | 318 ms   | 551 ms: 1.73x slower   |
| regex_dna                  | 112 ms   | 196 ms: 1.75x slower   |
| regex_v8                   | 13.5 ms  | 23.8 ms: 1.76x slower  |
| json_dumps                 | 7.05 ms  | 12.5 ms: 1.77x slower  |
| xml_etree_parse            | 91.2 ms  | 163 ms: 1.78x slower   |
| json_loads                 | 14.7 us  | 28.9 us: 1.96x slower  |
| create_gc_cycles           | 1.25 ms  | 2.54 ms: 2.03x slower  |
| many_optionals             | 438 us   | 924 us: 2.11x slower   |
| regex_effbot               | 1.42 ms  | 3.28 ms: 2.30x slower  |
| gc_traversal               | 2.06 ms  | 4.97 ms: 2.42x slower  |
| Geometric mean             | (ref)    | 1.37x slower           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.280x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.38x
- 95% likely to have a slowdown of 1.37x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown