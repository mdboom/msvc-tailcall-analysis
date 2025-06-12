# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.240x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | clang-PGO              |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 204 ms: 1.17x faster   |
| docutils       | 1.81 sec    | 1.55 sec: 1.17x faster |
| html5lib       | 40.8 ms     | 35.2 ms: 1.16x faster  |
| sphinx         | 723 ms      | 599 ms: 1.21x faster   |
| Geometric mean | (ref)       | 1.18x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | clang-PGO             |
|----------------------------|:-----------:|:---------------------:|
| async_tree_io              | 429 ms      | 349 ms: 1.23x faster  |
| async_tree_none            | 188 ms      | 155 ms: 1.21x faster  |
| coroutines                 | 13.5 ms     | 11.1 ms: 1.21x faster |
| async_tree_none_tg         | 178 ms      | 147 ms: 1.20x faster  |
| async_tree_memoization     | 227 ms      | 190 ms: 1.20x faster  |
| async_tree_io_tg           | 419 ms      | 352 ms: 1.19x faster  |
| async_generators           | 224 ms      | 188 ms: 1.19x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 310 ms: 1.19x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 309 ms: 1.17x faster  |
| async_tree_memoization_tg  | 218 ms      | 195 ms: 1.12x faster  |
| asyncio_websockets         | 304 ms      | 400 ms: 1.32x slower  |
| Geometric mean             | (ref)       | 1.14x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | clang-PGO             |
|----------------|:-----------:|:---------------------:|
| float          | 44.8 ms     | 38.5 ms: 1.16x faster |
| nbody          | 58.8 ms     | 52.9 ms: 1.11x faster |
| pidigits       | 147 ms      | 148 ms: 1.01x slower  |
| Geometric mean | (ref)       | 1.08x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | clang-PGO             |
|----------------|:-----------:|:---------------------:|
| regex_v8       | 16.7 ms     | 13.5 ms: 1.23x faster |
| regex_compile  | 88.0 ms     | 73.4 ms: 1.20x faster |
| regex_effbot   | 1.76 ms     | 1.65 ms: 1.07x faster |
| regex_dna      | 117 ms      | 121 ms: 1.03x slower  |
| Geometric mean | (ref)       | 1.11x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | clang-PGO              |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 14.2 us: 1.49x faster  |
| unpickle_pure_python | 154 us      | 109 us: 1.41x faster   |
| xml_etree_generate   | 66.8 ms     | 48.4 ms: 1.38x faster  |
| json_dumps           | 7.94 ms     | 5.76 ms: 1.38x faster  |
| xml_etree_process    | 46.5 ms     | 34.0 ms: 1.37x faster  |
| pickle_pure_python   | 236 us      | 175 us: 1.34x faster   |
| tomli_loads          | 1.38 sec    | 1.13 sec: 1.22x faster |
| xml_etree_iterparse  | 71.5 ms     | 60.7 ms: 1.18x faster  |
| xml_etree_parse      | 104 ms      | 88.8 ms: 1.17x faster  |
| Geometric mean       | (ref)       | 1.32x faster           |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | clang-PGO             |
|-----------------|:-----------:|:---------------------:|
| django_template | 27.5 ms     | 19.5 ms: 1.41x faster |
| genshi_text     | 16.2 ms     | 12.0 ms: 1.35x faster |
| mako            | 7.44 ms     | 5.72 ms: 1.30x faster |
| genshi_xml      | 35.3 ms     | 27.4 ms: 1.29x faster |
| Geometric mean  | (ref)       | 1.34x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | clang-PGO              |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 47.1 ms     | 14.2 ms: 3.30x faster  |
| many_optionals             | 813 us      | 405 us: 2.01x faster   |
| richards_super             | 40.4 ms     | 24.6 ms: 1.64x faster  |
| richards                   | 35.0 ms     | 21.9 ms: 1.60x faster  |
| json_loads                 | 21.1 us     | 14.2 us: 1.49x faster  |
| deepcopy_reduce            | 2.12 us     | 1.49 us: 1.43x faster  |
| logging_silent             | 62.9 ns     | 44.5 ns: 1.42x faster  |
| unpickle_pure_python       | 154 us      | 109 us: 1.41x faster   |
| deepcopy_memo              | 21.3 us     | 15.1 us: 1.41x faster  |
| django_template            | 27.5 ms     | 19.5 ms: 1.41x faster  |
| comprehensions             | 12.2 us     | 8.84 us: 1.38x faster  |
| xml_etree_generate         | 66.8 ms     | 48.4 ms: 1.38x faster  |
| coverage                   | 56.4 ms     | 40.9 ms: 1.38x faster  |
| nqueens                    | 65.7 ms     | 47.7 ms: 1.38x faster  |
| json_dumps                 | 7.94 ms     | 5.76 ms: 1.38x faster  |
| deepcopy                   | 199 us      | 145 us: 1.37x faster   |
| xml_etree_process          | 46.5 ms     | 34.0 ms: 1.37x faster  |
| raytrace                   | 187 ms      | 137 ms: 1.36x faster   |
| genshi_text                | 16.2 ms     | 12.0 ms: 1.35x faster  |
| pickle_pure_python         | 236 us      | 175 us: 1.34x faster   |
| chaos                      | 41.4 ms     | 31.1 ms: 1.33x faster  |
| hexiom                     | 4.17 ms     | 3.13 ms: 1.33x faster  |
| json                       | 3.77 ms     | 2.83 ms: 1.33x faster  |
| scimark_lu                 | 65.2 ms     | 49.1 ms: 1.33x faster  |
| sqlglot_v2_normalize       | 79.0 ms     | 59.9 ms: 1.32x faster  |
| deltablue                  | 2.09 ms     | 1.59 ms: 1.31x faster  |
| scimark_monte_carlo        | 42.9 ms     | 32.8 ms: 1.31x faster  |
| typing_runtime_protocols   | 113 us      | 86.2 us: 1.31x faster  |
| spectral_norm              | 58.4 ms     | 44.7 ms: 1.31x faster  |
| mako                       | 7.44 ms     | 5.72 ms: 1.30x faster  |
| thrift                     | 561 us      | 434 us: 1.29x faster   |
| pprint_safe_repr           | 558 ms      | 432 ms: 1.29x faster   |
| pprint_pformat             | 1.13 sec    | 874 ms: 1.29x faster   |
| sqlglot_v2_optimize        | 38.4 ms     | 29.8 ms: 1.29x faster  |
| genshi_xml                 | 35.3 ms     | 27.4 ms: 1.29x faster  |
| sqlglot_v2_parse           | 876 us      | 686 us: 1.28x faster   |
| telco                      | 5.33 ms     | 4.20 ms: 1.27x faster  |
| bpe_tokeniser              | 3.17 sec    | 2.50 sec: 1.27x faster |
| fannkuch                   | 265 ms      | 209 ms: 1.27x faster   |
| sqlglot_v2_transpile       | 1.09 ms     | 868 us: 1.26x faster   |
| crypto_pyaes               | 49.3 ms     | 39.4 ms: 1.25x faster  |
| sympy_expand               | 324 ms      | 259 ms: 1.25x faster   |
| scimark_sor                | 73.9 ms     | 59.1 ms: 1.25x faster  |
| scimark_fft                | 178 ms      | 143 ms: 1.25x faster   |
| logging_simple             | 6.67 us     | 5.39 us: 1.24x faster  |
| regex_v8                   | 16.7 ms     | 13.5 ms: 1.23x faster  |
| logging_format             | 7.18 us     | 5.83 us: 1.23x faster  |
| async_tree_io              | 429 ms      | 349 ms: 1.23x faster   |
| tomli_loads                | 1.38 sec    | 1.13 sec: 1.22x faster |
| sympy_str                  | 187 ms      | 153 ms: 1.22x faster   |
| async_tree_none            | 188 ms      | 155 ms: 1.21x faster   |
| coroutines                 | 13.5 ms     | 11.1 ms: 1.21x faster  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.05 ms: 1.21x faster  |
| sphinx                     | 723 ms      | 599 ms: 1.21x faster   |
| mdp                        | 1.57 sec    | 1.30 sec: 1.21x faster |
| pyflate                    | 295 ms      | 245 ms: 1.21x faster   |
| async_tree_none_tg         | 178 ms      | 147 ms: 1.20x faster   |
| pycparser                  | 765 ms      | 637 ms: 1.20x faster   |
| regex_compile              | 88.0 ms     | 73.4 ms: 1.20x faster  |
| go                         | 78.0 ms     | 65.1 ms: 1.20x faster  |
| async_tree_memoization     | 227 ms      | 190 ms: 1.20x faster   |
| async_tree_io_tg           | 419 ms      | 352 ms: 1.19x faster   |
| pylint                     | 217 ms      | 182 ms: 1.19x faster   |
| async_generators           | 224 ms      | 188 ms: 1.19x faster   |
| sympy_sum                  | 96.6 ms     | 81.4 ms: 1.19x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 310 ms: 1.19x faster   |
| xml_etree_iterparse        | 71.5 ms     | 60.7 ms: 1.18x faster  |
| sympy_integrate            | 13.9 ms     | 11.8 ms: 1.18x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 309 ms: 1.17x faster   |
| docutils                   | 1.81 sec    | 1.55 sec: 1.17x faster |
| xml_etree_parse            | 104 ms      | 88.8 ms: 1.17x faster  |
| 2to3                       | 237 ms      | 204 ms: 1.17x faster   |
| float                      | 44.8 ms     | 38.5 ms: 1.16x faster  |
| html5lib                   | 40.8 ms     | 35.2 ms: 1.16x faster  |
| generators                 | 18.1 ms     | 15.8 ms: 1.15x faster  |
| meteor_contest             | 78.1 ms     | 68.7 ms: 1.14x faster  |
| sqlite_synth               | 1.68 us     | 1.49 us: 1.13x faster  |
| async_tree_memoization_tg  | 218 ms      | 195 ms: 1.12x faster   |
| nbody                      | 58.8 ms     | 52.9 ms: 1.11x faster  |
| k_core                     | 1.76 sec    | 1.61 sec: 1.09x faster |
| dulwich_log                | 43.0 ms     | 39.5 ms: 1.09x faster  |
| regex_effbot               | 1.76 ms     | 1.65 ms: 1.07x faster  |
| shortest_path              | 357 ms      | 345 ms: 1.04x faster   |
| pidigits                   | 147 ms      | 148 ms: 1.01x slower   |
| regex_dna                  | 117 ms      | 121 ms: 1.03x slower   |
| pathlib                    | 25.6 ms     | 30.4 ms: 1.19x slower  |
| asyncio_websockets         | 304 ms      | 400 ms: 1.32x slower   |
| Geometric mean             | (ref)       | 1.24x faster           |

Benchmark hidden because not significant (5): python_startup, create_gc_cycles, python_startup_no_site, connected_components, gc_traversal
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.240x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown