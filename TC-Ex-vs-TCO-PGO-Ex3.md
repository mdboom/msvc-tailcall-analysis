# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.075x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                  |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 231 ms: 1.07x slower   |
| docutils       | 1.66 sec    | 1.77 sec: 1.07x slower |
| html5lib       | 37.8 ms     | 38.8 ms: 1.03x slower  |
| sphinx         | 641 ms      | 702 ms: 1.09x slower   |
| Geometric mean | (ref)       | 1.06x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TC-Ex                 |
|----------------------------|:-----------:|:---------------------:|
| async_tree_memoization_tg  | 208 ms      | 210 ms: 1.01x slower  |
| async_tree_io_tg           | 377 ms      | 385 ms: 1.02x slower  |
| async_tree_none            | 170 ms      | 174 ms: 1.02x slower  |
| async_tree_memoization     | 205 ms      | 210 ms: 1.02x slower  |
| coroutines                 | 12.0 ms     | 12.3 ms: 1.03x slower |
| async_tree_none_tg         | 161 ms      | 167 ms: 1.04x slower  |
| async_generators           | 201 ms      | 213 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 330 ms      | 359 ms: 1.09x slower  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 363 ms: 1.10x slower  |
| Geometric mean             | (ref)       | 1.04x slower          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| nbody          | 55.6 ms     | 53.1 ms: 1.05x faster |
| float          | 42.0 ms     | 41.4 ms: 1.01x faster |
| Geometric mean | (ref)       | 1.02x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| regex_dna      | 120 ms      | 121 ms: 1.01x slower  |
| regex_compile  | 79.4 ms     | 81.9 ms: 1.03x slower |
| regex_v8       | 14.2 ms     | 16.3 ms: 1.15x slower |
| regex_effbot   | 1.47 ms     | 1.85 ms: 1.25x slower |
| Geometric mean | (ref)       | 1.11x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-Ex                  |
|----------------------|:-----------:|:----------------------:|
| tomli_loads          | 1.17 sec    | 1.26 sec: 1.07x slower |
| pickle_pure_python   | 199 us      | 223 us: 1.12x slower   |
| xml_etree_iterparse  | 61.2 ms     | 70.4 ms: 1.15x slower  |
| xml_etree_parse      | 89.4 ms     | 105 ms: 1.17x slower   |
| unpickle_pure_python | 124 us      | 148 us: 1.19x slower   |
| xml_etree_process    | 36.8 ms     | 44.7 ms: 1.21x slower  |
| json_dumps           | 6.40 ms     | 7.79 ms: 1.22x slower  |
| xml_etree_generate   | 53.1 ms     | 64.7 ms: 1.22x slower  |
| json_loads           | 14.5 us     | 21.9 us: 1.51x slower  |
| Geometric mean       | (ref)       | 1.20x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TC-Ex                 |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.6 ms     | 19.4 ms: 1.04x slower |
| python_startup         | 24.7 ms     | 26.4 ms: 1.07x slower |
| Geometric mean         | (ref)       | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TC-Ex                 |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.3 ms     | 31.3 ms: 1.03x faster |
| genshi_text     | 14.3 ms     | 14.5 ms: 1.01x slower |
| django_template | 23.6 ms     | 25.2 ms: 1.07x slower |
| mako            | 6.25 ms     | 7.84 ms: 1.25x slower |
| Geometric mean  | (ref)       | 1.07x slower          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TC-Ex                  |
|----------------------------|:-----------:|:----------------------:|
| nbody                      | 55.6 ms     | 53.1 ms: 1.05x faster  |
| connected_components       | 325 ms      | 311 ms: 1.04x faster   |
| genshi_xml                 | 32.3 ms     | 31.3 ms: 1.03x faster  |
| shortest_path              | 352 ms      | 347 ms: 1.01x faster   |
| float                      | 42.0 ms     | 41.4 ms: 1.01x faster  |
| generators                 | 16.5 ms     | 16.3 ms: 1.01x faster  |
| regex_dna                  | 120 ms      | 121 ms: 1.01x slower   |
| genshi_text                | 14.3 ms     | 14.5 ms: 1.01x slower  |
| mdp                        | 1.43 sec    | 1.44 sec: 1.01x slower |
| async_tree_memoization_tg  | 208 ms      | 210 ms: 1.01x slower   |
| deltablue                  | 1.88 ms     | 1.91 ms: 1.01x slower  |
| sqlglot_v2_transpile       | 993 us      | 1.01 ms: 1.02x slower  |
| sqlglot_v2_parse           | 781 us      | 798 us: 1.02x slower   |
| async_tree_io_tg           | 377 ms      | 385 ms: 1.02x slower   |
| async_tree_none            | 170 ms      | 174 ms: 1.02x slower   |
| async_tree_memoization     | 205 ms      | 210 ms: 1.02x slower   |
| sympy_str                  | 173 ms      | 177 ms: 1.02x slower   |
| html5lib                   | 37.8 ms     | 38.8 ms: 1.03x slower  |
| coroutines                 | 12.0 ms     | 12.3 ms: 1.03x slower  |
| regex_compile              | 79.4 ms     | 81.9 ms: 1.03x slower  |
| spectral_norm              | 49.4 ms     | 51.1 ms: 1.03x slower  |
| pycparser                  | 689 ms      | 713 ms: 1.03x slower   |
| pyflate                    | 264 ms      | 274 ms: 1.03x slower   |
| pathlib                    | 24.2 ms     | 25.1 ms: 1.04x slower  |
| async_tree_none_tg         | 161 ms      | 167 ms: 1.04x slower   |
| python_startup_no_site     | 18.6 ms     | 19.4 ms: 1.04x slower  |
| logging_format             | 6.42 us     | 6.70 us: 1.04x slower  |
| sympy_integrate            | 12.8 ms     | 13.4 ms: 1.05x slower  |
| raytrace                   | 162 ms      | 169 ms: 1.05x slower   |
| meteor_contest             | 70.9 ms     | 74.5 ms: 1.05x slower  |
| dulwich_log                | 40.3 ms     | 42.3 ms: 1.05x slower  |
| richards                   | 29.4 ms     | 30.9 ms: 1.05x slower  |
| async_generators           | 201 ms      | 213 ms: 1.06x slower   |
| sqlglot_v2_normalize       | 69.0 ms     | 73.3 ms: 1.06x slower  |
| richards_super             | 33.7 ms     | 35.8 ms: 1.06x slower  |
| logging_simple             | 5.87 us     | 6.25 us: 1.06x slower  |
| chaos                      | 35.4 ms     | 37.7 ms: 1.07x slower  |
| python_startup             | 24.7 ms     | 26.4 ms: 1.07x slower  |
| docutils                   | 1.66 sec    | 1.77 sec: 1.07x slower |
| create_gc_cycles           | 1.25 ms     | 1.34 ms: 1.07x slower  |
| django_template            | 23.6 ms     | 25.2 ms: 1.07x slower  |
| 2to3                       | 215 ms      | 231 ms: 1.07x slower   |
| tomli_loads                | 1.17 sec    | 1.26 sec: 1.07x slower |
| sympy_sum                  | 85.2 ms     | 91.4 ms: 1.07x slower  |
| sqlite_synth               | 1.56 us     | 1.68 us: 1.07x slower  |
| subparsers                 | 41.4 ms     | 44.5 ms: 1.08x slower  |
| sympy_expand               | 283 ms      | 304 ms: 1.08x slower   |
| pprint_safe_repr           | 474 ms      | 510 ms: 1.08x slower   |
| deepcopy                   | 167 us      | 180 us: 1.08x slower   |
| nqueens                    | 55.2 ms     | 59.6 ms: 1.08x slower  |
| typing_runtime_protocols   | 97.8 us     | 106 us: 1.08x slower   |
| pprint_pformat             | 956 ms      | 1.04 sec: 1.09x slower |
| async_tree_cpu_io_mixed    | 330 ms      | 359 ms: 1.09x slower   |
| crypto_pyaes               | 43.9 ms     | 48.0 ms: 1.09x slower  |
| scimark_monte_carlo        | 35.6 ms     | 38.9 ms: 1.09x slower  |
| sphinx                     | 641 ms      | 702 ms: 1.09x slower   |
| sqlglot_v2_optimize        | 32.9 ms     | 36.1 ms: 1.09x slower  |
| scimark_fft                | 153 ms      | 169 ms: 1.10x slower   |
| async_tree_cpu_io_mixed_tg | 330 ms      | 363 ms: 1.10x slower   |
| bpe_tokeniser              | 2.72 sec    | 3.01 sec: 1.11x slower |
| many_optionals             | 685 us      | 762 us: 1.11x slower   |
| fannkuch                   | 225 ms      | 250 ms: 1.12x slower   |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.47 ms: 1.12x slower  |
| pickle_pure_python         | 199 us      | 223 us: 1.12x slower   |
| hexiom                     | 3.49 ms     | 3.92 ms: 1.12x slower  |
| thrift                     | 491 us      | 551 us: 1.12x slower   |
| deepcopy_reduce            | 1.68 us     | 1.90 us: 1.13x slower  |
| scimark_sor                | 60.5 ms     | 68.6 ms: 1.13x slower  |
| deepcopy_memo              | 16.8 us     | 19.3 us: 1.14x slower  |
| telco                      | 4.59 ms     | 5.26 ms: 1.15x slower  |
| regex_v8                   | 14.2 ms     | 16.3 ms: 1.15x slower  |
| xml_etree_iterparse        | 61.2 ms     | 70.4 ms: 1.15x slower  |
| comprehensions             | 9.76 us     | 11.3 us: 1.16x slower  |
| coverage                   | 47.5 ms     | 55.4 ms: 1.16x slower  |
| xml_etree_parse            | 89.4 ms     | 105 ms: 1.17x slower   |
| unpickle_pure_python       | 124 us      | 148 us: 1.19x slower   |
| xml_etree_process          | 36.8 ms     | 44.7 ms: 1.21x slower  |
| json_dumps                 | 6.40 ms     | 7.79 ms: 1.22x slower  |
| xml_etree_generate         | 53.1 ms     | 64.7 ms: 1.22x slower  |
| logging_silent             | 49.7 ns     | 61.1 ns: 1.23x slower  |
| json                       | 3.04 ms     | 3.78 ms: 1.24x slower  |
| regex_effbot               | 1.47 ms     | 1.85 ms: 1.25x slower  |
| mako                       | 6.25 ms     | 7.84 ms: 1.25x slower  |
| scimark_lu                 | 50.3 ms     | 64.2 ms: 1.28x slower  |
| gc_traversal               | 2.12 ms     | 2.83 ms: 1.34x slower  |
| json_loads                 | 14.5 us     | 21.9 us: 1.51x slower  |
| Geometric mean             | (ref)       | 1.08x slower           |

Benchmark hidden because not significant (6): asyncio_websockets, go, k_core, pidigits, async_tree_io, pylint
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.075x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown