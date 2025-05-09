# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TC-PGO-Ex2             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 216 ms: 1.05x faster   |
| docutils       | 1.68 sec | 1.63 sec: 1.03x faster |
| html5lib       | 40.8 ms  | 36.1 ms: 1.13x faster  |
| sphinx         | 658 ms   | 638 ms: 1.03x faster   |
| Geometric mean | (ref)    | 1.06x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TC-PGO-Ex2            |
|----------------------------|:-------:|:---------------------:|
| async_tree_io              | 423 ms  | 375 ms: 1.13x faster  |
| async_tree_none_tg         | 176 ms  | 159 ms: 1.11x faster  |
| async_tree_io_tg           | 410 ms  | 371 ms: 1.10x faster  |
| async_tree_none            | 187 ms  | 170 ms: 1.10x faster  |
| async_generators           | 226 ms  | 206 ms: 1.10x faster  |
| async_tree_memoization     | 224 ms  | 205 ms: 1.10x faster  |
| coroutines                 | 13.5 ms | 12.4 ms: 1.08x faster |
| async_tree_cpu_io_mixed_tg | 343 ms  | 328 ms: 1.05x faster  |
| async_tree_memoization_tg  | 216 ms  | 209 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 329 ms: 1.03x faster  |
| Geometric mean             | (ref)   | 1.07x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 53.3 ms: 1.39x faster |
| float          | 47.8 ms | 40.2 ms: 1.19x faster |
| pidigits       | 152 ms  | 146 ms: 1.04x faster  |
| Geometric mean | (ref)   | 1.20x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TC-PGO-Ex2            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 74.8 ms: 1.18x faster |
| regex_effbot   | 1.42 ms | 1.40 ms: 1.02x faster |
| regex_dna      | 112 ms  | 115 ms: 1.02x slower  |
| regex_v8       | 13.5 ms | 14.1 ms: 1.04x slower |
| Geometric mean | (ref)   | 1.03x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TC-PGO-Ex2             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 123 us: 1.27x faster   |
| tomli_loads          | 1.47 sec | 1.17 sec: 1.25x faster |
| pickle_pure_python   | 237 us   | 201 us: 1.18x faster   |
| xml_etree_generate   | 58.7 ms  | 51.5 ms: 1.14x faster  |
| xml_etree_process    | 41.5 ms  | 36.7 ms: 1.13x faster  |
| json_dumps           | 7.05 ms  | 6.48 ms: 1.09x faster  |
| xml_etree_iterparse  | 63.7 ms  | 60.4 ms: 1.06x faster  |
| xml_etree_parse      | 91.2 ms  | 89.0 ms: 1.03x faster  |
| json_loads           | 14.7 us  | 14.5 us: 1.02x faster  |
| Geometric mean       | (ref)    | 1.12x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | TC-PGO-Ex2            |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.8 ms | 19.6 ms: 1.01x faster |
| Geometric mean         | (ref)   | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TC-PGO-Ex2            |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 36.3 ms | 30.7 ms: 1.18x faster |
| genshi_text     | 16.5 ms | 14.2 ms: 1.16x faster |
| mako            | 6.86 ms | 6.12 ms: 1.12x faster |
| django_template | 25.1 ms | 23.4 ms: 1.07x faster |
| Geometric mean  | (ref)   | 1.13x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | TC-PGO-Ex2             |
|----------------------------|:--------:|:----------------------:|
| nbody                      | 74.1 ms  | 53.3 ms: 1.39x faster  |
| scimark_sor                | 91.0 ms  | 67.5 ms: 1.35x faster  |
| pathlib                    | 32.1 ms  | 24.3 ms: 1.32x faster  |
| generators                 | 19.3 ms  | 14.8 ms: 1.30x faster  |
| go                         | 88.6 ms  | 68.4 ms: 1.30x faster  |
| scimark_monte_carlo        | 47.1 ms  | 37.0 ms: 1.27x faster  |
| unpickle_pure_python       | 155 us   | 123 us: 1.27x faster   |
| scimark_fft                | 192 ms   | 152 ms: 1.27x faster   |
| hexiom                     | 4.38 ms  | 3.47 ms: 1.26x faster  |
| fannkuch                   | 296 ms   | 236 ms: 1.26x faster   |
| tomli_loads                | 1.47 sec | 1.17 sec: 1.25x faster |
| deltablue                  | 2.29 ms  | 1.85 ms: 1.24x faster  |
| deepcopy_memo              | 21.0 us  | 17.0 us: 1.23x faster  |
| scimark_lu                 | 66.9 ms  | 54.4 ms: 1.23x faster  |
| logging_silent             | 65.2 ns  | 53.3 ns: 1.22x faster  |
| chaos                      | 43.6 ms  | 35.9 ms: 1.22x faster  |
| pyflate                    | 315 ms   | 260 ms: 1.21x faster   |
| sqlglot_v2_parse           | 892 us   | 740 us: 1.21x faster   |
| spectral_norm              | 61.5 ms  | 51.1 ms: 1.20x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.26 ms: 1.20x faster  |
| crypto_pyaes               | 50.0 ms  | 41.6 ms: 1.20x faster  |
| float                      | 47.8 ms  | 40.2 ms: 1.19x faster  |
| deepcopy                   | 190 us   | 160 us: 1.19x faster   |
| genshi_xml                 | 36.3 ms  | 30.7 ms: 1.18x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 933 us: 1.18x faster   |
| regex_compile              | 88.2 ms  | 74.8 ms: 1.18x faster  |
| nqueens                    | 63.6 ms  | 54.0 ms: 1.18x faster  |
| pickle_pure_python         | 237 us   | 201 us: 1.18x faster   |
| mdp                        | 1.64 sec | 1.40 sec: 1.17x faster |
| deepcopy_reduce            | 1.94 us  | 1.66 us: 1.17x faster  |
| pprint_safe_repr           | 558 ms   | 478 ms: 1.17x faster   |
| comprehensions             | 11.3 us  | 9.73 us: 1.16x faster  |
| pprint_pformat             | 1.13 sec | 968 ms: 1.16x faster   |
| genshi_text                | 16.5 ms  | 14.2 ms: 1.16x faster  |
| raytrace                   | 191 ms   | 166 ms: 1.15x faster   |
| xml_etree_generate         | 58.7 ms  | 51.5 ms: 1.14x faster  |
| xml_etree_process          | 41.5 ms  | 36.7 ms: 1.13x faster  |
| html5lib                   | 40.8 ms  | 36.1 ms: 1.13x faster  |
| logging_simple             | 6.53 us  | 5.78 us: 1.13x faster  |
| async_tree_io              | 423 ms   | 375 ms: 1.13x faster   |
| sympy_expand               | 302 ms   | 269 ms: 1.12x faster   |
| mako                       | 6.86 ms  | 6.12 ms: 1.12x faster  |
| sympy_str                  | 176 ms   | 158 ms: 1.12x faster   |
| pycparser                  | 738 ms   | 664 ms: 1.11x faster   |
| logging_format             | 7.03 us  | 6.34 us: 1.11x faster  |
| sympy_integrate            | 13.5 ms  | 12.2 ms: 1.11x faster  |
| async_tree_none_tg         | 176 ms   | 159 ms: 1.11x faster   |
| meteor_contest             | 76.9 ms  | 69.5 ms: 1.11x faster  |
| async_tree_io_tg           | 410 ms   | 371 ms: 1.10x faster   |
| richards                   | 30.7 ms  | 27.8 ms: 1.10x faster  |
| sympy_sum                  | 90.5 ms  | 82.1 ms: 1.10x faster  |
| sqlglot_v2_normalize       | 73.6 ms  | 66.9 ms: 1.10x faster  |
| async_tree_none            | 187 ms   | 170 ms: 1.10x faster   |
| async_generators           | 226 ms   | 206 ms: 1.10x faster   |
| dulwich_log                | 43.4 ms  | 39.5 ms: 1.10x faster  |
| async_tree_memoization     | 224 ms   | 205 ms: 1.10x faster   |
| bpe_tokeniser              | 2.96 sec | 2.71 sec: 1.09x faster |
| richards_super             | 35.1 ms  | 32.2 ms: 1.09x faster  |
| sqlglot_v2_optimize        | 35.0 ms  | 32.2 ms: 1.09x faster  |
| json_dumps                 | 7.05 ms  | 6.48 ms: 1.09x faster  |
| coroutines                 | 13.5 ms  | 12.4 ms: 1.08x faster  |
| telco                      | 4.89 ms  | 4.54 ms: 1.08x faster  |
| django_template            | 25.1 ms  | 23.4 ms: 1.07x faster  |
| typing_runtime_protocols   | 106 us   | 98.9 us: 1.07x faster  |
| xml_etree_iterparse        | 63.7 ms  | 60.4 ms: 1.06x faster  |
| json                       | 3.14 ms  | 2.98 ms: 1.05x faster  |
| thrift                     | 507 us   | 482 us: 1.05x faster   |
| 2to3                       | 227 ms   | 216 ms: 1.05x faster   |
| async_tree_cpu_io_mixed_tg | 343 ms   | 328 ms: 1.05x faster   |
| pidigits                   | 152 ms   | 146 ms: 1.04x faster   |
| async_tree_memoization_tg  | 216 ms   | 209 ms: 1.03x faster   |
| docutils                   | 1.68 sec | 1.63 sec: 1.03x faster |
| shortest_path              | 359 ms   | 348 ms: 1.03x faster   |
| sphinx                     | 658 ms   | 638 ms: 1.03x faster   |
| async_tree_cpu_io_mixed    | 339 ms   | 329 ms: 1.03x faster   |
| connected_components       | 329 ms   | 321 ms: 1.03x faster   |
| xml_etree_parse            | 91.2 ms  | 89.0 ms: 1.03x faster  |
| sqlite_synth               | 1.59 us  | 1.56 us: 1.02x faster  |
| regex_effbot               | 1.42 ms  | 1.40 ms: 1.02x faster  |
| json_loads                 | 14.7 us  | 14.5 us: 1.02x faster  |
| python_startup_no_site     | 19.8 ms  | 19.6 ms: 1.01x faster  |
| create_gc_cycles           | 1.25 ms  | 1.27 ms: 1.01x slower  |
| regex_dna                  | 112 ms   | 115 ms: 1.02x slower   |
| regex_v8                   | 13.5 ms  | 14.1 ms: 1.04x slower  |
| coverage                   | 46.8 ms  | 49.5 ms: 1.06x slower  |
| many_optionals             | 438 us   | 761 us: 1.74x slower   |
| subparsers                 | 16.1 ms  | 44.9 ms: 2.79x slower  |
| Geometric mean             | (ref)    | 1.10x faster           |

Benchmark hidden because not significant (7): bench_thread_pool, k_core, pylint, asyncio_websockets, python_startup, bench_mp_pool, gc_traversal

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown