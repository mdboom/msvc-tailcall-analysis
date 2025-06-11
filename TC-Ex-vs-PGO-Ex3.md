# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.008x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 231 ms: 1.02x slower   |
| docutils       | 1.71 sec | 1.77 sec: 1.04x slower |
| html5lib       | 40.5 ms  | 38.8 ms: 1.04x faster  |
| sphinx         | 670 ms   | 702 ms: 1.05x slower   |
| Geometric mean | (ref)    | 1.01x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| async_tree_io              | 417 ms  | 384 ms: 1.09x faster  |
| coroutines                 | 13.1 ms | 12.3 ms: 1.07x faster |
| async_tree_none            | 186 ms  | 174 ms: 1.07x faster  |
| async_tree_io_tg           | 410 ms  | 385 ms: 1.07x faster  |
| async_tree_memoization     | 223 ms  | 210 ms: 1.06x faster  |
| async_tree_none_tg         | 176 ms  | 167 ms: 1.05x faster  |
| async_tree_memoization_tg  | 219 ms  | 210 ms: 1.04x faster  |
| async_generators           | 219 ms  | 213 ms: 1.02x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms  | 363 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 340 ms  | 359 ms: 1.06x slower  |
| Geometric mean             | (ref)   | 1.03x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 53.1 ms: 1.48x faster |
| float          | 44.2 ms | 41.4 ms: 1.07x faster |
| pidigits       | 148 ms  | 146 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.17x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 86.1 ms | 81.9 ms: 1.05x faster |
| regex_dna      | 116 ms  | 121 ms: 1.04x slower  |
| regex_v8       | 13.8 ms | 16.3 ms: 1.18x slower |
| regex_effbot   | 1.46 ms | 1.85 ms: 1.27x slower |
| Geometric mean | (ref)   | 1.10x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.44 sec | 1.26 sec: 1.14x faster |
| unpickle_pure_python | 147 us   | 148 us: 1.01x slower   |
| pickle_pure_python   | 217 us   | 223 us: 1.02x slower   |
| xml_etree_process    | 39.7 ms  | 44.7 ms: 1.13x slower  |
| xml_etree_iterparse  | 62.3 ms  | 70.4 ms: 1.13x slower  |
| xml_etree_generate   | 56.8 ms  | 64.7 ms: 1.14x slower  |
| json_dumps           | 6.69 ms  | 7.79 ms: 1.16x slower  |
| xml_etree_parse      | 88.8 ms  | 105 ms: 1.18x slower   |
| json_loads           | 15.3 us  | 21.9 us: 1.43x slower  |
| Geometric mean       | (ref)    | 1.11x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 19.4 ms: 1.04x slower |
| python_startup         | 24.5 ms | 26.4 ms: 1.08x slower |
| Geometric mean         | (ref)   | 1.06x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TC-Ex                 |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 31.3 ms: 1.12x faster |
| genshi_text     | 15.8 ms | 14.5 ms: 1.10x faster |
| django_template | 25.5 ms | 25.2 ms: 1.01x faster |
| mako            | 6.50 ms | 7.84 ms: 1.21x slower |
| Geometric mean  | (ref)   | 1.01x faster          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 78.3 ms  | 53.1 ms: 1.48x faster  |
| generators                 | 20.0 ms  | 16.3 ms: 1.23x faster  |
| scimark_sor                | 84.2 ms  | 68.6 ms: 1.23x faster  |
| go                         | 84.1 ms  | 70.4 ms: 1.19x faster  |
| raytrace                   | 201 ms   | 169 ms: 1.19x faster   |
| scimark_monte_carlo        | 45.3 ms  | 38.9 ms: 1.16x faster  |
| deltablue                  | 2.18 ms  | 1.91 ms: 1.14x faster  |
| tomli_loads                | 1.44 sec | 1.26 sec: 1.14x faster |
| spectral_norm              | 58.1 ms  | 51.1 ms: 1.14x faster  |
| mdp                        | 1.62 sec | 1.44 sec: 1.12x faster |
| richards                   | 34.5 ms  | 30.9 ms: 1.12x faster  |
| chaos                      | 42.2 ms  | 37.7 ms: 1.12x faster  |
| genshi_xml                 | 35.0 ms  | 31.3 ms: 1.12x faster  |
| richards_super             | 39.9 ms  | 35.8 ms: 1.12x faster  |
| scimark_fft                | 187 ms   | 169 ms: 1.11x faster   |
| genshi_text                | 15.8 ms  | 14.5 ms: 1.10x faster  |
| pyflate                    | 300 ms   | 274 ms: 1.10x faster   |
| hexiom                     | 4.28 ms  | 3.92 ms: 1.09x faster  |
| sqlglot_v2_parse           | 870 us   | 798 us: 1.09x faster   |
| async_tree_io              | 417 ms   | 384 ms: 1.09x faster   |
| sqlglot_v2_transpile       | 1.09 ms  | 1.01 ms: 1.08x faster  |
| coroutines                 | 13.1 ms  | 12.3 ms: 1.07x faster  |
| async_tree_none            | 186 ms   | 174 ms: 1.07x faster   |
| float                      | 44.2 ms  | 41.4 ms: 1.07x faster  |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.47 ms: 1.07x faster  |
| async_tree_io_tg           | 410 ms   | 385 ms: 1.07x faster   |
| async_tree_memoization     | 223 ms   | 210 ms: 1.06x faster   |
| logging_format             | 7.11 us  | 6.70 us: 1.06x faster  |
| async_tree_none_tg         | 176 ms   | 167 ms: 1.05x faster   |
| regex_compile              | 86.1 ms  | 81.9 ms: 1.05x faster  |
| fannkuch                   | 263 ms   | 250 ms: 1.05x faster   |
| pprint_pformat             | 1.09 sec | 1.04 sec: 1.05x faster |
| pycparser                  | 745 ms   | 713 ms: 1.05x faster   |
| logging_simple             | 6.53 us  | 6.25 us: 1.04x faster  |
| html5lib                   | 40.5 ms  | 38.8 ms: 1.04x faster  |
| nqueens                    | 62.2 ms  | 59.6 ms: 1.04x faster  |
| pprint_safe_repr           | 532 ms   | 510 ms: 1.04x faster   |
| connected_components       | 324 ms   | 311 ms: 1.04x faster   |
| sqlglot_v2_normalize       | 76.3 ms  | 73.3 ms: 1.04x faster  |
| async_tree_memoization_tg  | 219 ms   | 210 ms: 1.04x faster   |
| deepcopy                   | 185 us   | 180 us: 1.03x faster   |
| async_generators           | 219 ms   | 213 ms: 1.02x faster   |
| shortest_path              | 354 ms   | 347 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 146 ms: 1.02x faster   |
| sympy_integrate            | 13.6 ms  | 13.4 ms: 1.02x faster  |
| crypto_pyaes               | 48.6 ms  | 48.0 ms: 1.01x faster  |
| django_template            | 25.5 ms  | 25.2 ms: 1.01x faster  |
| sympy_sum                  | 90.8 ms  | 91.4 ms: 1.01x slower  |
| unpickle_pure_python       | 147 us   | 148 us: 1.01x slower   |
| deepcopy_reduce            | 1.88 us  | 1.90 us: 1.01x slower  |
| comprehensions             | 11.2 us  | 11.3 us: 1.01x slower  |
| sqlglot_v2_optimize        | 35.6 ms  | 36.1 ms: 1.01x slower  |
| 2to3                       | 227 ms   | 231 ms: 1.02x slower   |
| pathlib                    | 24.6 ms  | 25.1 ms: 1.02x slower  |
| pickle_pure_python         | 217 us   | 223 us: 1.02x slower   |
| bpe_tokeniser              | 2.93 sec | 3.01 sec: 1.03x slower |
| docutils                   | 1.71 sec | 1.77 sec: 1.04x slower |
| regex_dna                  | 116 ms   | 121 ms: 1.04x slower   |
| python_startup_no_site     | 18.7 ms  | 19.4 ms: 1.04x slower  |
| sphinx                     | 670 ms   | 702 ms: 1.05x slower   |
| scimark_lu                 | 61.1 ms  | 64.2 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 344 ms   | 363 ms: 1.05x slower   |
| thrift                     | 522 us   | 551 us: 1.05x slower   |
| async_tree_cpu_io_mixed    | 340 ms   | 359 ms: 1.06x slower   |
| sqlite_synth               | 1.57 us  | 1.68 us: 1.07x slower  |
| create_gc_cycles           | 1.25 ms  | 1.34 ms: 1.07x slower  |
| logging_silent             | 57.0 ns  | 61.1 ns: 1.07x slower  |
| python_startup             | 24.5 ms  | 26.4 ms: 1.08x slower  |
| subparsers                 | 41.0 ms  | 44.5 ms: 1.08x slower  |
| many_optionals             | 695 us   | 762 us: 1.10x slower   |
| telco                      | 4.75 ms  | 5.26 ms: 1.11x slower  |
| coverage                   | 49.2 ms  | 55.4 ms: 1.12x slower  |
| xml_etree_process          | 39.7 ms  | 44.7 ms: 1.13x slower  |
| xml_etree_iterparse        | 62.3 ms  | 70.4 ms: 1.13x slower  |
| xml_etree_generate         | 56.8 ms  | 64.7 ms: 1.14x slower  |
| json_dumps                 | 6.69 ms  | 7.79 ms: 1.16x slower  |
| xml_etree_parse            | 88.8 ms  | 105 ms: 1.18x slower   |
| regex_v8                   | 13.8 ms  | 16.3 ms: 1.18x slower  |
| json                       | 3.16 ms  | 3.78 ms: 1.20x slower  |
| mako                       | 6.50 ms  | 7.84 ms: 1.21x slower  |
| regex_effbot               | 1.46 ms  | 1.85 ms: 1.27x slower  |
| gc_traversal               | 2.07 ms  | 2.83 ms: 1.37x slower  |
| json_loads                 | 15.3 us  | 21.9 us: 1.43x slower  |
| Geometric mean             | (ref)    | 1.01x faster           |

Benchmark hidden because not significant (9): pylint, k_core, sympy_expand, dulwich_log, typing_runtime_protocols, meteor_contest, sympy_str, asyncio_websockets, deepcopy_memo
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown