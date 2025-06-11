# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | PGO-Ex3                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 227 ms: 1.05x faster   |
| docutils       | 1.81 sec    | 1.71 sec: 1.06x faster |
| html5lib       | 40.8 ms     | 40.5 ms: 1.01x faster  |
| sphinx         | 723 ms      | 670 ms: 1.08x faster   |
| Geometric mean | (ref)       | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | PGO-Ex3               |
|----------------------------|:-----------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 367 ms      | 344 ms: 1.07x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 340 ms: 1.07x faster  |
| async_tree_io              | 429 ms      | 417 ms: 1.03x faster  |
| coroutines                 | 13.5 ms     | 13.1 ms: 1.02x faster |
| async_generators           | 224 ms      | 219 ms: 1.02x faster  |
| async_tree_io_tg           | 419 ms      | 410 ms: 1.02x faster  |
| async_tree_memoization     | 227 ms      | 223 ms: 1.02x faster  |
| async_tree_none            | 188 ms      | 186 ms: 1.01x faster  |
| async_tree_none_tg         | 178 ms      | 176 ms: 1.01x faster  |
| asyncio_websockets         | 304 ms      | 311 ms: 1.02x slower  |
| Geometric mean             | (ref)       | 1.02x faster          |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | PGO-Ex3               |
|----------------|:-----------:|:---------------------:|
| float          | 44.8 ms     | 44.2 ms: 1.01x faster |
| pidigits       | 147 ms      | 148 ms: 1.01x slower  |
| nbody          | 58.8 ms     | 78.3 ms: 1.33x slower |
| Geometric mean | (ref)       | 1.10x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | PGO-Ex3               |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.76 ms     | 1.46 ms: 1.21x faster |
| regex_v8       | 16.7 ms     | 13.8 ms: 1.21x faster |
| regex_compile  | 88.0 ms     | 86.1 ms: 1.02x faster |
| regex_dna      | 117 ms      | 116 ms: 1.01x faster  |
| Geometric mean | (ref)       | 1.11x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | PGO-Ex3                |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 15.3 us: 1.38x faster  |
| json_dumps           | 7.94 ms     | 6.69 ms: 1.19x faster  |
| xml_etree_generate   | 66.8 ms     | 56.8 ms: 1.18x faster  |
| xml_etree_process    | 46.5 ms     | 39.7 ms: 1.17x faster  |
| xml_etree_parse      | 104 ms      | 88.8 ms: 1.17x faster  |
| xml_etree_iterparse  | 71.5 ms     | 62.3 ms: 1.15x faster  |
| pickle_pure_python   | 236 us      | 217 us: 1.08x faster   |
| unpickle_pure_python | 154 us      | 147 us: 1.05x faster   |
| tomli_loads          | 1.38 sec    | 1.44 sec: 1.04x slower |
| Geometric mean       | (ref)       | 1.14x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | PGO-Ex3               |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.9 ms     | 24.5 ms: 1.10x faster |
| python_startup_no_site | 20.1 ms     | 18.7 ms: 1.08x faster |
| Geometric mean         | (ref)       | 1.09x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | PGO-Ex3               |
|-----------------|:-----------:|:---------------------:|
| mako            | 7.44 ms     | 6.50 ms: 1.14x faster |
| django_template | 27.5 ms     | 25.5 ms: 1.08x faster |
| genshi_text     | 16.2 ms     | 15.8 ms: 1.02x faster |
| genshi_xml      | 35.3 ms     | 35.0 ms: 1.01x faster |
| Geometric mean  | (ref)       | 1.06x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | PGO-Ex3                |
|----------------------------|:-----------:|:----------------------:|
| json_loads                 | 21.1 us     | 15.3 us: 1.38x faster  |
| gc_traversal               | 2.77 ms     | 2.07 ms: 1.34x faster  |
| regex_effbot               | 1.76 ms     | 1.46 ms: 1.21x faster  |
| regex_v8                   | 16.7 ms     | 13.8 ms: 1.21x faster  |
| json                       | 3.77 ms     | 3.16 ms: 1.19x faster  |
| json_dumps                 | 7.94 ms     | 6.69 ms: 1.19x faster  |
| xml_etree_generate         | 66.8 ms     | 56.8 ms: 1.18x faster  |
| xml_etree_process          | 46.5 ms     | 39.7 ms: 1.17x faster  |
| many_optionals             | 813 us      | 695 us: 1.17x faster   |
| xml_etree_parse            | 104 ms      | 88.8 ms: 1.17x faster  |
| xml_etree_iterparse        | 71.5 ms     | 62.3 ms: 1.15x faster  |
| subparsers                 | 47.1 ms     | 41.0 ms: 1.15x faster  |
| coverage                   | 56.4 ms     | 49.2 ms: 1.15x faster  |
| mako                       | 7.44 ms     | 6.50 ms: 1.14x faster  |
| deepcopy_reduce            | 2.12 us     | 1.88 us: 1.13x faster  |
| telco                      | 5.33 ms     | 4.75 ms: 1.12x faster  |
| deepcopy_memo              | 21.3 us     | 19.1 us: 1.11x faster  |
| create_gc_cycles           | 1.38 ms     | 1.25 ms: 1.11x faster  |
| logging_silent             | 62.9 ns     | 57.0 ns: 1.10x faster  |
| python_startup             | 26.9 ms     | 24.5 ms: 1.10x faster  |
| comprehensions             | 12.2 us     | 11.2 us: 1.09x faster  |
| pickle_pure_python         | 236 us      | 217 us: 1.08x faster   |
| bpe_tokeniser              | 3.17 sec    | 2.93 sec: 1.08x faster |
| sphinx                     | 723 ms      | 670 ms: 1.08x faster   |
| sqlglot_v2_optimize        | 38.4 ms     | 35.6 ms: 1.08x faster  |
| python_startup_no_site     | 20.1 ms     | 18.7 ms: 1.08x faster  |
| django_template            | 27.5 ms     | 25.5 ms: 1.08x faster  |
| thrift                     | 561 us      | 522 us: 1.07x faster   |
| deepcopy                   | 199 us      | 185 us: 1.07x faster   |
| sqlite_synth               | 1.68 us     | 1.57 us: 1.07x faster  |
| scimark_lu                 | 65.2 ms     | 61.1 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 344 ms: 1.07x faster   |
| async_tree_cpu_io_mixed    | 362 ms      | 340 ms: 1.07x faster   |
| typing_runtime_protocols   | 113 us      | 106 us: 1.06x faster   |
| docutils                   | 1.81 sec    | 1.71 sec: 1.06x faster |
| sympy_sum                  | 96.6 ms     | 90.8 ms: 1.06x faster  |
| sympy_expand               | 324 ms      | 305 ms: 1.06x faster   |
| nqueens                    | 65.7 ms     | 62.2 ms: 1.06x faster  |
| sympy_str                  | 187 ms      | 177 ms: 1.06x faster   |
| meteor_contest             | 78.1 ms     | 74.3 ms: 1.05x faster  |
| pprint_safe_repr           | 558 ms      | 532 ms: 1.05x faster   |
| unpickle_pure_python       | 154 us      | 147 us: 1.05x faster   |
| 2to3                       | 237 ms      | 227 ms: 1.05x faster   |
| pylint                     | 217 ms      | 208 ms: 1.04x faster   |
| pprint_pformat             | 1.13 sec    | 1.09 sec: 1.04x faster |
| pathlib                    | 25.6 ms     | 24.6 ms: 1.04x faster  |
| sqlglot_v2_normalize       | 79.0 ms     | 76.3 ms: 1.03x faster  |
| async_tree_io              | 429 ms      | 417 ms: 1.03x faster   |
| pycparser                  | 765 ms      | 745 ms: 1.03x faster   |
| coroutines                 | 13.5 ms     | 13.1 ms: 1.02x faster  |
| async_generators           | 224 ms      | 219 ms: 1.02x faster   |
| regex_compile              | 88.0 ms     | 86.1 ms: 1.02x faster  |
| async_tree_io_tg           | 419 ms      | 410 ms: 1.02x faster   |
| logging_simple             | 6.67 us     | 6.53 us: 1.02x faster  |
| genshi_text                | 16.2 ms     | 15.8 ms: 1.02x faster  |
| sympy_integrate            | 13.9 ms     | 13.6 ms: 1.02x faster  |
| async_tree_memoization     | 227 ms      | 223 ms: 1.02x faster   |
| dulwich_log                | 43.0 ms     | 42.4 ms: 1.01x faster  |
| crypto_pyaes               | 49.3 ms     | 48.6 ms: 1.01x faster  |
| async_tree_none            | 188 ms      | 186 ms: 1.01x faster   |
| richards                   | 35.0 ms     | 34.5 ms: 1.01x faster  |
| float                      | 44.8 ms     | 44.2 ms: 1.01x faster  |
| regex_dna                  | 117 ms      | 116 ms: 1.01x faster   |
| richards_super             | 40.4 ms     | 39.9 ms: 1.01x faster  |
| logging_format             | 7.18 us     | 7.11 us: 1.01x faster  |
| html5lib                   | 40.8 ms     | 40.5 ms: 1.01x faster  |
| async_tree_none_tg         | 178 ms      | 176 ms: 1.01x faster   |
| genshi_xml                 | 35.3 ms     | 35.0 ms: 1.01x faster  |
| shortest_path              | 357 ms      | 354 ms: 1.01x faster   |
| sqlglot_v2_parse           | 876 us      | 870 us: 1.01x faster   |
| fannkuch                   | 265 ms      | 263 ms: 1.01x faster   |
| pidigits                   | 147 ms      | 148 ms: 1.01x slower   |
| pyflate                    | 295 ms      | 300 ms: 1.02x slower   |
| chaos                      | 41.4 ms     | 42.2 ms: 1.02x slower  |
| asyncio_websockets         | 304 ms      | 311 ms: 1.02x slower   |
| hexiom                     | 4.17 ms     | 4.28 ms: 1.03x slower  |
| mdp                        | 1.57 sec    | 1.62 sec: 1.03x slower |
| tomli_loads                | 1.38 sec    | 1.44 sec: 1.04x slower |
| deltablue                  | 2.09 ms     | 2.18 ms: 1.05x slower  |
| scimark_fft                | 178 ms      | 187 ms: 1.05x slower   |
| scimark_monte_carlo        | 42.9 ms     | 45.3 ms: 1.06x slower  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.63 ms: 1.06x slower  |
| raytrace                   | 187 ms      | 201 ms: 1.08x slower   |
| go                         | 78.0 ms     | 84.1 ms: 1.08x slower  |
| generators                 | 18.1 ms     | 20.0 ms: 1.11x slower  |
| scimark_sor                | 73.9 ms     | 84.2 ms: 1.14x slower  |
| nbody                      | 58.8 ms     | 78.3 ms: 1.33x slower  |
| Geometric mean             | (ref)       | 1.05x faster           |

Benchmark hidden because not significant (5): k_core, connected_components, spectral_norm, sqlglot_v2_transpile, async_tree_memoization_tg
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown