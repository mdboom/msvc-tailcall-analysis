# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.700x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.56x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 204 ms: 1.52x faster   |
| docutils       | 2.31 sec | 1.55 sec: 1.49x faster |
| html5lib       | 52.5 ms  | 35.2 ms: 1.49x faster  |
| sphinx         | 933 ms   | 599 ms: 1.56x faster   |
| Geometric mean | (ref)    | 1.51x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 11.1 ms: 2.02x faster |
| async_generators           | 348 ms  | 188 ms: 1.85x faster  |
| async_tree_none            | 267 ms  | 155 ms: 1.72x faster  |
| async_tree_none_tg         | 243 ms  | 147 ms: 1.65x faster  |
| async_tree_memoization     | 313 ms  | 190 ms: 1.65x faster  |
| async_tree_io_tg           | 576 ms  | 352 ms: 1.64x faster  |
| async_tree_io              | 570 ms  | 349 ms: 1.63x faster  |
| async_tree_memoization_tg  | 304 ms  | 195 ms: 1.56x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 309 ms: 1.47x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 310 ms: 1.43x faster  |
| asyncio_websockets         | 330 ms  | 400 ms: 1.21x slower  |
| Geometric mean             | (ref)   | 1.55x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | clang-PGO             |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 38.5 ms: 2.02x faster |
| nbody          | 103 ms  | 52.9 ms: 1.96x faster |
| pidigits       | 156 ms  | 148 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.61x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 73.4 ms: 1.77x faster |
| regex_v8       | 17.5 ms | 13.5 ms: 1.30x faster |
| regex_effbot   | 1.87 ms | 1.65 ms: 1.13x faster |
| regex_dna      | 123 ms  | 121 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.28x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 109 us: 2.61x faster   |
| pickle_pure_python   | 364 us   | 175 us: 2.08x faster   |
| xml_etree_process    | 66.9 ms  | 34.0 ms: 1.97x faster  |
| xml_etree_generate   | 92.6 ms  | 48.4 ms: 1.91x faster  |
| tomli_loads          | 2.07 sec | 1.13 sec: 1.83x faster |
| json_loads           | 23.3 us  | 14.2 us: 1.64x faster  |
| json_dumps           | 9.44 ms  | 5.76 ms: 1.64x faster  |
| xml_etree_iterparse  | 94.3 ms  | 60.7 ms: 1.55x faster  |
| xml_etree_parse      | 112 ms   | 88.8 ms: 1.27x faster  |
| Geometric mean       | (ref)    | 1.80x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | clang-PGO             |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.6 ms: 1.11x faster |
| python_startup_no_site | 22.0 ms | 20.0 ms: 1.10x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 5.72 ms: 2.11x faster |
| genshi_text     | 23.9 ms | 12.0 ms: 2.00x faster |
| django_template | 38.0 ms | 19.5 ms: 1.94x faster |
| genshi_xml      | 50.4 ms | 27.4 ms: 1.84x faster |
| Geometric mean  | (ref)   | 1.97x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 124 ns   | 44.5 ns: 2.80x faster  |
| richards_super             | 67.7 ms  | 24.6 ms: 2.75x faster  |
| richards                   | 59.0 ms  | 21.9 ms: 2.69x faster  |
| deltablue                  | 4.22 ms  | 1.59 ms: 2.65x faster  |
| unpickle_pure_python       | 284 us   | 109 us: 2.61x faster   |
| scimark_lu                 | 119 ms   | 49.1 ms: 2.43x faster  |
| hexiom                     | 7.44 ms  | 3.13 ms: 2.38x faster  |
| scimark_sor                | 139 ms   | 59.1 ms: 2.35x faster  |
| scimark_monte_carlo        | 75.8 ms  | 32.8 ms: 2.31x faster  |
| raytrace                   | 313 ms   | 137 ms: 2.27x faster   |
| spectral_norm              | 102 ms   | 44.7 ms: 2.27x faster  |
| comprehensions             | 20.1 us  | 8.84 us: 2.27x faster  |
| deepcopy_memo              | 34.0 us  | 15.1 us: 2.26x faster  |
| generators                 | 35.6 ms  | 15.8 ms: 2.25x faster  |
| chaos                      | 69.3 ms  | 31.1 ms: 2.23x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.05 ms: 2.16x faster  |
| go                         | 140 ms   | 65.1 ms: 2.16x faster  |
| mako                       | 12.1 ms  | 5.72 ms: 2.11x faster  |
| pickle_pure_python         | 364 us   | 175 us: 2.08x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 686 us: 2.05x faster   |
| crypto_pyaes               | 80.1 ms  | 39.4 ms: 2.03x faster  |
| nqueens                    | 96.9 ms  | 47.7 ms: 2.03x faster  |
| float                      | 78.0 ms  | 38.5 ms: 2.02x faster  |
| coroutines                 | 22.4 ms  | 11.1 ms: 2.02x faster  |
| genshi_text                | 23.9 ms  | 12.0 ms: 2.00x faster  |
| fannkuch                   | 418 ms   | 209 ms: 2.00x faster   |
| xml_etree_process          | 66.9 ms  | 34.0 ms: 1.97x faster  |
| nbody                      | 103 ms   | 52.9 ms: 1.96x faster  |
| pyflate                    | 477 ms   | 245 ms: 1.95x faster   |
| django_template            | 38.0 ms  | 19.5 ms: 1.94x faster  |
| sqlglot_v2_transpile       | 1.69 ms  | 868 us: 1.94x faster   |
| scimark_fft                | 276 ms   | 143 ms: 1.93x faster   |
| deepcopy_reduce            | 2.86 us  | 1.49 us: 1.93x faster  |
| deepcopy                   | 278 us   | 145 us: 1.92x faster   |
| xml_etree_generate         | 92.6 ms  | 48.4 ms: 1.91x faster  |
| pprint_safe_repr           | 825 ms   | 432 ms: 1.91x faster   |
| pprint_pformat             | 1.66 sec | 874 ms: 1.90x faster   |
| async_generators           | 348 ms   | 188 ms: 1.85x faster   |
| genshi_xml                 | 50.4 ms  | 27.4 ms: 1.84x faster  |
| tomli_loads                | 2.07 sec | 1.13 sec: 1.83x faster |
| sqlglot_v2_normalize       | 109 ms   | 59.9 ms: 1.82x faster  |
| typing_runtime_protocols   | 154 us   | 86.2 us: 1.79x faster  |
| bpe_tokeniser              | 4.45 sec | 2.50 sec: 1.78x faster |
| sqlglot_v2_optimize        | 52.8 ms  | 29.8 ms: 1.77x faster  |
| regex_compile              | 130 ms   | 73.4 ms: 1.77x faster  |
| logging_simple             | 9.30 us  | 5.39 us: 1.72x faster  |
| async_tree_none            | 267 ms   | 155 ms: 1.72x faster   |
| logging_format             | 9.92 us  | 5.83 us: 1.70x faster  |
| async_tree_none_tg         | 243 ms   | 147 ms: 1.65x faster   |
| async_tree_memoization     | 313 ms   | 190 ms: 1.65x faster   |
| json_loads                 | 23.3 us  | 14.2 us: 1.64x faster  |
| json_dumps                 | 9.44 ms  | 5.76 ms: 1.64x faster  |
| thrift                     | 710 us   | 434 us: 1.64x faster   |
| async_tree_io_tg           | 576 ms   | 352 ms: 1.64x faster   |
| async_tree_io              | 570 ms   | 349 ms: 1.63x faster   |
| sympy_str                  | 247 ms   | 153 ms: 1.62x faster   |
| sympy_expand               | 419 ms   | 259 ms: 1.62x faster   |
| pycparser                  | 1.01 sec | 637 ms: 1.59x faster   |
| telco                      | 6.56 ms  | 4.20 ms: 1.56x faster  |
| sympy_integrate            | 18.4 ms  | 11.8 ms: 1.56x faster  |
| async_tree_memoization_tg  | 304 ms   | 195 ms: 1.56x faster   |
| sphinx                     | 933 ms   | 599 ms: 1.56x faster   |
| coverage                   | 63.7 ms  | 40.9 ms: 1.56x faster  |
| xml_etree_iterparse        | 94.3 ms  | 60.7 ms: 1.55x faster  |
| sympy_sum                  | 123 ms   | 81.4 ms: 1.52x faster  |
| 2to3                       | 309 ms   | 204 ms: 1.52x faster   |
| subparsers                 | 21.5 ms  | 14.2 ms: 1.51x faster  |
| docutils                   | 2.31 sec | 1.55 sec: 1.49x faster |
| html5lib                   | 52.5 ms  | 35.2 ms: 1.49x faster  |
| pylint                     | 269 ms   | 182 ms: 1.47x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 309 ms: 1.47x faster   |
| mdp                        | 1.89 sec | 1.30 sec: 1.45x faster |
| meteor_contest             | 99.5 ms  | 68.7 ms: 1.45x faster  |
| json                       | 4.07 ms  | 2.83 ms: 1.44x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 310 ms: 1.43x faster   |
| many_optionals             | 559 us   | 405 us: 1.38x faster   |
| k_core                     | 2.18 sec | 1.61 sec: 1.36x faster |
| dulwich_log                | 52.4 ms  | 39.5 ms: 1.33x faster  |
| sqlite_synth               | 1.96 us  | 1.49 us: 1.31x faster  |
| regex_v8                   | 17.5 ms  | 13.5 ms: 1.30x faster  |
| shortest_path              | 437 ms   | 345 ms: 1.27x faster   |
| xml_etree_parse            | 112 ms   | 88.8 ms: 1.27x faster  |
| pathlib                    | 37.5 ms  | 30.4 ms: 1.23x faster  |
| connected_components       | 395 ms   | 325 ms: 1.21x faster   |
| gc_traversal               | 3.25 ms  | 2.79 ms: 1.17x faster  |
| regex_effbot               | 1.87 ms  | 1.65 ms: 1.13x faster  |
| python_startup             | 29.5 ms  | 26.6 ms: 1.11x faster  |
| python_startup_no_site     | 22.0 ms  | 20.0 ms: 1.10x faster  |
| pidigits                   | 156 ms   | 148 ms: 1.05x faster   |
| create_gc_cycles           | 1.42 ms  | 1.37 ms: 1.03x faster  |
| regex_dna                  | 123 ms   | 121 ms: 1.02x faster   |
| asyncio_websockets         | 330 ms   | 400 ms: 1.21x slower   |
| Geometric mean             | (ref)    | 1.71x faster           |
Ignored benchmarks (2) of Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.700x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.61x
- 95% likely to have a speedup of 1.59x
- 99% likely to have a speedup of 1.56x

# Memory
- memory change: unknown