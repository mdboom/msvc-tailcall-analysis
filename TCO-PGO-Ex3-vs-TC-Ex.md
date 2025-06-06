# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 212 ms: 1.09x faster   |
| docutils       | 1.77 sec | 1.67 sec: 1.06x faster |
| html5lib       | 38.8 ms  | 37.9 ms: 1.02x faster  |
| sphinx         | 702 ms   | 645 ms: 1.09x faster   |
| Geometric mean | (ref)    | 1.06x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 329 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 330 ms: 1.09x faster  |
| async_generators           | 213 ms  | 202 ms: 1.05x faster  |
| async_tree_none_tg         | 167 ms  | 159 ms: 1.05x faster  |
| asyncio_websockets         | 312 ms  | 301 ms: 1.04x faster  |
| coroutines                 | 12.3 ms | 11.9 ms: 1.03x faster |
| async_tree_io_tg           | 385 ms  | 377 ms: 1.02x faster  |
| async_tree_none            | 174 ms  | 170 ms: 1.02x faster  |
| async_tree_memoization     | 210 ms  | 206 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 41.9 ms: 1.01x slower |
| nbody          | 53.1 ms | 55.2 ms: 1.04x slower |
| Geometric mean | (ref)   | 1.02x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.46 ms: 1.26x faster |
| regex_v8       | 16.3 ms | 13.2 ms: 1.23x faster |
| regex_compile  | 81.9 ms | 78.1 ms: 1.05x faster |
| Geometric mean | (ref)   | 1.13x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.7 us: 1.49x faster  |
| xml_etree_process    | 44.7 ms  | 37.0 ms: 1.21x faster  |
| xml_etree_generate   | 64.7 ms  | 53.6 ms: 1.21x faster  |
| json_dumps           | 7.79 ms  | 6.55 ms: 1.19x faster  |
| xml_etree_parse      | 105 ms   | 89.3 ms: 1.17x faster  |
| unpickle_pure_python | 148 us   | 127 us: 1.16x faster   |
| xml_etree_iterparse  | 70.4 ms  | 61.2 ms: 1.15x faster  |
| pickle_pure_python   | 223 us   | 199 us: 1.12x faster   |
| tomli_loads          | 1.26 sec | 1.18 sec: 1.07x faster |
| Geometric mean       | (ref)    | 1.19x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 24.7 ms: 1.07x faster |
| python_startup_no_site | 19.4 ms | 18.7 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.28 ms: 1.25x faster |
| django_template | 25.2 ms | 22.9 ms: 1.10x faster |
| genshi_text     | 14.5 ms | 14.3 ms: 1.01x faster |
| genshi_xml      | 31.3 ms | 32.8 ms: 1.05x slower |
| Geometric mean  | (ref)   | 1.07x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 14.7 us: 1.49x faster  |
| gc_traversal               | 2.83 ms  | 2.11 ms: 1.34x faster  |
| json                       | 3.78 ms  | 2.97 ms: 1.27x faster  |
| regex_effbot               | 1.85 ms  | 1.46 ms: 1.26x faster  |
| scimark_lu                 | 64.2 ms  | 50.9 ms: 1.26x faster  |
| mako                       | 7.84 ms  | 6.28 ms: 1.25x faster  |
| logging_silent             | 61.1 ns  | 49.4 ns: 1.24x faster  |
| regex_v8                   | 16.3 ms  | 13.2 ms: 1.23x faster  |
| xml_etree_process          | 44.7 ms  | 37.0 ms: 1.21x faster  |
| xml_etree_generate         | 64.7 ms  | 53.6 ms: 1.21x faster  |
| json_dumps                 | 7.79 ms  | 6.55 ms: 1.19x faster  |
| xml_etree_parse            | 105 ms   | 89.3 ms: 1.17x faster  |
| unpickle_pure_python       | 148 us   | 127 us: 1.16x faster   |
| deepcopy_memo              | 19.3 us  | 16.6 us: 1.16x faster  |
| telco                      | 5.26 ms  | 4.57 ms: 1.15x faster  |
| xml_etree_iterparse        | 70.4 ms  | 61.2 ms: 1.15x faster  |
| coverage                   | 55.4 ms  | 48.2 ms: 1.15x faster  |
| many_optionals             | 762 us   | 665 us: 1.14x faster   |
| comprehensions             | 11.3 us  | 9.87 us: 1.14x faster  |
| thrift                     | 551 us   | 482 us: 1.14x faster   |
| fannkuch                   | 250 ms   | 223 ms: 1.12x faster   |
| scimark_sor                | 68.6 ms  | 61.1 ms: 1.12x faster  |
| pickle_pure_python         | 223 us   | 199 us: 1.12x faster   |
| deepcopy_reduce            | 1.90 us  | 1.70 us: 1.12x faster  |
| hexiom                     | 3.92 ms  | 3.54 ms: 1.11x faster  |
| bpe_tokeniser              | 3.01 sec | 2.72 sec: 1.11x faster |
| django_template            | 25.2 ms  | 22.9 ms: 1.10x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms   | 329 ms: 1.10x faster   |
| nqueens                    | 59.6 ms  | 54.4 ms: 1.10x faster  |
| scimark_fft                | 169 ms   | 154 ms: 1.09x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 33.0 ms: 1.09x faster  |
| subparsers                 | 44.5 ms  | 40.7 ms: 1.09x faster  |
| 2to3                       | 231 ms   | 212 ms: 1.09x faster   |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.27 ms: 1.09x faster  |
| async_tree_cpu_io_mixed    | 359 ms   | 330 ms: 1.09x faster   |
| sphinx                     | 702 ms   | 645 ms: 1.09x faster   |
| pprint_safe_repr           | 510 ms   | 470 ms: 1.09x faster   |
| scimark_monte_carlo        | 38.9 ms  | 36.0 ms: 1.08x faster  |
| richards_super             | 35.8 ms  | 33.1 ms: 1.08x faster  |
| deepcopy                   | 180 us   | 167 us: 1.08x faster   |
| sympy_expand               | 304 ms   | 282 ms: 1.08x faster   |
| sympy_str                  | 177 ms   | 164 ms: 1.08x faster   |
| richards                   | 30.9 ms  | 28.7 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us  | 1.56 us: 1.07x faster  |
| typing_runtime_protocols   | 106 us   | 98.8 us: 1.07x faster  |
| pprint_pformat             | 1.04 sec | 967 ms: 1.07x faster   |
| tomli_loads                | 1.26 sec | 1.18 sec: 1.07x faster |
| python_startup             | 26.4 ms  | 24.7 ms: 1.07x faster  |
| docutils                   | 1.77 sec | 1.67 sec: 1.06x faster |
| meteor_contest             | 74.5 ms  | 70.2 ms: 1.06x faster  |
| sympy_sum                  | 91.4 ms  | 86.3 ms: 1.06x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 69.3 ms: 1.06x faster  |
| raytrace                   | 169 ms   | 160 ms: 1.06x faster   |
| async_generators           | 213 ms   | 202 ms: 1.05x faster   |
| dulwich_log                | 42.3 ms  | 40.2 ms: 1.05x faster  |
| create_gc_cycles           | 1.34 ms  | 1.27 ms: 1.05x faster  |
| async_tree_none_tg         | 167 ms   | 159 ms: 1.05x faster   |
| regex_compile              | 81.9 ms  | 78.1 ms: 1.05x faster  |
| logging_simple             | 6.25 us  | 5.97 us: 1.05x faster  |
| sqlglot_v2_transpile       | 1.01 ms  | 970 us: 1.05x faster   |
| sympy_integrate            | 13.4 ms  | 12.8 ms: 1.04x faster  |
| pathlib                    | 25.1 ms  | 24.1 ms: 1.04x faster  |
| sqlglot_v2_parse           | 798 us   | 766 us: 1.04x faster   |
| pycparser                  | 713 ms   | 686 ms: 1.04x faster   |
| asyncio_websockets         | 312 ms   | 301 ms: 1.04x faster   |
| python_startup_no_site     | 19.4 ms  | 18.7 ms: 1.04x faster  |
| spectral_norm              | 51.1 ms  | 49.4 ms: 1.03x faster  |
| pylint                     | 205 ms   | 198 ms: 1.03x faster   |
| logging_format             | 6.70 us  | 6.50 us: 1.03x faster  |
| coroutines                 | 12.3 ms  | 11.9 ms: 1.03x faster  |
| chaos                      | 37.7 ms  | 36.9 ms: 1.02x faster  |
| async_tree_io_tg           | 385 ms   | 377 ms: 1.02x faster   |
| html5lib                   | 38.8 ms  | 37.9 ms: 1.02x faster  |
| async_tree_none            | 174 ms   | 170 ms: 1.02x faster   |
| async_tree_memoization     | 210 ms   | 206 ms: 1.02x faster   |
| pyflate                    | 274 ms   | 268 ms: 1.02x faster   |
| deltablue                  | 1.91 ms  | 1.88 ms: 1.02x faster  |
| genshi_text                | 14.5 ms  | 14.3 ms: 1.01x faster  |
| crypto_pyaes               | 48.0 ms  | 47.4 ms: 1.01x faster  |
| float                      | 41.4 ms  | 41.9 ms: 1.01x slower  |
| generators                 | 16.3 ms  | 16.5 ms: 1.01x slower  |
| shortest_path              | 347 ms   | 353 ms: 1.02x slower   |
| nbody                      | 53.1 ms  | 55.2 ms: 1.04x slower  |
| connected_components       | 311 ms   | 326 ms: 1.05x slower   |
| genshi_xml                 | 31.3 ms  | 32.8 ms: 1.05x slower  |
| mdp                        | 1.44 sec | 1.62 sec: 1.12x slower |
| Geometric mean             | (ref)    | 1.08x faster           |

Benchmark hidden because not significant (6): async_tree_memoization_tg, pidigits, regex_dna, async_tree_io, k_core, go
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown