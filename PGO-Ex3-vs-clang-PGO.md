# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.157x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | PGO-Ex3                |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 227 ms: 1.11x slower   |
| docutils       | 1.55 sec  | 1.71 sec: 1.10x slower |
| html5lib       | 35.2 ms   | 40.5 ms: 1.15x slower  |
| sphinx         | 599 ms    | 670 ms: 1.12x slower   |
| Geometric mean | (ref)     | 1.12x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | PGO-Ex3               |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 311 ms: 1.29x faster  |
| async_tree_cpu_io_mixed    | 309 ms    | 340 ms: 1.10x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 344 ms: 1.11x slower  |
| async_tree_memoization_tg  | 195 ms    | 219 ms: 1.12x slower  |
| async_generators           | 188 ms    | 219 ms: 1.16x slower  |
| async_tree_io_tg           | 352 ms    | 410 ms: 1.17x slower  |
| async_tree_memoization     | 190 ms    | 223 ms: 1.18x slower  |
| coroutines                 | 11.1 ms   | 13.1 ms: 1.18x slower |
| async_tree_none_tg         | 147 ms    | 176 ms: 1.19x slower  |
| async_tree_io              | 349 ms    | 417 ms: 1.19x slower  |
| async_tree_none            | 155 ms    | 186 ms: 1.20x slower  |
| Geometric mean             | (ref)     | 1.12x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | PGO-Ex3               |
|----------------|:---------:|:---------------------:|
| float          | 38.5 ms   | 44.2 ms: 1.15x slower |
| nbody          | 52.9 ms   | 78.3 ms: 1.48x slower |
| Geometric mean | (ref)     | 1.19x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | PGO-Ex3               |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.46 ms: 1.13x faster |
| regex_dna      | 121 ms    | 116 ms: 1.04x faster  |
| regex_compile  | 73.4 ms   | 86.1 ms: 1.17x slower |
| Geometric mean | (ref)     | 1.00x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | PGO-Ex3                |
|----------------------|:---------:|:----------------------:|
| xml_etree_iterparse  | 60.7 ms   | 62.3 ms: 1.03x slower  |
| json_loads           | 14.2 us   | 15.3 us: 1.08x slower  |
| json_dumps           | 5.76 ms   | 6.69 ms: 1.16x slower  |
| xml_etree_process    | 34.0 ms   | 39.7 ms: 1.17x slower  |
| xml_etree_generate   | 48.4 ms   | 56.8 ms: 1.17x slower  |
| pickle_pure_python   | 175 us    | 217 us: 1.24x slower   |
| tomli_loads          | 1.13 sec  | 1.44 sec: 1.27x slower |
| unpickle_pure_python | 109 us    | 147 us: 1.35x slower   |
| Geometric mean       | (ref)     | 1.16x slower           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | PGO-Ex3               |
|------------------------|:---------:|:---------------------:|
| python_startup         | 26.6 ms   | 24.5 ms: 1.09x faster |
| python_startup_no_site | 20.0 ms   | 18.7 ms: 1.07x faster |
| Geometric mean         | (ref)     | 1.08x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | PGO-Ex3               |
|-----------------|:---------:|:---------------------:|
| mako            | 5.72 ms   | 6.50 ms: 1.14x slower |
| genshi_xml      | 27.4 ms   | 35.0 ms: 1.28x slower |
| django_template | 19.5 ms   | 25.5 ms: 1.31x slower |
| genshi_text     | 12.0 ms   | 15.8 ms: 1.33x slower |
| Geometric mean  | (ref)     | 1.26x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | PGO-Ex3                |
|----------------------------|:---------:|:----------------------:|
| gc_traversal               | 2.79 ms   | 2.07 ms: 1.35x faster  |
| asyncio_websockets         | 400 ms    | 311 ms: 1.29x faster   |
| pathlib                    | 30.4 ms   | 24.6 ms: 1.23x faster  |
| regex_effbot               | 1.65 ms   | 1.46 ms: 1.13x faster  |
| create_gc_cycles           | 1.37 ms   | 1.25 ms: 1.10x faster  |
| python_startup             | 26.6 ms   | 24.5 ms: 1.09x faster  |
| python_startup_no_site     | 20.0 ms   | 18.7 ms: 1.07x faster  |
| regex_dna                  | 121 ms    | 116 ms: 1.04x faster   |
| xml_etree_iterparse        | 60.7 ms   | 62.3 ms: 1.03x slower  |
| shortest_path              | 345 ms    | 354 ms: 1.03x slower   |
| sqlite_synth               | 1.49 us   | 1.57 us: 1.05x slower  |
| dulwich_log                | 39.5 ms   | 42.4 ms: 1.07x slower  |
| k_core                     | 1.61 sec  | 1.73 sec: 1.08x slower |
| json_loads                 | 14.2 us   | 15.3 us: 1.08x slower  |
| meteor_contest             | 68.7 ms   | 74.3 ms: 1.08x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 340 ms: 1.10x slower   |
| docutils                   | 1.55 sec  | 1.71 sec: 1.10x slower |
| async_tree_cpu_io_mixed_tg | 310 ms    | 344 ms: 1.11x slower   |
| 2to3                       | 204 ms    | 227 ms: 1.11x slower   |
| json                       | 2.83 ms   | 3.16 ms: 1.12x slower  |
| sympy_sum                  | 81.4 ms   | 90.8 ms: 1.12x slower  |
| sphinx                     | 599 ms    | 670 ms: 1.12x slower   |
| async_tree_memoization_tg  | 195 ms    | 219 ms: 1.12x slower   |
| telco                      | 4.20 ms   | 4.75 ms: 1.13x slower  |
| mako                       | 5.72 ms   | 6.50 ms: 1.14x slower  |
| pylint                     | 182 ms    | 208 ms: 1.14x slower   |
| html5lib                   | 35.2 ms   | 40.5 ms: 1.15x slower  |
| float                      | 38.5 ms   | 44.2 ms: 1.15x slower  |
| sympy_integrate            | 11.8 ms   | 13.6 ms: 1.16x slower  |
| sympy_str                  | 153 ms    | 177 ms: 1.16x slower   |
| async_generators           | 188 ms    | 219 ms: 1.16x slower   |
| json_dumps                 | 5.76 ms   | 6.69 ms: 1.16x slower  |
| async_tree_io_tg           | 352 ms    | 410 ms: 1.17x slower   |
| xml_etree_process          | 34.0 ms   | 39.7 ms: 1.17x slower  |
| pycparser                  | 637 ms    | 745 ms: 1.17x slower   |
| bpe_tokeniser              | 2.50 sec  | 2.93 sec: 1.17x slower |
| regex_compile              | 73.4 ms   | 86.1 ms: 1.17x slower  |
| xml_etree_generate         | 48.4 ms   | 56.8 ms: 1.17x slower  |
| async_tree_memoization     | 190 ms    | 223 ms: 1.18x slower   |
| sympy_expand               | 259 ms    | 305 ms: 1.18x slower   |
| coroutines                 | 11.1 ms   | 13.1 ms: 1.18x slower  |
| async_tree_none_tg         | 147 ms    | 176 ms: 1.19x slower   |
| async_tree_io              | 349 ms    | 417 ms: 1.19x slower   |
| sqlglot_v2_optimize        | 29.8 ms   | 35.6 ms: 1.20x slower  |
| async_tree_none            | 155 ms    | 186 ms: 1.20x slower   |
| coverage                   | 40.9 ms   | 49.2 ms: 1.20x slower  |
| thrift                     | 434 us    | 522 us: 1.20x slower   |
| logging_simple             | 5.39 us   | 6.53 us: 1.21x slower  |
| logging_format             | 5.83 us   | 7.11 us: 1.22x slower  |
| pyflate                    | 245 ms    | 300 ms: 1.23x slower   |
| typing_runtime_protocols   | 86.2 us   | 106 us: 1.23x slower   |
| pprint_safe_repr           | 432 ms    | 532 ms: 1.23x slower   |
| crypto_pyaes               | 39.4 ms   | 48.6 ms: 1.23x slower  |
| pickle_pure_python         | 175 us    | 217 us: 1.24x slower   |
| scimark_lu                 | 49.1 ms   | 61.1 ms: 1.24x slower  |
| pprint_pformat             | 874 ms    | 1.09 sec: 1.24x slower |
| mdp                        | 1.30 sec  | 1.62 sec: 1.25x slower |
| fannkuch                   | 209 ms    | 263 ms: 1.26x slower   |
| sqlglot_v2_transpile       | 868 us    | 1.09 ms: 1.26x slower  |
| deepcopy_reduce            | 1.49 us   | 1.88 us: 1.26x slower  |
| comprehensions             | 8.84 us   | 11.2 us: 1.26x slower  |
| sqlglot_v2_parse           | 686 us    | 870 us: 1.27x slower   |
| deepcopy_memo              | 15.1 us   | 19.1 us: 1.27x slower  |
| generators                 | 15.8 ms   | 20.0 ms: 1.27x slower  |
| tomli_loads                | 1.13 sec  | 1.44 sec: 1.27x slower |
| sqlglot_v2_normalize       | 59.9 ms   | 76.3 ms: 1.27x slower  |
| genshi_xml                 | 27.4 ms   | 35.0 ms: 1.28x slower  |
| deepcopy                   | 145 us    | 185 us: 1.28x slower   |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.63 ms: 1.28x slower  |
| logging_silent             | 44.5 ns   | 57.0 ns: 1.28x slower  |
| go                         | 65.1 ms   | 84.1 ms: 1.29x slower  |
| spectral_norm              | 44.7 ms   | 58.1 ms: 1.30x slower  |
| nqueens                    | 47.7 ms   | 62.2 ms: 1.30x slower  |
| django_template            | 19.5 ms   | 25.5 ms: 1.31x slower  |
| scimark_fft                | 143 ms    | 187 ms: 1.31x slower   |
| genshi_text                | 12.0 ms   | 15.8 ms: 1.33x slower  |
| unpickle_pure_python       | 109 us    | 147 us: 1.35x slower   |
| chaos                      | 31.1 ms   | 42.2 ms: 1.36x slower  |
| hexiom                     | 3.13 ms   | 4.28 ms: 1.37x slower  |
| deltablue                  | 1.59 ms   | 2.18 ms: 1.37x slower  |
| scimark_monte_carlo        | 32.8 ms   | 45.3 ms: 1.38x slower  |
| scimark_sor                | 59.1 ms   | 84.2 ms: 1.43x slower  |
| raytrace                   | 137 ms    | 201 ms: 1.46x slower   |
| nbody                      | 52.9 ms   | 78.3 ms: 1.48x slower  |
| richards                   | 21.9 ms   | 34.5 ms: 1.58x slower  |
| richards_super             | 24.6 ms   | 39.9 ms: 1.62x slower  |
| many_optionals             | 405 us    | 695 us: 1.71x slower   |
| subparsers                 | 14.2 ms   | 41.0 ms: 2.88x slower  |
| Geometric mean             | (ref)     | 1.19x slower           |

Benchmark hidden because not significant (4): connected_components, pidigits, xml_etree_parse, regex_v8

- Geometric mean (including insignificant results): 1.157x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown