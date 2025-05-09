# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.270x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | Ex                     |
|----------------|:--------:|:----------------------:|
| 2to3           | 237 ms   | 309 ms: 1.30x slower   |
| docutils       | 1.81 sec | 2.31 sec: 1.27x slower |
| html5lib       | 40.8 ms  | 52.5 ms: 1.29x slower  |
| sphinx         | 723 ms   | 933 ms: 1.29x slower   |
| Geometric mean | (ref)    | 1.29x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | Ex                    |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 304 ms  | 330 ms: 1.09x slower  |
| async_tree_cpu_io_mixed_tg | 367 ms  | 444 ms: 1.21x slower  |
| async_tree_cpu_io_mixed    | 362 ms  | 455 ms: 1.26x slower  |
| async_tree_io              | 429 ms  | 570 ms: 1.33x slower  |
| async_tree_none_tg         | 178 ms  | 243 ms: 1.37x slower  |
| async_tree_io_tg           | 419 ms  | 576 ms: 1.37x slower  |
| async_tree_memoization     | 227 ms  | 313 ms: 1.38x slower  |
| async_tree_memoization_tg  | 218 ms  | 304 ms: 1.40x slower  |
| async_tree_none            | 188 ms  | 267 ms: 1.42x slower  |
| async_generators           | 224 ms  | 348 ms: 1.56x slower  |
| coroutines                 | 13.5 ms | 22.4 ms: 1.67x slower |
| Geometric mean             | (ref)   | 1.36x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | Ex                    |
|----------------|:-------:|:---------------------:|
| pidigits       | 147 ms  | 156 ms: 1.07x slower  |
| float          | 44.8 ms | 78.0 ms: 1.74x slower |
| nbody          | 58.8 ms | 103 ms: 1.76x slower  |
| Geometric mean | (ref)   | 1.48x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | Ex                    |
|----------------|:-------:|:---------------------:|
| regex_dna      | 117 ms  | 123 ms: 1.05x slower  |
| regex_v8       | 16.7 ms | 17.5 ms: 1.05x slower |
| regex_effbot   | 1.76 ms | 1.87 ms: 1.06x slower |
| regex_compile  | 88.0 ms | 130 ms: 1.48x slower  |
| Geometric mean | (ref)   | 1.15x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | Ex                     |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 104 ms   | 112 ms: 1.09x slower   |
| json_loads           | 21.1 us  | 23.3 us: 1.10x slower  |
| json_dumps           | 7.94 ms  | 9.44 ms: 1.19x slower  |
| xml_etree_iterparse  | 71.5 ms  | 94.3 ms: 1.32x slower  |
| xml_etree_generate   | 66.8 ms  | 92.6 ms: 1.39x slower  |
| xml_etree_process    | 46.5 ms  | 66.9 ms: 1.44x slower  |
| tomli_loads          | 1.38 sec | 2.07 sec: 1.50x slower |
| pickle_pure_python   | 236 us   | 364 us: 1.55x slower   |
| unpickle_pure_python | 154 us   | 284 us: 1.85x slower   |
| Geometric mean       | (ref)    | 1.36x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | Ex                    |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.1 ms | 22.0 ms: 1.09x slower |
| python_startup         | 26.9 ms | 29.5 ms: 1.10x slower |
| Geometric mean         | (ref)   | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | Ex                    |
|-----------------|:-------:|:---------------------:|
| django_template | 27.5 ms | 38.0 ms: 1.38x slower |
| genshi_xml      | 35.3 ms | 50.4 ms: 1.43x slower |
| genshi_text     | 16.2 ms | 23.9 ms: 1.48x slower |
| mako            | 7.44 ms | 12.1 ms: 1.62x slower |
| Geometric mean  | (ref)   | 1.48x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | Ex                     |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 47.1 ms  | 21.5 ms: 2.19x faster  |
| many_optionals             | 813 us   | 559 us: 1.45x faster   |
| create_gc_cycles           | 1.38 ms  | 1.42 ms: 1.02x slower  |
| regex_dna                  | 117 ms   | 123 ms: 1.05x slower   |
| regex_v8                   | 16.7 ms  | 17.5 ms: 1.05x slower  |
| regex_effbot               | 1.76 ms  | 1.87 ms: 1.06x slower  |
| bench_mp_pool              | 95.0 ms  | 101 ms: 1.06x slower   |
| pidigits                   | 147 ms   | 156 ms: 1.07x slower   |
| json                       | 3.77 ms  | 4.07 ms: 1.08x slower  |
| xml_etree_parse            | 104 ms   | 112 ms: 1.09x slower   |
| asyncio_websockets         | 304 ms   | 330 ms: 1.09x slower   |
| python_startup_no_site     | 20.1 ms  | 22.0 ms: 1.09x slower  |
| python_startup             | 26.9 ms  | 29.5 ms: 1.10x slower  |
| json_loads                 | 21.1 us  | 23.3 us: 1.10x slower  |
| coverage                   | 56.4 ms  | 63.7 ms: 1.13x slower  |
| sqlite_synth               | 1.68 us  | 1.96 us: 1.16x slower  |
| gc_traversal               | 2.77 ms  | 3.25 ms: 1.17x slower  |
| json_dumps                 | 7.94 ms  | 9.44 ms: 1.19x slower  |
| mdp                        | 1.57 sec | 1.89 sec: 1.20x slower |
| async_tree_cpu_io_mixed_tg | 367 ms   | 444 ms: 1.21x slower   |
| connected_components       | 326 ms   | 395 ms: 1.21x slower   |
| dulwich_log                | 43.0 ms  | 52.4 ms: 1.22x slower  |
| shortest_path              | 357 ms   | 437 ms: 1.22x slower   |
| telco                      | 5.33 ms  | 6.56 ms: 1.23x slower  |
| pylint                     | 217 ms   | 269 ms: 1.24x slower   |
| k_core                     | 1.76 sec | 2.18 sec: 1.24x slower |
| async_tree_cpu_io_mixed    | 362 ms   | 455 ms: 1.26x slower   |
| thrift                     | 561 us   | 710 us: 1.27x slower   |
| docutils                   | 1.81 sec | 2.31 sec: 1.27x slower |
| meteor_contest             | 78.1 ms  | 99.5 ms: 1.27x slower  |
| sympy_sum                  | 96.6 ms  | 123 ms: 1.28x slower   |
| html5lib                   | 40.8 ms  | 52.5 ms: 1.29x slower  |
| sphinx                     | 723 ms   | 933 ms: 1.29x slower   |
| sympy_expand               | 324 ms   | 419 ms: 1.29x slower   |
| 2to3                       | 237 ms   | 309 ms: 1.30x slower   |
| xml_etree_iterparse        | 71.5 ms  | 94.3 ms: 1.32x slower  |
| sympy_str                  | 187 ms   | 247 ms: 1.33x slower   |
| pycparser                  | 765 ms   | 1.01 sec: 1.33x slower |
| async_tree_io              | 429 ms   | 570 ms: 1.33x slower   |
| sympy_integrate            | 13.9 ms  | 18.4 ms: 1.33x slower  |
| deepcopy_reduce            | 2.12 us  | 2.86 us: 1.35x slower  |
| typing_runtime_protocols   | 113 us   | 154 us: 1.37x slower   |
| async_tree_none_tg         | 178 ms   | 243 ms: 1.37x slower   |
| async_tree_io_tg           | 419 ms   | 576 ms: 1.37x slower   |
| sqlglot_v2_optimize        | 38.4 ms  | 52.8 ms: 1.38x slower  |
| async_tree_memoization     | 227 ms   | 313 ms: 1.38x slower   |
| logging_format             | 7.18 us  | 9.92 us: 1.38x slower  |
| sqlglot_v2_normalize       | 79.0 ms  | 109 ms: 1.38x slower   |
| django_template            | 27.5 ms  | 38.0 ms: 1.38x slower  |
| xml_etree_generate         | 66.8 ms  | 92.6 ms: 1.39x slower  |
| logging_simple             | 6.67 us  | 9.30 us: 1.39x slower  |
| async_tree_memoization_tg  | 218 ms   | 304 ms: 1.40x slower   |
| deepcopy                   | 199 us   | 278 us: 1.40x slower   |
| bpe_tokeniser              | 3.17 sec | 4.45 sec: 1.40x slower |
| bench_thread_pool          | 906 us   | 1.28 ms: 1.41x slower  |
| async_tree_none            | 188 ms   | 267 ms: 1.42x slower   |
| genshi_xml                 | 35.3 ms  | 50.4 ms: 1.43x slower  |
| xml_etree_process          | 46.5 ms  | 66.9 ms: 1.44x slower  |
| pathlib                    | 25.6 ms  | 37.5 ms: 1.47x slower  |
| pprint_pformat             | 1.13 sec | 1.66 sec: 1.47x slower |
| nqueens                    | 65.7 ms  | 96.9 ms: 1.47x slower  |
| regex_compile              | 88.0 ms  | 130 ms: 1.48x slower   |
| pprint_safe_repr           | 558 ms   | 825 ms: 1.48x slower   |
| genshi_text                | 16.2 ms  | 23.9 ms: 1.48x slower  |
| tomli_loads                | 1.38 sec | 2.07 sec: 1.50x slower |
| sqlglot_v2_transpile       | 1.09 ms  | 1.69 ms: 1.54x slower  |
| pickle_pure_python         | 236 us   | 364 us: 1.55x slower   |
| scimark_fft                | 178 ms   | 276 ms: 1.55x slower   |
| async_generators           | 224 ms   | 348 ms: 1.56x slower   |
| fannkuch                   | 265 ms   | 418 ms: 1.58x slower   |
| deepcopy_memo              | 21.3 us  | 34.0 us: 1.60x slower  |
| sqlglot_v2_parse           | 876 us   | 1.41 ms: 1.60x slower  |
| pyflate                    | 295 ms   | 477 ms: 1.62x slower   |
| mako                       | 7.44 ms  | 12.1 ms: 1.62x slower  |
| crypto_pyaes               | 49.3 ms  | 80.1 ms: 1.62x slower  |
| comprehensions             | 12.2 us  | 20.1 us: 1.64x slower  |
| coroutines                 | 13.5 ms  | 22.4 ms: 1.67x slower  |
| chaos                      | 41.4 ms  | 69.3 ms: 1.67x slower  |
| raytrace                   | 187 ms   | 313 ms: 1.67x slower   |
| richards_super             | 40.4 ms  | 67.7 ms: 1.68x slower  |
| richards                   | 35.0 ms  | 59.0 ms: 1.69x slower  |
| spectral_norm              | 58.4 ms  | 102 ms: 1.74x slower   |
| float                      | 44.8 ms  | 78.0 ms: 1.74x slower  |
| nbody                      | 58.8 ms  | 103 ms: 1.76x slower   |
| scimark_monte_carlo        | 42.9 ms  | 75.8 ms: 1.77x slower  |
| hexiom                     | 4.17 ms  | 7.44 ms: 1.79x slower  |
| scimark_sparse_mat_mult    | 2.48 ms  | 4.43 ms: 1.79x slower  |
| go                         | 78.0 ms  | 140 ms: 1.80x slower   |
| scimark_lu                 | 65.2 ms  | 119 ms: 1.83x slower   |
| unpickle_pure_python       | 154 us   | 284 us: 1.85x slower   |
| scimark_sor                | 73.9 ms  | 139 ms: 1.88x slower   |
| generators                 | 18.1 ms  | 35.6 ms: 1.97x slower  |
| logging_silent             | 62.9 ns  | 124 ns: 1.97x slower   |
| deltablue                  | 2.09 ms  | 4.22 ms: 2.02x slower  |
| Geometric mean             | (ref)    | 1.37x slower           |

- Geometric mean (including insignificant results): 1.270x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.32x
- 95% likely to have a slowdown of 1.32x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: unknown