# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 215 ms: 1.07x faster   |
| docutils       | 1.77 sec | 1.66 sec: 1.07x faster |
| html5lib       | 38.8 ms  | 37.8 ms: 1.03x faster  |
| sphinx         | 702 ms   | 641 ms: 1.09x faster   |
| Geometric mean | (ref)    | 1.06x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 330 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 330 ms: 1.09x faster  |
| async_generators           | 213 ms  | 201 ms: 1.06x faster  |
| async_tree_none_tg         | 167 ms  | 161 ms: 1.04x faster  |
| coroutines                 | 12.3 ms | 12.0 ms: 1.03x faster |
| async_tree_memoization     | 210 ms  | 205 ms: 1.02x faster  |
| async_tree_none            | 174 ms  | 170 ms: 1.02x faster  |
| async_tree_io_tg           | 385 ms  | 377 ms: 1.02x faster  |
| async_tree_memoization_tg  | 210 ms  | 208 ms: 1.01x faster  |
| Geometric mean             | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (2): async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 42.0 ms: 1.01x slower |
| nbody          | 53.1 ms | 55.6 ms: 1.05x slower |
| Geometric mean | (ref)   | 1.02x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.47 ms: 1.25x faster |
| regex_v8       | 16.3 ms | 14.2 ms: 1.15x faster |
| regex_compile  | 81.9 ms | 79.4 ms: 1.03x faster |
| regex_dna      | 121 ms  | 120 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.11x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.5 us: 1.51x faster  |
| xml_etree_generate   | 64.7 ms  | 53.1 ms: 1.22x faster  |
| json_dumps           | 7.79 ms  | 6.40 ms: 1.22x faster  |
| xml_etree_process    | 44.7 ms  | 36.8 ms: 1.21x faster  |
| unpickle_pure_python | 148 us   | 124 us: 1.19x faster   |
| xml_etree_parse      | 105 ms   | 89.4 ms: 1.17x faster  |
| xml_etree_iterparse  | 70.4 ms  | 61.2 ms: 1.15x faster  |
| pickle_pure_python   | 223 us   | 199 us: 1.12x faster   |
| tomli_loads          | 1.26 sec | 1.17 sec: 1.07x faster |
| Geometric mean       | (ref)    | 1.20x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 24.7 ms: 1.07x faster |
| python_startup_no_site | 19.4 ms | 18.6 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.25 ms: 1.25x faster |
| django_template | 25.2 ms | 23.6 ms: 1.07x faster |
| genshi_text     | 14.5 ms | 14.3 ms: 1.01x faster |
| genshi_xml      | 31.3 ms | 32.3 ms: 1.03x slower |
| Geometric mean  | (ref)   | 1.07x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 14.5 us: 1.51x faster  |
| gc_traversal               | 2.83 ms  | 2.12 ms: 1.34x faster  |
| scimark_lu                 | 64.2 ms  | 50.3 ms: 1.28x faster  |
| mako                       | 7.84 ms  | 6.25 ms: 1.25x faster  |
| regex_effbot               | 1.85 ms  | 1.47 ms: 1.25x faster  |
| json                       | 3.78 ms  | 3.04 ms: 1.24x faster  |
| logging_silent             | 61.1 ns  | 49.7 ns: 1.23x faster  |
| xml_etree_generate         | 64.7 ms  | 53.1 ms: 1.22x faster  |
| json_dumps                 | 7.79 ms  | 6.40 ms: 1.22x faster  |
| xml_etree_process          | 44.7 ms  | 36.8 ms: 1.21x faster  |
| unpickle_pure_python       | 148 us   | 124 us: 1.19x faster   |
| xml_etree_parse            | 105 ms   | 89.4 ms: 1.17x faster  |
| coverage                   | 55.4 ms  | 47.5 ms: 1.16x faster  |
| comprehensions             | 11.3 us  | 9.76 us: 1.16x faster  |
| xml_etree_iterparse        | 70.4 ms  | 61.2 ms: 1.15x faster  |
| regex_v8                   | 16.3 ms  | 14.2 ms: 1.15x faster  |
| telco                      | 5.26 ms  | 4.59 ms: 1.15x faster  |
| deepcopy_memo              | 19.3 us  | 16.8 us: 1.14x faster  |
| scimark_sor                | 68.6 ms  | 60.5 ms: 1.13x faster  |
| deepcopy_reduce            | 1.90 us  | 1.68 us: 1.13x faster  |
| thrift                     | 551 us   | 491 us: 1.12x faster   |
| hexiom                     | 3.92 ms  | 3.49 ms: 1.12x faster  |
| pickle_pure_python         | 223 us   | 199 us: 1.12x faster   |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.21 ms: 1.12x faster  |
| fannkuch                   | 250 ms   | 225 ms: 1.12x faster   |
| many_optionals             | 762 us   | 685 us: 1.11x faster   |
| bpe_tokeniser              | 3.01 sec | 2.72 sec: 1.11x faster |
| async_tree_cpu_io_mixed_tg | 363 ms   | 330 ms: 1.10x faster   |
| scimark_fft                | 169 ms   | 153 ms: 1.10x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 32.9 ms: 1.09x faster  |
| sphinx                     | 702 ms   | 641 ms: 1.09x faster   |
| scimark_monte_carlo        | 38.9 ms  | 35.6 ms: 1.09x faster  |
| crypto_pyaes               | 48.0 ms  | 43.9 ms: 1.09x faster  |
| async_tree_cpu_io_mixed    | 359 ms   | 330 ms: 1.09x faster   |
| pprint_pformat             | 1.04 sec | 956 ms: 1.09x faster   |
| typing_runtime_protocols   | 106 us   | 97.8 us: 1.08x faster  |
| nqueens                    | 59.6 ms  | 55.2 ms: 1.08x faster  |
| deepcopy                   | 180 us   | 167 us: 1.08x faster   |
| pprint_safe_repr           | 510 ms   | 474 ms: 1.08x faster   |
| sympy_expand               | 304 ms   | 283 ms: 1.08x faster   |
| subparsers                 | 44.5 ms  | 41.4 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us  | 1.56 us: 1.07x faster  |
| sympy_sum                  | 91.4 ms  | 85.2 ms: 1.07x faster  |
| tomli_loads                | 1.26 sec | 1.17 sec: 1.07x faster |
| 2to3                       | 231 ms   | 215 ms: 1.07x faster   |
| django_template            | 25.2 ms  | 23.6 ms: 1.07x faster  |
| create_gc_cycles           | 1.34 ms  | 1.25 ms: 1.07x faster  |
| docutils                   | 1.77 sec | 1.66 sec: 1.07x faster |
| python_startup             | 26.4 ms  | 24.7 ms: 1.07x faster  |
| chaos                      | 37.7 ms  | 35.4 ms: 1.07x faster  |
| logging_simple             | 6.25 us  | 5.87 us: 1.06x faster  |
| richards_super             | 35.8 ms  | 33.7 ms: 1.06x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 69.0 ms: 1.06x faster  |
| async_generators           | 213 ms   | 201 ms: 1.06x faster   |
| richards                   | 30.9 ms  | 29.4 ms: 1.05x faster  |
| dulwich_log                | 42.3 ms  | 40.3 ms: 1.05x faster  |
| meteor_contest             | 74.5 ms  | 70.9 ms: 1.05x faster  |
| raytrace                   | 169 ms   | 162 ms: 1.05x faster   |
| sympy_integrate            | 13.4 ms  | 12.8 ms: 1.05x faster  |
| logging_format             | 6.70 us  | 6.42 us: 1.04x faster  |
| python_startup_no_site     | 19.4 ms  | 18.6 ms: 1.04x faster  |
| async_tree_none_tg         | 167 ms   | 161 ms: 1.04x faster   |
| pathlib                    | 25.1 ms  | 24.2 ms: 1.04x faster  |
| pyflate                    | 274 ms   | 264 ms: 1.03x faster   |
| pycparser                  | 713 ms   | 689 ms: 1.03x faster   |
| spectral_norm              | 51.1 ms  | 49.4 ms: 1.03x faster  |
| regex_compile              | 81.9 ms  | 79.4 ms: 1.03x faster  |
| coroutines                 | 12.3 ms  | 12.0 ms: 1.03x faster  |
| html5lib                   | 38.8 ms  | 37.8 ms: 1.03x faster  |
| sympy_str                  | 177 ms   | 173 ms: 1.02x faster   |
| async_tree_memoization     | 210 ms   | 205 ms: 1.02x faster   |
| async_tree_none            | 174 ms   | 170 ms: 1.02x faster   |
| async_tree_io_tg           | 385 ms   | 377 ms: 1.02x faster   |
| sqlglot_v2_parse           | 798 us   | 781 us: 1.02x faster   |
| sqlglot_v2_transpile       | 1.01 ms  | 993 us: 1.02x faster   |
| deltablue                  | 1.91 ms  | 1.88 ms: 1.01x faster  |
| async_tree_memoization_tg  | 210 ms   | 208 ms: 1.01x faster   |
| mdp                        | 1.44 sec | 1.43 sec: 1.01x faster |
| genshi_text                | 14.5 ms  | 14.3 ms: 1.01x faster  |
| regex_dna                  | 121 ms   | 120 ms: 1.01x faster   |
| generators                 | 16.3 ms  | 16.5 ms: 1.01x slower  |
| float                      | 41.4 ms  | 42.0 ms: 1.01x slower  |
| shortest_path              | 347 ms   | 352 ms: 1.01x slower   |
| genshi_xml                 | 31.3 ms  | 32.3 ms: 1.03x slower  |
| connected_components       | 311 ms   | 325 ms: 1.04x slower   |
| nbody                      | 53.1 ms  | 55.6 ms: 1.05x slower  |
| Geometric mean             | (ref)    | 1.08x faster           |

Benchmark hidden because not significant (6): pylint, async_tree_io, pidigits, k_core, go, asyncio_websockets
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown