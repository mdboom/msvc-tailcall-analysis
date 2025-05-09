# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.041x slower
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TCO-PGO-Ex2            |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 237 ms: 1.04x slower   |
| docutils       | 1.68 sec | 1.81 sec: 1.08x slower |
| sphinx         | 658 ms   | 723 ms: 1.10x slower   |
| Geometric mean | (ref)    | 1.06x slower           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO    | TCO-PGO-Ex2          |
|----------------------------|:------:|:--------------------:|
| asyncio_websockets         | 318 ms | 304 ms: 1.05x faster |
| async_generators           | 226 ms | 224 ms: 1.01x faster |
| async_tree_memoization     | 224 ms | 227 ms: 1.01x slower |
| async_tree_io              | 423 ms | 429 ms: 1.01x slower |
| async_tree_io_tg           | 410 ms | 419 ms: 1.02x slower |
| async_tree_cpu_io_mixed    | 339 ms | 362 ms: 1.07x slower |
| async_tree_cpu_io_mixed_tg | 343 ms | 367 ms: 1.07x slower |
| Geometric mean             | (ref)  | 1.01x slower         |

Benchmark hidden because not significant (4): coroutines, async_tree_none_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 58.8 ms: 1.26x faster |
| float          | 47.8 ms | 44.8 ms: 1.07x faster |
| pidigits       | 152 ms  | 147 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.12x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| regex_dna      | 112 ms  | 117 ms: 1.04x slower  |
| regex_v8       | 13.5 ms | 16.7 ms: 1.23x slower |
| regex_effbot   | 1.42 ms | 1.76 ms: 1.24x slower |
| Geometric mean | (ref)   | 1.12x slower          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TCO-PGO-Ex2            |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.47 sec | 1.38 sec: 1.06x faster |
| unpickle_pure_python | 155 us   | 154 us: 1.01x faster   |
| pickle_pure_python   | 237 us   | 236 us: 1.01x faster   |
| xml_etree_process    | 41.5 ms  | 46.5 ms: 1.12x slower  |
| xml_etree_iterparse  | 63.7 ms  | 71.5 ms: 1.12x slower  |
| json_dumps           | 7.05 ms  | 7.94 ms: 1.13x slower  |
| xml_etree_parse      | 91.2 ms  | 104 ms: 1.14x slower   |
| xml_etree_generate   | 58.7 ms  | 66.8 ms: 1.14x slower  |
| json_loads           | 14.7 us  | 21.1 us: 1.43x slower  |
| Geometric mean       | (ref)    | 1.10x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TCO-PGO-Ex2           |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 20.1 ms: 1.01x slower |
| python_startup         | 26.1 ms | 26.9 ms: 1.03x slower |
| Geometric mean         | (ref)   | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TCO-PGO-Ex2           |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 36.3 ms | 35.3 ms: 1.03x faster |
| genshi_text     | 16.5 ms | 16.2 ms: 1.02x faster |
| mako            | 6.86 ms | 7.44 ms: 1.08x slower |
| django_template | 25.1 ms | 27.5 ms: 1.09x slower |
| Geometric mean  | (ref)   | 1.03x slower          |

All benchmarks:
===============

| Benchmark                  | PGO      | TCO-PGO-Ex2            |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 74.1 ms  | 58.8 ms: 1.26x faster  |
| pathlib                    | 32.1 ms  | 25.6 ms: 1.26x faster  |
| scimark_sor                | 91.0 ms  | 73.9 ms: 1.23x faster  |
| go                         | 88.6 ms  | 78.0 ms: 1.14x faster  |
| fannkuch                   | 296 ms   | 265 ms: 1.12x faster   |
| deltablue                  | 2.29 ms  | 2.09 ms: 1.10x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.48 ms: 1.10x faster  |
| scimark_monte_carlo        | 47.1 ms  | 42.9 ms: 1.10x faster  |
| scimark_fft                | 192 ms   | 178 ms: 1.08x faster   |
| pyflate                    | 315 ms   | 295 ms: 1.07x faster   |
| generators                 | 19.3 ms  | 18.1 ms: 1.07x faster  |
| float                      | 47.8 ms  | 44.8 ms: 1.07x faster  |
| tomli_loads                | 1.47 sec | 1.38 sec: 1.06x faster |
| spectral_norm              | 61.5 ms  | 58.4 ms: 1.05x faster  |
| chaos                      | 43.6 ms  | 41.4 ms: 1.05x faster  |
| hexiom                     | 4.38 ms  | 4.17 ms: 1.05x faster  |
| asyncio_websockets         | 318 ms   | 304 ms: 1.05x faster   |
| mdp                        | 1.64 sec | 1.57 sec: 1.04x faster |
| pidigits                   | 152 ms   | 147 ms: 1.04x faster   |
| logging_silent             | 65.2 ns  | 62.9 ns: 1.04x faster  |
| genshi_xml                 | 36.3 ms  | 35.3 ms: 1.03x faster  |
| scimark_lu                 | 66.9 ms  | 65.2 ms: 1.03x faster  |
| raytrace                   | 191 ms   | 187 ms: 1.02x faster   |
| genshi_text                | 16.5 ms  | 16.2 ms: 1.02x faster  |
| sqlglot_v2_parse           | 892 us   | 876 us: 1.02x faster   |
| crypto_pyaes               | 50.0 ms  | 49.3 ms: 1.01x faster  |
| async_generators           | 226 ms   | 224 ms: 1.01x faster   |
| connected_components       | 329 ms   | 326 ms: 1.01x faster   |
| unpickle_pure_python       | 155 us   | 154 us: 1.01x faster   |
| dulwich_log                | 43.4 ms  | 43.0 ms: 1.01x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 1.09 ms: 1.01x faster  |
| shortest_path              | 359 ms   | 357 ms: 1.01x faster   |
| pickle_pure_python         | 237 us   | 236 us: 1.01x faster   |
| async_tree_memoization     | 224 ms   | 227 ms: 1.01x slower   |
| deepcopy_memo              | 21.0 us  | 21.3 us: 1.01x slower  |
| python_startup_no_site     | 19.8 ms  | 20.1 ms: 1.01x slower  |
| async_tree_io              | 423 ms   | 429 ms: 1.01x slower   |
| meteor_contest             | 76.9 ms  | 78.1 ms: 1.02x slower  |
| logging_simple             | 6.53 us  | 6.67 us: 1.02x slower  |
| logging_format             | 7.03 us  | 7.18 us: 1.02x slower  |
| async_tree_io_tg           | 410 ms   | 419 ms: 1.02x slower   |
| sympy_integrate            | 13.5 ms  | 13.9 ms: 1.03x slower  |
| python_startup             | 26.1 ms  | 26.9 ms: 1.03x slower  |
| nqueens                    | 63.6 ms  | 65.7 ms: 1.03x slower  |
| pycparser                  | 738 ms   | 765 ms: 1.04x slower   |
| 2to3                       | 227 ms   | 237 ms: 1.04x slower   |
| regex_dna                  | 112 ms   | 117 ms: 1.04x slower   |
| deepcopy                   | 190 us   | 199 us: 1.05x slower   |
| bench_thread_pool          | 864 us   | 906 us: 1.05x slower   |
| sqlite_synth               | 1.59 us  | 1.68 us: 1.06x slower  |
| sympy_str                  | 176 ms   | 187 ms: 1.06x slower   |
| typing_runtime_protocols   | 106 us   | 113 us: 1.06x slower   |
| sympy_sum                  | 90.5 ms  | 96.6 ms: 1.07x slower  |
| async_tree_cpu_io_mixed    | 339 ms   | 362 ms: 1.07x slower   |
| bpe_tokeniser              | 2.96 sec | 3.17 sec: 1.07x slower |
| bench_mp_pool              | 88.7 ms  | 95.0 ms: 1.07x slower  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 367 ms: 1.07x slower   |
| sqlglot_v2_normalize       | 73.6 ms  | 79.0 ms: 1.07x slower  |
| sympy_expand               | 302 ms   | 324 ms: 1.07x slower   |
| comprehensions             | 11.3 us  | 12.2 us: 1.08x slower  |
| pylint                     | 201 ms   | 217 ms: 1.08x slower   |
| docutils                   | 1.68 sec | 1.81 sec: 1.08x slower |
| mako                       | 6.86 ms  | 7.44 ms: 1.08x slower  |
| telco                      | 4.89 ms  | 5.33 ms: 1.09x slower  |
| deepcopy_reduce            | 1.94 us  | 2.12 us: 1.09x slower  |
| sqlglot_v2_optimize        | 35.0 ms  | 38.4 ms: 1.09x slower  |
| django_template            | 25.1 ms  | 27.5 ms: 1.09x slower  |
| sphinx                     | 658 ms   | 723 ms: 1.10x slower   |
| create_gc_cycles           | 1.25 ms  | 1.38 ms: 1.11x slower  |
| thrift                     | 507 us   | 561 us: 1.11x slower   |
| xml_etree_process          | 41.5 ms  | 46.5 ms: 1.12x slower  |
| xml_etree_iterparse        | 63.7 ms  | 71.5 ms: 1.12x slower  |
| json_dumps                 | 7.05 ms  | 7.94 ms: 1.13x slower  |
| xml_etree_parse            | 91.2 ms  | 104 ms: 1.14x slower   |
| xml_etree_generate         | 58.7 ms  | 66.8 ms: 1.14x slower  |
| richards                   | 30.7 ms  | 35.0 ms: 1.14x slower  |
| richards_super             | 35.1 ms  | 40.4 ms: 1.15x slower  |
| json                       | 3.14 ms  | 3.77 ms: 1.20x slower  |
| coverage                   | 46.8 ms  | 56.4 ms: 1.21x slower  |
| regex_v8                   | 13.5 ms  | 16.7 ms: 1.23x slower  |
| regex_effbot               | 1.42 ms  | 1.76 ms: 1.24x slower  |
| gc_traversal               | 2.06 ms  | 2.77 ms: 1.35x slower  |
| json_loads                 | 14.7 us  | 21.1 us: 1.43x slower  |
| many_optionals             | 438 us   | 813 us: 1.86x slower   |
| subparsers                 | 16.1 ms  | 47.1 ms: 2.93x slower  |
| Geometric mean             | (ref)    | 1.04x slower           |

Benchmark hidden because not significant (9): coroutines, regex_compile, pprint_safe_repr, html5lib, pprint_pformat, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, k_core

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 98.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown