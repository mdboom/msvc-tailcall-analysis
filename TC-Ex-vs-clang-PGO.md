# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.151x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TC-Ex                  |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 231 ms: 1.13x slower   |
| docutils       | 1.55 sec  | 1.77 sec: 1.14x slower |
| html5lib       | 35.2 ms   | 38.8 ms: 1.10x slower  |
| sphinx         | 599 ms    | 702 ms: 1.17x slower   |
| Geometric mean | (ref)     | 1.14x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TC-Ex                 |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 312 ms: 1.28x faster  |
| async_tree_memoization_tg  | 195 ms    | 210 ms: 1.08x slower  |
| async_tree_io_tg           | 352 ms    | 385 ms: 1.09x slower  |
| async_tree_io              | 349 ms    | 384 ms: 1.10x slower  |
| coroutines                 | 11.1 ms   | 12.3 ms: 1.10x slower |
| async_tree_memoization     | 190 ms    | 210 ms: 1.11x slower  |
| async_tree_none            | 155 ms    | 174 ms: 1.12x slower  |
| async_generators           | 188 ms    | 213 ms: 1.13x slower  |
| async_tree_none_tg         | 147 ms    | 167 ms: 1.13x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 359 ms: 1.16x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 363 ms: 1.17x slower  |
| Geometric mean             | (ref)     | 1.08x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TC-Ex                 |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 146 ms: 1.02x faster  |
| float          | 38.5 ms   | 41.4 ms: 1.08x slower |
| Geometric mean | (ref)     | 1.02x slower          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TC-Ex                 |
|----------------|:---------:|:---------------------:|
| regex_compile  | 73.4 ms   | 81.9 ms: 1.12x slower |
| regex_effbot   | 1.65 ms   | 1.85 ms: 1.12x slower |
| regex_v8       | 13.5 ms   | 16.3 ms: 1.21x slower |
| Geometric mean | (ref)     | 1.11x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TC-Ex                  |
|----------------------|:---------:|:----------------------:|
| tomli_loads          | 1.13 sec  | 1.26 sec: 1.11x slower |
| xml_etree_iterparse  | 60.7 ms   | 70.4 ms: 1.16x slower  |
| xml_etree_parse      | 88.8 ms   | 105 ms: 1.18x slower   |
| pickle_pure_python   | 175 us    | 223 us: 1.27x slower   |
| xml_etree_process    | 34.0 ms   | 44.7 ms: 1.32x slower  |
| xml_etree_generate   | 48.4 ms   | 64.7 ms: 1.34x slower  |
| json_dumps           | 5.76 ms   | 7.79 ms: 1.35x slower  |
| unpickle_pure_python | 109 us    | 148 us: 1.36x slower   |
| json_loads           | 14.2 us   | 21.9 us: 1.54x slower  |
| Geometric mean       | (ref)     | 1.29x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | TC-Ex                 |
|------------------------|:---------:|:---------------------:|
| python_startup_no_site | 20.0 ms   | 19.4 ms: 1.03x faster |
| Geometric mean         | (ref)     | 1.02x faster          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TC-Ex                 |
|-----------------|:---------:|:---------------------:|
| genshi_xml      | 27.4 ms   | 31.3 ms: 1.14x slower |
| genshi_text     | 12.0 ms   | 14.5 ms: 1.21x slower |
| django_template | 19.5 ms   | 25.2 ms: 1.29x slower |
| mako            | 5.72 ms   | 7.84 ms: 1.37x slower |
| Geometric mean  | (ref)     | 1.25x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TC-Ex                  |
|----------------------------|:---------:|:----------------------:|
| asyncio_websockets         | 400 ms    | 312 ms: 1.28x faster   |
| pathlib                    | 30.4 ms   | 25.1 ms: 1.21x faster  |
| connected_components       | 325 ms    | 311 ms: 1.04x faster   |
| python_startup_no_site     | 20.0 ms   | 19.4 ms: 1.03x faster  |
| create_gc_cycles           | 1.37 ms   | 1.34 ms: 1.02x faster  |
| pidigits                   | 148 ms    | 146 ms: 1.02x faster   |
| shortest_path              | 345 ms    | 347 ms: 1.00x slower   |
| gc_traversal               | 2.79 ms   | 2.83 ms: 1.02x slower  |
| generators                 | 15.8 ms   | 16.3 ms: 1.03x slower  |
| k_core                     | 1.61 sec  | 1.71 sec: 1.06x slower |
| dulwich_log                | 39.5 ms   | 42.3 ms: 1.07x slower  |
| float                      | 38.5 ms   | 41.4 ms: 1.08x slower  |
| async_tree_memoization_tg  | 195 ms    | 210 ms: 1.08x slower   |
| go                         | 65.1 ms   | 70.4 ms: 1.08x slower  |
| meteor_contest             | 68.7 ms   | 74.5 ms: 1.08x slower  |
| async_tree_io_tg           | 352 ms    | 385 ms: 1.09x slower   |
| html5lib                   | 35.2 ms   | 38.8 ms: 1.10x slower  |
| async_tree_io              | 349 ms    | 384 ms: 1.10x slower   |
| coroutines                 | 11.1 ms   | 12.3 ms: 1.10x slower  |
| async_tree_memoization     | 190 ms    | 210 ms: 1.11x slower   |
| mdp                        | 1.30 sec  | 1.44 sec: 1.11x slower |
| tomli_loads                | 1.13 sec  | 1.26 sec: 1.11x slower |
| regex_compile              | 73.4 ms   | 81.9 ms: 1.12x slower  |
| pyflate                    | 245 ms    | 274 ms: 1.12x slower   |
| pycparser                  | 637 ms    | 713 ms: 1.12x slower   |
| regex_effbot               | 1.65 ms   | 1.85 ms: 1.12x slower  |
| async_tree_none            | 155 ms    | 174 ms: 1.12x slower   |
| sqlite_synth               | 1.49 us   | 1.68 us: 1.12x slower  |
| pylint                     | 182 ms    | 205 ms: 1.12x slower   |
| sympy_sum                  | 81.4 ms   | 91.4 ms: 1.12x slower  |
| async_generators           | 188 ms    | 213 ms: 1.13x slower   |
| 2to3                       | 204 ms    | 231 ms: 1.13x slower   |
| async_tree_none_tg         | 147 ms    | 167 ms: 1.13x slower   |
| sympy_integrate            | 11.8 ms   | 13.4 ms: 1.14x slower  |
| spectral_norm              | 44.7 ms   | 51.1 ms: 1.14x slower  |
| genshi_xml                 | 27.4 ms   | 31.3 ms: 1.14x slower  |
| docutils                   | 1.55 sec  | 1.77 sec: 1.14x slower |
| logging_format             | 5.83 us   | 6.70 us: 1.15x slower  |
| xml_etree_iterparse        | 60.7 ms   | 70.4 ms: 1.16x slower  |
| logging_simple             | 5.39 us   | 6.25 us: 1.16x slower  |
| sympy_str                  | 153 ms    | 177 ms: 1.16x slower   |
| scimark_sor                | 59.1 ms   | 68.6 ms: 1.16x slower  |
| sqlglot_v2_parse           | 686 us    | 798 us: 1.16x slower   |
| async_tree_cpu_io_mixed    | 309 ms    | 359 ms: 1.16x slower   |
| sqlglot_v2_transpile       | 868 us    | 1.01 ms: 1.17x slower  |
| sphinx                     | 599 ms    | 702 ms: 1.17x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 363 ms: 1.17x slower   |
| sympy_expand               | 259 ms    | 304 ms: 1.17x slower   |
| xml_etree_parse            | 88.8 ms   | 105 ms: 1.18x slower   |
| scimark_fft                | 143 ms    | 169 ms: 1.18x slower   |
| pprint_safe_repr           | 432 ms    | 510 ms: 1.18x slower   |
| pprint_pformat             | 874 ms    | 1.04 sec: 1.19x slower |
| scimark_monte_carlo        | 32.8 ms   | 38.9 ms: 1.19x slower  |
| fannkuch                   | 209 ms    | 250 ms: 1.20x slower   |
| deltablue                  | 1.59 ms   | 1.91 ms: 1.20x slower  |
| bpe_tokeniser              | 2.50 sec  | 3.01 sec: 1.20x slower |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.47 ms: 1.20x slower  |
| regex_v8                   | 13.5 ms   | 16.3 ms: 1.21x slower  |
| genshi_text                | 12.0 ms   | 14.5 ms: 1.21x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 36.1 ms: 1.21x slower  |
| chaos                      | 31.1 ms   | 37.7 ms: 1.21x slower  |
| crypto_pyaes               | 39.4 ms   | 48.0 ms: 1.22x slower  |
| sqlglot_v2_normalize       | 59.9 ms   | 73.3 ms: 1.22x slower  |
| typing_runtime_protocols   | 86.2 us   | 106 us: 1.23x slower   |
| raytrace                   | 137 ms    | 169 ms: 1.23x slower   |
| deepcopy                   | 145 us    | 180 us: 1.25x slower   |
| nqueens                    | 47.7 ms   | 59.6 ms: 1.25x slower  |
| hexiom                     | 3.13 ms   | 3.92 ms: 1.25x slower  |
| telco                      | 4.20 ms   | 5.26 ms: 1.25x slower  |
| thrift                     | 434 us    | 551 us: 1.27x slower   |
| pickle_pure_python         | 175 us    | 223 us: 1.27x slower   |
| deepcopy_reduce            | 1.49 us   | 1.90 us: 1.27x slower  |
| comprehensions             | 8.84 us   | 11.3 us: 1.28x slower  |
| deepcopy_memo              | 15.1 us   | 19.3 us: 1.28x slower  |
| django_template            | 19.5 ms   | 25.2 ms: 1.29x slower  |
| scimark_lu                 | 49.1 ms   | 64.2 ms: 1.31x slower  |
| xml_etree_process          | 34.0 ms   | 44.7 ms: 1.32x slower  |
| json                       | 2.83 ms   | 3.78 ms: 1.33x slower  |
| xml_etree_generate         | 48.4 ms   | 64.7 ms: 1.34x slower  |
| json_dumps                 | 5.76 ms   | 7.79 ms: 1.35x slower  |
| coverage                   | 40.9 ms   | 55.4 ms: 1.35x slower  |
| unpickle_pure_python       | 109 us    | 148 us: 1.36x slower   |
| mako                       | 5.72 ms   | 7.84 ms: 1.37x slower  |
| logging_silent             | 44.5 ns   | 61.1 ns: 1.37x slower  |
| richards                   | 21.9 ms   | 30.9 ms: 1.41x slower  |
| richards_super             | 24.6 ms   | 35.8 ms: 1.45x slower  |
| json_loads                 | 14.2 us   | 21.9 us: 1.54x slower  |
| many_optionals             | 405 us    | 762 us: 1.88x slower   |
| subparsers                 | 14.2 ms   | 44.5 ms: 3.12x slower  |
| Geometric mean             | (ref)     | 1.18x slower           |

Benchmark hidden because not significant (3): python_startup, regex_dna, nbody
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.151x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown