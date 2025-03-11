# Results vs. base

- fork: unknown
- ref: NoTC-PGO-NoEx
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.008x slower
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-NoPGO-Ex | NoTC-PGO-NoEx          |
|----------------|:-----------:|:----------------------:|
| 2to3           | 231 ms      | 227 ms: 1.02x faster   |
| docutils       | 1.77 sec    | 1.68 sec: 1.05x faster |
| html5lib       | 38.8 ms     | 40.8 ms: 1.05x slower  |
| sphinx         | 702 ms      | 658 ms: 1.07x faster   |
| Geometric mean | (ref)       | 1.02x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-NoPGO-Ex | NoTC-PGO-NoEx         |
|----------------------------|:-----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 359 ms      | 339 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms      | 343 ms: 1.06x faster  |
| asyncio_websockets         | 312 ms      | 318 ms: 1.02x slower  |
| async_tree_memoization_tg  | 210 ms      | 216 ms: 1.02x slower  |
| async_tree_none_tg         | 167 ms      | 176 ms: 1.06x slower  |
| async_generators           | 213 ms      | 226 ms: 1.06x slower  |
| async_tree_io_tg           | 385 ms      | 410 ms: 1.06x slower  |
| async_tree_memoization     | 210 ms      | 224 ms: 1.07x slower  |
| async_tree_none            | 174 ms      | 187 ms: 1.07x slower  |
| coroutines                 | 12.3 ms     | 13.5 ms: 1.10x slower |
| async_tree_io              | 384 ms      | 423 ms: 1.10x slower  |
| Geometric mean             | (ref)       | 1.04x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-NoPGO-Ex | NoTC-PGO-NoEx         |
|----------------|:-----------:|:---------------------:|
| pidigits       | 146 ms      | 152 ms: 1.05x slower  |
| float          | 41.4 ms     | 47.8 ms: 1.15x slower |
| nbody          | 53.1 ms     | 74.1 ms: 1.40x slower |
| Geometric mean | (ref)       | 1.19x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-NoPGO-Ex | NoTC-PGO-NoEx         |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.85 ms     | 1.42 ms: 1.30x faster |
| regex_v8       | 16.3 ms     | 13.5 ms: 1.20x faster |
| regex_dna      | 121 ms      | 112 ms: 1.07x faster  |
| regex_compile  | 81.9 ms     | 88.2 ms: 1.08x slower |
| Geometric mean | (ref)       | 1.12x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-NoPGO-Ex | NoTC-PGO-NoEx          |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.9 us     | 14.7 us: 1.49x faster  |
| xml_etree_parse      | 105 ms      | 91.2 ms: 1.15x faster  |
| json_dumps           | 7.79 ms     | 7.05 ms: 1.10x faster  |
| xml_etree_iterparse  | 70.4 ms     | 63.7 ms: 1.10x faster  |
| xml_etree_generate   | 64.7 ms     | 58.7 ms: 1.10x faster  |
| xml_etree_process    | 44.7 ms     | 41.5 ms: 1.08x faster  |
| unpickle_pure_python | 148 us      | 155 us: 1.05x slower   |
| pickle_pure_python   | 223 us      | 237 us: 1.06x slower   |
| tomli_loads          | 1.26 sec    | 1.47 sec: 1.16x slower |
| Geometric mean       | (ref)       | 1.07x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-NoPGO-Ex | NoTC-PGO-NoEx         |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.4 ms     | 26.1 ms: 1.01x faster |
| python_startup_no_site | 19.4 ms     | 19.8 ms: 1.02x slower |
| Geometric mean         | (ref)       | 1.00x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark      | TC-NoPGO-Ex | NoTC-PGO-NoEx         |
|----------------|:-----------:|:---------------------:|
| mako           | 7.84 ms     | 6.86 ms: 1.14x faster |
| genshi_text    | 14.5 ms     | 16.5 ms: 1.14x slower |
| genshi_xml     | 31.3 ms     | 36.3 ms: 1.16x slower |
| Geometric mean | (ref)       | 1.04x slower          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | TC-NoPGO-Ex | NoTC-PGO-NoEx          |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 44.5 ms     | 16.1 ms: 2.76x faster  |
| many_optionals             | 762 us      | 438 us: 1.74x faster   |
| json_loads                 | 21.9 us     | 14.7 us: 1.49x faster  |
| gc_traversal               | 2.83 ms     | 2.06 ms: 1.38x faster  |
| regex_effbot               | 1.85 ms     | 1.42 ms: 1.30x faster  |
| json                       | 3.78 ms     | 3.14 ms: 1.20x faster  |
| regex_v8                   | 16.3 ms     | 13.5 ms: 1.20x faster  |
| coverage                   | 55.4 ms     | 46.8 ms: 1.18x faster  |
| xml_etree_parse            | 105 ms      | 91.2 ms: 1.15x faster  |
| mako                       | 7.84 ms     | 6.86 ms: 1.14x faster  |
| json_dumps                 | 7.79 ms     | 7.05 ms: 1.10x faster  |
| xml_etree_iterparse        | 70.4 ms     | 63.7 ms: 1.10x faster  |
| xml_etree_generate         | 64.7 ms     | 58.7 ms: 1.10x faster  |
| thrift                     | 551 us      | 507 us: 1.09x faster   |
| xml_etree_process          | 44.7 ms     | 41.5 ms: 1.08x faster  |
| telco                      | 5.26 ms     | 4.89 ms: 1.07x faster  |
| regex_dna                  | 121 ms      | 112 ms: 1.07x faster   |
| create_gc_cycles           | 1.34 ms     | 1.25 ms: 1.07x faster  |
| sphinx                     | 702 ms      | 658 ms: 1.07x faster   |
| async_tree_cpu_io_mixed    | 359 ms      | 339 ms: 1.06x faster   |
| async_tree_cpu_io_mixed_tg | 363 ms      | 343 ms: 1.06x faster   |
| bench_mp_pool              | 93.6 ms     | 88.7 ms: 1.06x faster  |
| sqlite_synth               | 1.68 us     | 1.59 us: 1.05x faster  |
| docutils                   | 1.77 sec    | 1.68 sec: 1.05x faster |
| sqlglot_v2_optimize        | 36.1 ms     | 35.0 ms: 1.03x faster  |
| richards_super             | 35.8 ms     | 35.1 ms: 1.02x faster  |
| bpe_tokeniser              | 3.01 sec    | 2.96 sec: 1.02x faster |
| 2to3                       | 231 ms      | 227 ms: 1.02x faster   |
| python_startup             | 26.4 ms     | 26.1 ms: 1.01x faster  |
| sympy_sum                  | 91.4 ms     | 90.5 ms: 1.01x faster  |
| sympy_expand               | 304 ms      | 302 ms: 1.01x faster   |
| richards                   | 30.9 ms     | 30.7 ms: 1.01x faster  |
| sympy_str                  | 177 ms      | 176 ms: 1.01x faster   |
| comprehensions             | 11.3 us     | 11.3 us: 1.00x slower  |
| sympy_integrate            | 13.4 ms     | 13.5 ms: 1.01x slower  |
| k_core                     | 1.71 sec    | 1.73 sec: 1.01x slower |
| asyncio_websockets         | 312 ms      | 318 ms: 1.02x slower   |
| python_startup_no_site     | 19.4 ms     | 19.8 ms: 1.02x slower  |
| deepcopy_reduce            | 1.90 us     | 1.94 us: 1.02x slower  |
| dulwich_log                | 42.3 ms     | 43.4 ms: 1.02x slower  |
| async_tree_memoization_tg  | 210 ms      | 216 ms: 1.02x slower   |
| meteor_contest             | 74.5 ms     | 76.9 ms: 1.03x slower  |
| pycparser                  | 713 ms      | 738 ms: 1.04x slower   |
| shortest_path              | 347 ms      | 359 ms: 1.04x slower   |
| crypto_pyaes               | 48.0 ms     | 50.0 ms: 1.04x slower  |
| scimark_lu                 | 64.2 ms     | 66.9 ms: 1.04x slower  |
| logging_simple             | 6.25 us     | 6.53 us: 1.04x slower  |
| pidigits                   | 146 ms      | 152 ms: 1.05x slower   |
| logging_format             | 6.70 us     | 7.03 us: 1.05x slower  |
| unpickle_pure_python       | 148 us      | 155 us: 1.05x slower   |
| deepcopy                   | 180 us      | 190 us: 1.05x slower   |
| html5lib                   | 38.8 ms     | 40.8 ms: 1.05x slower  |
| async_tree_none_tg         | 167 ms      | 176 ms: 1.06x slower   |
| connected_components       | 311 ms      | 329 ms: 1.06x slower   |
| async_generators           | 213 ms      | 226 ms: 1.06x slower   |
| async_tree_io_tg           | 385 ms      | 410 ms: 1.06x slower   |
| pickle_pure_python         | 223 us      | 237 us: 1.06x slower   |
| nqueens                    | 59.6 ms     | 63.6 ms: 1.07x slower  |
| logging_silent             | 61.1 ns     | 65.2 ns: 1.07x slower  |
| async_tree_memoization     | 210 ms      | 224 ms: 1.07x slower   |
| async_tree_none            | 174 ms      | 187 ms: 1.07x slower   |
| regex_compile              | 81.9 ms     | 88.2 ms: 1.08x slower  |
| pprint_pformat             | 1.04 sec    | 1.13 sec: 1.09x slower |
| sqlglot_v2_transpile       | 1.01 ms     | 1.10 ms: 1.09x slower  |
| deepcopy_memo              | 19.3 us     | 21.0 us: 1.09x slower  |
| pprint_safe_repr           | 510 ms      | 558 ms: 1.09x slower   |
| coroutines                 | 12.3 ms     | 13.5 ms: 1.10x slower  |
| async_tree_io              | 384 ms      | 423 ms: 1.10x slower   |
| scimark_sparse_mat_mult    | 2.47 ms     | 2.72 ms: 1.10x slower  |
| sqlglot_v2_parse           | 798 us      | 892 us: 1.12x slower   |
| hexiom                     | 3.92 ms     | 4.38 ms: 1.12x slower  |
| raytrace                   | 169 ms      | 191 ms: 1.13x slower   |
| mdp                        | 1.44 sec    | 1.64 sec: 1.13x slower |
| genshi_text                | 14.5 ms     | 16.5 ms: 1.14x slower  |
| scimark_fft                | 169 ms      | 192 ms: 1.14x slower   |
| float                      | 41.4 ms     | 47.8 ms: 1.15x slower  |
| pyflate                    | 274 ms      | 315 ms: 1.15x slower   |
| chaos                      | 37.7 ms     | 43.6 ms: 1.16x slower  |
| genshi_xml                 | 31.3 ms     | 36.3 ms: 1.16x slower  |
| tomli_loads                | 1.26 sec    | 1.47 sec: 1.16x slower |
| fannkuch                   | 250 ms      | 296 ms: 1.18x slower   |
| generators                 | 16.3 ms     | 19.3 ms: 1.19x slower  |
| deltablue                  | 1.91 ms     | 2.29 ms: 1.20x slower  |
| spectral_norm              | 51.1 ms     | 61.5 ms: 1.21x slower  |
| scimark_monte_carlo        | 38.9 ms     | 47.1 ms: 1.21x slower  |
| go                         | 70.4 ms     | 88.6 ms: 1.26x slower  |
| pathlib                    | 25.1 ms     | 32.1 ms: 1.28x slower  |
| scimark_sor                | 68.6 ms     | 91.0 ms: 1.33x slower  |
| nbody                      | 53.1 ms     | 74.1 ms: 1.40x slower  |
| Geometric mean             | (ref)       | 1.01x slower           |

Benchmark hidden because not significant (5): pylint, bench_thread_pool, django_template, typing_runtime_protocols, sqlglot_v2_normalize

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown