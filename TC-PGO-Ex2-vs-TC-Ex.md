# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 216 ms: 1.07x faster   |
| docutils       | 1.77 sec | 1.63 sec: 1.09x faster |
| html5lib       | 38.8 ms  | 36.1 ms: 1.07x faster  |
| sphinx         | 702 ms   | 638 ms: 1.10x faster   |
| Geometric mean | (ref)    | 1.08x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 328 ms: 1.11x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 329 ms: 1.09x faster  |
| async_tree_none_tg         | 167 ms  | 159 ms: 1.05x faster  |
| async_tree_io_tg           | 385 ms  | 371 ms: 1.04x faster  |
| async_generators           | 213 ms  | 206 ms: 1.04x faster  |
| async_tree_memoization     | 210 ms  | 205 ms: 1.02x faster  |
| async_tree_io              | 384 ms  | 375 ms: 1.02x faster  |
| async_tree_none            | 174 ms  | 170 ms: 1.02x faster  |
| coroutines                 | 12.3 ms | 12.4 ms: 1.01x slower |
| asyncio_websockets         | 312 ms  | 317 ms: 1.02x slower  |
| Geometric mean             | (ref)   | 1.03x faster          |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 40.2 ms: 1.03x faster |
| Geometric mean | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.40 ms: 1.32x faster |
| regex_v8       | 16.3 ms | 14.1 ms: 1.16x faster |
| regex_compile  | 81.9 ms | 74.8 ms: 1.10x faster |
| regex_dna      | 121 ms  | 115 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.15x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.5 us: 1.52x faster  |
| xml_etree_generate   | 64.7 ms  | 51.5 ms: 1.26x faster  |
| xml_etree_process    | 44.7 ms  | 36.7 ms: 1.22x faster  |
| unpickle_pure_python | 148 us   | 123 us: 1.21x faster   |
| json_dumps           | 7.79 ms  | 6.48 ms: 1.20x faster  |
| xml_etree_parse      | 105 ms   | 89.0 ms: 1.17x faster  |
| xml_etree_iterparse  | 70.4 ms  | 60.4 ms: 1.17x faster  |
| pickle_pure_python   | 223 us   | 201 us: 1.10x faster   |
| tomli_loads          | 1.26 sec | 1.17 sec: 1.07x faster |
| Geometric mean       | (ref)    | 1.21x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TC-Ex   | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| python_startup | 26.4 ms | 26.0 ms: 1.02x faster |
| Geometric mean | (ref)   | 1.00x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.12 ms: 1.28x faster |
| django_template | 25.2 ms | 23.4 ms: 1.08x faster |
| genshi_xml      | 31.3 ms | 30.7 ms: 1.02x faster |
| genshi_text     | 14.5 ms | 14.2 ms: 1.02x faster |
| Geometric mean  | (ref)   | 1.09x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 14.5 us: 1.52x faster  |
| gc_traversal               | 2.83 ms  | 2.07 ms: 1.36x faster  |
| regex_effbot               | 1.85 ms  | 1.40 ms: 1.32x faster  |
| mako                       | 7.84 ms  | 6.12 ms: 1.28x faster  |
| json                       | 3.78 ms  | 2.98 ms: 1.27x faster  |
| xml_etree_generate         | 64.7 ms  | 51.5 ms: 1.26x faster  |
| xml_etree_process          | 44.7 ms  | 36.7 ms: 1.22x faster  |
| unpickle_pure_python       | 148 us   | 123 us: 1.21x faster   |
| json_dumps                 | 7.79 ms  | 6.48 ms: 1.20x faster  |
| scimark_lu                 | 64.2 ms  | 54.4 ms: 1.18x faster  |
| xml_etree_parse            | 105 ms   | 89.0 ms: 1.17x faster  |
| xml_etree_iterparse        | 70.4 ms  | 60.4 ms: 1.17x faster  |
| comprehensions             | 11.3 us  | 9.73 us: 1.16x faster  |
| telco                      | 5.26 ms  | 4.54 ms: 1.16x faster  |
| regex_v8                   | 16.3 ms  | 14.1 ms: 1.16x faster  |
| crypto_pyaes               | 48.0 ms  | 41.6 ms: 1.15x faster  |
| logging_silent             | 61.1 ns  | 53.3 ns: 1.15x faster  |
| thrift                     | 551 us   | 482 us: 1.14x faster   |
| deepcopy_reduce            | 1.90 us  | 1.66 us: 1.14x faster  |
| sympy_expand               | 304 ms   | 269 ms: 1.13x faster   |
| deepcopy_memo              | 19.3 us  | 17.0 us: 1.13x faster  |
| deepcopy                   | 180 us   | 160 us: 1.13x faster   |
| hexiom                     | 3.92 ms  | 3.47 ms: 1.13x faster  |
| sympy_str                  | 177 ms   | 158 ms: 1.12x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 32.2 ms: 1.12x faster  |
| coverage                   | 55.4 ms  | 49.5 ms: 1.12x faster  |
| richards_super             | 35.8 ms  | 32.2 ms: 1.11x faster  |
| sympy_sum                  | 91.4 ms  | 82.1 ms: 1.11x faster  |
| bpe_tokeniser              | 3.01 sec | 2.71 sec: 1.11x faster |
| richards                   | 30.9 ms  | 27.8 ms: 1.11x faster  |
| scimark_fft                | 169 ms   | 152 ms: 1.11x faster   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 328 ms: 1.11x faster   |
| pickle_pure_python         | 223 us   | 201 us: 1.10x faster   |
| nqueens                    | 59.6 ms  | 54.0 ms: 1.10x faster  |
| sphinx                     | 702 ms   | 638 ms: 1.10x faster   |
| generators                 | 16.3 ms  | 14.8 ms: 1.10x faster  |
| sympy_integrate            | 13.4 ms  | 12.2 ms: 1.10x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 66.9 ms: 1.10x faster  |
| regex_compile              | 81.9 ms  | 74.8 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 359 ms   | 329 ms: 1.09x faster   |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.26 ms: 1.09x faster  |
| docutils                   | 1.77 sec | 1.63 sec: 1.09x faster |
| sqlglot_v2_transpile       | 1.01 ms  | 933 us: 1.09x faster   |
| logging_simple             | 6.25 us  | 5.78 us: 1.08x faster  |
| sqlglot_v2_parse           | 798 us   | 740 us: 1.08x faster   |
| django_template            | 25.2 ms  | 23.4 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us  | 1.56 us: 1.08x faster  |
| html5lib                   | 38.8 ms  | 36.1 ms: 1.07x faster  |
| tomli_loads                | 1.26 sec | 1.17 sec: 1.07x faster |
| dulwich_log                | 42.3 ms  | 39.5 ms: 1.07x faster  |
| pycparser                  | 713 ms   | 664 ms: 1.07x faster   |
| typing_runtime_protocols   | 106 us   | 98.9 us: 1.07x faster  |
| meteor_contest             | 74.5 ms  | 69.5 ms: 1.07x faster  |
| pprint_pformat             | 1.04 sec | 968 ms: 1.07x faster   |
| pprint_safe_repr           | 510 ms   | 478 ms: 1.07x faster   |
| 2to3                       | 231 ms   | 216 ms: 1.07x faster   |
| fannkuch                   | 250 ms   | 236 ms: 1.06x faster   |
| logging_format             | 6.70 us  | 6.34 us: 1.06x faster  |
| create_gc_cycles           | 1.34 ms  | 1.27 ms: 1.06x faster  |
| pyflate                    | 274 ms   | 260 ms: 1.05x faster   |
| scimark_monte_carlo        | 38.9 ms  | 37.0 ms: 1.05x faster  |
| chaos                      | 37.7 ms  | 35.9 ms: 1.05x faster  |
| bench_mp_pool              | 93.6 ms  | 89.1 ms: 1.05x faster  |
| async_tree_none_tg         | 167 ms   | 159 ms: 1.05x faster   |
| regex_dna                  | 121 ms   | 115 ms: 1.05x faster   |
| async_tree_io_tg           | 385 ms   | 371 ms: 1.04x faster   |
| async_generators           | 213 ms   | 206 ms: 1.04x faster   |
| mdp                        | 1.44 sec | 1.40 sec: 1.03x faster |
| deltablue                  | 1.91 ms  | 1.85 ms: 1.03x faster  |
| float                      | 41.4 ms  | 40.2 ms: 1.03x faster  |
| pylint                     | 205 ms   | 199 ms: 1.03x faster   |
| pathlib                    | 25.1 ms  | 24.3 ms: 1.03x faster  |
| go                         | 70.4 ms  | 68.4 ms: 1.03x faster  |
| bench_thread_pool          | 876 us   | 851 us: 1.03x faster   |
| async_tree_memoization     | 210 ms   | 205 ms: 1.02x faster   |
| async_tree_io              | 384 ms   | 375 ms: 1.02x faster   |
| async_tree_none            | 174 ms   | 170 ms: 1.02x faster   |
| genshi_xml                 | 31.3 ms  | 30.7 ms: 1.02x faster  |
| raytrace                   | 169 ms   | 166 ms: 1.02x faster   |
| genshi_text                | 14.5 ms  | 14.2 ms: 1.02x faster  |
| scimark_sor                | 68.6 ms  | 67.5 ms: 1.02x faster  |
| python_startup             | 26.4 ms  | 26.0 ms: 1.02x faster  |
| coroutines                 | 12.3 ms  | 12.4 ms: 1.01x slower  |
| asyncio_websockets         | 312 ms   | 317 ms: 1.02x slower   |
| connected_components       | 311 ms   | 321 ms: 1.03x slower   |
| Geometric mean             | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (9): async_tree_memoization_tg, many_optionals, k_core, spectral_norm, pidigits, shortest_path, nbody, python_startup_no_site, subparsers

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown