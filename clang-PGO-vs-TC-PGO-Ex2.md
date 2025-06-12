# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | clang-PGO              |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 204 ms: 1.06x faster   |
| docutils       | 1.63 sec   | 1.55 sec: 1.05x faster |
| html5lib       | 36.1 ms    | 35.2 ms: 1.02x faster  |
| sphinx         | 638 ms     | 599 ms: 1.06x faster   |
| Geometric mean | (ref)      | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | clang-PGO             |
|----------------------------|:----------:|:---------------------:|
| coroutines                 | 12.4 ms    | 11.1 ms: 1.12x faster |
| async_tree_none            | 170 ms     | 155 ms: 1.09x faster  |
| async_generators           | 206 ms     | 188 ms: 1.09x faster  |
| async_tree_none_tg         | 159 ms     | 147 ms: 1.08x faster  |
| async_tree_memoization     | 205 ms     | 190 ms: 1.08x faster  |
| async_tree_io              | 375 ms     | 349 ms: 1.07x faster  |
| async_tree_memoization_tg  | 209 ms     | 195 ms: 1.07x faster  |
| async_tree_cpu_io_mixed    | 329 ms     | 309 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 310 ms: 1.06x faster  |
| async_tree_io_tg           | 371 ms     | 352 ms: 1.05x faster  |
| asyncio_websockets         | 317 ms     | 400 ms: 1.26x slower  |
| Geometric mean             | (ref)      | 1.05x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | clang-PGO             |
|----------------|:----------:|:---------------------:|
| float          | 40.2 ms    | 38.5 ms: 1.04x faster |
| nbody          | 53.3 ms    | 52.9 ms: 1.01x faster |
| pidigits       | 146 ms     | 148 ms: 1.02x slower  |
| Geometric mean | (ref)      | 1.01x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | clang-PGO             |
|----------------|:----------:|:---------------------:|
| regex_v8       | 14.1 ms    | 13.5 ms: 1.04x faster |
| regex_compile  | 74.8 ms    | 73.4 ms: 1.02x faster |
| regex_dna      | 115 ms     | 121 ms: 1.05x slower  |
| regex_effbot   | 1.40 ms    | 1.65 ms: 1.18x slower |
| Geometric mean | (ref)      | 1.04x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | clang-PGO              |
|----------------------|:----------:|:----------------------:|
| pickle_pure_python   | 201 us     | 175 us: 1.15x faster   |
| unpickle_pure_python | 123 us     | 109 us: 1.13x faster   |
| json_dumps           | 6.48 ms    | 5.76 ms: 1.13x faster  |
| xml_etree_process    | 36.7 ms    | 34.0 ms: 1.08x faster  |
| xml_etree_generate   | 51.5 ms    | 48.4 ms: 1.06x faster  |
| tomli_loads          | 1.17 sec   | 1.13 sec: 1.04x faster |
| json_loads           | 14.5 us    | 14.2 us: 1.02x faster  |
| Geometric mean       | (ref)      | 1.06x faster           |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | clang-PGO             |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 20.0 ms: 1.02x slower |
| python_startup         | 26.0 ms    | 26.6 ms: 1.02x slower |
| Geometric mean         | (ref)      | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | clang-PGO             |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 19.5 ms: 1.20x faster |
| genshi_text     | 14.2 ms    | 12.0 ms: 1.19x faster |
| genshi_xml      | 30.7 ms    | 27.4 ms: 1.12x faster |
| mako            | 6.12 ms    | 5.72 ms: 1.07x faster |
| Geometric mean  | (ref)      | 1.14x faster          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | clang-PGO              |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 44.9 ms    | 14.2 ms: 3.15x faster  |
| many_optionals             | 761 us     | 405 us: 1.88x faster   |
| richards_super             | 32.2 ms    | 24.6 ms: 1.31x faster  |
| richards                   | 27.8 ms    | 21.9 ms: 1.27x faster  |
| coverage                   | 49.5 ms    | 40.9 ms: 1.21x faster  |
| raytrace                   | 166 ms     | 137 ms: 1.21x faster   |
| logging_silent             | 53.3 ns    | 44.5 ns: 1.20x faster  |
| django_template            | 23.4 ms    | 19.5 ms: 1.20x faster  |
| genshi_text                | 14.2 ms    | 12.0 ms: 1.19x faster  |
| deltablue                  | 1.85 ms    | 1.59 ms: 1.16x faster  |
| chaos                      | 35.9 ms    | 31.1 ms: 1.15x faster  |
| pickle_pure_python         | 201 us     | 175 us: 1.15x faster   |
| typing_runtime_protocols   | 98.9 us    | 86.2 us: 1.15x faster  |
| spectral_norm              | 51.1 ms    | 44.7 ms: 1.14x faster  |
| scimark_sor                | 67.5 ms    | 59.1 ms: 1.14x faster  |
| nqueens                    | 54.0 ms    | 47.7 ms: 1.13x faster  |
| deepcopy_memo              | 17.0 us    | 15.1 us: 1.13x faster  |
| scimark_monte_carlo        | 37.0 ms    | 32.8 ms: 1.13x faster  |
| fannkuch                   | 236 ms     | 209 ms: 1.13x faster   |
| unpickle_pure_python       | 123 us     | 109 us: 1.13x faster   |
| json_dumps                 | 6.48 ms    | 5.76 ms: 1.13x faster  |
| genshi_xml                 | 30.7 ms    | 27.4 ms: 1.12x faster  |
| coroutines                 | 12.4 ms    | 11.1 ms: 1.12x faster  |
| sqlglot_v2_normalize       | 66.9 ms    | 59.9 ms: 1.12x faster  |
| deepcopy_reduce            | 1.66 us    | 1.49 us: 1.12x faster  |
| thrift                     | 482 us     | 434 us: 1.11x faster   |
| hexiom                     | 3.47 ms    | 3.13 ms: 1.11x faster  |
| scimark_lu                 | 54.4 ms    | 49.1 ms: 1.11x faster  |
| pprint_safe_repr           | 478 ms     | 432 ms: 1.11x faster   |
| pprint_pformat             | 968 ms     | 874 ms: 1.11x faster   |
| deepcopy                   | 160 us     | 145 us: 1.11x faster   |
| scimark_sparse_mat_mult    | 2.26 ms    | 2.05 ms: 1.10x faster  |
| comprehensions             | 9.73 us    | 8.84 us: 1.10x faster  |
| async_tree_none            | 170 ms     | 155 ms: 1.09x faster   |
| async_generators           | 206 ms     | 188 ms: 1.09x faster   |
| pylint                     | 199 ms     | 182 ms: 1.09x faster   |
| logging_format             | 6.34 us    | 5.83 us: 1.09x faster  |
| bpe_tokeniser              | 2.71 sec   | 2.50 sec: 1.08x faster |
| async_tree_none_tg         | 159 ms     | 147 ms: 1.08x faster   |
| sqlglot_v2_optimize        | 32.2 ms    | 29.8 ms: 1.08x faster  |
| telco                      | 4.54 ms    | 4.20 ms: 1.08x faster  |
| async_tree_memoization     | 205 ms     | 190 ms: 1.08x faster   |
| xml_etree_process          | 36.7 ms    | 34.0 ms: 1.08x faster  |
| sqlglot_v2_parse           | 740 us     | 686 us: 1.08x faster   |
| mdp                        | 1.40 sec   | 1.30 sec: 1.08x faster |
| sqlglot_v2_transpile       | 933 us     | 868 us: 1.07x faster   |
| async_tree_io              | 375 ms     | 349 ms: 1.07x faster   |
| logging_simple             | 5.78 us    | 5.39 us: 1.07x faster  |
| mako                       | 6.12 ms    | 5.72 ms: 1.07x faster  |
| async_tree_memoization_tg  | 209 ms     | 195 ms: 1.07x faster   |
| async_tree_cpu_io_mixed    | 329 ms     | 309 ms: 1.07x faster   |
| scimark_fft                | 152 ms     | 143 ms: 1.06x faster   |
| sphinx                     | 638 ms     | 599 ms: 1.06x faster   |
| xml_etree_generate         | 51.5 ms    | 48.4 ms: 1.06x faster  |
| k_core                     | 1.71 sec   | 1.61 sec: 1.06x faster |
| pyflate                    | 260 ms     | 245 ms: 1.06x faster   |
| 2to3                       | 216 ms     | 204 ms: 1.06x faster   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 310 ms: 1.06x faster   |
| crypto_pyaes               | 41.6 ms    | 39.4 ms: 1.06x faster  |
| async_tree_io_tg           | 371 ms     | 352 ms: 1.05x faster   |
| json                       | 2.98 ms    | 2.83 ms: 1.05x faster  |
| docutils                   | 1.63 sec   | 1.55 sec: 1.05x faster |
| go                         | 68.4 ms    | 65.1 ms: 1.05x faster  |
| float                      | 40.2 ms    | 38.5 ms: 1.04x faster  |
| pycparser                  | 664 ms     | 637 ms: 1.04x faster   |
| regex_v8                   | 14.1 ms    | 13.5 ms: 1.04x faster  |
| sqlite_synth               | 1.56 us    | 1.49 us: 1.04x faster  |
| sympy_expand               | 269 ms     | 259 ms: 1.04x faster   |
| tomli_loads                | 1.17 sec   | 1.13 sec: 1.04x faster |
| sympy_integrate            | 12.2 ms    | 11.8 ms: 1.04x faster  |
| sympy_str                  | 158 ms     | 153 ms: 1.03x faster   |
| html5lib                   | 36.1 ms    | 35.2 ms: 1.02x faster  |
| regex_compile              | 74.8 ms    | 73.4 ms: 1.02x faster  |
| json_loads                 | 14.5 us    | 14.2 us: 1.02x faster  |
| meteor_contest             | 69.5 ms    | 68.7 ms: 1.01x faster  |
| sympy_sum                  | 82.1 ms    | 81.4 ms: 1.01x faster  |
| shortest_path              | 348 ms     | 345 ms: 1.01x faster   |
| nbody                      | 53.3 ms    | 52.9 ms: 1.01x faster  |
| connected_components       | 321 ms     | 325 ms: 1.01x slower   |
| pidigits                   | 146 ms     | 148 ms: 1.02x slower   |
| python_startup_no_site     | 19.6 ms    | 20.0 ms: 1.02x slower  |
| python_startup             | 26.0 ms    | 26.6 ms: 1.02x slower  |
| regex_dna                  | 115 ms     | 121 ms: 1.05x slower   |
| generators                 | 14.8 ms    | 15.8 ms: 1.06x slower  |
| create_gc_cycles           | 1.27 ms    | 1.37 ms: 1.08x slower  |
| regex_effbot               | 1.40 ms    | 1.65 ms: 1.18x slower  |
| pathlib                    | 24.3 ms    | 30.4 ms: 1.25x slower  |
| asyncio_websockets         | 317 ms     | 400 ms: 1.26x slower   |
| gc_traversal               | 2.07 ms    | 2.79 ms: 1.34x slower  |
| Geometric mean             | (ref)      | 1.08x faster           |

Benchmark hidden because not significant (3): xml_etree_parse, dulwich_log, xml_etree_iterparse
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown