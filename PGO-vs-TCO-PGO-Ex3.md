# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO                    |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 227 ms: 1.06x slower   |
| docutils       | 1.66 sec    | 1.68 sec: 1.01x slower |
| html5lib       | 37.8 ms     | 40.8 ms: 1.08x slower  |
| sphinx         | 641 ms      | 658 ms: 1.03x slower   |
| Geometric mean | (ref)       | 1.04x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | PGO                   |
|----------------------------|:-----------:|:---------------------:|
| asyncio_websockets         | 313 ms      | 318 ms: 1.02x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 339 ms: 1.03x slower  |
| async_tree_memoization_tg  | 208 ms      | 216 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 343 ms: 1.04x slower  |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower  |
| async_tree_memoization     | 205 ms      | 224 ms: 1.09x slower  |
| async_tree_none_tg         | 161 ms      | 176 ms: 1.10x slower  |
| async_tree_none            | 170 ms      | 187 ms: 1.10x slower  |
| async_tree_io              | 382 ms      | 423 ms: 1.11x slower  |
| async_generators           | 201 ms      | 226 ms: 1.13x slower  |
| coroutines                 | 12.0 ms     | 13.5 ms: 1.13x slower |
| Geometric mean             | (ref)       | 1.08x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | PGO                   |
|----------------|:-----------:|:---------------------:|
| pidigits       | 145 ms      | 152 ms: 1.05x slower  |
| float          | 42.0 ms     | 47.8 ms: 1.14x slower |
| nbody          | 55.6 ms     | 74.1 ms: 1.33x slower |
| Geometric mean | (ref)       | 1.17x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | PGO                   |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 112 ms: 1.07x faster  |
| regex_v8       | 14.2 ms     | 13.5 ms: 1.05x faster |
| regex_effbot   | 1.47 ms     | 1.42 ms: 1.03x faster |
| regex_compile  | 79.4 ms     | 88.2 ms: 1.11x slower |
| Geometric mean | (ref)       | 1.01x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | PGO                    |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 14.5 us     | 14.7 us: 1.02x slower  |
| xml_etree_parse      | 89.4 ms     | 91.2 ms: 1.02x slower  |
| xml_etree_iterparse  | 61.2 ms     | 63.7 ms: 1.04x slower  |
| json_dumps           | 6.40 ms     | 7.05 ms: 1.10x slower  |
| xml_etree_generate   | 53.1 ms     | 58.7 ms: 1.11x slower  |
| xml_etree_process    | 36.8 ms     | 41.5 ms: 1.13x slower  |
| pickle_pure_python   | 199 us      | 237 us: 1.19x slower   |
| tomli_loads          | 1.17 sec    | 1.47 sec: 1.25x slower |
| unpickle_pure_python | 124 us      | 155 us: 1.25x slower   |
| Geometric mean       | (ref)       | 1.12x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | PGO                   |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 24.7 ms     | 26.1 ms: 1.05x slower |
| python_startup_no_site | 18.6 ms     | 19.8 ms: 1.07x slower |
| Geometric mean         | (ref)       | 1.06x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | PGO                   |
|-----------------|:-----------:|:---------------------:|
| django_template | 23.6 ms     | 25.1 ms: 1.07x slower |
| mako            | 6.25 ms     | 6.86 ms: 1.10x slower |
| genshi_xml      | 32.3 ms     | 36.3 ms: 1.12x slower |
| genshi_text     | 14.3 ms     | 16.5 ms: 1.15x slower |
| Geometric mean  | (ref)       | 1.11x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | PGO                    |
|----------------------------|:-----------:|:----------------------:|
| subparsers                 | 41.4 ms     | 16.1 ms: 2.57x faster  |
| many_optionals             | 685 us      | 438 us: 1.56x faster   |
| regex_dna                  | 120 ms      | 112 ms: 1.07x faster   |
| regex_v8                   | 14.2 ms     | 13.5 ms: 1.05x faster  |
| regex_effbot               | 1.47 ms     | 1.42 ms: 1.03x faster  |
| gc_traversal               | 2.12 ms     | 2.06 ms: 1.03x faster  |
| coverage                   | 47.5 ms     | 46.8 ms: 1.02x faster  |
| connected_components       | 325 ms      | 329 ms: 1.01x slower   |
| docutils                   | 1.66 sec    | 1.68 sec: 1.01x slower |
| k_core                     | 1.70 sec    | 1.73 sec: 1.02x slower |
| json_loads                 | 14.5 us     | 14.7 us: 1.02x slower  |
| asyncio_websockets         | 313 ms      | 318 ms: 1.02x slower   |
| sympy_str                  | 173 ms      | 176 ms: 1.02x slower   |
| sqlite_synth               | 1.56 us     | 1.59 us: 1.02x slower  |
| xml_etree_parse            | 89.4 ms     | 91.2 ms: 1.02x slower  |
| shortest_path              | 352 ms      | 359 ms: 1.02x slower   |
| sphinx                     | 641 ms      | 658 ms: 1.03x slower   |
| async_tree_cpu_io_mixed    | 330 ms      | 339 ms: 1.03x slower   |
| json                       | 3.04 ms     | 3.14 ms: 1.03x slower  |
| thrift                     | 491 us      | 507 us: 1.03x slower   |
| async_tree_memoization_tg  | 208 ms      | 216 ms: 1.04x slower   |
| async_tree_cpu_io_mixed_tg | 330 ms      | 343 ms: 1.04x slower   |
| xml_etree_iterparse        | 61.2 ms     | 63.7 ms: 1.04x slower  |
| richards_super             | 33.7 ms     | 35.1 ms: 1.04x slower  |
| richards                   | 29.4 ms     | 30.7 ms: 1.05x slower  |
| pidigits                   | 145 ms      | 152 ms: 1.05x slower   |
| python_startup             | 24.7 ms     | 26.1 ms: 1.05x slower  |
| sympy_integrate            | 12.8 ms     | 13.5 ms: 1.06x slower  |
| 2to3                       | 215 ms      | 227 ms: 1.06x slower   |
| sympy_sum                  | 85.2 ms     | 90.5 ms: 1.06x slower  |
| sqlglot_v2_optimize        | 32.9 ms     | 35.0 ms: 1.06x slower  |
| telco                      | 4.59 ms     | 4.89 ms: 1.07x slower  |
| django_template            | 23.6 ms     | 25.1 ms: 1.07x slower  |
| python_startup_no_site     | 18.6 ms     | 19.8 ms: 1.07x slower  |
| sqlglot_v2_normalize       | 69.0 ms     | 73.6 ms: 1.07x slower  |
| sympy_expand               | 283 ms      | 302 ms: 1.07x slower   |
| pycparser                  | 689 ms      | 738 ms: 1.07x slower   |
| dulwich_log                | 40.3 ms     | 43.4 ms: 1.08x slower  |
| html5lib                   | 37.8 ms     | 40.8 ms: 1.08x slower  |
| meteor_contest             | 70.9 ms     | 76.9 ms: 1.08x slower  |
| typing_runtime_protocols   | 97.8 us     | 106 us: 1.08x slower   |
| async_tree_io_tg           | 377 ms      | 410 ms: 1.09x slower   |
| bpe_tokeniser              | 2.72 sec    | 2.96 sec: 1.09x slower |
| async_tree_memoization     | 205 ms      | 224 ms: 1.09x slower   |
| logging_format             | 6.42 us     | 7.03 us: 1.10x slower  |
| async_tree_none_tg         | 161 ms      | 176 ms: 1.10x slower   |
| mako                       | 6.25 ms     | 6.86 ms: 1.10x slower  |
| async_tree_none            | 170 ms      | 187 ms: 1.10x slower   |
| json_dumps                 | 6.40 ms     | 7.05 ms: 1.10x slower  |
| xml_etree_generate         | 53.1 ms     | 58.7 ms: 1.11x slower  |
| async_tree_io              | 382 ms      | 423 ms: 1.11x slower   |
| sqlglot_v2_transpile       | 993 us      | 1.10 ms: 1.11x slower  |
| regex_compile              | 79.4 ms     | 88.2 ms: 1.11x slower  |
| logging_simple             | 5.87 us     | 6.53 us: 1.11x slower  |
| genshi_xml                 | 32.3 ms     | 36.3 ms: 1.12x slower  |
| async_generators           | 201 ms      | 226 ms: 1.13x slower   |
| coroutines                 | 12.0 ms     | 13.5 ms: 1.13x slower  |
| xml_etree_process          | 36.8 ms     | 41.5 ms: 1.13x slower  |
| deepcopy                   | 167 us      | 190 us: 1.13x slower   |
| float                      | 42.0 ms     | 47.8 ms: 1.14x slower  |
| crypto_pyaes               | 43.9 ms     | 50.0 ms: 1.14x slower  |
| sqlglot_v2_parse           | 781 us      | 892 us: 1.14x slower   |
| mdp                        | 1.43 sec    | 1.64 sec: 1.15x slower |
| nqueens                    | 55.2 ms     | 63.6 ms: 1.15x slower  |
| genshi_text                | 14.3 ms     | 16.5 ms: 1.15x slower  |
| deepcopy_reduce            | 1.68 us     | 1.94 us: 1.16x slower  |
| comprehensions             | 9.76 us     | 11.3 us: 1.16x slower  |
| generators                 | 16.5 ms     | 19.3 ms: 1.17x slower  |
| pprint_safe_repr           | 474 ms      | 558 ms: 1.18x slower   |
| pprint_pformat             | 956 ms      | 1.13 sec: 1.18x slower |
| raytrace                   | 162 ms      | 191 ms: 1.18x slower   |
| pickle_pure_python         | 199 us      | 237 us: 1.19x slower   |
| pyflate                    | 264 ms      | 315 ms: 1.19x slower   |
| deltablue                  | 1.88 ms     | 2.29 ms: 1.22x slower  |
| chaos                      | 35.4 ms     | 43.6 ms: 1.23x slower  |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.72 ms: 1.23x slower  |
| spectral_norm              | 49.4 ms     | 61.5 ms: 1.25x slower  |
| deepcopy_memo              | 16.8 us     | 21.0 us: 1.25x slower  |
| tomli_loads                | 1.17 sec    | 1.47 sec: 1.25x slower |
| unpickle_pure_python       | 124 us      | 155 us: 1.25x slower   |
| scimark_fft                | 153 ms      | 192 ms: 1.25x slower   |
| hexiom                     | 3.49 ms     | 4.38 ms: 1.26x slower  |
| go                         | 70.5 ms     | 88.6 ms: 1.26x slower  |
| logging_silent             | 49.7 ns     | 65.2 ns: 1.31x slower  |
| fannkuch                   | 225 ms      | 296 ms: 1.32x slower   |
| scimark_monte_carlo        | 35.6 ms     | 47.1 ms: 1.32x slower  |
| pathlib                    | 24.2 ms     | 32.1 ms: 1.33x slower  |
| scimark_lu                 | 50.3 ms     | 66.9 ms: 1.33x slower  |
| nbody                      | 55.6 ms     | 74.1 ms: 1.33x slower  |
| scimark_sor                | 60.5 ms     | 91.0 ms: 1.50x slower  |
| Geometric mean             | (ref)       | 1.09x slower           |

Benchmark hidden because not significant (2): create_gc_cycles, pylint
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown