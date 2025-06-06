# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TCO-PGO-Ex3            |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 212 ms: 1.07x faster   |
| docutils       | 1.68 sec | 1.67 sec: 1.01x faster |
| html5lib       | 40.8 ms  | 37.9 ms: 1.07x faster  |
| sphinx         | 658 ms   | 645 ms: 1.02x faster   |
| Geometric mean | (ref)    | 1.04x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TCO-PGO-Ex3           |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.5 ms | 11.9 ms: 1.13x faster |
| async_generators           | 226 ms  | 202 ms: 1.12x faster  |
| async_tree_none_tg         | 176 ms  | 159 ms: 1.11x faster  |
| async_tree_io              | 423 ms  | 384 ms: 1.10x faster  |
| async_tree_none            | 187 ms  | 170 ms: 1.10x faster  |
| async_tree_memoization     | 224 ms  | 206 ms: 1.09x faster  |
| async_tree_io_tg           | 410 ms  | 377 ms: 1.09x faster  |
| asyncio_websockets         | 318 ms  | 301 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 329 ms: 1.04x faster  |
| async_tree_memoization_tg  | 216 ms  | 208 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 330 ms: 1.03x faster  |
| Geometric mean             | (ref)   | 1.08x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 55.2 ms: 1.34x faster |
| float          | 47.8 ms | 41.9 ms: 1.14x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.17x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TCO-PGO-Ex3           |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 78.1 ms: 1.13x faster |
| regex_effbot   | 1.42 ms | 1.46 ms: 1.03x slower |
| regex_dna      | 112 ms  | 120 ms: 1.07x slower  |
| Geometric mean | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TCO-PGO-Ex3            |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.47 sec | 1.18 sec: 1.25x faster |
| unpickle_pure_python | 155 us   | 127 us: 1.22x faster   |
| pickle_pure_python   | 237 us   | 199 us: 1.19x faster   |
| xml_etree_process    | 41.5 ms  | 37.0 ms: 1.12x faster  |
| xml_etree_generate   | 58.7 ms  | 53.6 ms: 1.09x faster  |
| json_dumps           | 7.05 ms  | 6.55 ms: 1.08x faster  |
| xml_etree_iterparse  | 63.7 ms  | 61.2 ms: 1.04x faster  |
| xml_etree_parse      | 91.2 ms  | 89.3 ms: 1.02x faster  |
| Geometric mean       | (ref)    | 1.11x faster           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TCO-PGO-Ex3           |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 18.7 ms: 1.06x faster |
| python_startup         | 26.1 ms | 24.7 ms: 1.06x faster |
| Geometric mean         | (ref)   | 1.06x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TCO-PGO-Ex3           |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 14.3 ms: 1.16x faster |
| genshi_xml      | 36.3 ms | 32.8 ms: 1.11x faster |
| django_template | 25.1 ms | 22.9 ms: 1.10x faster |
| mako            | 6.86 ms | 6.28 ms: 1.09x faster |
| Geometric mean  | (ref)   | 1.11x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | TCO-PGO-Ex3            |
|----------------------------|:--------:|:----------------------:|
| scimark_sor                | 91.0 ms  | 61.1 ms: 1.49x faster  |
| nbody                      | 74.1 ms  | 55.2 ms: 1.34x faster  |
| pathlib                    | 32.1 ms  | 24.1 ms: 1.33x faster  |
| fannkuch                   | 296 ms   | 223 ms: 1.33x faster   |
| logging_silent             | 65.2 ns  | 49.4 ns: 1.32x faster  |
| scimark_lu                 | 66.9 ms  | 50.9 ms: 1.31x faster  |
| scimark_monte_carlo        | 47.1 ms  | 36.0 ms: 1.31x faster  |
| deepcopy_memo              | 21.0 us  | 16.6 us: 1.27x faster  |
| go                         | 88.6 ms  | 70.9 ms: 1.25x faster  |
| scimark_fft                | 192 ms   | 154 ms: 1.25x faster   |
| tomli_loads                | 1.47 sec | 1.18 sec: 1.25x faster |
| spectral_norm              | 61.5 ms  | 49.4 ms: 1.25x faster  |
| hexiom                     | 4.38 ms  | 3.54 ms: 1.24x faster  |
| unpickle_pure_python       | 155 us   | 127 us: 1.22x faster   |
| deltablue                  | 2.29 ms  | 1.88 ms: 1.22x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.27 ms: 1.20x faster  |
| raytrace                   | 191 ms   | 160 ms: 1.19x faster   |
| pickle_pure_python         | 237 us   | 199 us: 1.19x faster   |
| pprint_safe_repr           | 558 ms   | 470 ms: 1.19x faster   |
| chaos                      | 43.6 ms  | 36.9 ms: 1.18x faster  |
| pyflate                    | 315 ms   | 268 ms: 1.18x faster   |
| generators                 | 19.3 ms  | 16.5 ms: 1.17x faster  |
| nqueens                    | 63.6 ms  | 54.4 ms: 1.17x faster  |
| sqlglot_v2_parse           | 892 us   | 766 us: 1.16x faster   |
| pprint_pformat             | 1.13 sec | 967 ms: 1.16x faster   |
| genshi_text                | 16.5 ms  | 14.3 ms: 1.16x faster  |
| comprehensions             | 11.3 us  | 9.87 us: 1.15x faster  |
| deepcopy_reduce            | 1.94 us  | 1.70 us: 1.14x faster  |
| float                      | 47.8 ms  | 41.9 ms: 1.14x faster  |
| deepcopy                   | 190 us   | 167 us: 1.14x faster   |
| sqlglot_v2_transpile       | 1.10 ms  | 970 us: 1.14x faster   |
| coroutines                 | 13.5 ms  | 11.9 ms: 1.13x faster  |
| regex_compile              | 88.2 ms  | 78.1 ms: 1.13x faster  |
| xml_etree_process          | 41.5 ms  | 37.0 ms: 1.12x faster  |
| async_generators           | 226 ms   | 202 ms: 1.12x faster   |
| async_tree_none_tg         | 176 ms   | 159 ms: 1.11x faster   |
| genshi_xml                 | 36.3 ms  | 32.8 ms: 1.11x faster  |
| async_tree_io              | 423 ms   | 384 ms: 1.10x faster   |
| django_template            | 25.1 ms  | 22.9 ms: 1.10x faster  |
| async_tree_none            | 187 ms   | 170 ms: 1.10x faster   |
| xml_etree_generate         | 58.7 ms  | 53.6 ms: 1.09x faster  |
| meteor_contest             | 76.9 ms  | 70.2 ms: 1.09x faster  |
| logging_simple             | 6.53 us  | 5.97 us: 1.09x faster  |
| mako                       | 6.86 ms  | 6.28 ms: 1.09x faster  |
| async_tree_memoization     | 224 ms   | 206 ms: 1.09x faster   |
| bpe_tokeniser              | 2.96 sec | 2.72 sec: 1.09x faster |
| async_tree_io_tg           | 410 ms   | 377 ms: 1.09x faster   |
| logging_format             | 7.03 us  | 6.50 us: 1.08x faster  |
| dulwich_log                | 43.4 ms  | 40.2 ms: 1.08x faster  |
| pycparser                  | 738 ms   | 686 ms: 1.08x faster   |
| json_dumps                 | 7.05 ms  | 6.55 ms: 1.08x faster  |
| html5lib                   | 40.8 ms  | 37.9 ms: 1.07x faster  |
| typing_runtime_protocols   | 106 us   | 98.8 us: 1.07x faster  |
| 2to3                       | 227 ms   | 212 ms: 1.07x faster   |
| sympy_str                  | 176 ms   | 164 ms: 1.07x faster   |
| sympy_expand               | 302 ms   | 282 ms: 1.07x faster   |
| telco                      | 4.89 ms  | 4.57 ms: 1.07x faster  |
| richards                   | 30.7 ms  | 28.7 ms: 1.07x faster  |
| richards_super             | 35.1 ms  | 33.1 ms: 1.06x faster  |
| sqlglot_v2_normalize       | 73.6 ms  | 69.3 ms: 1.06x faster  |
| sqlglot_v2_optimize        | 35.0 ms  | 33.0 ms: 1.06x faster  |
| python_startup_no_site     | 19.8 ms  | 18.7 ms: 1.06x faster  |
| asyncio_websockets         | 318 ms   | 301 ms: 1.06x faster   |
| json                       | 3.14 ms  | 2.97 ms: 1.06x faster  |
| python_startup             | 26.1 ms  | 24.7 ms: 1.06x faster  |
| crypto_pyaes               | 50.0 ms  | 47.4 ms: 1.05x faster  |
| sympy_integrate            | 13.5 ms  | 12.8 ms: 1.05x faster  |
| thrift                     | 507 us   | 482 us: 1.05x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| sympy_sum                  | 90.5 ms  | 86.3 ms: 1.05x faster  |
| xml_etree_iterparse        | 63.7 ms  | 61.2 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 329 ms: 1.04x faster   |
| async_tree_memoization_tg  | 216 ms   | 208 ms: 1.03x faster   |
| async_tree_cpu_io_mixed    | 339 ms   | 330 ms: 1.03x faster   |
| xml_etree_parse            | 91.2 ms  | 89.3 ms: 1.02x faster  |
| sphinx                     | 658 ms   | 645 ms: 1.02x faster   |
| shortest_path              | 359 ms   | 353 ms: 1.02x faster   |
| sqlite_synth               | 1.59 us  | 1.56 us: 1.02x faster  |
| mdp                        | 1.64 sec | 1.62 sec: 1.01x faster |
| connected_components       | 329 ms   | 326 ms: 1.01x faster   |
| docutils                   | 1.68 sec | 1.67 sec: 1.01x faster |
| create_gc_cycles           | 1.25 ms  | 1.27 ms: 1.02x slower  |
| gc_traversal               | 2.06 ms  | 2.11 ms: 1.02x slower  |
| regex_effbot               | 1.42 ms  | 1.46 ms: 1.03x slower  |
| coverage                   | 46.8 ms  | 48.2 ms: 1.03x slower  |
| regex_dna                  | 112 ms   | 120 ms: 1.07x slower   |
| many_optionals             | 438 us   | 665 us: 1.52x slower   |
| subparsers                 | 16.1 ms  | 40.7 ms: 2.53x slower  |
| Geometric mean             | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (4): regex_v8, k_core, pylint, json_loads
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown