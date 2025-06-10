# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.121x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 237 ms: 1.10x slower   |
| docutils       | 1.66 sec    | 1.81 sec: 1.10x slower |
| html5lib       | 37.8 ms     | 40.8 ms: 1.08x slower  |
| sphinx         | 641 ms      | 723 ms: 1.13x slower   |
| Geometric mean | (ref)       | 1.10x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 313 ms      | 304 ms: 1.03x faster  |
| async_tree_memoization_tg  | 208 ms      | 218 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 362 ms: 1.10x slower  |
| async_tree_none_tg         | 161 ms      | 178 ms: 1.10x slower  |
| async_tree_memoization     | 205 ms      | 227 ms: 1.11x slower  |
| async_tree_none            | 170 ms      | 188 ms: 1.11x slower  |
| async_generators           | 201 ms      | 224 ms: 1.11x slower  |
| async_tree_io_tg           | 377 ms      | 419 ms: 1.11x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 367 ms: 1.11x slower  |
| async_tree_io              | 382 ms      | 429 ms: 1.12x slower  |
| coroutines                 | 12.0 ms     | 13.5 ms: 1.13x slower |
| Geometric mean             | (ref)       | 1.09x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 147 ms: 1.01x slower  |
| nbody          | 55.6 ms     | 58.8 ms: 1.06x slower |
| float          | 42.0 ms     | 44.8 ms: 1.07x slower |
| Geometric mean | (ref)       | 1.04x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 117 ms: 1.02x faster  |
| regex_compile  | 79.4 ms     | 88.0 ms: 1.11x slower |
| regex_v8       | 14.2 ms     | 16.7 ms: 1.17x slower |
| regex_effbot   | 1.47 ms     | 1.76 ms: 1.20x slower |
| Geometric mean | (ref)       | 1.11x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms     | 104 ms: 1.16x slower   |
| xml_etree_iterparse  | 61.2 ms     | 71.5 ms: 1.17x slower  |
| tomli_loads          | 1.17 sec    | 1.38 sec: 1.18x slower |
| pickle_pure_python   | 199 us      | 236 us: 1.18x slower   |
| json_dumps           | 6.40 ms     | 7.94 ms: 1.24x slower  |
| unpickle_pure_python | 124 us      | 154 us: 1.24x slower   |
| xml_etree_generate   | 53.1 ms     | 66.8 ms: 1.26x slower  |
| xml_etree_process    | 36.8 ms     | 46.5 ms: 1.26x slower  |
| json_loads           | 14.5 us     | 21.1 us: 1.46x slower  |
| Geometric mean       | (ref)       | 1.24x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 20.1 ms: 1.08x slower |
| python_startup         | 24.7 ms     | 26.9 ms: 1.09x slower |
| Geometric mean         | (ref)       | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.3 ms     | 35.3 ms: 1.09x slower |
| genshi_text     | 14.3 ms     | 16.2 ms: 1.13x slower |
| django_template | 23.6 ms     | 27.5 ms: 1.17x slower |
| mako            | 6.25 ms     | 7.44 ms: 1.19x slower |
| Geometric mean  | (ref)       | 1.14x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------------|:-----------:|:----------------------:|
| asyncio_websockets         | 313 ms      | 304 ms: 1.03x faster   |
| regex_dna                  | 120 ms      | 117 ms: 1.02x faster   |
| pidigits                   | 145 ms      | 147 ms: 1.01x slower   |
| shortest_path              | 352 ms      | 357 ms: 1.02x slower   |
| k_core                     | 1.70 sec    | 1.76 sec: 1.03x slower |
| async_tree_memoization_tg  | 208 ms      | 218 ms: 1.05x slower   |
| nbody                      | 55.6 ms     | 58.8 ms: 1.06x slower  |
| pathlib                    | 24.2 ms     | 25.6 ms: 1.06x slower  |
| float                      | 42.0 ms     | 44.8 ms: 1.07x slower  |
| dulwich_log                | 40.3 ms     | 43.0 ms: 1.07x slower  |
| sympy_str                  | 173 ms      | 187 ms: 1.08x slower   |
| sqlite_synth               | 1.56 us     | 1.68 us: 1.08x slower  |
| pylint                     | 201 ms      | 217 ms: 1.08x slower   |
| html5lib                   | 37.8 ms     | 40.8 ms: 1.08x slower  |
| python_startup_no_site     | 18.6 ms     | 20.1 ms: 1.08x slower  |
| sympy_integrate            | 12.8 ms     | 13.9 ms: 1.08x slower  |
| python_startup             | 24.7 ms     | 26.9 ms: 1.09x slower  |
| genshi_xml                 | 32.3 ms     | 35.3 ms: 1.09x slower  |
| docutils                   | 1.66 sec    | 1.81 sec: 1.10x slower |
| generators                 | 16.5 ms     | 18.1 ms: 1.10x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 362 ms: 1.10x slower   |
| mdp                        | 1.43 sec    | 1.57 sec: 1.10x slower |
| sqlglot_v2_transpile       | 993 us      | 1.09 ms: 1.10x slower  |
| meteor_contest             | 70.9 ms     | 78.1 ms: 1.10x slower  |
| 2to3                       | 215 ms      | 237 ms: 1.10x slower   |
| async_tree_none_tg         | 161 ms      | 178 ms: 1.10x slower   |
| create_gc_cycles           | 1.25 ms     | 1.38 ms: 1.11x slower  |
| async_tree_memoization     | 205 ms      | 227 ms: 1.11x slower   |
| go                         | 70.5 ms     | 78.0 ms: 1.11x slower  |
| deltablue                  | 1.88 ms     | 2.09 ms: 1.11x slower  |
| async_tree_none            | 170 ms      | 188 ms: 1.11x slower   |
| regex_compile              | 79.4 ms     | 88.0 ms: 1.11x slower  |
| pycparser                  | 689 ms      | 765 ms: 1.11x slower   |
| async_generators           | 201 ms      | 224 ms: 1.11x slower   |
| async_tree_io_tg           | 377 ms      | 419 ms: 1.11x slower   |
| async_tree_cpu_io_mixed_tg | 330 ms      | 367 ms: 1.11x slower   |
| pyflate                    | 264 ms      | 295 ms: 1.12x slower   |
| logging_format             | 6.42 us     | 7.18 us: 1.12x slower  |
| sqlglot_v2_parse           | 781 us      | 876 us: 1.12x slower   |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.48 ms: 1.12x slower  |
| crypto_pyaes               | 43.9 ms     | 49.3 ms: 1.12x slower  |
| async_tree_io              | 382 ms      | 429 ms: 1.12x slower   |
| coroutines                 | 12.0 ms     | 13.5 ms: 1.13x slower  |
| sphinx                     | 641 ms      | 723 ms: 1.13x slower   |
| genshi_text                | 14.3 ms     | 16.2 ms: 1.13x slower  |
| sympy_sum                  | 85.2 ms     | 96.6 ms: 1.13x slower  |
| logging_simple             | 5.87 us     | 6.67 us: 1.14x slower  |
| subparsers                 | 41.4 ms     | 47.1 ms: 1.14x slower  |
| thrift                     | 491 us      | 561 us: 1.14x slower   |
| sqlglot_v2_normalize       | 69.0 ms     | 79.0 ms: 1.14x slower  |
| sympy_expand               | 283 ms      | 324 ms: 1.15x slower   |
| typing_runtime_protocols   | 97.8 us     | 113 us: 1.15x slower   |
| raytrace                   | 162 ms      | 187 ms: 1.16x slower   |
| scimark_fft                | 153 ms      | 178 ms: 1.16x slower   |
| xml_etree_parse            | 89.4 ms     | 104 ms: 1.16x slower   |
| telco                      | 4.59 ms     | 5.33 ms: 1.16x slower  |
| sqlglot_v2_optimize        | 32.9 ms     | 38.4 ms: 1.16x slower  |
| bpe_tokeniser              | 2.72 sec    | 3.17 sec: 1.16x slower |
| django_template            | 23.6 ms     | 27.5 ms: 1.17x slower  |
| xml_etree_iterparse        | 61.2 ms     | 71.5 ms: 1.17x slower  |
| chaos                      | 35.4 ms     | 41.4 ms: 1.17x slower  |
| regex_v8                   | 14.2 ms     | 16.7 ms: 1.17x slower  |
| pprint_safe_repr           | 474 ms      | 558 ms: 1.18x slower   |
| tomli_loads                | 1.17 sec    | 1.38 sec: 1.18x slower |
| fannkuch                   | 225 ms      | 265 ms: 1.18x slower   |
| pprint_pformat             | 956 ms      | 1.13 sec: 1.18x slower |
| spectral_norm              | 49.4 ms     | 58.4 ms: 1.18x slower  |
| pickle_pure_python         | 199 us      | 236 us: 1.18x slower   |
| coverage                   | 47.5 ms     | 56.4 ms: 1.19x slower  |
| many_optionals             | 685 us      | 813 us: 1.19x slower   |
| deepcopy                   | 167 us      | 199 us: 1.19x slower   |
| richards                   | 29.4 ms     | 35.0 ms: 1.19x slower  |
| mako                       | 6.25 ms     | 7.44 ms: 1.19x slower  |
| nqueens                    | 55.2 ms     | 65.7 ms: 1.19x slower  |
| hexiom                     | 3.49 ms     | 4.17 ms: 1.19x slower  |
| regex_effbot               | 1.47 ms     | 1.76 ms: 1.20x slower  |
| richards_super             | 33.7 ms     | 40.4 ms: 1.20x slower  |
| scimark_monte_carlo        | 35.6 ms     | 42.9 ms: 1.20x slower  |
| scimark_sor                | 60.5 ms     | 73.9 ms: 1.22x slower  |
| json_dumps                 | 6.40 ms     | 7.94 ms: 1.24x slower  |
| json                       | 3.04 ms     | 3.77 ms: 1.24x slower  |
| unpickle_pure_python       | 124 us      | 154 us: 1.24x slower   |
| comprehensions             | 9.76 us     | 12.2 us: 1.25x slower  |
| xml_etree_generate         | 53.1 ms     | 66.8 ms: 1.26x slower  |
| xml_etree_process          | 36.8 ms     | 46.5 ms: 1.26x slower  |
| deepcopy_memo              | 16.8 us     | 21.3 us: 1.27x slower  |
| logging_silent             | 49.7 ns     | 62.9 ns: 1.27x slower  |
| deepcopy_reduce            | 1.68 us     | 2.12 us: 1.27x slower  |
| scimark_lu                 | 50.3 ms     | 65.2 ms: 1.30x slower  |
| gc_traversal               | 2.12 ms     | 2.77 ms: 1.31x slower  |
| json_loads                 | 14.5 us     | 21.1 us: 1.46x slower  |
| Geometric mean             | (ref)       | 1.14x slower           |

Benchmark hidden because not significant (1): connected_components
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.121x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown