# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.386x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 231 ms: 1.29x faster   |
| docutils       | 2.17 sec | 1.77 sec: 1.23x faster |
| html5lib       | 51.3 ms  | 38.8 ms: 1.32x faster  |
| sphinx         | 872 ms   | 702 ms: 1.24x faster   |
| Geometric mean | (ref)    | 1.27x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 21.9 ms | 12.3 ms: 1.79x faster |
| async_generators           | 328 ms  | 213 ms: 1.54x faster  |
| async_tree_io_tg           | 559 ms  | 385 ms: 1.45x faster  |
| async_tree_io              | 553 ms  | 384 ms: 1.44x faster  |
| async_tree_none            | 249 ms  | 174 ms: 1.44x faster  |
| async_tree_memoization     | 297 ms  | 210 ms: 1.42x faster  |
| async_tree_none_tg         | 236 ms  | 167 ms: 1.41x faster  |
| async_tree_memoization_tg  | 291 ms  | 210 ms: 1.38x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 359 ms: 1.21x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms  | 363 ms: 1.17x faster  |
| asyncio_websockets         | 317 ms  | 312 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.37x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 101 ms  | 53.1 ms: 1.89x faster |
| float          | 75.4 ms | 41.4 ms: 1.82x faster |
| pidigits       | 152 ms  | 146 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.53x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 125 ms  | 81.9 ms: 1.52x faster |
| regex_v8       | 17.1 ms | 16.3 ms: 1.05x faster |
| regex_effbot   | 1.81 ms | 1.85 ms: 1.02x slower |
| Geometric mean | (ref)   | 1.12x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 274 us   | 148 us: 1.85x faster   |
| pickle_pure_python   | 355 us   | 223 us: 1.59x faster   |
| tomli_loads          | 1.99 sec | 1.26 sec: 1.58x faster |
| xml_etree_process    | 64.6 ms  | 44.7 ms: 1.44x faster  |
| xml_etree_generate   | 89.5 ms  | 64.7 ms: 1.38x faster  |
| xml_etree_iterparse  | 89.9 ms  | 70.4 ms: 1.28x faster  |
| json_dumps           | 9.01 ms  | 7.79 ms: 1.16x faster  |
| xml_etree_parse      | 108 ms   | 105 ms: 1.03x faster   |
| json_loads           | 22.3 us  | 21.9 us: 1.02x faster  |
| Geometric mean       | (ref)    | 1.35x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | default | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.4 ms | 19.4 ms: 1.05x faster |
| python_startup         | 27.3 ms | 26.4 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.04x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TC-Ex                 |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 23.2 ms | 14.5 ms: 1.60x faster |
| genshi_xml      | 48.8 ms | 31.3 ms: 1.56x faster |
| mako            | 11.7 ms | 7.84 ms: 1.49x faster |
| django_template | 36.9 ms | 25.2 ms: 1.46x faster |
| Geometric mean  | (ref)   | 1.53x faster          |

All benchmarks:
===============

| Benchmark                  | default  | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| deltablue                  | 4.09 ms  | 1.91 ms: 2.14x faster  |
| generators                 | 33.8 ms  | 16.3 ms: 2.07x faster  |
| scimark_sor                | 135 ms   | 68.6 ms: 1.97x faster  |
| logging_silent             | 119 ns   | 61.1 ns: 1.95x faster  |
| go                         | 137 ms   | 70.4 ms: 1.94x faster  |
| spectral_norm              | 97.7 ms  | 51.1 ms: 1.91x faster  |
| scimark_monte_carlo        | 73.9 ms  | 38.9 ms: 1.90x faster  |
| nbody                      | 101 ms   | 53.1 ms: 1.89x faster  |
| richards                   | 57.8 ms  | 30.9 ms: 1.87x faster  |
| hexiom                     | 7.27 ms  | 3.92 ms: 1.86x faster  |
| unpickle_pure_python       | 274 us   | 148 us: 1.85x faster   |
| richards_super             | 65.8 ms  | 35.8 ms: 1.84x faster  |
| float                      | 75.4 ms  | 41.4 ms: 1.82x faster  |
| scimark_lu                 | 116 ms   | 64.2 ms: 1.81x faster  |
| raytrace                   | 304 ms   | 169 ms: 1.79x faster   |
| coroutines                 | 21.9 ms  | 12.3 ms: 1.79x faster  |
| scimark_sparse_mat_mult    | 4.34 ms  | 2.47 ms: 1.76x faster  |
| chaos                      | 65.2 ms  | 37.7 ms: 1.73x faster  |
| comprehensions             | 19.4 us  | 11.3 us: 1.71x faster  |
| deepcopy_memo              | 32.9 us  | 19.3 us: 1.71x faster  |
| sqlglot_v2_parse           | 1.36 ms  | 798 us: 1.70x faster   |
| pyflate                    | 462 ms   | 274 ms: 1.69x faster   |
| fannkuch                   | 407 ms   | 250 ms: 1.63x faster   |
| crypto_pyaes               | 77.9 ms  | 48.0 ms: 1.62x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 1.01 ms: 1.62x faster  |
| genshi_text                | 23.2 ms  | 14.5 ms: 1.60x faster  |
| pickle_pure_python         | 355 us   | 223 us: 1.59x faster   |
| scimark_fft                | 269 ms   | 169 ms: 1.59x faster   |
| nqueens                    | 94.3 ms  | 59.6 ms: 1.58x faster  |
| tomli_loads                | 1.99 sec | 1.26 sec: 1.58x faster |
| genshi_xml                 | 48.8 ms  | 31.3 ms: 1.56x faster  |
| pprint_pformat             | 1.61 sec | 1.04 sec: 1.55x faster |
| pprint_safe_repr           | 788 ms   | 510 ms: 1.54x faster   |
| async_generators           | 328 ms   | 213 ms: 1.54x faster   |
| regex_compile              | 125 ms   | 81.9 ms: 1.52x faster  |
| deepcopy                   | 269 us   | 180 us: 1.49x faster   |
| mako                       | 11.7 ms  | 7.84 ms: 1.49x faster  |
| django_template            | 36.9 ms  | 25.2 ms: 1.46x faster  |
| deepcopy_reduce            | 2.77 us  | 1.90 us: 1.46x faster  |
| async_tree_io_tg           | 559 ms   | 385 ms: 1.45x faster   |
| sqlglot_v2_normalize       | 106 ms   | 73.3 ms: 1.45x faster  |
| xml_etree_process          | 64.6 ms  | 44.7 ms: 1.44x faster  |
| async_tree_io              | 553 ms   | 384 ms: 1.44x faster   |
| async_tree_none            | 249 ms   | 174 ms: 1.44x faster   |
| bpe_tokeniser              | 4.30 sec | 3.01 sec: 1.43x faster |
| typing_runtime_protocols   | 150 us   | 106 us: 1.42x faster   |
| logging_simple             | 8.87 us  | 6.25 us: 1.42x faster  |
| async_tree_memoization     | 297 ms   | 210 ms: 1.42x faster   |
| async_tree_none_tg         | 236 ms   | 167 ms: 1.41x faster   |
| sqlglot_v2_optimize        | 51.0 ms  | 36.1 ms: 1.41x faster  |
| logging_format             | 9.33 us  | 6.70 us: 1.39x faster  |
| pycparser                  | 992 ms   | 713 ms: 1.39x faster   |
| async_tree_memoization_tg  | 291 ms   | 210 ms: 1.38x faster   |
| xml_etree_generate         | 89.5 ms  | 64.7 ms: 1.38x faster  |
| pathlib                    | 34.4 ms  | 25.1 ms: 1.37x faster  |
| sympy_str                  | 238 ms   | 177 ms: 1.35x faster   |
| sympy_expand               | 405 ms   | 304 ms: 1.33x faster   |
| sympy_integrate            | 17.8 ms  | 13.4 ms: 1.33x faster  |
| html5lib                   | 51.3 ms  | 38.8 ms: 1.32x faster  |
| sympy_sum                  | 119 ms   | 91.4 ms: 1.31x faster  |
| 2to3                       | 298 ms   | 231 ms: 1.29x faster   |
| meteor_contest             | 95.9 ms  | 74.5 ms: 1.29x faster  |
| xml_etree_iterparse        | 89.9 ms  | 70.4 ms: 1.28x faster  |
| thrift                     | 694 us   | 551 us: 1.26x faster   |
| mdp                        | 1.81 sec | 1.44 sec: 1.26x faster |
| sphinx                     | 872 ms   | 702 ms: 1.24x faster   |
| pylint                     | 253 ms   | 205 ms: 1.23x faster   |
| docutils                   | 2.17 sec | 1.77 sec: 1.23x faster |
| telco                      | 6.44 ms  | 5.26 ms: 1.22x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 359 ms: 1.21x faster   |
| dulwich_log                | 51.0 ms  | 42.3 ms: 1.21x faster  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 363 ms: 1.17x faster   |
| json_dumps                 | 9.01 ms  | 7.79 ms: 1.16x faster  |
| bench_thread_pool          | 1.01 ms  | 876 us: 1.15x faster   |
| coverage                   | 61.9 ms  | 55.4 ms: 1.12x faster  |
| connected_components       | 347 ms   | 311 ms: 1.11x faster   |
| gc_traversal               | 3.15 ms  | 2.83 ms: 1.11x faster  |
| sqlite_synth               | 1.84 us  | 1.68 us: 1.10x faster  |
| shortest_path              | 378 ms   | 347 ms: 1.09x faster   |
| k_core                     | 1.83 sec | 1.71 sec: 1.07x faster |
| python_startup_no_site     | 20.4 ms  | 19.4 ms: 1.05x faster  |
| regex_v8                   | 17.1 ms  | 16.3 ms: 1.05x faster  |
| create_gc_cycles           | 1.40 ms  | 1.34 ms: 1.05x faster  |
| json                       | 3.96 ms  | 3.78 ms: 1.05x faster  |
| pidigits                   | 152 ms   | 146 ms: 1.04x faster   |
| python_startup             | 27.3 ms  | 26.4 ms: 1.04x faster  |
| xml_etree_parse            | 108 ms   | 105 ms: 1.03x faster   |
| bench_mp_pool              | 96.2 ms  | 93.6 ms: 1.03x faster  |
| json_loads                 | 22.3 us  | 21.9 us: 1.02x faster  |
| asyncio_websockets         | 317 ms   | 312 ms: 1.02x faster   |
| regex_effbot               | 1.81 ms  | 1.85 ms: 1.02x slower  |
| many_optionals             | 547 us   | 762 us: 1.39x slower   |
| subparsers                 | 20.8 ms  | 44.5 ms: 2.14x slower  |
| Geometric mean             | (ref)    | 1.39x faster           |

Benchmark hidden because not significant (1): regex_dna

- Geometric mean (including insignificant results): 1.386x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: unknown