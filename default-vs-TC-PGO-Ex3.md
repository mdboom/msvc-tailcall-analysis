# Results vs. base

- fork: unknown
- ref: default
- machine: unknown-unknown
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.380x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.46x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | default                |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 298 ms: 1.46x slower   |
| docutils       | 1.58 sec   | 2.17 sec: 1.37x slower |
| html5lib       | 35.5 ms    | 51.3 ms: 1.45x slower  |
| sphinx         | 615 ms     | 872 ms: 1.42x slower   |
| Geometric mean | (ref)      | 1.42x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | default               |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 304 ms     | 317 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 424 ms: 1.31x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 437 ms: 1.34x slower  |
| async_tree_memoization_tg  | 201 ms     | 291 ms: 1.45x slower  |
| async_tree_memoization     | 196 ms     | 297 ms: 1.52x slower  |
| async_tree_io              | 353 ms     | 553 ms: 1.56x slower  |
| async_tree_io_tg           | 356 ms     | 559 ms: 1.57x slower  |
| async_tree_none_tg         | 150 ms     | 236 ms: 1.58x slower  |
| async_tree_none            | 157 ms     | 249 ms: 1.59x slower  |
| async_generators           | 199 ms     | 328 ms: 1.65x slower  |
| coroutines                 | 10.8 ms    | 21.9 ms: 2.03x slower |
| Geometric mean             | (ref)      | 1.49x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | default               |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 152 ms: 1.05x slower  |
| float          | 37.1 ms    | 75.4 ms: 2.03x slower |
| nbody          | 45.7 ms    | 101 ms: 2.20x slower  |
| Geometric mean | (ref)      | 1.67x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | default               |
|----------------|:----------:|:---------------------:|
| regex_v8       | 13.9 ms    | 17.1 ms: 1.23x slower |
| regex_effbot   | 1.45 ms    | 1.81 ms: 1.25x slower |
| regex_compile  | 70.7 ms    | 125 ms: 1.76x slower  |
| Geometric mean | (ref)      | 1.28x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | default                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 108 ms: 1.21x slower   |
| json_dumps           | 6.19 ms    | 9.01 ms: 1.45x slower  |
| xml_etree_iterparse  | 59.5 ms    | 89.9 ms: 1.51x slower  |
| json_loads           | 14.8 us    | 22.3 us: 1.51x slower  |
| xml_etree_generate   | 49.4 ms    | 89.5 ms: 1.81x slower  |
| xml_etree_process    | 33.8 ms    | 64.6 ms: 1.91x slower  |
| pickle_pure_python   | 184 us     | 355 us: 1.93x slower   |
| tomli_loads          | 1.03 sec   | 1.99 sec: 1.94x slower |
| unpickle_pure_python | 110 us     | 274 us: 2.50x slower   |
| Geometric mean       | (ref)      | 1.72x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | default               |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 20.4 ms: 1.09x slower |
| python_startup         | 24.7 ms    | 27.3 ms: 1.11x slower |
| Geometric mean         | (ref)      | 1.10x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | default               |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 48.8 ms: 1.66x slower |
| django_template | 20.9 ms    | 36.9 ms: 1.76x slower |
| genshi_text     | 12.3 ms    | 23.2 ms: 1.88x slower |
| mako            | 5.80 ms    | 11.7 ms: 2.02x slower |
| Geometric mean  | (ref)      | 1.82x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | default                |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 40.6 ms    | 20.8 ms: 1.95x faster  |
| many_optionals             | 659 us     | 547 us: 1.20x faster   |
| asyncio_websockets         | 304 ms     | 317 ms: 1.04x slower   |
| pidigits                   | 145 ms     | 152 ms: 1.05x slower   |
| connected_components       | 320 ms     | 347 ms: 1.08x slower   |
| shortest_path              | 347 ms     | 378 ms: 1.09x slower   |
| python_startup_no_site     | 18.7 ms    | 20.4 ms: 1.09x slower  |
| k_core                     | 1.67 sec   | 1.83 sec: 1.10x slower |
| python_startup             | 24.7 ms    | 27.3 ms: 1.11x slower  |
| create_gc_cycles           | 1.26 ms    | 1.40 ms: 1.11x slower  |
| sqlite_synth               | 1.56 us    | 1.84 us: 1.18x slower  |
| xml_etree_parse            | 89.4 ms    | 108 ms: 1.21x slower   |
| regex_v8                   | 13.9 ms    | 17.1 ms: 1.23x slower  |
| regex_effbot               | 1.45 ms    | 1.81 ms: 1.25x slower  |
| mdp                        | 1.41 sec   | 1.81 sec: 1.29x slower |
| dulwich_log                | 39.1 ms    | 51.0 ms: 1.31x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 424 ms: 1.31x slower   |
| pylint                     | 193 ms     | 253 ms: 1.31x slower   |
| async_tree_cpu_io_mixed    | 327 ms     | 437 ms: 1.34x slower   |
| coverage                   | 46.2 ms    | 61.9 ms: 1.34x slower  |
| json                       | 2.95 ms    | 3.96 ms: 1.34x slower  |
| docutils                   | 1.58 sec   | 2.17 sec: 1.37x slower |
| sphinx                     | 615 ms     | 872 ms: 1.42x slower   |
| meteor_contest             | 66.6 ms    | 95.9 ms: 1.44x slower  |
| html5lib                   | 35.5 ms    | 51.3 ms: 1.45x slower  |
| telco                      | 4.45 ms    | 6.44 ms: 1.45x slower  |
| async_tree_memoization_tg  | 201 ms     | 291 ms: 1.45x slower   |
| json_dumps                 | 6.19 ms    | 9.01 ms: 1.45x slower  |
| pathlib                    | 23.6 ms    | 34.4 ms: 1.46x slower  |
| 2to3                       | 204 ms     | 298 ms: 1.46x slower   |
| sympy_sum                  | 80.7 ms    | 119 ms: 1.48x slower   |
| sympy_integrate            | 12.0 ms    | 17.8 ms: 1.48x slower  |
| thrift                     | 461 us     | 694 us: 1.50x slower   |
| gc_traversal               | 2.09 ms    | 3.15 ms: 1.51x slower  |
| xml_etree_iterparse        | 59.5 ms    | 89.9 ms: 1.51x slower  |
| json_loads                 | 14.8 us    | 22.3 us: 1.51x slower  |
| async_tree_memoization     | 196 ms     | 297 ms: 1.52x slower   |
| sympy_expand               | 263 ms     | 405 ms: 1.54x slower   |
| pycparser                  | 642 ms     | 992 ms: 1.54x slower   |
| sympy_str                  | 153 ms     | 238 ms: 1.55x slower   |
| async_tree_io              | 353 ms     | 553 ms: 1.56x slower   |
| async_tree_io_tg           | 356 ms     | 559 ms: 1.57x slower   |
| async_tree_none_tg         | 150 ms     | 236 ms: 1.58x slower   |
| logging_format             | 5.90 us    | 9.33 us: 1.58x slower  |
| async_tree_none            | 157 ms     | 249 ms: 1.59x slower   |
| logging_simple             | 5.42 us    | 8.87 us: 1.64x slower  |
| async_generators           | 199 ms     | 328 ms: 1.65x slower   |
| genshi_xml                 | 29.5 ms    | 48.8 ms: 1.66x slower  |
| sqlglot_v2_optimize        | 30.5 ms    | 51.0 ms: 1.67x slower  |
| typing_runtime_protocols   | 89.7 us    | 150 us: 1.68x slower   |
| sqlglot_v2_normalize       | 62.6 ms    | 106 ms: 1.70x slower   |
| bpe_tokeniser              | 2.52 sec   | 4.30 sec: 1.71x slower |
| django_template            | 20.9 ms    | 36.9 ms: 1.76x slower  |
| regex_compile              | 70.7 ms    | 125 ms: 1.76x slower   |
| xml_etree_generate         | 49.4 ms    | 89.5 ms: 1.81x slower  |
| deepcopy_reduce            | 1.51 us    | 2.77 us: 1.83x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.64 ms: 1.83x slower  |
| pprint_safe_repr           | 429 ms     | 788 ms: 1.84x slower   |
| deepcopy                   | 147 us     | 269 us: 1.84x slower   |
| genshi_text                | 12.3 ms    | 23.2 ms: 1.88x slower  |
| pprint_pformat             | 853 ms     | 1.61 sec: 1.89x slower |
| nqueens                    | 49.7 ms    | 94.3 ms: 1.90x slower  |
| xml_etree_process          | 33.8 ms    | 64.6 ms: 1.91x slower  |
| scimark_fft                | 140 ms     | 269 ms: 1.91x slower   |
| crypto_pyaes               | 40.4 ms    | 77.9 ms: 1.93x slower  |
| pickle_pure_python         | 184 us     | 355 us: 1.93x slower   |
| tomli_loads                | 1.03 sec   | 1.99 sec: 1.94x slower |
| pyflate                    | 236 ms     | 462 ms: 1.96x slower   |
| sqlglot_v2_parse           | 695 us     | 1.36 ms: 1.96x slower  |
| fannkuch                   | 203 ms     | 407 ms: 2.01x slower   |
| mako                       | 5.80 ms    | 11.7 ms: 2.02x slower  |
| coroutines                 | 10.8 ms    | 21.9 ms: 2.03x slower  |
| float                      | 37.1 ms    | 75.4 ms: 2.03x slower  |
| chaos                      | 31.3 ms    | 65.2 ms: 2.09x slower  |
| raytrace                   | 145 ms     | 304 ms: 2.09x slower   |
| scimark_sparse_mat_mult    | 2.02 ms    | 4.34 ms: 2.15x slower  |
| nbody                      | 45.7 ms    | 101 ms: 2.20x slower   |
| richards_super             | 29.4 ms    | 65.8 ms: 2.23x slower  |
| comprehensions             | 8.65 us    | 19.4 us: 2.24x slower  |
| deepcopy_memo              | 14.7 us    | 32.9 us: 2.24x slower  |
| go                         | 61.0 ms    | 137 ms: 2.25x slower   |
| richards                   | 25.5 ms    | 57.8 ms: 2.27x slower  |
| scimark_monte_carlo        | 31.5 ms    | 73.9 ms: 2.35x slower  |
| generators                 | 14.2 ms    | 33.8 ms: 2.37x slower  |
| spectral_norm              | 40.9 ms    | 97.7 ms: 2.39x slower  |
| hexiom                     | 3.00 ms    | 7.27 ms: 2.43x slower  |
| deltablue                  | 1.64 ms    | 4.09 ms: 2.49x slower  |
| unpickle_pure_python       | 110 us     | 274 us: 2.50x slower   |
| scimark_lu                 | 44.3 ms    | 116 ms: 2.62x slower   |
| scimark_sor                | 51.1 ms    | 135 ms: 2.64x slower   |
| logging_silent             | 44.1 ns    | 119 ns: 2.71x slower   |
| Geometric mean             | (ref)      | 1.62x slower           |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (2) of default.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.380x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.52x
- 95% likely to have a slowdown of 1.50x
- 99% likely to have a slowdown of 1.46x

# Memory
- memory change: unknown