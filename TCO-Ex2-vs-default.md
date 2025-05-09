# Results vs. base

- fork: unknown
- ref: TCO-Ex2
- machine: unknown-unknown
- commit hash: f963239ff1
- commit date: 2025-02-25
- overall geometric mean: 1.001x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | default  | TCO-Ex2                |
|----------------|:--------:|:----------------------:|
| 2to3           | 298 ms   | 293 ms: 1.02x faster   |
| docutils       | 2.17 sec | 2.11 sec: 1.03x faster |
| sphinx         | 872 ms   | 843 ms: 1.03x faster   |
| Geometric mean | (ref)    | 1.02x faster           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | default | TCO-Ex2               |
|----------------------------|:-------:|:---------------------:|
| async_generators           | 328 ms  | 321 ms: 1.02x faster  |
| asyncio_websockets         | 317 ms  | 311 ms: 1.02x faster  |
| async_tree_cpu_io_mixed    | 437 ms  | 434 ms: 1.01x faster  |
| async_tree_io_tg           | 559 ms  | 563 ms: 1.01x slower  |
| coroutines                 | 21.9 ms | 22.1 ms: 1.01x slower |
| async_tree_cpu_io_mixed_tg | 424 ms  | 428 ms: 1.01x slower  |
| Geometric mean             | (ref)   | 1.00x faster          |

Benchmark hidden because not significant (5): async_tree_none, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | default | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| pidigits       | 152 ms  | 148 ms: 1.03x faster  |
| float          | 75.4 ms | 73.5 ms: 1.03x faster |
| nbody          | 101 ms  | 98.8 ms: 1.02x faster |
| Geometric mean | (ref)   | 1.02x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | default | TCO-Ex2               |
|----------------|:-------:|:---------------------:|
| regex_dna      | 121 ms  | 118 ms: 1.03x faster  |
| regex_effbot   | 1.81 ms | 1.77 ms: 1.02x faster |
| regex_compile  | 125 ms  | 123 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.02x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | default  | TCO-Ex2                |
|----------------------|:--------:|:----------------------:|
| json_loads           | 22.3 us  | 21.4 us: 1.04x faster  |
| xml_etree_iterparse  | 89.9 ms  | 87.5 ms: 1.03x faster  |
| xml_etree_process    | 64.6 ms  | 63.0 ms: 1.03x faster  |
| xml_etree_generate   | 89.5 ms  | 87.5 ms: 1.02x faster  |
| tomli_loads          | 1.99 sec | 1.97 sec: 1.01x faster |
| unpickle_pure_python | 274 us   | 271 us: 1.01x faster   |
| Geometric mean       | (ref)    | 1.02x faster           |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | default | TCO-Ex2               |
|-----------------|:-------:|:---------------------:|
| django_template | 36.9 ms | 35.8 ms: 1.03x faster |
| mako            | 11.7 ms | 11.4 ms: 1.02x faster |
| genshi_text     | 23.2 ms | 23.4 ms: 1.01x slower |
| Geometric mean  | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | default  | TCO-Ex2                |
|----------------------------|:--------:|:----------------------:|
| pathlib                    | 34.4 ms  | 26.8 ms: 1.28x faster  |
| richards                   | 57.8 ms  | 51.0 ms: 1.13x faster  |
| richards_super             | 65.8 ms  | 58.0 ms: 1.13x faster  |
| gc_traversal               | 3.15 ms  | 2.79 ms: 1.13x faster  |
| fannkuch                   | 407 ms   | 386 ms: 1.06x faster   |
| json_loads                 | 22.3 us  | 21.4 us: 1.04x faster  |
| sphinx                     | 872 ms   | 843 ms: 1.03x faster   |
| sqlite_synth               | 1.84 us  | 1.78 us: 1.03x faster  |
| django_template            | 36.9 ms  | 35.8 ms: 1.03x faster  |
| sqlglot_v2_optimize        | 51.0 ms  | 49.6 ms: 1.03x faster  |
| docutils                   | 2.17 sec | 2.11 sec: 1.03x faster |
| regex_dna                  | 121 ms   | 118 ms: 1.03x faster   |
| logging_simple             | 8.87 us  | 8.63 us: 1.03x faster  |
| sqlglot_v2_normalize       | 106 ms   | 103 ms: 1.03x faster   |
| typing_runtime_protocols   | 150 us   | 146 us: 1.03x faster   |
| xml_etree_iterparse        | 89.9 ms  | 87.5 ms: 1.03x faster  |
| pidigits                   | 152 ms   | 148 ms: 1.03x faster   |
| float                      | 75.4 ms  | 73.5 ms: 1.03x faster  |
| xml_etree_process          | 64.6 ms  | 63.0 ms: 1.03x faster  |
| pycparser                  | 992 ms   | 968 ms: 1.02x faster   |
| deepcopy_reduce            | 2.77 us  | 2.71 us: 1.02x faster  |
| regex_effbot               | 1.81 ms  | 1.77 ms: 1.02x faster  |
| mako                       | 11.7 ms  | 11.4 ms: 1.02x faster  |
| logging_format             | 9.33 us  | 9.13 us: 1.02x faster  |
| xml_etree_generate         | 89.5 ms  | 87.5 ms: 1.02x faster  |
| async_generators           | 328 ms   | 321 ms: 1.02x faster   |
| thrift                     | 694 us   | 680 us: 1.02x faster   |
| asyncio_websockets         | 317 ms   | 311 ms: 1.02x faster   |
| 2to3                       | 298 ms   | 293 ms: 1.02x faster   |
| nbody                      | 101 ms   | 98.8 ms: 1.02x faster  |
| sympy_str                  | 238 ms   | 234 ms: 1.02x faster   |
| scimark_sparse_mat_mult    | 4.34 ms  | 4.27 ms: 1.02x faster  |
| sympy_integrate            | 17.8 ms  | 17.5 ms: 1.02x faster  |
| sympy_sum                  | 119 ms   | 118 ms: 1.01x faster   |
| telco                      | 6.44 ms  | 6.34 ms: 1.01x faster  |
| regex_compile              | 125 ms   | 123 ms: 1.01x faster   |
| crypto_pyaes               | 77.9 ms  | 76.8 ms: 1.01x faster  |
| sqlglot_v2_transpile       | 1.64 ms  | 1.62 ms: 1.01x faster  |
| coverage                   | 61.9 ms  | 61.1 ms: 1.01x faster  |
| scimark_sor                | 135 ms   | 133 ms: 1.01x faster   |
| sympy_expand               | 405 ms   | 399 ms: 1.01x faster   |
| deepcopy                   | 269 us   | 266 us: 1.01x faster   |
| nqueens                    | 94.3 ms  | 93.2 ms: 1.01x faster  |
| tomli_loads                | 1.99 sec | 1.97 sec: 1.01x faster |
| sqlglot_v2_parse           | 1.36 ms  | 1.34 ms: 1.01x faster  |
| dulwich_log                | 51.0 ms  | 50.5 ms: 1.01x faster  |
| pyflate                    | 462 ms   | 457 ms: 1.01x faster   |
| unpickle_pure_python       | 274 us   | 271 us: 1.01x faster   |
| generators                 | 33.8 ms  | 33.5 ms: 1.01x faster  |
| meteor_contest             | 95.9 ms  | 95.0 ms: 1.01x faster  |
| spectral_norm              | 97.7 ms  | 97.1 ms: 1.01x faster  |
| async_tree_cpu_io_mixed    | 437 ms   | 434 ms: 1.01x faster   |
| scimark_fft                | 269 ms   | 267 ms: 1.00x faster   |
| async_tree_io_tg           | 559 ms   | 563 ms: 1.01x slower   |
| coroutines                 | 21.9 ms  | 22.1 ms: 1.01x slower  |
| async_tree_cpu_io_mixed_tg | 424 ms   | 428 ms: 1.01x slower   |
| raytrace                   | 304 ms   | 306 ms: 1.01x slower   |
| go                         | 137 ms   | 138 ms: 1.01x slower   |
| genshi_text                | 23.2 ms  | 23.4 ms: 1.01x slower  |
| connected_components       | 347 ms   | 351 ms: 1.01x slower   |
| bench_mp_pool              | 96.2 ms  | 97.6 ms: 1.01x slower  |
| shortest_path              | 378 ms   | 384 ms: 1.01x slower   |
| logging_silent             | 119 ns   | 121 ns: 1.02x slower   |
| scimark_monte_carlo        | 73.9 ms  | 75.2 ms: 1.02x slower  |
| chaos                      | 65.2 ms  | 67.0 ms: 1.03x slower  |
| many_optionals             | 547 us   | 890 us: 1.63x slower   |
| subparsers                 | 20.8 ms  | 50.4 ms: 2.42x slower  |
| Geometric mean             | (ref)    | 1.00x faster           |

Benchmark hidden because not significant (27): pylint, regex_v8, async_tree_none, json, create_gc_cycles, python_startup, scimark_lu, async_tree_none_tg, python_startup_no_site, deltablue, async_tree_io, json_dumps, async_tree_memoization, pickle_pure_python, html5lib, xml_etree_parse, genshi_xml, hexiom, k_core, bpe_tokeniser, pprint_safe_repr, pprint_pformat, comprehensions, async_tree_memoization_tg, deepcopy_memo, bench_thread_pool, mdp

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown