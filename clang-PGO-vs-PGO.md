# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.188x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 204 ms: 1.12x faster   |
| docutils       | 1.68 sec | 1.55 sec: 1.09x faster |
| html5lib       | 40.8 ms  | 35.2 ms: 1.16x faster  |
| sphinx         | 658 ms   | 599 ms: 1.10x faster   |
| Geometric mean | (ref)    | 1.11x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.5 ms | 11.1 ms: 1.21x faster |
| async_tree_io              | 423 ms  | 349 ms: 1.21x faster  |
| async_tree_none            | 187 ms  | 155 ms: 1.20x faster  |
| async_generators           | 226 ms  | 188 ms: 1.20x faster  |
| async_tree_none_tg         | 176 ms  | 147 ms: 1.20x faster  |
| async_tree_memoization     | 224 ms  | 190 ms: 1.18x faster  |
| async_tree_io_tg           | 410 ms  | 352 ms: 1.16x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 310 ms: 1.11x faster  |
| async_tree_memoization_tg  | 216 ms  | 195 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 309 ms: 1.10x faster  |
| asyncio_websockets         | 318 ms  | 400 ms: 1.26x slower  |
| Geometric mean             | (ref)   | 1.13x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | clang-PGO             |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 52.9 ms: 1.40x faster |
| float          | 47.8 ms | 38.5 ms: 1.24x faster |
| pidigits       | 152 ms  | 148 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.21x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 73.4 ms: 1.20x faster |
| regex_dna      | 112 ms  | 121 ms: 1.07x slower  |
| regex_effbot   | 1.42 ms | 1.65 ms: 1.16x slower |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 109 us: 1.43x faster   |
| pickle_pure_python   | 237 us   | 175 us: 1.35x faster   |
| tomli_loads          | 1.47 sec | 1.13 sec: 1.30x faster |
| json_dumps           | 7.05 ms  | 5.76 ms: 1.22x faster  |
| xml_etree_process    | 41.5 ms  | 34.0 ms: 1.22x faster  |
| xml_etree_generate   | 58.7 ms  | 48.4 ms: 1.21x faster  |
| xml_etree_iterparse  | 63.7 ms  | 60.7 ms: 1.05x faster  |
| json_loads           | 14.7 us  | 14.2 us: 1.04x faster  |
| xml_etree_parse      | 91.2 ms  | 88.8 ms: 1.03x faster  |
| Geometric mean       | (ref)    | 1.20x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | PGO     | clang-PGO             |
|----------------|:-------:|:---------------------:|
| python_startup | 26.1 ms | 26.6 ms: 1.02x slower |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 12.0 ms: 1.38x faster |
| genshi_xml      | 36.3 ms | 27.4 ms: 1.33x faster |
| django_template | 25.1 ms | 19.5 ms: 1.28x faster |
| mako            | 6.86 ms | 5.72 ms: 1.20x faster |
| Geometric mean  | (ref)   | 1.30x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| scimark_sor                | 91.0 ms  | 59.1 ms: 1.54x faster  |
| logging_silent             | 65.2 ns  | 44.5 ns: 1.47x faster  |
| deltablue                  | 2.29 ms  | 1.59 ms: 1.44x faster  |
| scimark_monte_carlo        | 47.1 ms  | 32.8 ms: 1.44x faster  |
| unpickle_pure_python       | 155 us   | 109 us: 1.43x faster   |
| richards_super             | 35.1 ms  | 24.6 ms: 1.43x faster  |
| fannkuch                   | 296 ms   | 209 ms: 1.42x faster   |
| chaos                      | 43.6 ms  | 31.1 ms: 1.40x faster  |
| richards                   | 30.7 ms  | 21.9 ms: 1.40x faster  |
| hexiom                     | 4.38 ms  | 3.13 ms: 1.40x faster  |
| nbody                      | 74.1 ms  | 52.9 ms: 1.40x faster  |
| deepcopy_memo              | 21.0 us  | 15.1 us: 1.40x faster  |
| raytrace                   | 191 ms   | 137 ms: 1.39x faster   |
| genshi_text                | 16.5 ms  | 12.0 ms: 1.38x faster  |
| spectral_norm              | 61.5 ms  | 44.7 ms: 1.38x faster  |
| go                         | 88.6 ms  | 65.1 ms: 1.36x faster  |
| scimark_lu                 | 66.9 ms  | 49.1 ms: 1.36x faster  |
| pickle_pure_python         | 237 us   | 175 us: 1.35x faster   |
| scimark_fft                | 192 ms   | 143 ms: 1.35x faster   |
| nqueens                    | 63.6 ms  | 47.7 ms: 1.33x faster  |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.05 ms: 1.33x faster  |
| genshi_xml                 | 36.3 ms  | 27.4 ms: 1.33x faster  |
| deepcopy                   | 190 us   | 145 us: 1.31x faster   |
| deepcopy_reduce            | 1.94 us  | 1.49 us: 1.30x faster  |
| sqlglot_v2_parse           | 892 us   | 686 us: 1.30x faster   |
| tomli_loads                | 1.47 sec | 1.13 sec: 1.30x faster |
| pprint_safe_repr           | 558 ms   | 432 ms: 1.29x faster   |
| pyflate                    | 315 ms   | 245 ms: 1.29x faster   |
| pprint_pformat             | 1.13 sec | 874 ms: 1.29x faster   |
| django_template            | 25.1 ms  | 19.5 ms: 1.28x faster  |
| comprehensions             | 11.3 us  | 8.84 us: 1.28x faster  |
| crypto_pyaes               | 50.0 ms  | 39.4 ms: 1.27x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 868 us: 1.27x faster   |
| mdp                        | 1.64 sec | 1.30 sec: 1.26x faster |
| float                      | 47.8 ms  | 38.5 ms: 1.24x faster  |
| typing_runtime_protocols   | 106 us   | 86.2 us: 1.23x faster  |
| sqlglot_v2_normalize       | 73.6 ms  | 59.9 ms: 1.23x faster  |
| generators                 | 19.3 ms  | 15.8 ms: 1.22x faster  |
| json_dumps                 | 7.05 ms  | 5.76 ms: 1.22x faster  |
| xml_etree_process          | 41.5 ms  | 34.0 ms: 1.22x faster  |
| coroutines                 | 13.5 ms  | 11.1 ms: 1.21x faster  |
| async_tree_io              | 423 ms   | 349 ms: 1.21x faster   |
| xml_etree_generate         | 58.7 ms  | 48.4 ms: 1.21x faster  |
| logging_simple             | 6.53 us  | 5.39 us: 1.21x faster  |
| logging_format             | 7.03 us  | 5.83 us: 1.20x faster  |
| async_tree_none            | 187 ms   | 155 ms: 1.20x faster   |
| async_generators           | 226 ms   | 188 ms: 1.20x faster   |
| regex_compile              | 88.2 ms  | 73.4 ms: 1.20x faster  |
| mako                       | 6.86 ms  | 5.72 ms: 1.20x faster  |
| async_tree_none_tg         | 176 ms   | 147 ms: 1.20x faster   |
| bpe_tokeniser              | 2.96 sec | 2.50 sec: 1.18x faster |
| async_tree_memoization     | 224 ms   | 190 ms: 1.18x faster   |
| sqlglot_v2_optimize        | 35.0 ms  | 29.8 ms: 1.18x faster  |
| thrift                     | 507 us   | 434 us: 1.17x faster   |
| telco                      | 4.89 ms  | 4.20 ms: 1.17x faster  |
| sympy_expand               | 302 ms   | 259 ms: 1.17x faster   |
| async_tree_io_tg           | 410 ms   | 352 ms: 1.16x faster   |
| pycparser                  | 738 ms   | 637 ms: 1.16x faster   |
| html5lib                   | 40.8 ms  | 35.2 ms: 1.16x faster  |
| sympy_str                  | 176 ms   | 153 ms: 1.15x faster   |
| sympy_integrate            | 13.5 ms  | 11.8 ms: 1.15x faster  |
| coverage                   | 46.8 ms  | 40.9 ms: 1.14x faster  |
| subparsers                 | 16.1 ms  | 14.2 ms: 1.13x faster  |
| meteor_contest             | 76.9 ms  | 68.7 ms: 1.12x faster  |
| 2to3                       | 227 ms   | 204 ms: 1.12x faster   |
| sympy_sum                  | 90.5 ms  | 81.4 ms: 1.11x faster  |
| json                       | 3.14 ms  | 2.83 ms: 1.11x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms   | 310 ms: 1.11x faster   |
| async_tree_memoization_tg  | 216 ms   | 195 ms: 1.10x faster   |
| pylint                     | 201 ms   | 182 ms: 1.10x faster   |
| sphinx                     | 658 ms   | 599 ms: 1.10x faster   |
| dulwich_log                | 43.4 ms  | 39.5 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 339 ms   | 309 ms: 1.10x faster   |
| docutils                   | 1.68 sec | 1.55 sec: 1.09x faster |
| many_optionals             | 438 us   | 405 us: 1.08x faster   |
| k_core                     | 1.73 sec | 1.61 sec: 1.08x faster |
| sqlite_synth               | 1.59 us  | 1.49 us: 1.06x faster  |
| pathlib                    | 32.1 ms  | 30.4 ms: 1.06x faster  |
| xml_etree_iterparse        | 63.7 ms  | 60.7 ms: 1.05x faster  |
| shortest_path              | 359 ms   | 345 ms: 1.04x faster   |
| json_loads                 | 14.7 us  | 14.2 us: 1.04x faster  |
| xml_etree_parse            | 91.2 ms  | 88.8 ms: 1.03x faster  |
| pidigits                   | 152 ms   | 148 ms: 1.03x faster   |
| connected_components       | 329 ms   | 325 ms: 1.01x faster   |
| python_startup             | 26.1 ms  | 26.6 ms: 1.02x slower  |
| regex_dna                  | 112 ms   | 121 ms: 1.07x slower   |
| create_gc_cycles           | 1.25 ms  | 1.37 ms: 1.10x slower  |
| regex_effbot               | 1.42 ms  | 1.65 ms: 1.16x slower  |
| asyncio_websockets         | 318 ms   | 400 ms: 1.26x slower   |
| gc_traversal               | 2.06 ms  | 2.79 ms: 1.36x slower  |
| Geometric mean             | (ref)    | 1.19x faster           |

Benchmark hidden because not significant (2): regex_v8, python_startup_no_site
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.188x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown