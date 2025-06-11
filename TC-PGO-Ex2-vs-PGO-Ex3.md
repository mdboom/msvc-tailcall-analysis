# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO-Ex3  | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 216 ms: 1.05x faster   |
| docutils       | 1.71 sec | 1.63 sec: 1.05x faster |
| html5lib       | 40.5 ms  | 36.1 ms: 1.12x faster  |
| sphinx         | 670 ms   | 638 ms: 1.05x faster   |
| Geometric mean | (ref)    | 1.07x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO-Ex3 | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| async_tree_io              | 417 ms  | 375 ms: 1.11x faster  |
| async_tree_io_tg           | 410 ms  | 371 ms: 1.11x faster  |
| async_tree_none_tg         | 176 ms  | 159 ms: 1.10x faster  |
| async_tree_none            | 186 ms  | 170 ms: 1.09x faster  |
| async_tree_memoization     | 223 ms  | 205 ms: 1.09x faster  |
| async_generators           | 219 ms  | 206 ms: 1.06x faster  |
| coroutines                 | 13.1 ms | 12.4 ms: 1.06x faster |
| async_tree_cpu_io_mixed_tg | 344 ms  | 328 ms: 1.05x faster  |
| async_tree_memoization_tg  | 219 ms  | 209 ms: 1.05x faster  |
| async_tree_cpu_io_mixed    | 340 ms  | 329 ms: 1.03x faster  |
| asyncio_websockets         | 311 ms  | 317 ms: 1.02x slower  |
| Geometric mean             | (ref)   | 1.07x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| nbody          | 78.3 ms | 53.3 ms: 1.47x faster |
| float          | 44.2 ms | 40.2 ms: 1.10x faster |
| pidigits       | 148 ms  | 146 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.18x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 86.1 ms | 74.8 ms: 1.15x faster |
| regex_effbot   | 1.46 ms | 1.40 ms: 1.04x faster |
| regex_dna      | 116 ms  | 115 ms: 1.01x faster  |
| regex_v8       | 13.8 ms | 14.1 ms: 1.02x slower |
| Geometric mean | (ref)   | 1.04x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO-Ex3  | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.44 sec | 1.17 sec: 1.22x faster |
| unpickle_pure_python | 147 us   | 123 us: 1.20x faster   |
| xml_etree_generate   | 56.8 ms  | 51.5 ms: 1.10x faster  |
| xml_etree_process    | 39.7 ms  | 36.7 ms: 1.08x faster  |
| pickle_pure_python   | 217 us   | 201 us: 1.08x faster   |
| json_loads           | 15.3 us  | 14.5 us: 1.06x faster  |
| xml_etree_iterparse  | 62.3 ms  | 60.4 ms: 1.03x faster  |
| json_dumps           | 6.69 ms  | 6.48 ms: 1.03x faster  |
| Geometric mean       | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO-Ex3 | TC-PGO-Ex2            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 18.7 ms | 19.6 ms: 1.05x slower |
| python_startup         | 24.5 ms | 26.0 ms: 1.06x slower |
| Geometric mean         | (ref)   | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO-Ex3 | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 35.0 ms | 30.7 ms: 1.14x faster |
| genshi_text     | 15.8 ms | 14.2 ms: 1.12x faster |
| django_template | 25.5 ms | 23.4 ms: 1.09x faster |
| mako            | 6.50 ms | 6.12 ms: 1.06x faster |
| Geometric mean  | (ref)   | 1.10x faster          |

All benchmarks:
===============

| Benchmark                  | PGO-Ex3  | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 78.3 ms  | 53.3 ms: 1.47x faster  |
| generators                 | 20.0 ms  | 14.8 ms: 1.35x faster  |
| scimark_sor                | 84.2 ms  | 67.5 ms: 1.25x faster  |
| richards_super             | 39.9 ms  | 32.2 ms: 1.24x faster  |
| richards                   | 34.5 ms  | 27.8 ms: 1.24x faster  |
| scimark_fft                | 187 ms   | 152 ms: 1.23x faster   |
| hexiom                     | 4.28 ms  | 3.47 ms: 1.23x faster  |
| go                         | 84.1 ms  | 68.4 ms: 1.23x faster  |
| scimark_monte_carlo        | 45.3 ms  | 37.0 ms: 1.22x faster  |
| tomli_loads                | 1.44 sec | 1.17 sec: 1.22x faster |
| raytrace                   | 201 ms   | 166 ms: 1.21x faster   |
| unpickle_pure_python       | 147 us   | 123 us: 1.20x faster   |
| deltablue                  | 2.18 ms  | 1.85 ms: 1.18x faster  |
| sqlglot_v2_parse           | 870 us   | 740 us: 1.18x faster   |
| chaos                      | 42.2 ms  | 35.9 ms: 1.18x faster  |
| sqlglot_v2_transpile       | 1.09 ms  | 933 us: 1.17x faster   |
| crypto_pyaes               | 48.6 ms  | 41.6 ms: 1.17x faster  |
| scimark_sparse_mat_mult    | 2.63 ms  | 2.26 ms: 1.16x faster  |
| mdp                        | 1.62 sec | 1.40 sec: 1.16x faster |
| deepcopy                   | 185 us   | 160 us: 1.16x faster   |
| pyflate                    | 300 ms   | 260 ms: 1.15x faster   |
| nqueens                    | 62.2 ms  | 54.0 ms: 1.15x faster  |
| regex_compile              | 86.1 ms  | 74.8 ms: 1.15x faster  |
| comprehensions             | 11.2 us  | 9.73 us: 1.15x faster  |
| sqlglot_v2_normalize       | 76.3 ms  | 66.9 ms: 1.14x faster  |
| genshi_xml                 | 35.0 ms  | 30.7 ms: 1.14x faster  |
| spectral_norm              | 58.1 ms  | 51.1 ms: 1.14x faster  |
| sympy_expand               | 305 ms   | 269 ms: 1.13x faster   |
| deepcopy_reduce            | 1.88 us  | 1.66 us: 1.13x faster  |
| logging_simple             | 6.53 us  | 5.78 us: 1.13x faster  |
| pprint_pformat             | 1.09 sec | 968 ms: 1.12x faster   |
| scimark_lu                 | 61.1 ms  | 54.4 ms: 1.12x faster  |
| deepcopy_memo              | 19.1 us  | 17.0 us: 1.12x faster  |
| logging_format             | 7.11 us  | 6.34 us: 1.12x faster  |
| html5lib                   | 40.5 ms  | 36.1 ms: 1.12x faster  |
| pycparser                  | 745 ms   | 664 ms: 1.12x faster   |
| sympy_str                  | 177 ms   | 158 ms: 1.12x faster   |
| genshi_text                | 15.8 ms  | 14.2 ms: 1.12x faster  |
| fannkuch                   | 263 ms   | 236 ms: 1.12x faster   |
| sympy_integrate            | 13.6 ms  | 12.2 ms: 1.12x faster  |
| pprint_safe_repr           | 532 ms   | 478 ms: 1.11x faster   |
| async_tree_io              | 417 ms   | 375 ms: 1.11x faster   |
| async_tree_io_tg           | 410 ms   | 371 ms: 1.11x faster   |
| sympy_sum                  | 90.8 ms  | 82.1 ms: 1.11x faster  |
| sqlglot_v2_optimize        | 35.6 ms  | 32.2 ms: 1.11x faster  |
| xml_etree_generate         | 56.8 ms  | 51.5 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms   | 159 ms: 1.10x faster   |
| float                      | 44.2 ms  | 40.2 ms: 1.10x faster  |
| async_tree_none            | 186 ms   | 170 ms: 1.09x faster   |
| django_template            | 25.5 ms  | 23.4 ms: 1.09x faster  |
| async_tree_memoization     | 223 ms   | 205 ms: 1.09x faster   |
| thrift                     | 522 us   | 482 us: 1.08x faster   |
| bpe_tokeniser              | 2.93 sec | 2.71 sec: 1.08x faster |
| xml_etree_process          | 39.7 ms  | 36.7 ms: 1.08x faster  |
| pickle_pure_python         | 217 us   | 201 us: 1.08x faster   |
| dulwich_log                | 42.4 ms  | 39.5 ms: 1.07x faster  |
| typing_runtime_protocols   | 106 us   | 98.9 us: 1.07x faster  |
| logging_silent             | 57.0 ns  | 53.3 ns: 1.07x faster  |
| meteor_contest             | 74.3 ms  | 69.5 ms: 1.07x faster  |
| mako                       | 6.50 ms  | 6.12 ms: 1.06x faster  |
| async_generators           | 219 ms   | 206 ms: 1.06x faster   |
| json                       | 3.16 ms  | 2.98 ms: 1.06x faster  |
| json_loads                 | 15.3 us  | 14.5 us: 1.06x faster  |
| coroutines                 | 13.1 ms  | 12.4 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 344 ms   | 328 ms: 1.05x faster   |
| sphinx                     | 670 ms   | 638 ms: 1.05x faster   |
| docutils                   | 1.71 sec | 1.63 sec: 1.05x faster |
| pylint                     | 208 ms   | 199 ms: 1.05x faster   |
| async_tree_memoization_tg  | 219 ms   | 209 ms: 1.05x faster   |
| 2to3                       | 227 ms   | 216 ms: 1.05x faster   |
| telco                      | 4.75 ms  | 4.54 ms: 1.05x faster  |
| regex_effbot               | 1.46 ms  | 1.40 ms: 1.04x faster  |
| async_tree_cpu_io_mixed    | 340 ms   | 329 ms: 1.03x faster   |
| xml_etree_iterparse        | 62.3 ms  | 60.4 ms: 1.03x faster  |
| json_dumps                 | 6.69 ms  | 6.48 ms: 1.03x faster  |
| shortest_path              | 354 ms   | 348 ms: 1.02x faster   |
| pidigits                   | 148 ms   | 146 ms: 1.02x faster   |
| pathlib                    | 24.6 ms  | 24.3 ms: 1.01x faster  |
| connected_components       | 324 ms   | 321 ms: 1.01x faster   |
| regex_dna                  | 116 ms   | 115 ms: 1.01x faster   |
| create_gc_cycles           | 1.25 ms  | 1.27 ms: 1.01x slower  |
| asyncio_websockets         | 311 ms   | 317 ms: 1.02x slower   |
| regex_v8                   | 13.8 ms  | 14.1 ms: 1.02x slower  |
| python_startup_no_site     | 18.7 ms  | 19.6 ms: 1.05x slower  |
| python_startup             | 24.5 ms  | 26.0 ms: 1.06x slower  |
| subparsers                 | 41.0 ms  | 44.9 ms: 1.09x slower  |
| many_optionals             | 695 us   | 761 us: 1.10x slower   |
| Geometric mean             | (ref)    | 1.10x faster           |

Benchmark hidden because not significant (5): k_core, sqlite_synth, xml_etree_parse, gc_traversal, coverage
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown