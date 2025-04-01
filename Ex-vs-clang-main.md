# Results vs. base

- fork: unknown
- ref: Ex
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.334x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-main | Ex                     |
|----------------|:----------:|:----------------------:|
| 2to3           | 220 ms     | 309 ms: 1.40x slower   |
| docutils       | 1.65 sec   | 2.31 sec: 1.39x slower |
| html5lib       | 39.0 ms    | 52.5 ms: 1.35x slower  |
| sphinx         | 653 ms     | 933 ms: 1.43x slower   |
| Geometric mean | (ref)      | 1.39x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-main | Ex                    |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 342 ms     | 444 ms: 1.30x slower  |
| async_tree_cpu_io_mixed    | 337 ms     | 455 ms: 1.35x slower  |
| async_tree_io              | 416 ms     | 570 ms: 1.37x slower  |
| async_tree_none_tg         | 176 ms     | 243 ms: 1.39x slower  |
| async_tree_io_tg           | 407 ms     | 576 ms: 1.41x slower  |
| async_tree_memoization_tg  | 215 ms     | 304 ms: 1.42x slower  |
| async_tree_none            | 185 ms     | 267 ms: 1.44x slower  |
| async_tree_memoization     | 216 ms     | 313 ms: 1.45x slower  |
| async_generators           | 223 ms     | 348 ms: 1.56x slower  |
| coroutines                 | 13.4 ms    | 22.4 ms: 1.67x slower |
| asyncio_websockets         | 158 ms     | 330 ms: 2.09x slower  |
| Geometric mean             | (ref)      | 1.48x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-main | Ex                    |
|----------------|:----------:|:---------------------:|
| pidigits       | 149 ms     | 156 ms: 1.04x slower  |
| nbody          | 64.2 ms    | 103 ms: 1.61x slower  |
| float          | 44.7 ms    | 78.0 ms: 1.75x slower |
| Geometric mean | (ref)      | 1.43x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-main | Ex                    |
|----------------|:----------:|:---------------------:|
| regex_dna      | 114 ms     | 123 ms: 1.08x slower  |
| regex_v8       | 13.4 ms    | 17.5 ms: 1.31x slower |
| regex_effbot   | 1.39 ms    | 1.87 ms: 1.34x slower |
| regex_compile  | 82.3 ms    | 130 ms: 1.58x slower  |
| Geometric mean | (ref)      | 1.31x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-main | Ex                     |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 87.6 ms    | 112 ms: 1.28x slower   |
| json_dumps           | 6.78 ms    | 9.44 ms: 1.39x slower  |
| tomli_loads          | 1.41 sec   | 2.07 sec: 1.47x slower |
| xml_etree_iterparse  | 64.1 ms    | 94.3 ms: 1.47x slower  |
| json_loads           | 15.1 us    | 23.3 us: 1.54x slower  |
| xml_etree_generate   | 57.2 ms    | 92.6 ms: 1.62x slower  |
| xml_etree_process    | 40.9 ms    | 66.9 ms: 1.64x slower  |
| pickle_pure_python   | 216 us     | 364 us: 1.69x slower   |
| unpickle_pure_python | 140 us     | 284 us: 2.03x slower   |
| Geometric mean       | (ref)      | 1.56x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-main | Ex                    |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 20.4 ms    | 22.0 ms: 1.08x slower |
| python_startup         | 25.8 ms    | 29.5 ms: 1.14x slower |
| Geometric mean         | (ref)      | 1.11x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-main | Ex                    |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 34.2 ms    | 50.4 ms: 1.48x slower |
| django_template | 25.4 ms    | 38.0 ms: 1.50x slower |
| genshi_text     | 15.8 ms    | 23.9 ms: 1.51x slower |
| mako            | 6.71 ms    | 12.1 ms: 1.80x slower |
| Geometric mean  | (ref)      | 1.57x slower          |

All benchmarks:
===============

| Benchmark                  | clang-main | Ex                     |
|----------------------------|:----------:|:----------------------:|
| pidigits                   | 149 ms     | 156 ms: 1.04x slower   |
| python_startup_no_site     | 20.4 ms    | 22.0 ms: 1.08x slower  |
| regex_dna                  | 114 ms     | 123 ms: 1.08x slower   |
| create_gc_cycles           | 1.25 ms    | 1.42 ms: 1.14x slower  |
| bench_mp_pool              | 88.9 ms    | 101 ms: 1.14x slower   |
| python_startup             | 25.8 ms    | 29.5 ms: 1.14x slower  |
| pathlib                    | 32.5 ms    | 37.5 ms: 1.16x slower  |
| connected_components       | 336 ms     | 395 ms: 1.18x slower   |
| shortest_path              | 366 ms     | 437 ms: 1.19x slower   |
| sqlite_synth               | 1.58 us    | 1.96 us: 1.24x slower  |
| dulwich_log                | 42.1 ms    | 52.4 ms: 1.24x slower  |
| k_core                     | 1.71 sec   | 2.18 sec: 1.27x slower |
| xml_etree_parse            | 87.6 ms    | 112 ms: 1.28x slower   |
| many_optionals             | 432 us     | 559 us: 1.29x slower   |
| async_tree_cpu_io_mixed_tg | 342 ms     | 444 ms: 1.30x slower   |
| meteor_contest             | 76.2 ms    | 99.5 ms: 1.31x slower  |
| regex_v8                   | 13.4 ms    | 17.5 ms: 1.31x slower  |
| coverage                   | 48.3 ms    | 63.7 ms: 1.32x slower  |
| json                       | 3.09 ms    | 4.07 ms: 1.32x slower  |
| regex_effbot               | 1.39 ms    | 1.87 ms: 1.34x slower  |
| pylint                     | 200 ms     | 269 ms: 1.35x slower   |
| html5lib                   | 39.0 ms    | 52.5 ms: 1.35x slower  |
| telco                      | 4.87 ms    | 6.56 ms: 1.35x slower  |
| subparsers                 | 15.9 ms    | 21.5 ms: 1.35x slower  |
| async_tree_cpu_io_mixed    | 337 ms     | 455 ms: 1.35x slower   |
| async_tree_io              | 416 ms     | 570 ms: 1.37x slower   |
| sympy_sum                  | 89.6 ms    | 123 ms: 1.38x slower   |
| async_tree_none_tg         | 176 ms     | 243 ms: 1.39x slower   |
| json_dumps                 | 6.78 ms    | 9.44 ms: 1.39x slower  |
| sympy_expand               | 301 ms     | 419 ms: 1.39x slower   |
| pycparser                  | 728 ms     | 1.01 sec: 1.39x slower |
| docutils                   | 1.65 sec   | 2.31 sec: 1.39x slower |
| 2to3                       | 220 ms     | 309 ms: 1.40x slower   |
| sympy_str                  | 175 ms     | 247 ms: 1.41x slower   |
| async_tree_io_tg           | 407 ms     | 576 ms: 1.41x slower   |
| async_tree_memoization_tg  | 215 ms     | 304 ms: 1.42x slower   |
| sphinx                     | 653 ms     | 933 ms: 1.43x slower   |
| sympy_integrate            | 12.9 ms    | 18.4 ms: 1.43x slower  |
| typing_runtime_protocols   | 107 us     | 154 us: 1.44x slower   |
| async_tree_none            | 185 ms     | 267 ms: 1.44x slower   |
| logging_format             | 6.88 us    | 9.92 us: 1.44x slower  |
| async_tree_memoization     | 216 ms     | 313 ms: 1.45x slower   |
| logging_simple             | 6.39 us    | 9.30 us: 1.46x slower  |
| tomli_loads                | 1.41 sec   | 2.07 sec: 1.47x slower |
| xml_etree_iterparse        | 64.1 ms    | 94.3 ms: 1.47x slower  |
| bench_thread_pool          | 864 us     | 1.28 ms: 1.48x slower  |
| genshi_xml                 | 34.2 ms    | 50.4 ms: 1.48x slower  |
| sqlglot_v2_normalize       | 73.4 ms    | 109 ms: 1.49x slower   |
| scimark_fft                | 185 ms     | 276 ms: 1.49x slower   |
| django_template            | 25.4 ms    | 38.0 ms: 1.50x slower  |
| sqlglot_v2_optimize        | 35.1 ms    | 52.8 ms: 1.51x slower  |
| genshi_text                | 15.8 ms    | 23.9 ms: 1.51x slower  |
| bpe_tokeniser              | 2.93 sec   | 4.45 sec: 1.52x slower |
| deepcopy_reduce            | 1.88 us    | 2.86 us: 1.52x slower  |
| nqueens                    | 63.5 ms    | 96.9 ms: 1.53x slower  |
| json_loads                 | 15.1 us    | 23.3 us: 1.54x slower  |
| deepcopy                   | 180 us     | 278 us: 1.54x slower   |
| pprint_pformat             | 1.07 sec   | 1.66 sec: 1.56x slower |
| async_generators           | 223 ms     | 348 ms: 1.56x slower   |
| gc_traversal               | 2.08 ms    | 3.25 ms: 1.56x slower  |
| regex_compile              | 82.3 ms    | 130 ms: 1.58x slower   |
| pprint_safe_repr           | 521 ms     | 825 ms: 1.58x slower   |
| sqlglot_v2_transpile       | 1.05 ms    | 1.69 ms: 1.60x slower  |
| fannkuch                   | 260 ms     | 418 ms: 1.61x slower   |
| nbody                      | 64.2 ms    | 103 ms: 1.61x slower   |
| xml_etree_generate         | 57.2 ms    | 92.6 ms: 1.62x slower  |
| xml_etree_process          | 40.9 ms    | 66.9 ms: 1.64x slower  |
| pyflate                    | 291 ms     | 477 ms: 1.64x slower   |
| scimark_sparse_mat_mult    | 2.69 ms    | 4.43 ms: 1.65x slower  |
| sqlglot_v2_parse           | 851 us     | 1.41 ms: 1.65x slower  |
| coroutines                 | 13.4 ms    | 22.4 ms: 1.67x slower  |
| pickle_pure_python         | 216 us     | 364 us: 1.69x slower   |
| crypto_pyaes               | 47.3 ms    | 80.1 ms: 1.69x slower  |
| chaos                      | 40.2 ms    | 69.3 ms: 1.73x slower  |
| raytrace                   | 181 ms     | 313 ms: 1.73x slower   |
| go                         | 80.8 ms    | 140 ms: 1.74x slower   |
| scimark_monte_carlo        | 43.5 ms    | 75.8 ms: 1.74x slower  |
| float                      | 44.7 ms    | 78.0 ms: 1.75x slower  |
| comprehensions             | 11.5 us    | 20.1 us: 1.75x slower  |
| deepcopy_memo              | 19.1 us    | 34.0 us: 1.78x slower  |
| mako                       | 6.71 ms    | 12.1 ms: 1.80x slower  |
| hexiom                     | 4.12 ms    | 7.44 ms: 1.81x slower  |
| scimark_sor                | 76.7 ms    | 139 ms: 1.81x slower   |
| spectral_norm              | 55.1 ms    | 102 ms: 1.85x slower   |
| scimark_lu                 | 61.6 ms    | 119 ms: 1.94x slower   |
| generators                 | 17.9 ms    | 35.6 ms: 1.98x slower  |
| deltablue                  | 2.12 ms    | 4.22 ms: 1.99x slower  |
| unpickle_pure_python       | 140 us     | 284 us: 2.03x slower   |
| asyncio_websockets         | 158 ms     | 330 ms: 2.09x slower   |
| richards                   | 27.8 ms    | 59.0 ms: 2.12x slower  |
| richards_super             | 31.5 ms    | 67.7 ms: 2.15x slower  |
| logging_silent             | 56.3 ns    | 124 ns: 2.21x slower   |
| mdp                        | 799 ms     | 1.89 sec: 2.37x slower |
| Geometric mean             | (ref)      | 1.50x slower           |
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of Ex.json: thrift

- Geometric mean (including insignificant results): 1.334x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.42x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: unknown