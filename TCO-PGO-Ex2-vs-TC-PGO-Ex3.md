# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.183x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 237 ms: 1.16x slower   |
| docutils       | 1.58 sec   | 1.81 sec: 1.15x slower |
| html5lib       | 35.5 ms    | 40.8 ms: 1.15x slower  |
| sphinx         | 615 ms     | 723 ms: 1.18x slower   |
| Geometric mean | (ref)      | 1.16x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------------------|:----------:|:---------------------:|
| async_tree_memoization_tg  | 201 ms     | 218 ms: 1.09x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 362 ms: 1.11x slower  |
| async_generators           | 199 ms     | 224 ms: 1.13x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 367 ms: 1.13x slower  |
| async_tree_memoization     | 196 ms     | 227 ms: 1.16x slower  |
| async_tree_io_tg           | 356 ms     | 419 ms: 1.18x slower  |
| async_tree_none_tg         | 150 ms     | 178 ms: 1.18x slower  |
| async_tree_none            | 157 ms     | 188 ms: 1.20x slower  |
| async_tree_io              | 353 ms     | 429 ms: 1.21x slower  |
| coroutines                 | 10.8 ms    | 13.5 ms: 1.25x slower |
| Geometric mean             | (ref)      | 1.15x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 147 ms: 1.01x slower  |
| float          | 37.1 ms    | 44.8 ms: 1.21x slower |
| nbody          | 45.7 ms    | 58.8 ms: 1.28x slower |
| Geometric mean | (ref)      | 1.16x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 117 ms: 1.03x faster  |
| regex_v8       | 13.9 ms    | 16.7 ms: 1.19x slower |
| regex_effbot   | 1.45 ms    | 1.76 ms: 1.21x slower |
| regex_compile  | 70.7 ms    | 88.0 ms: 1.25x slower |
| Geometric mean | (ref)      | 1.15x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 104 ms: 1.16x slower   |
| xml_etree_iterparse  | 59.5 ms    | 71.5 ms: 1.20x slower  |
| pickle_pure_python   | 184 us     | 236 us: 1.28x slower   |
| json_dumps           | 6.19 ms    | 7.94 ms: 1.28x slower  |
| tomli_loads          | 1.03 sec   | 1.38 sec: 1.35x slower |
| xml_etree_generate   | 49.4 ms    | 66.8 ms: 1.35x slower  |
| xml_etree_process    | 33.8 ms    | 46.5 ms: 1.38x slower  |
| unpickle_pure_python | 110 us     | 154 us: 1.40x slower   |
| json_loads           | 14.8 us    | 21.1 us: 1.43x slower  |
| Geometric mean       | (ref)      | 1.31x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 20.1 ms: 1.07x slower |
| python_startup         | 24.7 ms    | 26.9 ms: 1.09x slower |
| Geometric mean         | (ref)      | 1.08x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-PGO-Ex2           |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 35.3 ms: 1.20x slower |
| mako            | 5.80 ms    | 7.44 ms: 1.28x slower |
| genshi_text     | 12.3 ms    | 16.2 ms: 1.31x slower |
| django_template | 20.9 ms    | 27.5 ms: 1.31x slower |
| Geometric mean  | (ref)      | 1.27x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex2            |
|----------------------------|:----------:|:----------------------:|
| regex_dna                  | 121 ms     | 117 ms: 1.03x faster   |
| pidigits                   | 145 ms     | 147 ms: 1.01x slower   |
| connected_components       | 320 ms     | 326 ms: 1.02x slower   |
| shortest_path              | 347 ms     | 357 ms: 1.03x slower   |
| k_core                     | 1.67 sec   | 1.76 sec: 1.05x slower |
| python_startup_no_site     | 18.7 ms    | 20.1 ms: 1.07x slower  |
| sqlite_synth               | 1.56 us    | 1.68 us: 1.08x slower  |
| pathlib                    | 23.6 ms    | 25.6 ms: 1.08x slower  |
| async_tree_memoization_tg  | 201 ms     | 218 ms: 1.09x slower   |
| python_startup             | 24.7 ms    | 26.9 ms: 1.09x slower  |
| create_gc_cycles           | 1.26 ms    | 1.38 ms: 1.10x slower  |
| dulwich_log                | 39.1 ms    | 43.0 ms: 1.10x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 362 ms: 1.11x slower   |
| mdp                        | 1.41 sec   | 1.57 sec: 1.12x slower |
| async_generators           | 199 ms     | 224 ms: 1.13x slower   |
| pylint                     | 193 ms     | 217 ms: 1.13x slower   |
| async_tree_cpu_io_mixed_tg | 325 ms     | 367 ms: 1.13x slower   |
| docutils                   | 1.58 sec   | 1.81 sec: 1.15x slower |
| html5lib                   | 35.5 ms    | 40.8 ms: 1.15x slower  |
| async_tree_memoization     | 196 ms     | 227 ms: 1.16x slower   |
| sympy_integrate            | 12.0 ms    | 13.9 ms: 1.16x slower  |
| xml_etree_parse            | 89.4 ms    | 104 ms: 1.16x slower   |
| subparsers                 | 40.6 ms    | 47.1 ms: 1.16x slower  |
| 2to3                       | 204 ms     | 237 ms: 1.16x slower   |
| meteor_contest             | 66.6 ms    | 78.1 ms: 1.17x slower  |
| sphinx                     | 615 ms     | 723 ms: 1.18x slower   |
| async_tree_io_tg           | 356 ms     | 419 ms: 1.18x slower   |
| async_tree_none_tg         | 150 ms     | 178 ms: 1.18x slower   |
| pycparser                  | 642 ms     | 765 ms: 1.19x slower   |
| regex_v8                   | 13.9 ms    | 16.7 ms: 1.19x slower  |
| async_tree_none            | 157 ms     | 188 ms: 1.20x slower   |
| genshi_xml                 | 29.5 ms    | 35.3 ms: 1.20x slower  |
| sympy_sum                  | 80.7 ms    | 96.6 ms: 1.20x slower  |
| telco                      | 4.45 ms    | 5.33 ms: 1.20x slower  |
| xml_etree_iterparse        | 59.5 ms    | 71.5 ms: 1.20x slower  |
| float                      | 37.1 ms    | 44.8 ms: 1.21x slower  |
| regex_effbot               | 1.45 ms    | 1.76 ms: 1.21x slower  |
| async_tree_io              | 353 ms     | 429 ms: 1.21x slower   |
| sympy_str                  | 153 ms     | 187 ms: 1.22x slower   |
| thrift                     | 461 us     | 561 us: 1.22x slower   |
| logging_format             | 5.90 us    | 7.18 us: 1.22x slower  |
| crypto_pyaes               | 40.4 ms    | 49.3 ms: 1.22x slower  |
| coverage                   | 46.2 ms    | 56.4 ms: 1.22x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.09 ms: 1.22x slower  |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.48 ms: 1.23x slower  |
| logging_simple             | 5.42 us    | 6.67 us: 1.23x slower  |
| sympy_expand               | 263 ms     | 324 ms: 1.23x slower   |
| many_optionals             | 659 us     | 813 us: 1.23x slower   |
| regex_compile              | 70.7 ms    | 88.0 ms: 1.25x slower  |
| coroutines                 | 10.8 ms    | 13.5 ms: 1.25x slower  |
| pyflate                    | 236 ms     | 295 ms: 1.25x slower   |
| bpe_tokeniser              | 2.52 sec   | 3.17 sec: 1.26x slower |
| typing_runtime_protocols   | 89.7 us    | 113 us: 1.26x slower   |
| sqlglot_v2_optimize        | 30.5 ms    | 38.4 ms: 1.26x slower  |
| sqlglot_v2_parse           | 695 us     | 876 us: 1.26x slower   |
| sqlglot_v2_normalize       | 62.6 ms    | 79.0 ms: 1.26x slower  |
| scimark_fft                | 140 ms     | 178 ms: 1.27x slower   |
| generators                 | 14.2 ms    | 18.1 ms: 1.27x slower  |
| deltablue                  | 1.64 ms    | 2.09 ms: 1.27x slower  |
| json                       | 2.95 ms    | 3.77 ms: 1.28x slower  |
| go                         | 61.0 ms    | 78.0 ms: 1.28x slower  |
| pickle_pure_python         | 184 us     | 236 us: 1.28x slower   |
| json_dumps                 | 6.19 ms    | 7.94 ms: 1.28x slower  |
| mako                       | 5.80 ms    | 7.44 ms: 1.28x slower  |
| nbody                      | 45.7 ms    | 58.8 ms: 1.28x slower  |
| raytrace                   | 145 ms     | 187 ms: 1.29x slower   |
| pprint_safe_repr           | 429 ms     | 558 ms: 1.30x slower   |
| fannkuch                   | 203 ms     | 265 ms: 1.30x slower   |
| genshi_text                | 12.3 ms    | 16.2 ms: 1.31x slower  |
| django_template            | 20.9 ms    | 27.5 ms: 1.31x slower  |
| nqueens                    | 49.7 ms    | 65.7 ms: 1.32x slower  |
| pprint_pformat             | 853 ms     | 1.13 sec: 1.32x slower |
| gc_traversal               | 2.09 ms    | 2.77 ms: 1.33x slower  |
| chaos                      | 31.3 ms    | 41.4 ms: 1.33x slower  |
| tomli_loads                | 1.03 sec   | 1.38 sec: 1.35x slower |
| xml_etree_generate         | 49.4 ms    | 66.8 ms: 1.35x slower  |
| deepcopy                   | 147 us     | 199 us: 1.36x slower   |
| scimark_monte_carlo        | 31.5 ms    | 42.9 ms: 1.36x slower  |
| richards                   | 25.5 ms    | 35.0 ms: 1.37x slower  |
| richards_super             | 29.4 ms    | 40.4 ms: 1.37x slower  |
| xml_etree_process          | 33.8 ms    | 46.5 ms: 1.38x slower  |
| hexiom                     | 3.00 ms    | 4.17 ms: 1.39x slower  |
| deepcopy_reduce            | 1.51 us    | 2.12 us: 1.40x slower  |
| unpickle_pure_python       | 110 us     | 154 us: 1.40x slower   |
| comprehensions             | 8.65 us    | 12.2 us: 1.41x slower  |
| spectral_norm              | 40.9 ms    | 58.4 ms: 1.43x slower  |
| logging_silent             | 44.1 ns    | 62.9 ns: 1.43x slower  |
| json_loads                 | 14.8 us    | 21.1 us: 1.43x slower  |
| scimark_sor                | 51.1 ms    | 73.9 ms: 1.45x slower  |
| deepcopy_memo              | 14.7 us    | 21.3 us: 1.45x slower  |
| scimark_lu                 | 44.3 ms    | 65.2 ms: 1.47x slower  |
| Geometric mean             | (ref)      | 1.23x slower           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of TCO-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.183x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.18x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: unknown