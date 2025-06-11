# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 204 ms: 1.11x faster   |
| docutils       | 1.71 sec | 1.58 sec: 1.08x faster |
| html5lib       | 40.5 ms  | 35.5 ms: 1.14x faster  |
| sphinx         | 670 ms   | 615 ms: 1.09x faster   |
| Geometric mean | (ref)    | 1.11x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.1 ms | 10.8 ms: 1.22x faster |
| async_tree_none            | 186 ms  | 157 ms: 1.18x faster  |
| async_tree_io              | 417 ms  | 353 ms: 1.18x faster  |
| async_tree_none_tg         | 176 ms  | 150 ms: 1.17x faster  |
| async_tree_io_tg           | 410 ms  | 356 ms: 1.15x faster  |
| async_tree_memoization     | 223 ms  | 196 ms: 1.14x faster  |
| async_generators           | 219 ms  | 199 ms: 1.10x faster  |
| async_tree_memoization_tg  | 219 ms  | 201 ms: 1.09x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 325 ms: 1.06x faster  |
| async_tree_cpu_io_mixed    | 340 ms  | 327 ms: 1.04x faster  |
| asyncio_websockets         | 311 ms  | 304 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.12x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 45.7 ms: 1.71x faster |
| float          | 44.2 ms | 37.1 ms: 1.19x faster |
| pidigits       | 148 ms  | 145 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.28x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 86.1 ms | 70.7 ms: 1.22x faster |
| regex_dna      | 116 ms  | 121 ms: 1.04x slower  |
| Geometric mean | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.44 sec | 1.03 sec: 1.40x faster |
| unpickle_pure_python | 147 us   | 110 us: 1.34x faster   |
| pickle_pure_python   | 217 us   | 184 us: 1.18x faster   |
| xml_etree_process    | 39.7 ms  | 33.8 ms: 1.18x faster  |
| xml_etree_generate   | 56.8 ms  | 49.4 ms: 1.15x faster  |
| json_dumps           | 6.69 ms  | 6.19 ms: 1.08x faster  |
| xml_etree_iterparse  | 62.3 ms  | 59.5 ms: 1.05x faster  |
| json_loads           | 15.3 us  | 14.8 us: 1.04x faster  |
| xml_etree_parse      | 88.8 ms  | 89.4 ms: 1.01x slower  |
| Geometric mean       | (ref)    | 1.15x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| python_startup | 24.5 ms | 24.7 ms: 1.01x slower |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 15.8 ms | 12.3 ms: 1.28x faster |
| django_template | 25.5 ms | 20.9 ms: 1.22x faster |
| genshi_xml      | 35.0 ms | 29.5 ms: 1.19x faster |
| mako            | 6.50 ms | 5.80 ms: 1.12x faster |
| Geometric mean  | (ref)   | 1.20x faster          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 78.3 ms  | 45.7 ms: 1.71x faster  |
| scimark_sor                | 84.2 ms  | 51.1 ms: 1.65x faster  |
| scimark_monte_carlo        | 45.3 ms  | 31.5 ms: 1.44x faster  |
| hexiom                     | 4.28 ms  | 3.00 ms: 1.43x faster  |
| spectral_norm              | 58.1 ms  | 40.9 ms: 1.42x faster  |
| generators                 | 20.0 ms  | 14.2 ms: 1.41x faster  |
| tomli_loads                | 1.44 sec | 1.03 sec: 1.40x faster |
| raytrace                   | 201 ms   | 145 ms: 1.39x faster   |
| go                         | 84.1 ms  | 61.0 ms: 1.38x faster  |
| scimark_lu                 | 61.1 ms  | 44.3 ms: 1.38x faster  |
| richards_super             | 39.9 ms  | 29.4 ms: 1.36x faster  |
| richards                   | 34.5 ms  | 25.5 ms: 1.35x faster  |
| chaos                      | 42.2 ms  | 31.3 ms: 1.35x faster  |
| unpickle_pure_python       | 147 us   | 110 us: 1.34x faster   |
| scimark_fft                | 187 ms   | 140 ms: 1.33x faster   |
| deltablue                  | 2.18 ms  | 1.64 ms: 1.33x faster  |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.02 ms: 1.30x faster  |
| deepcopy_memo              | 19.1 us  | 14.7 us: 1.30x faster  |
| logging_silent             | 57.0 ns  | 44.1 ns: 1.29x faster  |
| fannkuch                   | 263 ms   | 203 ms: 1.29x faster   |
| comprehensions             | 11.2 us  | 8.65 us: 1.29x faster  |
| genshi_text                | 15.8 ms  | 12.3 ms: 1.28x faster  |
| pprint_pformat             | 1.09 sec | 853 ms: 1.28x faster   |
| pyflate                    | 300 ms   | 236 ms: 1.27x faster   |
| deepcopy                   | 185 us   | 147 us: 1.26x faster   |
| sqlglot_v2_parse           | 870 us   | 695 us: 1.25x faster   |
| nqueens                    | 62.2 ms  | 49.7 ms: 1.25x faster  |
| deepcopy_reduce            | 1.88 us  | 1.51 us: 1.24x faster  |
| pprint_safe_repr           | 532 ms   | 429 ms: 1.24x faster   |
| sqlglot_v2_transpile       | 1.09 ms  | 894 us: 1.22x faster   |
| sqlglot_v2_normalize       | 76.3 ms  | 62.6 ms: 1.22x faster  |
| django_template            | 25.5 ms  | 20.9 ms: 1.22x faster  |
| regex_compile              | 86.1 ms  | 70.7 ms: 1.22x faster  |
| coroutines                 | 13.1 ms  | 10.8 ms: 1.22x faster  |
| logging_simple             | 6.53 us  | 5.42 us: 1.21x faster  |
| logging_format             | 7.11 us  | 5.90 us: 1.20x faster  |
| crypto_pyaes               | 48.6 ms  | 40.4 ms: 1.20x faster  |
| float                      | 44.2 ms  | 37.1 ms: 1.19x faster  |
| genshi_xml                 | 35.0 ms  | 29.5 ms: 1.19x faster  |
| typing_runtime_protocols   | 106 us   | 89.7 us: 1.18x faster  |
| pickle_pure_python         | 217 us   | 184 us: 1.18x faster   |
| async_tree_none            | 186 ms   | 157 ms: 1.18x faster   |
| async_tree_io              | 417 ms   | 353 ms: 1.18x faster   |
| xml_etree_process          | 39.7 ms  | 33.8 ms: 1.18x faster  |
| async_tree_none_tg         | 176 ms   | 150 ms: 1.17x faster   |
| sqlglot_v2_optimize        | 35.6 ms  | 30.5 ms: 1.17x faster  |
| bpe_tokeniser              | 2.93 sec | 2.52 sec: 1.16x faster |
| sympy_expand               | 305 ms   | 263 ms: 1.16x faster   |
| pycparser                  | 745 ms   | 642 ms: 1.16x faster   |
| async_tree_io_tg           | 410 ms   | 356 ms: 1.15x faster   |
| mdp                        | 1.62 sec | 1.41 sec: 1.15x faster |
| sympy_str                  | 177 ms   | 153 ms: 1.15x faster   |
| xml_etree_generate         | 56.8 ms  | 49.4 ms: 1.15x faster  |
| html5lib                   | 40.5 ms  | 35.5 ms: 1.14x faster  |
| async_tree_memoization     | 223 ms   | 196 ms: 1.14x faster   |
| sympy_integrate            | 13.6 ms  | 12.0 ms: 1.14x faster  |
| thrift                     | 522 us   | 461 us: 1.13x faster   |
| sympy_sum                  | 90.8 ms  | 80.7 ms: 1.13x faster  |
| mako                       | 6.50 ms  | 5.80 ms: 1.12x faster  |
| meteor_contest             | 74.3 ms  | 66.6 ms: 1.12x faster  |
| 2to3                       | 227 ms   | 204 ms: 1.11x faster   |
| async_generators           | 219 ms   | 199 ms: 1.10x faster   |
| async_tree_memoization_tg  | 219 ms   | 201 ms: 1.09x faster   |
| sphinx                     | 670 ms   | 615 ms: 1.09x faster   |
| dulwich_log                | 42.4 ms  | 39.1 ms: 1.08x faster  |
| pylint                     | 208 ms   | 193 ms: 1.08x faster   |
| docutils                   | 1.71 sec | 1.58 sec: 1.08x faster |
| json_dumps                 | 6.69 ms  | 6.19 ms: 1.08x faster  |
| telco                      | 4.75 ms  | 4.45 ms: 1.07x faster  |
| json                       | 3.16 ms  | 2.95 ms: 1.07x faster  |
| coverage                   | 49.2 ms  | 46.2 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms   | 325 ms: 1.06x faster   |
| many_optionals             | 695 us   | 659 us: 1.05x faster   |
| xml_etree_iterparse        | 62.3 ms  | 59.5 ms: 1.05x faster  |
| pathlib                    | 24.6 ms  | 23.6 ms: 1.04x faster  |
| async_tree_cpu_io_mixed    | 340 ms   | 327 ms: 1.04x faster   |
| json_loads                 | 15.3 us  | 14.8 us: 1.04x faster  |
| k_core                     | 1.73 sec | 1.67 sec: 1.04x faster |
| asyncio_websockets         | 311 ms   | 304 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 145 ms: 1.02x faster   |
| shortest_path              | 354 ms   | 347 ms: 1.02x faster   |
| subparsers                 | 41.0 ms  | 40.6 ms: 1.01x faster  |
| connected_components       | 324 ms   | 320 ms: 1.01x faster   |
| sqlite_synth               | 1.57 us  | 1.56 us: 1.01x faster  |
| xml_etree_parse            | 88.8 ms  | 89.4 ms: 1.01x slower  |
| python_startup             | 24.5 ms  | 24.7 ms: 1.01x slower  |
| create_gc_cycles           | 1.25 ms  | 1.26 ms: 1.01x slower  |
| regex_dna                  | 116 ms   | 121 ms: 1.04x slower   |
| Geometric mean             | (ref)    | 1.17x faster           |

Benchmark hidden because not significant (4): regex_effbot, python_startup_no_site, gc_traversal, regex_v8

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown