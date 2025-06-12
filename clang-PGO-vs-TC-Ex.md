# Results vs. base

- fork: unknown
- ref: clang-PGO
- machine: unknown-unknown
- commit hash: d8a1cf4
- commit date: 2025-03-04
- overall geometric mean: 1.179x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | clang-PGO              |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 204 ms: 1.13x faster   |
| docutils       | 1.77 sec | 1.55 sec: 1.14x faster |
| html5lib       | 38.8 ms  | 35.2 ms: 1.10x faster  |
| sphinx         | 702 ms   | 599 ms: 1.17x faster   |
| Geometric mean | (ref)    | 1.14x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | clang-PGO             |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 310 ms: 1.17x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 309 ms: 1.16x faster  |
| async_tree_none_tg         | 167 ms  | 147 ms: 1.13x faster  |
| async_generators           | 213 ms  | 188 ms: 1.13x faster  |
| async_tree_none            | 174 ms  | 155 ms: 1.12x faster  |
| async_tree_memoization     | 210 ms  | 190 ms: 1.11x faster  |
| coroutines                 | 12.3 ms | 11.1 ms: 1.10x faster |
| async_tree_io              | 384 ms  | 349 ms: 1.10x faster  |
| async_tree_io_tg           | 385 ms  | 352 ms: 1.09x faster  |
| async_tree_memoization_tg  | 210 ms  | 195 ms: 1.08x faster  |
| asyncio_websockets         | 312 ms  | 400 ms: 1.28x slower  |
| Geometric mean             | (ref)   | 1.08x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | clang-PGO             |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 38.5 ms: 1.08x faster |
| pidigits       | 146 ms  | 148 ms: 1.02x slower  |
| Geometric mean | (ref)   | 1.02x faster          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | clang-PGO             |
|----------------|:-------:|:---------------------:|
| regex_v8       | 16.3 ms | 13.5 ms: 1.21x faster |
| regex_effbot   | 1.85 ms | 1.65 ms: 1.12x faster |
| regex_compile  | 81.9 ms | 73.4 ms: 1.12x faster |
| Geometric mean | (ref)   | 1.11x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | clang-PGO              |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.2 us: 1.54x faster  |
| unpickle_pure_python | 148 us   | 109 us: 1.36x faster   |
| json_dumps           | 7.79 ms  | 5.76 ms: 1.35x faster  |
| xml_etree_generate   | 64.7 ms  | 48.4 ms: 1.34x faster  |
| xml_etree_process    | 44.7 ms  | 34.0 ms: 1.32x faster  |
| pickle_pure_python   | 223 us   | 175 us: 1.27x faster   |
| xml_etree_parse      | 105 ms   | 88.8 ms: 1.18x faster  |
| xml_etree_iterparse  | 70.4 ms  | 60.7 ms: 1.16x faster  |
| tomli_loads          | 1.26 sec | 1.13 sec: 1.11x faster |
| Geometric mean       | (ref)    | 1.29x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | clang-PGO             |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.4 ms | 20.0 ms: 1.03x slower |
| Geometric mean         | (ref)   | 1.02x slower          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | clang-PGO             |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 5.72 ms: 1.37x faster |
| django_template | 25.2 ms | 19.5 ms: 1.29x faster |
| genshi_text     | 14.5 ms | 12.0 ms: 1.21x faster |
| genshi_xml      | 31.3 ms | 27.4 ms: 1.14x faster |
| Geometric mean  | (ref)   | 1.25x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | clang-PGO              |
|----------------------------|:--------:|:----------------------:|
| subparsers                 | 44.5 ms  | 14.2 ms: 3.12x faster  |
| many_optionals             | 762 us   | 405 us: 1.88x faster   |
| json_loads                 | 21.9 us  | 14.2 us: 1.54x faster  |
| richards_super             | 35.8 ms  | 24.6 ms: 1.45x faster  |
| richards                   | 30.9 ms  | 21.9 ms: 1.41x faster  |
| logging_silent             | 61.1 ns  | 44.5 ns: 1.37x faster  |
| mako                       | 7.84 ms  | 5.72 ms: 1.37x faster  |
| unpickle_pure_python       | 148 us   | 109 us: 1.36x faster   |
| coverage                   | 55.4 ms  | 40.9 ms: 1.35x faster  |
| json_dumps                 | 7.79 ms  | 5.76 ms: 1.35x faster  |
| xml_etree_generate         | 64.7 ms  | 48.4 ms: 1.34x faster  |
| json                       | 3.78 ms  | 2.83 ms: 1.33x faster  |
| xml_etree_process          | 44.7 ms  | 34.0 ms: 1.32x faster  |
| scimark_lu                 | 64.2 ms  | 49.1 ms: 1.31x faster  |
| django_template            | 25.2 ms  | 19.5 ms: 1.29x faster  |
| deepcopy_memo              | 19.3 us  | 15.1 us: 1.28x faster  |
| comprehensions             | 11.3 us  | 8.84 us: 1.28x faster  |
| deepcopy_reduce            | 1.90 us  | 1.49 us: 1.27x faster  |
| pickle_pure_python         | 223 us   | 175 us: 1.27x faster   |
| thrift                     | 551 us   | 434 us: 1.27x faster   |
| telco                      | 5.26 ms  | 4.20 ms: 1.25x faster  |
| hexiom                     | 3.92 ms  | 3.13 ms: 1.25x faster  |
| nqueens                    | 59.6 ms  | 47.7 ms: 1.25x faster  |
| deepcopy                   | 180 us   | 145 us: 1.25x faster   |
| raytrace                   | 169 ms   | 137 ms: 1.23x faster   |
| typing_runtime_protocols   | 106 us   | 86.2 us: 1.23x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 59.9 ms: 1.22x faster  |
| crypto_pyaes               | 48.0 ms  | 39.4 ms: 1.22x faster  |
| chaos                      | 37.7 ms  | 31.1 ms: 1.21x faster  |
| sqlglot_v2_optimize        | 36.1 ms  | 29.8 ms: 1.21x faster  |
| genshi_text                | 14.5 ms  | 12.0 ms: 1.21x faster  |
| regex_v8                   | 16.3 ms  | 13.5 ms: 1.21x faster  |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.05 ms: 1.20x faster  |
| bpe_tokeniser              | 3.01 sec | 2.50 sec: 1.20x faster |
| deltablue                  | 1.91 ms  | 1.59 ms: 1.20x faster  |
| fannkuch                   | 250 ms   | 209 ms: 1.20x faster   |
| scimark_monte_carlo        | 38.9 ms  | 32.8 ms: 1.19x faster  |
| pprint_pformat             | 1.04 sec | 874 ms: 1.19x faster   |
| pprint_safe_repr           | 510 ms   | 432 ms: 1.18x faster   |
| scimark_fft                | 169 ms   | 143 ms: 1.18x faster   |
| xml_etree_parse            | 105 ms   | 88.8 ms: 1.18x faster  |
| sympy_expand               | 304 ms   | 259 ms: 1.17x faster   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 310 ms: 1.17x faster   |
| sphinx                     | 702 ms   | 599 ms: 1.17x faster   |
| sqlglot_v2_transpile       | 1.01 ms  | 868 us: 1.17x faster   |
| async_tree_cpu_io_mixed    | 359 ms   | 309 ms: 1.16x faster   |
| sqlglot_v2_parse           | 798 us   | 686 us: 1.16x faster   |
| scimark_sor                | 68.6 ms  | 59.1 ms: 1.16x faster  |
| sympy_str                  | 177 ms   | 153 ms: 1.16x faster   |
| logging_simple             | 6.25 us  | 5.39 us: 1.16x faster  |
| xml_etree_iterparse        | 70.4 ms  | 60.7 ms: 1.16x faster  |
| logging_format             | 6.70 us  | 5.83 us: 1.15x faster  |
| docutils                   | 1.77 sec | 1.55 sec: 1.14x faster |
| genshi_xml                 | 31.3 ms  | 27.4 ms: 1.14x faster  |
| spectral_norm              | 51.1 ms  | 44.7 ms: 1.14x faster  |
| sympy_integrate            | 13.4 ms  | 11.8 ms: 1.14x faster  |
| async_tree_none_tg         | 167 ms   | 147 ms: 1.13x faster   |
| 2to3                       | 231 ms   | 204 ms: 1.13x faster   |
| async_generators           | 213 ms   | 188 ms: 1.13x faster   |
| sympy_sum                  | 91.4 ms  | 81.4 ms: 1.12x faster  |
| pylint                     | 205 ms   | 182 ms: 1.12x faster   |
| sqlite_synth               | 1.68 us  | 1.49 us: 1.12x faster  |
| async_tree_none            | 174 ms   | 155 ms: 1.12x faster   |
| regex_effbot               | 1.85 ms  | 1.65 ms: 1.12x faster  |
| pycparser                  | 713 ms   | 637 ms: 1.12x faster   |
| pyflate                    | 274 ms   | 245 ms: 1.12x faster   |
| regex_compile              | 81.9 ms  | 73.4 ms: 1.12x faster  |
| tomli_loads                | 1.26 sec | 1.13 sec: 1.11x faster |
| mdp                        | 1.44 sec | 1.30 sec: 1.11x faster |
| async_tree_memoization     | 210 ms   | 190 ms: 1.11x faster   |
| coroutines                 | 12.3 ms  | 11.1 ms: 1.10x faster  |
| async_tree_io              | 384 ms   | 349 ms: 1.10x faster   |
| html5lib                   | 38.8 ms  | 35.2 ms: 1.10x faster  |
| async_tree_io_tg           | 385 ms   | 352 ms: 1.09x faster   |
| meteor_contest             | 74.5 ms  | 68.7 ms: 1.08x faster  |
| go                         | 70.4 ms  | 65.1 ms: 1.08x faster  |
| async_tree_memoization_tg  | 210 ms   | 195 ms: 1.08x faster   |
| float                      | 41.4 ms  | 38.5 ms: 1.08x faster  |
| dulwich_log                | 42.3 ms  | 39.5 ms: 1.07x faster  |
| k_core                     | 1.71 sec | 1.61 sec: 1.06x faster |
| generators                 | 16.3 ms  | 15.8 ms: 1.03x faster  |
| gc_traversal               | 2.83 ms  | 2.79 ms: 1.02x faster  |
| shortest_path              | 347 ms   | 345 ms: 1.00x faster   |
| pidigits                   | 146 ms   | 148 ms: 1.02x slower   |
| create_gc_cycles           | 1.34 ms  | 1.37 ms: 1.02x slower  |
| python_startup_no_site     | 19.4 ms  | 20.0 ms: 1.03x slower  |
| connected_components       | 311 ms   | 325 ms: 1.04x slower   |
| pathlib                    | 25.1 ms  | 30.4 ms: 1.21x slower  |
| asyncio_websockets         | 312 ms   | 400 ms: 1.28x slower   |
| Geometric mean             | (ref)    | 1.18x faster           |

Benchmark hidden because not significant (3): nbody, regex_dna, python_startup
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.179x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown