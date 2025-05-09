# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.044x faster
- HPT reliability: 98.62%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | PGO                    |
|----------------|:--------:|:----------------------:|
| 2to3           | 237 ms   | 227 ms: 1.04x faster   |
| docutils       | 1.81 sec | 1.68 sec: 1.08x faster |
| sphinx         | 723 ms   | 658 ms: 1.10x faster   |
| Geometric mean | (ref)    | 1.06x faster           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | PGO                  |
|----------------------------|:-------:|:--------------------:|
| async_tree_cpu_io_mixed_tg | 367 ms  | 343 ms: 1.07x faster |
| async_tree_cpu_io_mixed    | 362 ms  | 339 ms: 1.07x faster |
| async_tree_io_tg           | 419 ms  | 410 ms: 1.02x faster |
| async_tree_io              | 429 ms  | 423 ms: 1.01x faster |
| async_tree_memoization     | 227 ms  | 224 ms: 1.01x faster |
| async_generators           | 224 ms  | 226 ms: 1.01x slower |
| asyncio_websockets         | 304 ms  | 318 ms: 1.05x slower |
| Geometric mean             | (ref)   | 1.01x faster         |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_none, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | PGO                   |
|----------------|:-------:|:---------------------:|
| pidigits       | 147 ms  | 152 ms: 1.04x slower  |
| float          | 44.8 ms | 47.8 ms: 1.07x slower |
| nbody          | 58.8 ms | 74.1 ms: 1.26x slower |
| Geometric mean | (ref)   | 1.12x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | PGO                   |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.76 ms | 1.42 ms: 1.24x faster |
| regex_v8       | 16.7 ms | 13.5 ms: 1.23x faster |
| regex_dna      | 117 ms  | 112 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.12x faster          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | PGO                    |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.1 us  | 14.7 us: 1.43x faster  |
| xml_etree_generate   | 66.8 ms  | 58.7 ms: 1.14x faster  |
| xml_etree_parse      | 104 ms   | 91.2 ms: 1.14x faster  |
| json_dumps           | 7.94 ms  | 7.05 ms: 1.13x faster  |
| xml_etree_iterparse  | 71.5 ms  | 63.7 ms: 1.12x faster  |
| xml_etree_process    | 46.5 ms  | 41.5 ms: 1.12x faster  |
| pickle_pure_python   | 236 us   | 237 us: 1.01x slower   |
| unpickle_pure_python | 154 us   | 155 us: 1.01x slower   |
| tomli_loads          | 1.38 sec | 1.47 sec: 1.06x slower |
| Geometric mean       | (ref)    | 1.10x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-Ex2 | PGO                   |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.9 ms | 26.1 ms: 1.03x faster |
| python_startup_no_site | 20.1 ms | 19.8 ms: 1.01x faster |
| Geometric mean         | (ref)   | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | PGO                   |
|-----------------|:-------:|:---------------------:|
| django_template | 27.5 ms | 25.1 ms: 1.09x faster |
| mako            | 7.44 ms | 6.86 ms: 1.08x faster |
| genshi_text     | 16.2 ms | 16.5 ms: 1.02x slower |
| genshi_xml      | 35.3 ms | 36.3 ms: 1.03x slower |
| Geometric mean  | (ref)   | 1.03x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | PGO                    |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 47.1 ms  | 16.1 ms: 2.93x faster  |
| many_optionals             | 813 us   | 438 us: 1.86x faster   |
| json_loads                 | 21.1 us  | 14.7 us: 1.43x faster  |
| gc_traversal               | 2.77 ms  | 2.06 ms: 1.35x faster  |
| regex_effbot               | 1.76 ms  | 1.42 ms: 1.24x faster  |
| regex_v8                   | 16.7 ms  | 13.5 ms: 1.23x faster  |
| coverage                   | 56.4 ms  | 46.8 ms: 1.21x faster  |
| json                       | 3.77 ms  | 3.14 ms: 1.20x faster  |
| richards_super             | 40.4 ms  | 35.1 ms: 1.15x faster  |
| richards                   | 35.0 ms  | 30.7 ms: 1.14x faster  |
| xml_etree_generate         | 66.8 ms  | 58.7 ms: 1.14x faster  |
| xml_etree_parse            | 104 ms   | 91.2 ms: 1.14x faster  |
| json_dumps                 | 7.94 ms  | 7.05 ms: 1.13x faster  |
| xml_etree_iterparse        | 71.5 ms  | 63.7 ms: 1.12x faster  |
| xml_etree_process          | 46.5 ms  | 41.5 ms: 1.12x faster  |
| thrift                     | 561 us   | 507 us: 1.11x faster   |
| create_gc_cycles           | 1.38 ms  | 1.25 ms: 1.11x faster  |
| sphinx                     | 723 ms   | 658 ms: 1.10x faster   |
| django_template            | 27.5 ms  | 25.1 ms: 1.09x faster  |
| sqlglot_v2_optimize        | 38.4 ms  | 35.0 ms: 1.09x faster  |
| deepcopy_reduce            | 2.12 us  | 1.94 us: 1.09x faster  |
| telco                      | 5.33 ms  | 4.89 ms: 1.09x faster  |
| mako                       | 7.44 ms  | 6.86 ms: 1.08x faster  |
| docutils                   | 1.81 sec | 1.68 sec: 1.08x faster |
| pylint                     | 217 ms   | 201 ms: 1.08x faster   |
| comprehensions             | 12.2 us  | 11.3 us: 1.08x faster  |
| sympy_expand               | 324 ms   | 302 ms: 1.07x faster   |
| sqlglot_v2_normalize       | 79.0 ms  | 73.6 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms   | 343 ms: 1.07x faster   |
| bench_mp_pool              | 95.0 ms  | 88.7 ms: 1.07x faster  |
| bpe_tokeniser              | 3.17 sec | 2.96 sec: 1.07x faster |
| async_tree_cpu_io_mixed    | 362 ms   | 339 ms: 1.07x faster   |
| sympy_sum                  | 96.6 ms  | 90.5 ms: 1.07x faster  |
| typing_runtime_protocols   | 113 us   | 106 us: 1.06x faster   |
| sympy_str                  | 187 ms   | 176 ms: 1.06x faster   |
| sqlite_synth               | 1.68 us  | 1.59 us: 1.06x faster  |
| bench_thread_pool          | 906 us   | 864 us: 1.05x faster   |
| deepcopy                   | 199 us   | 190 us: 1.05x faster   |
| regex_dna                  | 117 ms   | 112 ms: 1.04x faster   |
| 2to3                       | 237 ms   | 227 ms: 1.04x faster   |
| pycparser                  | 765 ms   | 738 ms: 1.04x faster   |
| nqueens                    | 65.7 ms  | 63.6 ms: 1.03x faster  |
| python_startup             | 26.9 ms  | 26.1 ms: 1.03x faster  |
| sympy_integrate            | 13.9 ms  | 13.5 ms: 1.03x faster  |
| async_tree_io_tg           | 419 ms   | 410 ms: 1.02x faster   |
| logging_format             | 7.18 us  | 7.03 us: 1.02x faster  |
| logging_simple             | 6.67 us  | 6.53 us: 1.02x faster  |
| meteor_contest             | 78.1 ms  | 76.9 ms: 1.02x faster  |
| async_tree_io              | 429 ms   | 423 ms: 1.01x faster   |
| python_startup_no_site     | 20.1 ms  | 19.8 ms: 1.01x faster  |
| deepcopy_memo              | 21.3 us  | 21.0 us: 1.01x faster  |
| async_tree_memoization     | 227 ms   | 224 ms: 1.01x faster   |
| pickle_pure_python         | 236 us   | 237 us: 1.01x slower   |
| shortest_path              | 357 ms   | 359 ms: 1.01x slower   |
| sqlglot_v2_transpile       | 1.09 ms  | 1.10 ms: 1.01x slower  |
| dulwich_log                | 43.0 ms  | 43.4 ms: 1.01x slower  |
| unpickle_pure_python       | 154 us   | 155 us: 1.01x slower   |
| connected_components       | 326 ms   | 329 ms: 1.01x slower   |
| async_generators           | 224 ms   | 226 ms: 1.01x slower   |
| crypto_pyaes               | 49.3 ms  | 50.0 ms: 1.01x slower  |
| sqlglot_v2_parse           | 876 us   | 892 us: 1.02x slower   |
| genshi_text                | 16.2 ms  | 16.5 ms: 1.02x slower  |
| raytrace                   | 187 ms   | 191 ms: 1.02x slower   |
| scimark_lu                 | 65.2 ms  | 66.9 ms: 1.03x slower  |
| genshi_xml                 | 35.3 ms  | 36.3 ms: 1.03x slower  |
| logging_silent             | 62.9 ns  | 65.2 ns: 1.04x slower  |
| pidigits                   | 147 ms   | 152 ms: 1.04x slower   |
| mdp                        | 1.57 sec | 1.64 sec: 1.04x slower |
| asyncio_websockets         | 304 ms   | 318 ms: 1.05x slower   |
| hexiom                     | 4.17 ms  | 4.38 ms: 1.05x slower  |
| chaos                      | 41.4 ms  | 43.6 ms: 1.05x slower  |
| spectral_norm              | 58.4 ms  | 61.5 ms: 1.05x slower  |
| tomli_loads                | 1.38 sec | 1.47 sec: 1.06x slower |
| float                      | 44.8 ms  | 47.8 ms: 1.07x slower  |
| generators                 | 18.1 ms  | 19.3 ms: 1.07x slower  |
| pyflate                    | 295 ms   | 315 ms: 1.07x slower   |
| scimark_fft                | 178 ms   | 192 ms: 1.08x slower   |
| scimark_monte_carlo        | 42.9 ms  | 47.1 ms: 1.10x slower  |
| scimark_sparse_mat_mult    | 2.48 ms  | 2.72 ms: 1.10x slower  |
| deltablue                  | 2.09 ms  | 2.29 ms: 1.10x slower  |
| fannkuch                   | 265 ms   | 296 ms: 1.12x slower   |
| go                         | 78.0 ms  | 88.6 ms: 1.14x slower  |
| scimark_sor                | 73.9 ms  | 91.0 ms: 1.23x slower  |
| pathlib                    | 25.6 ms  | 32.1 ms: 1.26x slower  |
| nbody                      | 58.8 ms  | 74.1 ms: 1.26x slower  |
| Geometric mean             | (ref)    | 1.04x faster           |

Benchmark hidden because not significant (9): k_core, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, pprint_pformat, html5lib, pprint_safe_repr, regex_compile, coroutines

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 98.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown