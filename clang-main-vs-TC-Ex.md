# Results vs. base

- fork: unknown
- ref: clang-main
- machine: unknown-unknown
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.040x faster
- HPT reliability: 67.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | clang-main             |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 220 ms: 1.05x faster   |
| docutils       | 1.77 sec | 1.65 sec: 1.07x faster |
| sphinx         | 702 ms   | 653 ms: 1.07x faster   |
| Geometric mean | (ref)    | 1.05x faster           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | clang-main            |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 312 ms  | 158 ms: 1.98x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 337 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms  | 342 ms: 1.06x faster  |
| async_tree_memoization_tg  | 210 ms  | 215 ms: 1.02x slower  |
| async_tree_memoization     | 210 ms  | 216 ms: 1.03x slower  |
| async_generators           | 213 ms  | 223 ms: 1.05x slower  |
| async_tree_none_tg         | 167 ms  | 176 ms: 1.05x slower  |
| async_tree_io_tg           | 385 ms  | 407 ms: 1.06x slower  |
| async_tree_none            | 174 ms  | 185 ms: 1.07x slower  |
| async_tree_io              | 384 ms  | 416 ms: 1.09x slower  |
| coroutines                 | 12.3 ms | 13.4 ms: 1.09x slower |
| Geometric mean             | (ref)   | 1.03x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | clang-main            |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 149 ms: 1.03x slower  |
| float          | 41.4 ms | 44.7 ms: 1.08x slower |
| nbody          | 53.1 ms | 64.2 ms: 1.21x slower |
| Geometric mean | (ref)   | 1.10x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | clang-main            |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.39 ms: 1.33x faster |
| regex_v8       | 16.3 ms | 13.4 ms: 1.22x faster |
| regex_dna      | 121 ms  | 114 ms: 1.06x faster  |
| regex_compile  | 81.9 ms | 82.3 ms: 1.00x slower |
| Geometric mean | (ref)   | 1.14x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | clang-main             |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 15.1 us: 1.45x faster  |
| xml_etree_parse      | 105 ms   | 87.6 ms: 1.19x faster  |
| json_dumps           | 7.79 ms  | 6.78 ms: 1.15x faster  |
| xml_etree_generate   | 64.7 ms  | 57.2 ms: 1.13x faster  |
| xml_etree_iterparse  | 70.4 ms  | 64.1 ms: 1.10x faster  |
| xml_etree_process    | 44.7 ms  | 40.9 ms: 1.09x faster  |
| unpickle_pure_python | 148 us   | 140 us: 1.06x faster   |
| pickle_pure_python   | 223 us   | 216 us: 1.03x faster   |
| tomli_loads          | 1.26 sec | 1.41 sec: 1.12x slower |
| Geometric mean       | (ref)    | 1.11x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | clang-main            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 25.8 ms: 1.02x faster |
| python_startup_no_site | 19.4 ms | 20.4 ms: 1.05x slower |
| Geometric mean         | (ref)   | 1.02x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | clang-main            |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.71 ms: 1.17x faster |
| django_template | 25.2 ms | 25.4 ms: 1.01x slower |
| genshi_xml      | 31.3 ms | 34.2 ms: 1.09x slower |
| genshi_text     | 14.5 ms | 15.8 ms: 1.09x slower |
| Geometric mean  | (ref)   | 1.01x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | clang-main             |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 44.5 ms  | 15.9 ms: 2.79x faster  |
| asyncio_websockets         | 312 ms   | 158 ms: 1.98x faster   |
| mdp                        | 1.44 sec | 799 ms: 1.81x faster   |
| many_optionals             | 762 us   | 432 us: 1.76x faster   |
| json_loads                 | 21.9 us  | 15.1 us: 1.45x faster  |
| gc_traversal               | 2.83 ms  | 2.08 ms: 1.36x faster  |
| regex_effbot               | 1.85 ms  | 1.39 ms: 1.33x faster  |
| json                       | 3.78 ms  | 3.09 ms: 1.22x faster  |
| regex_v8                   | 16.3 ms  | 13.4 ms: 1.22x faster  |
| xml_etree_parse            | 105 ms   | 87.6 ms: 1.19x faster  |
| mako                       | 7.84 ms  | 6.71 ms: 1.17x faster  |
| json_dumps                 | 7.79 ms  | 6.78 ms: 1.15x faster  |
| coverage                   | 55.4 ms  | 48.3 ms: 1.15x faster  |
| richards_super             | 35.8 ms  | 31.5 ms: 1.14x faster  |
| xml_etree_generate         | 64.7 ms  | 57.2 ms: 1.13x faster  |
| richards                   | 30.9 ms  | 27.8 ms: 1.11x faster  |
| xml_etree_iterparse        | 70.4 ms  | 64.1 ms: 1.10x faster  |
| xml_etree_process          | 44.7 ms  | 40.9 ms: 1.09x faster  |
| logging_silent             | 61.1 ns  | 56.3 ns: 1.09x faster  |
| telco                      | 5.26 ms  | 4.87 ms: 1.08x faster  |
| sphinx                     | 702 ms   | 653 ms: 1.07x faster   |
| create_gc_cycles           | 1.34 ms  | 1.25 ms: 1.07x faster  |
| docutils                   | 1.77 sec | 1.65 sec: 1.07x faster |
| async_tree_cpu_io_mixed    | 359 ms   | 337 ms: 1.07x faster   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 342 ms: 1.06x faster   |
| sqlite_synth               | 1.68 us  | 1.58 us: 1.06x faster  |
| regex_dna                  | 121 ms   | 114 ms: 1.06x faster   |
| unpickle_pure_python       | 148 us   | 140 us: 1.06x faster   |
| bench_mp_pool              | 93.6 ms  | 88.9 ms: 1.05x faster  |
| 2to3                       | 231 ms   | 220 ms: 1.05x faster   |
| scimark_lu                 | 64.2 ms  | 61.6 ms: 1.04x faster  |
| sympy_integrate            | 13.4 ms  | 12.9 ms: 1.04x faster  |
| pickle_pure_python         | 223 us   | 216 us: 1.03x faster   |
| sqlglot_v2_optimize        | 36.1 ms  | 35.1 ms: 1.03x faster  |
| bpe_tokeniser              | 3.01 sec | 2.93 sec: 1.03x faster |
| pylint                     | 205 ms   | 200 ms: 1.03x faster   |
| python_startup             | 26.4 ms  | 25.8 ms: 1.02x faster  |
| sympy_sum                  | 91.4 ms  | 89.6 ms: 1.02x faster  |
| crypto_pyaes               | 48.0 ms  | 47.3 ms: 1.01x faster  |
| sympy_expand               | 304 ms   | 301 ms: 1.01x faster   |
| sympy_str                  | 177 ms   | 175 ms: 1.01x faster   |
| deepcopy_memo              | 19.3 us  | 19.1 us: 1.01x faster  |
| deepcopy_reduce            | 1.90 us  | 1.88 us: 1.01x faster  |
| dulwich_log                | 42.3 ms  | 42.1 ms: 1.01x faster  |
| regex_compile              | 81.9 ms  | 82.3 ms: 1.00x slower  |
| django_template            | 25.2 ms  | 25.4 ms: 1.01x slower  |
| typing_runtime_protocols   | 106 us   | 107 us: 1.01x slower   |
| comprehensions             | 11.3 us  | 11.5 us: 1.02x slower  |
| pycparser                  | 713 ms   | 728 ms: 1.02x slower   |
| async_tree_memoization_tg  | 210 ms   | 215 ms: 1.02x slower   |
| pprint_safe_repr           | 510 ms   | 521 ms: 1.02x slower   |
| logging_simple             | 6.25 us  | 6.39 us: 1.02x slower  |
| meteor_contest             | 74.5 ms  | 76.2 ms: 1.02x slower  |
| logging_format             | 6.70 us  | 6.88 us: 1.03x slower  |
| pidigits                   | 146 ms   | 149 ms: 1.03x slower   |
| pprint_pformat             | 1.04 sec | 1.07 sec: 1.03x slower |
| async_tree_memoization     | 210 ms   | 216 ms: 1.03x slower   |
| sqlglot_v2_transpile       | 1.01 ms  | 1.05 ms: 1.04x slower  |
| fannkuch                   | 250 ms   | 260 ms: 1.04x slower   |
| async_generators           | 213 ms   | 223 ms: 1.05x slower   |
| async_tree_none_tg         | 167 ms   | 176 ms: 1.05x slower   |
| hexiom                     | 3.92 ms  | 4.12 ms: 1.05x slower  |
| python_startup_no_site     | 19.4 ms  | 20.4 ms: 1.05x slower  |
| shortest_path              | 347 ms   | 366 ms: 1.06x slower   |
| async_tree_io_tg           | 385 ms   | 407 ms: 1.06x slower   |
| chaos                      | 37.7 ms  | 40.2 ms: 1.06x slower  |
| nqueens                    | 59.6 ms  | 63.5 ms: 1.06x slower  |
| pyflate                    | 274 ms   | 291 ms: 1.06x slower   |
| sqlglot_v2_parse           | 798 us   | 851 us: 1.07x slower   |
| async_tree_none            | 174 ms   | 185 ms: 1.07x slower   |
| raytrace                   | 169 ms   | 181 ms: 1.07x slower   |
| float                      | 41.4 ms  | 44.7 ms: 1.08x slower  |
| connected_components       | 311 ms   | 336 ms: 1.08x slower   |
| spectral_norm              | 51.1 ms  | 55.1 ms: 1.08x slower  |
| async_tree_io              | 384 ms   | 416 ms: 1.09x slower   |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.69 ms: 1.09x slower  |
| genshi_xml                 | 31.3 ms  | 34.2 ms: 1.09x slower  |
| genshi_text                | 14.5 ms  | 15.8 ms: 1.09x slower  |
| coroutines                 | 12.3 ms  | 13.4 ms: 1.09x slower  |
| scimark_fft                | 169 ms   | 185 ms: 1.09x slower   |
| generators                 | 16.3 ms  | 17.9 ms: 1.10x slower  |
| deltablue                  | 1.91 ms  | 2.12 ms: 1.11x slower  |
| scimark_monte_carlo        | 38.9 ms  | 43.5 ms: 1.12x slower  |
| scimark_sor                | 68.6 ms  | 76.7 ms: 1.12x slower  |
| tomli_loads                | 1.26 sec | 1.41 sec: 1.12x slower |
| go                         | 70.4 ms  | 80.8 ms: 1.15x slower  |
| nbody                      | 53.1 ms  | 64.2 ms: 1.21x slower  |
| pathlib                    | 25.1 ms  | 32.5 ms: 1.29x slower  |
| Geometric mean             | (ref)    | 1.04x faster           |

Benchmark hidden because not significant (5): bench_thread_pool, deepcopy, sqlglot_v2_normalize, k_core, html5lib
Ignored benchmarks (1) of TC-Ex.json: thrift
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 67.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown