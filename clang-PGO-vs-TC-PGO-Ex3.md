# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.012x faster
- HPT reliability: 93.61%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | clang-PGO              |
|----------------|:----------:|:----------------------:|
| docutils       | 1.58 sec   | 1.55 sec: 1.02x faster |
| sphinx         | 615 ms     | 599 ms: 1.03x faster   |
| Geometric mean | (ref)      | 1.01x faster           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | clang-PGO             |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 327 ms     | 309 ms: 1.06x faster  |
| async_generators           | 199 ms     | 188 ms: 1.05x faster  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 310 ms: 1.05x faster  |
| async_tree_memoization     | 196 ms     | 190 ms: 1.04x faster  |
| async_tree_memoization_tg  | 201 ms     | 195 ms: 1.03x faster  |
| async_tree_none_tg         | 150 ms     | 147 ms: 1.02x faster  |
| async_tree_io_tg           | 356 ms     | 352 ms: 1.01x faster  |
| coroutines                 | 10.8 ms    | 11.1 ms: 1.03x slower |
| asyncio_websockets         | 304 ms     | 400 ms: 1.32x slower  |
| Geometric mean             | (ref)      | 1.00x slower          |

Benchmark hidden because not significant (2): async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | clang-PGO             |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 148 ms: 1.02x slower  |
| float          | 37.1 ms    | 38.5 ms: 1.04x slower |
| nbody          | 45.7 ms    | 52.9 ms: 1.16x slower |
| Geometric mean | (ref)      | 1.07x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | clang-PGO             |
|----------------|:----------:|:---------------------:|
| regex_v8       | 13.9 ms    | 13.5 ms: 1.03x faster |
| regex_compile  | 70.7 ms    | 73.4 ms: 1.04x slower |
| regex_effbot   | 1.45 ms    | 1.65 ms: 1.13x slower |
| Geometric mean | (ref)      | 1.03x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | clang-PGO              |
|----------------------|:----------:|:----------------------:|
| json_dumps           | 6.19 ms    | 5.76 ms: 1.07x faster  |
| pickle_pure_python   | 184 us     | 175 us: 1.05x faster   |
| json_loads           | 14.8 us    | 14.2 us: 1.04x faster  |
| xml_etree_generate   | 49.4 ms    | 48.4 ms: 1.02x faster  |
| unpickle_pure_python | 110 us     | 109 us: 1.01x faster   |
| xml_etree_parse      | 89.4 ms    | 88.8 ms: 1.01x faster  |
| xml_etree_process    | 33.8 ms    | 34.0 ms: 1.01x slower  |
| xml_etree_iterparse  | 59.5 ms    | 60.7 ms: 1.02x slower  |
| tomli_loads          | 1.03 sec   | 1.13 sec: 1.10x slower |
| Geometric mean       | (ref)      | 1.01x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | clang-PGO             |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 20.0 ms: 1.07x slower |
| python_startup         | 24.7 ms    | 26.6 ms: 1.08x slower |
| Geometric mean         | (ref)      | 1.07x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | clang-PGO             |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 27.4 ms: 1.08x faster |
| django_template | 20.9 ms    | 19.5 ms: 1.07x faster |
| genshi_text     | 12.3 ms    | 12.0 ms: 1.03x faster |
| mako            | 5.80 ms    | 5.72 ms: 1.01x faster |
| Geometric mean  | (ref)      | 1.05x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | clang-PGO              |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 40.6 ms    | 14.2 ms: 2.85x faster  |
| many_optionals             | 659 us     | 405 us: 1.63x faster   |
| richards_super             | 29.4 ms    | 24.6 ms: 1.20x faster  |
| richards                   | 25.5 ms    | 21.9 ms: 1.16x faster  |
| coverage                   | 46.2 ms    | 40.9 ms: 1.13x faster  |
| mdp                        | 1.41 sec   | 1.30 sec: 1.08x faster |
| genshi_xml                 | 29.5 ms    | 27.4 ms: 1.08x faster  |
| json_dumps                 | 6.19 ms    | 5.76 ms: 1.07x faster  |
| django_template            | 20.9 ms    | 19.5 ms: 1.07x faster  |
| thrift                     | 461 us     | 434 us: 1.06x faster   |
| telco                      | 4.45 ms    | 4.20 ms: 1.06x faster  |
| async_tree_cpu_io_mixed    | 327 ms     | 309 ms: 1.06x faster   |
| pylint                     | 193 ms     | 182 ms: 1.06x faster   |
| raytrace                   | 145 ms     | 137 ms: 1.06x faster   |
| async_generators           | 199 ms     | 188 ms: 1.05x faster   |
| pickle_pure_python         | 184 us     | 175 us: 1.05x faster   |
| async_tree_cpu_io_mixed_tg | 325 ms     | 310 ms: 1.05x faster   |
| sqlglot_v2_normalize       | 62.6 ms    | 59.9 ms: 1.05x faster  |
| json                       | 2.95 ms    | 2.83 ms: 1.04x faster  |
| nqueens                    | 49.7 ms    | 47.7 ms: 1.04x faster  |
| sqlite_synth               | 1.56 us    | 1.49 us: 1.04x faster  |
| typing_runtime_protocols   | 89.7 us    | 86.2 us: 1.04x faster  |
| k_core                     | 1.67 sec   | 1.61 sec: 1.04x faster |
| json_loads                 | 14.8 us    | 14.2 us: 1.04x faster  |
| async_tree_memoization     | 196 ms     | 190 ms: 1.04x faster   |
| genshi_text                | 12.3 ms    | 12.0 ms: 1.03x faster  |
| deltablue                  | 1.64 ms    | 1.59 ms: 1.03x faster  |
| regex_v8                   | 13.9 ms    | 13.5 ms: 1.03x faster  |
| sqlglot_v2_transpile       | 894 us     | 868 us: 1.03x faster   |
| async_tree_memoization_tg  | 201 ms     | 195 ms: 1.03x faster   |
| sphinx                     | 615 ms     | 599 ms: 1.03x faster   |
| crypto_pyaes               | 40.4 ms    | 39.4 ms: 1.03x faster  |
| sqlglot_v2_optimize        | 30.5 ms    | 29.8 ms: 1.02x faster  |
| xml_etree_generate         | 49.4 ms    | 48.4 ms: 1.02x faster  |
| docutils                   | 1.58 sec   | 1.55 sec: 1.02x faster |
| async_tree_none_tg         | 150 ms     | 147 ms: 1.02x faster   |
| sympy_integrate            | 12.0 ms    | 11.8 ms: 1.02x faster  |
| deepcopy_reduce            | 1.51 us    | 1.49 us: 1.02x faster  |
| mako                       | 5.80 ms    | 5.72 ms: 1.01x faster  |
| sympy_expand               | 263 ms     | 259 ms: 1.01x faster   |
| deepcopy                   | 147 us     | 145 us: 1.01x faster   |
| sqlglot_v2_parse           | 695 us     | 686 us: 1.01x faster   |
| logging_format             | 5.90 us    | 5.83 us: 1.01x faster  |
| async_tree_io_tg           | 356 ms     | 352 ms: 1.01x faster   |
| bpe_tokeniser              | 2.52 sec   | 2.50 sec: 1.01x faster |
| unpickle_pure_python       | 110 us     | 109 us: 1.01x faster   |
| xml_etree_parse            | 89.4 ms    | 88.8 ms: 1.01x faster  |
| shortest_path              | 347 ms     | 345 ms: 1.01x faster   |
| pprint_safe_repr           | 429 ms     | 432 ms: 1.01x slower   |
| xml_etree_process          | 33.8 ms    | 34.0 ms: 1.01x slower  |
| sympy_sum                  | 80.7 ms    | 81.4 ms: 1.01x slower  |
| logging_silent             | 44.1 ns    | 44.5 ns: 1.01x slower  |
| dulwich_log                | 39.1 ms    | 39.5 ms: 1.01x slower  |
| connected_components       | 320 ms     | 325 ms: 1.01x slower   |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.05 ms: 1.02x slower  |
| scimark_fft                | 140 ms     | 143 ms: 1.02x slower   |
| xml_etree_iterparse        | 59.5 ms    | 60.7 ms: 1.02x slower  |
| pidigits                   | 145 ms     | 148 ms: 1.02x slower   |
| comprehensions             | 8.65 us    | 8.84 us: 1.02x slower  |
| deepcopy_memo              | 14.7 us    | 15.1 us: 1.03x slower  |
| pprint_pformat             | 853 ms     | 874 ms: 1.03x slower   |
| fannkuch                   | 203 ms     | 209 ms: 1.03x slower   |
| coroutines                 | 10.8 ms    | 11.1 ms: 1.03x slower  |
| meteor_contest             | 66.6 ms    | 68.7 ms: 1.03x slower  |
| pyflate                    | 236 ms     | 245 ms: 1.04x slower   |
| float                      | 37.1 ms    | 38.5 ms: 1.04x slower  |
| regex_compile              | 70.7 ms    | 73.4 ms: 1.04x slower  |
| scimark_monte_carlo        | 31.5 ms    | 32.8 ms: 1.04x slower  |
| hexiom                     | 3.00 ms    | 3.13 ms: 1.04x slower  |
| go                         | 61.0 ms    | 65.1 ms: 1.07x slower  |
| python_startup_no_site     | 18.7 ms    | 20.0 ms: 1.07x slower  |
| python_startup             | 24.7 ms    | 26.6 ms: 1.08x slower  |
| create_gc_cycles           | 1.26 ms    | 1.37 ms: 1.09x slower  |
| spectral_norm              | 40.9 ms    | 44.7 ms: 1.09x slower  |
| tomli_loads                | 1.03 sec   | 1.13 sec: 1.10x slower |
| generators                 | 14.2 ms    | 15.8 ms: 1.11x slower  |
| scimark_lu                 | 44.3 ms    | 49.1 ms: 1.11x slower  |
| regex_effbot               | 1.45 ms    | 1.65 ms: 1.13x slower  |
| scimark_sor                | 51.1 ms    | 59.1 ms: 1.16x slower  |
| nbody                      | 45.7 ms    | 52.9 ms: 1.16x slower  |
| pathlib                    | 23.6 ms    | 30.4 ms: 1.29x slower  |
| asyncio_websockets         | 304 ms     | 400 ms: 1.32x slower   |
| gc_traversal               | 2.09 ms    | 2.79 ms: 1.33x slower  |
| Geometric mean             | (ref)      | 1.01x faster           |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io, pycparser, html5lib, chaos, sympy_str, logging_simple, 2to3, regex_dna

- Geometric mean (including insignificant results): 1.012x faster

# HPT report

- Reliability score: 93.61% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown