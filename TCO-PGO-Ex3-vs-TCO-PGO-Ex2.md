# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 215 ms: 1.10x faster   |
| docutils       | 1.81 sec    | 1.66 sec: 1.10x faster |
| html5lib       | 40.8 ms     | 37.8 ms: 1.08x faster  |
| sphinx         | 723 ms      | 641 ms: 1.13x faster   |
| Geometric mean | (ref)       | 1.10x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------------------|:-----------:|:---------------------:|
| coroutines                 | 13.5 ms     | 12.0 ms: 1.13x faster |
| async_tree_io              | 429 ms      | 382 ms: 1.12x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 330 ms: 1.11x faster  |
| async_tree_io_tg           | 419 ms      | 377 ms: 1.11x faster  |
| async_generators           | 224 ms      | 201 ms: 1.11x faster  |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster  |
| async_tree_memoization     | 227 ms      | 205 ms: 1.11x faster  |
| async_tree_none_tg         | 178 ms      | 161 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 330 ms: 1.10x faster  |
| async_tree_memoization_tg  | 218 ms      | 208 ms: 1.05x faster  |
| asyncio_websockets         | 304 ms      | 313 ms: 1.03x slower  |
| Geometric mean             | (ref)       | 1.09x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-----------:|:---------------------:|
| float          | 44.8 ms     | 42.0 ms: 1.07x faster |
| nbody          | 58.8 ms     | 55.6 ms: 1.06x faster |
| pidigits       | 147 ms      | 145 ms: 1.01x faster  |
| Geometric mean | (ref)       | 1.04x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.76 ms     | 1.47 ms: 1.20x faster |
| regex_v8       | 16.7 ms     | 14.2 ms: 1.17x faster |
| regex_compile  | 88.0 ms     | 79.4 ms: 1.11x faster |
| regex_dna      | 117 ms      | 120 ms: 1.02x slower  |
| Geometric mean | (ref)       | 1.11x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 14.5 us: 1.46x faster  |
| xml_etree_process    | 46.5 ms     | 36.8 ms: 1.26x faster  |
| xml_etree_generate   | 66.8 ms     | 53.1 ms: 1.26x faster  |
| unpickle_pure_python | 154 us      | 124 us: 1.24x faster   |
| json_dumps           | 7.94 ms     | 6.40 ms: 1.24x faster  |
| pickle_pure_python   | 236 us      | 199 us: 1.18x faster   |
| tomli_loads          | 1.38 sec    | 1.17 sec: 1.18x faster |
| xml_etree_iterparse  | 71.5 ms     | 61.2 ms: 1.17x faster  |
| xml_etree_parse      | 104 ms      | 89.4 ms: 1.16x faster  |
| Geometric mean       | (ref)       | 1.24x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.9 ms     | 24.7 ms: 1.09x faster |
| python_startup_no_site | 20.1 ms     | 18.6 ms: 1.08x faster |
| Geometric mean         | (ref)       | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|-----------------|:-----------:|:---------------------:|
| mako            | 7.44 ms     | 6.25 ms: 1.19x faster |
| django_template | 27.5 ms     | 23.6 ms: 1.17x faster |
| genshi_text     | 16.2 ms     | 14.3 ms: 1.13x faster |
| genshi_xml      | 35.3 ms     | 32.3 ms: 1.09x faster |
| Geometric mean  | (ref)       | 1.14x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------------------|:-----------:|:----------------------:|
| json_loads                 | 21.1 us     | 14.5 us: 1.46x faster  |
| gc_traversal               | 2.77 ms     | 2.12 ms: 1.31x faster  |
| scimark_lu                 | 65.2 ms     | 50.3 ms: 1.30x faster  |
| deepcopy_reduce            | 2.12 us     | 1.68 us: 1.27x faster  |
| logging_silent             | 62.9 ns     | 49.7 ns: 1.27x faster  |
| deepcopy_memo              | 21.3 us     | 16.8 us: 1.27x faster  |
| xml_etree_process          | 46.5 ms     | 36.8 ms: 1.26x faster  |
| xml_etree_generate         | 66.8 ms     | 53.1 ms: 1.26x faster  |
| comprehensions             | 12.2 us     | 9.76 us: 1.25x faster  |
| unpickle_pure_python       | 154 us      | 124 us: 1.24x faster   |
| json                       | 3.77 ms     | 3.04 ms: 1.24x faster  |
| json_dumps                 | 7.94 ms     | 6.40 ms: 1.24x faster  |
| scimark_sor                | 73.9 ms     | 60.5 ms: 1.22x faster  |
| scimark_monte_carlo        | 42.9 ms     | 35.6 ms: 1.20x faster  |
| richards_super             | 40.4 ms     | 33.7 ms: 1.20x faster  |
| regex_effbot               | 1.76 ms     | 1.47 ms: 1.20x faster  |
| hexiom                     | 4.17 ms     | 3.49 ms: 1.19x faster  |
| nqueens                    | 65.7 ms     | 55.2 ms: 1.19x faster  |
| mako                       | 7.44 ms     | 6.25 ms: 1.19x faster  |
| richards                   | 35.0 ms     | 29.4 ms: 1.19x faster  |
| deepcopy                   | 199 us      | 167 us: 1.19x faster   |
| many_optionals             | 813 us      | 685 us: 1.19x faster   |
| coverage                   | 56.4 ms     | 47.5 ms: 1.19x faster  |
| pickle_pure_python         | 236 us      | 199 us: 1.18x faster   |
| spectral_norm              | 58.4 ms     | 49.4 ms: 1.18x faster  |
| pprint_pformat             | 1.13 sec    | 956 ms: 1.18x faster   |
| fannkuch                   | 265 ms      | 225 ms: 1.18x faster   |
| tomli_loads                | 1.38 sec    | 1.17 sec: 1.18x faster |
| pprint_safe_repr           | 558 ms      | 474 ms: 1.18x faster   |
| regex_v8                   | 16.7 ms     | 14.2 ms: 1.17x faster  |
| chaos                      | 41.4 ms     | 35.4 ms: 1.17x faster  |
| xml_etree_iterparse        | 71.5 ms     | 61.2 ms: 1.17x faster  |
| django_template            | 27.5 ms     | 23.6 ms: 1.17x faster  |
| bpe_tokeniser              | 3.17 sec    | 2.72 sec: 1.16x faster |
| sqlglot_v2_optimize        | 38.4 ms     | 32.9 ms: 1.16x faster  |
| telco                      | 5.33 ms     | 4.59 ms: 1.16x faster  |
| xml_etree_parse            | 104 ms      | 89.4 ms: 1.16x faster  |
| scimark_fft                | 178 ms      | 153 ms: 1.16x faster   |
| raytrace                   | 187 ms      | 162 ms: 1.16x faster   |
| typing_runtime_protocols   | 113 us      | 97.8 us: 1.15x faster  |
| sympy_expand               | 324 ms      | 283 ms: 1.15x faster   |
| sqlglot_v2_normalize       | 79.0 ms     | 69.0 ms: 1.14x faster  |
| thrift                     | 561 us      | 491 us: 1.14x faster   |
| subparsers                 | 47.1 ms     | 41.4 ms: 1.14x faster  |
| logging_simple             | 6.67 us     | 5.87 us: 1.14x faster  |
| sympy_sum                  | 96.6 ms     | 85.2 ms: 1.13x faster  |
| genshi_text                | 16.2 ms     | 14.3 ms: 1.13x faster  |
| sphinx                     | 723 ms      | 641 ms: 1.13x faster   |
| coroutines                 | 13.5 ms     | 12.0 ms: 1.13x faster  |
| async_tree_io              | 429 ms      | 382 ms: 1.12x faster   |
| crypto_pyaes               | 49.3 ms     | 43.9 ms: 1.12x faster  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.21 ms: 1.12x faster  |
| sqlglot_v2_parse           | 876 us      | 781 us: 1.12x faster   |
| logging_format             | 7.18 us     | 6.42 us: 1.12x faster  |
| pyflate                    | 295 ms      | 264 ms: 1.12x faster   |
| async_tree_cpu_io_mixed_tg | 367 ms      | 330 ms: 1.11x faster   |
| async_tree_io_tg           | 419 ms      | 377 ms: 1.11x faster   |
| async_generators           | 224 ms      | 201 ms: 1.11x faster   |
| pycparser                  | 765 ms      | 689 ms: 1.11x faster   |
| regex_compile              | 88.0 ms     | 79.4 ms: 1.11x faster  |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster   |
| deltablue                  | 2.09 ms     | 1.88 ms: 1.11x faster  |
| go                         | 78.0 ms     | 70.5 ms: 1.11x faster  |
| async_tree_memoization     | 227 ms      | 205 ms: 1.11x faster   |
| create_gc_cycles           | 1.38 ms     | 1.25 ms: 1.11x faster  |
| async_tree_none_tg         | 178 ms      | 161 ms: 1.10x faster   |
| 2to3                       | 237 ms      | 215 ms: 1.10x faster   |
| meteor_contest             | 78.1 ms     | 70.9 ms: 1.10x faster  |
| sqlglot_v2_transpile       | 1.09 ms     | 993 us: 1.10x faster   |
| mdp                        | 1.57 sec    | 1.43 sec: 1.10x faster |
| async_tree_cpu_io_mixed    | 362 ms      | 330 ms: 1.10x faster   |
| generators                 | 18.1 ms     | 16.5 ms: 1.10x faster  |
| docutils                   | 1.81 sec    | 1.66 sec: 1.10x faster |
| genshi_xml                 | 35.3 ms     | 32.3 ms: 1.09x faster  |
| python_startup             | 26.9 ms     | 24.7 ms: 1.09x faster  |
| sympy_integrate            | 13.9 ms     | 12.8 ms: 1.08x faster  |
| python_startup_no_site     | 20.1 ms     | 18.6 ms: 1.08x faster  |
| html5lib                   | 40.8 ms     | 37.8 ms: 1.08x faster  |
| pylint                     | 217 ms      | 201 ms: 1.08x faster   |
| sqlite_synth               | 1.68 us     | 1.56 us: 1.08x faster  |
| sympy_str                  | 187 ms      | 173 ms: 1.08x faster   |
| dulwich_log                | 43.0 ms     | 40.3 ms: 1.07x faster  |
| float                      | 44.8 ms     | 42.0 ms: 1.07x faster  |
| pathlib                    | 25.6 ms     | 24.2 ms: 1.06x faster  |
| nbody                      | 58.8 ms     | 55.6 ms: 1.06x faster  |
| async_tree_memoization_tg  | 218 ms      | 208 ms: 1.05x faster   |
| k_core                     | 1.76 sec    | 1.70 sec: 1.03x faster |
| shortest_path              | 357 ms      | 352 ms: 1.02x faster   |
| pidigits                   | 147 ms      | 145 ms: 1.01x faster   |
| regex_dna                  | 117 ms      | 120 ms: 1.02x slower   |
| asyncio_websockets         | 304 ms      | 313 ms: 1.03x slower   |
| Geometric mean             | (ref)       | 1.14x faster           |

Benchmark hidden because not significant (1): connected_components
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown