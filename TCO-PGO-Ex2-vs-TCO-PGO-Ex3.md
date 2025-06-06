# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.120x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 237 ms: 1.12x slower   |
| docutils       | 1.67 sec    | 1.81 sec: 1.09x slower |
| html5lib       | 37.9 ms     | 40.8 ms: 1.08x slower  |
| sphinx         | 645 ms      | 723 ms: 1.12x slower   |
| Geometric mean | (ref)       | 1.10x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 301 ms      | 304 ms: 1.01x slower  |
| async_tree_memoization_tg  | 208 ms      | 218 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 362 ms: 1.10x slower  |
| async_tree_memoization     | 206 ms      | 227 ms: 1.10x slower  |
| async_generators           | 202 ms      | 224 ms: 1.10x slower  |
| async_tree_none            | 170 ms      | 188 ms: 1.11x slower  |
| async_tree_io_tg           | 377 ms      | 419 ms: 1.11x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 367 ms: 1.12x slower  |
| async_tree_none_tg         | 159 ms      | 178 ms: 1.12x slower  |
| async_tree_io              | 384 ms      | 429 ms: 1.12x slower  |
| coroutines                 | 11.9 ms     | 13.5 ms: 1.13x slower |
| Geometric mean             | (ref)       | 1.10x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 147 ms: 1.01x slower  |
| nbody          | 55.2 ms     | 58.8 ms: 1.06x slower |
| float          | 41.9 ms     | 44.8 ms: 1.07x slower |
| Geometric mean | (ref)       | 1.05x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 117 ms: 1.03x faster  |
| regex_compile  | 78.1 ms     | 88.0 ms: 1.13x slower |
| regex_effbot   | 1.46 ms     | 1.76 ms: 1.21x slower |
| regex_v8       | 13.2 ms     | 16.7 ms: 1.26x slower |
| Geometric mean | (ref)       | 1.14x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.3 ms     | 104 ms: 1.16x slower   |
| xml_etree_iterparse  | 61.2 ms     | 71.5 ms: 1.17x slower  |
| tomli_loads          | 1.18 sec    | 1.38 sec: 1.18x slower |
| pickle_pure_python   | 199 us      | 236 us: 1.18x slower   |
| unpickle_pure_python | 127 us      | 154 us: 1.21x slower   |
| json_dumps           | 6.55 ms     | 7.94 ms: 1.21x slower  |
| xml_etree_generate   | 53.6 ms     | 66.8 ms: 1.25x slower  |
| xml_etree_process    | 37.0 ms     | 46.5 ms: 1.26x slower  |
| json_loads           | 14.7 us     | 21.1 us: 1.43x slower  |
| Geometric mean       | (ref)       | 1.22x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 20.1 ms: 1.07x slower |
| python_startup         | 24.7 ms     | 26.9 ms: 1.09x slower |
| Geometric mean         | (ref)       | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TCO-PGO-Ex2           |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 35.3 ms: 1.08x slower |
| genshi_text     | 14.3 ms     | 16.2 ms: 1.13x slower |
| mako            | 6.28 ms     | 7.44 ms: 1.18x slower |
| django_template | 22.9 ms     | 27.5 ms: 1.20x slower |
| Geometric mean  | (ref)       | 1.15x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------------|:-----------:|:----------------------:|
| mdp                        | 1.62 sec    | 1.57 sec: 1.03x faster |
| regex_dna                  | 120 ms      | 117 ms: 1.03x faster   |
| pidigits                   | 145 ms      | 147 ms: 1.01x slower   |
| asyncio_websockets         | 301 ms      | 304 ms: 1.01x slower   |
| shortest_path              | 353 ms      | 357 ms: 1.01x slower   |
| k_core                     | 1.71 sec    | 1.76 sec: 1.03x slower |
| crypto_pyaes               | 47.4 ms     | 49.3 ms: 1.04x slower  |
| async_tree_memoization_tg  | 208 ms      | 218 ms: 1.05x slower   |
| pathlib                    | 24.1 ms     | 25.6 ms: 1.06x slower  |
| nbody                      | 55.2 ms     | 58.8 ms: 1.06x slower  |
| float                      | 41.9 ms     | 44.8 ms: 1.07x slower  |
| dulwich_log                | 40.2 ms     | 43.0 ms: 1.07x slower  |
| python_startup_no_site     | 18.7 ms     | 20.1 ms: 1.07x slower  |
| genshi_xml                 | 32.8 ms     | 35.3 ms: 1.08x slower  |
| html5lib                   | 37.9 ms     | 40.8 ms: 1.08x slower  |
| sqlite_synth               | 1.56 us     | 1.68 us: 1.08x slower  |
| sympy_integrate            | 12.8 ms     | 13.9 ms: 1.08x slower  |
| python_startup             | 24.7 ms     | 26.9 ms: 1.09x slower  |
| create_gc_cycles           | 1.27 ms     | 1.38 ms: 1.09x slower  |
| docutils                   | 1.67 sec    | 1.81 sec: 1.09x slower |
| pylint                     | 198 ms      | 217 ms: 1.09x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 2.48 ms: 1.09x slower  |
| generators                 | 16.5 ms     | 18.1 ms: 1.10x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 362 ms: 1.10x slower   |
| pyflate                    | 268 ms      | 295 ms: 1.10x slower   |
| go                         | 70.9 ms     | 78.0 ms: 1.10x slower  |
| async_tree_memoization     | 206 ms      | 227 ms: 1.10x slower   |
| async_generators           | 202 ms      | 224 ms: 1.10x slower   |
| logging_format             | 6.50 us     | 7.18 us: 1.11x slower  |
| async_tree_none            | 170 ms      | 188 ms: 1.11x slower   |
| deltablue                  | 1.88 ms     | 2.09 ms: 1.11x slower  |
| meteor_contest             | 70.2 ms     | 78.1 ms: 1.11x slower  |
| async_tree_io_tg           | 377 ms      | 419 ms: 1.11x slower   |
| pycparser                  | 686 ms      | 765 ms: 1.12x slower   |
| async_tree_cpu_io_mixed_tg | 329 ms      | 367 ms: 1.12x slower   |
| logging_simple             | 5.97 us     | 6.67 us: 1.12x slower  |
| async_tree_none_tg         | 159 ms      | 178 ms: 1.12x slower   |
| sympy_sum                  | 86.3 ms     | 96.6 ms: 1.12x slower  |
| async_tree_io              | 384 ms      | 429 ms: 1.12x slower   |
| sphinx                     | 645 ms      | 723 ms: 1.12x slower   |
| 2to3                       | 212 ms      | 237 ms: 1.12x slower   |
| chaos                      | 36.9 ms     | 41.4 ms: 1.12x slower  |
| regex_compile              | 78.1 ms     | 88.0 ms: 1.13x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.09 ms: 1.13x slower  |
| coroutines                 | 11.9 ms     | 13.5 ms: 1.13x slower  |
| genshi_text                | 14.3 ms     | 16.2 ms: 1.13x slower  |
| sympy_str                  | 164 ms      | 187 ms: 1.14x slower   |
| sqlglot_v2_normalize       | 69.3 ms     | 79.0 ms: 1.14x slower  |
| typing_runtime_protocols   | 98.8 us     | 113 us: 1.14x slower   |
| sqlglot_v2_parse           | 766 us      | 876 us: 1.14x slower   |
| sympy_expand               | 282 ms      | 324 ms: 1.15x slower   |
| scimark_fft                | 154 ms      | 178 ms: 1.15x slower   |
| subparsers                 | 40.7 ms     | 47.1 ms: 1.16x slower  |
| xml_etree_parse            | 89.3 ms     | 104 ms: 1.16x slower   |
| sqlglot_v2_optimize        | 33.0 ms     | 38.4 ms: 1.16x slower  |
| thrift                     | 482 us      | 561 us: 1.16x slower   |
| raytrace                   | 160 ms      | 187 ms: 1.16x slower   |
| telco                      | 4.57 ms     | 5.33 ms: 1.17x slower  |
| bpe_tokeniser              | 2.72 sec    | 3.17 sec: 1.17x slower |
| pprint_pformat             | 967 ms      | 1.13 sec: 1.17x slower |
| xml_etree_iterparse        | 61.2 ms     | 71.5 ms: 1.17x slower  |
| coverage                   | 48.2 ms     | 56.4 ms: 1.17x slower  |
| tomli_loads                | 1.18 sec    | 1.38 sec: 1.18x slower |
| hexiom                     | 3.54 ms     | 4.17 ms: 1.18x slower  |
| spectral_norm              | 49.4 ms     | 58.4 ms: 1.18x slower  |
| pickle_pure_python         | 199 us      | 236 us: 1.18x slower   |
| mako                       | 6.28 ms     | 7.44 ms: 1.18x slower  |
| pprint_safe_repr           | 470 ms      | 558 ms: 1.19x slower   |
| fannkuch                   | 223 ms      | 265 ms: 1.19x slower   |
| deepcopy                   | 167 us      | 199 us: 1.19x slower   |
| scimark_monte_carlo        | 36.0 ms     | 42.9 ms: 1.19x slower  |
| django_template            | 22.9 ms     | 27.5 ms: 1.20x slower  |
| regex_effbot               | 1.46 ms     | 1.76 ms: 1.21x slower  |
| scimark_sor                | 61.1 ms     | 73.9 ms: 1.21x slower  |
| nqueens                    | 54.4 ms     | 65.7 ms: 1.21x slower  |
| unpickle_pure_python       | 127 us      | 154 us: 1.21x slower   |
| json_dumps                 | 6.55 ms     | 7.94 ms: 1.21x slower  |
| richards                   | 28.7 ms     | 35.0 ms: 1.22x slower  |
| richards_super             | 33.1 ms     | 40.4 ms: 1.22x slower  |
| many_optionals             | 665 us      | 813 us: 1.22x slower   |
| comprehensions             | 9.87 us     | 12.2 us: 1.24x slower  |
| xml_etree_generate         | 53.6 ms     | 66.8 ms: 1.25x slower  |
| deepcopy_reduce            | 1.70 us     | 2.12 us: 1.25x slower  |
| xml_etree_process          | 37.0 ms     | 46.5 ms: 1.26x slower  |
| regex_v8                   | 13.2 ms     | 16.7 ms: 1.26x slower  |
| json                       | 2.97 ms     | 3.77 ms: 1.27x slower  |
| logging_silent             | 49.4 ns     | 62.9 ns: 1.27x slower  |
| scimark_lu                 | 50.9 ms     | 65.2 ms: 1.28x slower  |
| deepcopy_memo              | 16.6 us     | 21.3 us: 1.28x slower  |
| gc_traversal               | 2.11 ms     | 2.77 ms: 1.32x slower  |
| json_loads                 | 14.7 us     | 21.1 us: 1.43x slower  |
| Geometric mean             | (ref)       | 1.14x slower           |

Benchmark hidden because not significant (1): connected_components
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.120x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown