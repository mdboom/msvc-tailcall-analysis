# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.613x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 204 ms: 1.46x faster   |
| docutils       | 2.17 sec | 1.58 sec: 1.37x faster |
| html5lib       | 51.3 ms  | 35.5 ms: 1.45x faster  |
| sphinx         | 872 ms   | 615 ms: 1.42x faster   |
| Geometric mean | (ref)    | 1.42x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 10.8 ms: 2.03x faster |
| async_generators           | 328 ms  | 199 ms: 1.65x faster  |
| async_tree_none            | 249 ms  | 157 ms: 1.59x faster  |
| async_tree_none_tg         | 236 ms  | 150 ms: 1.58x faster  |
| async_tree_io_tg           | 559 ms  | 356 ms: 1.57x faster  |
| async_tree_io              | 553 ms  | 353 ms: 1.56x faster  |
| async_tree_memoization     | 297 ms  | 196 ms: 1.52x faster  |
| async_tree_memoization_tg  | 291 ms  | 201 ms: 1.45x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 327 ms: 1.34x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 325 ms: 1.31x faster  |
| asyncio_websockets         | 317 ms  | 304 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.49x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 45.7 ms: 2.20x faster |
| float          | 75.4 ms | 37.1 ms: 2.03x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.67x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 70.7 ms: 1.76x faster |
| regex_effbot   | 1.81 ms | 1.45 ms: 1.25x faster |
| regex_v8       | 17.1 ms | 13.9 ms: 1.23x faster |
| Geometric mean | (ref)   | 1.28x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 110 us: 2.50x faster   |
| tomli_loads          | 1.99 sec | 1.03 sec: 1.94x faster |
| pickle_pure_python   | 355 us   | 184 us: 1.93x faster   |
| xml_etree_process    | 64.6 ms  | 33.8 ms: 1.91x faster  |
| xml_etree_generate   | 89.5 ms  | 49.4 ms: 1.81x faster  |
| json_loads           | 22.3 us  | 14.8 us: 1.51x faster  |
| xml_etree_iterparse  | 89.9 ms  | 59.5 ms: 1.51x faster  |
| json_dumps           | 9.01 ms  | 6.19 ms: 1.45x faster  |
| xml_etree_parse      | 108 ms   | 89.4 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.72x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 24.7 ms: 1.11x faster |
| python_startup_no_site | 20.4 ms | 18.7 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 5.80 ms: 2.02x faster |
| genshi_text     | 23.2 ms | 12.3 ms: 1.88x faster |
| django_template | 36.9 ms | 20.9 ms: 1.76x faster |
| genshi_xml      | 48.8 ms | 29.5 ms: 1.66x faster |
| Geometric mean  | (ref)   | 1.82x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 44.1 ns: 2.71x faster  |
| scimark_sor                | 135 ms   | 51.1 ms: 2.64x faster  |
| scimark_lu                 | 116 ms   | 44.3 ms: 2.62x faster  |
| unpickle_pure_python       | 274 us   | 110 us: 2.50x faster   |
| deltablue                  | 4.09 ms  | 1.64 ms: 2.49x faster  |
| hexiom                     | 7.27 ms  | 3.00 ms: 2.43x faster  |
| spectral_norm              | 97.7 ms  | 40.9 ms: 2.39x faster  |
| generators                 | 33.8 ms  | 14.2 ms: 2.37x faster  |
| scimark_monte_carlo        | 73.9 ms  | 31.5 ms: 2.35x faster  |
| richards                   | 57.8 ms  | 25.5 ms: 2.27x faster  |
| go                         | 137 ms   | 61.0 ms: 2.25x faster  |
| deepcopy_memo              | 32.9 us  | 14.7 us: 2.24x faster  |
| comprehensions             | 19.4 us  | 8.65 us: 2.24x faster  |
| richards_super             | 65.8 ms  | 29.4 ms: 2.23x faster  |
| nbody                      | 101 ms   | 45.7 ms: 2.20x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.02 ms: 2.15x faster  |
| raytrace                   | 304 ms   | 145 ms: 2.09x faster   |
| chaos                      | 65.2 ms  | 31.3 ms: 2.09x faster  |
| float                      | 75.4 ms  | 37.1 ms: 2.03x faster  |
| coroutines                 | 21.9 ms  | 10.8 ms: 2.03x faster  |
| mako                       | 11.7 ms  | 5.80 ms: 2.02x faster  |
| fannkuch                   | 407 ms   | 203 ms: 2.01x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 695 us: 1.96x faster   |
| pyflate                    | 462 ms   | 236 ms: 1.96x faster   |
| tomli_loads                | 1.99 sec | 1.03 sec: 1.94x faster |
| pickle_pure_python         | 355 us   | 184 us: 1.93x faster   |
| crypto_pyaes               | 77.9 ms  | 40.4 ms: 1.93x faster  |
| scimark_fft                | 269 ms   | 140 ms: 1.91x faster   |
| xml_etree_process          | 64.6 ms  | 33.8 ms: 1.91x faster  |
| nqueens                    | 94.3 ms  | 49.7 ms: 1.90x faster  |
| pprint_pformat             | 1.61 sec | 853 ms: 1.89x faster   |
| genshi_text                | 23.2 ms  | 12.3 ms: 1.88x faster  |
| deepcopy                   | 269 us   | 147 us: 1.84x faster   |
| pprint_safe_repr           | 788 ms   | 429 ms: 1.84x faster   |
| sqlglot_v2_transpile       | 1.64 ms  | 894 us: 1.83x faster   |
| deepcopy_reduce            | 2.77 us  | 1.51 us: 1.83x faster  |
| xml_etree_generate         | 89.5 ms  | 49.4 ms: 1.81x faster  |
| regex_compile              | 125 ms   | 70.7 ms: 1.76x faster  |
| django_template            | 36.9 ms  | 20.9 ms: 1.76x faster  |
| bpe_tokeniser              | 4.30 sec | 2.52 sec: 1.71x faster |
| sqlglot_v2_normalize       | 106 ms   | 62.6 ms: 1.70x faster  |
| typing_runtime_protocols   | 150 us   | 89.7 us: 1.68x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 30.5 ms: 1.67x faster  |
| genshi_xml                 | 48.8 ms  | 29.5 ms: 1.66x faster  |
| async_generators           | 328 ms   | 199 ms: 1.65x faster   |
| logging_simple             | 8.87 us  | 5.42 us: 1.64x faster  |
| async_tree_none            | 249 ms   | 157 ms: 1.59x faster   |
| logging_format             | 9.33 us  | 5.90 us: 1.58x faster  |
| async_tree_none_tg         | 236 ms   | 150 ms: 1.58x faster   |
| async_tree_io_tg           | 559 ms   | 356 ms: 1.57x faster   |
| async_tree_io              | 553 ms   | 353 ms: 1.56x faster   |
| sympy_str                  | 238 ms   | 153 ms: 1.55x faster   |
| pycparser                  | 992 ms   | 642 ms: 1.54x faster   |
| sympy_expand               | 405 ms   | 263 ms: 1.54x faster   |
| async_tree_memoization     | 297 ms   | 196 ms: 1.52x faster   |
| json_loads                 | 22.3 us  | 14.8 us: 1.51x faster  |
| xml_etree_iterparse        | 89.9 ms  | 59.5 ms: 1.51x faster  |
| gc_traversal               | 3.15 ms  | 2.09 ms: 1.51x faster  |
| thrift                     | 694 us   | 461 us: 1.50x faster   |
| sympy_integrate            | 17.8 ms  | 12.0 ms: 1.48x faster  |
| sympy_sum                  | 119 ms   | 80.7 ms: 1.48x faster  |
| 2to3                       | 298 ms   | 204 ms: 1.46x faster   |
| pathlib                    | 34.4 ms  | 23.6 ms: 1.46x faster  |
| json_dumps                 | 9.01 ms  | 6.19 ms: 1.45x faster  |
| async_tree_memoization_tg  | 291 ms   | 201 ms: 1.45x faster   |
| telco                      | 6.44 ms  | 4.45 ms: 1.45x faster  |
| html5lib                   | 51.3 ms  | 35.5 ms: 1.45x faster  |
| meteor_contest             | 95.9 ms  | 66.6 ms: 1.44x faster  |
| sphinx                     | 872 ms   | 615 ms: 1.42x faster   |
| docutils                   | 2.17 sec | 1.58 sec: 1.37x faster |
| json                       | 3.96 ms  | 2.95 ms: 1.34x faster  |
| coverage                   | 61.9 ms  | 46.2 ms: 1.34x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 327 ms: 1.34x faster   |
| pylint                     | 253 ms   | 193 ms: 1.31x faster   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 325 ms: 1.31x faster   |
| dulwich_log                | 51.0 ms  | 39.1 ms: 1.31x faster  |
| mdp                        | 1.81 sec | 1.41 sec: 1.29x faster |
| regex_effbot               | 1.81 ms  | 1.45 ms: 1.25x faster  |
| regex_v8                   | 17.1 ms  | 13.9 ms: 1.23x faster  |
| xml_etree_parse            | 108 ms   | 89.4 ms: 1.21x faster  |
| sqlite_synth               | 1.84 us  | 1.56 us: 1.18x faster  |
| create_gc_cycles           | 1.40 ms  | 1.26 ms: 1.11x faster  |
| python_startup             | 27.3 ms  | 24.7 ms: 1.11x faster  |
| k_core                     | 1.83 sec | 1.67 sec: 1.10x faster |
| python_startup_no_site     | 20.4 ms  | 18.7 ms: 1.09x faster  |
| shortest_path              | 378 ms   | 347 ms: 1.09x faster   |
| connected_components       | 347 ms   | 320 ms: 1.08x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| asyncio_websockets         | 317 ms   | 304 ms: 1.04x faster   |
| many_optionals             | 547 us   | 659 us: 1.20x slower   |
| subparsers                 | 20.8 ms  | 40.6 ms: 1.95x slower  |
| Geometric mean             | (ref)    | 1.62x faster           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.613x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.52x
- 95% likely to have a speedup of 1.50x
- 99% likely to have a speedup of 1.46x

# Memory
- memory change: unknown