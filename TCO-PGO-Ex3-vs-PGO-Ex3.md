# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 215 ms: 1.05x faster   |
| docutils       | 1.71 sec | 1.66 sec: 1.03x faster |
| html5lib       | 40.5 ms  | 37.8 ms: 1.07x faster  |
| sphinx         | 670 ms   | 641 ms: 1.04x faster   |
| Geometric mean | (ref)    | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.1 ms | 12.0 ms: 1.10x faster |
| async_tree_none_tg         | 176 ms  | 161 ms: 1.09x faster  |
| async_tree_none            | 186 ms  | 170 ms: 1.09x faster  |
| async_tree_io              | 417 ms  | 382 ms: 1.09x faster  |
| async_tree_io_tg           | 410 ms  | 377 ms: 1.09x faster  |
| async_tree_memoization     | 223 ms  | 205 ms: 1.09x faster  |
| async_generators           | 219 ms  | 201 ms: 1.09x faster  |
| async_tree_memoization_tg  | 219 ms  | 208 ms: 1.05x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 330 ms: 1.04x faster  |
| async_tree_cpu_io_mixed    | 340 ms  | 330 ms: 1.03x faster  |
| Geometric mean             | (ref)   | 1.07x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 55.6 ms: 1.41x faster |
| float          | 44.2 ms | 42.0 ms: 1.05x faster |
| pidigits       | 148 ms  | 145 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.15x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 86.1 ms | 79.4 ms: 1.08x faster |
| regex_effbot   | 1.46 ms | 1.47 ms: 1.01x slower |
| regex_dna      | 116 ms  | 120 ms: 1.03x slower  |
| regex_v8       | 13.8 ms | 14.2 ms: 1.03x slower |
| Geometric mean | (ref)   | 1.00x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.44 sec | 1.17 sec: 1.22x faster |
| unpickle_pure_python | 147 us   | 124 us: 1.18x faster   |
| pickle_pure_python   | 217 us   | 199 us: 1.09x faster   |
| xml_etree_process    | 39.7 ms  | 36.8 ms: 1.08x faster  |
| xml_etree_generate   | 56.8 ms  | 53.1 ms: 1.07x faster  |
| json_loads           | 15.3 us  | 14.5 us: 1.06x faster  |
| json_dumps           | 6.69 ms  | 6.40 ms: 1.04x faster  |
| xml_etree_iterparse  | 62.3 ms  | 61.2 ms: 1.02x faster  |
| xml_etree_parse      | 88.8 ms  | 89.4 ms: 1.01x slower  |
| Geometric mean       | (ref)    | 1.08x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| python_startup | 24.5 ms | 24.7 ms: 1.01x slower |
| Geometric mean | (ref)   | 1.00x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 15.8 ms | 14.3 ms: 1.11x faster |
| django_template | 25.5 ms | 23.6 ms: 1.08x faster |
| genshi_xml      | 35.0 ms | 32.3 ms: 1.08x faster |
| mako            | 6.50 ms | 6.25 ms: 1.04x faster |
| Geometric mean  | (ref)   | 1.08x faster          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 78.3 ms  | 55.6 ms: 1.41x faster  |
| scimark_sor                | 84.2 ms  | 60.5 ms: 1.39x faster  |
| scimark_monte_carlo        | 45.3 ms  | 35.6 ms: 1.27x faster  |
| raytrace                   | 201 ms   | 162 ms: 1.25x faster   |
| hexiom                     | 4.28 ms  | 3.49 ms: 1.22x faster  |
| tomli_loads                | 1.44 sec | 1.17 sec: 1.22x faster |
| scimark_fft                | 187 ms   | 153 ms: 1.22x faster   |
| generators                 | 20.0 ms  | 16.5 ms: 1.22x faster  |
| scimark_lu                 | 61.1 ms  | 50.3 ms: 1.21x faster  |
| go                         | 84.1 ms  | 70.5 ms: 1.19x faster  |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.21 ms: 1.19x faster  |
| chaos                      | 42.2 ms  | 35.4 ms: 1.19x faster  |
| richards_super             | 39.9 ms  | 33.7 ms: 1.19x faster  |
| unpickle_pure_python       | 147 us   | 124 us: 1.18x faster   |
| spectral_norm              | 58.1 ms  | 49.4 ms: 1.18x faster  |
| richards                   | 34.5 ms  | 29.4 ms: 1.18x faster  |
| fannkuch                   | 263 ms   | 225 ms: 1.17x faster   |
| deltablue                  | 2.18 ms  | 1.88 ms: 1.16x faster  |
| logging_silent             | 57.0 ns  | 49.7 ns: 1.15x faster  |
| comprehensions             | 11.2 us  | 9.76 us: 1.15x faster  |
| mdp                        | 1.62 sec | 1.43 sec: 1.14x faster |
| pprint_pformat             | 1.09 sec | 956 ms: 1.14x faster   |
| deepcopy_memo              | 19.1 us  | 16.8 us: 1.13x faster  |
| pyflate                    | 300 ms   | 264 ms: 1.13x faster   |
| nqueens                    | 62.2 ms  | 55.2 ms: 1.13x faster  |
| deepcopy_reduce            | 1.88 us  | 1.68 us: 1.12x faster  |
| pprint_safe_repr           | 532 ms   | 474 ms: 1.12x faster   |
| sqlglot_v2_parse           | 870 us   | 781 us: 1.11x faster   |
| logging_simple             | 6.53 us  | 5.87 us: 1.11x faster  |
| genshi_text                | 15.8 ms  | 14.3 ms: 1.11x faster  |
| logging_format             | 7.11 us  | 6.42 us: 1.11x faster  |
| deepcopy                   | 185 us   | 167 us: 1.11x faster   |
| crypto_pyaes               | 48.6 ms  | 43.9 ms: 1.11x faster  |
| sqlglot_v2_normalize       | 76.3 ms  | 69.0 ms: 1.11x faster  |
| sqlglot_v2_transpile       | 1.09 ms  | 993 us: 1.10x faster   |
| coroutines                 | 13.1 ms  | 12.0 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms   | 161 ms: 1.09x faster   |
| async_tree_none            | 186 ms   | 170 ms: 1.09x faster   |
| pickle_pure_python         | 217 us   | 199 us: 1.09x faster   |
| async_tree_io              | 417 ms   | 382 ms: 1.09x faster   |
| async_tree_io_tg           | 410 ms   | 377 ms: 1.09x faster   |
| async_tree_memoization     | 223 ms   | 205 ms: 1.09x faster   |
| async_generators           | 219 ms   | 201 ms: 1.09x faster   |
| regex_compile              | 86.1 ms  | 79.4 ms: 1.08x faster  |
| typing_runtime_protocols   | 106 us   | 97.8 us: 1.08x faster  |
| django_template            | 25.5 ms  | 23.6 ms: 1.08x faster  |
| genshi_xml                 | 35.0 ms  | 32.3 ms: 1.08x faster  |
| pycparser                  | 745 ms   | 689 ms: 1.08x faster   |
| sqlglot_v2_optimize        | 35.6 ms  | 32.9 ms: 1.08x faster  |
| sympy_expand               | 305 ms   | 283 ms: 1.08x faster   |
| xml_etree_process          | 39.7 ms  | 36.8 ms: 1.08x faster  |
| bpe_tokeniser              | 2.93 sec | 2.72 sec: 1.08x faster |
| xml_etree_generate         | 56.8 ms  | 53.1 ms: 1.07x faster  |
| html5lib                   | 40.5 ms  | 37.8 ms: 1.07x faster  |
| sympy_sum                  | 90.8 ms  | 85.2 ms: 1.07x faster  |
| thrift                     | 522 us   | 491 us: 1.06x faster   |
| sympy_integrate            | 13.6 ms  | 12.8 ms: 1.06x faster  |
| json_loads                 | 15.3 us  | 14.5 us: 1.06x faster  |
| async_tree_memoization_tg  | 219 ms   | 208 ms: 1.05x faster   |
| float                      | 44.2 ms  | 42.0 ms: 1.05x faster  |
| 2to3                       | 227 ms   | 215 ms: 1.05x faster   |
| dulwich_log                | 42.4 ms  | 40.3 ms: 1.05x faster  |
| meteor_contest             | 74.3 ms  | 70.9 ms: 1.05x faster  |
| sphinx                     | 670 ms   | 641 ms: 1.04x faster   |
| async_tree_cpu_io_mixed_tg | 344 ms   | 330 ms: 1.04x faster   |
| json_dumps                 | 6.69 ms  | 6.40 ms: 1.04x faster  |
| mako                       | 6.50 ms  | 6.25 ms: 1.04x faster  |
| json                       | 3.16 ms  | 3.04 ms: 1.04x faster  |
| pylint                     | 208 ms   | 201 ms: 1.04x faster   |
| coverage                   | 49.2 ms  | 47.5 ms: 1.04x faster  |
| telco                      | 4.75 ms  | 4.59 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 340 ms   | 330 ms: 1.03x faster   |
| docutils                   | 1.71 sec | 1.66 sec: 1.03x faster |
| pidigits                   | 148 ms   | 145 ms: 1.02x faster   |
| sympy_str                  | 177 ms   | 173 ms: 1.02x faster   |
| pathlib                    | 24.6 ms  | 24.2 ms: 1.02x faster  |
| xml_etree_iterparse        | 62.3 ms  | 61.2 ms: 1.02x faster  |
| k_core                     | 1.73 sec | 1.70 sec: 1.02x faster |
| many_optionals             | 695 us   | 685 us: 1.01x faster   |
| shortest_path              | 354 ms   | 352 ms: 1.01x faster   |
| xml_etree_parse            | 88.8 ms  | 89.4 ms: 1.01x slower  |
| subparsers                 | 41.0 ms  | 41.4 ms: 1.01x slower  |
| python_startup             | 24.5 ms  | 24.7 ms: 1.01x slower  |
| regex_effbot               | 1.46 ms  | 1.47 ms: 1.01x slower  |
| gc_traversal               | 2.07 ms  | 2.12 ms: 1.02x slower  |
| regex_dna                  | 116 ms   | 120 ms: 1.03x slower   |
| regex_v8                   | 13.8 ms  | 14.2 ms: 1.03x slower  |
| Geometric mean             | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (5): sqlite_synth, python_startup_no_site, create_gc_cycles, connected_components, asyncio_websockets

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown