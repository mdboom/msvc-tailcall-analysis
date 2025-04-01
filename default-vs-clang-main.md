# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.307x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-main | default                |
|----------------|:----------:|:----------------------:|
| 2to3           | 220 ms     | 298 ms: 1.36x slower   |
| docutils       | 1.65 sec   | 2.17 sec: 1.31x slower |
| html5lib       | 39.0 ms    | 51.3 ms: 1.31x slower  |
| sphinx         | 653 ms     | 872 ms: 1.33x slower   |
| Geometric mean | (ref)      | 1.33x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-main | default               |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 342 ms     | 424 ms: 1.24x slower  |
| async_tree_cpu_io_mixed    | 337 ms     | 437 ms: 1.30x slower  |
| async_tree_io              | 416 ms     | 553 ms: 1.33x slower  |
| async_tree_none            | 185 ms     | 249 ms: 1.35x slower  |
| async_tree_none_tg         | 176 ms     | 236 ms: 1.35x slower  |
| async_tree_memoization_tg  | 215 ms     | 291 ms: 1.35x slower  |
| async_tree_io_tg           | 407 ms     | 559 ms: 1.37x slower  |
| async_tree_memoization     | 216 ms     | 297 ms: 1.38x slower  |
| async_generators           | 223 ms     | 328 ms: 1.47x slower  |
| coroutines                 | 13.4 ms    | 21.9 ms: 1.63x slower |
| asyncio_websockets         | 158 ms     | 317 ms: 2.01x slower  |
| Geometric mean             | (ref)      | 1.42x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-main | default               |
|----------------|:----------:|:---------------------:|
| pidigits       | 149 ms     | 152 ms: 1.02x slower  |
| nbody          | 64.2 ms    | 101 ms: 1.57x slower  |
| float          | 44.7 ms    | 75.4 ms: 1.69x slower |
| Geometric mean | (ref)      | 1.39x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-main | default               |
|----------------|:----------:|:---------------------:|
| regex_dna      | 114 ms     | 121 ms: 1.06x slower  |
| regex_v8       | 13.4 ms    | 17.1 ms: 1.28x slower |
| regex_effbot   | 1.39 ms    | 1.81 ms: 1.30x slower |
| regex_compile  | 82.3 ms    | 125 ms: 1.51x slower  |
| Geometric mean | (ref)      | 1.28x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-main | default                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 87.6 ms    | 108 ms: 1.23x slower   |
| json_dumps           | 6.78 ms    | 9.01 ms: 1.33x slower  |
| xml_etree_iterparse  | 64.1 ms    | 89.9 ms: 1.40x slower  |
| tomli_loads          | 1.41 sec   | 1.99 sec: 1.41x slower |
| json_loads           | 15.1 us    | 22.3 us: 1.48x slower  |
| xml_etree_generate   | 57.2 ms    | 89.5 ms: 1.56x slower  |
| xml_etree_process    | 40.9 ms    | 64.6 ms: 1.58x slower  |
| pickle_pure_python   | 216 us     | 355 us: 1.64x slower   |
| unpickle_pure_python | 140 us     | 274 us: 1.96x slower   |
| Geometric mean       | (ref)      | 1.50x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | clang-main | default               |
|----------------|:----------:|:---------------------:|
| python_startup | 25.8 ms    | 27.3 ms: 1.06x slower |
| Geometric mean | (ref)      | 1.03x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-main | default               |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 34.2 ms    | 48.8 ms: 1.43x slower |
| django_template | 25.4 ms    | 36.9 ms: 1.45x slower |
| genshi_text     | 15.8 ms    | 23.2 ms: 1.47x slower |
| mako            | 6.71 ms    | 11.7 ms: 1.74x slower |
| Geometric mean  | (ref)      | 1.52x slower          |

All benchmarks:
===============

| Benchmark                  | clang-main | default                |
|----------------------------|:----------:|:----------------------:|
| pidigits                   | 149 ms     | 152 ms: 1.02x slower   |
| connected_components       | 336 ms     | 347 ms: 1.03x slower   |
| shortest_path              | 366 ms     | 378 ms: 1.03x slower   |
| python_startup             | 25.8 ms    | 27.3 ms: 1.06x slower  |
| regex_dna                  | 114 ms     | 121 ms: 1.06x slower   |
| pathlib                    | 32.5 ms    | 34.4 ms: 1.06x slower  |
| k_core                     | 1.71 sec   | 1.83 sec: 1.07x slower |
| bench_mp_pool              | 88.9 ms    | 96.2 ms: 1.08x slower  |
| create_gc_cycles           | 1.25 ms    | 1.40 ms: 1.13x slower  |
| bench_thread_pool          | 864 us     | 1.01 ms: 1.16x slower  |
| sqlite_synth               | 1.58 us    | 1.84 us: 1.17x slower  |
| dulwich_log                | 42.1 ms    | 51.0 ms: 1.21x slower  |
| xml_etree_parse            | 87.6 ms    | 108 ms: 1.23x slower   |
| async_tree_cpu_io_mixed_tg | 342 ms     | 424 ms: 1.24x slower   |
| meteor_contest             | 76.2 ms    | 95.9 ms: 1.26x slower  |
| pylint                     | 200 ms     | 253 ms: 1.26x slower   |
| many_optionals             | 432 us     | 547 us: 1.27x slower   |
| regex_v8                   | 13.4 ms    | 17.1 ms: 1.28x slower  |
| coverage                   | 48.3 ms    | 61.9 ms: 1.28x slower  |
| json                       | 3.09 ms    | 3.96 ms: 1.28x slower  |
| async_tree_cpu_io_mixed    | 337 ms     | 437 ms: 1.30x slower   |
| regex_effbot               | 1.39 ms    | 1.81 ms: 1.30x slower  |
| subparsers                 | 15.9 ms    | 20.8 ms: 1.31x slower  |
| docutils                   | 1.65 sec   | 2.17 sec: 1.31x slower |
| html5lib                   | 39.0 ms    | 51.3 ms: 1.31x slower  |
| telco                      | 4.87 ms    | 6.44 ms: 1.32x slower  |
| async_tree_io              | 416 ms     | 553 ms: 1.33x slower   |
| json_dumps                 | 6.78 ms    | 9.01 ms: 1.33x slower  |
| sympy_sum                  | 89.6 ms    | 119 ms: 1.33x slower   |
| sphinx                     | 653 ms     | 872 ms: 1.33x slower   |
| async_tree_none            | 185 ms     | 249 ms: 1.35x slower   |
| async_tree_none_tg         | 176 ms     | 236 ms: 1.35x slower   |
| sympy_expand               | 301 ms     | 405 ms: 1.35x slower   |
| async_tree_memoization_tg  | 215 ms     | 291 ms: 1.35x slower   |
| 2to3                       | 220 ms     | 298 ms: 1.36x slower   |
| logging_format             | 6.88 us    | 9.33 us: 1.36x slower  |
| sympy_str                  | 175 ms     | 238 ms: 1.36x slower   |
| pycparser                  | 728 ms     | 992 ms: 1.36x slower   |
| async_tree_io_tg           | 407 ms     | 559 ms: 1.37x slower   |
| async_tree_memoization     | 216 ms     | 297 ms: 1.38x slower   |
| sympy_integrate            | 12.9 ms    | 17.8 ms: 1.38x slower  |
| logging_simple             | 6.39 us    | 8.87 us: 1.39x slower  |
| xml_etree_iterparse        | 64.1 ms    | 89.9 ms: 1.40x slower  |
| typing_runtime_protocols   | 107 us     | 150 us: 1.40x slower   |
| tomli_loads                | 1.41 sec   | 1.99 sec: 1.41x slower |
| genshi_xml                 | 34.2 ms    | 48.8 ms: 1.43x slower  |
| sqlglot_v2_normalize       | 73.4 ms    | 106 ms: 1.45x slower   |
| django_template            | 25.4 ms    | 36.9 ms: 1.45x slower  |
| sqlglot_v2_optimize        | 35.1 ms    | 51.0 ms: 1.45x slower  |
| scimark_fft                | 185 ms     | 269 ms: 1.45x slower   |
| genshi_text                | 15.8 ms    | 23.2 ms: 1.47x slower  |
| async_generators           | 223 ms     | 328 ms: 1.47x slower   |
| bpe_tokeniser              | 2.93 sec   | 4.30 sec: 1.47x slower |
| deepcopy_reduce            | 1.88 us    | 2.77 us: 1.47x slower  |
| json_loads                 | 15.1 us    | 22.3 us: 1.48x slower  |
| nqueens                    | 63.5 ms    | 94.3 ms: 1.49x slower  |
| deepcopy                   | 180 us     | 269 us: 1.49x slower   |
| pprint_pformat             | 1.07 sec   | 1.61 sec: 1.51x slower |
| pprint_safe_repr           | 521 ms     | 788 ms: 1.51x slower   |
| regex_compile              | 82.3 ms    | 125 ms: 1.51x slower   |
| gc_traversal               | 2.08 ms    | 3.15 ms: 1.52x slower  |
| sqlglot_v2_transpile       | 1.05 ms    | 1.64 ms: 1.56x slower  |
| xml_etree_generate         | 57.2 ms    | 89.5 ms: 1.56x slower  |
| fannkuch                   | 260 ms     | 407 ms: 1.57x slower   |
| nbody                      | 64.2 ms    | 101 ms: 1.57x slower   |
| xml_etree_process          | 40.9 ms    | 64.6 ms: 1.58x slower  |
| pyflate                    | 291 ms     | 462 ms: 1.59x slower   |
| sqlglot_v2_parse           | 851 us     | 1.36 ms: 1.60x slower  |
| scimark_sparse_mat_mult    | 2.69 ms    | 4.34 ms: 1.62x slower  |
| chaos                      | 40.2 ms    | 65.2 ms: 1.62x slower  |
| coroutines                 | 13.4 ms    | 21.9 ms: 1.63x slower  |
| pickle_pure_python         | 216 us     | 355 us: 1.64x slower   |
| crypto_pyaes               | 47.3 ms    | 77.9 ms: 1.65x slower  |
| raytrace                   | 181 ms     | 304 ms: 1.68x slower   |
| comprehensions             | 11.5 us    | 19.4 us: 1.69x slower  |
| float                      | 44.7 ms    | 75.4 ms: 1.69x slower  |
| go                         | 80.8 ms    | 137 ms: 1.69x slower   |
| scimark_monte_carlo        | 43.5 ms    | 73.9 ms: 1.70x slower  |
| deepcopy_memo              | 19.1 us    | 32.9 us: 1.72x slower  |
| mako                       | 6.71 ms    | 11.7 ms: 1.74x slower  |
| scimark_sor                | 76.7 ms    | 135 ms: 1.76x slower   |
| hexiom                     | 4.12 ms    | 7.27 ms: 1.77x slower  |
| spectral_norm              | 55.1 ms    | 97.7 ms: 1.77x slower  |
| generators                 | 17.9 ms    | 33.8 ms: 1.88x slower  |
| scimark_lu                 | 61.6 ms    | 116 ms: 1.89x slower   |
| deltablue                  | 2.12 ms    | 4.09 ms: 1.93x slower  |
| unpickle_pure_python       | 140 us     | 274 us: 1.96x slower   |
| asyncio_websockets         | 158 ms     | 317 ms: 2.01x slower   |
| richards                   | 27.8 ms    | 57.8 ms: 2.08x slower  |
| richards_super             | 31.5 ms    | 65.8 ms: 2.09x slower  |
| logging_silent             | 56.3 ns    | 119 ns: 2.12x slower   |
| mdp                        | 799 ms     | 1.81 sec: 2.27x slower |
| Geometric mean             | (ref)      | 1.44x slower           |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of default.json: thrift

- Geometric mean (including insignificant results): 1.307x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.36x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown