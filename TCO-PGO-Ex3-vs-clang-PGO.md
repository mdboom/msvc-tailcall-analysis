# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TCO-PGO-Ex3            |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 215 ms: 1.06x slower   |
| docutils       | 1.55 sec  | 1.66 sec: 1.07x slower |
| html5lib       | 35.2 ms   | 37.8 ms: 1.07x slower  |
| sphinx         | 599 ms    | 641 ms: 1.07x slower   |
| Geometric mean | (ref)     | 1.07x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TCO-PGO-Ex3           |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 313 ms: 1.28x faster  |
| async_tree_memoization_tg  | 195 ms    | 208 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 330 ms: 1.06x slower  |
| async_generators           | 188 ms    | 201 ms: 1.07x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 330 ms: 1.07x slower  |
| async_tree_io_tg           | 352 ms    | 377 ms: 1.07x slower  |
| coroutines                 | 11.1 ms   | 12.0 ms: 1.08x slower |
| async_tree_memoization     | 190 ms    | 205 ms: 1.08x slower  |
| async_tree_none_tg         | 147 ms    | 161 ms: 1.09x slower  |
| async_tree_none            | 155 ms    | 170 ms: 1.09x slower  |
| async_tree_io              | 349 ms    | 382 ms: 1.10x slower  |
| Geometric mean             | (ref)     | 1.05x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TCO-PGO-Ex3           |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 145 ms: 1.02x faster  |
| nbody          | 52.9 ms   | 55.6 ms: 1.05x slower |
| float          | 38.5 ms   | 42.0 ms: 1.09x slower |
| Geometric mean | (ref)     | 1.04x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TCO-PGO-Ex3           |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.47 ms: 1.12x faster |
| regex_dna      | 121 ms    | 120 ms: 1.01x faster  |
| regex_v8       | 13.5 ms   | 14.2 ms: 1.05x slower |
| regex_compile  | 73.4 ms   | 79.4 ms: 1.08x slower |
| Geometric mean | (ref)     | 1.00x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TCO-PGO-Ex3            |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 89.4 ms: 1.01x slower  |
| xml_etree_iterparse  | 60.7 ms   | 61.2 ms: 1.01x slower  |
| json_loads           | 14.2 us   | 14.5 us: 1.02x slower  |
| tomli_loads          | 1.13 sec  | 1.17 sec: 1.04x slower |
| xml_etree_process    | 34.0 ms   | 36.8 ms: 1.08x slower  |
| xml_etree_generate   | 48.4 ms   | 53.1 ms: 1.10x slower  |
| json_dumps           | 5.76 ms   | 6.40 ms: 1.11x slower  |
| pickle_pure_python   | 175 us    | 199 us: 1.14x slower   |
| unpickle_pure_python | 109 us    | 124 us: 1.14x slower   |
| Geometric mean       | (ref)     | 1.07x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | TCO-PGO-Ex3           |
|------------------------|:---------:|:---------------------:|
| python_startup         | 26.6 ms   | 24.7 ms: 1.08x faster |
| python_startup_no_site | 20.0 ms   | 18.6 ms: 1.07x faster |
| Geometric mean         | (ref)     | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TCO-PGO-Ex3           |
|-----------------|:---------:|:---------------------:|
| mako            | 5.72 ms   | 6.25 ms: 1.09x slower |
| genshi_xml      | 27.4 ms   | 32.3 ms: 1.18x slower |
| genshi_text     | 12.0 ms   | 14.3 ms: 1.19x slower |
| django_template | 19.5 ms   | 23.6 ms: 1.21x slower |
| Geometric mean  | (ref)     | 1.17x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TCO-PGO-Ex3            |
|----------------------------|:---------:|:----------------------:|
| gc_traversal               | 2.79 ms   | 2.12 ms: 1.32x faster  |
| asyncio_websockets         | 400 ms    | 313 ms: 1.28x faster   |
| pathlib                    | 30.4 ms   | 24.2 ms: 1.26x faster  |
| regex_effbot               | 1.65 ms   | 1.47 ms: 1.12x faster  |
| create_gc_cycles           | 1.37 ms   | 1.25 ms: 1.10x faster  |
| python_startup             | 26.6 ms   | 24.7 ms: 1.08x faster  |
| python_startup_no_site     | 20.0 ms   | 18.6 ms: 1.07x faster  |
| pidigits                   | 148 ms    | 145 ms: 1.02x faster   |
| regex_dna                  | 121 ms    | 120 ms: 1.01x faster   |
| xml_etree_parse            | 88.8 ms   | 89.4 ms: 1.01x slower  |
| xml_etree_iterparse        | 60.7 ms   | 61.2 ms: 1.01x slower  |
| json_loads                 | 14.2 us   | 14.5 us: 1.02x slower  |
| shortest_path              | 345 ms    | 352 ms: 1.02x slower   |
| dulwich_log                | 39.5 ms   | 40.3 ms: 1.02x slower  |
| scimark_lu                 | 49.1 ms   | 50.3 ms: 1.02x slower  |
| scimark_sor                | 59.1 ms   | 60.5 ms: 1.02x slower  |
| meteor_contest             | 68.7 ms   | 70.9 ms: 1.03x slower  |
| tomli_loads                | 1.13 sec  | 1.17 sec: 1.04x slower |
| generators                 | 15.8 ms   | 16.5 ms: 1.04x slower  |
| sqlite_synth               | 1.49 us   | 1.56 us: 1.04x slower  |
| sympy_sum                  | 81.4 ms   | 85.2 ms: 1.05x slower  |
| nbody                      | 52.9 ms   | 55.6 ms: 1.05x slower  |
| regex_v8                   | 13.5 ms   | 14.2 ms: 1.05x slower  |
| 2to3                       | 204 ms    | 215 ms: 1.06x slower   |
| k_core                     | 1.61 sec  | 1.70 sec: 1.06x slower |
| async_tree_memoization_tg  | 195 ms    | 208 ms: 1.06x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 330 ms: 1.06x slower   |
| async_generators           | 188 ms    | 201 ms: 1.07x slower   |
| async_tree_cpu_io_mixed    | 309 ms    | 330 ms: 1.07x slower   |
| sphinx                     | 599 ms    | 641 ms: 1.07x slower   |
| docutils                   | 1.55 sec  | 1.66 sec: 1.07x slower |
| async_tree_io_tg           | 352 ms    | 377 ms: 1.07x slower   |
| html5lib                   | 35.2 ms   | 37.8 ms: 1.07x slower  |
| json                       | 2.83 ms   | 3.04 ms: 1.07x slower  |
| fannkuch                   | 209 ms    | 225 ms: 1.07x slower   |
| scimark_fft                | 143 ms    | 153 ms: 1.07x slower   |
| coroutines                 | 11.1 ms   | 12.0 ms: 1.08x slower  |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.21 ms: 1.08x slower  |
| pyflate                    | 245 ms    | 264 ms: 1.08x slower   |
| async_tree_memoization     | 190 ms    | 205 ms: 1.08x slower   |
| regex_compile              | 73.4 ms   | 79.4 ms: 1.08x slower  |
| pycparser                  | 637 ms    | 689 ms: 1.08x slower   |
| go                         | 65.1 ms   | 70.5 ms: 1.08x slower  |
| xml_etree_process          | 34.0 ms   | 36.8 ms: 1.08x slower  |
| sympy_integrate            | 11.8 ms   | 12.8 ms: 1.09x slower  |
| scimark_monte_carlo        | 32.8 ms   | 35.6 ms: 1.09x slower  |
| bpe_tokeniser              | 2.50 sec  | 2.72 sec: 1.09x slower |
| logging_simple             | 5.39 us   | 5.87 us: 1.09x slower  |
| async_tree_none_tg         | 147 ms    | 161 ms: 1.09x slower   |
| float                      | 38.5 ms   | 42.0 ms: 1.09x slower  |
| sympy_expand               | 259 ms    | 283 ms: 1.09x slower   |
| pprint_pformat             | 874 ms    | 956 ms: 1.09x slower   |
| mako                       | 5.72 ms   | 6.25 ms: 1.09x slower  |
| async_tree_none            | 155 ms    | 170 ms: 1.09x slower   |
| telco                      | 4.20 ms   | 4.59 ms: 1.09x slower  |
| async_tree_io              | 349 ms    | 382 ms: 1.10x slower   |
| xml_etree_generate         | 48.4 ms   | 53.1 ms: 1.10x slower  |
| mdp                        | 1.30 sec  | 1.43 sec: 1.10x slower |
| pprint_safe_repr           | 432 ms    | 474 ms: 1.10x slower   |
| logging_format             | 5.83 us   | 6.42 us: 1.10x slower  |
| pylint                     | 182 ms    | 201 ms: 1.10x slower   |
| comprehensions             | 8.84 us   | 9.76 us: 1.10x slower  |
| spectral_norm              | 44.7 ms   | 49.4 ms: 1.11x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 32.9 ms: 1.11x slower  |
| json_dumps                 | 5.76 ms   | 6.40 ms: 1.11x slower  |
| crypto_pyaes               | 39.4 ms   | 43.9 ms: 1.12x slower  |
| hexiom                     | 3.13 ms   | 3.49 ms: 1.12x slower  |
| logging_silent             | 44.5 ns   | 49.7 ns: 1.12x slower  |
| deepcopy_memo              | 15.1 us   | 16.8 us: 1.12x slower  |
| deepcopy_reduce            | 1.49 us   | 1.68 us: 1.13x slower  |
| thrift                     | 434 us    | 491 us: 1.13x slower   |
| sympy_str                  | 153 ms    | 173 ms: 1.13x slower   |
| typing_runtime_protocols   | 86.2 us   | 97.8 us: 1.14x slower  |
| pickle_pure_python         | 175 us    | 199 us: 1.14x slower   |
| unpickle_pure_python       | 109 us    | 124 us: 1.14x slower   |
| sqlglot_v2_parse           | 686 us    | 781 us: 1.14x slower   |
| chaos                      | 31.1 ms   | 35.4 ms: 1.14x slower  |
| sqlglot_v2_transpile       | 868 us    | 993 us: 1.14x slower   |
| sqlglot_v2_normalize       | 59.9 ms   | 69.0 ms: 1.15x slower  |
| deepcopy                   | 145 us    | 167 us: 1.16x slower   |
| nqueens                    | 47.7 ms   | 55.2 ms: 1.16x slower  |
| coverage                   | 40.9 ms   | 47.5 ms: 1.16x slower  |
| raytrace                   | 137 ms    | 162 ms: 1.18x slower   |
| genshi_xml                 | 27.4 ms   | 32.3 ms: 1.18x slower  |
| deltablue                  | 1.59 ms   | 1.88 ms: 1.18x slower  |
| genshi_text                | 12.0 ms   | 14.3 ms: 1.19x slower  |
| django_template            | 19.5 ms   | 23.6 ms: 1.21x slower  |
| richards                   | 21.9 ms   | 29.4 ms: 1.34x slower  |
| richards_super             | 24.6 ms   | 33.7 ms: 1.37x slower  |
| many_optionals             | 405 us    | 685 us: 1.69x slower   |
| subparsers                 | 14.2 ms   | 41.4 ms: 2.90x slower  |
| Geometric mean             | (ref)     | 1.09x slower           |

Benchmark hidden because not significant (1): connected_components

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown