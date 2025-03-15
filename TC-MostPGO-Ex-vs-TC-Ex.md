# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TC-MostPGO-Ex          |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 209 ms: 1.11x faster   |
| docutils       | 1.77 sec | 1.74 sec: 1.02x faster |
| html5lib       | 38.8 ms  | 37.2 ms: 1.04x faster  |
| sphinx         | 702 ms   | 666 ms: 1.05x faster   |
| Geometric mean | (ref)    | 1.05x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TC-MostPGO-Ex         |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed_tg | 363 ms  | 331 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 332 ms: 1.08x faster  |
| async_generators           | 213 ms  | 202 ms: 1.06x faster  |
| async_tree_none            | 174 ms  | 165 ms: 1.05x faster  |
| async_tree_none_tg         | 167 ms  | 160 ms: 1.05x faster  |
| async_tree_memoization     | 210 ms  | 202 ms: 1.04x faster  |
| coroutines                 | 12.3 ms | 11.8 ms: 1.04x faster |
| async_tree_io_tg           | 385 ms  | 374 ms: 1.03x faster  |
| async_tree_io              | 384 ms  | 374 ms: 1.03x faster  |
| Geometric mean             | (ref)   | 1.04x faster          |

Benchmark hidden because not significant (2): async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| float          | 41.4 ms | 40.4 ms: 1.03x faster |
| pidigits       | 146 ms  | 151 ms: 1.04x slower  |
| Geometric mean | (ref)   | 1.00x slower          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.53 ms: 1.21x faster |
| regex_v8       | 16.3 ms | 15.3 ms: 1.07x faster |
| regex_compile  | 81.9 ms | 79.3 ms: 1.03x faster |
| regex_dna      | 121 ms  | 125 ms: 1.04x slower  |
| Geometric mean | (ref)   | 1.06x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TC-MostPGO-Ex          |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 15.8 us: 1.38x faster  |
| unpickle_pure_python | 148 us   | 123 us: 1.20x faster   |
| xml_etree_generate   | 64.7 ms  | 54.3 ms: 1.19x faster  |
| xml_etree_process    | 44.7 ms  | 37.9 ms: 1.18x faster  |
| pickle_pure_python   | 223 us   | 195 us: 1.14x faster   |
| json_dumps           | 7.79 ms  | 6.84 ms: 1.14x faster  |
| xml_etree_parse      | 105 ms   | 92.6 ms: 1.13x faster  |
| xml_etree_iterparse  | 70.4 ms  | 64.2 ms: 1.10x faster  |
| tomli_loads          | 1.26 sec | 1.18 sec: 1.06x faster |
| Geometric mean       | (ref)    | 1.17x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TC-MostPGO-Ex         |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 19.4 ms | 19.9 ms: 1.02x slower |
| Geometric mean         | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TC-MostPGO-Ex         |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 6.50 ms: 1.21x faster |
| django_template | 25.2 ms | 22.9 ms: 1.10x faster |
| genshi_text     | 14.5 ms | 14.1 ms: 1.03x faster |
| Geometric mean  | (ref)   | 1.08x faster          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TC-MostPGO-Ex          |
|----------------------------|:--------:|:----------------------:|
| json_loads                 | 21.9 us  | 15.8 us: 1.38x faster  |
| gc_traversal               | 2.83 ms  | 2.21 ms: 1.28x faster  |
| regex_effbot               | 1.85 ms  | 1.53 ms: 1.21x faster  |
| mako                       | 7.84 ms  | 6.50 ms: 1.21x faster  |
| unpickle_pure_python       | 148 us   | 123 us: 1.20x faster   |
| coverage                   | 55.4 ms  | 46.2 ms: 1.20x faster  |
| json                       | 3.78 ms  | 3.16 ms: 1.20x faster  |
| xml_etree_generate         | 64.7 ms  | 54.3 ms: 1.19x faster  |
| xml_etree_process          | 44.7 ms  | 37.9 ms: 1.18x faster  |
| comprehensions             | 11.3 us  | 9.60 us: 1.18x faster  |
| scimark_lu                 | 64.2 ms  | 55.5 ms: 1.16x faster  |
| logging_silent             | 61.1 ns  | 53.0 ns: 1.15x faster  |
| crypto_pyaes               | 48.0 ms  | 41.7 ms: 1.15x faster  |
| telco                      | 5.26 ms  | 4.60 ms: 1.14x faster  |
| pickle_pure_python         | 223 us   | 195 us: 1.14x faster   |
| json_dumps                 | 7.79 ms  | 6.84 ms: 1.14x faster  |
| many_optionals             | 762 us   | 669 us: 1.14x faster   |
| deepcopy                   | 180 us   | 159 us: 1.14x faster   |
| thrift                     | 551 us   | 487 us: 1.13x faster   |
| deepcopy_memo              | 19.3 us  | 17.0 us: 1.13x faster  |
| xml_etree_parse            | 105 ms   | 92.6 ms: 1.13x faster  |
| bpe_tokeniser              | 3.01 sec | 2.67 sec: 1.13x faster |
| deepcopy_reduce            | 1.90 us  | 1.69 us: 1.12x faster  |
| richards_super             | 35.8 ms  | 32.0 ms: 1.12x faster  |
| scimark_fft                | 169 ms   | 151 ms: 1.12x faster   |
| 2to3                       | 231 ms   | 209 ms: 1.11x faster   |
| chaos                      | 37.7 ms  | 34.2 ms: 1.10x faster  |
| nqueens                    | 59.6 ms  | 54.2 ms: 1.10x faster  |
| sqlglot_v2_normalize       | 73.3 ms  | 66.7 ms: 1.10x faster  |
| django_template            | 25.2 ms  | 22.9 ms: 1.10x faster  |
| async_tree_cpu_io_mixed_tg | 363 ms   | 331 ms: 1.10x faster   |
| richards                   | 30.9 ms  | 28.1 ms: 1.10x faster  |
| scimark_sparse_mat_mult    | 2.47 ms  | 2.25 ms: 1.10x faster  |
| xml_etree_iterparse        | 70.4 ms  | 64.2 ms: 1.10x faster  |
| scimark_monte_carlo        | 38.9 ms  | 35.5 ms: 1.10x faster  |
| hexiom                     | 3.92 ms  | 3.58 ms: 1.09x faster  |
| sqlglot_v2_optimize        | 36.1 ms  | 33.0 ms: 1.09x faster  |
| spectral_norm              | 51.1 ms  | 46.7 ms: 1.09x faster  |
| sympy_expand               | 304 ms   | 279 ms: 1.09x faster   |
| sympy_str                  | 177 ms   | 163 ms: 1.09x faster   |
| scimark_sor                | 68.6 ms  | 63.1 ms: 1.09x faster  |
| async_tree_cpu_io_mixed    | 359 ms   | 332 ms: 1.08x faster   |
| typing_runtime_protocols   | 106 us   | 98.1 us: 1.08x faster  |
| subparsers                 | 44.5 ms  | 41.2 ms: 1.08x faster  |
| pprint_pformat             | 1.04 sec | 963 ms: 1.08x faster   |
| sqlglot_v2_parse           | 798 us   | 742 us: 1.07x faster   |
| sqlglot_v2_transpile       | 1.01 ms  | 943 us: 1.07x faster   |
| fannkuch                   | 250 ms   | 233 ms: 1.07x faster   |
| sqlite_synth               | 1.68 us  | 1.56 us: 1.07x faster  |
| logging_simple             | 6.25 us  | 5.84 us: 1.07x faster  |
| bench_thread_pool          | 876 us   | 819 us: 1.07x faster   |
| regex_v8                   | 16.3 ms  | 15.3 ms: 1.07x faster  |
| tomli_loads                | 1.26 sec | 1.18 sec: 1.06x faster |
| pprint_safe_repr           | 510 ms   | 481 ms: 1.06x faster   |
| async_generators           | 213 ms   | 202 ms: 1.06x faster   |
| bench_mp_pool              | 93.6 ms  | 88.6 ms: 1.06x faster  |
| async_tree_none            | 174 ms   | 165 ms: 1.05x faster   |
| sphinx                     | 702 ms   | 666 ms: 1.05x faster   |
| logging_format             | 6.70 us  | 6.39 us: 1.05x faster  |
| raytrace                   | 169 ms   | 162 ms: 1.05x faster   |
| async_tree_none_tg         | 167 ms   | 160 ms: 1.05x faster   |
| html5lib                   | 38.8 ms  | 37.2 ms: 1.04x faster  |
| async_tree_memoization     | 210 ms   | 202 ms: 1.04x faster   |
| sympy_integrate            | 13.4 ms  | 12.9 ms: 1.04x faster  |
| sympy_sum                  | 91.4 ms  | 88.0 ms: 1.04x faster  |
| coroutines                 | 12.3 ms  | 11.8 ms: 1.04x faster  |
| pyflate                    | 274 ms   | 264 ms: 1.04x faster   |
| pycparser                  | 713 ms   | 688 ms: 1.04x faster   |
| regex_compile              | 81.9 ms  | 79.3 ms: 1.03x faster  |
| async_tree_io_tg           | 385 ms   | 374 ms: 1.03x faster   |
| meteor_contest             | 74.5 ms  | 72.3 ms: 1.03x faster  |
| genshi_text                | 14.5 ms  | 14.1 ms: 1.03x faster  |
| float                      | 41.4 ms  | 40.4 ms: 1.03x faster  |
| go                         | 70.4 ms  | 68.6 ms: 1.03x faster  |
| async_tree_io              | 384 ms   | 374 ms: 1.03x faster   |
| deltablue                  | 1.91 ms  | 1.87 ms: 1.02x faster  |
| dulwich_log                | 42.3 ms  | 41.5 ms: 1.02x faster  |
| docutils                   | 1.77 sec | 1.74 sec: 1.02x faster |
| pathlib                    | 25.1 ms  | 25.5 ms: 1.01x slower  |
| python_startup_no_site     | 19.4 ms  | 19.9 ms: 1.02x slower  |
| regex_dna                  | 121 ms   | 125 ms: 1.04x slower   |
| pidigits                   | 146 ms   | 151 ms: 1.04x slower   |
| mdp                        | 1.44 sec | 1.56 sec: 1.08x slower |
| shortest_path              | 347 ms   | 399 ms: 1.15x slower   |
| k_core                     | 1.71 sec | 2.00 sec: 1.17x slower |
| connected_components       | 311 ms   | 366 ms: 1.18x slower   |
| Geometric mean             | (ref)    | 1.07x faster           |

Benchmark hidden because not significant (8): pylint, async_tree_memoization_tg, python_startup, nbody, genshi_xml, generators, create_gc_cycles, asyncio_websockets

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown