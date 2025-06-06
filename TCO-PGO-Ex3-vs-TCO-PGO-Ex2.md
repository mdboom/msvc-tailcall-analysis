# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 212 ms: 1.12x faster   |
| docutils       | 1.81 sec    | 1.67 sec: 1.09x faster |
| html5lib       | 40.8 ms     | 37.9 ms: 1.08x faster  |
| sphinx         | 723 ms      | 645 ms: 1.12x faster   |
| Geometric mean | (ref)       | 1.10x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------------------|:-----------:|:---------------------:|
| coroutines                 | 13.5 ms     | 11.9 ms: 1.13x faster |
| async_tree_io              | 429 ms      | 384 ms: 1.12x faster  |
| async_tree_none_tg         | 178 ms      | 159 ms: 1.12x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 329 ms: 1.12x faster  |
| async_tree_io_tg           | 419 ms      | 377 ms: 1.11x faster  |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster  |
| async_generators           | 224 ms      | 202 ms: 1.10x faster  |
| async_tree_memoization     | 227 ms      | 206 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 330 ms: 1.10x faster  |
| async_tree_memoization_tg  | 218 ms      | 208 ms: 1.05x faster  |
| asyncio_websockets         | 304 ms      | 301 ms: 1.01x faster  |
| Geometric mean             | (ref)       | 1.10x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-----------:|:---------------------:|
| float          | 44.8 ms     | 41.9 ms: 1.07x faster |
| nbody          | 58.8 ms     | 55.2 ms: 1.06x faster |
| pidigits       | 147 ms      | 145 ms: 1.01x faster  |
| Geometric mean | (ref)       | 1.05x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:-----------:|:---------------------:|
| regex_v8       | 16.7 ms     | 13.2 ms: 1.26x faster |
| regex_effbot   | 1.76 ms     | 1.46 ms: 1.21x faster |
| regex_compile  | 88.0 ms     | 78.1 ms: 1.13x faster |
| regex_dna      | 117 ms      | 120 ms: 1.03x slower  |
| Geometric mean | (ref)       | 1.14x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 14.7 us: 1.43x faster  |
| xml_etree_process    | 46.5 ms     | 37.0 ms: 1.26x faster  |
| xml_etree_generate   | 66.8 ms     | 53.6 ms: 1.25x faster  |
| json_dumps           | 7.94 ms     | 6.55 ms: 1.21x faster  |
| unpickle_pure_python | 154 us      | 127 us: 1.21x faster   |
| pickle_pure_python   | 236 us      | 199 us: 1.18x faster   |
| tomli_loads          | 1.38 sec    | 1.18 sec: 1.18x faster |
| xml_etree_iterparse  | 71.5 ms     | 61.2 ms: 1.17x faster  |
| xml_etree_parse      | 104 ms      | 89.3 ms: 1.16x faster  |
| Geometric mean       | (ref)       | 1.22x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.9 ms     | 24.7 ms: 1.09x faster |
| python_startup_no_site | 20.1 ms     | 18.7 ms: 1.07x faster |
| Geometric mean         | (ref)       | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TCO-PGO-Ex3           |
|-----------------|:-----------:|:---------------------:|
| django_template | 27.5 ms     | 22.9 ms: 1.20x faster |
| mako            | 7.44 ms     | 6.28 ms: 1.18x faster |
| genshi_text     | 16.2 ms     | 14.3 ms: 1.13x faster |
| genshi_xml      | 35.3 ms     | 32.8 ms: 1.08x faster |
| Geometric mean  | (ref)       | 1.15x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------------------|:-----------:|:----------------------:|
| json_loads                 | 21.1 us     | 14.7 us: 1.43x faster  |
| gc_traversal               | 2.77 ms     | 2.11 ms: 1.32x faster  |
| deepcopy_memo              | 21.3 us     | 16.6 us: 1.28x faster  |
| scimark_lu                 | 65.2 ms     | 50.9 ms: 1.28x faster  |
| logging_silent             | 62.9 ns     | 49.4 ns: 1.27x faster  |
| json                       | 3.77 ms     | 2.97 ms: 1.27x faster  |
| regex_v8                   | 16.7 ms     | 13.2 ms: 1.26x faster  |
| xml_etree_process          | 46.5 ms     | 37.0 ms: 1.26x faster  |
| deepcopy_reduce            | 2.12 us     | 1.70 us: 1.25x faster  |
| xml_etree_generate         | 66.8 ms     | 53.6 ms: 1.25x faster  |
| comprehensions             | 12.2 us     | 9.87 us: 1.24x faster  |
| many_optionals             | 813 us      | 665 us: 1.22x faster   |
| richards_super             | 40.4 ms     | 33.1 ms: 1.22x faster  |
| richards                   | 35.0 ms     | 28.7 ms: 1.22x faster  |
| json_dumps                 | 7.94 ms     | 6.55 ms: 1.21x faster  |
| unpickle_pure_python       | 154 us      | 127 us: 1.21x faster   |
| nqueens                    | 65.7 ms     | 54.4 ms: 1.21x faster  |
| scimark_sor                | 73.9 ms     | 61.1 ms: 1.21x faster  |
| regex_effbot               | 1.76 ms     | 1.46 ms: 1.21x faster  |
| django_template            | 27.5 ms     | 22.9 ms: 1.20x faster  |
| scimark_monte_carlo        | 42.9 ms     | 36.0 ms: 1.19x faster  |
| deepcopy                   | 199 us      | 167 us: 1.19x faster   |
| fannkuch                   | 265 ms      | 223 ms: 1.19x faster   |
| pprint_safe_repr           | 558 ms      | 470 ms: 1.19x faster   |
| mako                       | 7.44 ms     | 6.28 ms: 1.18x faster  |
| pickle_pure_python         | 236 us      | 199 us: 1.18x faster   |
| spectral_norm              | 58.4 ms     | 49.4 ms: 1.18x faster  |
| hexiom                     | 4.17 ms     | 3.54 ms: 1.18x faster  |
| tomli_loads                | 1.38 sec    | 1.18 sec: 1.18x faster |
| coverage                   | 56.4 ms     | 48.2 ms: 1.17x faster  |
| xml_etree_iterparse        | 71.5 ms     | 61.2 ms: 1.17x faster  |
| pprint_pformat             | 1.13 sec    | 967 ms: 1.17x faster   |
| bpe_tokeniser              | 3.17 sec    | 2.72 sec: 1.17x faster |
| telco                      | 5.33 ms     | 4.57 ms: 1.17x faster  |
| raytrace                   | 187 ms      | 160 ms: 1.16x faster   |
| thrift                     | 561 us      | 482 us: 1.16x faster   |
| sqlglot_v2_optimize        | 38.4 ms     | 33.0 ms: 1.16x faster  |
| xml_etree_parse            | 104 ms      | 89.3 ms: 1.16x faster  |
| subparsers                 | 47.1 ms     | 40.7 ms: 1.16x faster  |
| scimark_fft                | 178 ms      | 154 ms: 1.15x faster   |
| sympy_expand               | 324 ms      | 282 ms: 1.15x faster   |
| sqlglot_v2_parse           | 876 us      | 766 us: 1.14x faster   |
| typing_runtime_protocols   | 113 us      | 98.8 us: 1.14x faster  |
| sqlglot_v2_normalize       | 79.0 ms     | 69.3 ms: 1.14x faster  |
| sympy_str                  | 187 ms      | 164 ms: 1.14x faster   |
| genshi_text                | 16.2 ms     | 14.3 ms: 1.13x faster  |
| coroutines                 | 13.5 ms     | 11.9 ms: 1.13x faster  |
| sqlglot_v2_transpile       | 1.09 ms     | 970 us: 1.13x faster   |
| regex_compile              | 88.0 ms     | 78.1 ms: 1.13x faster  |
| chaos                      | 41.4 ms     | 36.9 ms: 1.12x faster  |
| 2to3                       | 237 ms      | 212 ms: 1.12x faster   |
| sphinx                     | 723 ms      | 645 ms: 1.12x faster   |
| async_tree_io              | 429 ms      | 384 ms: 1.12x faster   |
| sympy_sum                  | 96.6 ms     | 86.3 ms: 1.12x faster  |
| async_tree_none_tg         | 178 ms      | 159 ms: 1.12x faster   |
| logging_simple             | 6.67 us     | 5.97 us: 1.12x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 329 ms: 1.12x faster   |
| pycparser                  | 765 ms      | 686 ms: 1.12x faster   |
| async_tree_io_tg           | 419 ms      | 377 ms: 1.11x faster   |
| meteor_contest             | 78.1 ms     | 70.2 ms: 1.11x faster  |
| deltablue                  | 2.09 ms     | 1.88 ms: 1.11x faster  |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster   |
| logging_format             | 7.18 us     | 6.50 us: 1.11x faster  |
| async_generators           | 224 ms      | 202 ms: 1.10x faster   |
| async_tree_memoization     | 227 ms      | 206 ms: 1.10x faster   |
| go                         | 78.0 ms     | 70.9 ms: 1.10x faster  |
| pyflate                    | 295 ms      | 268 ms: 1.10x faster   |
| async_tree_cpu_io_mixed    | 362 ms      | 330 ms: 1.10x faster   |
| generators                 | 18.1 ms     | 16.5 ms: 1.10x faster  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.27 ms: 1.09x faster  |
| pylint                     | 217 ms      | 198 ms: 1.09x faster   |
| docutils                   | 1.81 sec    | 1.67 sec: 1.09x faster |
| create_gc_cycles           | 1.38 ms     | 1.27 ms: 1.09x faster  |
| python_startup             | 26.9 ms     | 24.7 ms: 1.09x faster  |
| sympy_integrate            | 13.9 ms     | 12.8 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us     | 1.56 us: 1.08x faster  |
| html5lib                   | 40.8 ms     | 37.9 ms: 1.08x faster  |
| genshi_xml                 | 35.3 ms     | 32.8 ms: 1.08x faster  |
| python_startup_no_site     | 20.1 ms     | 18.7 ms: 1.07x faster  |
| dulwich_log                | 43.0 ms     | 40.2 ms: 1.07x faster  |
| float                      | 44.8 ms     | 41.9 ms: 1.07x faster  |
| nbody                      | 58.8 ms     | 55.2 ms: 1.06x faster  |
| pathlib                    | 25.6 ms     | 24.1 ms: 1.06x faster  |
| async_tree_memoization_tg  | 218 ms      | 208 ms: 1.05x faster   |
| crypto_pyaes               | 49.3 ms     | 47.4 ms: 1.04x faster  |
| k_core                     | 1.76 sec    | 1.71 sec: 1.03x faster |
| shortest_path              | 357 ms      | 353 ms: 1.01x faster   |
| asyncio_websockets         | 304 ms      | 301 ms: 1.01x faster   |
| pidigits                   | 147 ms      | 145 ms: 1.01x faster   |
| regex_dna                  | 117 ms      | 120 ms: 1.03x slower   |
| mdp                        | 1.57 sec    | 1.62 sec: 1.03x slower |
| Geometric mean             | (ref)       | 1.14x faster           |

Benchmark hidden because not significant (1): connected_components
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown