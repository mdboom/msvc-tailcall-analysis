# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.147x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO-Ex3                |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 227 ms: 1.11x slower   |
| docutils       | 1.58 sec   | 1.71 sec: 1.08x slower |
| html5lib       | 35.5 ms    | 40.5 ms: 1.14x slower  |
| sphinx         | 615 ms     | 670 ms: 1.09x slower   |
| Geometric mean | (ref)      | 1.11x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | PGO-Ex3               |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 304 ms     | 311 ms: 1.02x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 340 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 344 ms: 1.06x slower  |
| async_tree_memoization_tg  | 201 ms     | 219 ms: 1.09x slower  |
| async_generators           | 199 ms     | 219 ms: 1.10x slower  |
| async_tree_memoization     | 196 ms     | 223 ms: 1.14x slower  |
| async_tree_io_tg           | 356 ms     | 410 ms: 1.15x slower  |
| async_tree_none_tg         | 150 ms     | 176 ms: 1.17x slower  |
| async_tree_io              | 353 ms     | 417 ms: 1.18x slower  |
| async_tree_none            | 157 ms     | 186 ms: 1.18x slower  |
| coroutines                 | 10.8 ms    | 13.1 ms: 1.22x slower |
| Geometric mean             | (ref)      | 1.12x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | PGO-Ex3               |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 148 ms: 1.02x slower  |
| float          | 37.1 ms    | 44.2 ms: 1.19x slower |
| nbody          | 45.7 ms    | 78.3 ms: 1.71x slower |
| Geometric mean | (ref)      | 1.28x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | PGO-Ex3               |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 116 ms: 1.04x faster  |
| regex_compile  | 70.7 ms    | 86.1 ms: 1.22x slower |
| Geometric mean | (ref)      | 1.04x slower          |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | PGO-Ex3                |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 88.8 ms: 1.01x faster  |
| json_loads           | 14.8 us    | 15.3 us: 1.04x slower  |
| xml_etree_iterparse  | 59.5 ms    | 62.3 ms: 1.05x slower  |
| json_dumps           | 6.19 ms    | 6.69 ms: 1.08x slower  |
| xml_etree_generate   | 49.4 ms    | 56.8 ms: 1.15x slower  |
| xml_etree_process    | 33.8 ms    | 39.7 ms: 1.18x slower  |
| pickle_pure_python   | 184 us     | 217 us: 1.18x slower   |
| unpickle_pure_python | 110 us     | 147 us: 1.34x slower   |
| tomli_loads          | 1.03 sec   | 1.44 sec: 1.40x slower |
| Geometric mean       | (ref)      | 1.15x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | TC-PGO-Ex3 | PGO-Ex3               |
|----------------|:----------:|:---------------------:|
| python_startup | 24.7 ms    | 24.5 ms: 1.01x faster |
| Geometric mean | (ref)      | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | PGO-Ex3               |
|-----------------|:----------:|:---------------------:|
| mako            | 5.80 ms    | 6.50 ms: 1.12x slower |
| genshi_xml      | 29.5 ms    | 35.0 ms: 1.19x slower |
| django_template | 20.9 ms    | 25.5 ms: 1.22x slower |
| genshi_text     | 12.3 ms    | 15.8 ms: 1.28x slower |
| Geometric mean  | (ref)      | 1.20x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | PGO-Ex3                |
|----------------------------|:----------:|:----------------------:|
| regex_dna                  | 121 ms     | 116 ms: 1.04x faster   |
| create_gc_cycles           | 1.26 ms    | 1.25 ms: 1.01x faster  |
| python_startup             | 24.7 ms    | 24.5 ms: 1.01x faster  |
| xml_etree_parse            | 89.4 ms    | 88.8 ms: 1.01x faster  |
| sqlite_synth               | 1.56 us    | 1.57 us: 1.01x slower  |
| connected_components       | 320 ms     | 324 ms: 1.01x slower   |
| subparsers                 | 40.6 ms    | 41.0 ms: 1.01x slower  |
| shortest_path              | 347 ms     | 354 ms: 1.02x slower   |
| pidigits                   | 145 ms     | 148 ms: 1.02x slower   |
| asyncio_websockets         | 304 ms     | 311 ms: 1.02x slower   |
| k_core                     | 1.67 sec   | 1.73 sec: 1.04x slower |
| json_loads                 | 14.8 us    | 15.3 us: 1.04x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 340 ms: 1.04x slower   |
| pathlib                    | 23.6 ms    | 24.6 ms: 1.04x slower  |
| xml_etree_iterparse        | 59.5 ms    | 62.3 ms: 1.05x slower  |
| many_optionals             | 659 us     | 695 us: 1.05x slower   |
| async_tree_cpu_io_mixed_tg | 325 ms     | 344 ms: 1.06x slower   |
| coverage                   | 46.2 ms    | 49.2 ms: 1.07x slower  |
| json                       | 2.95 ms    | 3.16 ms: 1.07x slower  |
| telco                      | 4.45 ms    | 4.75 ms: 1.07x slower  |
| json_dumps                 | 6.19 ms    | 6.69 ms: 1.08x slower  |
| docutils                   | 1.58 sec   | 1.71 sec: 1.08x slower |
| pylint                     | 193 ms     | 208 ms: 1.08x slower   |
| dulwich_log                | 39.1 ms    | 42.4 ms: 1.08x slower  |
| sphinx                     | 615 ms     | 670 ms: 1.09x slower   |
| async_tree_memoization_tg  | 201 ms     | 219 ms: 1.09x slower   |
| async_generators           | 199 ms     | 219 ms: 1.10x slower   |
| 2to3                       | 204 ms     | 227 ms: 1.11x slower   |
| meteor_contest             | 66.6 ms    | 74.3 ms: 1.12x slower  |
| mako                       | 5.80 ms    | 6.50 ms: 1.12x slower  |
| sympy_sum                  | 80.7 ms    | 90.8 ms: 1.13x slower  |
| thrift                     | 461 us     | 522 us: 1.13x slower   |
| sympy_integrate            | 12.0 ms    | 13.6 ms: 1.14x slower  |
| async_tree_memoization     | 196 ms     | 223 ms: 1.14x slower   |
| html5lib                   | 35.5 ms    | 40.5 ms: 1.14x slower  |
| xml_etree_generate         | 49.4 ms    | 56.8 ms: 1.15x slower  |
| sympy_str                  | 153 ms     | 177 ms: 1.15x slower   |
| mdp                        | 1.41 sec   | 1.62 sec: 1.15x slower |
| async_tree_io_tg           | 356 ms     | 410 ms: 1.15x slower   |
| pycparser                  | 642 ms     | 745 ms: 1.16x slower   |
| sympy_expand               | 263 ms     | 305 ms: 1.16x slower   |
| bpe_tokeniser              | 2.52 sec   | 2.93 sec: 1.16x slower |
| sqlglot_v2_optimize        | 30.5 ms    | 35.6 ms: 1.17x slower  |
| async_tree_none_tg         | 150 ms     | 176 ms: 1.17x slower   |
| xml_etree_process          | 33.8 ms    | 39.7 ms: 1.18x slower  |
| async_tree_io              | 353 ms     | 417 ms: 1.18x slower   |
| async_tree_none            | 157 ms     | 186 ms: 1.18x slower   |
| pickle_pure_python         | 184 us     | 217 us: 1.18x slower   |
| typing_runtime_protocols   | 89.7 us    | 106 us: 1.18x slower   |
| genshi_xml                 | 29.5 ms    | 35.0 ms: 1.19x slower  |
| float                      | 37.1 ms    | 44.2 ms: 1.19x slower  |
| crypto_pyaes               | 40.4 ms    | 48.6 ms: 1.20x slower  |
| logging_format             | 5.90 us    | 7.11 us: 1.20x slower  |
| logging_simple             | 5.42 us    | 6.53 us: 1.21x slower  |
| coroutines                 | 10.8 ms    | 13.1 ms: 1.22x slower  |
| regex_compile              | 70.7 ms    | 86.1 ms: 1.22x slower  |
| django_template            | 20.9 ms    | 25.5 ms: 1.22x slower  |
| sqlglot_v2_normalize       | 62.6 ms    | 76.3 ms: 1.22x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.09 ms: 1.22x slower  |
| pprint_safe_repr           | 429 ms     | 532 ms: 1.24x slower   |
| deepcopy_reduce            | 1.51 us    | 1.88 us: 1.24x slower  |
| nqueens                    | 49.7 ms    | 62.2 ms: 1.25x slower  |
| sqlglot_v2_parse           | 695 us     | 870 us: 1.25x slower   |
| deepcopy                   | 147 us     | 185 us: 1.26x slower   |
| pyflate                    | 236 ms     | 300 ms: 1.27x slower   |
| pprint_pformat             | 853 ms     | 1.09 sec: 1.28x slower |
| genshi_text                | 12.3 ms    | 15.8 ms: 1.28x slower  |
| comprehensions             | 8.65 us    | 11.2 us: 1.29x slower  |
| fannkuch                   | 203 ms     | 263 ms: 1.29x slower   |
| logging_silent             | 44.1 ns    | 57.0 ns: 1.29x slower  |
| deepcopy_memo              | 14.7 us    | 19.1 us: 1.30x slower  |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.63 ms: 1.30x slower  |
| deltablue                  | 1.64 ms    | 2.18 ms: 1.33x slower  |
| scimark_fft                | 140 ms     | 187 ms: 1.33x slower   |
| unpickle_pure_python       | 110 us     | 147 us: 1.34x slower   |
| chaos                      | 31.3 ms    | 42.2 ms: 1.35x slower  |
| richards                   | 25.5 ms    | 34.5 ms: 1.35x slower  |
| richards_super             | 29.4 ms    | 39.9 ms: 1.36x slower  |
| scimark_lu                 | 44.3 ms    | 61.1 ms: 1.38x slower  |
| go                         | 61.0 ms    | 84.1 ms: 1.38x slower  |
| raytrace                   | 145 ms     | 201 ms: 1.39x slower   |
| tomli_loads                | 1.03 sec   | 1.44 sec: 1.40x slower |
| generators                 | 14.2 ms    | 20.0 ms: 1.41x slower  |
| spectral_norm              | 40.9 ms    | 58.1 ms: 1.42x slower  |
| hexiom                     | 3.00 ms    | 4.28 ms: 1.43x slower  |
| scimark_monte_carlo        | 31.5 ms    | 45.3 ms: 1.44x slower  |
| scimark_sor                | 51.1 ms    | 84.2 ms: 1.65x slower  |
| nbody                      | 45.7 ms    | 78.3 ms: 1.71x slower  |
| Geometric mean             | (ref)      | 1.17x slower           |

Benchmark hidden because not significant (4): regex_v8, gc_traversal, python_startup_no_site, regex_effbot

- Geometric mean (including insignificant results): 1.147x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown