# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.679x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 204 ms: 1.51x faster   |
| docutils       | 2.31 sec | 1.58 sec: 1.46x faster |
| html5lib       | 52.5 ms  | 35.5 ms: 1.48x faster  |
| sphinx         | 933 ms   | 615 ms: 1.52x faster   |
| Geometric mean | (ref)    | 1.49x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 10.8 ms: 2.08x faster |
| async_generators           | 348 ms  | 199 ms: 1.75x faster  |
| async_tree_none            | 267 ms  | 157 ms: 1.70x faster  |
| async_tree_none_tg         | 243 ms  | 150 ms: 1.62x faster  |
| async_tree_io_tg           | 576 ms  | 356 ms: 1.62x faster  |
| async_tree_io              | 570 ms  | 353 ms: 1.61x faster  |
| async_tree_memoization     | 313 ms  | 196 ms: 1.59x faster  |
| async_tree_memoization_tg  | 304 ms  | 201 ms: 1.52x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 327 ms: 1.39x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 325 ms: 1.37x faster  |
| asyncio_websockets         | 330 ms  | 304 ms: 1.08x faster  |
| Geometric mean             | (ref)   | 1.56x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 45.7 ms: 2.26x faster |
| float          | 78.0 ms | 37.1 ms: 2.10x faster |
| pidigits       | 156 ms  | 145 ms: 1.08x faster  |
| Geometric mean | (ref)   | 1.72x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 70.7 ms: 1.84x faster |
| regex_effbot   | 1.87 ms | 1.45 ms: 1.28x faster |
| regex_v8       | 17.5 ms | 13.9 ms: 1.26x faster |
| regex_dna      | 123 ms  | 121 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.32x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 110 us: 2.59x faster   |
| tomli_loads          | 2.07 sec | 1.03 sec: 2.01x faster |
| pickle_pure_python   | 364 us   | 184 us: 1.98x faster   |
| xml_etree_process    | 66.9 ms  | 33.8 ms: 1.98x faster  |
| xml_etree_generate   | 92.6 ms  | 49.4 ms: 1.87x faster  |
| xml_etree_iterparse  | 94.3 ms  | 59.5 ms: 1.58x faster  |
| json_loads           | 23.3 us  | 14.8 us: 1.58x faster  |
| json_dumps           | 9.44 ms  | 6.19 ms: 1.52x faster  |
| xml_etree_parse      | 112 ms   | 89.4 ms: 1.26x faster  |
| Geometric mean       | (ref)    | 1.78x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 24.7 ms: 1.19x faster |
| python_startup_no_site | 22.0 ms | 18.7 ms: 1.18x faster |
| Geometric mean         | (ref)   | 1.18x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 5.80 ms: 2.08x faster |
| genshi_text     | 23.9 ms | 12.3 ms: 1.94x faster |
| django_template | 38.0 ms | 20.9 ms: 1.81x faster |
| genshi_xml      | 50.4 ms | 29.5 ms: 1.71x faster |
| Geometric mean  | (ref)   | 1.88x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 44.1 ns: 2.82x faster  |
| scimark_sor                | 139 ms   | 51.1 ms: 2.71x faster  |
| scimark_lu                 | 119 ms   | 44.3 ms: 2.69x faster  |
| unpickle_pure_python       | 284 us   | 110 us: 2.59x faster   |
| deltablue                  | 4.22 ms  | 1.64 ms: 2.57x faster  |
| generators                 | 35.6 ms  | 14.2 ms: 2.50x faster  |
| hexiom                     | 7.44 ms  | 3.00 ms: 2.49x faster  |
| spectral_norm              | 102 ms   | 40.9 ms: 2.49x faster  |
| scimark_monte_carlo        | 75.8 ms  | 31.5 ms: 2.41x faster  |
| comprehensions             | 20.1 us  | 8.65 us: 2.32x faster  |
| deepcopy_memo              | 34.0 us  | 14.7 us: 2.32x faster  |
| richards                   | 59.0 ms  | 25.5 ms: 2.32x faster  |
| go                         | 140 ms   | 61.0 ms: 2.30x faster  |
| richards_super             | 67.7 ms  | 29.4 ms: 2.30x faster  |
| nbody                      | 103 ms   | 45.7 ms: 2.26x faster  |
| chaos                      | 69.3 ms  | 31.3 ms: 2.22x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.02 ms: 2.19x faster  |
| raytrace                   | 313 ms   | 145 ms: 2.16x faster   |
| float                      | 78.0 ms  | 37.1 ms: 2.10x faster  |
| mako                       | 12.1 ms  | 5.80 ms: 2.08x faster  |
| coroutines                 | 22.4 ms  | 10.8 ms: 2.08x faster  |
| fannkuch                   | 418 ms   | 203 ms: 2.06x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 695 us: 2.02x faster   |
| pyflate                    | 477 ms   | 236 ms: 2.02x faster   |
| tomli_loads                | 2.07 sec | 1.03 sec: 2.01x faster |
| pickle_pure_python         | 364 us   | 184 us: 1.98x faster   |
| crypto_pyaes               | 80.1 ms  | 40.4 ms: 1.98x faster  |
| xml_etree_process          | 66.9 ms  | 33.8 ms: 1.98x faster  |
| scimark_fft                | 276 ms   | 140 ms: 1.97x faster   |
| nqueens                    | 96.9 ms  | 49.7 ms: 1.95x faster  |
| pprint_pformat             | 1.66 sec | 853 ms: 1.95x faster   |
| genshi_text                | 23.9 ms  | 12.3 ms: 1.94x faster  |
| pprint_safe_repr           | 825 ms   | 429 ms: 1.92x faster   |
| deepcopy                   | 278 us   | 147 us: 1.90x faster   |
| deepcopy_reduce            | 2.86 us  | 1.51 us: 1.89x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 894 us: 1.89x faster   |
| xml_etree_generate         | 92.6 ms  | 49.4 ms: 1.87x faster  |
| regex_compile              | 130 ms   | 70.7 ms: 1.84x faster  |
| django_template            | 38.0 ms  | 20.9 ms: 1.81x faster  |
| bpe_tokeniser              | 4.45 sec | 2.52 sec: 1.76x faster |
| async_generators           | 348 ms   | 199 ms: 1.75x faster   |
| sqlglot_v2_normalize       | 109 ms   | 62.6 ms: 1.74x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 30.5 ms: 1.73x faster  |
| logging_simple             | 9.30 us  | 5.42 us: 1.72x faster  |
| typing_runtime_protocols   | 154 us   | 89.7 us: 1.72x faster  |
| genshi_xml                 | 50.4 ms  | 29.5 ms: 1.71x faster  |
| async_tree_none            | 267 ms   | 157 ms: 1.70x faster   |
| logging_format             | 9.92 us  | 5.90 us: 1.68x faster  |
| async_tree_none_tg         | 243 ms   | 150 ms: 1.62x faster   |
| async_tree_io_tg           | 576 ms   | 356 ms: 1.62x faster   |
| sympy_str                  | 247 ms   | 153 ms: 1.61x faster   |
| async_tree_io              | 570 ms   | 353 ms: 1.61x faster   |
| async_tree_memoization     | 313 ms   | 196 ms: 1.59x faster   |
| sympy_expand               | 419 ms   | 263 ms: 1.59x faster   |
| pathlib                    | 37.5 ms  | 23.6 ms: 1.59x faster  |
| xml_etree_iterparse        | 94.3 ms  | 59.5 ms: 1.58x faster  |
| pycparser                  | 1.01 sec | 642 ms: 1.58x faster   |
| json_loads                 | 23.3 us  | 14.8 us: 1.58x faster  |
| gc_traversal               | 3.25 ms  | 2.09 ms: 1.55x faster  |
| thrift                     | 710 us   | 461 us: 1.54x faster   |
| sympy_integrate            | 18.4 ms  | 12.0 ms: 1.54x faster  |
| sympy_sum                  | 123 ms   | 80.7 ms: 1.53x faster  |
| json_dumps                 | 9.44 ms  | 6.19 ms: 1.52x faster  |
| sphinx                     | 933 ms   | 615 ms: 1.52x faster   |
| async_tree_memoization_tg  | 304 ms   | 201 ms: 1.52x faster   |
| 2to3                       | 309 ms   | 204 ms: 1.51x faster   |
| meteor_contest             | 99.5 ms  | 66.6 ms: 1.49x faster  |
| html5lib                   | 52.5 ms  | 35.5 ms: 1.48x faster  |
| telco                      | 6.56 ms  | 4.45 ms: 1.48x faster  |
| docutils                   | 2.31 sec | 1.58 sec: 1.46x faster |
| pylint                     | 269 ms   | 193 ms: 1.40x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 327 ms: 1.39x faster   |
| json                       | 4.07 ms  | 2.95 ms: 1.38x faster  |
| coverage                   | 63.7 ms  | 46.2 ms: 1.38x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 325 ms: 1.37x faster   |
| mdp                        | 1.89 sec | 1.41 sec: 1.34x faster |
| dulwich_log                | 52.4 ms  | 39.1 ms: 1.34x faster  |
| k_core                     | 2.18 sec | 1.67 sec: 1.31x faster |
| regex_effbot               | 1.87 ms  | 1.45 ms: 1.28x faster  |
| shortest_path              | 437 ms   | 347 ms: 1.26x faster   |
| xml_etree_parse            | 112 ms   | 89.4 ms: 1.26x faster  |
| regex_v8                   | 17.5 ms  | 13.9 ms: 1.26x faster  |
| sqlite_synth               | 1.96 us  | 1.56 us: 1.26x faster  |
| connected_components       | 395 ms   | 320 ms: 1.23x faster   |
| python_startup             | 29.5 ms  | 24.7 ms: 1.19x faster  |
| python_startup_no_site     | 22.0 ms  | 18.7 ms: 1.18x faster  |
| create_gc_cycles           | 1.42 ms  | 1.26 ms: 1.12x faster  |
| asyncio_websockets         | 330 ms   | 304 ms: 1.08x faster   |
| pidigits                   | 156 ms   | 145 ms: 1.08x faster   |
| regex_dna                  | 123 ms   | 121 ms: 1.02x faster   |
| many_optionals             | 559 us   | 659 us: 1.18x slower   |
| subparsers                 | 21.5 ms  | 40.6 ms: 1.89x slower  |
| Geometric mean             | (ref)    | 1.69x faster           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.679x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.58x
- 95% likely to have a speedup of 1.56x
- 99% likely to have a speedup of 1.53x

# Memory
- memory change: unknown