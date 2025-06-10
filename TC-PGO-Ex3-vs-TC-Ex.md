# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.164x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TC-PGO-Ex3             |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 204 ms: 1.13x faster   |
| docutils       | 1.77 sec | 1.58 sec: 1.12x faster |
| html5lib       | 38.8 ms  | 35.5 ms: 1.09x faster  |
| sphinx         | 702 ms   | 615 ms: 1.14x faster   |
| Geometric mean | (ref)    | 1.12x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TC-PGO-Ex3            |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 12.3 ms | 10.8 ms: 1.14x faster |
| async_tree_cpu_io_mixed_tg | 363 ms  | 325 ms: 1.12x faster  |
| async_tree_none_tg         | 167 ms  | 150 ms: 1.11x faster  |
| async_tree_none            | 174 ms  | 157 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 327 ms: 1.10x faster  |
| async_tree_io              | 384 ms  | 353 ms: 1.09x faster  |
| async_tree_io_tg           | 385 ms  | 356 ms: 1.08x faster  |
| async_generators           | 213 ms  | 199 ms: 1.07x faster  |
| async_tree_memoization     | 210 ms  | 196 ms: 1.07x faster  |
| async_tree_memoization_tg  | 210 ms  | 201 ms: 1.05x faster  |
| asyncio_websockets         | 312 ms  | 304 ms: 1.02x faster  |
| Geometric mean             | (ref)   | 1.09x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| nbody          | 53.1 ms | 45.7 ms: 1.16x faster |
| float          | 41.4 ms | 37.1 ms: 1.12x faster |
| Geometric mean | (ref)   | 1.09x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TC-PGO-Ex3            |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.45 ms: 1.27x faster |
| regex_v8       | 16.3 ms | 13.9 ms: 1.17x faster |
| regex_compile  | 81.9 ms | 70.7 ms: 1.16x faster |
| Geometric mean | (ref)   | 1.15x faster          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TC-PGO-Ex3             |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 14.8 us: 1.49x faster  |
| unpickle_pure_python | 148 us   | 110 us: 1.35x faster   |
| xml_etree_process    | 44.7 ms  | 33.8 ms: 1.32x faster  |
| xml_etree_generate   | 64.7 ms  | 49.4 ms: 1.31x faster  |
| json_dumps           | 7.79 ms  | 6.19 ms: 1.26x faster  |
| tomli_loads          | 1.26 sec | 1.03 sec: 1.23x faster |
| pickle_pure_python   | 223 us   | 184 us: 1.21x faster   |
| xml_etree_iterparse  | 70.4 ms  | 59.5 ms: 1.18x faster  |
| xml_etree_parse      | 105 ms   | 89.4 ms: 1.17x faster  |
| Geometric mean       | (ref)    | 1.28x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TC-PGO-Ex3            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 24.7 ms: 1.07x faster |
| python_startup_no_site | 19.4 ms | 18.7 ms: 1.04x faster |
| Geometric mean         | (ref)   | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TC-PGO-Ex3            |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 5.80 ms: 1.35x faster |
| django_template | 25.2 ms | 20.9 ms: 1.20x faster |
| genshi_text     | 14.5 ms | 12.3 ms: 1.17x faster |
| genshi_xml      | 31.3 ms | 29.5 ms: 1.06x faster |
| Geometric mean  | (ref)   | 1.19x faster          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TC-PGO-Ex3             |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 14.8 us: 1.49x faster  |
| scimark_lu                 | 64.2 ms  | 44.3 ms: 1.45x faster  |
| logging_silent             | 61.1 ns  | 44.1 ns: 1.39x faster  |
| gc_traversal               | 2.83 ms  | 2.09 ms: 1.35x faster  |
| mako                       | 7.84 ms  | 5.80 ms: 1.35x faster  |
| unpickle_pure_python       | 148 us   | 110 us: 1.35x faster   |
| scimark_sor                | 68.6 ms  | 51.1 ms: 1.34x faster  |
| xml_etree_process          | 44.7 ms  | 33.8 ms: 1.32x faster  |
| deepcopy_memo              | 19.3 us  | 14.7 us: 1.31x faster  |
| xml_etree_generate         | 64.7 ms  | 49.4 ms: 1.31x faster  |
| hexiom                     | 3.92 ms  | 3.00 ms: 1.31x faster  |
| comprehensions             | 11.3 us  | 8.65 us: 1.31x faster  |
| json                       | 3.78 ms  | 2.95 ms: 1.28x faster  |
| regex_effbot               | 1.85 ms  | 1.45 ms: 1.27x faster  |
| json_dumps                 | 7.79 ms  | 6.19 ms: 1.26x faster  |
| deepcopy_reduce            | 1.90 us  | 1.51 us: 1.25x faster  |
| spectral_norm              | 51.1 ms  | 40.9 ms: 1.25x faster  |
| scimark_monte_carlo        | 38.9 ms  | 31.5 ms: 1.24x faster  |
| fannkuch                   | 250 ms   | 203 ms: 1.23x faster   |
| deepcopy                   | 180 us   | 147 us: 1.23x faster   |
| tomli_loads                | 1.26 sec | 1.03 sec: 1.23x faster |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.02 ms: 1.22x faster  |
| pprint_pformat             | 1.04 sec | 853 ms: 1.22x faster   |
| richards_super             | 35.8 ms  | 29.4 ms: 1.22x faster  |
| richards                   | 30.9 ms  | 25.5 ms: 1.21x faster  |
| pickle_pure_python         | 223 us   | 184 us: 1.21x faster   |
| chaos                      | 37.7 ms  | 31.3 ms: 1.21x faster  |
| django_template            | 25.2 ms  | 20.9 ms: 1.20x faster  |
| scimark_fft                | 169 ms   | 140 ms: 1.20x faster   |
| nqueens                    | 59.6 ms  | 49.7 ms: 1.20x faster  |
| coverage                   | 55.4 ms  | 46.2 ms: 1.20x faster  |
| thrift                     | 551 us   | 461 us: 1.19x faster   |
| bpe_tokeniser              | 3.01 sec | 2.52 sec: 1.19x faster |
| pprint_safe_repr           | 510 ms   | 429 ms: 1.19x faster   |
| crypto_pyaes               | 48.0 ms  | 40.4 ms: 1.19x faster  |
| telco                      | 5.26 ms  | 4.45 ms: 1.18x faster  |
| sqlglot_v2_optimize        | 36.1 ms  | 30.5 ms: 1.18x faster  |
| xml_etree_iterparse        | 70.4 ms  | 59.5 ms: 1.18x faster  |
| typing_runtime_protocols   | 106 us   | 89.7 us: 1.18x faster  |
| genshi_text                | 14.5 ms  | 12.3 ms: 1.17x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 62.6 ms: 1.17x faster  |
| xml_etree_parse            | 105 ms   | 89.4 ms: 1.17x faster  |
| regex_v8                   | 16.3 ms  | 13.9 ms: 1.17x faster  |
| raytrace                   | 169 ms   | 145 ms: 1.17x faster   |
| deltablue                  | 1.91 ms  | 1.64 ms: 1.16x faster  |
| nbody                      | 53.1 ms  | 45.7 ms: 1.16x faster  |
| regex_compile              | 81.9 ms  | 70.7 ms: 1.16x faster  |
| pyflate                    | 274 ms   | 236 ms: 1.16x faster   |
| sympy_expand               | 304 ms   | 263 ms: 1.16x faster   |
| many_optionals             | 762 us   | 659 us: 1.16x faster   |
| go                         | 70.4 ms  | 61.0 ms: 1.16x faster  |
| sympy_str                  | 177 ms   | 153 ms: 1.15x faster   |
| logging_simple             | 6.25 us  | 5.42 us: 1.15x faster  |
| sqlglot_v2_parse           | 798 us   | 695 us: 1.15x faster   |
| generators                 | 16.3 ms  | 14.2 ms: 1.14x faster  |
| sphinx                     | 702 ms   | 615 ms: 1.14x faster   |
| coroutines                 | 12.3 ms  | 10.8 ms: 1.14x faster  |
| logging_format             | 6.70 us  | 5.90 us: 1.14x faster  |
| sqlglot_v2_transpile       | 1.01 ms  | 894 us: 1.13x faster   |
| sympy_sum                  | 91.4 ms  | 80.7 ms: 1.13x faster  |
| 2to3                       | 231 ms   | 204 ms: 1.13x faster   |
| docutils                   | 1.77 sec | 1.58 sec: 1.12x faster |
| meteor_contest             | 74.5 ms  | 66.6 ms: 1.12x faster  |
| float                      | 41.4 ms  | 37.1 ms: 1.12x faster  |
| sympy_integrate            | 13.4 ms  | 12.0 ms: 1.12x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms   | 325 ms: 1.12x faster   |
| async_tree_none_tg         | 167 ms   | 150 ms: 1.11x faster   |
| pycparser                  | 713 ms   | 642 ms: 1.11x faster   |
| async_tree_none            | 174 ms   | 157 ms: 1.10x faster   |
| async_tree_cpu_io_mixed    | 359 ms   | 327 ms: 1.10x faster   |
| subparsers                 | 44.5 ms  | 40.6 ms: 1.10x faster  |
| html5lib                   | 38.8 ms  | 35.5 ms: 1.09x faster  |
| async_tree_io              | 384 ms   | 353 ms: 1.09x faster   |
| async_tree_io_tg           | 385 ms   | 356 ms: 1.08x faster   |
| dulwich_log                | 42.3 ms  | 39.1 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us  | 1.56 us: 1.08x faster  |
| async_generators           | 213 ms   | 199 ms: 1.07x faster   |
| async_tree_memoization     | 210 ms   | 196 ms: 1.07x faster   |
| python_startup             | 26.4 ms  | 24.7 ms: 1.07x faster  |
| pylint                     | 205 ms   | 193 ms: 1.06x faster   |
| pathlib                    | 25.1 ms  | 23.6 ms: 1.06x faster  |
| genshi_xml                 | 31.3 ms  | 29.5 ms: 1.06x faster  |
| create_gc_cycles           | 1.34 ms  | 1.26 ms: 1.06x faster  |
| async_tree_memoization_tg  | 210 ms   | 201 ms: 1.05x faster   |
| python_startup_no_site     | 19.4 ms  | 18.7 ms: 1.04x faster  |
| mdp                        | 1.44 sec | 1.41 sec: 1.03x faster |
| asyncio_websockets         | 312 ms   | 304 ms: 1.02x faster   |
| k_core                     | 1.71 sec | 1.67 sec: 1.02x faster |
| connected_components       | 311 ms   | 320 ms: 1.03x slower   |
| Geometric mean             | (ref)    | 1.17x faster           |

Benchmark hidden because not significant (3): pidigits, regex_dna, shortest_path
Ignored benchmarks (2) of TC-Ex.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.164x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown