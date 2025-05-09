# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.001x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-Ex2  | default                |
|----------------|:--------:|:----------------------:|
| 2to3           | 293 ms   | 298 ms: 1.02x slower   |
| docutils       | 2.11 sec | 2.17 sec: 1.03x slower |
| sphinx         | 843 ms   | 872 ms: 1.03x slower   |
| Geometric mean | (ref)    | 1.02x slower           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-Ex2 | default               |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 428 ms  | 424 ms: 1.01x faster  |
| coroutines                 | 22.1 ms | 21.9 ms: 1.01x faster |
| async_tree_io_tg           | 563 ms  | 559 ms: 1.01x faster  |
| async_tree_cpu_io_mixed    | 434 ms  | 437 ms: 1.01x slower  |
| asyncio_websockets         | 311 ms  | 317 ms: 1.02x slower  |
| async_generators           | 321 ms  | 328 ms: 1.02x slower  |
| Geometric mean             | (ref)   | 1.00x slower          |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-Ex2 | default               |
|----------------|:-------:|:---------------------:|
| nbody          | 98.8 ms | 101 ms: 1.02x slower  |
| float          | 73.5 ms | 75.4 ms: 1.03x slower |
| pidigits       | 148 ms  | 152 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.02x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-Ex2 | default               |
|----------------|:-------:|:---------------------:|
| regex_compile  | 123 ms  | 125 ms: 1.01x slower  |
| regex_effbot   | 1.77 ms | 1.81 ms: 1.02x slower |
| regex_dna      | 118 ms  | 121 ms: 1.03x slower  |
| Geometric mean | (ref)   | 1.02x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-Ex2  | default                |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 271 us   | 274 us: 1.01x slower   |
| tomli_loads          | 1.97 sec | 1.99 sec: 1.01x slower |
| xml_etree_generate   | 87.5 ms  | 89.5 ms: 1.02x slower  |
| xml_etree_process    | 63.0 ms  | 64.6 ms: 1.03x slower  |
| xml_etree_iterparse  | 87.5 ms  | 89.9 ms: 1.03x slower  |
| json_loads           | 21.4 us  | 22.3 us: 1.04x slower  |
| Geometric mean       | (ref)    | 1.02x slower           |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-Ex2 | default               |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 23.4 ms | 23.2 ms: 1.01x faster |
| mako            | 11.4 ms | 11.7 ms: 1.02x slower |
| django_template | 35.8 ms | 36.9 ms: 1.03x slower |
| Geometric mean  | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | TCO-Ex2  | default                |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 50.4 ms  | 20.8 ms: 2.42x faster  |
| many_optionals             | 890 us   | 547 us: 1.63x faster   |
| chaos                      | 67.0 ms  | 65.2 ms: 1.03x faster  |
| scimark_monte_carlo        | 75.2 ms  | 73.9 ms: 1.02x faster  |
| logging_silent             | 121 ns   | 119 ns: 1.02x faster   |
| shortest_path              | 384 ms   | 378 ms: 1.01x faster   |
| bench_mp_pool              | 97.6 ms  | 96.2 ms: 1.01x faster  |
| connected_components       | 351 ms   | 347 ms: 1.01x faster   |
| genshi_text                | 23.4 ms  | 23.2 ms: 1.01x faster  |
| go                         | 138 ms   | 137 ms: 1.01x faster   |
| raytrace                   | 306 ms   | 304 ms: 1.01x faster   |
| async_tree_cpu_io_mixed_tg | 428 ms   | 424 ms: 1.01x faster   |
| coroutines                 | 22.1 ms  | 21.9 ms: 1.01x faster  |
| async_tree_io_tg           | 563 ms   | 559 ms: 1.01x faster   |
| scimark_fft                | 267 ms   | 269 ms: 1.00x slower   |
| async_tree_cpu_io_mixed    | 434 ms   | 437 ms: 1.01x slower   |
| spectral_norm              | 97.1 ms  | 97.7 ms: 1.01x slower  |
| meteor_contest             | 95.0 ms  | 95.9 ms: 1.01x slower  |
| generators                 | 33.5 ms  | 33.8 ms: 1.01x slower  |
| unpickle_pure_python       | 271 us   | 274 us: 1.01x slower   |
| pyflate                    | 457 ms   | 462 ms: 1.01x slower   |
| dulwich_log                | 50.5 ms  | 51.0 ms: 1.01x slower  |
| sqlglot_v2_parse           | 1.34 ms  | 1.36 ms: 1.01x slower  |
| tomli_loads                | 1.97 sec | 1.99 sec: 1.01x slower |
| nqueens                    | 93.2 ms  | 94.3 ms: 1.01x slower  |
| deepcopy                   | 266 us   | 269 us: 1.01x slower   |
| sympy_expand               | 399 ms   | 405 ms: 1.01x slower   |
| scimark_sor                | 133 ms   | 135 ms: 1.01x slower   |
| coverage                   | 61.1 ms  | 61.9 ms: 1.01x slower  |
| sqlglot_v2_transpile       | 1.62 ms  | 1.64 ms: 1.01x slower  |
| crypto_pyaes               | 76.8 ms  | 77.9 ms: 1.01x slower  |
| regex_compile              | 123 ms   | 125 ms: 1.01x slower   |
| telco                      | 6.34 ms  | 6.44 ms: 1.01x slower  |
| sympy_sum                  | 118 ms   | 119 ms: 1.01x slower   |
| sympy_integrate            | 17.5 ms  | 17.8 ms: 1.02x slower  |
| scimark_sparse_mat_mult    | 4.27 ms  | 4.34 ms: 1.02x slower  |
| sympy_str                  | 234 ms   | 238 ms: 1.02x slower   |
| nbody                      | 98.8 ms  | 101 ms: 1.02x slower   |
| 2to3                       | 293 ms   | 298 ms: 1.02x slower   |
| asyncio_websockets         | 311 ms   | 317 ms: 1.02x slower   |
| thrift                     | 680 us   | 694 us: 1.02x slower   |
| async_generators           | 321 ms   | 328 ms: 1.02x slower   |
| xml_etree_generate         | 87.5 ms  | 89.5 ms: 1.02x slower  |
| logging_format             | 9.13 us  | 9.33 us: 1.02x slower  |
| mako                       | 11.4 ms  | 11.7 ms: 1.02x slower  |
| regex_effbot               | 1.77 ms  | 1.81 ms: 1.02x slower  |
| deepcopy_reduce            | 2.71 us  | 2.77 us: 1.02x slower  |
| pycparser                  | 968 ms   | 992 ms: 1.02x slower   |
| xml_etree_process          | 63.0 ms  | 64.6 ms: 1.03x slower  |
| float                      | 73.5 ms  | 75.4 ms: 1.03x slower  |
| pidigits                   | 148 ms   | 152 ms: 1.03x slower   |
| xml_etree_iterparse        | 87.5 ms  | 89.9 ms: 1.03x slower  |
| typing_runtime_protocols   | 146 us   | 150 us: 1.03x slower   |
| sqlglot_v2_normalize       | 103 ms   | 106 ms: 1.03x slower   |
| logging_simple             | 8.63 us  | 8.87 us: 1.03x slower  |
| regex_dna                  | 118 ms   | 121 ms: 1.03x slower   |
| docutils                   | 2.11 sec | 2.17 sec: 1.03x slower |
| sqlglot_v2_optimize        | 49.6 ms  | 51.0 ms: 1.03x slower  |
| django_template            | 35.8 ms  | 36.9 ms: 1.03x slower  |
| sqlite_synth               | 1.78 us  | 1.84 us: 1.03x slower  |
| sphinx                     | 843 ms   | 872 ms: 1.03x slower   |
| json_loads                 | 21.4 us  | 22.3 us: 1.04x slower  |
| fannkuch                   | 386 ms   | 407 ms: 1.06x slower   |
| gc_traversal               | 2.79 ms  | 3.15 ms: 1.13x slower  |
| richards_super             | 58.0 ms  | 65.8 ms: 1.13x slower  |
| richards                   | 51.0 ms  | 57.8 ms: 1.13x slower  |
| pathlib                    | 26.8 ms  | 34.4 ms: 1.28x slower  |
| Geometric mean             | (ref)    | 1.00x slower           |

Benchmark hidden because not significant (27): mdp, bench_thread_pool, deepcopy_memo, async_tree_memoization_tg, comprehensions, pprint_pformat, pprint_safe_repr, bpe_tokeniser, k_core, hexiom, genshi_xml, xml_etree_parse, html5lib, pickle_pure_python, async_tree_memoization, json_dumps, async_tree_io, deltablue, python_startup_no_site, async_tree_none_tg, scimark_lu, python_startup, create_gc_cycles, json, async_tree_none, regex_v8, pylint

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown