# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.074x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                  |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 231 ms: 1.09x slower   |
| docutils       | 1.67 sec    | 1.77 sec: 1.06x slower |
| html5lib       | 37.9 ms     | 38.8 ms: 1.02x slower  |
| sphinx         | 645 ms      | 702 ms: 1.09x slower   |
| Geometric mean | (ref)       | 1.06x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TC-Ex                 |
|----------------------------|:-----------:|:---------------------:|
| async_tree_memoization     | 206 ms      | 210 ms: 1.02x slower  |
| async_tree_none            | 170 ms      | 174 ms: 1.02x slower  |
| async_tree_io_tg           | 377 ms      | 385 ms: 1.02x slower  |
| coroutines                 | 11.9 ms     | 12.3 ms: 1.03x slower |
| asyncio_websockets         | 301 ms      | 312 ms: 1.04x slower  |
| async_tree_none_tg         | 159 ms      | 167 ms: 1.05x slower  |
| async_generators           | 202 ms      | 213 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 359 ms: 1.09x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 363 ms: 1.10x slower  |
| Geometric mean             | (ref)       | 1.04x slower          |

Benchmark hidden because not significant (2): async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| nbody          | 55.2 ms     | 53.1 ms: 1.04x faster |
| float          | 41.9 ms     | 41.4 ms: 1.01x faster |
| Geometric mean | (ref)       | 1.02x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 78.1 ms     | 81.9 ms: 1.05x slower |
| regex_v8       | 13.2 ms     | 16.3 ms: 1.23x slower |
| regex_effbot   | 1.46 ms     | 1.85 ms: 1.26x slower |
| Geometric mean | (ref)       | 1.13x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-Ex                  |
|----------------------|:-----------:|:----------------------:|
| tomli_loads          | 1.18 sec    | 1.26 sec: 1.07x slower |
| pickle_pure_python   | 199 us      | 223 us: 1.12x slower   |
| xml_etree_iterparse  | 61.2 ms     | 70.4 ms: 1.15x slower  |
| unpickle_pure_python | 127 us      | 148 us: 1.16x slower   |
| xml_etree_parse      | 89.3 ms     | 105 ms: 1.17x slower   |
| json_dumps           | 6.55 ms     | 7.79 ms: 1.19x slower  |
| xml_etree_generate   | 53.6 ms     | 64.7 ms: 1.21x slower  |
| xml_etree_process    | 37.0 ms     | 44.7 ms: 1.21x slower  |
| json_loads           | 14.7 us     | 21.9 us: 1.49x slower  |
| Geometric mean       | (ref)       | 1.19x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TC-Ex                 |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 19.4 ms: 1.04x slower |
| python_startup         | 24.7 ms     | 26.4 ms: 1.07x slower |
| Geometric mean         | (ref)       | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TC-Ex                 |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 31.3 ms: 1.05x faster |
| genshi_text     | 14.3 ms     | 14.5 ms: 1.01x slower |
| django_template | 22.9 ms     | 25.2 ms: 1.10x slower |
| mako            | 6.28 ms     | 7.84 ms: 1.25x slower |
| Geometric mean  | (ref)       | 1.07x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TC-Ex                  |
|----------------------------|:-----------:|:----------------------:|
| mdp                        | 1.62 sec    | 1.44 sec: 1.12x faster |
| genshi_xml                 | 32.8 ms     | 31.3 ms: 1.05x faster  |
| connected_components       | 326 ms      | 311 ms: 1.05x faster   |
| nbody                      | 55.2 ms     | 53.1 ms: 1.04x faster  |
| shortest_path              | 353 ms      | 347 ms: 1.02x faster   |
| generators                 | 16.5 ms     | 16.3 ms: 1.01x faster  |
| float                      | 41.9 ms     | 41.4 ms: 1.01x faster  |
| crypto_pyaes               | 47.4 ms     | 48.0 ms: 1.01x slower  |
| genshi_text                | 14.3 ms     | 14.5 ms: 1.01x slower  |
| deltablue                  | 1.88 ms     | 1.91 ms: 1.02x slower  |
| pyflate                    | 268 ms      | 274 ms: 1.02x slower   |
| async_tree_memoization     | 206 ms      | 210 ms: 1.02x slower   |
| async_tree_none            | 170 ms      | 174 ms: 1.02x slower   |
| html5lib                   | 37.9 ms     | 38.8 ms: 1.02x slower  |
| async_tree_io_tg           | 377 ms      | 385 ms: 1.02x slower   |
| chaos                      | 36.9 ms     | 37.7 ms: 1.02x slower  |
| coroutines                 | 11.9 ms     | 12.3 ms: 1.03x slower  |
| logging_format             | 6.50 us     | 6.70 us: 1.03x slower  |
| pylint                     | 198 ms      | 205 ms: 1.03x slower   |
| spectral_norm              | 49.4 ms     | 51.1 ms: 1.03x slower  |
| python_startup_no_site     | 18.7 ms     | 19.4 ms: 1.04x slower  |
| asyncio_websockets         | 301 ms      | 312 ms: 1.04x slower   |
| pycparser                  | 686 ms      | 713 ms: 1.04x slower   |
| sqlglot_v2_parse           | 766 us      | 798 us: 1.04x slower   |
| pathlib                    | 24.1 ms     | 25.1 ms: 1.04x slower  |
| sympy_integrate            | 12.8 ms     | 13.4 ms: 1.04x slower  |
| sqlglot_v2_transpile       | 970 us      | 1.01 ms: 1.05x slower  |
| logging_simple             | 5.97 us     | 6.25 us: 1.05x slower  |
| regex_compile              | 78.1 ms     | 81.9 ms: 1.05x slower  |
| async_tree_none_tg         | 159 ms      | 167 ms: 1.05x slower   |
| create_gc_cycles           | 1.27 ms     | 1.34 ms: 1.05x slower  |
| dulwich_log                | 40.2 ms     | 42.3 ms: 1.05x slower  |
| async_generators           | 202 ms      | 213 ms: 1.05x slower   |
| raytrace                   | 160 ms      | 169 ms: 1.06x slower   |
| sqlglot_v2_normalize       | 69.3 ms     | 73.3 ms: 1.06x slower  |
| sympy_sum                  | 86.3 ms     | 91.4 ms: 1.06x slower  |
| meteor_contest             | 70.2 ms     | 74.5 ms: 1.06x slower  |
| docutils                   | 1.67 sec    | 1.77 sec: 1.06x slower |
| python_startup             | 24.7 ms     | 26.4 ms: 1.07x slower  |
| tomli_loads                | 1.18 sec    | 1.26 sec: 1.07x slower |
| pprint_pformat             | 967 ms      | 1.04 sec: 1.07x slower |
| typing_runtime_protocols   | 98.8 us     | 106 us: 1.07x slower   |
| sqlite_synth               | 1.56 us     | 1.68 us: 1.07x slower  |
| richards                   | 28.7 ms     | 30.9 ms: 1.08x slower  |
| sympy_str                  | 164 ms      | 177 ms: 1.08x slower   |
| sympy_expand               | 282 ms      | 304 ms: 1.08x slower   |
| deepcopy                   | 167 us      | 180 us: 1.08x slower   |
| richards_super             | 33.1 ms     | 35.8 ms: 1.08x slower  |
| scimark_monte_carlo        | 36.0 ms     | 38.9 ms: 1.08x slower  |
| pprint_safe_repr           | 470 ms      | 510 ms: 1.09x slower   |
| sphinx                     | 645 ms      | 702 ms: 1.09x slower   |
| async_tree_cpu_io_mixed    | 330 ms      | 359 ms: 1.09x slower   |
| scimark_sparse_mat_mult    | 2.27 ms     | 2.47 ms: 1.09x slower  |
| 2to3                       | 212 ms      | 231 ms: 1.09x slower   |
| subparsers                 | 40.7 ms     | 44.5 ms: 1.09x slower  |
| sqlglot_v2_optimize        | 33.0 ms     | 36.1 ms: 1.09x slower  |
| scimark_fft                | 154 ms      | 169 ms: 1.09x slower   |
| nqueens                    | 54.4 ms     | 59.6 ms: 1.10x slower  |
| async_tree_cpu_io_mixed_tg | 329 ms      | 363 ms: 1.10x slower   |
| django_template            | 22.9 ms     | 25.2 ms: 1.10x slower  |
| bpe_tokeniser              | 2.72 sec    | 3.01 sec: 1.11x slower |
| hexiom                     | 3.54 ms     | 3.92 ms: 1.11x slower  |
| deepcopy_reduce            | 1.70 us     | 1.90 us: 1.12x slower  |
| pickle_pure_python         | 199 us      | 223 us: 1.12x slower   |
| scimark_sor                | 61.1 ms     | 68.6 ms: 1.12x slower  |
| fannkuch                   | 223 ms      | 250 ms: 1.12x slower   |
| thrift                     | 482 us      | 551 us: 1.14x slower   |
| comprehensions             | 9.87 us     | 11.3 us: 1.14x slower  |
| many_optionals             | 665 us      | 762 us: 1.14x slower   |
| coverage                   | 48.2 ms     | 55.4 ms: 1.15x slower  |
| xml_etree_iterparse        | 61.2 ms     | 70.4 ms: 1.15x slower  |
| telco                      | 4.57 ms     | 5.26 ms: 1.15x slower  |
| deepcopy_memo              | 16.6 us     | 19.3 us: 1.16x slower  |
| unpickle_pure_python       | 127 us      | 148 us: 1.16x slower   |
| xml_etree_parse            | 89.3 ms     | 105 ms: 1.17x slower   |
| json_dumps                 | 6.55 ms     | 7.79 ms: 1.19x slower  |
| xml_etree_generate         | 53.6 ms     | 64.7 ms: 1.21x slower  |
| xml_etree_process          | 37.0 ms     | 44.7 ms: 1.21x slower  |
| regex_v8                   | 13.2 ms     | 16.3 ms: 1.23x slower  |
| logging_silent             | 49.4 ns     | 61.1 ns: 1.24x slower  |
| mako                       | 6.28 ms     | 7.84 ms: 1.25x slower  |
| scimark_lu                 | 50.9 ms     | 64.2 ms: 1.26x slower  |
| regex_effbot               | 1.46 ms     | 1.85 ms: 1.26x slower  |
| json                       | 2.97 ms     | 3.78 ms: 1.27x slower  |
| gc_traversal               | 2.11 ms     | 2.83 ms: 1.34x slower  |
| json_loads                 | 14.7 us     | 21.9 us: 1.49x slower  |
| Geometric mean             | (ref)       | 1.08x slower           |

Benchmark hidden because not significant (6): go, k_core, async_tree_io, regex_dna, pidigits, async_tree_memoization_tg
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.074x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown