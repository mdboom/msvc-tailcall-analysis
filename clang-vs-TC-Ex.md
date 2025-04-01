# Results vs. base

- fork: unknown
- ref: clang
- machine: unknown-unknown
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.203x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | clang                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 207 ms: 1.12x faster   |
| docutils       | 1.77 sec | 1.56 sec: 1.14x faster |
| html5lib       | 38.8 ms  | 34.9 ms: 1.11x faster  |
| sphinx         | 702 ms   | 603 ms: 1.16x faster   |
| Geometric mean | (ref)    | 1.13x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | clang                 |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 312 ms  | 159 ms: 1.96x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms  | 316 ms: 1.15x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 313 ms: 1.15x faster  |
| coroutines                 | 12.3 ms | 10.7 ms: 1.14x faster |
| async_generators           | 213 ms  | 187 ms: 1.14x faster  |
| async_tree_memoization     | 210 ms  | 187 ms: 1.12x faster  |
| async_tree_none_tg         | 167 ms  | 150 ms: 1.11x faster  |
| async_tree_io_tg           | 385 ms  | 351 ms: 1.10x faster  |
| async_tree_none            | 174 ms  | 159 ms: 1.09x faster  |
| async_tree_io              | 384 ms  | 353 ms: 1.09x faster  |
| async_tree_memoization_tg  | 210 ms  | 197 ms: 1.07x faster  |
| Geometric mean             | (ref)   | 1.17x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | clang                 |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 36.9 ms: 1.12x faster |
| nbody          | 53.1 ms | 49.1 ms: 1.08x faster |
| Geometric mean | (ref)   | 1.07x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | clang                 |
|----------------|:-------:|:---------------------:|
| regex_v8       | 16.3 ms | 13.0 ms: 1.26x faster |
| regex_effbot   | 1.85 ms | 1.54 ms: 1.20x faster |
| regex_compile  | 81.9 ms | 69.8 ms: 1.17x faster |
| regex_dna      | 121 ms  | 117 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.16x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | clang                  |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.1 us: 1.56x faster  |
| unpickle_pure_python | 148 us   | 107 us: 1.38x faster   |
| json_dumps           | 7.79 ms  | 5.66 ms: 1.38x faster  |
| xml_etree_generate   | 64.7 ms  | 49.1 ms: 1.32x faster  |
| xml_etree_process    | 44.7 ms  | 34.0 ms: 1.32x faster  |
| pickle_pure_python   | 223 us   | 173 us: 1.29x faster   |
| xml_etree_parse      | 105 ms   | 89.4 ms: 1.17x faster  |
| tomli_loads          | 1.26 sec | 1.09 sec: 1.16x faster |
| xml_etree_iterparse  | 70.4 ms  | 61.5 ms: 1.14x faster  |
| Geometric mean       | (ref)    | 1.29x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | clang                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.4 ms | 20.9 ms: 1.08x slower |
| Geometric mean         | (ref)   | 1.04x slower          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | clang                 |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 5.83 ms: 1.35x faster |
| genshi_text     | 14.5 ms | 11.9 ms: 1.21x faster |
| django_template | 25.2 ms | 21.3 ms: 1.18x faster |
| genshi_xml      | 31.3 ms | 29.0 ms: 1.08x faster |
| Geometric mean  | (ref)   | 1.20x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | clang                  |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 44.5 ms  | 15.3 ms: 2.91x faster  |
| mdp                        | 1.44 sec | 682 ms: 2.12x faster   |
| asyncio_websockets         | 312 ms   | 159 ms: 1.96x faster   |
| many_optionals             | 762 us   | 409 us: 1.86x faster   |
| json_loads                 | 21.9 us  | 14.1 us: 1.56x faster  |
| logging_silent             | 61.1 ns  | 41.1 ns: 1.49x faster  |
| scimark_lu                 | 64.2 ms  | 43.5 ms: 1.47x faster  |
| coverage                   | 55.4 ms  | 39.8 ms: 1.39x faster  |
| scimark_sor                | 68.6 ms  | 49.3 ms: 1.39x faster  |
| unpickle_pure_python       | 148 us   | 107 us: 1.38x faster   |
| deepcopy_memo              | 19.3 us  | 14.0 us: 1.38x faster  |
| json_dumps                 | 7.79 ms  | 5.66 ms: 1.38x faster  |
| scimark_monte_carlo        | 38.9 ms  | 28.6 ms: 1.36x faster  |
| mako                       | 7.84 ms  | 5.83 ms: 1.35x faster  |
| json                       | 3.78 ms  | 2.81 ms: 1.34x faster  |
| xml_etree_generate         | 64.7 ms  | 49.1 ms: 1.32x faster  |
| xml_etree_process          | 44.7 ms  | 34.0 ms: 1.32x faster  |
| hexiom                     | 3.92 ms  | 2.98 ms: 1.31x faster  |
| comprehensions             | 11.3 us  | 8.64 us: 1.31x faster  |
| pickle_pure_python         | 223 us   | 173 us: 1.29x faster   |
| regex_v8                   | 16.3 ms  | 13.0 ms: 1.26x faster  |
| deepcopy                   | 180 us   | 144 us: 1.25x faster   |
| deepcopy_reduce            | 1.90 us  | 1.52 us: 1.25x faster  |
| pprint_pformat             | 1.04 sec | 835 ms: 1.24x faster   |
| scimark_sparse_mat_mult    | 2.47 ms  | 1.99 ms: 1.24x faster  |
| telco                      | 5.26 ms  | 4.25 ms: 1.24x faster  |
| pprint_safe_repr           | 510 ms   | 415 ms: 1.23x faster   |
| genshi_text                | 14.5 ms  | 11.9 ms: 1.21x faster  |
| fannkuch                   | 250 ms   | 207 ms: 1.21x faster   |
| typing_runtime_protocols   | 106 us   | 87.6 us: 1.21x faster  |
| scimark_fft                | 169 ms   | 139 ms: 1.21x faster   |
| regex_effbot               | 1.85 ms  | 1.54 ms: 1.20x faster  |
| chaos                      | 37.7 ms  | 31.4 ms: 1.20x faster  |
| crypto_pyaes               | 48.0 ms  | 39.9 ms: 1.20x faster  |
| nqueens                    | 59.6 ms  | 49.8 ms: 1.20x faster  |
| sympy_integrate            | 13.4 ms  | 11.2 ms: 1.20x faster  |
| spectral_norm              | 51.1 ms  | 42.8 ms: 1.19x faster  |
| raytrace                   | 169 ms   | 142 ms: 1.19x faster   |
| sympy_expand               | 304 ms   | 256 ms: 1.19x faster   |
| sympy_str                  | 177 ms   | 149 ms: 1.19x faster   |
| django_template            | 25.2 ms  | 21.3 ms: 1.18x faster  |
| richards_super             | 35.8 ms  | 30.2 ms: 1.18x faster  |
| bpe_tokeniser              | 3.01 sec | 2.55 sec: 1.18x faster |
| richards                   | 30.9 ms  | 26.3 ms: 1.18x faster  |
| regex_compile              | 81.9 ms  | 69.8 ms: 1.17x faster  |
| sqlglot_v2_parse           | 798 us   | 682 us: 1.17x faster   |
| xml_etree_parse            | 105 ms   | 89.4 ms: 1.17x faster  |
| pyflate                    | 274 ms   | 234 ms: 1.17x faster   |
| sphinx                     | 702 ms   | 603 ms: 1.16x faster   |
| deltablue                  | 1.91 ms  | 1.64 ms: 1.16x faster  |
| sqlglot_v2_transpile       | 1.01 ms  | 873 us: 1.16x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 31.1 ms: 1.16x faster  |
| tomli_loads                | 1.26 sec | 1.09 sec: 1.16x faster |
| sympy_sum                  | 91.4 ms  | 79.2 ms: 1.15x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms   | 316 ms: 1.15x faster   |
| async_tree_cpu_io_mixed    | 359 ms   | 313 ms: 1.15x faster   |
| go                         | 70.4 ms  | 61.5 ms: 1.14x faster  |
| xml_etree_iterparse        | 70.4 ms  | 61.5 ms: 1.14x faster  |
| coroutines                 | 12.3 ms  | 10.7 ms: 1.14x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 64.2 ms: 1.14x faster  |
| async_generators           | 213 ms   | 187 ms: 1.14x faster   |
| docutils                   | 1.77 sec | 1.56 sec: 1.14x faster |
| logging_simple             | 6.25 us  | 5.55 us: 1.13x faster  |
| logging_format             | 6.70 us  | 5.96 us: 1.13x faster  |
| float                      | 41.4 ms  | 36.9 ms: 1.12x faster  |
| async_tree_memoization     | 210 ms   | 187 ms: 1.12x faster   |
| 2to3                       | 231 ms   | 207 ms: 1.12x faster   |
| meteor_contest             | 74.5 ms  | 66.8 ms: 1.12x faster  |
| dulwich_log                | 42.3 ms  | 38.0 ms: 1.11x faster  |
| async_tree_none_tg         | 167 ms   | 150 ms: 1.11x faster   |
| sqlite_synth               | 1.68 us  | 1.51 us: 1.11x faster  |
| html5lib                   | 38.8 ms  | 34.9 ms: 1.11x faster  |
| generators                 | 16.3 ms  | 14.8 ms: 1.10x faster  |
| pycparser                  | 713 ms   | 647 ms: 1.10x faster   |
| async_tree_io_tg           | 385 ms   | 351 ms: 1.10x faster   |
| async_tree_none            | 174 ms   | 159 ms: 1.09x faster   |
| pylint                     | 205 ms   | 188 ms: 1.09x faster   |
| async_tree_io              | 384 ms   | 353 ms: 1.09x faster   |
| nbody                      | 53.1 ms  | 49.1 ms: 1.08x faster  |
| genshi_xml                 | 31.3 ms  | 29.0 ms: 1.08x faster  |
| async_tree_memoization_tg  | 210 ms   | 197 ms: 1.07x faster   |
| bench_thread_pool          | 876 us   | 823 us: 1.06x faster   |
| bench_mp_pool              | 93.6 ms  | 88.6 ms: 1.06x faster  |
| k_core                     | 1.71 sec | 1.66 sec: 1.03x faster |
| regex_dna                  | 121 ms   | 117 ms: 1.03x faster   |
| gc_traversal               | 2.83 ms  | 2.76 ms: 1.03x faster  |
| shortest_path              | 347 ms   | 351 ms: 1.01x slower   |
| create_gc_cycles           | 1.34 ms  | 1.36 ms: 1.02x slower  |
| connected_components       | 311 ms   | 329 ms: 1.06x slower   |
| python_startup_no_site     | 19.4 ms  | 20.9 ms: 1.08x slower  |
| pathlib                    | 25.1 ms  | 30.7 ms: 1.22x slower  |
| Geometric mean             | (ref)    | 1.20x faster           |

Benchmark hidden because not significant (2): pidigits, python_startup
Ignored benchmarks (1) of TC-Ex.json: thrift

- Geometric mean (including insignificant results): 1.203x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown