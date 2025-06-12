# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.187x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 204 ms: 1.11x faster   |
| docutils       | 1.71 sec | 1.55 sec: 1.10x faster |
| html5lib       | 40.5 ms  | 35.2 ms: 1.15x faster  |
| sphinx         | 670 ms   | 599 ms: 1.12x faster   |
| Geometric mean | (ref)    | 1.12x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| async_tree_none            | 186 ms  | 155 ms: 1.20x faster  |
| async_tree_io              | 417 ms  | 349 ms: 1.19x faster  |
| async_tree_none_tg         | 176 ms  | 147 ms: 1.19x faster  |
| coroutines                 | 13.1 ms | 11.1 ms: 1.18x faster |
| async_tree_memoization     | 223 ms  | 190 ms: 1.18x faster  |
| async_tree_io_tg           | 410 ms  | 352 ms: 1.17x faster  |
| async_generators           | 219 ms  | 188 ms: 1.16x faster  |
| async_tree_memoization_tg  | 219 ms  | 195 ms: 1.12x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 310 ms: 1.11x faster  |
| async_tree_cpu_io_mixed    | 340 ms  | 309 ms: 1.10x faster  |
| asyncio_websockets         | 311 ms  | 400 ms: 1.29x slower  |
| Geometric mean             | (ref)   | 1.12x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | clang-PGO             |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 52.9 ms: 1.48x faster |
| float          | 44.2 ms | 38.5 ms: 1.15x faster |
| Geometric mean | (ref)   | 1.19x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_compile  | 86.1 ms | 73.4 ms: 1.17x faster |
| regex_dna      | 116 ms  | 121 ms: 1.04x slower  |
| regex_effbot   | 1.46 ms | 1.65 ms: 1.13x slower |
| Geometric mean | (ref)   | 1.00x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 147 us   | 109 us: 1.35x faster   |
| tomli_loads          | 1.44 sec | 1.13 sec: 1.27x faster |
| pickle_pure_python   | 217 us   | 175 us: 1.24x faster   |
| xml_etree_generate   | 56.8 ms  | 48.4 ms: 1.17x faster  |
| xml_etree_process    | 39.7 ms  | 34.0 ms: 1.17x faster  |
| json_dumps           | 6.69 ms  | 5.76 ms: 1.16x faster  |
| json_loads           | 15.3 us  | 14.2 us: 1.08x faster  |
| xml_etree_iterparse  | 62.3 ms  | 60.7 ms: 1.03x faster  |
| Geometric mean       | (ref)    | 1.16x faster           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | clang-PGO             |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 20.0 ms: 1.07x slower |
| python_startup         | 24.5 ms | 26.6 ms: 1.09x slower |
| Geometric mean         | (ref)   | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 15.8 ms | 12.0 ms: 1.33x faster |
| django_template | 25.5 ms | 19.5 ms: 1.31x faster |
| genshi_xml      | 35.0 ms | 27.4 ms: 1.28x faster |
| mako            | 6.50 ms | 5.72 ms: 1.14x faster |
| Geometric mean  | (ref)   | 1.26x faster          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 41.0 ms  | 14.2 ms: 2.88x faster  |
| many_optionals             | 695 us   | 405 us: 1.71x faster   |
| richards_super             | 39.9 ms  | 24.6 ms: 1.62x faster  |
| richards                   | 34.5 ms  | 21.9 ms: 1.58x faster  |
| nbody                      | 78.3 ms  | 52.9 ms: 1.48x faster  |
| raytrace                   | 201 ms   | 137 ms: 1.46x faster   |
| scimark_sor                | 84.2 ms  | 59.1 ms: 1.43x faster  |
| scimark_monte_carlo        | 45.3 ms  | 32.8 ms: 1.38x faster  |
| deltablue                  | 2.18 ms  | 1.59 ms: 1.37x faster  |
| hexiom                     | 4.28 ms  | 3.13 ms: 1.37x faster  |
| chaos                      | 42.2 ms  | 31.1 ms: 1.36x faster  |
| unpickle_pure_python       | 147 us   | 109 us: 1.35x faster   |
| genshi_text                | 15.8 ms  | 12.0 ms: 1.33x faster  |
| scimark_fft                | 187 ms   | 143 ms: 1.31x faster   |
| django_template            | 25.5 ms  | 19.5 ms: 1.31x faster  |
| nqueens                    | 62.2 ms  | 47.7 ms: 1.30x faster  |
| spectral_norm              | 58.1 ms  | 44.7 ms: 1.30x faster  |
| go                         | 84.1 ms  | 65.1 ms: 1.29x faster  |
| logging_silent             | 57.0 ns  | 44.5 ns: 1.28x faster  |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.05 ms: 1.28x faster  |
| deepcopy                   | 185 us   | 145 us: 1.28x faster   |
| genshi_xml                 | 35.0 ms  | 27.4 ms: 1.28x faster  |
| sqlglot_v2_normalize       | 76.3 ms  | 59.9 ms: 1.27x faster  |
| tomli_loads                | 1.44 sec | 1.13 sec: 1.27x faster |
| generators                 | 20.0 ms  | 15.8 ms: 1.27x faster  |
| deepcopy_memo              | 19.1 us  | 15.1 us: 1.27x faster  |
| sqlglot_v2_parse           | 870 us   | 686 us: 1.27x faster   |
| comprehensions             | 11.2 us  | 8.84 us: 1.26x faster  |
| deepcopy_reduce            | 1.88 us  | 1.49 us: 1.26x faster  |
| sqlglot_v2_transpile       | 1.09 ms  | 868 us: 1.26x faster   |
| fannkuch                   | 263 ms   | 209 ms: 1.26x faster   |
| mdp                        | 1.62 sec | 1.30 sec: 1.25x faster |
| pprint_pformat             | 1.09 sec | 874 ms: 1.24x faster   |
| scimark_lu                 | 61.1 ms  | 49.1 ms: 1.24x faster  |
| pickle_pure_python         | 217 us   | 175 us: 1.24x faster   |
| crypto_pyaes               | 48.6 ms  | 39.4 ms: 1.23x faster  |
| pprint_safe_repr           | 532 ms   | 432 ms: 1.23x faster   |
| typing_runtime_protocols   | 106 us   | 86.2 us: 1.23x faster  |
| pyflate                    | 300 ms   | 245 ms: 1.23x faster   |
| logging_format             | 7.11 us  | 5.83 us: 1.22x faster  |
| logging_simple             | 6.53 us  | 5.39 us: 1.21x faster  |
| thrift                     | 522 us   | 434 us: 1.20x faster   |
| coverage                   | 49.2 ms  | 40.9 ms: 1.20x faster  |
| async_tree_none            | 186 ms   | 155 ms: 1.20x faster   |
| sqlglot_v2_optimize        | 35.6 ms  | 29.8 ms: 1.20x faster  |
| async_tree_io              | 417 ms   | 349 ms: 1.19x faster   |
| async_tree_none_tg         | 176 ms   | 147 ms: 1.19x faster   |
| coroutines                 | 13.1 ms  | 11.1 ms: 1.18x faster  |
| sympy_expand               | 305 ms   | 259 ms: 1.18x faster   |
| async_tree_memoization     | 223 ms   | 190 ms: 1.18x faster   |
| xml_etree_generate         | 56.8 ms  | 48.4 ms: 1.17x faster  |
| regex_compile              | 86.1 ms  | 73.4 ms: 1.17x faster  |
| bpe_tokeniser              | 2.93 sec | 2.50 sec: 1.17x faster |
| pycparser                  | 745 ms   | 637 ms: 1.17x faster   |
| xml_etree_process          | 39.7 ms  | 34.0 ms: 1.17x faster  |
| async_tree_io_tg           | 410 ms   | 352 ms: 1.17x faster   |
| json_dumps                 | 6.69 ms  | 5.76 ms: 1.16x faster  |
| async_generators           | 219 ms   | 188 ms: 1.16x faster   |
| sympy_str                  | 177 ms   | 153 ms: 1.16x faster   |
| sympy_integrate            | 13.6 ms  | 11.8 ms: 1.16x faster  |
| float                      | 44.2 ms  | 38.5 ms: 1.15x faster  |
| html5lib                   | 40.5 ms  | 35.2 ms: 1.15x faster  |
| pylint                     | 208 ms   | 182 ms: 1.14x faster   |
| mako                       | 6.50 ms  | 5.72 ms: 1.14x faster  |
| telco                      | 4.75 ms  | 4.20 ms: 1.13x faster  |
| async_tree_memoization_tg  | 219 ms   | 195 ms: 1.12x faster   |
| sphinx                     | 670 ms   | 599 ms: 1.12x faster   |
| sympy_sum                  | 90.8 ms  | 81.4 ms: 1.12x faster  |
| json                       | 3.16 ms  | 2.83 ms: 1.12x faster  |
| 2to3                       | 227 ms   | 204 ms: 1.11x faster   |
| async_tree_cpu_io_mixed_tg | 344 ms   | 310 ms: 1.11x faster   |
| docutils                   | 1.71 sec | 1.55 sec: 1.10x faster |
| async_tree_cpu_io_mixed    | 340 ms   | 309 ms: 1.10x faster   |
| meteor_contest             | 74.3 ms  | 68.7 ms: 1.08x faster  |
| json_loads                 | 15.3 us  | 14.2 us: 1.08x faster  |
| k_core                     | 1.73 sec | 1.61 sec: 1.08x faster |
| dulwich_log                | 42.4 ms  | 39.5 ms: 1.07x faster  |
| sqlite_synth               | 1.57 us  | 1.49 us: 1.05x faster  |
| shortest_path              | 354 ms   | 345 ms: 1.03x faster   |
| xml_etree_iterparse        | 62.3 ms  | 60.7 ms: 1.03x faster  |
| regex_dna                  | 116 ms   | 121 ms: 1.04x slower   |
| python_startup_no_site     | 18.7 ms  | 20.0 ms: 1.07x slower  |
| python_startup             | 24.5 ms  | 26.6 ms: 1.09x slower  |
| create_gc_cycles           | 1.25 ms  | 1.37 ms: 1.10x slower  |
| regex_effbot               | 1.46 ms  | 1.65 ms: 1.13x slower  |
| pathlib                    | 24.6 ms  | 30.4 ms: 1.23x slower  |
| asyncio_websockets         | 311 ms   | 400 ms: 1.29x slower   |
| gc_traversal               | 2.07 ms  | 2.79 ms: 1.35x slower  |
| Geometric mean             | (ref)    | 1.19x faster           |

Benchmark hidden because not significant (4): regex_v8, xml_etree_parse, pidigits, connected_components

- Geometric mean (including insignificant results): 1.187x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown