# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.011x slower
- HPT reliability: 93.61%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TC-PGO-Ex3             |
|----------------|:---------:|:----------------------:|
| docutils       | 1.55 sec  | 1.58 sec: 1.02x slower |
| sphinx         | 599 ms    | 615 ms: 1.03x slower   |
| Geometric mean | (ref)     | 1.01x slower           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TC-PGO-Ex3            |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 304 ms: 1.32x faster  |
| coroutines                 | 11.1 ms   | 10.8 ms: 1.03x faster |
| async_tree_io_tg           | 352 ms    | 356 ms: 1.01x slower  |
| async_tree_none_tg         | 147 ms    | 150 ms: 1.02x slower  |
| async_tree_memoization_tg  | 195 ms    | 201 ms: 1.03x slower  |
| async_tree_memoization     | 190 ms    | 196 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 325 ms: 1.05x slower  |
| async_generators           | 188 ms    | 199 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 327 ms: 1.06x slower  |
| Geometric mean             | (ref)     | 1.00x faster          |

Benchmark hidden because not significant (2): async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TC-PGO-Ex3            |
|----------------|:---------:|:---------------------:|
| nbody          | 52.9 ms   | 45.7 ms: 1.16x faster |
| float          | 38.5 ms   | 37.1 ms: 1.04x faster |
| pidigits       | 148 ms    | 145 ms: 1.02x faster  |
| Geometric mean | (ref)     | 1.07x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TC-PGO-Ex3            |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.45 ms: 1.13x faster |
| regex_compile  | 73.4 ms   | 70.7 ms: 1.04x faster |
| regex_v8       | 13.5 ms   | 13.9 ms: 1.03x slower |
| Geometric mean | (ref)     | 1.03x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TC-PGO-Ex3             |
|----------------------|:---------:|:----------------------:|
| tomli_loads          | 1.13 sec  | 1.03 sec: 1.10x faster |
| xml_etree_iterparse  | 60.7 ms   | 59.5 ms: 1.02x faster  |
| xml_etree_process    | 34.0 ms   | 33.8 ms: 1.01x faster  |
| xml_etree_parse      | 88.8 ms   | 89.4 ms: 1.01x slower  |
| unpickle_pure_python | 109 us    | 110 us: 1.01x slower   |
| xml_etree_generate   | 48.4 ms   | 49.4 ms: 1.02x slower  |
| json_loads           | 14.2 us   | 14.8 us: 1.04x slower  |
| pickle_pure_python   | 175 us    | 184 us: 1.05x slower   |
| json_dumps           | 5.76 ms   | 6.19 ms: 1.07x slower  |
| Geometric mean       | (ref)     | 1.01x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | TC-PGO-Ex3            |
|------------------------|:---------:|:---------------------:|
| python_startup         | 26.6 ms   | 24.7 ms: 1.08x faster |
| python_startup_no_site | 20.0 ms   | 18.7 ms: 1.07x faster |
| Geometric mean         | (ref)     | 1.07x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TC-PGO-Ex3            |
|-----------------|:---------:|:---------------------:|
| mako            | 5.72 ms   | 5.80 ms: 1.01x slower |
| genshi_text     | 12.0 ms   | 12.3 ms: 1.03x slower |
| django_template | 19.5 ms   | 20.9 ms: 1.07x slower |
| genshi_xml      | 27.4 ms   | 29.5 ms: 1.08x slower |
| Geometric mean  | (ref)     | 1.05x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TC-PGO-Ex3             |
|----------------------------|:---------:|:----------------------:|
| gc_traversal               | 2.79 ms   | 2.09 ms: 1.33x faster  |
| asyncio_websockets         | 400 ms    | 304 ms: 1.32x faster   |
| pathlib                    | 30.4 ms   | 23.6 ms: 1.29x faster  |
| nbody                      | 52.9 ms   | 45.7 ms: 1.16x faster  |
| scimark_sor                | 59.1 ms   | 51.1 ms: 1.16x faster  |
| regex_effbot               | 1.65 ms   | 1.45 ms: 1.13x faster  |
| scimark_lu                 | 49.1 ms   | 44.3 ms: 1.11x faster  |
| generators                 | 15.8 ms   | 14.2 ms: 1.11x faster  |
| tomli_loads                | 1.13 sec  | 1.03 sec: 1.10x faster |
| spectral_norm              | 44.7 ms   | 40.9 ms: 1.09x faster  |
| create_gc_cycles           | 1.37 ms   | 1.26 ms: 1.09x faster  |
| python_startup             | 26.6 ms   | 24.7 ms: 1.08x faster  |
| python_startup_no_site     | 20.0 ms   | 18.7 ms: 1.07x faster  |
| go                         | 65.1 ms   | 61.0 ms: 1.07x faster  |
| hexiom                     | 3.13 ms   | 3.00 ms: 1.04x faster  |
| scimark_monte_carlo        | 32.8 ms   | 31.5 ms: 1.04x faster  |
| regex_compile              | 73.4 ms   | 70.7 ms: 1.04x faster  |
| float                      | 38.5 ms   | 37.1 ms: 1.04x faster  |
| pyflate                    | 245 ms    | 236 ms: 1.04x faster   |
| meteor_contest             | 68.7 ms   | 66.6 ms: 1.03x faster  |
| coroutines                 | 11.1 ms   | 10.8 ms: 1.03x faster  |
| fannkuch                   | 209 ms    | 203 ms: 1.03x faster   |
| pprint_pformat             | 874 ms    | 853 ms: 1.03x faster   |
| deepcopy_memo              | 15.1 us   | 14.7 us: 1.03x faster  |
| comprehensions             | 8.84 us   | 8.65 us: 1.02x faster  |
| pidigits                   | 148 ms    | 145 ms: 1.02x faster   |
| xml_etree_iterparse        | 60.7 ms   | 59.5 ms: 1.02x faster  |
| scimark_fft                | 143 ms    | 140 ms: 1.02x faster   |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.02 ms: 1.02x faster  |
| connected_components       | 325 ms    | 320 ms: 1.01x faster   |
| dulwich_log                | 39.5 ms   | 39.1 ms: 1.01x faster  |
| logging_silent             | 44.5 ns   | 44.1 ns: 1.01x faster  |
| sympy_sum                  | 81.4 ms   | 80.7 ms: 1.01x faster  |
| xml_etree_process          | 34.0 ms   | 33.8 ms: 1.01x faster  |
| pprint_safe_repr           | 432 ms    | 429 ms: 1.01x faster   |
| shortest_path              | 345 ms    | 347 ms: 1.01x slower   |
| xml_etree_parse            | 88.8 ms   | 89.4 ms: 1.01x slower  |
| unpickle_pure_python       | 109 us    | 110 us: 1.01x slower   |
| bpe_tokeniser              | 2.50 sec  | 2.52 sec: 1.01x slower |
| async_tree_io_tg           | 352 ms    | 356 ms: 1.01x slower   |
| logging_format             | 5.83 us   | 5.90 us: 1.01x slower  |
| sqlglot_v2_parse           | 686 us    | 695 us: 1.01x slower   |
| deepcopy                   | 145 us    | 147 us: 1.01x slower   |
| sympy_expand               | 259 ms    | 263 ms: 1.01x slower   |
| mako                       | 5.72 ms   | 5.80 ms: 1.01x slower  |
| deepcopy_reduce            | 1.49 us   | 1.51 us: 1.02x slower  |
| sympy_integrate            | 11.8 ms   | 12.0 ms: 1.02x slower  |
| async_tree_none_tg         | 147 ms    | 150 ms: 1.02x slower   |
| docutils                   | 1.55 sec  | 1.58 sec: 1.02x slower |
| xml_etree_generate         | 48.4 ms   | 49.4 ms: 1.02x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 30.5 ms: 1.02x slower  |
| crypto_pyaes               | 39.4 ms   | 40.4 ms: 1.03x slower  |
| sphinx                     | 599 ms    | 615 ms: 1.03x slower   |
| async_tree_memoization_tg  | 195 ms    | 201 ms: 1.03x slower   |
| sqlglot_v2_transpile       | 868 us    | 894 us: 1.03x slower   |
| regex_v8                   | 13.5 ms   | 13.9 ms: 1.03x slower  |
| deltablue                  | 1.59 ms   | 1.64 ms: 1.03x slower  |
| genshi_text                | 12.0 ms   | 12.3 ms: 1.03x slower  |
| async_tree_memoization     | 190 ms    | 196 ms: 1.04x slower   |
| json_loads                 | 14.2 us   | 14.8 us: 1.04x slower  |
| k_core                     | 1.61 sec  | 1.67 sec: 1.04x slower |
| typing_runtime_protocols   | 86.2 us   | 89.7 us: 1.04x slower  |
| sqlite_synth               | 1.49 us   | 1.56 us: 1.04x slower  |
| nqueens                    | 47.7 ms   | 49.7 ms: 1.04x slower  |
| json                       | 2.83 ms   | 2.95 ms: 1.04x slower  |
| sqlglot_v2_normalize       | 59.9 ms   | 62.6 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 325 ms: 1.05x slower   |
| pickle_pure_python         | 175 us    | 184 us: 1.05x slower   |
| async_generators           | 188 ms    | 199 ms: 1.05x slower   |
| raytrace                   | 137 ms    | 145 ms: 1.06x slower   |
| pylint                     | 182 ms    | 193 ms: 1.06x slower   |
| async_tree_cpu_io_mixed    | 309 ms    | 327 ms: 1.06x slower   |
| telco                      | 4.20 ms   | 4.45 ms: 1.06x slower  |
| thrift                     | 434 us    | 461 us: 1.06x slower   |
| django_template            | 19.5 ms   | 20.9 ms: 1.07x slower  |
| json_dumps                 | 5.76 ms   | 6.19 ms: 1.07x slower  |
| genshi_xml                 | 27.4 ms   | 29.5 ms: 1.08x slower  |
| mdp                        | 1.30 sec  | 1.41 sec: 1.08x slower |
| coverage                   | 40.9 ms   | 46.2 ms: 1.13x slower  |
| richards                   | 21.9 ms   | 25.5 ms: 1.16x slower  |
| richards_super             | 24.6 ms   | 29.4 ms: 1.20x slower  |
| many_optionals             | 405 us    | 659 us: 1.63x slower   |
| subparsers                 | 14.2 ms   | 40.6 ms: 2.85x slower  |
| Geometric mean             | (ref)     | 1.01x slower           |

Benchmark hidden because not significant (9): regex_dna, 2to3, logging_simple, sympy_str, chaos, html5lib, pycparser, async_tree_io, async_tree_none

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 93.61% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown