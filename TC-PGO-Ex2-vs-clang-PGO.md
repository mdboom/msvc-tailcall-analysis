# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.075x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | TC-PGO-Ex2             |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 216 ms: 1.06x slower   |
| docutils       | 1.55 sec  | 1.63 sec: 1.05x slower |
| html5lib       | 35.2 ms   | 36.1 ms: 1.02x slower  |
| sphinx         | 599 ms    | 638 ms: 1.06x slower   |
| Geometric mean | (ref)     | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | TC-PGO-Ex2            |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 317 ms: 1.26x faster  |
| async_tree_io_tg           | 352 ms    | 371 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 328 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 309 ms    | 329 ms: 1.07x slower  |
| async_tree_memoization_tg  | 195 ms    | 209 ms: 1.07x slower  |
| async_tree_io              | 349 ms    | 375 ms: 1.07x slower  |
| async_tree_memoization     | 190 ms    | 205 ms: 1.08x slower  |
| async_tree_none_tg         | 147 ms    | 159 ms: 1.08x slower  |
| async_generators           | 188 ms    | 206 ms: 1.09x slower  |
| async_tree_none            | 155 ms    | 170 ms: 1.09x slower  |
| coroutines                 | 11.1 ms   | 12.4 ms: 1.12x slower |
| Geometric mean             | (ref)     | 1.05x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | TC-PGO-Ex2            |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 146 ms: 1.02x faster  |
| nbody          | 52.9 ms   | 53.3 ms: 1.01x slower |
| float          | 38.5 ms   | 40.2 ms: 1.04x slower |
| Geometric mean | (ref)     | 1.01x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | TC-PGO-Ex2            |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.40 ms: 1.18x faster |
| regex_dna      | 121 ms    | 115 ms: 1.05x faster  |
| regex_compile  | 73.4 ms   | 74.8 ms: 1.02x slower |
| regex_v8       | 13.5 ms   | 14.1 ms: 1.04x slower |
| Geometric mean | (ref)     | 1.04x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | TC-PGO-Ex2             |
|----------------------|:---------:|:----------------------:|
| json_loads           | 14.2 us   | 14.5 us: 1.02x slower  |
| tomli_loads          | 1.13 sec  | 1.17 sec: 1.04x slower |
| xml_etree_generate   | 48.4 ms   | 51.5 ms: 1.06x slower  |
| xml_etree_process    | 34.0 ms   | 36.7 ms: 1.08x slower  |
| json_dumps           | 5.76 ms   | 6.48 ms: 1.13x slower  |
| unpickle_pure_python | 109 us    | 123 us: 1.13x slower   |
| pickle_pure_python   | 175 us    | 201 us: 1.15x slower   |
| Geometric mean       | (ref)     | 1.06x slower           |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-PGO | TC-PGO-Ex2            |
|------------------------|:---------:|:---------------------:|
| python_startup         | 26.6 ms   | 26.0 ms: 1.02x faster |
| python_startup_no_site | 20.0 ms   | 19.6 ms: 1.02x faster |
| Geometric mean         | (ref)     | 1.02x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | TC-PGO-Ex2            |
|-----------------|:---------:|:---------------------:|
| mako            | 5.72 ms   | 6.12 ms: 1.07x slower |
| genshi_xml      | 27.4 ms   | 30.7 ms: 1.12x slower |
| genshi_text     | 12.0 ms   | 14.2 ms: 1.19x slower |
| django_template | 19.5 ms   | 23.4 ms: 1.20x slower |
| Geometric mean  | (ref)     | 1.14x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | TC-PGO-Ex2             |
|----------------------------|:---------:|:----------------------:|
| gc_traversal               | 2.79 ms   | 2.07 ms: 1.34x faster  |
| asyncio_websockets         | 400 ms    | 317 ms: 1.26x faster   |
| pathlib                    | 30.4 ms   | 24.3 ms: 1.25x faster  |
| regex_effbot               | 1.65 ms   | 1.40 ms: 1.18x faster  |
| create_gc_cycles           | 1.37 ms   | 1.27 ms: 1.08x faster  |
| generators                 | 15.8 ms   | 14.8 ms: 1.06x faster  |
| regex_dna                  | 121 ms    | 115 ms: 1.05x faster   |
| python_startup             | 26.6 ms   | 26.0 ms: 1.02x faster  |
| python_startup_no_site     | 20.0 ms   | 19.6 ms: 1.02x faster  |
| pidigits                   | 148 ms    | 146 ms: 1.02x faster   |
| connected_components       | 325 ms    | 321 ms: 1.01x faster   |
| nbody                      | 52.9 ms   | 53.3 ms: 1.01x slower  |
| shortest_path              | 345 ms    | 348 ms: 1.01x slower   |
| sympy_sum                  | 81.4 ms   | 82.1 ms: 1.01x slower  |
| meteor_contest             | 68.7 ms   | 69.5 ms: 1.01x slower  |
| json_loads                 | 14.2 us   | 14.5 us: 1.02x slower  |
| regex_compile              | 73.4 ms   | 74.8 ms: 1.02x slower  |
| html5lib                   | 35.2 ms   | 36.1 ms: 1.02x slower  |
| sympy_str                  | 153 ms    | 158 ms: 1.03x slower   |
| sympy_integrate            | 11.8 ms   | 12.2 ms: 1.04x slower  |
| tomli_loads                | 1.13 sec  | 1.17 sec: 1.04x slower |
| sympy_expand               | 259 ms    | 269 ms: 1.04x slower   |
| sqlite_synth               | 1.49 us   | 1.56 us: 1.04x slower  |
| regex_v8                   | 13.5 ms   | 14.1 ms: 1.04x slower  |
| pycparser                  | 637 ms    | 664 ms: 1.04x slower   |
| float                      | 38.5 ms   | 40.2 ms: 1.04x slower  |
| go                         | 65.1 ms   | 68.4 ms: 1.05x slower  |
| docutils                   | 1.55 sec  | 1.63 sec: 1.05x slower |
| json                       | 2.83 ms   | 2.98 ms: 1.05x slower  |
| async_tree_io_tg           | 352 ms    | 371 ms: 1.05x slower   |
| crypto_pyaes               | 39.4 ms   | 41.6 ms: 1.06x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 328 ms: 1.06x slower   |
| 2to3                       | 204 ms    | 216 ms: 1.06x slower   |
| pyflate                    | 245 ms    | 260 ms: 1.06x slower   |
| k_core                     | 1.61 sec  | 1.71 sec: 1.06x slower |
| xml_etree_generate         | 48.4 ms   | 51.5 ms: 1.06x slower  |
| sphinx                     | 599 ms    | 638 ms: 1.06x slower   |
| scimark_fft                | 143 ms    | 152 ms: 1.06x slower   |
| async_tree_cpu_io_mixed    | 309 ms    | 329 ms: 1.07x slower   |
| async_tree_memoization_tg  | 195 ms    | 209 ms: 1.07x slower   |
| mako                       | 5.72 ms   | 6.12 ms: 1.07x slower  |
| logging_simple             | 5.39 us   | 5.78 us: 1.07x slower  |
| async_tree_io              | 349 ms    | 375 ms: 1.07x slower   |
| sqlglot_v2_transpile       | 868 us    | 933 us: 1.07x slower   |
| mdp                        | 1.30 sec  | 1.40 sec: 1.08x slower |
| sqlglot_v2_parse           | 686 us    | 740 us: 1.08x slower   |
| xml_etree_process          | 34.0 ms   | 36.7 ms: 1.08x slower  |
| async_tree_memoization     | 190 ms    | 205 ms: 1.08x slower   |
| telco                      | 4.20 ms   | 4.54 ms: 1.08x slower  |
| sqlglot_v2_optimize        | 29.8 ms   | 32.2 ms: 1.08x slower  |
| async_tree_none_tg         | 147 ms    | 159 ms: 1.08x slower   |
| bpe_tokeniser              | 2.50 sec  | 2.71 sec: 1.08x slower |
| logging_format             | 5.83 us   | 6.34 us: 1.09x slower  |
| pylint                     | 182 ms    | 199 ms: 1.09x slower   |
| async_generators           | 188 ms    | 206 ms: 1.09x slower   |
| async_tree_none            | 155 ms    | 170 ms: 1.09x slower   |
| comprehensions             | 8.84 us   | 9.73 us: 1.10x slower  |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.26 ms: 1.10x slower  |
| deepcopy                   | 145 us    | 160 us: 1.11x slower   |
| pprint_pformat             | 874 ms    | 968 ms: 1.11x slower   |
| pprint_safe_repr           | 432 ms    | 478 ms: 1.11x slower   |
| scimark_lu                 | 49.1 ms   | 54.4 ms: 1.11x slower  |
| hexiom                     | 3.13 ms   | 3.47 ms: 1.11x slower  |
| thrift                     | 434 us    | 482 us: 1.11x slower   |
| deepcopy_reduce            | 1.49 us   | 1.66 us: 1.12x slower  |
| sqlglot_v2_normalize       | 59.9 ms   | 66.9 ms: 1.12x slower  |
| coroutines                 | 11.1 ms   | 12.4 ms: 1.12x slower  |
| genshi_xml                 | 27.4 ms   | 30.7 ms: 1.12x slower  |
| json_dumps                 | 5.76 ms   | 6.48 ms: 1.13x slower  |
| unpickle_pure_python       | 109 us    | 123 us: 1.13x slower   |
| fannkuch                   | 209 ms    | 236 ms: 1.13x slower   |
| scimark_monte_carlo        | 32.8 ms   | 37.0 ms: 1.13x slower  |
| deepcopy_memo              | 15.1 us   | 17.0 us: 1.13x slower  |
| nqueens                    | 47.7 ms   | 54.0 ms: 1.13x slower  |
| scimark_sor                | 59.1 ms   | 67.5 ms: 1.14x slower  |
| spectral_norm              | 44.7 ms   | 51.1 ms: 1.14x slower  |
| typing_runtime_protocols   | 86.2 us   | 98.9 us: 1.15x slower  |
| pickle_pure_python         | 175 us    | 201 us: 1.15x slower   |
| chaos                      | 31.1 ms   | 35.9 ms: 1.15x slower  |
| deltablue                  | 1.59 ms   | 1.85 ms: 1.16x slower  |
| genshi_text                | 12.0 ms   | 14.2 ms: 1.19x slower  |
| django_template            | 19.5 ms   | 23.4 ms: 1.20x slower  |
| logging_silent             | 44.5 ns   | 53.3 ns: 1.20x slower  |
| raytrace                   | 137 ms    | 166 ms: 1.21x slower   |
| coverage                   | 40.9 ms   | 49.5 ms: 1.21x slower  |
| richards                   | 21.9 ms   | 27.8 ms: 1.27x slower  |
| richards_super             | 24.6 ms   | 32.2 ms: 1.31x slower  |
| many_optionals             | 405 us    | 761 us: 1.88x slower   |
| subparsers                 | 14.2 ms   | 44.9 ms: 3.15x slower  |
| Geometric mean             | (ref)     | 1.08x slower           |

Benchmark hidden because not significant (3): xml_etree_iterparse, dulwich_log, xml_etree_parse
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.075x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown