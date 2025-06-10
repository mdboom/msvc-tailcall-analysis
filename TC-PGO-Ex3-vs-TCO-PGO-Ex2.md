# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.225x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 204 ms: 1.16x faster   |
| docutils       | 1.81 sec    | 1.58 sec: 1.15x faster |
| html5lib       | 40.8 ms     | 35.5 ms: 1.15x faster  |
| sphinx         | 723 ms      | 615 ms: 1.18x faster   |
| Geometric mean | (ref)       | 1.16x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------------------|:-----------:|:---------------------:|
| coroutines                 | 13.5 ms     | 10.8 ms: 1.25x faster |
| async_tree_io              | 429 ms      | 353 ms: 1.21x faster  |
| async_tree_none            | 188 ms      | 157 ms: 1.20x faster  |
| async_tree_none_tg         | 178 ms      | 150 ms: 1.18x faster  |
| async_tree_io_tg           | 419 ms      | 356 ms: 1.18x faster  |
| async_tree_memoization     | 227 ms      | 196 ms: 1.16x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 325 ms: 1.13x faster  |
| async_generators           | 224 ms      | 199 ms: 1.13x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 327 ms: 1.11x faster  |
| async_tree_memoization_tg  | 218 ms      | 201 ms: 1.09x faster  |
| Geometric mean             | (ref)       | 1.15x faster          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| nbody          | 58.8 ms     | 45.7 ms: 1.28x faster |
| float          | 44.8 ms     | 37.1 ms: 1.21x faster |
| pidigits       | 147 ms      | 145 ms: 1.01x faster  |
| Geometric mean | (ref)       | 1.16x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 88.0 ms     | 70.7 ms: 1.25x faster |
| regex_effbot   | 1.76 ms     | 1.45 ms: 1.21x faster |
| regex_v8       | 16.7 ms     | 13.9 ms: 1.19x faster |
| regex_dna      | 117 ms      | 121 ms: 1.03x slower  |
| Geometric mean | (ref)       | 1.15x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 14.8 us: 1.43x faster  |
| unpickle_pure_python | 154 us      | 110 us: 1.40x faster   |
| xml_etree_process    | 46.5 ms     | 33.8 ms: 1.38x faster  |
| xml_etree_generate   | 66.8 ms     | 49.4 ms: 1.35x faster  |
| tomli_loads          | 1.38 sec    | 1.03 sec: 1.35x faster |
| json_dumps           | 7.94 ms     | 6.19 ms: 1.28x faster  |
| pickle_pure_python   | 236 us      | 184 us: 1.28x faster   |
| xml_etree_iterparse  | 71.5 ms     | 59.5 ms: 1.20x faster  |
| xml_etree_parse      | 104 ms      | 89.4 ms: 1.16x faster  |
| Geometric mean       | (ref)       | 1.31x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.9 ms     | 24.7 ms: 1.09x faster |
| python_startup_no_site | 20.1 ms     | 18.7 ms: 1.07x faster |
| Geometric mean         | (ref)       | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TC-PGO-Ex3            |
|-----------------|:-----------:|:---------------------:|
| django_template | 27.5 ms     | 20.9 ms: 1.31x faster |
| genshi_text     | 16.2 ms     | 12.3 ms: 1.31x faster |
| mako            | 7.44 ms     | 5.80 ms: 1.28x faster |
| genshi_xml      | 35.3 ms     | 29.5 ms: 1.20x faster |
| Geometric mean  | (ref)       | 1.27x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------------|:-----------:|:----------------------:|
| scimark_lu                 | 65.2 ms     | 44.3 ms: 1.47x faster  |
| deepcopy_memo              | 21.3 us     | 14.7 us: 1.45x faster  |
| scimark_sor                | 73.9 ms     | 51.1 ms: 1.45x faster  |
| json_loads                 | 21.1 us     | 14.8 us: 1.43x faster  |
| logging_silent             | 62.9 ns     | 44.1 ns: 1.43x faster  |
| spectral_norm              | 58.4 ms     | 40.9 ms: 1.43x faster  |
| comprehensions             | 12.2 us     | 8.65 us: 1.41x faster  |
| unpickle_pure_python       | 154 us      | 110 us: 1.40x faster   |
| deepcopy_reduce            | 2.12 us     | 1.51 us: 1.40x faster  |
| hexiom                     | 4.17 ms     | 3.00 ms: 1.39x faster  |
| xml_etree_process          | 46.5 ms     | 33.8 ms: 1.38x faster  |
| richards_super             | 40.4 ms     | 29.4 ms: 1.37x faster  |
| richards                   | 35.0 ms     | 25.5 ms: 1.37x faster  |
| scimark_monte_carlo        | 42.9 ms     | 31.5 ms: 1.36x faster  |
| deepcopy                   | 199 us      | 147 us: 1.36x faster   |
| xml_etree_generate         | 66.8 ms     | 49.4 ms: 1.35x faster  |
| tomli_loads                | 1.38 sec    | 1.03 sec: 1.35x faster |
| chaos                      | 41.4 ms     | 31.3 ms: 1.33x faster  |
| gc_traversal               | 2.77 ms     | 2.09 ms: 1.33x faster  |
| pprint_pformat             | 1.13 sec    | 853 ms: 1.32x faster   |
| nqueens                    | 65.7 ms     | 49.7 ms: 1.32x faster  |
| django_template            | 27.5 ms     | 20.9 ms: 1.31x faster  |
| genshi_text                | 16.2 ms     | 12.3 ms: 1.31x faster  |
| fannkuch                   | 265 ms      | 203 ms: 1.30x faster   |
| pprint_safe_repr           | 558 ms      | 429 ms: 1.30x faster   |
| raytrace                   | 187 ms      | 145 ms: 1.29x faster   |
| nbody                      | 58.8 ms     | 45.7 ms: 1.28x faster  |
| mako                       | 7.44 ms     | 5.80 ms: 1.28x faster  |
| json_dumps                 | 7.94 ms     | 6.19 ms: 1.28x faster  |
| pickle_pure_python         | 236 us      | 184 us: 1.28x faster   |
| go                         | 78.0 ms     | 61.0 ms: 1.28x faster  |
| json                       | 3.77 ms     | 2.95 ms: 1.28x faster  |
| deltablue                  | 2.09 ms     | 1.64 ms: 1.27x faster  |
| generators                 | 18.1 ms     | 14.2 ms: 1.27x faster  |
| scimark_fft                | 178 ms      | 140 ms: 1.27x faster   |
| sqlglot_v2_normalize       | 79.0 ms     | 62.6 ms: 1.26x faster  |
| sqlglot_v2_parse           | 876 us      | 695 us: 1.26x faster   |
| sqlglot_v2_optimize        | 38.4 ms     | 30.5 ms: 1.26x faster  |
| typing_runtime_protocols   | 113 us      | 89.7 us: 1.26x faster  |
| bpe_tokeniser              | 3.17 sec    | 2.52 sec: 1.26x faster |
| pyflate                    | 295 ms      | 236 ms: 1.25x faster   |
| coroutines                 | 13.5 ms     | 10.8 ms: 1.25x faster  |
| regex_compile              | 88.0 ms     | 70.7 ms: 1.25x faster  |
| many_optionals             | 813 us      | 659 us: 1.23x faster   |
| sympy_expand               | 324 ms      | 263 ms: 1.23x faster   |
| logging_simple             | 6.67 us     | 5.42 us: 1.23x faster  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.02 ms: 1.23x faster  |
| sqlglot_v2_transpile       | 1.09 ms     | 894 us: 1.22x faster   |
| coverage                   | 56.4 ms     | 46.2 ms: 1.22x faster  |
| crypto_pyaes               | 49.3 ms     | 40.4 ms: 1.22x faster  |
| logging_format             | 7.18 us     | 5.90 us: 1.22x faster  |
| thrift                     | 561 us      | 461 us: 1.22x faster   |
| sympy_str                  | 187 ms      | 153 ms: 1.22x faster   |
| async_tree_io              | 429 ms      | 353 ms: 1.21x faster   |
| regex_effbot               | 1.76 ms     | 1.45 ms: 1.21x faster  |
| float                      | 44.8 ms     | 37.1 ms: 1.21x faster  |
| xml_etree_iterparse        | 71.5 ms     | 59.5 ms: 1.20x faster  |
| telco                      | 5.33 ms     | 4.45 ms: 1.20x faster  |
| sympy_sum                  | 96.6 ms     | 80.7 ms: 1.20x faster  |
| genshi_xml                 | 35.3 ms     | 29.5 ms: 1.20x faster  |
| async_tree_none            | 188 ms      | 157 ms: 1.20x faster   |
| regex_v8                   | 16.7 ms     | 13.9 ms: 1.19x faster  |
| pycparser                  | 765 ms      | 642 ms: 1.19x faster   |
| async_tree_none_tg         | 178 ms      | 150 ms: 1.18x faster   |
| async_tree_io_tg           | 419 ms      | 356 ms: 1.18x faster   |
| sphinx                     | 723 ms      | 615 ms: 1.18x faster   |
| meteor_contest             | 78.1 ms     | 66.6 ms: 1.17x faster  |
| 2to3                       | 237 ms      | 204 ms: 1.16x faster   |
| subparsers                 | 47.1 ms     | 40.6 ms: 1.16x faster  |
| xml_etree_parse            | 104 ms      | 89.4 ms: 1.16x faster  |
| sympy_integrate            | 13.9 ms     | 12.0 ms: 1.16x faster  |
| async_tree_memoization     | 227 ms      | 196 ms: 1.16x faster   |
| html5lib                   | 40.8 ms     | 35.5 ms: 1.15x faster  |
| docutils                   | 1.81 sec    | 1.58 sec: 1.15x faster |
| async_tree_cpu_io_mixed_tg | 367 ms      | 325 ms: 1.13x faster   |
| pylint                     | 217 ms      | 193 ms: 1.13x faster   |
| async_generators           | 224 ms      | 199 ms: 1.13x faster   |
| mdp                        | 1.57 sec    | 1.41 sec: 1.12x faster |
| async_tree_cpu_io_mixed    | 362 ms      | 327 ms: 1.11x faster   |
| dulwich_log                | 43.0 ms     | 39.1 ms: 1.10x faster  |
| create_gc_cycles           | 1.38 ms     | 1.26 ms: 1.10x faster  |
| python_startup             | 26.9 ms     | 24.7 ms: 1.09x faster  |
| async_tree_memoization_tg  | 218 ms      | 201 ms: 1.09x faster   |
| pathlib                    | 25.6 ms     | 23.6 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us     | 1.56 us: 1.08x faster  |
| python_startup_no_site     | 20.1 ms     | 18.7 ms: 1.07x faster  |
| k_core                     | 1.76 sec    | 1.67 sec: 1.05x faster |
| shortest_path              | 357 ms      | 347 ms: 1.03x faster   |
| connected_components       | 326 ms      | 320 ms: 1.02x faster   |
| pidigits                   | 147 ms      | 145 ms: 1.01x faster   |
| regex_dna                  | 117 ms      | 121 ms: 1.03x slower   |
| Geometric mean             | (ref)       | 1.23x faster           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.225x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown