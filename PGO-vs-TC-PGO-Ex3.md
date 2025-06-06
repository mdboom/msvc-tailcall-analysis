# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.390x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO                    |
|----------------|:----------:|:----------------------:|
| 2to3           | 251 ms     | 227 ms: 1.11x faster   |
| docutils       | 2.61 sec   | 1.68 sec: 1.55x faster |
| html5lib       | 57.3 ms    | 40.8 ms: 1.40x faster  |
| sphinx         | 1.00 sec   | 658 ms: 1.52x faster   |
| Geometric mean | (ref)      | 1.38x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | PGO                   |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 551 ms     | 318 ms: 1.73x faster  |
| coroutines                 | 22.1 ms    | 13.5 ms: 1.64x faster |
| async_generators           | 368 ms     | 226 ms: 1.62x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 339 ms: 1.52x faster  |
| async_tree_io_tg           | 606 ms     | 410 ms: 1.48x faster  |
| async_tree_cpu_io_mixed_tg | 504 ms     | 343 ms: 1.47x faster  |
| async_tree_memoization_tg  | 307 ms     | 216 ms: 1.42x faster  |
| async_tree_io              | 596 ms     | 423 ms: 1.41x faster  |
| async_tree_none_tg         | 242 ms     | 176 ms: 1.37x faster  |
| async_tree_memoization     | 306 ms     | 224 ms: 1.37x faster  |
| async_tree_none            | 249 ms     | 187 ms: 1.34x faster  |
| Geometric mean             | (ref)      | 1.48x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO                   |
|----------------|:----------:|:---------------------:|
| pidigits       | 219 ms     | 152 ms: 1.44x faster  |
| float          | 66.8 ms    | 47.8 ms: 1.40x faster |
| nbody          | 86.4 ms    | 74.1 ms: 1.17x faster |
| Geometric mean | (ref)      | 1.33x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | PGO                   |
|----------------|:----------:|:---------------------:|
| regex_effbot   | 3.28 ms    | 1.42 ms: 2.30x faster |
| regex_v8       | 23.8 ms    | 13.5 ms: 1.76x faster |
| regex_dna      | 196 ms     | 112 ms: 1.75x faster  |
| regex_compile  | 125 ms     | 88.2 ms: 1.42x faster |
| Geometric mean | (ref)      | 1.78x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | PGO                    |
|----------------------|:----------:|:----------------------:|
| json_loads           | 28.9 us    | 14.7 us: 1.96x faster  |
| xml_etree_parse      | 163 ms     | 91.2 ms: 1.78x faster  |
| json_dumps           | 12.5 ms    | 7.05 ms: 1.77x faster  |
| xml_etree_iterparse  | 103 ms     | 63.7 ms: 1.61x faster  |
| xml_etree_generate   | 86.8 ms    | 58.7 ms: 1.48x faster  |
| xml_etree_process    | 58.7 ms    | 41.5 ms: 1.41x faster  |
| unpickle_pure_python | 217 us     | 155 us: 1.40x faster   |
| pickle_pure_python   | 306 us     | 237 us: 1.29x faster   |
| tomli_loads          | 1.88 sec   | 1.47 sec: 1.28x faster |
| Geometric mean       | (ref)      | 1.54x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | PGO                   |
|------------------------|:----------:|:---------------------:|
| python_startup         | 12.7 ms    | 26.1 ms: 2.05x slower |
| python_startup_no_site | 7.02 ms    | 19.8 ms: 2.83x slower |
| Geometric mean         | (ref)      | 2.41x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | PGO                   |
|-----------------|:----------:|:---------------------:|
| mako            | 11.6 ms    | 6.86 ms: 1.69x faster |
| genshi_xml      | 48.1 ms    | 36.3 ms: 1.32x faster |
| genshi_text     | 21.2 ms    | 16.5 ms: 1.29x faster |
| django_template | 30.6 ms    | 25.1 ms: 1.22x faster |
| Geometric mean  | (ref)      | 1.37x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | PGO                    |
|----------------------------|:----------:|:----------------------:|
| gc_traversal               | 4.97 ms    | 2.06 ms: 2.42x faster  |
| regex_effbot               | 3.28 ms    | 1.42 ms: 2.30x faster  |
| many_optionals             | 924 us     | 438 us: 2.11x faster   |
| create_gc_cycles           | 2.54 ms    | 1.25 ms: 2.03x faster  |
| json_loads                 | 28.9 us    | 14.7 us: 1.96x faster  |
| xml_etree_parse            | 163 ms     | 91.2 ms: 1.78x faster  |
| json_dumps                 | 12.5 ms    | 7.05 ms: 1.77x faster  |
| regex_v8                   | 23.8 ms    | 13.5 ms: 1.76x faster  |
| regex_dna                  | 196 ms     | 112 ms: 1.75x faster   |
| asyncio_websockets         | 551 ms     | 318 ms: 1.73x faster   |
| coverage                   | 79.6 ms    | 46.8 ms: 1.70x faster  |
| mako                       | 11.6 ms    | 6.86 ms: 1.69x faster  |
| json                       | 5.28 ms    | 3.14 ms: 1.68x faster  |
| sqlite_synth               | 2.66 us    | 1.59 us: 1.67x faster  |
| coroutines                 | 22.1 ms    | 13.5 ms: 1.64x faster  |
| async_generators           | 368 ms     | 226 ms: 1.62x faster   |
| mdp                        | 2.65 sec   | 1.64 sec: 1.61x faster |
| xml_etree_iterparse        | 103 ms     | 63.7 ms: 1.61x faster  |
| scimark_lu                 | 107 ms     | 66.9 ms: 1.60x faster  |
| richards_super             | 55.6 ms    | 35.1 ms: 1.58x faster  |
| sympy_sum                  | 143 ms     | 90.5 ms: 1.58x faster  |
| pycparser                  | 1.16 sec   | 738 ms: 1.56x faster   |
| docutils                   | 2.61 sec   | 1.68 sec: 1.55x faster |
| richards                   | 47.4 ms    | 30.7 ms: 1.54x faster  |
| async_tree_cpu_io_mixed    | 517 ms     | 339 ms: 1.52x faster   |
| sphinx                     | 1.00 sec   | 658 ms: 1.52x faster   |
| scimark_sparse_mat_mult    | 4.14 ms    | 2.72 ms: 1.52x faster  |
| telco                      | 7.39 ms    | 4.89 ms: 1.51x faster  |
| scimark_fft                | 289 ms     | 192 ms: 1.50x faster   |
| sqlglot_v2_optimize        | 52.2 ms    | 35.0 ms: 1.49x faster  |
| bpe_tokeniser              | 4.39 sec   | 2.96 sec: 1.48x faster |
| generators                 | 28.6 ms    | 19.3 ms: 1.48x faster  |
| xml_etree_generate         | 86.8 ms    | 58.7 ms: 1.48x faster  |
| async_tree_io_tg           | 606 ms     | 410 ms: 1.48x faster   |
| async_tree_cpu_io_mixed_tg | 504 ms     | 343 ms: 1.47x faster   |
| sympy_str                  | 258 ms     | 176 ms: 1.47x faster   |
| sympy_expand               | 440 ms     | 302 ms: 1.46x faster   |
| thrift                     | 737 us     | 507 us: 1.45x faster   |
| crypto_pyaes               | 72.5 ms    | 50.0 ms: 1.45x faster  |
| meteor_contest             | 111 ms     | 76.9 ms: 1.44x faster  |
| pidigits                   | 219 ms     | 152 ms: 1.44x faster   |
| dulwich_log                | 61.8 ms    | 43.4 ms: 1.43x faster  |
| async_tree_memoization_tg  | 307 ms     | 216 ms: 1.42x faster   |
| sqlglot_v2_normalize       | 104 ms     | 73.6 ms: 1.42x faster  |
| regex_compile              | 125 ms     | 88.2 ms: 1.42x faster  |
| xml_etree_process          | 58.7 ms    | 41.5 ms: 1.41x faster  |
| async_tree_io              | 596 ms     | 423 ms: 1.41x faster   |
| html5lib                   | 57.3 ms    | 40.8 ms: 1.40x faster  |
| float                      | 66.8 ms    | 47.8 ms: 1.40x faster  |
| sympy_integrate            | 18.9 ms    | 13.5 ms: 1.40x faster  |
| deepcopy_memo              | 29.4 us    | 21.0 us: 1.40x faster  |
| unpickle_pure_python       | 217 us     | 155 us: 1.40x faster   |
| typing_runtime_protocols   | 148 us     | 106 us: 1.39x faster   |
| async_tree_none_tg         | 242 ms     | 176 ms: 1.37x faster   |
| comprehensions             | 15.5 us    | 11.3 us: 1.37x faster  |
| pylint                     | 275 ms     | 201 ms: 1.37x faster   |
| async_tree_memoization     | 306 ms     | 224 ms: 1.37x faster   |
| sqlglot_v2_transpile       | 1.50 ms    | 1.10 ms: 1.36x faster  |
| connected_components       | 445 ms     | 329 ms: 1.35x faster   |
| spectral_norm              | 82.5 ms    | 61.5 ms: 1.34x faster  |
| sqlglot_v2_parse           | 1.20 ms    | 892 us: 1.34x faster   |
| raytrace                   | 255 ms     | 191 ms: 1.34x faster   |
| pprint_pformat             | 1.51 sec   | 1.13 sec: 1.34x faster |
| async_tree_none            | 249 ms     | 187 ms: 1.34x faster   |
| logging_silent             | 87.1 ns    | 65.2 ns: 1.34x faster  |
| shortest_path              | 480 ms     | 359 ms: 1.33x faster   |
| fannkuch                   | 393 ms     | 296 ms: 1.33x faster   |
| genshi_xml                 | 48.1 ms    | 36.3 ms: 1.32x faster  |
| pprint_safe_repr           | 736 ms     | 558 ms: 1.32x faster   |
| deltablue                  | 3.01 ms    | 2.29 ms: 1.31x faster  |
| k_core                     | 2.27 sec   | 1.73 sec: 1.31x faster |
| hexiom                     | 5.74 ms    | 4.38 ms: 1.31x faster  |
| deepcopy_reduce            | 2.53 us    | 1.94 us: 1.31x faster  |
| pyflate                    | 410 ms     | 315 ms: 1.30x faster   |
| pickle_pure_python         | 306 us     | 237 us: 1.29x faster   |
| genshi_text                | 21.2 ms    | 16.5 ms: 1.29x faster  |
| deepcopy                   | 244 us     | 190 us: 1.29x faster   |
| tomli_loads                | 1.88 sec   | 1.47 sec: 1.28x faster |
| scimark_monte_carlo        | 60.1 ms    | 47.1 ms: 1.28x faster  |
| go                         | 113 ms     | 88.6 ms: 1.27x faster  |
| subparsers                 | 20.2 ms    | 16.1 ms: 1.25x faster  |
| chaos                      | 53.3 ms    | 43.6 ms: 1.22x faster  |
| django_template            | 30.6 ms    | 25.1 ms: 1.22x faster  |
| nqueens                    | 75.4 ms    | 63.6 ms: 1.19x faster  |
| scimark_sor                | 107 ms     | 91.0 ms: 1.17x faster  |
| nbody                      | 86.4 ms    | 74.1 ms: 1.17x faster  |
| 2to3                       | 251 ms     | 227 ms: 1.11x faster   |
| bench_thread_pool          | 831 us     | 864 us: 1.04x slower   |
| bench_mp_pool              | 80.9 ms    | 88.7 ms: 1.10x slower  |
| logging_format             | 5.86 us    | 7.03 us: 1.20x slower  |
| logging_simple             | 5.26 us    | 6.53 us: 1.24x slower  |
| python_startup             | 12.7 ms    | 26.1 ms: 2.05x slower  |
| pathlib                    | 14.9 ms    | 32.1 ms: 2.16x slower  |
| python_startup_no_site     | 7.02 ms    | 19.8 ms: 2.83x slower  |
| Geometric mean             | (ref)      | 1.37x faster           |
Ignored benchmarks (2) of TC-PGO-Ex3.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.390x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown