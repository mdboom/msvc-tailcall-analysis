# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.193x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TCO-PGO-Ex2            |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 237 ms: 1.17x slower   |
| docutils       | 1.55 sec  | 1.81 sec: 1.17x slower |
| html5lib       | 35.2 ms   | 40.8 ms: 1.16x slower  |
| sphinx         | 599 ms    | 723 ms: 1.21x slower   |
| Geometric mean | (ref)     | 1.18x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TCO-PGO-Ex2           |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 304 ms: 1.32x faster  |
| async_tree_memoization_tg  | 195 ms    | 218 ms: 1.12x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 362 ms: 1.17x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 367 ms: 1.19x slower  |
| async_generators           | 188 ms    | 224 ms: 1.19x slower  |
| async_tree_io_tg           | 352 ms    | 419 ms: 1.19x slower  |
| async_tree_memoization     | 190 ms    | 227 ms: 1.20x slower  |
| async_tree_none_tg         | 147 ms    | 178 ms: 1.20x slower  |
| coroutines                 | 11.1 ms   | 13.5 ms: 1.21x slower |
| async_tree_none            | 155 ms    | 188 ms: 1.21x slower  |
| async_tree_io              | 349 ms    | 429 ms: 1.23x slower  |
| Geometric mean             | (ref)     | 1.14x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TCO-PGO-Ex2           |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 147 ms: 1.01x faster  |
| nbody          | 52.9 ms   | 58.8 ms: 1.11x slower |
| float          | 38.5 ms   | 44.8 ms: 1.16x slower |
| Geometric mean | (ref)     | 1.08x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TCO-PGO-Ex2           |
|----------------|:---------:|:---------------------:|
| regex_dna      | 121 ms    | 117 ms: 1.03x faster  |
| regex_effbot   | 1.65 ms   | 1.76 ms: 1.07x slower |
| regex_compile  | 73.4 ms   | 88.0 ms: 1.20x slower |
| regex_v8       | 13.5 ms   | 16.7 ms: 1.23x slower |
| Geometric mean | (ref)     | 1.11x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TCO-PGO-Ex2            |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 104 ms: 1.17x slower   |
| xml_etree_iterparse  | 60.7 ms   | 71.5 ms: 1.18x slower  |
| tomli_loads          | 1.13 sec  | 1.38 sec: 1.22x slower |
| pickle_pure_python   | 175 us    | 236 us: 1.34x slower   |
| xml_etree_process    | 34.0 ms   | 46.5 ms: 1.37x slower  |
| json_dumps           | 5.76 ms   | 7.94 ms: 1.38x slower  |
| xml_etree_generate   | 48.4 ms   | 66.8 ms: 1.38x slower  |
| unpickle_pure_python | 109 us    | 154 us: 1.41x slower   |
| json_loads           | 14.2 us   | 21.1 us: 1.49x slower  |
| Geometric mean       | (ref)     | 1.32x slower           |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TCO-PGO-Ex2           |
|-----------------|:---------:|:---------------------:|
| genshi_xml      | 27.4 ms   | 35.3 ms: 1.29x slower |
| mako            | 5.72 ms   | 7.44 ms: 1.30x slower |
| genshi_text     | 12.0 ms   | 16.2 ms: 1.35x slower |
| django_template | 19.5 ms   | 27.5 ms: 1.41x slower |
| Geometric mean  | (ref)     | 1.34x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TCO-PGO-Ex2            |
|----------------------------|:---------:|:----------------------:|
| asyncio_websockets         | 400 ms    | 304 ms: 1.32x faster   |
| pathlib                    | 30.4 ms   | 25.6 ms: 1.19x faster  |
| regex_dna                  | 121 ms    | 117 ms: 1.03x faster   |
| pidigits                   | 148 ms    | 147 ms: 1.01x faster   |
| shortest_path              | 345 ms    | 357 ms: 1.04x slower   |
| regex_effbot               | 1.65 ms   | 1.76 ms: 1.07x slower  |
| dulwich_log                | 39.5 ms   | 43.0 ms: 1.09x slower  |
| k_core                     | 1.61 sec  | 1.76 sec: 1.09x slower |
| nbody                      | 52.9 ms   | 58.8 ms: 1.11x slower  |
| async_tree_memoization_tg  | 195 ms    | 218 ms: 1.12x slower   |
| sqlite_synth               | 1.49 us   | 1.68 us: 1.13x slower  |
| meteor_contest             | 68.7 ms   | 78.1 ms: 1.14x slower  |
| generators                 | 15.8 ms   | 18.1 ms: 1.15x slower  |
| html5lib                   | 35.2 ms   | 40.8 ms: 1.16x slower  |
| float                      | 38.5 ms   | 44.8 ms: 1.16x slower  |
| 2to3                       | 204 ms    | 237 ms: 1.17x slower   |
| xml_etree_parse            | 88.8 ms   | 104 ms: 1.17x slower   |
| docutils                   | 1.55 sec  | 1.81 sec: 1.17x slower |
| async_tree_cpu_io_mixed    | 309 ms    | 362 ms: 1.17x slower   |
| sympy_integrate            | 11.8 ms   | 13.9 ms: 1.18x slower  |
| xml_etree_iterparse        | 60.7 ms   | 71.5 ms: 1.18x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 367 ms: 1.19x slower   |
| sympy_sum                  | 81.4 ms   | 96.6 ms: 1.19x slower  |
| async_generators           | 188 ms    | 224 ms: 1.19x slower   |
| pylint                     | 182 ms    | 217 ms: 1.19x slower   |
| async_tree_io_tg           | 352 ms    | 419 ms: 1.19x slower   |
| async_tree_memoization     | 190 ms    | 227 ms: 1.20x slower   |
| go                         | 65.1 ms   | 78.0 ms: 1.20x slower  |
| regex_compile              | 73.4 ms   | 88.0 ms: 1.20x slower  |
| pycparser                  | 637 ms    | 765 ms: 1.20x slower   |
| async_tree_none_tg         | 147 ms    | 178 ms: 1.20x slower   |
| pyflate                    | 245 ms    | 295 ms: 1.21x slower   |
| mdp                        | 1.30 sec  | 1.57 sec: 1.21x slower |
| sphinx                     | 599 ms    | 723 ms: 1.21x slower   |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.48 ms: 1.21x slower  |
| coroutines                 | 11.1 ms   | 13.5 ms: 1.21x slower  |
| async_tree_none            | 155 ms    | 188 ms: 1.21x slower   |
| sympy_str                  | 153 ms    | 187 ms: 1.22x slower   |
| tomli_loads                | 1.13 sec  | 1.38 sec: 1.22x slower |
| async_tree_io              | 349 ms    | 429 ms: 1.23x slower   |
| logging_format             | 5.83 us   | 7.18 us: 1.23x slower  |
| regex_v8                   | 13.5 ms   | 16.7 ms: 1.23x slower  |
| logging_simple             | 5.39 us   | 6.67 us: 1.24x slower  |
| scimark_fft                | 143 ms    | 178 ms: 1.25x slower   |
| scimark_sor                | 59.1 ms   | 73.9 ms: 1.25x slower  |
| sympy_expand               | 259 ms    | 324 ms: 1.25x slower   |
| crypto_pyaes               | 39.4 ms   | 49.3 ms: 1.25x slower  |
| sqlglot_v2_transpile       | 868 us    | 1.09 ms: 1.26x slower  |
| fannkuch                   | 209 ms    | 265 ms: 1.27x slower   |
| bpe_tokeniser              | 2.50 sec  | 3.17 sec: 1.27x slower |
| telco                      | 4.20 ms   | 5.33 ms: 1.27x slower  |
| sqlglot_v2_parse           | 686 us    | 876 us: 1.28x slower   |
| genshi_xml                 | 27.4 ms   | 35.3 ms: 1.29x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 38.4 ms: 1.29x slower  |
| pprint_pformat             | 874 ms    | 1.13 sec: 1.29x slower |
| pprint_safe_repr           | 432 ms    | 558 ms: 1.29x slower   |
| thrift                     | 434 us    | 561 us: 1.29x slower   |
| mako                       | 5.72 ms   | 7.44 ms: 1.30x slower  |
| spectral_norm              | 44.7 ms   | 58.4 ms: 1.31x slower  |
| typing_runtime_protocols   | 86.2 us   | 113 us: 1.31x slower   |
| scimark_monte_carlo        | 32.8 ms   | 42.9 ms: 1.31x slower  |
| deltablue                  | 1.59 ms   | 2.09 ms: 1.31x slower  |
| sqlglot_v2_normalize       | 59.9 ms   | 79.0 ms: 1.32x slower  |
| scimark_lu                 | 49.1 ms   | 65.2 ms: 1.33x slower  |
| json                       | 2.83 ms   | 3.77 ms: 1.33x slower  |
| hexiom                     | 3.13 ms   | 4.17 ms: 1.33x slower  |
| chaos                      | 31.1 ms   | 41.4 ms: 1.33x slower  |
| pickle_pure_python         | 175 us    | 236 us: 1.34x slower   |
| genshi_text                | 12.0 ms   | 16.2 ms: 1.35x slower  |
| raytrace                   | 137 ms    | 187 ms: 1.36x slower   |
| xml_etree_process          | 34.0 ms   | 46.5 ms: 1.37x slower  |
| deepcopy                   | 145 us    | 199 us: 1.37x slower   |
| json_dumps                 | 5.76 ms   | 7.94 ms: 1.38x slower  |
| nqueens                    | 47.7 ms   | 65.7 ms: 1.38x slower  |
| coverage                   | 40.9 ms   | 56.4 ms: 1.38x slower  |
| xml_etree_generate         | 48.4 ms   | 66.8 ms: 1.38x slower  |
| comprehensions             | 8.84 us   | 12.2 us: 1.38x slower  |
| django_template            | 19.5 ms   | 27.5 ms: 1.41x slower  |
| deepcopy_memo              | 15.1 us   | 21.3 us: 1.41x slower  |
| unpickle_pure_python       | 109 us    | 154 us: 1.41x slower   |
| logging_silent             | 44.5 ns   | 62.9 ns: 1.42x slower  |
| deepcopy_reduce            | 1.49 us   | 2.12 us: 1.43x slower  |
| json_loads                 | 14.2 us   | 21.1 us: 1.49x slower  |
| richards                   | 21.9 ms   | 35.0 ms: 1.60x slower  |
| richards_super             | 24.6 ms   | 40.4 ms: 1.64x slower  |
| many_optionals             | 405 us    | 813 us: 2.01x slower   |
| subparsers                 | 14.2 ms   | 47.1 ms: 3.30x slower  |
| Geometric mean             | (ref)     | 1.24x slower           |

Benchmark hidden because not significant (5): gc_traversal, connected_components, python_startup_no_site, create_gc_cycles, python_startup
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.193x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: unknown