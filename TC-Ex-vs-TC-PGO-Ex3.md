# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.140x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                  |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 231 ms: 1.13x slower   |
| docutils       | 1.58 sec   | 1.77 sec: 1.12x slower |
| html5lib       | 35.5 ms    | 38.8 ms: 1.09x slower  |
| sphinx         | 615 ms     | 702 ms: 1.14x slower   |
| Geometric mean | (ref)      | 1.12x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TC-Ex                 |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 304 ms     | 312 ms: 1.02x slower  |
| async_tree_memoization_tg  | 201 ms     | 210 ms: 1.05x slower  |
| async_tree_memoization     | 196 ms     | 210 ms: 1.07x slower  |
| async_generators           | 199 ms     | 213 ms: 1.07x slower  |
| async_tree_io_tg           | 356 ms     | 385 ms: 1.08x slower  |
| async_tree_io              | 353 ms     | 384 ms: 1.09x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 359 ms: 1.10x slower  |
| async_tree_none            | 157 ms     | 174 ms: 1.10x slower  |
| async_tree_none_tg         | 150 ms     | 167 ms: 1.11x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 363 ms: 1.12x slower  |
| coroutines                 | 10.8 ms    | 12.3 ms: 1.14x slower |
| Geometric mean             | (ref)      | 1.09x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| float          | 37.1 ms    | 41.4 ms: 1.12x slower |
| nbody          | 45.7 ms    | 53.1 ms: 1.16x slower |
| Geometric mean | (ref)      | 1.09x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TC-Ex                 |
|----------------|:----------:|:---------------------:|
| regex_compile  | 70.7 ms    | 81.9 ms: 1.16x slower |
| regex_v8       | 13.9 ms    | 16.3 ms: 1.17x slower |
| regex_effbot   | 1.45 ms    | 1.85 ms: 1.27x slower |
| Geometric mean | (ref)      | 1.15x slower          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TC-Ex                  |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.4 ms    | 105 ms: 1.17x slower   |
| xml_etree_iterparse  | 59.5 ms    | 70.4 ms: 1.18x slower  |
| pickle_pure_python   | 184 us     | 223 us: 1.21x slower   |
| tomli_loads          | 1.03 sec   | 1.26 sec: 1.23x slower |
| json_dumps           | 6.19 ms    | 7.79 ms: 1.26x slower  |
| xml_etree_generate   | 49.4 ms    | 64.7 ms: 1.31x slower  |
| xml_etree_process    | 33.8 ms    | 44.7 ms: 1.32x slower  |
| unpickle_pure_python | 110 us     | 148 us: 1.35x slower   |
| json_loads           | 14.8 us    | 21.9 us: 1.49x slower  |
| Geometric mean       | (ref)      | 1.28x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TC-Ex                 |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 19.4 ms: 1.04x slower |
| python_startup         | 24.7 ms    | 26.4 ms: 1.07x slower |
| Geometric mean         | (ref)      | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TC-Ex                 |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 31.3 ms: 1.06x slower |
| genshi_text     | 12.3 ms    | 14.5 ms: 1.17x slower |
| django_template | 20.9 ms    | 25.2 ms: 1.20x slower |
| mako            | 5.80 ms    | 7.84 ms: 1.35x slower |
| Geometric mean  | (ref)      | 1.19x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TC-Ex                  |
|----------------------------|:----------:|:----------------------:|
| connected_components       | 320 ms     | 311 ms: 1.03x faster   |
| k_core                     | 1.67 sec   | 1.71 sec: 1.02x slower |
| asyncio_websockets         | 304 ms     | 312 ms: 1.02x slower   |
| mdp                        | 1.41 sec   | 1.44 sec: 1.03x slower |
| python_startup_no_site     | 18.7 ms    | 19.4 ms: 1.04x slower  |
| async_tree_memoization_tg  | 201 ms     | 210 ms: 1.05x slower   |
| create_gc_cycles           | 1.26 ms    | 1.34 ms: 1.06x slower  |
| genshi_xml                 | 29.5 ms    | 31.3 ms: 1.06x slower  |
| pathlib                    | 23.6 ms    | 25.1 ms: 1.06x slower  |
| pylint                     | 193 ms     | 205 ms: 1.06x slower   |
| python_startup             | 24.7 ms    | 26.4 ms: 1.07x slower  |
| async_tree_memoization     | 196 ms     | 210 ms: 1.07x slower   |
| async_generators           | 199 ms     | 213 ms: 1.07x slower   |
| sqlite_synth               | 1.56 us    | 1.68 us: 1.08x slower  |
| dulwich_log                | 39.1 ms    | 42.3 ms: 1.08x slower  |
| async_tree_io_tg           | 356 ms     | 385 ms: 1.08x slower   |
| async_tree_io              | 353 ms     | 384 ms: 1.09x slower   |
| html5lib                   | 35.5 ms    | 38.8 ms: 1.09x slower  |
| subparsers                 | 40.6 ms    | 44.5 ms: 1.10x slower  |
| async_tree_cpu_io_mixed    | 327 ms     | 359 ms: 1.10x slower   |
| async_tree_none            | 157 ms     | 174 ms: 1.10x slower   |
| pycparser                  | 642 ms     | 713 ms: 1.11x slower   |
| async_tree_none_tg         | 150 ms     | 167 ms: 1.11x slower   |
| async_tree_cpu_io_mixed_tg | 325 ms     | 363 ms: 1.12x slower   |
| sympy_integrate            | 12.0 ms    | 13.4 ms: 1.12x slower  |
| float                      | 37.1 ms    | 41.4 ms: 1.12x slower  |
| meteor_contest             | 66.6 ms    | 74.5 ms: 1.12x slower  |
| docutils                   | 1.58 sec   | 1.77 sec: 1.12x slower |
| 2to3                       | 204 ms     | 231 ms: 1.13x slower   |
| sympy_sum                  | 80.7 ms    | 91.4 ms: 1.13x slower  |
| sqlglot_v2_transpile       | 894 us     | 1.01 ms: 1.13x slower  |
| logging_format             | 5.90 us    | 6.70 us: 1.14x slower  |
| coroutines                 | 10.8 ms    | 12.3 ms: 1.14x slower  |
| sphinx                     | 615 ms     | 702 ms: 1.14x slower   |
| generators                 | 14.2 ms    | 16.3 ms: 1.14x slower  |
| sqlglot_v2_parse           | 695 us     | 798 us: 1.15x slower   |
| logging_simple             | 5.42 us    | 6.25 us: 1.15x slower  |
| sympy_str                  | 153 ms     | 177 ms: 1.15x slower   |
| go                         | 61.0 ms    | 70.4 ms: 1.16x slower  |
| many_optionals             | 659 us     | 762 us: 1.16x slower   |
| sympy_expand               | 263 ms     | 304 ms: 1.16x slower   |
| pyflate                    | 236 ms     | 274 ms: 1.16x slower   |
| regex_compile              | 70.7 ms    | 81.9 ms: 1.16x slower  |
| nbody                      | 45.7 ms    | 53.1 ms: 1.16x slower  |
| deltablue                  | 1.64 ms    | 1.91 ms: 1.16x slower  |
| raytrace                   | 145 ms     | 169 ms: 1.17x slower   |
| regex_v8                   | 13.9 ms    | 16.3 ms: 1.17x slower  |
| xml_etree_parse            | 89.4 ms    | 105 ms: 1.17x slower   |
| sqlglot_v2_normalize       | 62.6 ms    | 73.3 ms: 1.17x slower  |
| genshi_text                | 12.3 ms    | 14.5 ms: 1.17x slower  |
| typing_runtime_protocols   | 89.7 us    | 106 us: 1.18x slower   |
| xml_etree_iterparse        | 59.5 ms    | 70.4 ms: 1.18x slower  |
| sqlglot_v2_optimize        | 30.5 ms    | 36.1 ms: 1.18x slower  |
| telco                      | 4.45 ms    | 5.26 ms: 1.18x slower  |
| crypto_pyaes               | 40.4 ms    | 48.0 ms: 1.19x slower  |
| pprint_safe_repr           | 429 ms     | 510 ms: 1.19x slower   |
| bpe_tokeniser              | 2.52 sec   | 3.01 sec: 1.19x slower |
| thrift                     | 461 us     | 551 us: 1.19x slower   |
| coverage                   | 46.2 ms    | 55.4 ms: 1.20x slower  |
| nqueens                    | 49.7 ms    | 59.6 ms: 1.20x slower  |
| scimark_fft                | 140 ms     | 169 ms: 1.20x slower   |
| django_template            | 20.9 ms    | 25.2 ms: 1.20x slower  |
| chaos                      | 31.3 ms    | 37.7 ms: 1.21x slower  |
| pickle_pure_python         | 184 us     | 223 us: 1.21x slower   |
| richards                   | 25.5 ms    | 30.9 ms: 1.21x slower  |
| richards_super             | 29.4 ms    | 35.8 ms: 1.22x slower  |
| pprint_pformat             | 853 ms     | 1.04 sec: 1.22x slower |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.47 ms: 1.22x slower  |
| tomli_loads                | 1.03 sec   | 1.26 sec: 1.23x slower |
| deepcopy                   | 147 us     | 180 us: 1.23x slower   |
| fannkuch                   | 203 ms     | 250 ms: 1.23x slower   |
| scimark_monte_carlo        | 31.5 ms    | 38.9 ms: 1.24x slower  |
| spectral_norm              | 40.9 ms    | 51.1 ms: 1.25x slower  |
| deepcopy_reduce            | 1.51 us    | 1.90 us: 1.25x slower  |
| json_dumps                 | 6.19 ms    | 7.79 ms: 1.26x slower  |
| regex_effbot               | 1.45 ms    | 1.85 ms: 1.27x slower  |
| json                       | 2.95 ms    | 3.78 ms: 1.28x slower  |
| comprehensions             | 8.65 us    | 11.3 us: 1.31x slower  |
| hexiom                     | 3.00 ms    | 3.92 ms: 1.31x slower  |
| xml_etree_generate         | 49.4 ms    | 64.7 ms: 1.31x slower  |
| deepcopy_memo              | 14.7 us    | 19.3 us: 1.31x slower  |
| xml_etree_process          | 33.8 ms    | 44.7 ms: 1.32x slower  |
| scimark_sor                | 51.1 ms    | 68.6 ms: 1.34x slower  |
| unpickle_pure_python       | 110 us     | 148 us: 1.35x slower   |
| mako                       | 5.80 ms    | 7.84 ms: 1.35x slower  |
| gc_traversal               | 2.09 ms    | 2.83 ms: 1.35x slower  |
| logging_silent             | 44.1 ns    | 61.1 ns: 1.39x slower  |
| scimark_lu                 | 44.3 ms    | 64.2 ms: 1.45x slower  |
| json_loads                 | 14.8 us    | 21.9 us: 1.49x slower  |
| Geometric mean             | (ref)      | 1.17x slower           |

Benchmark hidden because not significant (3): shortest_path, regex_dna, pidigits
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.140x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown