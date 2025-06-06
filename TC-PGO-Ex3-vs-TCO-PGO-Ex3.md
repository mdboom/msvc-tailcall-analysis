# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.339x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 251 ms: 1.19x slower   |
| docutils       | 1.67 sec    | 2.61 sec: 1.56x slower |
| html5lib       | 37.9 ms     | 57.3 ms: 1.51x slower  |
| sphinx         | 645 ms      | 1.00 sec: 1.55x slower |
| Geometric mean | (ref)       | 1.45x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------------------|:-----------:|:---------------------:|
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower  |
| async_tree_memoization_tg  | 208 ms      | 307 ms: 1.47x slower  |
| async_tree_memoization     | 206 ms      | 306 ms: 1.49x slower  |
| async_tree_none_tg         | 159 ms      | 242 ms: 1.52x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 504 ms: 1.53x slower  |
| async_tree_io              | 384 ms      | 596 ms: 1.55x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 517 ms: 1.56x slower  |
| async_tree_io_tg           | 377 ms      | 606 ms: 1.61x slower  |
| async_generators           | 202 ms      | 368 ms: 1.82x slower  |
| asyncio_websockets         | 301 ms      | 551 ms: 1.83x slower  |
| coroutines                 | 11.9 ms     | 22.1 ms: 1.85x slower |
| Geometric mean             | (ref)       | 1.60x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 219 ms: 1.51x slower  |
| nbody          | 55.2 ms     | 86.4 ms: 1.57x slower |
| float          | 41.9 ms     | 66.8 ms: 1.59x slower |
| Geometric mean | (ref)       | 1.56x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 78.1 ms     | 125 ms: 1.60x slower  |
| regex_dna      | 120 ms      | 196 ms: 1.63x slower  |
| regex_v8       | 13.2 ms     | 23.8 ms: 1.80x slower |
| regex_effbot   | 1.46 ms     | 3.28 ms: 2.24x slower |
| Geometric mean | (ref)       | 1.80x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------------|:-----------:|:----------------------:|
| pickle_pure_python   | 199 us      | 306 us: 1.54x slower   |
| xml_etree_process    | 37.0 ms     | 58.7 ms: 1.59x slower  |
| tomli_loads          | 1.18 sec    | 1.88 sec: 1.60x slower |
| xml_etree_generate   | 53.6 ms     | 86.8 ms: 1.62x slower  |
| xml_etree_iterparse  | 61.2 ms     | 103 ms: 1.68x slower   |
| unpickle_pure_python | 127 us      | 217 us: 1.71x slower   |
| xml_etree_parse      | 89.3 ms     | 163 ms: 1.82x slower   |
| json_dumps           | 6.55 ms     | 12.5 ms: 1.90x slower  |
| json_loads           | 14.7 us     | 28.9 us: 1.96x slower  |
| Geometric mean       | (ref)       | 1.71x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 7.02 ms: 2.67x faster |
| python_startup         | 24.7 ms     | 12.7 ms: 1.94x faster |
| Geometric mean         | (ref)       | 2.28x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|-----------------|:-----------:|:---------------------:|
| django_template | 22.9 ms     | 30.6 ms: 1.34x slower |
| genshi_xml      | 32.8 ms     | 48.1 ms: 1.47x slower |
| genshi_text     | 14.3 ms     | 21.2 ms: 1.49x slower |
| mako            | 6.28 ms     | 11.6 ms: 1.85x slower |
| Geometric mean  | (ref)       | 1.52x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------------------|:-----------:|:----------------------:|
| python_startup_no_site     | 18.7 ms     | 7.02 ms: 2.67x faster  |
| subparsers                 | 40.7 ms     | 20.2 ms: 2.02x faster  |
| python_startup             | 24.7 ms     | 12.7 ms: 1.94x faster  |
| pathlib                    | 24.1 ms     | 14.9 ms: 1.62x faster  |
| logging_simple             | 5.97 us     | 5.26 us: 1.14x faster  |
| logging_format             | 6.50 us     | 5.86 us: 1.11x faster  |
| 2to3                       | 212 ms      | 251 ms: 1.19x slower   |
| k_core                     | 1.71 sec    | 2.27 sec: 1.33x slower |
| django_template            | 22.9 ms     | 30.6 ms: 1.34x slower  |
| shortest_path              | 353 ms      | 480 ms: 1.36x slower   |
| connected_components       | 326 ms      | 445 ms: 1.37x slower   |
| pylint                     | 198 ms      | 275 ms: 1.39x slower   |
| nqueens                    | 54.4 ms     | 75.4 ms: 1.39x slower  |
| many_optionals             | 665 us      | 924 us: 1.39x slower   |
| chaos                      | 36.9 ms     | 53.3 ms: 1.45x slower  |
| deepcopy                   | 167 us      | 244 us: 1.46x slower   |
| async_tree_none            | 170 ms      | 249 ms: 1.47x slower   |
| genshi_xml                 | 32.8 ms     | 48.1 ms: 1.47x slower  |
| sympy_integrate            | 12.8 ms     | 18.9 ms: 1.47x slower  |
| async_tree_memoization_tg  | 208 ms      | 307 ms: 1.47x slower   |
| genshi_text                | 14.3 ms     | 21.2 ms: 1.49x slower  |
| async_tree_memoization     | 206 ms      | 306 ms: 1.49x slower   |
| deepcopy_reduce            | 1.70 us     | 2.53 us: 1.49x slower  |
| typing_runtime_protocols   | 98.8 us     | 148 us: 1.49x slower   |
| sqlglot_v2_normalize       | 69.3 ms     | 104 ms: 1.51x slower   |
| html5lib                   | 37.9 ms     | 57.3 ms: 1.51x slower  |
| pidigits                   | 145 ms      | 219 ms: 1.51x slower   |
| async_tree_none_tg         | 159 ms      | 242 ms: 1.52x slower   |
| pyflate                    | 268 ms      | 410 ms: 1.53x slower   |
| thrift                     | 482 us      | 737 us: 1.53x slower   |
| crypto_pyaes               | 47.4 ms     | 72.5 ms: 1.53x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 504 ms: 1.53x slower   |
| pickle_pure_python         | 199 us      | 306 us: 1.54x slower   |
| dulwich_log                | 40.2 ms     | 61.8 ms: 1.54x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.50 ms: 1.54x slower  |
| async_tree_io              | 384 ms      | 596 ms: 1.55x slower   |
| sphinx                     | 645 ms      | 1.00 sec: 1.55x slower |
| pprint_pformat             | 967 ms      | 1.51 sec: 1.56x slower |
| sympy_expand               | 282 ms      | 440 ms: 1.56x slower   |
| sqlglot_v2_parse           | 766 us      | 1.20 ms: 1.56x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 517 ms: 1.56x slower   |
| docutils                   | 1.67 sec    | 2.61 sec: 1.56x slower |
| pprint_safe_repr           | 470 ms      | 736 ms: 1.56x slower   |
| nbody                      | 55.2 ms     | 86.4 ms: 1.57x slower  |
| sympy_str                  | 164 ms      | 258 ms: 1.57x slower   |
| comprehensions             | 9.87 us     | 15.5 us: 1.57x slower  |
| meteor_contest             | 70.2 ms     | 111 ms: 1.58x slower   |
| sqlglot_v2_optimize        | 33.0 ms     | 52.2 ms: 1.58x slower  |
| xml_etree_process          | 37.0 ms     | 58.7 ms: 1.59x slower  |
| raytrace                   | 160 ms      | 255 ms: 1.59x slower   |
| go                         | 70.9 ms     | 113 ms: 1.59x slower   |
| float                      | 41.9 ms     | 66.8 ms: 1.59x slower  |
| regex_compile              | 78.1 ms     | 125 ms: 1.60x slower   |
| tomli_loads                | 1.18 sec    | 1.88 sec: 1.60x slower |
| deltablue                  | 1.88 ms     | 3.01 ms: 1.60x slower  |
| async_tree_io_tg           | 377 ms      | 606 ms: 1.61x slower   |
| bpe_tokeniser              | 2.72 sec    | 4.39 sec: 1.61x slower |
| telco                      | 4.57 ms     | 7.39 ms: 1.62x slower  |
| xml_etree_generate         | 53.6 ms     | 86.8 ms: 1.62x slower  |
| hexiom                     | 3.54 ms     | 5.74 ms: 1.62x slower  |
| regex_dna                  | 120 ms      | 196 ms: 1.63x slower   |
| mdp                        | 1.62 sec    | 2.65 sec: 1.63x slower |
| richards                   | 28.7 ms     | 47.4 ms: 1.65x slower  |
| coverage                   | 48.2 ms     | 79.6 ms: 1.65x slower  |
| sympy_sum                  | 86.3 ms     | 143 ms: 1.65x slower   |
| spectral_norm              | 49.4 ms     | 82.5 ms: 1.67x slower  |
| scimark_monte_carlo        | 36.0 ms     | 60.1 ms: 1.67x slower  |
| xml_etree_iterparse        | 61.2 ms     | 103 ms: 1.68x slower   |
| richards_super             | 33.1 ms     | 55.6 ms: 1.68x slower  |
| pycparser                  | 686 ms      | 1.16 sec: 1.68x slower |
| sqlite_synth               | 1.56 us     | 2.66 us: 1.70x slower  |
| unpickle_pure_python       | 127 us      | 217 us: 1.71x slower   |
| generators                 | 16.5 ms     | 28.6 ms: 1.73x slower  |
| scimark_sor                | 61.1 ms     | 107 ms: 1.74x slower   |
| logging_silent             | 49.4 ns     | 87.1 ns: 1.76x slower  |
| fannkuch                   | 223 ms      | 393 ms: 1.77x slower   |
| deepcopy_memo              | 16.6 us     | 29.4 us: 1.77x slower  |
| json                       | 2.97 ms     | 5.28 ms: 1.78x slower  |
| regex_v8                   | 13.2 ms     | 23.8 ms: 1.80x slower  |
| async_generators           | 202 ms      | 368 ms: 1.82x slower   |
| xml_etree_parse            | 89.3 ms     | 163 ms: 1.82x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 4.14 ms: 1.83x slower  |
| asyncio_websockets         | 301 ms      | 551 ms: 1.83x slower   |
| mako                       | 6.28 ms     | 11.6 ms: 1.85x slower  |
| coroutines                 | 11.9 ms     | 22.1 ms: 1.85x slower  |
| scimark_fft                | 154 ms      | 289 ms: 1.88x slower   |
| json_dumps                 | 6.55 ms     | 12.5 ms: 1.90x slower  |
| json_loads                 | 14.7 us     | 28.9 us: 1.96x slower  |
| create_gc_cycles           | 1.27 ms     | 2.54 ms: 1.99x slower  |
| scimark_lu                 | 50.9 ms     | 107 ms: 2.10x slower   |
| regex_effbot               | 1.46 ms     | 3.28 ms: 2.24x slower  |
| gc_traversal               | 2.11 ms     | 4.97 ms: 2.36x slower  |
| Geometric mean             | (ref)       | 1.51x slower           |
Ignored benchmarks (4) of TC-PGO-Ex3.json: bench_mp_pool, bench_thread_pool, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.339x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.55x
- 95% likely to have a slowdown of 1.54x
- 99% likely to have a slowdown of 1.53x

# Memory
- memory change: unknown