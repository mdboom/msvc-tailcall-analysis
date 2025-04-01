# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.169x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang    | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 207 ms   | 231 ms: 1.12x slower   |
| docutils       | 1.56 sec | 1.77 sec: 1.14x slower |
| html5lib       | 34.9 ms  | 38.8 ms: 1.11x slower  |
| sphinx         | 603 ms   | 702 ms: 1.16x slower   |
| Geometric mean | (ref)    | 1.13x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang   | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| async_tree_memoization_tg  | 197 ms  | 210 ms: 1.07x slower  |
| async_tree_io              | 353 ms  | 384 ms: 1.09x slower  |
| async_tree_none            | 159 ms  | 174 ms: 1.09x slower  |
| async_tree_io_tg           | 351 ms  | 385 ms: 1.10x slower  |
| async_tree_none_tg         | 150 ms  | 167 ms: 1.11x slower  |
| async_tree_memoization     | 187 ms  | 210 ms: 1.12x slower  |
| async_generators           | 187 ms  | 213 ms: 1.14x slower  |
| coroutines                 | 10.7 ms | 12.3 ms: 1.14x slower |
| async_tree_cpu_io_mixed    | 313 ms  | 359 ms: 1.15x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms  | 363 ms: 1.15x slower  |
| asyncio_websockets         | 159 ms  | 312 ms: 1.96x slower  |
| Geometric mean             | (ref)   | 1.17x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang   | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 49.1 ms | 53.1 ms: 1.08x slower |
| float          | 36.9 ms | 41.4 ms: 1.12x slower |
| Geometric mean | (ref)   | 1.07x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | clang   | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_dna      | 117 ms  | 121 ms: 1.03x slower  |
| regex_compile  | 69.8 ms | 81.9 ms: 1.17x slower |
| regex_effbot   | 1.54 ms | 1.85 ms: 1.20x slower |
| regex_v8       | 13.0 ms | 16.3 ms: 1.26x slower |
| Geometric mean | (ref)   | 1.16x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang    | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| xml_etree_iterparse  | 61.5 ms  | 70.4 ms: 1.14x slower  |
| tomli_loads          | 1.09 sec | 1.26 sec: 1.16x slower |
| xml_etree_parse      | 89.4 ms  | 105 ms: 1.17x slower   |
| pickle_pure_python   | 173 us   | 223 us: 1.29x slower   |
| xml_etree_process    | 34.0 ms  | 44.7 ms: 1.32x slower  |
| xml_etree_generate   | 49.1 ms  | 64.7 ms: 1.32x slower  |
| json_dumps           | 5.66 ms  | 7.79 ms: 1.38x slower  |
| unpickle_pure_python | 107 us   | 148 us: 1.38x slower   |
| json_loads           | 14.1 us  | 21.9 us: 1.56x slower  |
| Geometric mean       | (ref)    | 1.29x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang   | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.9 ms | 19.4 ms: 1.08x faster |
| Geometric mean         | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | clang   | TC-Ex                 |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 29.0 ms | 31.3 ms: 1.08x slower |
| django_template | 21.3 ms | 25.2 ms: 1.18x slower |
| genshi_text     | 11.9 ms | 14.5 ms: 1.21x slower |
| mako            | 5.83 ms | 7.84 ms: 1.35x slower |
| Geometric mean  | (ref)   | 1.20x slower          |

All benchmarks:
===============

| Benchmark                  | clang    | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| pathlib                    | 30.7 ms  | 25.1 ms: 1.22x faster  |
| python_startup_no_site     | 20.9 ms  | 19.4 ms: 1.08x faster  |
| connected_components       | 329 ms   | 311 ms: 1.06x faster   |
| create_gc_cycles           | 1.36 ms  | 1.34 ms: 1.02x faster  |
| shortest_path              | 351 ms   | 347 ms: 1.01x faster   |
| gc_traversal               | 2.76 ms  | 2.83 ms: 1.03x slower  |
| regex_dna                  | 117 ms   | 121 ms: 1.03x slower   |
| k_core                     | 1.66 sec | 1.71 sec: 1.03x slower |
| bench_mp_pool              | 88.6 ms  | 93.6 ms: 1.06x slower  |
| bench_thread_pool          | 823 us   | 876 us: 1.06x slower   |
| async_tree_memoization_tg  | 197 ms   | 210 ms: 1.07x slower   |
| genshi_xml                 | 29.0 ms  | 31.3 ms: 1.08x slower  |
| nbody                      | 49.1 ms  | 53.1 ms: 1.08x slower  |
| async_tree_io              | 353 ms   | 384 ms: 1.09x slower   |
| pylint                     | 188 ms   | 205 ms: 1.09x slower   |
| async_tree_none            | 159 ms   | 174 ms: 1.09x slower   |
| async_tree_io_tg           | 351 ms   | 385 ms: 1.10x slower   |
| pycparser                  | 647 ms   | 713 ms: 1.10x slower   |
| generators                 | 14.8 ms  | 16.3 ms: 1.10x slower  |
| html5lib                   | 34.9 ms  | 38.8 ms: 1.11x slower  |
| sqlite_synth               | 1.51 us  | 1.68 us: 1.11x slower  |
| async_tree_none_tg         | 150 ms   | 167 ms: 1.11x slower   |
| dulwich_log                | 38.0 ms  | 42.3 ms: 1.11x slower  |
| meteor_contest             | 66.8 ms  | 74.5 ms: 1.12x slower  |
| 2to3                       | 207 ms   | 231 ms: 1.12x slower   |
| async_tree_memoization     | 187 ms   | 210 ms: 1.12x slower   |
| float                      | 36.9 ms  | 41.4 ms: 1.12x slower  |
| logging_format             | 5.96 us  | 6.70 us: 1.13x slower  |
| logging_simple             | 5.55 us  | 6.25 us: 1.13x slower  |
| docutils                   | 1.56 sec | 1.77 sec: 1.14x slower |
| async_generators           | 187 ms   | 213 ms: 1.14x slower   |
| sqlglot_v2_normalize       | 64.2 ms  | 73.3 ms: 1.14x slower  |
| coroutines                 | 10.7 ms  | 12.3 ms: 1.14x slower  |
| xml_etree_iterparse        | 61.5 ms  | 70.4 ms: 1.14x slower  |
| go                         | 61.5 ms  | 70.4 ms: 1.14x slower  |
| async_tree_cpu_io_mixed    | 313 ms   | 359 ms: 1.15x slower   |
| async_tree_cpu_io_mixed_tg | 316 ms   | 363 ms: 1.15x slower   |
| sympy_sum                  | 79.2 ms  | 91.4 ms: 1.15x slower  |
| tomli_loads                | 1.09 sec | 1.26 sec: 1.16x slower |
| sqlglot_v2_optimize        | 31.1 ms  | 36.1 ms: 1.16x slower  |
| sqlglot_v2_transpile       | 873 us   | 1.01 ms: 1.16x slower  |
| deltablue                  | 1.64 ms  | 1.91 ms: 1.16x slower  |
| sphinx                     | 603 ms   | 702 ms: 1.16x slower   |
| pyflate                    | 234 ms   | 274 ms: 1.17x slower   |
| xml_etree_parse            | 89.4 ms  | 105 ms: 1.17x slower   |
| sqlglot_v2_parse           | 682 us   | 798 us: 1.17x slower   |
| regex_compile              | 69.8 ms  | 81.9 ms: 1.17x slower  |
| richards                   | 26.3 ms  | 30.9 ms: 1.18x slower  |
| bpe_tokeniser              | 2.55 sec | 3.01 sec: 1.18x slower |
| richards_super             | 30.2 ms  | 35.8 ms: 1.18x slower  |
| django_template            | 21.3 ms  | 25.2 ms: 1.18x slower  |
| sympy_str                  | 149 ms   | 177 ms: 1.19x slower   |
| sympy_expand               | 256 ms   | 304 ms: 1.19x slower   |
| raytrace                   | 142 ms   | 169 ms: 1.19x slower   |
| spectral_norm              | 42.8 ms  | 51.1 ms: 1.19x slower  |
| sympy_integrate            | 11.2 ms  | 13.4 ms: 1.20x slower  |
| nqueens                    | 49.8 ms  | 59.6 ms: 1.20x slower  |
| crypto_pyaes               | 39.9 ms  | 48.0 ms: 1.20x slower  |
| chaos                      | 31.4 ms  | 37.7 ms: 1.20x slower  |
| regex_effbot               | 1.54 ms  | 1.85 ms: 1.20x slower  |
| scimark_fft                | 139 ms   | 169 ms: 1.21x slower   |
| typing_runtime_protocols   | 87.6 us  | 106 us: 1.21x slower   |
| fannkuch                   | 207 ms   | 250 ms: 1.21x slower   |
| genshi_text                | 11.9 ms  | 14.5 ms: 1.21x slower  |
| pprint_safe_repr           | 415 ms   | 510 ms: 1.23x slower   |
| telco                      | 4.25 ms  | 5.26 ms: 1.24x slower  |
| scimark_sparse_mat_mult    | 1.99 ms  | 2.47 ms: 1.24x slower  |
| pprint_pformat             | 835 ms   | 1.04 sec: 1.24x slower |
| deepcopy_reduce            | 1.52 us  | 1.90 us: 1.25x slower  |
| deepcopy                   | 144 us   | 180 us: 1.25x slower   |
| regex_v8                   | 13.0 ms  | 16.3 ms: 1.26x slower  |
| pickle_pure_python         | 173 us   | 223 us: 1.29x slower   |
| comprehensions             | 8.64 us  | 11.3 us: 1.31x slower  |
| hexiom                     | 2.98 ms  | 3.92 ms: 1.31x slower  |
| xml_etree_process          | 34.0 ms  | 44.7 ms: 1.32x slower  |
| xml_etree_generate         | 49.1 ms  | 64.7 ms: 1.32x slower  |
| json                       | 2.81 ms  | 3.78 ms: 1.34x slower  |
| mako                       | 5.83 ms  | 7.84 ms: 1.35x slower  |
| scimark_monte_carlo        | 28.6 ms  | 38.9 ms: 1.36x slower  |
| json_dumps                 | 5.66 ms  | 7.79 ms: 1.38x slower  |
| deepcopy_memo              | 14.0 us  | 19.3 us: 1.38x slower  |
| unpickle_pure_python       | 107 us   | 148 us: 1.38x slower   |
| scimark_sor                | 49.3 ms  | 68.6 ms: 1.39x slower  |
| coverage                   | 39.8 ms  | 55.4 ms: 1.39x slower  |
| scimark_lu                 | 43.5 ms  | 64.2 ms: 1.47x slower  |
| logging_silent             | 41.1 ns  | 61.1 ns: 1.49x slower  |
| json_loads                 | 14.1 us  | 21.9 us: 1.56x slower  |
| many_optionals             | 409 us   | 762 us: 1.86x slower   |
| asyncio_websockets         | 159 ms   | 312 ms: 1.96x slower   |
| mdp                        | 682 ms   | 1.44 sec: 2.12x slower |
| subparsers                 | 15.3 ms  | 44.5 ms: 2.91x slower  |
| Geometric mean             | (ref)    | 1.20x slower           |

Benchmark hidden because not significant (2): python_startup, pidigits
Ignored benchmarks (1) of TC-Ex.json: thrift

- Geometric mean (including insignificant results): 1.169x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: unknown