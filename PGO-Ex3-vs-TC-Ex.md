# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.007x slower
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | PGO-Ex3                |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 227 ms: 1.02x faster   |
| docutils       | 1.77 sec | 1.71 sec: 1.04x faster |
| html5lib       | 38.8 ms  | 40.5 ms: 1.04x slower  |
| sphinx         | 702 ms   | 670 ms: 1.05x faster   |
| Geometric mean | (ref)    | 1.01x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | PGO-Ex3               |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed    | 359 ms  | 340 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms  | 344 ms: 1.05x faster  |
| async_generators           | 213 ms  | 219 ms: 1.02x slower  |
| async_tree_memoization_tg  | 210 ms  | 219 ms: 1.04x slower  |
| async_tree_none_tg         | 167 ms  | 176 ms: 1.05x slower  |
| async_tree_memoization     | 210 ms  | 223 ms: 1.06x slower  |
| async_tree_io_tg           | 385 ms  | 410 ms: 1.07x slower  |
| async_tree_none            | 174 ms  | 186 ms: 1.07x slower  |
| coroutines                 | 12.3 ms | 13.1 ms: 1.07x slower |
| async_tree_io              | 384 ms  | 417 ms: 1.09x slower  |
| Geometric mean             | (ref)   | 1.03x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 148 ms: 1.02x slower  |
| float          | 41.4 ms | 44.2 ms: 1.07x slower |
| nbody          | 53.1 ms | 78.3 ms: 1.48x slower |
| Geometric mean | (ref)   | 1.17x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | PGO-Ex3               |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.46 ms: 1.27x faster |
| regex_v8       | 16.3 ms | 13.8 ms: 1.18x faster |
| regex_dna      | 121 ms  | 116 ms: 1.04x faster  |
| regex_compile  | 81.9 ms | 86.1 ms: 1.05x slower |
| Geometric mean | (ref)   | 1.10x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | PGO-Ex3                |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 15.3 us: 1.43x faster  |
| xml_etree_parse      | 105 ms   | 88.8 ms: 1.18x faster  |
| json_dumps           | 7.79 ms  | 6.69 ms: 1.16x faster  |
| xml_etree_generate   | 64.7 ms  | 56.8 ms: 1.14x faster  |
| xml_etree_iterparse  | 70.4 ms  | 62.3 ms: 1.13x faster  |
| xml_etree_process    | 44.7 ms  | 39.7 ms: 1.13x faster  |
| pickle_pure_python   | 223 us   | 217 us: 1.02x faster   |
| unpickle_pure_python | 148 us   | 147 us: 1.01x faster   |
| tomli_loads          | 1.26 sec | 1.44 sec: 1.14x slower |
| Geometric mean       | (ref)    | 1.11x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | PGO-Ex3               |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 24.5 ms: 1.08x faster |
| python_startup_no_site | 19.4 ms | 18.7 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.06x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | PGO-Ex3               |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.50 ms: 1.21x faster |
| django_template | 25.2 ms | 25.5 ms: 1.01x slower |
| genshi_text     | 14.5 ms | 15.8 ms: 1.10x slower |
| genshi_xml      | 31.3 ms | 35.0 ms: 1.12x slower |
| Geometric mean  | (ref)   | 1.01x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | PGO-Ex3                |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 15.3 us: 1.43x faster  |
| gc_traversal               | 2.83 ms  | 2.07 ms: 1.37x faster  |
| regex_effbot               | 1.85 ms  | 1.46 ms: 1.27x faster  |
| mako                       | 7.84 ms  | 6.50 ms: 1.21x faster  |
| json                       | 3.78 ms  | 3.16 ms: 1.20x faster  |
| regex_v8                   | 16.3 ms  | 13.8 ms: 1.18x faster  |
| xml_etree_parse            | 105 ms   | 88.8 ms: 1.18x faster  |
| json_dumps                 | 7.79 ms  | 6.69 ms: 1.16x faster  |
| xml_etree_generate         | 64.7 ms  | 56.8 ms: 1.14x faster  |
| xml_etree_iterparse        | 70.4 ms  | 62.3 ms: 1.13x faster  |
| xml_etree_process          | 44.7 ms  | 39.7 ms: 1.13x faster  |
| coverage                   | 55.4 ms  | 49.2 ms: 1.12x faster  |
| telco                      | 5.26 ms  | 4.75 ms: 1.11x faster  |
| many_optionals             | 762 us   | 695 us: 1.10x faster   |
| subparsers                 | 44.5 ms  | 41.0 ms: 1.08x faster  |
| python_startup             | 26.4 ms  | 24.5 ms: 1.08x faster  |
| logging_silent             | 61.1 ns  | 57.0 ns: 1.07x faster  |
| create_gc_cycles           | 1.34 ms  | 1.25 ms: 1.07x faster  |
| sqlite_synth               | 1.68 us  | 1.57 us: 1.07x faster  |
| async_tree_cpu_io_mixed    | 359 ms   | 340 ms: 1.06x faster   |
| thrift                     | 551 us   | 522 us: 1.05x faster   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 344 ms: 1.05x faster   |
| scimark_lu                 | 64.2 ms  | 61.1 ms: 1.05x faster  |
| sphinx                     | 702 ms   | 670 ms: 1.05x faster   |
| python_startup_no_site     | 19.4 ms  | 18.7 ms: 1.04x faster  |
| regex_dna                  | 121 ms   | 116 ms: 1.04x faster   |
| docutils                   | 1.77 sec | 1.71 sec: 1.04x faster |
| bpe_tokeniser              | 3.01 sec | 2.93 sec: 1.03x faster |
| pickle_pure_python         | 223 us   | 217 us: 1.02x faster   |
| pathlib                    | 25.1 ms  | 24.6 ms: 1.02x faster  |
| 2to3                       | 231 ms   | 227 ms: 1.02x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 35.6 ms: 1.01x faster  |
| comprehensions             | 11.3 us  | 11.2 us: 1.01x faster  |
| deepcopy_reduce            | 1.90 us  | 1.88 us: 1.01x faster  |
| unpickle_pure_python       | 148 us   | 147 us: 1.01x faster   |
| sympy_sum                  | 91.4 ms  | 90.8 ms: 1.01x faster  |
| django_template            | 25.2 ms  | 25.5 ms: 1.01x slower  |
| crypto_pyaes               | 48.0 ms  | 48.6 ms: 1.01x slower  |
| sympy_integrate            | 13.4 ms  | 13.6 ms: 1.02x slower  |
| pidigits                   | 146 ms   | 148 ms: 1.02x slower   |
| shortest_path              | 347 ms   | 354 ms: 1.02x slower   |
| async_generators           | 213 ms   | 219 ms: 1.02x slower   |
| deepcopy                   | 180 us   | 185 us: 1.03x slower   |
| async_tree_memoization_tg  | 210 ms   | 219 ms: 1.04x slower   |
| sqlglot_v2_normalize       | 73.3 ms  | 76.3 ms: 1.04x slower  |
| connected_components       | 311 ms   | 324 ms: 1.04x slower   |
| pprint_safe_repr           | 510 ms   | 532 ms: 1.04x slower   |
| nqueens                    | 59.6 ms  | 62.2 ms: 1.04x slower  |
| html5lib                   | 38.8 ms  | 40.5 ms: 1.04x slower  |
| logging_simple             | 6.25 us  | 6.53 us: 1.04x slower  |
| pycparser                  | 713 ms   | 745 ms: 1.05x slower   |
| pprint_pformat             | 1.04 sec | 1.09 sec: 1.05x slower |
| fannkuch                   | 250 ms   | 263 ms: 1.05x slower   |
| regex_compile              | 81.9 ms  | 86.1 ms: 1.05x slower  |
| async_tree_none_tg         | 167 ms   | 176 ms: 1.05x slower   |
| logging_format             | 6.70 us  | 7.11 us: 1.06x slower  |
| async_tree_memoization     | 210 ms   | 223 ms: 1.06x slower   |
| async_tree_io_tg           | 385 ms   | 410 ms: 1.07x slower   |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.63 ms: 1.07x slower  |
| float                      | 41.4 ms  | 44.2 ms: 1.07x slower  |
| async_tree_none            | 174 ms   | 186 ms: 1.07x slower   |
| coroutines                 | 12.3 ms  | 13.1 ms: 1.07x slower  |
| sqlglot_v2_transpile       | 1.01 ms  | 1.09 ms: 1.08x slower  |
| async_tree_io              | 384 ms   | 417 ms: 1.09x slower   |
| sqlglot_v2_parse           | 798 us   | 870 us: 1.09x slower   |
| hexiom                     | 3.92 ms  | 4.28 ms: 1.09x slower  |
| pyflate                    | 274 ms   | 300 ms: 1.10x slower   |
| genshi_text                | 14.5 ms  | 15.8 ms: 1.10x slower  |
| scimark_fft                | 169 ms   | 187 ms: 1.11x slower   |
| richards_super             | 35.8 ms  | 39.9 ms: 1.12x slower  |
| genshi_xml                 | 31.3 ms  | 35.0 ms: 1.12x slower  |
| chaos                      | 37.7 ms  | 42.2 ms: 1.12x slower  |
| richards                   | 30.9 ms  | 34.5 ms: 1.12x slower  |
| mdp                        | 1.44 sec | 1.62 sec: 1.12x slower |
| spectral_norm              | 51.1 ms  | 58.1 ms: 1.14x slower  |
| tomli_loads                | 1.26 sec | 1.44 sec: 1.14x slower |
| deltablue                  | 1.91 ms  | 2.18 ms: 1.14x slower  |
| scimark_monte_carlo        | 38.9 ms  | 45.3 ms: 1.16x slower  |
| raytrace                   | 169 ms   | 201 ms: 1.19x slower   |
| go                         | 70.4 ms  | 84.1 ms: 1.19x slower  |
| scimark_sor                | 68.6 ms  | 84.2 ms: 1.23x slower  |
| generators                 | 16.3 ms  | 20.0 ms: 1.23x slower  |
| nbody                      | 53.1 ms  | 78.3 ms: 1.48x slower  |
| Geometric mean             | (ref)    | 1.01x slower           |

Benchmark hidden because not significant (9): deepcopy_memo, asyncio_websockets, sympy_str, meteor_contest, typing_runtime_protocols, dulwich_log, sympy_expand, k_core, pylint
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 98.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown