# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.008x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TC-Ex                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 231 ms: 1.02x slower   |
| docutils       | 1.68 sec | 1.77 sec: 1.05x slower |
| html5lib       | 40.8 ms  | 38.8 ms: 1.05x faster  |
| sphinx         | 658 ms   | 702 ms: 1.07x slower   |
| Geometric mean | (ref)    | 1.02x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TC-Ex                 |
|----------------------------|:-------:|:---------------------:|
| async_tree_io              | 423 ms  | 384 ms: 1.10x faster  |
| coroutines                 | 13.5 ms | 12.3 ms: 1.10x faster |
| async_tree_none            | 187 ms  | 174 ms: 1.07x faster  |
| async_tree_memoization     | 224 ms  | 210 ms: 1.07x faster  |
| async_tree_io_tg           | 410 ms  | 385 ms: 1.06x faster  |
| async_generators           | 226 ms  | 213 ms: 1.06x faster  |
| async_tree_none_tg         | 176 ms  | 167 ms: 1.06x faster  |
| async_tree_memoization_tg  | 216 ms  | 210 ms: 1.02x faster  |
| asyncio_websockets         | 318 ms  | 312 ms: 1.02x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 363 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 339 ms  | 359 ms: 1.06x slower  |
| Geometric mean             | (ref)   | 1.04x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 53.1 ms: 1.40x faster |
| float          | 47.8 ms | 41.4 ms: 1.15x faster |
| pidigits       | 152 ms  | 146 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.19x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 81.9 ms: 1.08x faster |
| regex_dna      | 112 ms  | 121 ms: 1.07x slower  |
| regex_v8       | 13.5 ms | 16.3 ms: 1.20x slower |
| regex_effbot   | 1.42 ms | 1.85 ms: 1.30x slower |
| Geometric mean | (ref)   | 1.12x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TC-Ex                  |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.47 sec | 1.26 sec: 1.16x faster |
| pickle_pure_python   | 237 us   | 223 us: 1.06x faster   |
| unpickle_pure_python | 155 us   | 148 us: 1.05x faster   |
| xml_etree_process    | 41.5 ms  | 44.7 ms: 1.08x slower  |
| xml_etree_generate   | 58.7 ms  | 64.7 ms: 1.10x slower  |
| xml_etree_iterparse  | 63.7 ms  | 70.4 ms: 1.10x slower  |
| json_dumps           | 7.05 ms  | 7.79 ms: 1.10x slower  |
| xml_etree_parse      | 91.2 ms  | 105 ms: 1.15x slower   |
| json_loads           | 14.7 us  | 21.9 us: 1.49x slower  |
| Geometric mean       | (ref)    | 1.07x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TC-Ex                 |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 19.4 ms: 1.02x faster |
| python_startup         | 26.1 ms | 26.4 ms: 1.01x slower |
| Geometric mean         | (ref)   | 1.00x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark      | PGO     | TC-Ex                 |
|----------------|:-------:|:---------------------:|
| genshi_xml     | 36.3 ms | 31.3 ms: 1.16x faster |
| genshi_text    | 16.5 ms | 14.5 ms: 1.14x faster |
| mako           | 6.86 ms | 7.84 ms: 1.14x slower |
| Geometric mean | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | PGO      | TC-Ex                  |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 74.1 ms  | 53.1 ms: 1.40x faster  |
| scimark_sor                | 91.0 ms  | 68.6 ms: 1.33x faster  |
| pathlib                    | 32.1 ms  | 25.1 ms: 1.28x faster  |
| go                         | 88.6 ms  | 70.4 ms: 1.26x faster  |
| scimark_monte_carlo        | 47.1 ms  | 38.9 ms: 1.21x faster  |
| spectral_norm              | 61.5 ms  | 51.1 ms: 1.21x faster  |
| deltablue                  | 2.29 ms  | 1.91 ms: 1.20x faster  |
| generators                 | 19.3 ms  | 16.3 ms: 1.19x faster  |
| fannkuch                   | 296 ms   | 250 ms: 1.18x faster   |
| tomli_loads                | 1.47 sec | 1.26 sec: 1.16x faster |
| genshi_xml                 | 36.3 ms  | 31.3 ms: 1.16x faster  |
| chaos                      | 43.6 ms  | 37.7 ms: 1.16x faster  |
| pyflate                    | 315 ms   | 274 ms: 1.15x faster   |
| float                      | 47.8 ms  | 41.4 ms: 1.15x faster  |
| scimark_fft                | 192 ms   | 169 ms: 1.14x faster   |
| genshi_text                | 16.5 ms  | 14.5 ms: 1.14x faster  |
| mdp                        | 1.64 sec | 1.44 sec: 1.13x faster |
| raytrace                   | 191 ms   | 169 ms: 1.13x faster   |
| hexiom                     | 4.38 ms  | 3.92 ms: 1.12x faster  |
| sqlglot_v2_parse           | 892 us   | 798 us: 1.12x faster   |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.47 ms: 1.10x faster  |
| async_tree_io              | 423 ms   | 384 ms: 1.10x faster   |
| coroutines                 | 13.5 ms  | 12.3 ms: 1.10x faster  |
| pprint_safe_repr           | 558 ms   | 510 ms: 1.09x faster   |
| deepcopy_memo              | 21.0 us  | 19.3 us: 1.09x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 1.01 ms: 1.09x faster  |
| pprint_pformat             | 1.13 sec | 1.04 sec: 1.09x faster |
| regex_compile              | 88.2 ms  | 81.9 ms: 1.08x faster  |
| async_tree_none            | 187 ms   | 174 ms: 1.07x faster   |
| async_tree_memoization     | 224 ms   | 210 ms: 1.07x faster   |
| logging_silent             | 65.2 ns  | 61.1 ns: 1.07x faster  |
| nqueens                    | 63.6 ms  | 59.6 ms: 1.07x faster  |
| pickle_pure_python         | 237 us   | 223 us: 1.06x faster   |
| async_tree_io_tg           | 410 ms   | 385 ms: 1.06x faster   |
| async_generators           | 226 ms   | 213 ms: 1.06x faster   |
| connected_components       | 329 ms   | 311 ms: 1.06x faster   |
| async_tree_none_tg         | 176 ms   | 167 ms: 1.06x faster   |
| html5lib                   | 40.8 ms  | 38.8 ms: 1.05x faster  |
| deepcopy                   | 190 us   | 180 us: 1.05x faster   |
| unpickle_pure_python       | 155 us   | 148 us: 1.05x faster   |
| logging_format             | 7.03 us  | 6.70 us: 1.05x faster  |
| pidigits                   | 152 ms   | 146 ms: 1.05x faster   |
| logging_simple             | 6.53 us  | 6.25 us: 1.04x faster  |
| scimark_lu                 | 66.9 ms  | 64.2 ms: 1.04x faster  |
| crypto_pyaes               | 50.0 ms  | 48.0 ms: 1.04x faster  |
| shortest_path              | 359 ms   | 347 ms: 1.04x faster   |
| pycparser                  | 738 ms   | 713 ms: 1.04x faster   |
| meteor_contest             | 76.9 ms  | 74.5 ms: 1.03x faster  |
| async_tree_memoization_tg  | 216 ms   | 210 ms: 1.02x faster   |
| dulwich_log                | 43.4 ms  | 42.3 ms: 1.02x faster  |
| deepcopy_reduce            | 1.94 us  | 1.90 us: 1.02x faster  |
| python_startup_no_site     | 19.8 ms  | 19.4 ms: 1.02x faster  |
| asyncio_websockets         | 318 ms   | 312 ms: 1.02x faster   |
| k_core                     | 1.73 sec | 1.71 sec: 1.01x faster |
| sympy_integrate            | 13.5 ms  | 13.4 ms: 1.01x faster  |
| comprehensions             | 11.3 us  | 11.3 us: 1.00x faster  |
| sympy_str                  | 176 ms   | 177 ms: 1.01x slower   |
| richards                   | 30.7 ms  | 30.9 ms: 1.01x slower  |
| sympy_expand               | 302 ms   | 304 ms: 1.01x slower   |
| sympy_sum                  | 90.5 ms  | 91.4 ms: 1.01x slower  |
| python_startup             | 26.1 ms  | 26.4 ms: 1.01x slower  |
| 2to3                       | 227 ms   | 231 ms: 1.02x slower   |
| bpe_tokeniser              | 2.96 sec | 3.01 sec: 1.02x slower |
| richards_super             | 35.1 ms  | 35.8 ms: 1.02x slower  |
| sqlglot_v2_optimize        | 35.0 ms  | 36.1 ms: 1.03x slower  |
| docutils                   | 1.68 sec | 1.77 sec: 1.05x slower |
| sqlite_synth               | 1.59 us  | 1.68 us: 1.05x slower  |
| bench_mp_pool              | 88.7 ms  | 93.6 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 363 ms: 1.06x slower   |
| async_tree_cpu_io_mixed    | 339 ms   | 359 ms: 1.06x slower   |
| sphinx                     | 658 ms   | 702 ms: 1.07x slower   |
| create_gc_cycles           | 1.25 ms  | 1.34 ms: 1.07x slower  |
| regex_dna                  | 112 ms   | 121 ms: 1.07x slower   |
| telco                      | 4.89 ms  | 5.26 ms: 1.07x slower  |
| xml_etree_process          | 41.5 ms  | 44.7 ms: 1.08x slower  |
| thrift                     | 507 us   | 551 us: 1.09x slower   |
| xml_etree_generate         | 58.7 ms  | 64.7 ms: 1.10x slower  |
| xml_etree_iterparse        | 63.7 ms  | 70.4 ms: 1.10x slower  |
| json_dumps                 | 7.05 ms  | 7.79 ms: 1.10x slower  |
| mako                       | 6.86 ms  | 7.84 ms: 1.14x slower  |
| xml_etree_parse            | 91.2 ms  | 105 ms: 1.15x slower   |
| coverage                   | 46.8 ms  | 55.4 ms: 1.18x slower  |
| regex_v8                   | 13.5 ms  | 16.3 ms: 1.20x slower  |
| json                       | 3.14 ms  | 3.78 ms: 1.20x slower  |
| regex_effbot               | 1.42 ms  | 1.85 ms: 1.30x slower  |
| gc_traversal               | 2.06 ms  | 2.83 ms: 1.38x slower  |
| json_loads                 | 14.7 us  | 21.9 us: 1.49x slower  |
| many_optionals             | 438 us   | 762 us: 1.74x slower   |
| subparsers                 | 16.1 ms  | 44.5 ms: 2.76x slower  |
| Geometric mean             | (ref)    | 1.01x faster           |

Benchmark hidden because not significant (5): sqlglot_v2_normalize, typing_runtime_protocols, django_template, bench_thread_pool, pylint

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.52% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown