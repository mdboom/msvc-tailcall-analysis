# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO-Ex3                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 227 ms: 1.05x slower   |
| docutils       | 1.66 sec    | 1.71 sec: 1.03x slower |
| html5lib       | 37.8 ms     | 40.5 ms: 1.07x slower  |
| sphinx         | 641 ms      | 670 ms: 1.04x slower   |
| Geometric mean | (ref)       | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | PGO-Ex3               |
|----------------------------|:-----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 330 ms      | 340 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 344 ms: 1.04x slower  |
| async_tree_memoization_tg  | 208 ms      | 219 ms: 1.05x slower  |
| async_generators           | 201 ms      | 219 ms: 1.09x slower  |
| async_tree_memoization     | 205 ms      | 223 ms: 1.09x slower  |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower  |
| async_tree_io              | 382 ms      | 417 ms: 1.09x slower  |
| async_tree_none            | 170 ms      | 186 ms: 1.09x slower  |
| async_tree_none_tg         | 161 ms      | 176 ms: 1.09x slower  |
| coroutines                 | 12.0 ms     | 13.1 ms: 1.10x slower |
| Geometric mean             | (ref)       | 1.07x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO-Ex3               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 148 ms: 1.02x slower  |
| float          | 42.0 ms     | 44.2 ms: 1.05x slower |
| nbody          | 55.6 ms     | 78.3 ms: 1.41x slower |
| Geometric mean | (ref)       | 1.15x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | PGO-Ex3               |
|----------------|:-----------:|:---------------------:|
| regex_v8       | 14.2 ms     | 13.8 ms: 1.03x faster |
| regex_dna      | 120 ms      | 116 ms: 1.03x faster  |
| regex_effbot   | 1.47 ms     | 1.46 ms: 1.01x faster |
| regex_compile  | 79.4 ms     | 86.1 ms: 1.08x slower |
| Geometric mean | (ref)       | 1.00x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | PGO-Ex3                |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms     | 88.8 ms: 1.01x faster  |
| xml_etree_iterparse  | 61.2 ms     | 62.3 ms: 1.02x slower  |
| json_dumps           | 6.40 ms     | 6.69 ms: 1.04x slower  |
| json_loads           | 14.5 us     | 15.3 us: 1.06x slower  |
| xml_etree_generate   | 53.1 ms     | 56.8 ms: 1.07x slower  |
| xml_etree_process    | 36.8 ms     | 39.7 ms: 1.08x slower  |
| pickle_pure_python   | 199 us      | 217 us: 1.09x slower   |
| unpickle_pure_python | 124 us      | 147 us: 1.18x slower   |
| tomli_loads          | 1.17 sec    | 1.44 sec: 1.22x slower |
| Geometric mean       | (ref)       | 1.08x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TCO-PGO-Ex3 | PGO-Ex3               |
|----------------|:-----------:|:---------------------:|
| python_startup | 24.7 ms     | 24.5 ms: 1.01x faster |
| Geometric mean | (ref)       | 1.00x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | PGO-Ex3               |
|-----------------|:-----------:|:---------------------:|
| mako            | 6.25 ms     | 6.50 ms: 1.04x slower |
| genshi_xml      | 32.3 ms     | 35.0 ms: 1.08x slower |
| django_template | 23.6 ms     | 25.5 ms: 1.08x slower |
| genshi_text     | 14.3 ms     | 15.8 ms: 1.11x slower |
| Geometric mean  | (ref)       | 1.08x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | PGO-Ex3                |
|----------------------------|:-----------:|:----------------------:|
| regex_v8                   | 14.2 ms     | 13.8 ms: 1.03x faster  |
| regex_dna                  | 120 ms      | 116 ms: 1.03x faster   |
| gc_traversal               | 2.12 ms     | 2.07 ms: 1.02x faster  |
| regex_effbot               | 1.47 ms     | 1.46 ms: 1.01x faster  |
| python_startup             | 24.7 ms     | 24.5 ms: 1.01x faster  |
| subparsers                 | 41.4 ms     | 41.0 ms: 1.01x faster  |
| xml_etree_parse            | 89.4 ms     | 88.8 ms: 1.01x faster  |
| shortest_path              | 352 ms      | 354 ms: 1.01x slower   |
| many_optionals             | 685 us      | 695 us: 1.01x slower   |
| k_core                     | 1.70 sec    | 1.73 sec: 1.02x slower |
| xml_etree_iterparse        | 61.2 ms     | 62.3 ms: 1.02x slower  |
| pathlib                    | 24.2 ms     | 24.6 ms: 1.02x slower  |
| sympy_str                  | 173 ms      | 177 ms: 1.02x slower   |
| pidigits                   | 145 ms      | 148 ms: 1.02x slower   |
| docutils                   | 1.66 sec    | 1.71 sec: 1.03x slower |
| async_tree_cpu_io_mixed    | 330 ms      | 340 ms: 1.03x slower   |
| telco                      | 4.59 ms     | 4.75 ms: 1.03x slower  |
| coverage                   | 47.5 ms     | 49.2 ms: 1.04x slower  |
| pylint                     | 201 ms      | 208 ms: 1.04x slower   |
| json                       | 3.04 ms     | 3.16 ms: 1.04x slower  |
| mako                       | 6.25 ms     | 6.50 ms: 1.04x slower  |
| json_dumps                 | 6.40 ms     | 6.69 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 344 ms: 1.04x slower   |
| sphinx                     | 641 ms      | 670 ms: 1.04x slower   |
| meteor_contest             | 70.9 ms     | 74.3 ms: 1.05x slower  |
| dulwich_log                | 40.3 ms     | 42.4 ms: 1.05x slower  |
| 2to3                       | 215 ms      | 227 ms: 1.05x slower   |
| float                      | 42.0 ms     | 44.2 ms: 1.05x slower  |
| async_tree_memoization_tg  | 208 ms      | 219 ms: 1.05x slower   |
| json_loads                 | 14.5 us     | 15.3 us: 1.06x slower  |
| sympy_integrate            | 12.8 ms     | 13.6 ms: 1.06x slower  |
| thrift                     | 491 us      | 522 us: 1.06x slower   |
| sympy_sum                  | 85.2 ms     | 90.8 ms: 1.07x slower  |
| html5lib                   | 37.8 ms     | 40.5 ms: 1.07x slower  |
| xml_etree_generate         | 53.1 ms     | 56.8 ms: 1.07x slower  |
| bpe_tokeniser              | 2.72 sec    | 2.93 sec: 1.08x slower |
| xml_etree_process          | 36.8 ms     | 39.7 ms: 1.08x slower  |
| sympy_expand               | 283 ms      | 305 ms: 1.08x slower   |
| sqlglot_v2_optimize        | 32.9 ms     | 35.6 ms: 1.08x slower  |
| pycparser                  | 689 ms      | 745 ms: 1.08x slower   |
| genshi_xml                 | 32.3 ms     | 35.0 ms: 1.08x slower  |
| django_template            | 23.6 ms     | 25.5 ms: 1.08x slower  |
| typing_runtime_protocols   | 97.8 us     | 106 us: 1.08x slower   |
| regex_compile              | 79.4 ms     | 86.1 ms: 1.08x slower  |
| async_generators           | 201 ms      | 219 ms: 1.09x slower   |
| async_tree_memoization     | 205 ms      | 223 ms: 1.09x slower   |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower   |
| async_tree_io              | 382 ms      | 417 ms: 1.09x slower   |
| pickle_pure_python         | 199 us      | 217 us: 1.09x slower   |
| async_tree_none            | 170 ms      | 186 ms: 1.09x slower   |
| async_tree_none_tg         | 161 ms      | 176 ms: 1.09x slower   |
| coroutines                 | 12.0 ms     | 13.1 ms: 1.10x slower  |
| sqlglot_v2_transpile       | 993 us      | 1.09 ms: 1.10x slower  |
| sqlglot_v2_normalize       | 69.0 ms     | 76.3 ms: 1.11x slower  |
| crypto_pyaes               | 43.9 ms     | 48.6 ms: 1.11x slower  |
| deepcopy                   | 167 us      | 185 us: 1.11x slower   |
| logging_format             | 6.42 us     | 7.11 us: 1.11x slower  |
| genshi_text                | 14.3 ms     | 15.8 ms: 1.11x slower  |
| logging_simple             | 5.87 us     | 6.53 us: 1.11x slower  |
| sqlglot_v2_parse           | 781 us      | 870 us: 1.11x slower   |
| pprint_safe_repr           | 474 ms      | 532 ms: 1.12x slower   |
| deepcopy_reduce            | 1.68 us     | 1.88 us: 1.12x slower  |
| nqueens                    | 55.2 ms     | 62.2 ms: 1.13x slower  |
| pyflate                    | 264 ms      | 300 ms: 1.13x slower   |
| deepcopy_memo              | 16.8 us     | 19.1 us: 1.13x slower  |
| pprint_pformat             | 956 ms      | 1.09 sec: 1.14x slower |
| mdp                        | 1.43 sec    | 1.62 sec: 1.14x slower |
| comprehensions             | 9.76 us     | 11.2 us: 1.15x slower  |
| logging_silent             | 49.7 ns     | 57.0 ns: 1.15x slower  |
| deltablue                  | 1.88 ms     | 2.18 ms: 1.16x slower  |
| fannkuch                   | 225 ms      | 263 ms: 1.17x slower   |
| richards                   | 29.4 ms     | 34.5 ms: 1.18x slower  |
| spectral_norm              | 49.4 ms     | 58.1 ms: 1.18x slower  |
| unpickle_pure_python       | 124 us      | 147 us: 1.18x slower   |
| richards_super             | 33.7 ms     | 39.9 ms: 1.19x slower  |
| chaos                      | 35.4 ms     | 42.2 ms: 1.19x slower  |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.63 ms: 1.19x slower  |
| go                         | 70.5 ms     | 84.1 ms: 1.19x slower  |
| scimark_lu                 | 50.3 ms     | 61.1 ms: 1.21x slower  |
| generators                 | 16.5 ms     | 20.0 ms: 1.22x slower  |
| scimark_fft                | 153 ms      | 187 ms: 1.22x slower   |
| tomli_loads                | 1.17 sec    | 1.44 sec: 1.22x slower |
| hexiom                     | 3.49 ms     | 4.28 ms: 1.22x slower  |
| raytrace                   | 162 ms      | 201 ms: 1.25x slower   |
| scimark_monte_carlo        | 35.6 ms     | 45.3 ms: 1.27x slower  |
| scimark_sor                | 60.5 ms     | 84.2 ms: 1.39x slower  |
| nbody                      | 55.6 ms     | 78.3 ms: 1.41x slower  |
| Geometric mean             | (ref)       | 1.09x slower           |

Benchmark hidden because not significant (5): asyncio_websockets, connected_components, create_gc_cycles, python_startup_no_site, sqlite_synth

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown