# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.070x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 215 ms: 1.06x slower   |
| docutils       | 1.58 sec   | 1.66 sec: 1.05x slower |
| html5lib       | 35.5 ms    | 37.8 ms: 1.07x slower  |
| sphinx         | 615 ms     | 641 ms: 1.04x slower   |
| Geometric mean | (ref)      | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 327 ms     | 330 ms: 1.01x slower  |
| async_generators           | 199 ms     | 201 ms: 1.01x slower  |
| async_tree_cpu_io_mixed_tg | 325 ms     | 330 ms: 1.01x slower  |
| asyncio_websockets         | 304 ms     | 313 ms: 1.03x slower  |
| async_tree_memoization_tg  | 201 ms     | 208 ms: 1.03x slower  |
| async_tree_memoization     | 196 ms     | 205 ms: 1.04x slower  |
| async_tree_io_tg           | 356 ms     | 377 ms: 1.06x slower  |
| async_tree_none_tg         | 150 ms     | 161 ms: 1.07x slower  |
| async_tree_none            | 157 ms     | 170 ms: 1.08x slower  |
| async_tree_io              | 353 ms     | 382 ms: 1.08x slower  |
| coroutines                 | 10.8 ms    | 12.0 ms: 1.11x slower |
| Geometric mean             | (ref)      | 1.05x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| float          | 37.1 ms    | 42.0 ms: 1.13x slower |
| nbody          | 45.7 ms    | 55.6 ms: 1.22x slower |
| Geometric mean | (ref)      | 1.11x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 120 ms: 1.01x faster  |
| regex_effbot   | 1.45 ms    | 1.47 ms: 1.01x slower |
| regex_compile  | 70.7 ms    | 79.4 ms: 1.12x slower |
| Geometric mean | (ref)      | 1.04x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------------|:----------:|:----------------------:|
| json_loads           | 14.8 us    | 14.5 us: 1.02x faster  |
| xml_etree_iterparse  | 59.5 ms    | 61.2 ms: 1.03x slower  |
| json_dumps           | 6.19 ms    | 6.40 ms: 1.03x slower  |
| xml_etree_generate   | 49.4 ms    | 53.1 ms: 1.07x slower  |
| pickle_pure_python   | 184 us     | 199 us: 1.08x slower   |
| xml_etree_process    | 33.8 ms    | 36.8 ms: 1.09x slower  |
| unpickle_pure_python | 110 us     | 124 us: 1.13x slower   |
| tomli_loads          | 1.03 sec   | 1.17 sec: 1.14x slower |
| Geometric mean       | (ref)      | 1.06x slower           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TCO-PGO-Ex3           |
|-----------------|:----------:|:---------------------:|
| mako            | 5.80 ms    | 6.25 ms: 1.08x slower |
| genshi_xml      | 29.5 ms    | 32.3 ms: 1.10x slower |
| django_template | 20.9 ms    | 23.6 ms: 1.12x slower |
| genshi_text     | 12.3 ms    | 14.3 ms: 1.16x slower |
| Geometric mean  | (ref)      | 1.11x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex3 | TCO-PGO-Ex3            |
|----------------------------|:----------:|:----------------------:|
| json_loads                 | 14.8 us    | 14.5 us: 1.02x faster  |
| create_gc_cycles           | 1.26 ms    | 1.25 ms: 1.01x faster  |
| regex_dna                  | 121 ms     | 120 ms: 1.01x faster   |
| async_tree_cpu_io_mixed    | 327 ms     | 330 ms: 1.01x slower   |
| regex_effbot               | 1.45 ms    | 1.47 ms: 1.01x slower  |
| async_generators           | 199 ms     | 201 ms: 1.01x slower   |
| shortest_path              | 347 ms     | 352 ms: 1.01x slower   |
| mdp                        | 1.41 sec   | 1.43 sec: 1.01x slower |
| async_tree_cpu_io_mixed_tg | 325 ms     | 330 ms: 1.01x slower   |
| connected_components       | 320 ms     | 325 ms: 1.02x slower   |
| subparsers                 | 40.6 ms    | 41.4 ms: 1.02x slower  |
| k_core                     | 1.67 sec   | 1.70 sec: 1.02x slower |
| pathlib                    | 23.6 ms    | 24.2 ms: 1.02x slower  |
| xml_etree_iterparse        | 59.5 ms    | 61.2 ms: 1.03x slower  |
| asyncio_websockets         | 304 ms     | 313 ms: 1.03x slower   |
| json                       | 2.95 ms    | 3.04 ms: 1.03x slower  |
| coverage                   | 46.2 ms    | 47.5 ms: 1.03x slower  |
| dulwich_log                | 39.1 ms    | 40.3 ms: 1.03x slower  |
| telco                      | 4.45 ms    | 4.59 ms: 1.03x slower  |
| async_tree_memoization_tg  | 201 ms     | 208 ms: 1.03x slower   |
| json_dumps                 | 6.19 ms    | 6.40 ms: 1.03x slower  |
| many_optionals             | 659 us     | 685 us: 1.04x slower   |
| sphinx                     | 615 ms     | 641 ms: 1.04x slower   |
| pylint                     | 193 ms     | 201 ms: 1.04x slower   |
| async_tree_memoization     | 196 ms     | 205 ms: 1.04x slower   |
| docutils                   | 1.58 sec   | 1.66 sec: 1.05x slower |
| 2to3                       | 204 ms     | 215 ms: 1.06x slower   |
| sympy_sum                  | 80.7 ms    | 85.2 ms: 1.06x slower  |
| async_tree_io_tg           | 356 ms     | 377 ms: 1.06x slower   |
| thrift                     | 461 us     | 491 us: 1.06x slower   |
| meteor_contest             | 66.6 ms    | 70.9 ms: 1.06x slower  |
| html5lib                   | 35.5 ms    | 37.8 ms: 1.07x slower  |
| sympy_integrate            | 12.0 ms    | 12.8 ms: 1.07x slower  |
| async_tree_none_tg         | 150 ms     | 161 ms: 1.07x slower   |
| pycparser                  | 642 ms     | 689 ms: 1.07x slower   |
| xml_etree_generate         | 49.4 ms    | 53.1 ms: 1.07x slower  |
| sympy_expand               | 263 ms     | 283 ms: 1.08x slower   |
| mako                       | 5.80 ms    | 6.25 ms: 1.08x slower  |
| async_tree_none            | 157 ms     | 170 ms: 1.08x slower   |
| bpe_tokeniser              | 2.52 sec   | 2.72 sec: 1.08x slower |
| sqlglot_v2_optimize        | 30.5 ms    | 32.9 ms: 1.08x slower  |
| async_tree_io              | 353 ms     | 382 ms: 1.08x slower   |
| pickle_pure_python         | 184 us     | 199 us: 1.08x slower   |
| logging_simple             | 5.42 us    | 5.87 us: 1.08x slower  |
| crypto_pyaes               | 40.4 ms    | 43.9 ms: 1.09x slower  |
| logging_format             | 5.90 us    | 6.42 us: 1.09x slower  |
| typing_runtime_protocols   | 89.7 us    | 97.8 us: 1.09x slower  |
| xml_etree_process          | 33.8 ms    | 36.8 ms: 1.09x slower  |
| scimark_fft                | 140 ms     | 153 ms: 1.09x slower   |
| scimark_sparse_mat_mult    | 2.02 ms    | 2.21 ms: 1.09x slower  |
| genshi_xml                 | 29.5 ms    | 32.3 ms: 1.10x slower  |
| sqlglot_v2_normalize       | 62.6 ms    | 69.0 ms: 1.10x slower  |
| fannkuch                   | 203 ms     | 225 ms: 1.11x slower   |
| pprint_safe_repr           | 429 ms     | 474 ms: 1.11x slower   |
| deepcopy_reduce            | 1.51 us    | 1.68 us: 1.11x slower  |
| coroutines                 | 10.8 ms    | 12.0 ms: 1.11x slower  |
| nqueens                    | 49.7 ms    | 55.2 ms: 1.11x slower  |
| sqlglot_v2_transpile       | 894 us     | 993 us: 1.11x slower   |
| raytrace                   | 145 ms     | 162 ms: 1.11x slower   |
| pyflate                    | 236 ms     | 264 ms: 1.12x slower   |
| pprint_pformat             | 853 ms     | 956 ms: 1.12x slower   |
| regex_compile              | 70.7 ms    | 79.4 ms: 1.12x slower  |
| django_template            | 20.9 ms    | 23.6 ms: 1.12x slower  |
| sqlglot_v2_parse           | 695 us     | 781 us: 1.12x slower   |
| logging_silent             | 44.1 ns    | 49.7 ns: 1.13x slower  |
| sympy_str                  | 153 ms     | 173 ms: 1.13x slower   |
| comprehensions             | 8.65 us    | 9.76 us: 1.13x slower  |
| unpickle_pure_python       | 110 us     | 124 us: 1.13x slower   |
| scimark_monte_carlo        | 31.5 ms    | 35.6 ms: 1.13x slower  |
| float                      | 37.1 ms    | 42.0 ms: 1.13x slower  |
| chaos                      | 31.3 ms    | 35.4 ms: 1.13x slower  |
| scimark_lu                 | 44.3 ms    | 50.3 ms: 1.13x slower  |
| deepcopy                   | 147 us     | 167 us: 1.14x slower   |
| tomli_loads                | 1.03 sec   | 1.17 sec: 1.14x slower |
| richards_super             | 29.4 ms    | 33.7 ms: 1.14x slower  |
| deltablue                  | 1.64 ms    | 1.88 ms: 1.15x slower  |
| deepcopy_memo              | 14.7 us    | 16.8 us: 1.15x slower  |
| richards                   | 25.5 ms    | 29.4 ms: 1.15x slower  |
| generators                 | 14.2 ms    | 16.5 ms: 1.16x slower  |
| go                         | 61.0 ms    | 70.5 ms: 1.16x slower  |
| genshi_text                | 12.3 ms    | 14.3 ms: 1.16x slower  |
| hexiom                     | 3.00 ms    | 3.49 ms: 1.17x slower  |
| scimark_sor                | 51.1 ms    | 60.5 ms: 1.18x slower  |
| spectral_norm              | 40.9 ms    | 49.4 ms: 1.21x slower  |
| nbody                      | 45.7 ms    | 55.6 ms: 1.22x slower  |
| Geometric mean             | (ref)      | 1.08x slower           |

Benchmark hidden because not significant (7): python_startup_no_site, pidigits, xml_etree_parse, python_startup, sqlite_synth, gc_traversal, regex_v8

- Geometric mean (including insignificant results): 1.070x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown