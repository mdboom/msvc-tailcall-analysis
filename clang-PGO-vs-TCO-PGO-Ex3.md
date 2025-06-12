# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | clang-PGO              |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 204 ms: 1.06x faster   |
| docutils       | 1.66 sec    | 1.55 sec: 1.07x faster |
| html5lib       | 37.8 ms     | 35.2 ms: 1.07x faster  |
| sphinx         | 641 ms      | 599 ms: 1.07x faster   |
| Geometric mean | (ref)       | 1.07x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | clang-PGO             |
|----------------------------|:-----------:|:---------------------:|
| async_tree_io              | 382 ms      | 349 ms: 1.10x faster  |
| async_tree_none            | 170 ms      | 155 ms: 1.09x faster  |
| async_tree_none_tg         | 161 ms      | 147 ms: 1.09x faster  |
| async_tree_memoization     | 205 ms      | 190 ms: 1.08x faster  |
| coroutines                 | 12.0 ms     | 11.1 ms: 1.08x faster |
| async_tree_io_tg           | 377 ms      | 352 ms: 1.07x faster  |
| async_tree_cpu_io_mixed    | 330 ms      | 309 ms: 1.07x faster  |
| async_generators           | 201 ms      | 188 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 310 ms: 1.06x faster  |
| async_tree_memoization_tg  | 208 ms      | 195 ms: 1.06x faster  |
| asyncio_websockets         | 313 ms      | 400 ms: 1.28x slower  |
| Geometric mean             | (ref)       | 1.05x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | clang-PGO             |
|----------------|:-----------:|:---------------------:|
| float          | 42.0 ms     | 38.5 ms: 1.09x faster |
| nbody          | 55.6 ms     | 52.9 ms: 1.05x faster |
| pidigits       | 145 ms      | 148 ms: 1.02x slower  |
| Geometric mean | (ref)       | 1.04x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | clang-PGO             |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 79.4 ms     | 73.4 ms: 1.08x faster |
| regex_v8       | 14.2 ms     | 13.5 ms: 1.05x faster |
| regex_dna      | 120 ms      | 121 ms: 1.01x slower  |
| regex_effbot   | 1.47 ms     | 1.65 ms: 1.12x slower |
| Geometric mean | (ref)       | 1.00x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | clang-PGO              |
|----------------------|:-----------:|:----------------------:|
| unpickle_pure_python | 124 us      | 109 us: 1.14x faster   |
| pickle_pure_python   | 199 us      | 175 us: 1.14x faster   |
| json_dumps           | 6.40 ms     | 5.76 ms: 1.11x faster  |
| xml_etree_generate   | 53.1 ms     | 48.4 ms: 1.10x faster  |
| xml_etree_process    | 36.8 ms     | 34.0 ms: 1.08x faster  |
| tomli_loads          | 1.17 sec    | 1.13 sec: 1.04x faster |
| json_loads           | 14.5 us     | 14.2 us: 1.02x faster  |
| xml_etree_iterparse  | 61.2 ms     | 60.7 ms: 1.01x faster  |
| xml_etree_parse      | 89.4 ms     | 88.8 ms: 1.01x faster  |
| Geometric mean       | (ref)       | 1.07x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | clang-PGO             |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 20.0 ms: 1.07x slower |
| python_startup         | 24.7 ms     | 26.6 ms: 1.08x slower |
| Geometric mean         | (ref)       | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | clang-PGO             |
|-----------------|:-----------:|:---------------------:|
| django_template | 23.6 ms     | 19.5 ms: 1.21x faster |
| genshi_text     | 14.3 ms     | 12.0 ms: 1.19x faster |
| genshi_xml      | 32.3 ms     | 27.4 ms: 1.18x faster |
| mako            | 6.25 ms     | 5.72 ms: 1.09x faster |
| Geometric mean  | (ref)       | 1.17x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | clang-PGO              |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 41.4 ms     | 14.2 ms: 2.90x faster  |
| many_optionals             | 685 us      | 405 us: 1.69x faster   |
| richards_super             | 33.7 ms     | 24.6 ms: 1.37x faster  |
| richards                   | 29.4 ms     | 21.9 ms: 1.34x faster  |
| django_template            | 23.6 ms     | 19.5 ms: 1.21x faster  |
| genshi_text                | 14.3 ms     | 12.0 ms: 1.19x faster  |
| deltablue                  | 1.88 ms     | 1.59 ms: 1.18x faster  |
| genshi_xml                 | 32.3 ms     | 27.4 ms: 1.18x faster  |
| raytrace                   | 162 ms      | 137 ms: 1.18x faster   |
| coverage                   | 47.5 ms     | 40.9 ms: 1.16x faster  |
| nqueens                    | 55.2 ms     | 47.7 ms: 1.16x faster  |
| deepcopy                   | 167 us      | 145 us: 1.16x faster   |
| sqlglot_v2_normalize       | 69.0 ms     | 59.9 ms: 1.15x faster  |
| sqlglot_v2_transpile       | 993 us      | 868 us: 1.14x faster   |
| chaos                      | 35.4 ms     | 31.1 ms: 1.14x faster  |
| sqlglot_v2_parse           | 781 us      | 686 us: 1.14x faster   |
| unpickle_pure_python       | 124 us      | 109 us: 1.14x faster   |
| pickle_pure_python         | 199 us      | 175 us: 1.14x faster   |
| typing_runtime_protocols   | 97.8 us     | 86.2 us: 1.14x faster  |
| sympy_str                  | 173 ms      | 153 ms: 1.13x faster   |
| thrift                     | 491 us      | 434 us: 1.13x faster   |
| deepcopy_reduce            | 1.68 us     | 1.49 us: 1.13x faster  |
| deepcopy_memo              | 16.8 us     | 15.1 us: 1.12x faster  |
| logging_silent             | 49.7 ns     | 44.5 ns: 1.12x faster  |
| hexiom                     | 3.49 ms     | 3.13 ms: 1.12x faster  |
| crypto_pyaes               | 43.9 ms     | 39.4 ms: 1.12x faster  |
| json_dumps                 | 6.40 ms     | 5.76 ms: 1.11x faster  |
| sqlglot_v2_optimize        | 32.9 ms     | 29.8 ms: 1.11x faster  |
| spectral_norm              | 49.4 ms     | 44.7 ms: 1.11x faster  |
| comprehensions             | 9.76 us     | 8.84 us: 1.10x faster  |
| pylint                     | 201 ms      | 182 ms: 1.10x faster   |
| logging_format             | 6.42 us     | 5.83 us: 1.10x faster  |
| pprint_safe_repr           | 474 ms      | 432 ms: 1.10x faster   |
| mdp                        | 1.43 sec    | 1.30 sec: 1.10x faster |
| xml_etree_generate         | 53.1 ms     | 48.4 ms: 1.10x faster  |
| async_tree_io              | 382 ms      | 349 ms: 1.10x faster   |
| telco                      | 4.59 ms     | 4.20 ms: 1.09x faster  |
| async_tree_none            | 170 ms      | 155 ms: 1.09x faster   |
| mako                       | 6.25 ms     | 5.72 ms: 1.09x faster  |
| pprint_pformat             | 956 ms      | 874 ms: 1.09x faster   |
| sympy_expand               | 283 ms      | 259 ms: 1.09x faster   |
| float                      | 42.0 ms     | 38.5 ms: 1.09x faster  |
| async_tree_none_tg         | 161 ms      | 147 ms: 1.09x faster   |
| logging_simple             | 5.87 us     | 5.39 us: 1.09x faster  |
| bpe_tokeniser              | 2.72 sec    | 2.50 sec: 1.09x faster |
| scimark_monte_carlo        | 35.6 ms     | 32.8 ms: 1.09x faster  |
| sympy_integrate            | 12.8 ms     | 11.8 ms: 1.09x faster  |
| xml_etree_process          | 36.8 ms     | 34.0 ms: 1.08x faster  |
| go                         | 70.5 ms     | 65.1 ms: 1.08x faster  |
| pycparser                  | 689 ms      | 637 ms: 1.08x faster   |
| regex_compile              | 79.4 ms     | 73.4 ms: 1.08x faster  |
| async_tree_memoization     | 205 ms      | 190 ms: 1.08x faster   |
| pyflate                    | 264 ms      | 245 ms: 1.08x faster   |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.05 ms: 1.08x faster  |
| coroutines                 | 12.0 ms     | 11.1 ms: 1.08x faster  |
| scimark_fft                | 153 ms      | 143 ms: 1.07x faster   |
| fannkuch                   | 225 ms      | 209 ms: 1.07x faster   |
| json                       | 3.04 ms     | 2.83 ms: 1.07x faster  |
| html5lib                   | 37.8 ms     | 35.2 ms: 1.07x faster  |
| async_tree_io_tg           | 377 ms      | 352 ms: 1.07x faster   |
| docutils                   | 1.66 sec    | 1.55 sec: 1.07x faster |
| sphinx                     | 641 ms      | 599 ms: 1.07x faster   |
| async_tree_cpu_io_mixed    | 330 ms      | 309 ms: 1.07x faster   |
| async_generators           | 201 ms      | 188 ms: 1.07x faster   |
| async_tree_cpu_io_mixed_tg | 330 ms      | 310 ms: 1.06x faster   |
| async_tree_memoization_tg  | 208 ms      | 195 ms: 1.06x faster   |
| k_core                     | 1.70 sec    | 1.61 sec: 1.06x faster |
| 2to3                       | 215 ms      | 204 ms: 1.06x faster   |
| regex_v8                   | 14.2 ms     | 13.5 ms: 1.05x faster  |
| nbody                      | 55.6 ms     | 52.9 ms: 1.05x faster  |
| sympy_sum                  | 85.2 ms     | 81.4 ms: 1.05x faster  |
| sqlite_synth               | 1.56 us     | 1.49 us: 1.04x faster  |
| generators                 | 16.5 ms     | 15.8 ms: 1.04x faster  |
| tomli_loads                | 1.17 sec    | 1.13 sec: 1.04x faster |
| meteor_contest             | 70.9 ms     | 68.7 ms: 1.03x faster  |
| scimark_sor                | 60.5 ms     | 59.1 ms: 1.02x faster  |
| scimark_lu                 | 50.3 ms     | 49.1 ms: 1.02x faster  |
| dulwich_log                | 40.3 ms     | 39.5 ms: 1.02x faster  |
| shortest_path              | 352 ms      | 345 ms: 1.02x faster   |
| json_loads                 | 14.5 us     | 14.2 us: 1.02x faster  |
| xml_etree_iterparse        | 61.2 ms     | 60.7 ms: 1.01x faster  |
| xml_etree_parse            | 89.4 ms     | 88.8 ms: 1.01x faster  |
| regex_dna                  | 120 ms      | 121 ms: 1.01x slower   |
| pidigits                   | 145 ms      | 148 ms: 1.02x slower   |
| python_startup_no_site     | 18.6 ms     | 20.0 ms: 1.07x slower  |
| python_startup             | 24.7 ms     | 26.6 ms: 1.08x slower  |
| create_gc_cycles           | 1.25 ms     | 1.37 ms: 1.10x slower  |
| regex_effbot               | 1.47 ms     | 1.65 ms: 1.12x slower  |
| pathlib                    | 24.2 ms     | 30.4 ms: 1.26x slower  |
| asyncio_websockets         | 313 ms      | 400 ms: 1.28x slower   |
| gc_traversal               | 2.12 ms     | 2.79 ms: 1.32x slower  |
| Geometric mean             | (ref)       | 1.09x faster           |

Benchmark hidden because not significant (1): connected_components

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown