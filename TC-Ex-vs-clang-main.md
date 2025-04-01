# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.038x slower
- HPT reliability: 67.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-main | TC-Ex                  |
|----------------|:----------:|:----------------------:|
| 2to3           | 220 ms     | 231 ms: 1.05x slower   |
| docutils       | 1.65 sec   | 1.77 sec: 1.07x slower |
| sphinx         | 653 ms     | 702 ms: 1.07x slower   |
| Geometric mean | (ref)      | 1.05x slower           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-main | TC-Ex                 |
|----------------------------|:----------:|:---------------------:|
| coroutines                 | 13.4 ms    | 12.3 ms: 1.09x faster |
| async_tree_io              | 416 ms     | 384 ms: 1.09x faster  |
| async_tree_none            | 185 ms     | 174 ms: 1.07x faster  |
| async_tree_io_tg           | 407 ms     | 385 ms: 1.06x faster  |
| async_tree_none_tg         | 176 ms     | 167 ms: 1.05x faster  |
| async_generators           | 223 ms     | 213 ms: 1.05x faster  |
| async_tree_memoization     | 216 ms     | 210 ms: 1.03x faster  |
| async_tree_memoization_tg  | 215 ms     | 210 ms: 1.02x faster  |
| async_tree_cpu_io_mixed_tg | 342 ms     | 363 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 337 ms     | 359 ms: 1.07x slower  |
| asyncio_websockets         | 158 ms     | 312 ms: 1.98x slower  |
| Geometric mean             | (ref)      | 1.03x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-main | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| nbody          | 64.2 ms    | 53.1 ms: 1.21x faster |
| float          | 44.7 ms    | 41.4 ms: 1.08x faster |
| pidigits       | 149 ms     | 146 ms: 1.03x faster  |
| Geometric mean | (ref)      | 1.10x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-main | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| regex_compile  | 82.3 ms    | 81.9 ms: 1.00x faster |
| regex_dna      | 114 ms     | 121 ms: 1.06x slower  |
| regex_v8       | 13.4 ms    | 16.3 ms: 1.22x slower |
| regex_effbot   | 1.39 ms    | 1.85 ms: 1.33x slower |
| Geometric mean | (ref)      | 1.14x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-main | TC-Ex                  |
|----------------------|:----------:|:----------------------:|
| tomli_loads          | 1.41 sec   | 1.26 sec: 1.12x faster |
| pickle_pure_python   | 216 us     | 223 us: 1.03x slower   |
| unpickle_pure_python | 140 us     | 148 us: 1.06x slower   |
| xml_etree_process    | 40.9 ms    | 44.7 ms: 1.09x slower  |
| xml_etree_iterparse  | 64.1 ms    | 70.4 ms: 1.10x slower  |
| xml_etree_generate   | 57.2 ms    | 64.7 ms: 1.13x slower  |
| json_dumps           | 6.78 ms    | 7.79 ms: 1.15x slower  |
| xml_etree_parse      | 87.6 ms    | 105 ms: 1.19x slower   |
| json_loads           | 15.1 us    | 21.9 us: 1.45x slower  |
| Geometric mean       | (ref)      | 1.11x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-main | TC-Ex                 |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 20.4 ms    | 19.4 ms: 1.05x faster |
| python_startup         | 25.8 ms    | 26.4 ms: 1.02x slower |
| Geometric mean         | (ref)      | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-main | TC-Ex                 |
|-----------------|:----------:|:---------------------:|
| genshi_text     | 15.8 ms    | 14.5 ms: 1.09x faster |
| genshi_xml      | 34.2 ms    | 31.3 ms: 1.09x faster |
| django_template | 25.4 ms    | 25.2 ms: 1.01x faster |
| mako            | 6.71 ms    | 7.84 ms: 1.17x slower |
| Geometric mean  | (ref)      | 1.01x faster          |

All benchmarks:
===============

| Benchmark                  | clang-main | TC-Ex                  |
|----------------------------|:----------:|:----------------------:|
| pathlib                    | 32.5 ms    | 25.1 ms: 1.29x faster  |
| nbody                      | 64.2 ms    | 53.1 ms: 1.21x faster  |
| go                         | 80.8 ms    | 70.4 ms: 1.15x faster  |
| tomli_loads                | 1.41 sec   | 1.26 sec: 1.12x faster |
| scimark_sor                | 76.7 ms    | 68.6 ms: 1.12x faster  |
| scimark_monte_carlo        | 43.5 ms    | 38.9 ms: 1.12x faster  |
| deltablue                  | 2.12 ms    | 1.91 ms: 1.11x faster  |
| generators                 | 17.9 ms    | 16.3 ms: 1.10x faster  |
| scimark_fft                | 185 ms     | 169 ms: 1.09x faster   |
| coroutines                 | 13.4 ms    | 12.3 ms: 1.09x faster  |
| genshi_text                | 15.8 ms    | 14.5 ms: 1.09x faster  |
| genshi_xml                 | 34.2 ms    | 31.3 ms: 1.09x faster  |
| scimark_sparse_mat_mult    | 2.69 ms    | 2.47 ms: 1.09x faster  |
| async_tree_io              | 416 ms     | 384 ms: 1.09x faster   |
| spectral_norm              | 55.1 ms    | 51.1 ms: 1.08x faster  |
| connected_components       | 336 ms     | 311 ms: 1.08x faster   |
| float                      | 44.7 ms    | 41.4 ms: 1.08x faster  |
| raytrace                   | 181 ms     | 169 ms: 1.07x faster   |
| async_tree_none            | 185 ms     | 174 ms: 1.07x faster   |
| sqlglot_v2_parse           | 851 us     | 798 us: 1.07x faster   |
| pyflate                    | 291 ms     | 274 ms: 1.06x faster   |
| nqueens                    | 63.5 ms    | 59.6 ms: 1.06x faster  |
| chaos                      | 40.2 ms    | 37.7 ms: 1.06x faster  |
| async_tree_io_tg           | 407 ms     | 385 ms: 1.06x faster   |
| shortest_path              | 366 ms     | 347 ms: 1.06x faster   |
| python_startup_no_site     | 20.4 ms    | 19.4 ms: 1.05x faster  |
| hexiom                     | 4.12 ms    | 3.92 ms: 1.05x faster  |
| async_tree_none_tg         | 176 ms     | 167 ms: 1.05x faster   |
| async_generators           | 223 ms     | 213 ms: 1.05x faster   |
| fannkuch                   | 260 ms     | 250 ms: 1.04x faster   |
| sqlglot_v2_transpile       | 1.05 ms    | 1.01 ms: 1.04x faster  |
| async_tree_memoization     | 216 ms     | 210 ms: 1.03x faster   |
| pprint_pformat             | 1.07 sec   | 1.04 sec: 1.03x faster |
| pidigits                   | 149 ms     | 146 ms: 1.03x faster   |
| logging_format             | 6.88 us    | 6.70 us: 1.03x faster  |
| meteor_contest             | 76.2 ms    | 74.5 ms: 1.02x faster  |
| logging_simple             | 6.39 us    | 6.25 us: 1.02x faster  |
| pprint_safe_repr           | 521 ms     | 510 ms: 1.02x faster   |
| async_tree_memoization_tg  | 215 ms     | 210 ms: 1.02x faster   |
| pycparser                  | 728 ms     | 713 ms: 1.02x faster   |
| comprehensions             | 11.5 us    | 11.3 us: 1.02x faster  |
| typing_runtime_protocols   | 107 us     | 106 us: 1.01x faster   |
| django_template            | 25.4 ms    | 25.2 ms: 1.01x faster  |
| regex_compile              | 82.3 ms    | 81.9 ms: 1.00x faster  |
| dulwich_log                | 42.1 ms    | 42.3 ms: 1.01x slower  |
| deepcopy_reduce            | 1.88 us    | 1.90 us: 1.01x slower  |
| deepcopy_memo              | 19.1 us    | 19.3 us: 1.01x slower  |
| sympy_str                  | 175 ms     | 177 ms: 1.01x slower   |
| sympy_expand               | 301 ms     | 304 ms: 1.01x slower   |
| crypto_pyaes               | 47.3 ms    | 48.0 ms: 1.01x slower  |
| sympy_sum                  | 89.6 ms    | 91.4 ms: 1.02x slower  |
| python_startup             | 25.8 ms    | 26.4 ms: 1.02x slower  |
| pylint                     | 200 ms     | 205 ms: 1.03x slower   |
| bpe_tokeniser              | 2.93 sec   | 3.01 sec: 1.03x slower |
| sqlglot_v2_optimize        | 35.1 ms    | 36.1 ms: 1.03x slower  |
| pickle_pure_python         | 216 us     | 223 us: 1.03x slower   |
| sympy_integrate            | 12.9 ms    | 13.4 ms: 1.04x slower  |
| scimark_lu                 | 61.6 ms    | 64.2 ms: 1.04x slower  |
| 2to3                       | 220 ms     | 231 ms: 1.05x slower   |
| bench_mp_pool              | 88.9 ms    | 93.6 ms: 1.05x slower  |
| unpickle_pure_python       | 140 us     | 148 us: 1.06x slower   |
| regex_dna                  | 114 ms     | 121 ms: 1.06x slower   |
| sqlite_synth               | 1.58 us    | 1.68 us: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 342 ms     | 363 ms: 1.06x slower   |
| async_tree_cpu_io_mixed    | 337 ms     | 359 ms: 1.07x slower   |
| docutils                   | 1.65 sec   | 1.77 sec: 1.07x slower |
| create_gc_cycles           | 1.25 ms    | 1.34 ms: 1.07x slower  |
| sphinx                     | 653 ms     | 702 ms: 1.07x slower   |
| telco                      | 4.87 ms    | 5.26 ms: 1.08x slower  |
| logging_silent             | 56.3 ns    | 61.1 ns: 1.09x slower  |
| xml_etree_process          | 40.9 ms    | 44.7 ms: 1.09x slower  |
| xml_etree_iterparse        | 64.1 ms    | 70.4 ms: 1.10x slower  |
| richards                   | 27.8 ms    | 30.9 ms: 1.11x slower  |
| xml_etree_generate         | 57.2 ms    | 64.7 ms: 1.13x slower  |
| richards_super             | 31.5 ms    | 35.8 ms: 1.14x slower  |
| coverage                   | 48.3 ms    | 55.4 ms: 1.15x slower  |
| json_dumps                 | 6.78 ms    | 7.79 ms: 1.15x slower  |
| mako                       | 6.71 ms    | 7.84 ms: 1.17x slower  |
| xml_etree_parse            | 87.6 ms    | 105 ms: 1.19x slower   |
| regex_v8                   | 13.4 ms    | 16.3 ms: 1.22x slower  |
| json                       | 3.09 ms    | 3.78 ms: 1.22x slower  |
| regex_effbot               | 1.39 ms    | 1.85 ms: 1.33x slower  |
| gc_traversal               | 2.08 ms    | 2.83 ms: 1.36x slower  |
| json_loads                 | 15.1 us    | 21.9 us: 1.45x slower  |
| many_optionals             | 432 us     | 762 us: 1.76x slower   |
| mdp                        | 799 ms     | 1.44 sec: 1.81x slower |
| asyncio_websockets         | 158 ms     | 312 ms: 1.98x slower   |
| subparsers                 | 15.9 ms    | 44.5 ms: 2.79x slower  |
| Geometric mean             | (ref)      | 1.04x slower           |

Benchmark hidden because not significant (5): html5lib, k_core, sqlglot_v2_normalize, deepcopy, bench_thread_pool
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of TC-Ex.json: thrift

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 67.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown