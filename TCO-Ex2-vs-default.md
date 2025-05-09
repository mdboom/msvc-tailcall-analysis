# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.318x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 237 ms: 1.26x faster   |
| docutils       | 2.17 sec | 1.81 sec: 1.20x faster |
| html5lib       | 51.3 ms  | 40.8 ms: 1.26x faster  |
| sphinx         | 872 ms   | 723 ms: 1.20x faster   |
| Geometric mean | (ref)    | 1.23x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 13.5 ms: 1.63x faster |
| async_generators           | 328 ms  | 224 ms: 1.47x faster  |
| async_tree_memoization_tg  | 291 ms  | 218 ms: 1.33x faster  |
| async_tree_io_tg           | 559 ms  | 419 ms: 1.33x faster  |
| async_tree_none_tg         | 236 ms  | 178 ms: 1.33x faster  |
| async_tree_none            | 249 ms  | 188 ms: 1.33x faster  |
| async_tree_memoization     | 297 ms  | 227 ms: 1.31x faster  |
| async_tree_io              | 553 ms  | 429 ms: 1.29x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 362 ms: 1.20x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 367 ms: 1.16x faster  |
| asyncio_websockets         | 317 ms  | 304 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.30x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 58.8 ms: 1.71x faster |
| float          | 75.4 ms | 44.8 ms: 1.68x faster |
| pidigits       | 152 ms  | 147 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.44x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 88.0 ms: 1.42x faster |
| regex_effbot   | 1.81 ms | 1.76 ms: 1.03x faster |
| regex_dna      | 121 ms  | 117 ms: 1.03x faster  |
| regex_v8       | 17.1 ms | 16.7 ms: 1.03x faster |
| Geometric mean | (ref)   | 1.11x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 154 us: 1.78x faster   |
| pickle_pure_python   | 355 us   | 236 us: 1.51x faster   |
| tomli_loads          | 1.99 sec | 1.38 sec: 1.44x faster |
| xml_etree_process    | 64.6 ms  | 46.5 ms: 1.39x faster  |
| xml_etree_generate   | 89.5 ms  | 66.8 ms: 1.34x faster  |
| xml_etree_iterparse  | 89.9 ms  | 71.5 ms: 1.26x faster  |
| json_dumps           | 9.01 ms  | 7.94 ms: 1.13x faster  |
| json_loads           | 22.3 us  | 21.1 us: 1.06x faster  |
| xml_etree_parse      | 108 ms   | 104 ms: 1.04x faster   |
| Geometric mean       | (ref)    | 1.31x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TCO-Ex2               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 26.9 ms: 1.02x faster |
| python_startup_no_site | 20.4 ms | 20.1 ms: 1.01x faster |
| Geometric mean         | (ref)   | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 7.44 ms: 1.57x faster |
| genshi_text     | 23.2 ms | 16.2 ms: 1.43x faster |
| genshi_xml      | 48.8 ms | 35.3 ms: 1.38x faster |
| django_template | 36.9 ms | 27.5 ms: 1.34x faster |
| Geometric mean  | (ref)   | 1.43x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.09 ms  | 2.09 ms: 1.96x faster  |
| logging_silent             | 119 ns   | 62.9 ns: 1.90x faster  |
| generators                 | 33.8 ms  | 18.1 ms: 1.87x faster  |
| scimark_sor                | 135 ms   | 73.9 ms: 1.83x faster  |
| scimark_lu                 | 116 ms   | 65.2 ms: 1.78x faster  |
| unpickle_pure_python       | 274 us   | 154 us: 1.78x faster   |
| go                         | 137 ms   | 78.0 ms: 1.76x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.48 ms: 1.75x faster  |
| hexiom                     | 7.27 ms  | 4.17 ms: 1.74x faster  |
| scimark_monte_carlo        | 73.9 ms  | 42.9 ms: 1.72x faster  |
| nbody                      | 101 ms   | 58.8 ms: 1.71x faster  |
| float                      | 75.4 ms  | 44.8 ms: 1.68x faster  |
| spectral_norm              | 97.7 ms  | 58.4 ms: 1.67x faster  |
| richards                   | 57.8 ms  | 35.0 ms: 1.65x faster  |
| richards_super             | 65.8 ms  | 40.4 ms: 1.63x faster  |
| coroutines                 | 21.9 ms  | 13.5 ms: 1.63x faster  |
| raytrace                   | 304 ms   | 187 ms: 1.63x faster   |
| comprehensions             | 19.4 us  | 12.2 us: 1.58x faster  |
| crypto_pyaes               | 77.9 ms  | 49.3 ms: 1.58x faster  |
| chaos                      | 65.2 ms  | 41.4 ms: 1.57x faster  |
| mako                       | 11.7 ms  | 7.44 ms: 1.57x faster  |
| pyflate                    | 462 ms   | 295 ms: 1.57x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 876 us: 1.55x faster   |
| deepcopy_memo              | 32.9 us  | 21.3 us: 1.54x faster  |
| fannkuch                   | 407 ms   | 265 ms: 1.54x faster   |
| scimark_fft                | 269 ms   | 178 ms: 1.51x faster   |
| pickle_pure_python         | 355 us   | 236 us: 1.51x faster   |
| sqlglot_v2_transpile       | 1.64 ms  | 1.09 ms: 1.50x faster  |
| async_generators           | 328 ms   | 224 ms: 1.47x faster   |
| tomli_loads                | 1.99 sec | 1.38 sec: 1.44x faster |
| nqueens                    | 94.3 ms  | 65.7 ms: 1.44x faster  |
| genshi_text                | 23.2 ms  | 16.2 ms: 1.43x faster  |
| pprint_pformat             | 1.61 sec | 1.13 sec: 1.43x faster |
| regex_compile              | 125 ms   | 88.0 ms: 1.42x faster  |
| pprint_safe_repr           | 788 ms   | 558 ms: 1.41x faster   |
| xml_etree_process          | 64.6 ms  | 46.5 ms: 1.39x faster  |
| genshi_xml                 | 48.8 ms  | 35.3 ms: 1.38x faster  |
| bpe_tokeniser              | 4.30 sec | 3.17 sec: 1.36x faster |
| deepcopy                   | 269 us   | 199 us: 1.35x faster   |
| sqlglot_v2_normalize       | 106 ms   | 79.0 ms: 1.34x faster  |
| pathlib                    | 34.4 ms  | 25.6 ms: 1.34x faster  |
| django_template            | 36.9 ms  | 27.5 ms: 1.34x faster  |
| xml_etree_generate         | 89.5 ms  | 66.8 ms: 1.34x faster  |
| async_tree_memoization_tg  | 291 ms   | 218 ms: 1.33x faster   |
| typing_runtime_protocols   | 150 us   | 113 us: 1.33x faster   |
| async_tree_io_tg           | 559 ms   | 419 ms: 1.33x faster   |
| async_tree_none_tg         | 236 ms   | 178 ms: 1.33x faster   |
| sqlglot_v2_optimize        | 51.0 ms  | 38.4 ms: 1.33x faster  |
| logging_simple             | 8.87 us  | 6.67 us: 1.33x faster  |
| async_tree_none            | 249 ms   | 188 ms: 1.33x faster   |
| async_tree_memoization     | 297 ms   | 227 ms: 1.31x faster   |
| deepcopy_reduce            | 2.77 us  | 2.12 us: 1.30x faster  |
| logging_format             | 9.33 us  | 7.18 us: 1.30x faster  |
| pycparser                  | 992 ms   | 765 ms: 1.30x faster   |
| async_tree_io              | 553 ms   | 429 ms: 1.29x faster   |
| sympy_integrate            | 17.8 ms  | 13.9 ms: 1.28x faster  |
| sympy_str                  | 238 ms   | 187 ms: 1.28x faster   |
| xml_etree_iterparse        | 89.9 ms  | 71.5 ms: 1.26x faster  |
| 2to3                       | 298 ms   | 237 ms: 1.26x faster   |
| html5lib                   | 51.3 ms  | 40.8 ms: 1.26x faster  |
| sympy_expand               | 405 ms   | 324 ms: 1.25x faster   |
| sympy_sum                  | 119 ms   | 96.6 ms: 1.24x faster  |
| thrift                     | 694 us   | 561 us: 1.24x faster   |
| meteor_contest             | 95.9 ms  | 78.1 ms: 1.23x faster  |
| telco                      | 6.44 ms  | 5.33 ms: 1.21x faster  |
| sphinx                     | 872 ms   | 723 ms: 1.20x faster   |
| async_tree_cpu_io_mixed    | 437 ms   | 362 ms: 1.20x faster   |
| docutils                   | 2.17 sec | 1.81 sec: 1.20x faster |
| dulwich_log                | 51.0 ms  | 43.0 ms: 1.19x faster  |
| pylint                     | 253 ms   | 217 ms: 1.16x faster   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 367 ms: 1.16x faster   |
| mdp                        | 1.81 sec | 1.57 sec: 1.16x faster |
| gc_traversal               | 3.15 ms  | 2.77 ms: 1.14x faster  |
| json_dumps                 | 9.01 ms  | 7.94 ms: 1.13x faster  |
| bench_thread_pool          | 1.01 ms  | 906 us: 1.11x faster   |
| coverage                   | 61.9 ms  | 56.4 ms: 1.10x faster  |
| sqlite_synth               | 1.84 us  | 1.68 us: 1.10x faster  |
| connected_components       | 347 ms   | 326 ms: 1.06x faster   |
| json_loads                 | 22.3 us  | 21.1 us: 1.06x faster  |
| shortest_path              | 378 ms   | 357 ms: 1.06x faster   |
| json                       | 3.96 ms  | 3.77 ms: 1.05x faster  |
| asyncio_websockets         | 317 ms   | 304 ms: 1.04x faster   |
| xml_etree_parse            | 108 ms   | 104 ms: 1.04x faster   |
| k_core                     | 1.83 sec | 1.76 sec: 1.04x faster |
| pidigits                   | 152 ms   | 147 ms: 1.04x faster   |
| regex_effbot               | 1.81 ms  | 1.76 ms: 1.03x faster  |
| regex_dna                  | 121 ms   | 117 ms: 1.03x faster   |
| regex_v8                   | 17.1 ms  | 16.7 ms: 1.03x faster  |
| python_startup             | 27.3 ms  | 26.9 ms: 1.02x faster  |
| create_gc_cycles           | 1.40 ms  | 1.38 ms: 1.01x faster  |
| python_startup_no_site     | 20.4 ms  | 20.1 ms: 1.01x faster  |
| bench_mp_pool              | 96.2 ms  | 95.0 ms: 1.01x faster  |
| many_optionals             | 547 us   | 813 us: 1.49x slower   |
| subparsers                 | 20.8 ms  | 47.1 ms: 2.27x slower  |
| Geometric mean             | (ref)    | 1.32x faster           |

- Geometric mean (including insignificant results): 1.318x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: unknown