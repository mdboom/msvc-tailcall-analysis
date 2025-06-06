# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.012x faster
- HPT reliability: 96.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2                |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 293 ms: 1.17x slower   |
| docutils       | 2.61 sec   | 2.11 sec: 1.24x faster |
| html5lib       | 57.3 ms    | 51.3 ms: 1.12x faster  |
| sphinx         | 1.00 sec   | 843 ms: 1.19x faster   |
| Geometric mean | (ref)      | 1.09x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-Ex2              |
|----------------------------|:----------:|:--------------------:|
| asyncio_websockets         | 551 ms     | 311 ms: 1.77x faster |
| async_tree_cpu_io_mixed    | 517 ms     | 434 ms: 1.19x faster |
| async_tree_cpu_io_mixed_tg | 504 ms     | 428 ms: 1.18x faster |
| async_generators           | 368 ms     | 321 ms: 1.15x faster |
| async_tree_io              | 596 ms     | 551 ms: 1.08x faster |
| async_tree_io_tg           | 606 ms     | 563 ms: 1.08x faster |
| async_tree_memoization_tg  | 307 ms     | 292 ms: 1.05x faster |
| async_tree_memoization     | 306 ms     | 297 ms: 1.03x faster |
| async_tree_none_tg         | 242 ms     | 236 ms: 1.03x faster |
| Geometric mean             | (ref)      | 1.13x faster         |

Benchmark hidden because not significant (2): async_tree_none, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| pidigits       | 219 ms     | 148 ms: 1.48x faster  |
| float          | 66.8 ms    | 73.5 ms: 1.10x slower |
| nbody          | 86.4 ms    | 98.8 ms: 1.14x slower |
| Geometric mean | (ref)      | 1.06x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-Ex2               |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.77 ms: 1.85x faster |
| regex_dna      | 196 ms     | 118 ms: 1.67x faster  |
| regex_v8       | 23.8 ms    | 17.0 ms: 1.40x faster |
| regex_compile  | 125 ms     | 123 ms: 1.02x faster  |
| Geometric mean | (ref)      | 1.45x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-Ex2                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 163 ms     | 108 ms: 1.51x faster   |
| json_dumps           | 12.5 ms    | 8.99 ms: 1.38x faster  |
| json_loads           | 28.9 us    | 21.4 us: 1.35x faster  |
| xml_etree_iterparse  | 103 ms     | 87.5 ms: 1.17x faster  |
| xml_etree_generate   | 86.8 ms    | 87.5 ms: 1.01x slower  |
| tomli_loads          | 1.88 sec   | 1.97 sec: 1.05x slower |
| xml_etree_process    | 58.7 ms    | 63.0 ms: 1.07x slower  |
| pickle_pure_python   | 306 us     | 354 us: 1.16x slower   |
| unpickle_pure_python | 217 us     | 271 us: 1.25x slower   |
| Geometric mean       | (ref)      | 1.08x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TCO-Ex2               |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 27.2 ms: 2.14x slower |
| python_startup_no_site | 7.02 ms    | 20.3 ms: 2.90x slower |
| Geometric mean         | (ref)      | 2.49x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-Ex2               |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 11.4 ms: 1.01x faster |
| genshi_xml      | 48.1 ms    | 48.8 ms: 1.01x slower |
| genshi_text     | 21.2 ms    | 23.4 ms: 1.10x slower |
| django_template | 30.6 ms    | 35.8 ms: 1.17x slower |
| Geometric mean  | (ref)      | 1.07x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-Ex2                |
|----------------------------|:----------:|:----------------------:|
| regex_effbot               | 3.28 ms    | 1.77 ms: 1.85x faster  |
| create_gc_cycles           | 2.54 ms    | 1.40 ms: 1.81x faster  |
| gc_traversal               | 4.97 ms    | 2.79 ms: 1.78x faster  |
| asyncio_websockets         | 551 ms     | 311 ms: 1.77x faster   |
| regex_dna                  | 196 ms     | 118 ms: 1.67x faster   |
| xml_etree_parse            | 163 ms     | 108 ms: 1.51x faster   |
| sqlite_synth               | 2.66 us    | 1.78 us: 1.49x faster  |
| pidigits                   | 219 ms     | 148 ms: 1.48x faster   |
| mdp                        | 2.65 sec   | 1.82 sec: 1.45x faster |
| regex_v8                   | 23.8 ms    | 17.0 ms: 1.40x faster  |
| json_dumps                 | 12.5 ms    | 8.99 ms: 1.38x faster  |
| json_loads                 | 28.9 us    | 21.4 us: 1.35x faster  |
| json                       | 5.28 ms    | 3.94 ms: 1.34x faster  |
| coverage                   | 79.6 ms    | 61.1 ms: 1.30x faster  |
| connected_components       | 445 ms     | 351 ms: 1.27x faster   |
| shortest_path              | 480 ms     | 384 ms: 1.25x faster   |
| k_core                     | 2.27 sec   | 1.83 sec: 1.24x faster |
| docutils                   | 2.61 sec   | 2.11 sec: 1.24x faster |
| dulwich_log                | 61.8 ms    | 50.5 ms: 1.22x faster  |
| sympy_sum                  | 143 ms     | 118 ms: 1.21x faster   |
| pycparser                  | 1.16 sec   | 968 ms: 1.19x faster   |
| async_tree_cpu_io_mixed    | 517 ms     | 434 ms: 1.19x faster   |
| sphinx                     | 1.00 sec   | 843 ms: 1.19x faster   |
| async_tree_cpu_io_mixed_tg | 504 ms     | 428 ms: 1.18x faster   |
| xml_etree_iterparse        | 103 ms     | 87.5 ms: 1.17x faster  |
| telco                      | 7.39 ms    | 6.34 ms: 1.17x faster  |
| meteor_contest             | 111 ms     | 95.0 ms: 1.16x faster  |
| async_generators           | 368 ms     | 321 ms: 1.15x faster   |
| html5lib                   | 57.3 ms    | 51.3 ms: 1.12x faster  |
| pylint                     | 275 ms     | 249 ms: 1.11x faster   |
| sympy_str                  | 258 ms     | 234 ms: 1.10x faster   |
| sympy_expand               | 440 ms     | 399 ms: 1.10x faster   |
| thrift                     | 737 us     | 680 us: 1.08x faster   |
| scimark_fft                | 289 ms     | 267 ms: 1.08x faster   |
| async_tree_io              | 596 ms     | 551 ms: 1.08x faster   |
| sympy_integrate            | 18.9 ms    | 17.5 ms: 1.08x faster  |
| async_tree_io_tg           | 606 ms     | 563 ms: 1.08x faster   |
| async_tree_memoization_tg  | 307 ms     | 292 ms: 1.05x faster   |
| sqlglot_v2_optimize        | 52.2 ms    | 49.6 ms: 1.05x faster  |
| many_optionals             | 924 us     | 890 us: 1.04x faster   |
| async_tree_memoization     | 306 ms     | 297 ms: 1.03x faster   |
| async_tree_none_tg         | 242 ms     | 236 ms: 1.03x faster   |
| fannkuch                   | 393 ms     | 386 ms: 1.02x faster   |
| bpe_tokeniser              | 4.39 sec   | 4.30 sec: 1.02x faster |
| regex_compile              | 125 ms     | 123 ms: 1.02x faster   |
| mako                       | 11.6 ms    | 11.4 ms: 1.01x faster  |
| sqlglot_v2_normalize       | 104 ms     | 103 ms: 1.01x faster   |
| typing_runtime_protocols   | 148 us     | 146 us: 1.01x faster   |
| xml_etree_generate         | 86.8 ms    | 87.5 ms: 1.01x slower  |
| genshi_xml                 | 48.1 ms    | 48.8 ms: 1.01x slower  |
| scimark_sparse_mat_mult    | 4.14 ms    | 4.27 ms: 1.03x slower  |
| richards_super             | 55.6 ms    | 58.0 ms: 1.04x slower  |
| tomli_loads                | 1.88 sec   | 1.97 sec: 1.05x slower |
| crypto_pyaes               | 72.5 ms    | 76.8 ms: 1.06x slower  |
| deepcopy_reduce            | 2.53 us    | 2.71 us: 1.07x slower  |
| pprint_pformat             | 1.51 sec   | 1.61 sec: 1.07x slower |
| xml_etree_process          | 58.7 ms    | 63.0 ms: 1.07x slower  |
| pprint_safe_repr           | 736 ms     | 789 ms: 1.07x slower   |
| richards                   | 47.4 ms    | 51.0 ms: 1.08x slower  |
| sqlglot_v2_transpile       | 1.50 ms    | 1.62 ms: 1.08x slower  |
| scimark_lu                 | 107 ms     | 116 ms: 1.08x slower   |
| deepcopy                   | 244 us     | 266 us: 1.09x slower   |
| float                      | 66.8 ms    | 73.5 ms: 1.10x slower  |
| genshi_text                | 21.2 ms    | 23.4 ms: 1.10x slower  |
| pyflate                    | 410 ms     | 457 ms: 1.12x slower   |
| deepcopy_memo              | 29.4 us    | 33.0 us: 1.12x slower  |
| sqlglot_v2_parse           | 1.20 ms    | 1.34 ms: 1.12x slower  |
| nbody                      | 86.4 ms    | 98.8 ms: 1.14x slower  |
| pickle_pure_python         | 306 us     | 354 us: 1.16x slower   |
| 2to3                       | 251 ms     | 293 ms: 1.17x slower   |
| generators                 | 28.6 ms    | 33.5 ms: 1.17x slower  |
| django_template            | 30.6 ms    | 35.8 ms: 1.17x slower  |
| spectral_norm              | 82.5 ms    | 97.1 ms: 1.18x slower  |
| raytrace                   | 255 ms     | 306 ms: 1.20x slower   |
| bench_mp_pool              | 80.9 ms    | 97.6 ms: 1.21x slower  |
| bench_thread_pool          | 831 us     | 1.01 ms: 1.22x slower  |
| go                         | 113 ms     | 138 ms: 1.23x slower   |
| nqueens                    | 75.4 ms    | 93.2 ms: 1.24x slower  |
| comprehensions             | 15.5 us    | 19.4 us: 1.25x slower  |
| scimark_monte_carlo        | 60.1 ms    | 75.2 ms: 1.25x slower  |
| unpickle_pure_python       | 217 us     | 271 us: 1.25x slower   |
| scimark_sor                | 107 ms     | 133 ms: 1.25x slower   |
| chaos                      | 53.3 ms    | 67.0 ms: 1.26x slower  |
| hexiom                     | 5.74 ms    | 7.27 ms: 1.27x slower  |
| deltablue                  | 3.01 ms    | 4.08 ms: 1.35x slower  |
| logging_silent             | 87.1 ns    | 121 ns: 1.40x slower   |
| logging_format             | 5.86 us    | 9.13 us: 1.56x slower  |
| logging_simple             | 5.26 us    | 8.63 us: 1.64x slower  |
| pathlib                    | 14.9 ms    | 26.8 ms: 1.80x slower  |
| python_startup             | 12.7 ms    | 27.2 ms: 2.14x slower  |
| subparsers                 | 20.2 ms    | 50.4 ms: 2.50x slower  |
| python_startup_no_site     | 7.02 ms    | 20.3 ms: 2.90x slower  |
| Geometric mean             | (ref)      | 1.00x faster           |

Benchmark hidden because not significant (2): async_tree_none, coroutines
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 96.44% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown