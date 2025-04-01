# Results vs. base

- fork: unknown
- ref: clang
- machine: unknown-unknown
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.670x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | clang                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 207 ms: 1.44x faster   |
| docutils       | 2.17 sec | 1.56 sec: 1.39x faster |
| html5lib       | 51.3 ms  | 34.9 ms: 1.47x faster  |
| sphinx         | 872 ms   | 603 ms: 1.45x faster   |
| Geometric mean | (ref)    | 1.44x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | clang                 |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 10.7 ms: 2.04x faster |
| asyncio_websockets         | 317 ms  | 159 ms: 2.00x faster  |
| async_generators           | 328 ms  | 187 ms: 1.75x faster  |
| async_tree_io_tg           | 559 ms  | 351 ms: 1.59x faster  |
| async_tree_memoization     | 297 ms  | 187 ms: 1.59x faster  |
| async_tree_none_tg         | 236 ms  | 150 ms: 1.57x faster  |
| async_tree_none            | 249 ms  | 159 ms: 1.57x faster  |
| async_tree_io              | 553 ms  | 353 ms: 1.57x faster  |
| async_tree_memoization_tg  | 291 ms  | 197 ms: 1.48x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 313 ms: 1.39x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 316 ms: 1.34x faster  |
| Geometric mean             | (ref)   | 1.61x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | clang                 |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 49.1 ms: 2.05x faster |
| float          | 75.4 ms | 36.9 ms: 2.04x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.64x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | clang                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 69.8 ms: 1.79x faster |
| regex_v8       | 17.1 ms | 13.0 ms: 1.32x faster |
| regex_effbot   | 1.81 ms | 1.54 ms: 1.18x faster |
| regex_dna      | 121 ms  | 117 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.30x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | clang                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 107 us: 2.56x faster   |
| pickle_pure_python   | 355 us   | 173 us: 2.05x faster   |
| xml_etree_process    | 64.6 ms  | 34.0 ms: 1.90x faster  |
| tomli_loads          | 1.99 sec | 1.09 sec: 1.83x faster |
| xml_etree_generate   | 89.5 ms  | 49.1 ms: 1.82x faster  |
| json_dumps           | 9.01 ms  | 5.66 ms: 1.59x faster  |
| json_loads           | 22.3 us  | 14.1 us: 1.59x faster  |
| xml_etree_iterparse  | 89.9 ms  | 61.5 ms: 1.46x faster  |
| xml_etree_parse      | 108 ms   | 89.4 ms: 1.21x faster  |
| Geometric mean       | (ref)    | 1.74x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | clang                 |
|------------------------|:-------:|:---------------------:|
| python_startup         | 27.3 ms | 26.4 ms: 1.03x faster |
| python_startup_no_site | 20.4 ms | 20.9 ms: 1.03x slower |
| Geometric mean         | (ref)   | 1.00x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | clang                 |
|-----------------|:-------:|:---------------------:|
| mako            | 11.7 ms | 5.83 ms: 2.01x faster |
| genshi_text     | 23.2 ms | 11.9 ms: 1.94x faster |
| django_template | 36.9 ms | 21.3 ms: 1.73x faster |
| genshi_xml      | 48.8 ms | 29.0 ms: 1.68x faster |
| Geometric mean  | (ref)   | 1.84x faster          |

All benchmarks:
===============

| Benchmark                  | default  | clang                  |
|----------------------------|:--------:|:----------------------:|
| logging_silent             | 119 ns   | 41.1 ns: 2.90x faster  |
| scimark_sor                | 135 ms   | 49.3 ms: 2.74x faster  |
| scimark_lu                 | 116 ms   | 43.5 ms: 2.67x faster  |
| mdp                        | 1.81 sec | 682 ms: 2.66x faster   |
| scimark_monte_carlo        | 73.9 ms  | 28.6 ms: 2.58x faster  |
| unpickle_pure_python       | 274 us   | 107 us: 2.56x faster   |
| deltablue                  | 4.09 ms  | 1.64 ms: 2.49x faster  |
| hexiom                     | 7.27 ms  | 2.98 ms: 2.44x faster  |
| deepcopy_memo              | 32.9 us  | 14.0 us: 2.35x faster  |
| generators                 | 33.8 ms  | 14.8 ms: 2.29x faster  |
| spectral_norm              | 97.7 ms  | 42.8 ms: 2.28x faster  |
| comprehensions             | 19.4 us  | 8.64 us: 2.24x faster  |
| go                         | 137 ms   | 61.5 ms: 2.23x faster  |
| richards                   | 57.8 ms  | 26.3 ms: 2.20x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 1.99 ms: 2.18x faster  |
| richards_super             | 65.8 ms  | 30.2 ms: 2.17x faster  |
| raytrace                   | 304 ms   | 142 ms: 2.14x faster   |
| chaos                      | 65.2 ms  | 31.4 ms: 2.08x faster  |
| nbody                      | 101 ms   | 49.1 ms: 2.05x faster  |
| pickle_pure_python         | 355 us   | 173 us: 2.05x faster   |
| float                      | 75.4 ms  | 36.9 ms: 2.04x faster  |
| coroutines                 | 21.9 ms  | 10.7 ms: 2.04x faster  |
| mako                       | 11.7 ms  | 5.83 ms: 2.01x faster  |
| asyncio_websockets         | 317 ms   | 159 ms: 2.00x faster   |
| sqlglot_v2_parse           | 1.36 ms  | 682 us: 1.99x faster   |
| fannkuch                   | 407 ms   | 207 ms: 1.97x faster   |
| pyflate                    | 462 ms   | 234 ms: 1.97x faster   |
| crypto_pyaes               | 77.9 ms  | 39.9 ms: 1.95x faster  |
| genshi_text                | 23.2 ms  | 11.9 ms: 1.94x faster  |
| pprint_pformat             | 1.61 sec | 835 ms: 1.93x faster   |
| scimark_fft                | 269 ms   | 139 ms: 1.93x faster   |
| xml_etree_process          | 64.6 ms  | 34.0 ms: 1.90x faster  |
| pprint_safe_repr           | 788 ms   | 415 ms: 1.90x faster   |
| nqueens                    | 94.3 ms  | 49.8 ms: 1.89x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 873 us: 1.88x faster   |
| deepcopy                   | 269 us   | 144 us: 1.87x faster   |
| tomli_loads                | 1.99 sec | 1.09 sec: 1.83x faster |
| deepcopy_reduce            | 2.77 us  | 1.52 us: 1.83x faster  |
| xml_etree_generate         | 89.5 ms  | 49.1 ms: 1.82x faster  |
| regex_compile              | 125 ms   | 69.8 ms: 1.79x faster  |
| async_generators           | 328 ms   | 187 ms: 1.75x faster   |
| django_template            | 36.9 ms  | 21.3 ms: 1.73x faster  |
| typing_runtime_protocols   | 150 us   | 87.6 us: 1.72x faster  |
| bpe_tokeniser              | 4.30 sec | 2.55 sec: 1.69x faster |
| genshi_xml                 | 48.8 ms  | 29.0 ms: 1.68x faster  |
| sqlglot_v2_normalize       | 106 ms   | 64.2 ms: 1.65x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 31.1 ms: 1.64x faster  |
| sympy_str                  | 238 ms   | 149 ms: 1.60x faster   |
| logging_simple             | 8.87 us  | 5.55 us: 1.60x faster  |
| async_tree_io_tg           | 559 ms   | 351 ms: 1.59x faster   |
| json_dumps                 | 9.01 ms  | 5.66 ms: 1.59x faster  |
| json_loads                 | 22.3 us  | 14.1 us: 1.59x faster  |
| async_tree_memoization     | 297 ms   | 187 ms: 1.59x faster   |
| sympy_integrate            | 17.8 ms  | 11.2 ms: 1.59x faster  |
| sympy_expand               | 405 ms   | 256 ms: 1.58x faster   |
| async_tree_none_tg         | 236 ms   | 150 ms: 1.57x faster   |
| async_tree_none            | 249 ms   | 159 ms: 1.57x faster   |
| async_tree_io              | 553 ms   | 353 ms: 1.57x faster   |
| logging_format             | 9.33 us  | 5.96 us: 1.57x faster  |
| coverage                   | 61.9 ms  | 39.8 ms: 1.56x faster  |
| pycparser                  | 992 ms   | 647 ms: 1.53x faster   |
| telco                      | 6.44 ms  | 4.25 ms: 1.52x faster  |
| sympy_sum                  | 119 ms   | 79.2 ms: 1.51x faster  |
| async_tree_memoization_tg  | 291 ms   | 197 ms: 1.48x faster   |
| html5lib                   | 51.3 ms  | 34.9 ms: 1.47x faster  |
| xml_etree_iterparse        | 89.9 ms  | 61.5 ms: 1.46x faster  |
| sphinx                     | 872 ms   | 603 ms: 1.45x faster   |
| 2to3                       | 298 ms   | 207 ms: 1.44x faster   |
| meteor_contest             | 95.9 ms  | 66.8 ms: 1.44x faster  |
| json                       | 3.96 ms  | 2.81 ms: 1.41x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 313 ms: 1.39x faster   |
| docutils                   | 2.17 sec | 1.56 sec: 1.39x faster |
| subparsers                 | 20.8 ms  | 15.3 ms: 1.36x faster  |
| pylint                     | 253 ms   | 188 ms: 1.34x faster   |
| async_tree_cpu_io_mixed_tg | 424 ms   | 316 ms: 1.34x faster   |
| dulwich_log                | 51.0 ms  | 38.0 ms: 1.34x faster  |
| many_optionals             | 547 us   | 409 us: 1.34x faster   |
| regex_v8                   | 17.1 ms  | 13.0 ms: 1.32x faster  |
| bench_thread_pool          | 1.01 ms  | 823 us: 1.22x faster   |
| sqlite_synth               | 1.84 us  | 1.51 us: 1.22x faster  |
| xml_etree_parse            | 108 ms   | 89.4 ms: 1.21x faster  |
| regex_effbot               | 1.81 ms  | 1.54 ms: 1.18x faster  |
| gc_traversal               | 3.15 ms  | 2.76 ms: 1.14x faster  |
| pathlib                    | 34.4 ms  | 30.7 ms: 1.12x faster  |
| k_core                     | 1.83 sec | 1.66 sec: 1.10x faster |
| bench_mp_pool              | 96.2 ms  | 88.6 ms: 1.09x faster  |
| shortest_path              | 378 ms   | 351 ms: 1.08x faster   |
| connected_components       | 347 ms   | 329 ms: 1.05x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| python_startup             | 27.3 ms  | 26.4 ms: 1.03x faster  |
| create_gc_cycles           | 1.40 ms  | 1.36 ms: 1.03x faster  |
| regex_dna                  | 121 ms   | 117 ms: 1.03x faster   |
| python_startup_no_site     | 20.4 ms  | 20.9 ms: 1.03x slower  |
| Geometric mean             | (ref)    | 1.67x faster           |
Ignored benchmarks (1) of default.json: thrift

- Geometric mean (including insignificant results): 1.670x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.57x
- 95% likely to have a speedup of 1.56x
- 99% likely to have a speedup of 1.53x

# Memory
- memory change: unknown