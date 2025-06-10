# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 215 ms      | 204 ms: 1.06x faster   |
| docutils       | 1.66 sec    | 1.58 sec: 1.05x faster |
| html5lib       | 37.8 ms     | 35.5 ms: 1.07x faster  |
| sphinx         | 641 ms      | 615 ms: 1.04x faster   |
| Geometric mean | (ref)       | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------------------|:-----------:|:---------------------:|
| coroutines                 | 12.0 ms     | 10.8 ms: 1.11x faster |
| async_tree_io              | 382 ms      | 353 ms: 1.08x faster  |
| async_tree_none            | 170 ms      | 157 ms: 1.08x faster  |
| async_tree_none_tg         | 161 ms      | 150 ms: 1.07x faster  |
| async_tree_io_tg           | 377 ms      | 356 ms: 1.06x faster  |
| async_tree_memoization     | 205 ms      | 196 ms: 1.04x faster  |
| async_tree_memoization_tg  | 208 ms      | 201 ms: 1.03x faster  |
| asyncio_websockets         | 313 ms      | 304 ms: 1.03x faster  |
| async_tree_cpu_io_mixed_tg | 330 ms      | 325 ms: 1.01x faster  |
| async_generators           | 201 ms      | 199 ms: 1.01x faster  |
| async_tree_cpu_io_mixed    | 330 ms      | 327 ms: 1.01x faster  |
| Geometric mean             | (ref)       | 1.05x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| nbody          | 55.6 ms     | 45.7 ms: 1.22x faster |
| float          | 42.0 ms     | 37.1 ms: 1.13x faster |
| Geometric mean | (ref)       | 1.11x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 79.4 ms     | 70.7 ms: 1.12x faster |
| regex_effbot   | 1.47 ms     | 1.45 ms: 1.01x faster |
| regex_dna      | 120 ms      | 121 ms: 1.01x slower  |
| Geometric mean | (ref)       | 1.04x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------------|:-----------:|:----------------------:|
| tomli_loads          | 1.17 sec    | 1.03 sec: 1.14x faster |
| unpickle_pure_python | 124 us      | 110 us: 1.13x faster   |
| xml_etree_process    | 36.8 ms     | 33.8 ms: 1.09x faster  |
| pickle_pure_python   | 199 us      | 184 us: 1.08x faster   |
| xml_etree_generate   | 53.1 ms     | 49.4 ms: 1.07x faster  |
| json_dumps           | 6.40 ms     | 6.19 ms: 1.03x faster  |
| xml_etree_iterparse  | 61.2 ms     | 59.5 ms: 1.03x faster  |
| json_loads           | 14.5 us     | 14.8 us: 1.02x slower  |
| Geometric mean       | (ref)       | 1.06x faster           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|-----------------|:-----------:|:---------------------:|
| genshi_text     | 14.3 ms     | 12.3 ms: 1.16x faster |
| django_template | 23.6 ms     | 20.9 ms: 1.12x faster |
| genshi_xml      | 32.3 ms     | 29.5 ms: 1.10x faster |
| mako            | 6.25 ms     | 5.80 ms: 1.08x faster |
| Geometric mean  | (ref)       | 1.11x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------------------|:-----------:|:----------------------:|
| nbody                      | 55.6 ms     | 45.7 ms: 1.22x faster  |
| spectral_norm              | 49.4 ms     | 40.9 ms: 1.21x faster  |
| scimark_sor                | 60.5 ms     | 51.1 ms: 1.18x faster  |
| hexiom                     | 3.49 ms     | 3.00 ms: 1.17x faster  |
| genshi_text                | 14.3 ms     | 12.3 ms: 1.16x faster  |
| go                         | 70.5 ms     | 61.0 ms: 1.16x faster  |
| generators                 | 16.5 ms     | 14.2 ms: 1.16x faster  |
| richards                   | 29.4 ms     | 25.5 ms: 1.15x faster  |
| deepcopy_memo              | 16.8 us     | 14.7 us: 1.15x faster  |
| deltablue                  | 1.88 ms     | 1.64 ms: 1.15x faster  |
| richards_super             | 33.7 ms     | 29.4 ms: 1.14x faster  |
| tomli_loads                | 1.17 sec    | 1.03 sec: 1.14x faster |
| deepcopy                   | 167 us      | 147 us: 1.14x faster   |
| scimark_lu                 | 50.3 ms     | 44.3 ms: 1.13x faster  |
| chaos                      | 35.4 ms     | 31.3 ms: 1.13x faster  |
| float                      | 42.0 ms     | 37.1 ms: 1.13x faster  |
| scimark_monte_carlo        | 35.6 ms     | 31.5 ms: 1.13x faster  |
| unpickle_pure_python       | 124 us      | 110 us: 1.13x faster   |
| comprehensions             | 9.76 us     | 8.65 us: 1.13x faster  |
| sympy_str                  | 173 ms      | 153 ms: 1.13x faster   |
| logging_silent             | 49.7 ns     | 44.1 ns: 1.13x faster  |
| sqlglot_v2_parse           | 781 us      | 695 us: 1.12x faster   |
| django_template            | 23.6 ms     | 20.9 ms: 1.12x faster  |
| regex_compile              | 79.4 ms     | 70.7 ms: 1.12x faster  |
| pprint_pformat             | 956 ms      | 853 ms: 1.12x faster   |
| pyflate                    | 264 ms      | 236 ms: 1.12x faster   |
| raytrace                   | 162 ms      | 145 ms: 1.11x faster   |
| sqlglot_v2_transpile       | 993 us      | 894 us: 1.11x faster   |
| nqueens                    | 55.2 ms     | 49.7 ms: 1.11x faster  |
| coroutines                 | 12.0 ms     | 10.8 ms: 1.11x faster  |
| deepcopy_reduce            | 1.68 us     | 1.51 us: 1.11x faster  |
| pprint_safe_repr           | 474 ms      | 429 ms: 1.11x faster   |
| fannkuch                   | 225 ms      | 203 ms: 1.11x faster   |
| sqlglot_v2_normalize       | 69.0 ms     | 62.6 ms: 1.10x faster  |
| genshi_xml                 | 32.3 ms     | 29.5 ms: 1.10x faster  |
| scimark_sparse_mat_mult    | 2.21 ms     | 2.02 ms: 1.09x faster  |
| scimark_fft                | 153 ms      | 140 ms: 1.09x faster   |
| xml_etree_process          | 36.8 ms     | 33.8 ms: 1.09x faster  |
| typing_runtime_protocols   | 97.8 us     | 89.7 us: 1.09x faster  |
| logging_format             | 6.42 us     | 5.90 us: 1.09x faster  |
| crypto_pyaes               | 43.9 ms     | 40.4 ms: 1.09x faster  |
| logging_simple             | 5.87 us     | 5.42 us: 1.08x faster  |
| pickle_pure_python         | 199 us      | 184 us: 1.08x faster   |
| async_tree_io              | 382 ms      | 353 ms: 1.08x faster   |
| sqlglot_v2_optimize        | 32.9 ms     | 30.5 ms: 1.08x faster  |
| bpe_tokeniser              | 2.72 sec    | 2.52 sec: 1.08x faster |
| async_tree_none            | 170 ms      | 157 ms: 1.08x faster   |
| mako                       | 6.25 ms     | 5.80 ms: 1.08x faster  |
| sympy_expand               | 283 ms      | 263 ms: 1.08x faster   |
| xml_etree_generate         | 53.1 ms     | 49.4 ms: 1.07x faster  |
| pycparser                  | 689 ms      | 642 ms: 1.07x faster   |
| async_tree_none_tg         | 161 ms      | 150 ms: 1.07x faster   |
| sympy_integrate            | 12.8 ms     | 12.0 ms: 1.07x faster  |
| html5lib                   | 37.8 ms     | 35.5 ms: 1.07x faster  |
| meteor_contest             | 70.9 ms     | 66.6 ms: 1.06x faster  |
| thrift                     | 491 us      | 461 us: 1.06x faster   |
| async_tree_io_tg           | 377 ms      | 356 ms: 1.06x faster   |
| sympy_sum                  | 85.2 ms     | 80.7 ms: 1.06x faster  |
| 2to3                       | 215 ms      | 204 ms: 1.06x faster   |
| docutils                   | 1.66 sec    | 1.58 sec: 1.05x faster |
| async_tree_memoization     | 205 ms      | 196 ms: 1.04x faster   |
| pylint                     | 201 ms      | 193 ms: 1.04x faster   |
| sphinx                     | 641 ms      | 615 ms: 1.04x faster   |
| many_optionals             | 685 us      | 659 us: 1.04x faster   |
| json_dumps                 | 6.40 ms     | 6.19 ms: 1.03x faster  |
| async_tree_memoization_tg  | 208 ms      | 201 ms: 1.03x faster   |
| telco                      | 4.59 ms     | 4.45 ms: 1.03x faster  |
| dulwich_log                | 40.3 ms     | 39.1 ms: 1.03x faster  |
| coverage                   | 47.5 ms     | 46.2 ms: 1.03x faster  |
| json                       | 3.04 ms     | 2.95 ms: 1.03x faster  |
| asyncio_websockets         | 313 ms      | 304 ms: 1.03x faster   |
| xml_etree_iterparse        | 61.2 ms     | 59.5 ms: 1.03x faster  |
| pathlib                    | 24.2 ms     | 23.6 ms: 1.02x faster  |
| k_core                     | 1.70 sec    | 1.67 sec: 1.02x faster |
| subparsers                 | 41.4 ms     | 40.6 ms: 1.02x faster  |
| connected_components       | 325 ms      | 320 ms: 1.02x faster   |
| async_tree_cpu_io_mixed_tg | 330 ms      | 325 ms: 1.01x faster   |
| mdp                        | 1.43 sec    | 1.41 sec: 1.01x faster |
| shortest_path              | 352 ms      | 347 ms: 1.01x faster   |
| async_generators           | 201 ms      | 199 ms: 1.01x faster   |
| regex_effbot               | 1.47 ms     | 1.45 ms: 1.01x faster  |
| async_tree_cpu_io_mixed    | 330 ms      | 327 ms: 1.01x faster   |
| regex_dna                  | 120 ms      | 121 ms: 1.01x slower   |
| create_gc_cycles           | 1.25 ms     | 1.26 ms: 1.01x slower  |
| json_loads                 | 14.5 us     | 14.8 us: 1.02x slower  |
| Geometric mean             | (ref)       | 1.08x faster           |

Benchmark hidden because not significant (7): regex_v8, gc_traversal, sqlite_synth, python_startup, xml_etree_parse, pidigits, python_startup_no_site

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown