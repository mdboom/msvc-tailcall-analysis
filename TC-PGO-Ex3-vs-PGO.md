# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.173x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 204 ms: 1.11x faster   |
| docutils       | 1.68 sec | 1.58 sec: 1.06x faster |
| html5lib       | 40.8 ms  | 35.5 ms: 1.15x faster  |
| sphinx         | 658 ms   | 615 ms: 1.07x faster   |
| Geometric mean | (ref)    | 1.10x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.5 ms | 10.8 ms: 1.25x faster |
| async_tree_io              | 423 ms  | 353 ms: 1.20x faster  |
| async_tree_none            | 187 ms  | 157 ms: 1.19x faster  |
| async_tree_none_tg         | 176 ms  | 150 ms: 1.18x faster  |
| async_tree_io_tg           | 410 ms  | 356 ms: 1.15x faster  |
| async_tree_memoization     | 224 ms  | 196 ms: 1.14x faster  |
| async_generators           | 226 ms  | 199 ms: 1.14x faster  |
| async_tree_memoization_tg  | 216 ms  | 201 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 325 ms: 1.05x faster  |
| asyncio_websockets         | 318 ms  | 304 ms: 1.05x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 327 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.13x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 45.7 ms: 1.62x faster |
| float          | 47.8 ms | 37.1 ms: 1.29x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.30x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 70.7 ms: 1.25x faster |
| regex_effbot   | 1.42 ms | 1.45 ms: 1.02x slower |
| regex_v8       | 13.5 ms | 13.9 ms: 1.03x slower |
| regex_dna      | 112 ms  | 121 ms: 1.07x slower  |
| Geometric mean | (ref)   | 1.03x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| tomli_loads          | 1.47 sec | 1.03 sec: 1.43x faster |
| unpickle_pure_python | 155 us   | 110 us: 1.42x faster   |
| pickle_pure_python   | 237 us   | 184 us: 1.29x faster   |
| xml_etree_process    | 41.5 ms  | 33.8 ms: 1.23x faster  |
| xml_etree_generate   | 58.7 ms  | 49.4 ms: 1.19x faster  |
| json_dumps           | 7.05 ms  | 6.19 ms: 1.14x faster  |
| xml_etree_iterparse  | 63.7 ms  | 59.5 ms: 1.07x faster  |
| xml_etree_parse      | 91.2 ms  | 89.4 ms: 1.02x faster  |
| Geometric mean       | (ref)    | 1.19x faster           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 18.7 ms: 1.06x faster |
| python_startup         | 26.1 ms | 24.7 ms: 1.05x faster |
| Geometric mean         | (ref)   | 1.06x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 12.3 ms: 1.34x faster |
| genshi_xml      | 36.3 ms | 29.5 ms: 1.23x faster |
| django_template | 25.1 ms | 20.9 ms: 1.20x faster |
| mako            | 6.86 ms | 5.80 ms: 1.18x faster |
| Geometric mean  | (ref)   | 1.24x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| scimark_sor                | 91.0 ms  | 51.1 ms: 1.78x faster  |
| nbody                      | 74.1 ms  | 45.7 ms: 1.62x faster  |
| scimark_lu                 | 66.9 ms  | 44.3 ms: 1.51x faster  |
| spectral_norm              | 61.5 ms  | 40.9 ms: 1.50x faster  |
| scimark_monte_carlo        | 47.1 ms  | 31.5 ms: 1.50x faster  |
| logging_silent             | 65.2 ns  | 44.1 ns: 1.48x faster  |
| hexiom                     | 4.38 ms  | 3.00 ms: 1.46x faster  |
| fannkuch                   | 296 ms   | 203 ms: 1.46x faster   |
| go                         | 88.6 ms  | 61.0 ms: 1.45x faster  |
| deepcopy_memo              | 21.0 us  | 14.7 us: 1.43x faster  |
| tomli_loads                | 1.47 sec | 1.03 sec: 1.43x faster |
| unpickle_pure_python       | 155 us   | 110 us: 1.42x faster   |
| deltablue                  | 2.29 ms  | 1.64 ms: 1.40x faster  |
| chaos                      | 43.6 ms  | 31.3 ms: 1.40x faster  |
| scimark_fft                | 192 ms   | 140 ms: 1.37x faster   |
| pathlib                    | 32.1 ms  | 23.6 ms: 1.36x faster  |
| generators                 | 19.3 ms  | 14.2 ms: 1.36x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.02 ms: 1.35x faster  |
| genshi_text                | 16.5 ms  | 12.3 ms: 1.34x faster  |
| pyflate                    | 315 ms   | 236 ms: 1.34x faster   |
| pprint_pformat             | 1.13 sec | 853 ms: 1.32x faster   |
| raytrace                   | 191 ms   | 145 ms: 1.31x faster   |
| comprehensions             | 11.3 us  | 8.65 us: 1.31x faster  |
| pprint_safe_repr           | 558 ms   | 429 ms: 1.30x faster   |
| deepcopy                   | 190 us   | 147 us: 1.29x faster   |
| float                      | 47.8 ms  | 37.1 ms: 1.29x faster  |
| pickle_pure_python         | 237 us   | 184 us: 1.29x faster   |
| sqlglot_v2_parse           | 892 us   | 695 us: 1.28x faster   |
| deepcopy_reduce            | 1.94 us  | 1.51 us: 1.28x faster  |
| nqueens                    | 63.6 ms  | 49.7 ms: 1.28x faster  |
| coroutines                 | 13.5 ms  | 10.8 ms: 1.25x faster  |
| regex_compile              | 88.2 ms  | 70.7 ms: 1.25x faster  |
| crypto_pyaes               | 50.0 ms  | 40.4 ms: 1.24x faster  |
| genshi_xml                 | 36.3 ms  | 29.5 ms: 1.23x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 894 us: 1.23x faster   |
| xml_etree_process          | 41.5 ms  | 33.8 ms: 1.23x faster  |
| logging_simple             | 6.53 us  | 5.42 us: 1.21x faster  |
| richards                   | 30.7 ms  | 25.5 ms: 1.21x faster  |
| django_template            | 25.1 ms  | 20.9 ms: 1.20x faster  |
| async_tree_io              | 423 ms   | 353 ms: 1.20x faster   |
| richards_super             | 35.1 ms  | 29.4 ms: 1.19x faster  |
| logging_format             | 7.03 us  | 5.90 us: 1.19x faster  |
| xml_etree_generate         | 58.7 ms  | 49.4 ms: 1.19x faster  |
| async_tree_none            | 187 ms   | 157 ms: 1.19x faster   |
| mako                       | 6.86 ms  | 5.80 ms: 1.18x faster  |
| typing_runtime_protocols   | 106 us   | 89.7 us: 1.18x faster  |
| sqlglot_v2_normalize       | 73.6 ms  | 62.6 ms: 1.18x faster  |
| async_tree_none_tg         | 176 ms   | 150 ms: 1.18x faster   |
| bpe_tokeniser              | 2.96 sec | 2.52 sec: 1.17x faster |
| mdp                        | 1.64 sec | 1.41 sec: 1.17x faster |
| meteor_contest             | 76.9 ms  | 66.6 ms: 1.15x faster  |
| async_tree_io_tg           | 410 ms   | 356 ms: 1.15x faster   |
| sympy_expand               | 302 ms   | 263 ms: 1.15x faster   |
| html5lib                   | 40.8 ms  | 35.5 ms: 1.15x faster  |
| pycparser                  | 738 ms   | 642 ms: 1.15x faster   |
| sqlglot_v2_optimize        | 35.0 ms  | 30.5 ms: 1.15x faster  |
| sympy_str                  | 176 ms   | 153 ms: 1.15x faster   |
| async_tree_memoization     | 224 ms   | 196 ms: 1.14x faster   |
| async_generators           | 226 ms   | 199 ms: 1.14x faster   |
| json_dumps                 | 7.05 ms  | 6.19 ms: 1.14x faster  |
| sympy_integrate            | 13.5 ms  | 12.0 ms: 1.13x faster  |
| sympy_sum                  | 90.5 ms  | 80.7 ms: 1.12x faster  |
| 2to3                       | 227 ms   | 204 ms: 1.11x faster   |
| dulwich_log                | 43.4 ms  | 39.1 ms: 1.11x faster  |
| telco                      | 4.89 ms  | 4.45 ms: 1.10x faster  |
| thrift                     | 507 us   | 461 us: 1.10x faster   |
| async_tree_memoization_tg  | 216 ms   | 201 ms: 1.07x faster   |
| xml_etree_iterparse        | 63.7 ms  | 59.5 ms: 1.07x faster  |
| sphinx                     | 658 ms   | 615 ms: 1.07x faster   |
| docutils                   | 1.68 sec | 1.58 sec: 1.06x faster |
| json                       | 3.14 ms  | 2.95 ms: 1.06x faster  |
| python_startup_no_site     | 19.8 ms  | 18.7 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 325 ms: 1.05x faster   |
| python_startup             | 26.1 ms  | 24.7 ms: 1.05x faster  |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| asyncio_websockets         | 318 ms   | 304 ms: 1.05x faster   |
| pylint                     | 201 ms   | 193 ms: 1.04x faster   |
| async_tree_cpu_io_mixed    | 339 ms   | 327 ms: 1.04x faster   |
| k_core                     | 1.73 sec | 1.67 sec: 1.04x faster |
| shortest_path              | 359 ms   | 347 ms: 1.04x faster   |
| connected_components       | 329 ms   | 320 ms: 1.03x faster   |
| xml_etree_parse            | 91.2 ms  | 89.4 ms: 1.02x faster  |
| sqlite_synth               | 1.59 us  | 1.56 us: 1.02x faster  |
| coverage                   | 46.8 ms  | 46.2 ms: 1.01x faster  |
| create_gc_cycles           | 1.25 ms  | 1.26 ms: 1.01x slower  |
| gc_traversal               | 2.06 ms  | 2.09 ms: 1.02x slower  |
| regex_effbot               | 1.42 ms  | 1.45 ms: 1.02x slower  |
| regex_v8                   | 13.5 ms  | 13.9 ms: 1.03x slower  |
| regex_dna                  | 112 ms   | 121 ms: 1.07x slower   |
| many_optionals             | 438 us   | 659 us: 1.50x slower   |
| subparsers                 | 16.1 ms  | 40.6 ms: 2.52x slower  |
| Geometric mean             | (ref)    | 1.18x faster           |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.173x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown