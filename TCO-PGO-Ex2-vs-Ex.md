# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.371x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | TCO-PGO-Ex2            |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 237 ms: 1.30x faster   |
| docutils       | 2.31 sec | 1.81 sec: 1.27x faster |
| html5lib       | 52.5 ms  | 40.8 ms: 1.29x faster  |
| sphinx         | 933 ms   | 723 ms: 1.29x faster   |
| Geometric mean | (ref)    | 1.29x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | TCO-PGO-Ex2           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 13.5 ms: 1.67x faster |
| async_generators           | 348 ms  | 224 ms: 1.56x faster  |
| async_tree_none            | 267 ms  | 188 ms: 1.42x faster  |
| async_tree_memoization_tg  | 304 ms  | 218 ms: 1.40x faster  |
| async_tree_memoization     | 313 ms  | 227 ms: 1.38x faster  |
| async_tree_io_tg           | 576 ms  | 419 ms: 1.37x faster  |
| async_tree_none_tg         | 243 ms  | 178 ms: 1.37x faster  |
| async_tree_io              | 570 ms  | 429 ms: 1.33x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 362 ms: 1.26x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 367 ms: 1.21x faster  |
| asyncio_websockets         | 330 ms  | 304 ms: 1.09x faster  |
| Geometric mean             | (ref)   | 1.36x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| nbody          | 103 ms  | 58.8 ms: 1.76x faster |
| float          | 78.0 ms | 44.8 ms: 1.74x faster |
| pidigits       | 156 ms  | 147 ms: 1.07x faster  |
| Geometric mean | (ref)   | 1.48x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 88.0 ms: 1.48x faster |
| regex_effbot   | 1.87 ms | 1.76 ms: 1.06x faster |
| regex_v8       | 17.5 ms | 16.7 ms: 1.05x faster |
| regex_dna      | 123 ms  | 117 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.15x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | TCO-PGO-Ex2            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 154 us: 1.85x faster   |
| pickle_pure_python   | 364 us   | 236 us: 1.55x faster   |
| tomli_loads          | 2.07 sec | 1.38 sec: 1.50x faster |
| xml_etree_process    | 66.9 ms  | 46.5 ms: 1.44x faster  |
| xml_etree_generate   | 92.6 ms  | 66.8 ms: 1.39x faster  |
| xml_etree_iterparse  | 94.3 ms  | 71.5 ms: 1.32x faster  |
| json_dumps           | 9.44 ms  | 7.94 ms: 1.19x faster  |
| json_loads           | 23.3 us  | 21.1 us: 1.10x faster  |
| xml_etree_parse      | 112 ms   | 104 ms: 1.09x faster   |
| Geometric mean       | (ref)    | 1.36x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | TCO-PGO-Ex2           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.9 ms: 1.10x faster |
| python_startup_no_site | 22.0 ms | 20.1 ms: 1.09x faster |
| Geometric mean         | (ref)   | 1.10x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | TCO-PGO-Ex2           |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 7.44 ms: 1.62x faster |
| genshi_text     | 23.9 ms | 16.2 ms: 1.48x faster |
| genshi_xml      | 50.4 ms | 35.3 ms: 1.43x faster |
| django_template | 38.0 ms | 27.5 ms: 1.38x faster |
| Geometric mean  | (ref)   | 1.48x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | TCO-PGO-Ex2            |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.22 ms  | 2.09 ms: 2.02x faster  |
| logging_silent             | 124 ns   | 62.9 ns: 1.97x faster  |
| generators                 | 35.6 ms  | 18.1 ms: 1.97x faster  |
| scimark_sor                | 139 ms   | 73.9 ms: 1.88x faster  |
| unpickle_pure_python       | 284 us   | 154 us: 1.85x faster   |
| scimark_lu                 | 119 ms   | 65.2 ms: 1.83x faster  |
| go                         | 140 ms   | 78.0 ms: 1.80x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.48 ms: 1.79x faster  |
| hexiom                     | 7.44 ms  | 4.17 ms: 1.79x faster  |
| scimark_monte_carlo        | 75.8 ms  | 42.9 ms: 1.77x faster  |
| nbody                      | 103 ms   | 58.8 ms: 1.76x faster  |
| float                      | 78.0 ms  | 44.8 ms: 1.74x faster  |
| spectral_norm              | 102 ms   | 58.4 ms: 1.74x faster  |
| richards                   | 59.0 ms  | 35.0 ms: 1.69x faster  |
| richards_super             | 67.7 ms  | 40.4 ms: 1.68x faster  |
| raytrace                   | 313 ms   | 187 ms: 1.67x faster   |
| chaos                      | 69.3 ms  | 41.4 ms: 1.67x faster  |
| coroutines                 | 22.4 ms  | 13.5 ms: 1.67x faster  |
| comprehensions             | 20.1 us  | 12.2 us: 1.64x faster  |
| crypto_pyaes               | 80.1 ms  | 49.3 ms: 1.62x faster  |
| mako                       | 12.1 ms  | 7.44 ms: 1.62x faster  |
| pyflate                    | 477 ms   | 295 ms: 1.62x faster   |
| sqlglot_v2_parse           | 1.41 ms  | 876 us: 1.60x faster   |
| deepcopy_memo              | 34.0 us  | 21.3 us: 1.60x faster  |
| fannkuch                   | 418 ms   | 265 ms: 1.58x faster   |
| async_generators           | 348 ms   | 224 ms: 1.56x faster   |
| scimark_fft                | 276 ms   | 178 ms: 1.55x faster   |
| pickle_pure_python         | 364 us   | 236 us: 1.55x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 1.09 ms: 1.54x faster  |
| tomli_loads                | 2.07 sec | 1.38 sec: 1.50x faster |
| genshi_text                | 23.9 ms  | 16.2 ms: 1.48x faster  |
| pprint_safe_repr           | 825 ms   | 558 ms: 1.48x faster   |
| regex_compile              | 130 ms   | 88.0 ms: 1.48x faster  |
| nqueens                    | 96.9 ms  | 65.7 ms: 1.47x faster  |
| pprint_pformat             | 1.66 sec | 1.13 sec: 1.47x faster |
| pathlib                    | 37.5 ms  | 25.6 ms: 1.47x faster  |
| xml_etree_process          | 66.9 ms  | 46.5 ms: 1.44x faster  |
| genshi_xml                 | 50.4 ms  | 35.3 ms: 1.43x faster  |
| async_tree_none            | 267 ms   | 188 ms: 1.42x faster   |
| bench_thread_pool          | 1.28 ms  | 906 us: 1.41x faster   |
| bpe_tokeniser              | 4.45 sec | 3.17 sec: 1.40x faster |
| deepcopy                   | 278 us   | 199 us: 1.40x faster   |
| async_tree_memoization_tg  | 304 ms   | 218 ms: 1.40x faster   |
| logging_simple             | 9.30 us  | 6.67 us: 1.39x faster  |
| xml_etree_generate         | 92.6 ms  | 66.8 ms: 1.39x faster  |
| django_template            | 38.0 ms  | 27.5 ms: 1.38x faster  |
| sqlglot_v2_normalize       | 109 ms   | 79.0 ms: 1.38x faster  |
| logging_format             | 9.92 us  | 7.18 us: 1.38x faster  |
| async_tree_memoization     | 313 ms   | 227 ms: 1.38x faster   |
| sqlglot_v2_optimize        | 52.8 ms  | 38.4 ms: 1.38x faster  |
| async_tree_io_tg           | 576 ms   | 419 ms: 1.37x faster   |
| async_tree_none_tg         | 243 ms   | 178 ms: 1.37x faster   |
| typing_runtime_protocols   | 154 us   | 113 us: 1.37x faster   |
| deepcopy_reduce            | 2.86 us  | 2.12 us: 1.35x faster  |
| sympy_integrate            | 18.4 ms  | 13.9 ms: 1.33x faster  |
| async_tree_io              | 570 ms   | 429 ms: 1.33x faster   |
| pycparser                  | 1.01 sec | 765 ms: 1.33x faster   |
| sympy_str                  | 247 ms   | 187 ms: 1.33x faster   |
| xml_etree_iterparse        | 94.3 ms  | 71.5 ms: 1.32x faster  |
| 2to3                       | 309 ms   | 237 ms: 1.30x faster   |
| sympy_expand               | 419 ms   | 324 ms: 1.29x faster   |
| sphinx                     | 933 ms   | 723 ms: 1.29x faster   |
| html5lib                   | 52.5 ms  | 40.8 ms: 1.29x faster  |
| sympy_sum                  | 123 ms   | 96.6 ms: 1.28x faster  |
| meteor_contest             | 99.5 ms  | 78.1 ms: 1.27x faster  |
| docutils                   | 2.31 sec | 1.81 sec: 1.27x faster |
| thrift                     | 710 us   | 561 us: 1.27x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 362 ms: 1.26x faster   |
| k_core                     | 2.18 sec | 1.76 sec: 1.24x faster |
| pylint                     | 269 ms   | 217 ms: 1.24x faster   |
| telco                      | 6.56 ms  | 5.33 ms: 1.23x faster  |
| shortest_path              | 437 ms   | 357 ms: 1.22x faster   |
| dulwich_log                | 52.4 ms  | 43.0 ms: 1.22x faster  |
| connected_components       | 395 ms   | 326 ms: 1.21x faster   |
| async_tree_cpu_io_mixed_tg | 444 ms   | 367 ms: 1.21x faster   |
| mdp                        | 1.89 sec | 1.57 sec: 1.20x faster |
| json_dumps                 | 9.44 ms  | 7.94 ms: 1.19x faster  |
| gc_traversal               | 3.25 ms  | 2.77 ms: 1.17x faster  |
| sqlite_synth               | 1.96 us  | 1.68 us: 1.16x faster  |
| coverage                   | 63.7 ms  | 56.4 ms: 1.13x faster  |
| json_loads                 | 23.3 us  | 21.1 us: 1.10x faster  |
| python_startup             | 29.5 ms  | 26.9 ms: 1.10x faster  |
| python_startup_no_site     | 22.0 ms  | 20.1 ms: 1.09x faster  |
| asyncio_websockets         | 330 ms   | 304 ms: 1.09x faster   |
| xml_etree_parse            | 112 ms   | 104 ms: 1.09x faster   |
| json                       | 4.07 ms  | 3.77 ms: 1.08x faster  |
| pidigits                   | 156 ms   | 147 ms: 1.07x faster   |
| bench_mp_pool              | 101 ms   | 95.0 ms: 1.06x faster  |
| regex_effbot               | 1.87 ms  | 1.76 ms: 1.06x faster  |
| regex_v8                   | 17.5 ms  | 16.7 ms: 1.05x faster  |
| regex_dna                  | 123 ms   | 117 ms: 1.05x faster   |
| create_gc_cycles           | 1.42 ms  | 1.38 ms: 1.02x faster  |
| many_optionals             | 559 us   | 813 us: 1.45x slower   |
| subparsers                 | 21.5 ms  | 47.1 ms: 2.19x slower  |
| Geometric mean             | (ref)    | 1.37x faster           |

- Geometric mean (including insignificant results): 1.371x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: unknown