# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-Ex                  |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 231 ms: 1.07x slower   |
| docutils       | 1.63 sec   | 1.77 sec: 1.09x slower |
| html5lib       | 36.1 ms    | 38.8 ms: 1.07x slower  |
| sphinx         | 638 ms     | 702 ms: 1.10x slower   |
| Geometric mean | (ref)      | 1.08x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | TC-Ex                 |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 317 ms     | 312 ms: 1.02x faster  |
| coroutines                 | 12.4 ms    | 12.3 ms: 1.01x faster |
| async_tree_none            | 170 ms     | 174 ms: 1.02x slower  |
| async_tree_io              | 375 ms     | 384 ms: 1.02x slower  |
| async_tree_memoization     | 205 ms     | 210 ms: 1.02x slower  |
| async_generators           | 206 ms     | 213 ms: 1.04x slower  |
| async_tree_io_tg           | 371 ms     | 385 ms: 1.04x slower  |
| async_tree_none_tg         | 159 ms     | 167 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 359 ms: 1.09x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 363 ms: 1.11x slower  |
| Geometric mean             | (ref)      | 1.03x slower          |

Benchmark hidden because not significant (1): async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| float          | 40.2 ms    | 41.4 ms: 1.03x slower |
| Geometric mean | (ref)      | 1.01x slower          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 121 ms: 1.05x slower  |
| regex_compile  | 74.8 ms    | 81.9 ms: 1.10x slower |
| regex_v8       | 14.1 ms    | 16.3 ms: 1.16x slower |
| regex_effbot   | 1.40 ms    | 1.85 ms: 1.32x slower |
| Geometric mean | (ref)      | 1.15x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TC-Ex                  |
|----------------------|:----------:|:----------------------:|
| tomli_loads          | 1.17 sec   | 1.26 sec: 1.07x slower |
| pickle_pure_python   | 201 us     | 223 us: 1.10x slower   |
| xml_etree_iterparse  | 60.4 ms    | 70.4 ms: 1.17x slower  |
| xml_etree_parse      | 89.0 ms    | 105 ms: 1.17x slower   |
| json_dumps           | 6.48 ms    | 7.79 ms: 1.20x slower  |
| unpickle_pure_python | 123 us     | 148 us: 1.21x slower   |
| xml_etree_process    | 36.7 ms    | 44.7 ms: 1.22x slower  |
| xml_etree_generate   | 51.5 ms    | 64.7 ms: 1.26x slower  |
| json_loads           | 14.5 us    | 21.9 us: 1.52x slower  |
| Geometric mean       | (ref)      | 1.21x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TC-PGO-Ex2 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| python_startup | 26.0 ms    | 26.4 ms: 1.02x slower |
| Geometric mean | (ref)      | 1.00x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TC-Ex                 |
|-----------------|:----------:|:---------------------:|
| genshi_text     | 14.2 ms    | 14.5 ms: 1.02x slower |
| genshi_xml      | 30.7 ms    | 31.3 ms: 1.02x slower |
| django_template | 23.4 ms    | 25.2 ms: 1.08x slower |
| mako            | 6.12 ms    | 7.84 ms: 1.28x slower |
| Geometric mean  | (ref)      | 1.09x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | TC-Ex                  |
|----------------------------|:----------:|:----------------------:|
| connected_components       | 321 ms     | 311 ms: 1.03x faster   |
| asyncio_websockets         | 317 ms     | 312 ms: 1.02x faster   |
| coroutines                 | 12.4 ms    | 12.3 ms: 1.01x faster  |
| python_startup             | 26.0 ms    | 26.4 ms: 1.02x slower  |
| scimark_sor                | 67.5 ms    | 68.6 ms: 1.02x slower  |
| genshi_text                | 14.2 ms    | 14.5 ms: 1.02x slower  |
| raytrace                   | 166 ms     | 169 ms: 1.02x slower   |
| genshi_xml                 | 30.7 ms    | 31.3 ms: 1.02x slower  |
| async_tree_none            | 170 ms     | 174 ms: 1.02x slower   |
| async_tree_io              | 375 ms     | 384 ms: 1.02x slower   |
| async_tree_memoization     | 205 ms     | 210 ms: 1.02x slower   |
| bench_thread_pool          | 851 us     | 876 us: 1.03x slower   |
| go                         | 68.4 ms    | 70.4 ms: 1.03x slower  |
| pathlib                    | 24.3 ms    | 25.1 ms: 1.03x slower  |
| pylint                     | 199 ms     | 205 ms: 1.03x slower   |
| float                      | 40.2 ms    | 41.4 ms: 1.03x slower  |
| deltablue                  | 1.85 ms    | 1.91 ms: 1.03x slower  |
| mdp                        | 1.40 sec   | 1.44 sec: 1.03x slower |
| async_generators           | 206 ms     | 213 ms: 1.04x slower   |
| async_tree_io_tg           | 371 ms     | 385 ms: 1.04x slower   |
| regex_dna                  | 115 ms     | 121 ms: 1.05x slower   |
| async_tree_none_tg         | 159 ms     | 167 ms: 1.05x slower   |
| bench_mp_pool              | 89.1 ms    | 93.6 ms: 1.05x slower  |
| chaos                      | 35.9 ms    | 37.7 ms: 1.05x slower  |
| scimark_monte_carlo        | 37.0 ms    | 38.9 ms: 1.05x slower  |
| pyflate                    | 260 ms     | 274 ms: 1.05x slower   |
| create_gc_cycles           | 1.27 ms    | 1.34 ms: 1.06x slower  |
| logging_format             | 6.34 us    | 6.70 us: 1.06x slower  |
| fannkuch                   | 236 ms     | 250 ms: 1.06x slower   |
| 2to3                       | 216 ms     | 231 ms: 1.07x slower   |
| pprint_safe_repr           | 478 ms     | 510 ms: 1.07x slower   |
| pprint_pformat             | 968 ms     | 1.04 sec: 1.07x slower |
| meteor_contest             | 69.5 ms    | 74.5 ms: 1.07x slower  |
| typing_runtime_protocols   | 98.9 us    | 106 us: 1.07x slower   |
| pycparser                  | 664 ms     | 713 ms: 1.07x slower   |
| dulwich_log                | 39.5 ms    | 42.3 ms: 1.07x slower  |
| tomli_loads                | 1.17 sec   | 1.26 sec: 1.07x slower |
| html5lib                   | 36.1 ms    | 38.8 ms: 1.07x slower  |
| sqlite_synth               | 1.56 us    | 1.68 us: 1.08x slower  |
| django_template            | 23.4 ms    | 25.2 ms: 1.08x slower  |
| sqlglot_v2_parse           | 740 us     | 798 us: 1.08x slower   |
| logging_simple             | 5.78 us    | 6.25 us: 1.08x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.01 ms: 1.09x slower  |
| docutils                   | 1.63 sec   | 1.77 sec: 1.09x slower |
| scimark_sparse_mat_mult    | 2.26 ms    | 2.47 ms: 1.09x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 359 ms: 1.09x slower   |
| regex_compile              | 74.8 ms    | 81.9 ms: 1.10x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 73.3 ms: 1.10x slower  |
| sympy_integrate            | 12.2 ms    | 13.4 ms: 1.10x slower  |
| generators                 | 14.8 ms    | 16.3 ms: 1.10x slower  |
| sphinx                     | 638 ms     | 702 ms: 1.10x slower   |
| nqueens                    | 54.0 ms    | 59.6 ms: 1.10x slower  |
| pickle_pure_python         | 201 us     | 223 us: 1.10x slower   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 363 ms: 1.11x slower   |
| scimark_fft                | 152 ms     | 169 ms: 1.11x slower   |
| richards                   | 27.8 ms    | 30.9 ms: 1.11x slower  |
| bpe_tokeniser              | 2.71 sec   | 3.01 sec: 1.11x slower |
| sympy_sum                  | 82.1 ms    | 91.4 ms: 1.11x slower  |
| richards_super             | 32.2 ms    | 35.8 ms: 1.11x slower  |
| coverage                   | 49.5 ms    | 55.4 ms: 1.12x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 36.1 ms: 1.12x slower  |
| sympy_str                  | 158 ms     | 177 ms: 1.12x slower   |
| hexiom                     | 3.47 ms    | 3.92 ms: 1.13x slower  |
| deepcopy                   | 160 us     | 180 us: 1.13x slower   |
| deepcopy_memo              | 17.0 us    | 19.3 us: 1.13x slower  |
| sympy_expand               | 269 ms     | 304 ms: 1.13x slower   |
| deepcopy_reduce            | 1.66 us    | 1.90 us: 1.14x slower  |
| thrift                     | 482 us     | 551 us: 1.14x slower   |
| logging_silent             | 53.3 ns    | 61.1 ns: 1.15x slower  |
| crypto_pyaes               | 41.6 ms    | 48.0 ms: 1.15x slower  |
| regex_v8                   | 14.1 ms    | 16.3 ms: 1.16x slower  |
| telco                      | 4.54 ms    | 5.26 ms: 1.16x slower  |
| comprehensions             | 9.73 us    | 11.3 us: 1.16x slower  |
| xml_etree_iterparse        | 60.4 ms    | 70.4 ms: 1.17x slower  |
| xml_etree_parse            | 89.0 ms    | 105 ms: 1.17x slower   |
| scimark_lu                 | 54.4 ms    | 64.2 ms: 1.18x slower  |
| json_dumps                 | 6.48 ms    | 7.79 ms: 1.20x slower  |
| unpickle_pure_python       | 123 us     | 148 us: 1.21x slower   |
| xml_etree_process          | 36.7 ms    | 44.7 ms: 1.22x slower  |
| xml_etree_generate         | 51.5 ms    | 64.7 ms: 1.26x slower  |
| json                       | 2.98 ms    | 3.78 ms: 1.27x slower  |
| mako                       | 6.12 ms    | 7.84 ms: 1.28x slower  |
| regex_effbot               | 1.40 ms    | 1.85 ms: 1.32x slower  |
| gc_traversal               | 2.07 ms    | 2.83 ms: 1.36x slower  |
| json_loads                 | 14.5 us    | 21.9 us: 1.52x slower  |
| Geometric mean             | (ref)      | 1.09x slower           |

Benchmark hidden because not significant (9): subparsers, python_startup_no_site, nbody, shortest_path, pidigits, spectral_norm, k_core, many_optionals, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown