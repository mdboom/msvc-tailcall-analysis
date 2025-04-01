# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.401x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.53x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang    | default                |
|----------------|:--------:|:----------------------:|
| 2to3           | 207 ms   | 298 ms: 1.44x slower   |
| docutils       | 1.56 sec | 2.17 sec: 1.39x slower |
| html5lib       | 34.9 ms  | 51.3 ms: 1.47x slower  |
| sphinx         | 603 ms   | 872 ms: 1.45x slower   |
| Geometric mean | (ref)    | 1.44x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang   | default               |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 316 ms  | 424 ms: 1.34x slower  |
| async_tree_cpu_io_mixed    | 313 ms  | 437 ms: 1.39x slower  |
| async_tree_memoization_tg  | 197 ms  | 291 ms: 1.48x slower  |
| async_tree_io              | 353 ms  | 553 ms: 1.57x slower  |
| async_tree_none            | 159 ms  | 249 ms: 1.57x slower  |
| async_tree_none_tg         | 150 ms  | 236 ms: 1.57x slower  |
| async_tree_memoization     | 187 ms  | 297 ms: 1.59x slower  |
| async_tree_io_tg           | 351 ms  | 559 ms: 1.59x slower  |
| async_generators           | 187 ms  | 328 ms: 1.75x slower  |
| asyncio_websockets         | 159 ms  | 317 ms: 2.00x slower  |
| coroutines                 | 10.7 ms | 21.9 ms: 2.04x slower |
| Geometric mean             | (ref)   | 1.61x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang   | default               |
|----------------|:-------:|:---------------------:|
| pidigits       | 145 ms  | 152 ms: 1.05x slower  |
| float          | 36.9 ms | 75.4 ms: 2.04x slower |
| nbody          | 49.1 ms | 101 ms: 2.05x slower  |
| Geometric mean | (ref)   | 1.64x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang   | default               |
|----------------|:-------:|:---------------------:|
| regex_dna      | 117 ms  | 121 ms: 1.03x slower  |
| regex_effbot   | 1.54 ms | 1.81 ms: 1.18x slower |
| regex_v8       | 13.0 ms | 17.1 ms: 1.32x slower |
| regex_compile  | 69.8 ms | 125 ms: 1.79x slower  |
| Geometric mean | (ref)   | 1.30x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang    | default                |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 89.4 ms  | 108 ms: 1.21x slower   |
| xml_etree_iterparse  | 61.5 ms  | 89.9 ms: 1.46x slower  |
| json_loads           | 14.1 us  | 22.3 us: 1.59x slower  |
| json_dumps           | 5.66 ms  | 9.01 ms: 1.59x slower  |
| xml_etree_generate   | 49.1 ms  | 89.5 ms: 1.82x slower  |
| tomli_loads          | 1.09 sec | 1.99 sec: 1.83x slower |
| xml_etree_process    | 34.0 ms  | 64.6 ms: 1.90x slower  |
| pickle_pure_python   | 173 us   | 355 us: 2.05x slower   |
| unpickle_pure_python | 107 us   | 274 us: 2.56x slower   |
| Geometric mean       | (ref)    | 1.74x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang   | default               |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.9 ms | 20.4 ms: 1.03x faster |
| python_startup         | 26.4 ms | 27.3 ms: 1.03x slower |
| Geometric mean         | (ref)   | 1.00x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang   | default               |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 29.0 ms | 48.8 ms: 1.68x slower |
| django_template | 21.3 ms | 36.9 ms: 1.73x slower |
| genshi_text     | 11.9 ms | 23.2 ms: 1.94x slower |
| mako            | 5.83 ms | 11.7 ms: 2.01x slower |
| Geometric mean  | (ref)   | 1.84x slower          |

All benchmarks:
===============

| Benchmark                  | clang    | default                |
|----------------------------|:--------:|:----------------------:|
| python_startup_no_site     | 20.9 ms  | 20.4 ms: 1.03x faster  |
| regex_dna                  | 117 ms   | 121 ms: 1.03x slower   |
| create_gc_cycles           | 1.36 ms  | 1.40 ms: 1.03x slower  |
| python_startup             | 26.4 ms  | 27.3 ms: 1.03x slower  |
| pidigits                   | 145 ms   | 152 ms: 1.05x slower   |
| connected_components       | 329 ms   | 347 ms: 1.05x slower   |
| shortest_path              | 351 ms   | 378 ms: 1.08x slower   |
| bench_mp_pool              | 88.6 ms  | 96.2 ms: 1.09x slower  |
| k_core                     | 1.66 sec | 1.83 sec: 1.10x slower |
| pathlib                    | 30.7 ms  | 34.4 ms: 1.12x slower  |
| gc_traversal               | 2.76 ms  | 3.15 ms: 1.14x slower  |
| regex_effbot               | 1.54 ms  | 1.81 ms: 1.18x slower  |
| xml_etree_parse            | 89.4 ms  | 108 ms: 1.21x slower   |
| sqlite_synth               | 1.51 us  | 1.84 us: 1.22x slower  |
| bench_thread_pool          | 823 us   | 1.01 ms: 1.22x slower  |
| regex_v8                   | 13.0 ms  | 17.1 ms: 1.32x slower  |
| many_optionals             | 409 us   | 547 us: 1.34x slower   |
| dulwich_log                | 38.0 ms  | 51.0 ms: 1.34x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms   | 424 ms: 1.34x slower   |
| pylint                     | 188 ms   | 253 ms: 1.34x slower   |
| subparsers                 | 15.3 ms  | 20.8 ms: 1.36x slower  |
| docutils                   | 1.56 sec | 2.17 sec: 1.39x slower |
| async_tree_cpu_io_mixed    | 313 ms   | 437 ms: 1.39x slower   |
| json                       | 2.81 ms  | 3.96 ms: 1.41x slower  |
| meteor_contest             | 66.8 ms  | 95.9 ms: 1.44x slower  |
| 2to3                       | 207 ms   | 298 ms: 1.44x slower   |
| sphinx                     | 603 ms   | 872 ms: 1.45x slower   |
| xml_etree_iterparse        | 61.5 ms  | 89.9 ms: 1.46x slower  |
| html5lib                   | 34.9 ms  | 51.3 ms: 1.47x slower  |
| async_tree_memoization_tg  | 197 ms   | 291 ms: 1.48x slower   |
| sympy_sum                  | 79.2 ms  | 119 ms: 1.51x slower   |
| telco                      | 4.25 ms  | 6.44 ms: 1.52x slower  |
| pycparser                  | 647 ms   | 992 ms: 1.53x slower   |
| coverage                   | 39.8 ms  | 61.9 ms: 1.56x slower  |
| logging_format             | 5.96 us  | 9.33 us: 1.57x slower  |
| async_tree_io              | 353 ms   | 553 ms: 1.57x slower   |
| async_tree_none            | 159 ms   | 249 ms: 1.57x slower   |
| async_tree_none_tg         | 150 ms   | 236 ms: 1.57x slower   |
| sympy_expand               | 256 ms   | 405 ms: 1.58x slower   |
| sympy_integrate            | 11.2 ms  | 17.8 ms: 1.59x slower  |
| async_tree_memoization     | 187 ms   | 297 ms: 1.59x slower   |
| json_loads                 | 14.1 us  | 22.3 us: 1.59x slower  |
| json_dumps                 | 5.66 ms  | 9.01 ms: 1.59x slower  |
| async_tree_io_tg           | 351 ms   | 559 ms: 1.59x slower   |
| logging_simple             | 5.55 us  | 8.87 us: 1.60x slower  |
| sympy_str                  | 149 ms   | 238 ms: 1.60x slower   |
| sqlglot_v2_optimize        | 31.1 ms  | 51.0 ms: 1.64x slower  |
| sqlglot_v2_normalize       | 64.2 ms  | 106 ms: 1.65x slower   |
| genshi_xml                 | 29.0 ms  | 48.8 ms: 1.68x slower  |
| bpe_tokeniser              | 2.55 sec | 4.30 sec: 1.69x slower |
| typing_runtime_protocols   | 87.6 us  | 150 us: 1.72x slower   |
| django_template            | 21.3 ms  | 36.9 ms: 1.73x slower  |
| async_generators           | 187 ms   | 328 ms: 1.75x slower   |
| regex_compile              | 69.8 ms  | 125 ms: 1.79x slower   |
| xml_etree_generate         | 49.1 ms  | 89.5 ms: 1.82x slower  |
| deepcopy_reduce            | 1.52 us  | 2.77 us: 1.83x slower  |
| tomli_loads                | 1.09 sec | 1.99 sec: 1.83x slower |
| deepcopy                   | 144 us   | 269 us: 1.87x slower   |
| sqlglot_v2_transpile       | 873 us   | 1.64 ms: 1.88x slower  |
| nqueens                    | 49.8 ms  | 94.3 ms: 1.89x slower  |
| pprint_safe_repr           | 415 ms   | 788 ms: 1.90x slower   |
| xml_etree_process          | 34.0 ms  | 64.6 ms: 1.90x slower  |
| scimark_fft                | 139 ms   | 269 ms: 1.93x slower   |
| pprint_pformat             | 835 ms   | 1.61 sec: 1.93x slower |
| genshi_text                | 11.9 ms  | 23.2 ms: 1.94x slower  |
| crypto_pyaes               | 39.9 ms  | 77.9 ms: 1.95x slower  |
| pyflate                    | 234 ms   | 462 ms: 1.97x slower   |
| fannkuch                   | 207 ms   | 407 ms: 1.97x slower   |
| sqlglot_v2_parse           | 682 us   | 1.36 ms: 1.99x slower  |
| asyncio_websockets         | 159 ms   | 317 ms: 2.00x slower   |
| mako                       | 5.83 ms  | 11.7 ms: 2.01x slower  |
| coroutines                 | 10.7 ms  | 21.9 ms: 2.04x slower  |
| float                      | 36.9 ms  | 75.4 ms: 2.04x slower  |
| pickle_pure_python         | 173 us   | 355 us: 2.05x slower   |
| nbody                      | 49.1 ms  | 101 ms: 2.05x slower   |
| chaos                      | 31.4 ms  | 65.2 ms: 2.08x slower  |
| raytrace                   | 142 ms   | 304 ms: 2.14x slower   |
| richards_super             | 30.2 ms  | 65.8 ms: 2.17x slower  |
| scimark_sparse_mat_mult    | 1.99 ms  | 4.34 ms: 2.18x slower  |
| richards                   | 26.3 ms  | 57.8 ms: 2.20x slower  |
| go                         | 61.5 ms  | 137 ms: 2.23x slower   |
| comprehensions             | 8.64 us  | 19.4 us: 2.24x slower  |
| spectral_norm              | 42.8 ms  | 97.7 ms: 2.28x slower  |
| generators                 | 14.8 ms  | 33.8 ms: 2.29x slower  |
| deepcopy_memo              | 14.0 us  | 32.9 us: 2.35x slower  |
| hexiom                     | 2.98 ms  | 7.27 ms: 2.44x slower  |
| deltablue                  | 1.64 ms  | 4.09 ms: 2.49x slower  |
| unpickle_pure_python       | 107 us   | 274 us: 2.56x slower   |
| scimark_monte_carlo        | 28.6 ms  | 73.9 ms: 2.58x slower  |
| mdp                        | 682 ms   | 1.81 sec: 2.66x slower |
| scimark_lu                 | 43.5 ms  | 116 ms: 2.67x slower   |
| scimark_sor                | 49.3 ms  | 135 ms: 2.74x slower   |
| logging_silent             | 41.1 ns  | 119 ns: 2.90x slower   |
| Geometric mean             | (ref)    | 1.67x slower           |
Ignored benchmarks (1) of default.json: thrift

- Geometric mean (including insignificant results): 1.401x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.57x
- 95% likely to have a slowdown of 1.56x
- 99% likely to have a slowdown of 1.53x

# Memory
- memory change: unknown