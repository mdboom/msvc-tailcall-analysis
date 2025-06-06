# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO                    |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 227 ms: 1.07x slower   |
| docutils       | 1.67 sec    | 1.68 sec: 1.01x slower |
| html5lib       | 37.9 ms     | 40.8 ms: 1.07x slower  |
| sphinx         | 645 ms      | 658 ms: 1.02x slower   |
| Geometric mean | (ref)       | 1.04x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | PGO                   |
|----------------------------|:-----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 330 ms      | 339 ms: 1.03x slower  |
| async_tree_memoization_tg  | 208 ms      | 216 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 343 ms: 1.04x slower  |
| asyncio_websockets         | 301 ms      | 318 ms: 1.06x slower  |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower  |
| async_tree_memoization     | 206 ms      | 224 ms: 1.09x slower  |
| async_tree_none            | 170 ms      | 187 ms: 1.10x slower  |
| async_tree_io              | 384 ms      | 423 ms: 1.10x slower  |
| async_tree_none_tg         | 159 ms      | 176 ms: 1.11x slower  |
| async_generators           | 202 ms      | 226 ms: 1.12x slower  |
| coroutines                 | 11.9 ms     | 13.5 ms: 1.13x slower |
| Geometric mean             | (ref)       | 1.08x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO                   |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 152 ms: 1.05x slower  |
| float          | 41.9 ms     | 47.8 ms: 1.14x slower |
| nbody          | 55.2 ms     | 74.1 ms: 1.34x slower |
| Geometric mean | (ref)       | 1.17x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | PGO                   |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 112 ms: 1.07x faster  |
| regex_effbot   | 1.46 ms     | 1.42 ms: 1.03x faster |
| regex_compile  | 78.1 ms     | 88.2 ms: 1.13x slower |
| Geometric mean | (ref)       | 1.01x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | PGO                    |
|----------------------|:-----------:|:----------------------:|
| xml_etree_parse      | 89.3 ms     | 91.2 ms: 1.02x slower  |
| xml_etree_iterparse  | 61.2 ms     | 63.7 ms: 1.04x slower  |
| json_dumps           | 6.55 ms     | 7.05 ms: 1.08x slower  |
| xml_etree_generate   | 53.6 ms     | 58.7 ms: 1.09x slower  |
| xml_etree_process    | 37.0 ms     | 41.5 ms: 1.12x slower  |
| pickle_pure_python   | 199 us      | 237 us: 1.19x slower   |
| unpickle_pure_python | 127 us      | 155 us: 1.22x slower   |
| tomli_loads          | 1.18 sec    | 1.47 sec: 1.25x slower |
| Geometric mean       | (ref)       | 1.11x slower           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | PGO                   |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 24.7 ms     | 26.1 ms: 1.06x slower |
| python_startup_no_site | 18.7 ms     | 19.8 ms: 1.06x slower |
| Geometric mean         | (ref)       | 1.06x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | PGO                   |
|-----------------|:-----------:|:---------------------:|
| mako            | 6.28 ms     | 6.86 ms: 1.09x slower |
| django_template | 22.9 ms     | 25.1 ms: 1.10x slower |
| genshi_xml      | 32.8 ms     | 36.3 ms: 1.11x slower |
| genshi_text     | 14.3 ms     | 16.5 ms: 1.16x slower |
| Geometric mean  | (ref)       | 1.11x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | PGO                    |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 40.7 ms     | 16.1 ms: 2.53x faster  |
| many_optionals             | 665 us      | 438 us: 1.52x faster   |
| regex_dna                  | 120 ms      | 112 ms: 1.07x faster   |
| coverage                   | 48.2 ms     | 46.8 ms: 1.03x faster  |
| regex_effbot               | 1.46 ms     | 1.42 ms: 1.03x faster  |
| gc_traversal               | 2.11 ms     | 2.06 ms: 1.02x faster  |
| create_gc_cycles           | 1.27 ms     | 1.25 ms: 1.02x faster  |
| docutils                   | 1.67 sec    | 1.68 sec: 1.01x slower |
| connected_components       | 326 ms      | 329 ms: 1.01x slower   |
| mdp                        | 1.62 sec    | 1.64 sec: 1.01x slower |
| sqlite_synth               | 1.56 us     | 1.59 us: 1.02x slower  |
| shortest_path              | 353 ms      | 359 ms: 1.02x slower   |
| sphinx                     | 645 ms      | 658 ms: 1.02x slower   |
| xml_etree_parse            | 89.3 ms     | 91.2 ms: 1.02x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 339 ms: 1.03x slower   |
| async_tree_memoization_tg  | 208 ms      | 216 ms: 1.03x slower   |
| async_tree_cpu_io_mixed_tg | 329 ms      | 343 ms: 1.04x slower   |
| xml_etree_iterparse        | 61.2 ms     | 63.7 ms: 1.04x slower  |
| sympy_sum                  | 86.3 ms     | 90.5 ms: 1.05x slower  |
| pidigits                   | 145 ms      | 152 ms: 1.05x slower   |
| thrift                     | 482 us      | 507 us: 1.05x slower   |
| sympy_integrate            | 12.8 ms     | 13.5 ms: 1.05x slower  |
| crypto_pyaes               | 47.4 ms     | 50.0 ms: 1.05x slower  |
| python_startup             | 24.7 ms     | 26.1 ms: 1.06x slower  |
| json                       | 2.97 ms     | 3.14 ms: 1.06x slower  |
| asyncio_websockets         | 301 ms      | 318 ms: 1.06x slower   |
| python_startup_no_site     | 18.7 ms     | 19.8 ms: 1.06x slower  |
| sqlglot_v2_optimize        | 33.0 ms     | 35.0 ms: 1.06x slower  |
| sqlglot_v2_normalize       | 69.3 ms     | 73.6 ms: 1.06x slower  |
| richards_super             | 33.1 ms     | 35.1 ms: 1.06x slower  |
| richards                   | 28.7 ms     | 30.7 ms: 1.07x slower  |
| telco                      | 4.57 ms     | 4.89 ms: 1.07x slower  |
| sympy_expand               | 282 ms      | 302 ms: 1.07x slower   |
| sympy_str                  | 164 ms      | 176 ms: 1.07x slower   |
| 2to3                       | 212 ms      | 227 ms: 1.07x slower   |
| typing_runtime_protocols   | 98.8 us     | 106 us: 1.07x slower   |
| html5lib                   | 37.9 ms     | 40.8 ms: 1.07x slower  |
| json_dumps                 | 6.55 ms     | 7.05 ms: 1.08x slower  |
| pycparser                  | 686 ms      | 738 ms: 1.08x slower   |
| dulwich_log                | 40.2 ms     | 43.4 ms: 1.08x slower  |
| logging_format             | 6.50 us     | 7.03 us: 1.08x slower  |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower   |
| bpe_tokeniser              | 2.72 sec    | 2.96 sec: 1.09x slower |
| async_tree_memoization     | 206 ms      | 224 ms: 1.09x slower   |
| mako                       | 6.28 ms     | 6.86 ms: 1.09x slower  |
| logging_simple             | 5.97 us     | 6.53 us: 1.09x slower  |
| meteor_contest             | 70.2 ms     | 76.9 ms: 1.09x slower  |
| xml_etree_generate         | 53.6 ms     | 58.7 ms: 1.09x slower  |
| async_tree_none            | 170 ms      | 187 ms: 1.10x slower   |
| django_template            | 22.9 ms     | 25.1 ms: 1.10x slower  |
| async_tree_io              | 384 ms      | 423 ms: 1.10x slower   |
| genshi_xml                 | 32.8 ms     | 36.3 ms: 1.11x slower  |
| async_tree_none_tg         | 159 ms      | 176 ms: 1.11x slower   |
| async_generators           | 202 ms      | 226 ms: 1.12x slower   |
| xml_etree_process          | 37.0 ms     | 41.5 ms: 1.12x slower  |
| regex_compile              | 78.1 ms     | 88.2 ms: 1.13x slower  |
| coroutines                 | 11.9 ms     | 13.5 ms: 1.13x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.10 ms: 1.14x slower  |
| deepcopy                   | 167 us      | 190 us: 1.14x slower   |
| float                      | 41.9 ms     | 47.8 ms: 1.14x slower  |
| deepcopy_reduce            | 1.70 us     | 1.94 us: 1.14x slower  |
| comprehensions             | 9.87 us     | 11.3 us: 1.15x slower  |
| genshi_text                | 14.3 ms     | 16.5 ms: 1.16x slower  |
| pprint_pformat             | 967 ms      | 1.13 sec: 1.16x slower |
| sqlglot_v2_parse           | 766 us      | 892 us: 1.16x slower   |
| nqueens                    | 54.4 ms     | 63.6 ms: 1.17x slower  |
| generators                 | 16.5 ms     | 19.3 ms: 1.17x slower  |
| pyflate                    | 268 ms      | 315 ms: 1.18x slower   |
| chaos                      | 36.9 ms     | 43.6 ms: 1.18x slower  |
| pprint_safe_repr           | 470 ms      | 558 ms: 1.19x slower   |
| pickle_pure_python         | 199 us      | 237 us: 1.19x slower   |
| raytrace                   | 160 ms      | 191 ms: 1.19x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 2.72 ms: 1.20x slower  |
| deltablue                  | 1.88 ms     | 2.29 ms: 1.22x slower  |
| unpickle_pure_python       | 127 us      | 155 us: 1.22x slower   |
| hexiom                     | 3.54 ms     | 4.38 ms: 1.24x slower  |
| spectral_norm              | 49.4 ms     | 61.5 ms: 1.25x slower  |
| tomli_loads                | 1.18 sec    | 1.47 sec: 1.25x slower |
| scimark_fft                | 154 ms      | 192 ms: 1.25x slower   |
| go                         | 70.9 ms     | 88.6 ms: 1.25x slower  |
| deepcopy_memo              | 16.6 us     | 21.0 us: 1.27x slower  |
| scimark_monte_carlo        | 36.0 ms     | 47.1 ms: 1.31x slower  |
| scimark_lu                 | 50.9 ms     | 66.9 ms: 1.31x slower  |
| logging_silent             | 49.4 ns     | 65.2 ns: 1.32x slower  |
| fannkuch                   | 223 ms      | 296 ms: 1.33x slower   |
| pathlib                    | 24.1 ms     | 32.1 ms: 1.33x slower  |
| nbody                      | 55.2 ms     | 74.1 ms: 1.34x slower  |
| scimark_sor                | 61.1 ms     | 91.0 ms: 1.49x slower  |
| Geometric mean             | (ref)       | 1.09x slower           |

Benchmark hidden because not significant (4): json_loads, pylint, k_core, regex_v8
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.081x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown