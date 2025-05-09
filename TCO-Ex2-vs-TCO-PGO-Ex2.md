# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.239x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-Ex2                |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 293 ms: 1.23x slower   |
| docutils       | 1.81 sec    | 2.11 sec: 1.16x slower |
| html5lib       | 40.8 ms     | 51.3 ms: 1.26x slower  |
| sphinx         | 723 ms      | 843 ms: 1.17x slower   |
| Geometric mean | (ref)       | 1.20x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TCO-Ex2               |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 304 ms      | 311 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 428 ms: 1.16x slower  |
| async_tree_cpu_io_mixed    | 362 ms      | 434 ms: 1.20x slower  |
| async_tree_io              | 429 ms      | 551 ms: 1.28x slower  |
| async_tree_memoization     | 227 ms      | 297 ms: 1.31x slower  |
| async_tree_none            | 188 ms      | 248 ms: 1.32x slower  |
| async_tree_none_tg         | 178 ms      | 236 ms: 1.33x slower  |
| async_tree_memoization_tg  | 218 ms      | 292 ms: 1.34x slower  |
| async_tree_io_tg           | 419 ms      | 563 ms: 1.34x slower  |
| async_generators           | 224 ms      | 321 ms: 1.44x slower  |
| coroutines                 | 13.5 ms     | 22.1 ms: 1.64x slower |
| Geometric mean             | (ref)       | 1.30x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| pidigits       | 147 ms      | 148 ms: 1.01x slower  |
| float          | 44.8 ms     | 73.5 ms: 1.64x slower |
| nbody          | 58.8 ms     | 98.8 ms: 1.68x slower |
| Geometric mean | (ref)       | 1.41x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.76 ms     | 1.77 ms: 1.01x slower |
| regex_compile  | 88.0 ms     | 123 ms: 1.40x slower  |
| Geometric mean | (ref)       | 1.09x slower          |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TCO-Ex2                |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 21.4 us: 1.02x slower  |
| xml_etree_parse      | 104 ms      | 108 ms: 1.04x slower   |
| json_dumps           | 7.94 ms     | 8.99 ms: 1.13x slower  |
| xml_etree_iterparse  | 71.5 ms     | 87.5 ms: 1.22x slower  |
| xml_etree_generate   | 66.8 ms     | 87.5 ms: 1.31x slower  |
| xml_etree_process    | 46.5 ms     | 63.0 ms: 1.35x slower  |
| tomli_loads          | 1.38 sec    | 1.97 sec: 1.42x slower |
| pickle_pure_python   | 236 us      | 354 us: 1.50x slower   |
| unpickle_pure_python | 154 us      | 271 us: 1.76x slower   |
| Geometric mean       | (ref)       | 1.29x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TCO-PGO-Ex2 | TCO-Ex2               |
|----------------|:-----------:|:---------------------:|
| python_startup | 26.9 ms     | 27.2 ms: 1.01x slower |
| Geometric mean | (ref)       | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TCO-Ex2               |
|-----------------|:-----------:|:---------------------:|
| django_template | 27.5 ms     | 35.8 ms: 1.30x slower |
| genshi_xml      | 35.3 ms     | 48.8 ms: 1.38x slower |
| genshi_text     | 16.2 ms     | 23.4 ms: 1.44x slower |
| mako            | 7.44 ms     | 11.4 ms: 1.54x slower |
| Geometric mean  | (ref)       | 1.42x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TCO-Ex2                |
|----------------------------|:-----------:|:----------------------:|
| gc_traversal               | 2.77 ms     | 2.79 ms: 1.01x slower  |
| regex_effbot               | 1.76 ms     | 1.77 ms: 1.01x slower  |
| create_gc_cycles           | 1.38 ms     | 1.40 ms: 1.01x slower  |
| pidigits                   | 147 ms      | 148 ms: 1.01x slower   |
| python_startup             | 26.9 ms     | 27.2 ms: 1.01x slower  |
| json_loads                 | 21.1 us     | 21.4 us: 1.02x slower  |
| asyncio_websockets         | 304 ms      | 311 ms: 1.03x slower   |
| bench_mp_pool              | 95.0 ms     | 97.6 ms: 1.03x slower  |
| k_core                     | 1.76 sec    | 1.83 sec: 1.04x slower |
| xml_etree_parse            | 104 ms      | 108 ms: 1.04x slower   |
| json                       | 3.77 ms     | 3.94 ms: 1.04x slower  |
| pathlib                    | 25.6 ms     | 26.8 ms: 1.05x slower  |
| sqlite_synth               | 1.68 us     | 1.78 us: 1.06x slower  |
| subparsers                 | 47.1 ms     | 50.4 ms: 1.07x slower  |
| shortest_path              | 357 ms      | 384 ms: 1.07x slower   |
| connected_components       | 326 ms      | 351 ms: 1.08x slower   |
| coverage                   | 56.4 ms     | 61.1 ms: 1.08x slower  |
| many_optionals             | 813 us      | 890 us: 1.09x slower   |
| bench_thread_pool          | 906 us      | 1.01 ms: 1.12x slower  |
| json_dumps                 | 7.94 ms     | 8.99 ms: 1.13x slower  |
| pylint                     | 217 ms      | 249 ms: 1.15x slower   |
| mdp                        | 1.57 sec    | 1.82 sec: 1.16x slower |
| docutils                   | 1.81 sec    | 2.11 sec: 1.16x slower |
| async_tree_cpu_io_mixed_tg | 367 ms      | 428 ms: 1.16x slower   |
| sphinx                     | 723 ms      | 843 ms: 1.17x slower   |
| dulwich_log                | 43.0 ms     | 50.5 ms: 1.17x slower  |
| telco                      | 5.33 ms     | 6.34 ms: 1.19x slower  |
| async_tree_cpu_io_mixed    | 362 ms      | 434 ms: 1.20x slower   |
| thrift                     | 561 us      | 680 us: 1.21x slower   |
| meteor_contest             | 78.1 ms     | 95.0 ms: 1.22x slower  |
| sympy_sum                  | 96.6 ms     | 118 ms: 1.22x slower   |
| xml_etree_iterparse        | 71.5 ms     | 87.5 ms: 1.22x slower  |
| sympy_expand               | 324 ms      | 399 ms: 1.23x slower   |
| 2to3                       | 237 ms      | 293 ms: 1.23x slower   |
| html5lib                   | 40.8 ms     | 51.3 ms: 1.26x slower  |
| sympy_str                  | 187 ms      | 234 ms: 1.26x slower   |
| sympy_integrate            | 13.9 ms     | 17.5 ms: 1.26x slower  |
| pycparser                  | 765 ms      | 968 ms: 1.27x slower   |
| logging_format             | 7.18 us     | 9.13 us: 1.27x slower  |
| deepcopy_reduce            | 2.12 us     | 2.71 us: 1.27x slower  |
| async_tree_io              | 429 ms      | 551 ms: 1.28x slower   |
| sqlglot_v2_optimize        | 38.4 ms     | 49.6 ms: 1.29x slower  |
| logging_simple             | 6.67 us     | 8.63 us: 1.29x slower  |
| typing_runtime_protocols   | 113 us      | 146 us: 1.30x slower   |
| django_template            | 27.5 ms     | 35.8 ms: 1.30x slower  |
| async_tree_memoization     | 227 ms      | 297 ms: 1.31x slower   |
| sqlglot_v2_normalize       | 79.0 ms     | 103 ms: 1.31x slower   |
| xml_etree_generate         | 66.8 ms     | 87.5 ms: 1.31x slower  |
| async_tree_none            | 188 ms      | 248 ms: 1.32x slower   |
| async_tree_none_tg         | 178 ms      | 236 ms: 1.33x slower   |
| deepcopy                   | 199 us      | 266 us: 1.34x slower   |
| async_tree_memoization_tg  | 218 ms      | 292 ms: 1.34x slower   |
| async_tree_io_tg           | 419 ms      | 563 ms: 1.34x slower   |
| xml_etree_process          | 46.5 ms     | 63.0 ms: 1.35x slower  |
| bpe_tokeniser              | 3.17 sec    | 4.30 sec: 1.36x slower |
| genshi_xml                 | 35.3 ms     | 48.8 ms: 1.38x slower  |
| regex_compile              | 88.0 ms     | 123 ms: 1.40x slower   |
| pprint_safe_repr           | 558 ms      | 789 ms: 1.41x slower   |
| nqueens                    | 65.7 ms     | 93.2 ms: 1.42x slower  |
| tomli_loads                | 1.38 sec    | 1.97 sec: 1.42x slower |
| pprint_pformat             | 1.13 sec    | 1.61 sec: 1.43x slower |
| async_generators           | 224 ms      | 321 ms: 1.44x slower   |
| richards_super             | 40.4 ms     | 58.0 ms: 1.44x slower  |
| genshi_text                | 16.2 ms     | 23.4 ms: 1.44x slower  |
| fannkuch                   | 265 ms      | 386 ms: 1.46x slower   |
| richards                   | 35.0 ms     | 51.0 ms: 1.46x slower  |
| sqlglot_v2_transpile       | 1.09 ms     | 1.62 ms: 1.48x slower  |
| pickle_pure_python         | 236 us      | 354 us: 1.50x slower   |
| scimark_fft                | 178 ms      | 267 ms: 1.50x slower   |
| sqlglot_v2_parse           | 876 us      | 1.34 ms: 1.53x slower  |
| mako                       | 7.44 ms     | 11.4 ms: 1.54x slower  |
| pyflate                    | 295 ms      | 457 ms: 1.55x slower   |
| deepcopy_memo              | 21.3 us     | 33.0 us: 1.55x slower  |
| crypto_pyaes               | 49.3 ms     | 76.8 ms: 1.56x slower  |
| comprehensions             | 12.2 us     | 19.4 us: 1.59x slower  |
| chaos                      | 41.4 ms     | 67.0 ms: 1.62x slower  |
| raytrace                   | 187 ms      | 306 ms: 1.64x slower   |
| coroutines                 | 13.5 ms     | 22.1 ms: 1.64x slower  |
| float                      | 44.8 ms     | 73.5 ms: 1.64x slower  |
| spectral_norm              | 58.4 ms     | 97.1 ms: 1.66x slower  |
| nbody                      | 58.8 ms     | 98.8 ms: 1.68x slower  |
| scimark_sparse_mat_mult    | 2.48 ms     | 4.27 ms: 1.72x slower  |
| hexiom                     | 4.17 ms     | 7.27 ms: 1.74x slower  |
| scimark_monte_carlo        | 42.9 ms     | 75.2 ms: 1.75x slower  |
| unpickle_pure_python       | 154 us      | 271 us: 1.76x slower   |
| go                         | 78.0 ms     | 138 ms: 1.77x slower   |
| scimark_lu                 | 65.2 ms     | 116 ms: 1.77x slower   |
| scimark_sor                | 73.9 ms     | 133 ms: 1.80x slower   |
| generators                 | 18.1 ms     | 33.5 ms: 1.85x slower  |
| logging_silent             | 62.9 ns     | 121 ns: 1.93x slower   |
| deltablue                  | 2.09 ms     | 4.08 ms: 1.95x slower  |
| Geometric mean             | (ref)       | 1.31x slower           |

Benchmark hidden because not significant (3): regex_dna, python_startup_no_site, regex_v8

- Geometric mean (including insignificant results): 1.239x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: unknown