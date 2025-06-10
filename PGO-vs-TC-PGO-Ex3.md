# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.147x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO                    |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 227 ms: 1.11x slower   |
| docutils       | 1.58 sec   | 1.68 sec: 1.06x slower |
| html5lib       | 35.5 ms    | 40.8 ms: 1.15x slower  |
| sphinx         | 615 ms     | 658 ms: 1.07x slower   |
| Geometric mean | (ref)      | 1.10x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | PGO                   |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 327 ms     | 339 ms: 1.04x slower  |
| asyncio_websockets         | 304 ms     | 318 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 343 ms: 1.05x slower  |
| async_tree_memoization_tg  | 201 ms     | 216 ms: 1.07x slower  |
| async_generators           | 199 ms     | 226 ms: 1.14x slower  |
| async_tree_memoization     | 196 ms     | 224 ms: 1.14x slower  |
| async_tree_io_tg           | 356 ms     | 410 ms: 1.15x slower  |
| async_tree_none_tg         | 150 ms     | 176 ms: 1.18x slower  |
| async_tree_none            | 157 ms     | 187 ms: 1.19x slower  |
| async_tree_io              | 353 ms     | 423 ms: 1.20x slower  |
| coroutines                 | 10.8 ms    | 13.5 ms: 1.25x slower |
| Geometric mean             | (ref)      | 1.13x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO                   |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 152 ms: 1.05x slower  |
| float          | 37.1 ms    | 47.8 ms: 1.29x slower |
| nbody          | 45.7 ms    | 74.1 ms: 1.62x slower |
| Geometric mean | (ref)      | 1.30x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | PGO                   |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 112 ms: 1.07x faster  |
| regex_v8       | 13.9 ms    | 13.5 ms: 1.03x faster |
| regex_effbot   | 1.45 ms    | 1.42 ms: 1.02x faster |
| regex_compile  | 70.7 ms    | 88.2 ms: 1.25x slower |
| Geometric mean | (ref)      | 1.03x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | PGO                    |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 91.2 ms: 1.02x slower  |
| xml_etree_iterparse  | 59.5 ms    | 63.7 ms: 1.07x slower  |
| json_dumps           | 6.19 ms    | 7.05 ms: 1.14x slower  |
| xml_etree_generate   | 49.4 ms    | 58.7 ms: 1.19x slower  |
| xml_etree_process    | 33.8 ms    | 41.5 ms: 1.23x slower  |
| pickle_pure_python   | 184 us     | 237 us: 1.29x slower   |
| unpickle_pure_python | 110 us     | 155 us: 1.42x slower   |
| tomli_loads          | 1.03 sec   | 1.47 sec: 1.43x slower |
| Geometric mean       | (ref)      | 1.19x slower           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | PGO                   |
|------------------------|:----------:|:---------------------:|
| python_startup         | 24.7 ms    | 26.1 ms: 1.05x slower |
| python_startup_no_site | 18.7 ms    | 19.8 ms: 1.06x slower |
| Geometric mean         | (ref)      | 1.06x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | PGO                   |
|-----------------|:----------:|:---------------------:|
| mako            | 5.80 ms    | 6.86 ms: 1.18x slower |
| django_template | 20.9 ms    | 25.1 ms: 1.20x slower |
| genshi_xml      | 29.5 ms    | 36.3 ms: 1.23x slower |
| genshi_text     | 12.3 ms    | 16.5 ms: 1.34x slower |
| Geometric mean  | (ref)      | 1.24x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | PGO                    |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 40.6 ms    | 16.1 ms: 2.52x faster  |
| many_optionals             | 659 us     | 438 us: 1.50x faster   |
| regex_dna                  | 121 ms     | 112 ms: 1.07x faster   |
| regex_v8                   | 13.9 ms    | 13.5 ms: 1.03x faster  |
| regex_effbot               | 1.45 ms    | 1.42 ms: 1.02x faster  |
| gc_traversal               | 2.09 ms    | 2.06 ms: 1.02x faster  |
| create_gc_cycles           | 1.26 ms    | 1.25 ms: 1.01x faster  |
| coverage                   | 46.2 ms    | 46.8 ms: 1.01x slower  |
| sqlite_synth               | 1.56 us    | 1.59 us: 1.02x slower  |
| xml_etree_parse            | 89.4 ms    | 91.2 ms: 1.02x slower  |
| connected_components       | 320 ms     | 329 ms: 1.03x slower   |
| shortest_path              | 347 ms     | 359 ms: 1.04x slower   |
| k_core                     | 1.67 sec   | 1.73 sec: 1.04x slower |
| async_tree_cpu_io_mixed    | 327 ms     | 339 ms: 1.04x slower   |
| pylint                     | 193 ms     | 201 ms: 1.04x slower   |
| asyncio_websockets         | 304 ms     | 318 ms: 1.05x slower   |
| pidigits                   | 145 ms     | 152 ms: 1.05x slower   |
| python_startup             | 24.7 ms    | 26.1 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 343 ms: 1.05x slower   |
| python_startup_no_site     | 18.7 ms    | 19.8 ms: 1.06x slower  |
| json                       | 2.95 ms    | 3.14 ms: 1.06x slower  |
| docutils                   | 1.58 sec   | 1.68 sec: 1.06x slower |
| sphinx                     | 615 ms     | 658 ms: 1.07x slower   |
| xml_etree_iterparse        | 59.5 ms    | 63.7 ms: 1.07x slower  |
| async_tree_memoization_tg  | 201 ms     | 216 ms: 1.07x slower   |
| thrift                     | 461 us     | 507 us: 1.10x slower   |
| telco                      | 4.45 ms    | 4.89 ms: 1.10x slower  |
| dulwich_log                | 39.1 ms    | 43.4 ms: 1.11x slower  |
| 2to3                       | 204 ms     | 227 ms: 1.11x slower   |
| sympy_sum                  | 80.7 ms    | 90.5 ms: 1.12x slower  |
| sympy_integrate            | 12.0 ms    | 13.5 ms: 1.13x slower  |
| json_dumps                 | 6.19 ms    | 7.05 ms: 1.14x slower  |
| async_generators           | 199 ms     | 226 ms: 1.14x slower   |
| async_tree_memoization     | 196 ms     | 224 ms: 1.14x slower   |
| sympy_str                  | 153 ms     | 176 ms: 1.15x slower   |
| sqlglot_v2_optimize        | 30.5 ms    | 35.0 ms: 1.15x slower  |
| pycparser                  | 642 ms     | 738 ms: 1.15x slower   |
| html5lib                   | 35.5 ms    | 40.8 ms: 1.15x slower  |
| sympy_expand               | 263 ms     | 302 ms: 1.15x slower   |
| async_tree_io_tg           | 356 ms     | 410 ms: 1.15x slower   |
| meteor_contest             | 66.6 ms    | 76.9 ms: 1.15x slower  |
| mdp                        | 1.41 sec   | 1.64 sec: 1.17x slower |
| bpe_tokeniser              | 2.52 sec   | 2.96 sec: 1.17x slower |
| async_tree_none_tg         | 150 ms     | 176 ms: 1.18x slower   |
| sqlglot_v2_normalize       | 62.6 ms    | 73.6 ms: 1.18x slower  |
| typing_runtime_protocols   | 89.7 us    | 106 us: 1.18x slower   |
| mako                       | 5.80 ms    | 6.86 ms: 1.18x slower  |
| async_tree_none            | 157 ms     | 187 ms: 1.19x slower   |
| xml_etree_generate         | 49.4 ms    | 58.7 ms: 1.19x slower  |
| logging_format             | 5.90 us    | 7.03 us: 1.19x slower  |
| richards_super             | 29.4 ms    | 35.1 ms: 1.19x slower  |
| async_tree_io              | 353 ms     | 423 ms: 1.20x slower   |
| django_template            | 20.9 ms    | 25.1 ms: 1.20x slower  |
| richards                   | 25.5 ms    | 30.7 ms: 1.21x slower  |
| logging_simple             | 5.42 us    | 6.53 us: 1.21x slower  |
| xml_etree_process          | 33.8 ms    | 41.5 ms: 1.23x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.10 ms: 1.23x slower  |
| genshi_xml                 | 29.5 ms    | 36.3 ms: 1.23x slower  |
| crypto_pyaes               | 40.4 ms    | 50.0 ms: 1.24x slower  |
| regex_compile              | 70.7 ms    | 88.2 ms: 1.25x slower  |
| coroutines                 | 10.8 ms    | 13.5 ms: 1.25x slower  |
| nqueens                    | 49.7 ms    | 63.6 ms: 1.28x slower  |
| deepcopy_reduce            | 1.51 us    | 1.94 us: 1.28x slower  |
| sqlglot_v2_parse           | 695 us     | 892 us: 1.28x slower   |
| pickle_pure_python         | 184 us     | 237 us: 1.29x slower   |
| float                      | 37.1 ms    | 47.8 ms: 1.29x slower  |
| deepcopy                   | 147 us     | 190 us: 1.29x slower   |
| pprint_safe_repr           | 429 ms     | 558 ms: 1.30x slower   |
| comprehensions             | 8.65 us    | 11.3 us: 1.31x slower  |
| raytrace                   | 145 ms     | 191 ms: 1.31x slower   |
| pprint_pformat             | 853 ms     | 1.13 sec: 1.32x slower |
| pyflate                    | 236 ms     | 315 ms: 1.34x slower   |
| genshi_text                | 12.3 ms    | 16.5 ms: 1.34x slower  |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.72 ms: 1.35x slower  |
| generators                 | 14.2 ms    | 19.3 ms: 1.36x slower  |
| pathlib                    | 23.6 ms    | 32.1 ms: 1.36x slower  |
| scimark_fft                | 140 ms     | 192 ms: 1.37x slower   |
| chaos                      | 31.3 ms    | 43.6 ms: 1.40x slower  |
| deltablue                  | 1.64 ms    | 2.29 ms: 1.40x slower  |
| unpickle_pure_python       | 110 us     | 155 us: 1.42x slower   |
| tomli_loads                | 1.03 sec   | 1.47 sec: 1.43x slower |
| deepcopy_memo              | 14.7 us    | 21.0 us: 1.43x slower  |
| go                         | 61.0 ms    | 88.6 ms: 1.45x slower  |
| fannkuch                   | 203 ms     | 296 ms: 1.46x slower   |
| hexiom                     | 3.00 ms    | 4.38 ms: 1.46x slower  |
| logging_silent             | 44.1 ns    | 65.2 ns: 1.48x slower  |
| scimark_monte_carlo        | 31.5 ms    | 47.1 ms: 1.50x slower  |
| spectral_norm              | 40.9 ms    | 61.5 ms: 1.50x slower  |
| scimark_lu                 | 44.3 ms    | 66.9 ms: 1.51x slower  |
| nbody                      | 45.7 ms    | 74.1 ms: 1.62x slower  |
| scimark_sor                | 51.1 ms    | 91.0 ms: 1.78x slower  |
| Geometric mean             | (ref)      | 1.18x slower           |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.147x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown