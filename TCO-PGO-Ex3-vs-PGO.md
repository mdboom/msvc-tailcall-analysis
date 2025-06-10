# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 215 ms: 1.06x faster   |
| docutils       | 1.68 sec | 1.66 sec: 1.01x faster |
| html5lib       | 40.8 ms  | 37.8 ms: 1.08x faster  |
| sphinx         | 658 ms   | 641 ms: 1.03x faster   |
| Geometric mean | (ref)    | 1.04x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.5 ms | 12.0 ms: 1.13x faster |
| async_generators           | 226 ms  | 201 ms: 1.13x faster  |
| async_tree_io              | 423 ms  | 382 ms: 1.11x faster  |
| async_tree_none            | 187 ms  | 170 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms  | 161 ms: 1.10x faster  |
| async_tree_memoization     | 224 ms  | 205 ms: 1.09x faster  |
| async_tree_io_tg           | 410 ms  | 377 ms: 1.09x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 330 ms: 1.04x faster  |
| async_tree_memoization_tg  | 216 ms  | 208 ms: 1.04x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 330 ms: 1.03x faster  |
| asyncio_websockets         | 318 ms  | 313 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.08x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 55.6 ms: 1.33x faster |
| float          | 47.8 ms | 42.0 ms: 1.14x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.17x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 79.4 ms: 1.11x faster |
| regex_effbot   | 1.42 ms | 1.47 ms: 1.03x slower |
| regex_v8       | 13.5 ms | 14.2 ms: 1.05x slower |
| regex_dna      | 112 ms  | 120 ms: 1.07x slower  |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 124 us: 1.25x faster   |
| tomli_loads          | 1.47 sec | 1.17 sec: 1.25x faster |
| pickle_pure_python   | 237 us   | 199 us: 1.19x faster   |
| xml_etree_process    | 41.5 ms  | 36.8 ms: 1.13x faster  |
| xml_etree_generate   | 58.7 ms  | 53.1 ms: 1.11x faster  |
| json_dumps           | 7.05 ms  | 6.40 ms: 1.10x faster  |
| xml_etree_iterparse  | 63.7 ms  | 61.2 ms: 1.04x faster  |
| xml_etree_parse      | 91.2 ms  | 89.4 ms: 1.02x faster  |
| json_loads           | 14.7 us  | 14.5 us: 1.02x faster  |
| Geometric mean       | (ref)    | 1.12x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 18.6 ms: 1.07x faster |
| python_startup         | 26.1 ms | 24.7 ms: 1.05x faster |
| Geometric mean         | (ref)   | 1.06x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 14.3 ms: 1.15x faster |
| genshi_xml      | 36.3 ms | 32.3 ms: 1.12x faster |
| mako            | 6.86 ms | 6.25 ms: 1.10x faster |
| django_template | 25.1 ms | 23.6 ms: 1.07x faster |
| Geometric mean  | (ref)   | 1.11x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| scimark_sor                | 91.0 ms  | 60.5 ms: 1.50x faster  |
| nbody                      | 74.1 ms  | 55.6 ms: 1.33x faster  |
| scimark_lu                 | 66.9 ms  | 50.3 ms: 1.33x faster  |
| pathlib                    | 32.1 ms  | 24.2 ms: 1.33x faster  |
| scimark_monte_carlo        | 47.1 ms  | 35.6 ms: 1.32x faster  |
| fannkuch                   | 296 ms   | 225 ms: 1.32x faster   |
| logging_silent             | 65.2 ns  | 49.7 ns: 1.31x faster  |
| go                         | 88.6 ms  | 70.5 ms: 1.26x faster  |
| hexiom                     | 4.38 ms  | 3.49 ms: 1.26x faster  |
| scimark_fft                | 192 ms   | 153 ms: 1.25x faster   |
| unpickle_pure_python       | 155 us   | 124 us: 1.25x faster   |
| tomli_loads                | 1.47 sec | 1.17 sec: 1.25x faster |
| deepcopy_memo              | 21.0 us  | 16.8 us: 1.25x faster  |
| spectral_norm              | 61.5 ms  | 49.4 ms: 1.25x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.21 ms: 1.23x faster  |
| chaos                      | 43.6 ms  | 35.4 ms: 1.23x faster  |
| deltablue                  | 2.29 ms  | 1.88 ms: 1.22x faster  |
| pyflate                    | 315 ms   | 264 ms: 1.19x faster   |
| pickle_pure_python         | 237 us   | 199 us: 1.19x faster   |
| raytrace                   | 191 ms   | 162 ms: 1.18x faster   |
| pprint_pformat             | 1.13 sec | 956 ms: 1.18x faster   |
| pprint_safe_repr           | 558 ms   | 474 ms: 1.18x faster   |
| generators                 | 19.3 ms  | 16.5 ms: 1.17x faster  |
| comprehensions             | 11.3 us  | 9.76 us: 1.16x faster  |
| deepcopy_reduce            | 1.94 us  | 1.68 us: 1.16x faster  |
| genshi_text                | 16.5 ms  | 14.3 ms: 1.15x faster  |
| nqueens                    | 63.6 ms  | 55.2 ms: 1.15x faster  |
| mdp                        | 1.64 sec | 1.43 sec: 1.15x faster |
| sqlglot_v2_parse           | 892 us   | 781 us: 1.14x faster   |
| crypto_pyaes               | 50.0 ms  | 43.9 ms: 1.14x faster  |
| float                      | 47.8 ms  | 42.0 ms: 1.14x faster  |
| deepcopy                   | 190 us   | 167 us: 1.13x faster   |
| xml_etree_process          | 41.5 ms  | 36.8 ms: 1.13x faster  |
| coroutines                 | 13.5 ms  | 12.0 ms: 1.13x faster  |
| async_generators           | 226 ms   | 201 ms: 1.13x faster   |
| genshi_xml                 | 36.3 ms  | 32.3 ms: 1.12x faster  |
| logging_simple             | 6.53 us  | 5.87 us: 1.11x faster  |
| regex_compile              | 88.2 ms  | 79.4 ms: 1.11x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 993 us: 1.11x faster   |
| async_tree_io              | 423 ms   | 382 ms: 1.11x faster   |
| xml_etree_generate         | 58.7 ms  | 53.1 ms: 1.11x faster  |
| json_dumps                 | 7.05 ms  | 6.40 ms: 1.10x faster  |
| async_tree_none            | 187 ms   | 170 ms: 1.10x faster   |
| mako                       | 6.86 ms  | 6.25 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms   | 161 ms: 1.10x faster   |
| logging_format             | 7.03 us  | 6.42 us: 1.10x faster  |
| async_tree_memoization     | 224 ms   | 205 ms: 1.09x faster   |
| bpe_tokeniser              | 2.96 sec | 2.72 sec: 1.09x faster |
| async_tree_io_tg           | 410 ms   | 377 ms: 1.09x faster   |
| typing_runtime_protocols   | 106 us   | 97.8 us: 1.08x faster  |
| meteor_contest             | 76.9 ms  | 70.9 ms: 1.08x faster  |
| html5lib                   | 40.8 ms  | 37.8 ms: 1.08x faster  |
| dulwich_log                | 43.4 ms  | 40.3 ms: 1.08x faster  |
| pycparser                  | 738 ms   | 689 ms: 1.07x faster   |
| sympy_expand               | 302 ms   | 283 ms: 1.07x faster   |
| sqlglot_v2_normalize       | 73.6 ms  | 69.0 ms: 1.07x faster  |
| python_startup_no_site     | 19.8 ms  | 18.6 ms: 1.07x faster  |
| django_template            | 25.1 ms  | 23.6 ms: 1.07x faster  |
| telco                      | 4.89 ms  | 4.59 ms: 1.07x faster  |
| sqlglot_v2_optimize        | 35.0 ms  | 32.9 ms: 1.06x faster  |
| sympy_sum                  | 90.5 ms  | 85.2 ms: 1.06x faster  |
| 2to3                       | 227 ms   | 215 ms: 1.06x faster   |
| sympy_integrate            | 13.5 ms  | 12.8 ms: 1.06x faster  |
| python_startup             | 26.1 ms  | 24.7 ms: 1.05x faster  |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| richards                   | 30.7 ms  | 29.4 ms: 1.05x faster  |
| richards_super             | 35.1 ms  | 33.7 ms: 1.04x faster  |
| xml_etree_iterparse        | 63.7 ms  | 61.2 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 330 ms: 1.04x faster   |
| async_tree_memoization_tg  | 216 ms   | 208 ms: 1.04x faster   |
| thrift                     | 507 us   | 491 us: 1.03x faster   |
| json                       | 3.14 ms  | 3.04 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 339 ms   | 330 ms: 1.03x faster   |
| sphinx                     | 658 ms   | 641 ms: 1.03x faster   |
| shortest_path              | 359 ms   | 352 ms: 1.02x faster   |
| xml_etree_parse            | 91.2 ms  | 89.4 ms: 1.02x faster  |
| sqlite_synth               | 1.59 us  | 1.56 us: 1.02x faster  |
| sympy_str                  | 176 ms   | 173 ms: 1.02x faster   |
| asyncio_websockets         | 318 ms   | 313 ms: 1.02x faster   |
| json_loads                 | 14.7 us  | 14.5 us: 1.02x faster  |
| k_core                     | 1.73 sec | 1.70 sec: 1.02x faster |
| docutils                   | 1.68 sec | 1.66 sec: 1.01x faster |
| connected_components       | 329 ms   | 325 ms: 1.01x faster   |
| coverage                   | 46.8 ms  | 47.5 ms: 1.02x slower  |
| gc_traversal               | 2.06 ms  | 2.12 ms: 1.03x slower  |
| regex_effbot               | 1.42 ms  | 1.47 ms: 1.03x slower  |
| regex_v8                   | 13.5 ms  | 14.2 ms: 1.05x slower  |
| regex_dna                  | 112 ms   | 120 ms: 1.07x slower   |
| many_optionals             | 438 us   | 685 us: 1.56x slower   |
| subparsers                 | 16.1 ms  | 41.4 ms: 2.57x slower  |
| Geometric mean             | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (2): pylint, create_gc_cycles
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.090x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown