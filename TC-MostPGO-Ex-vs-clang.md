# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.109x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang    | TC-MostPGO-Ex          |
|----------------|:--------:|:----------------------:|
| 2to3           | 207 ms   | 209 ms: 1.01x slower   |
| docutils       | 1.56 sec | 1.74 sec: 1.12x slower |
| html5lib       | 34.9 ms  | 37.2 ms: 1.07x slower  |
| sphinx         | 603 ms   | 666 ms: 1.10x slower   |
| Geometric mean | (ref)    | 1.07x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang   | TC-MostPGO-Ex         |
|----------------------------|:-------:|:---------------------:|
| async_tree_none            | 159 ms  | 165 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms  | 331 ms: 1.05x slower  |
| async_tree_cpu_io_mixed    | 313 ms  | 332 ms: 1.06x slower  |
| async_tree_io              | 353 ms  | 374 ms: 1.06x slower  |
| async_tree_memoization_tg  | 197 ms  | 209 ms: 1.06x slower  |
| async_tree_none_tg         | 150 ms  | 160 ms: 1.06x slower  |
| async_tree_io_tg           | 351 ms  | 374 ms: 1.07x slower  |
| async_tree_memoization     | 187 ms  | 202 ms: 1.08x slower  |
| async_generators           | 187 ms  | 202 ms: 1.08x slower  |
| coroutines                 | 10.7 ms | 11.8 ms: 1.10x slower |
| asyncio_websockets         | 159 ms  | 315 ms: 1.98x slower  |
| Geometric mean             | (ref)   | 1.13x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang   | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| pidigits       | 145 ms  | 151 ms: 1.04x slower  |
| nbody          | 49.1 ms | 53.0 ms: 1.08x slower |
| float          | 36.9 ms | 40.4 ms: 1.09x slower |
| Geometric mean | (ref)   | 1.07x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang   | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| regex_dna      | 117 ms  | 125 ms: 1.06x slower  |
| regex_compile  | 69.8 ms | 79.3 ms: 1.14x slower |
| regex_v8       | 13.0 ms | 15.3 ms: 1.18x slower |
| Geometric mean | (ref)   | 1.09x slower          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang    | TC-MostPGO-Ex          |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 89.4 ms  | 92.6 ms: 1.04x slower  |
| xml_etree_iterparse  | 61.5 ms  | 64.2 ms: 1.04x slower  |
| tomli_loads          | 1.09 sec | 1.18 sec: 1.09x slower |
| xml_etree_generate   | 49.1 ms  | 54.3 ms: 1.10x slower  |
| xml_etree_process    | 34.0 ms  | 37.9 ms: 1.11x slower  |
| json_loads           | 14.1 us  | 15.8 us: 1.13x slower  |
| pickle_pure_python   | 173 us   | 195 us: 1.13x slower   |
| unpickle_pure_python | 107 us   | 123 us: 1.15x slower   |
| json_dumps           | 5.66 ms  | 6.84 ms: 1.21x slower  |
| Geometric mean       | (ref)    | 1.11x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang   | TC-MostPGO-Ex         |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.9 ms | 19.9 ms: 1.05x faster |
| Geometric mean         | (ref)   | 1.03x faster          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | clang   | TC-MostPGO-Ex         |
|-----------------|:-------:|:---------------------:|
| django_template | 21.3 ms | 22.9 ms: 1.08x slower |
| genshi_xml      | 29.0 ms | 31.3 ms: 1.08x slower |
| mako            | 5.83 ms | 6.50 ms: 1.12x slower |
| genshi_text     | 11.9 ms | 14.1 ms: 1.18x slower |
| Geometric mean  | (ref)   | 1.11x slower          |

All benchmarks:
===============

| Benchmark                  | clang    | TC-MostPGO-Ex          |
|----------------------------|:--------:|:----------------------:|
| gc_traversal               | 2.76 ms  | 2.21 ms: 1.25x faster  |
| pathlib                    | 30.7 ms  | 25.5 ms: 1.20x faster  |
| python_startup_no_site     | 20.9 ms  | 19.9 ms: 1.05x faster  |
| 2to3                       | 207 ms   | 209 ms: 1.01x slower   |
| sqlite_synth               | 1.51 us  | 1.56 us: 1.03x slower  |
| xml_etree_parse            | 89.4 ms  | 92.6 ms: 1.04x slower  |
| async_tree_none            | 159 ms   | 165 ms: 1.04x slower   |
| sqlglot_v2_normalize       | 64.2 ms  | 66.7 ms: 1.04x slower  |
| pidigits                   | 145 ms   | 151 ms: 1.04x slower   |
| xml_etree_iterparse        | 61.5 ms  | 64.2 ms: 1.04x slower  |
| crypto_pyaes               | 39.9 ms  | 41.7 ms: 1.04x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms   | 331 ms: 1.05x slower   |
| bpe_tokeniser              | 2.55 sec | 2.67 sec: 1.05x slower |
| logging_simple             | 5.55 us  | 5.84 us: 1.05x slower  |
| async_tree_cpu_io_mixed    | 313 ms   | 332 ms: 1.06x slower   |
| richards_super             | 30.2 ms  | 32.0 ms: 1.06x slower  |
| sqlglot_v2_optimize        | 31.1 ms  | 33.0 ms: 1.06x slower  |
| async_tree_io              | 353 ms   | 374 ms: 1.06x slower   |
| async_tree_memoization_tg  | 197 ms   | 209 ms: 1.06x slower   |
| async_tree_none_tg         | 150 ms   | 160 ms: 1.06x slower   |
| pycparser                  | 647 ms   | 688 ms: 1.06x slower   |
| regex_dna                  | 117 ms   | 125 ms: 1.06x slower   |
| html5lib                   | 34.9 ms  | 37.2 ms: 1.07x slower  |
| async_tree_io_tg           | 351 ms   | 374 ms: 1.07x slower   |
| richards                   | 26.3 ms  | 28.1 ms: 1.07x slower  |
| logging_format             | 5.96 us  | 6.39 us: 1.07x slower  |
| pylint                     | 188 ms   | 202 ms: 1.07x slower   |
| django_template            | 21.3 ms  | 22.9 ms: 1.08x slower  |
| async_tree_memoization     | 187 ms   | 202 ms: 1.08x slower   |
| async_generators           | 187 ms   | 202 ms: 1.08x slower   |
| genshi_xml                 | 29.0 ms  | 31.3 ms: 1.08x slower  |
| sqlglot_v2_transpile       | 873 us   | 943 us: 1.08x slower   |
| nbody                      | 49.1 ms  | 53.0 ms: 1.08x slower  |
| telco                      | 4.25 ms  | 4.60 ms: 1.08x slower  |
| meteor_contest             | 66.8 ms  | 72.3 ms: 1.08x slower  |
| scimark_fft                | 139 ms   | 151 ms: 1.08x slower   |
| nqueens                    | 49.8 ms  | 54.2 ms: 1.09x slower  |
| chaos                      | 31.4 ms  | 34.2 ms: 1.09x slower  |
| tomli_loads                | 1.09 sec | 1.18 sec: 1.09x slower |
| sqlglot_v2_parse           | 682 us   | 742 us: 1.09x slower   |
| sympy_expand               | 256 ms   | 279 ms: 1.09x slower   |
| spectral_norm              | 42.8 ms  | 46.7 ms: 1.09x slower  |
| dulwich_log                | 38.0 ms  | 41.5 ms: 1.09x slower  |
| sympy_str                  | 149 ms   | 163 ms: 1.09x slower   |
| float                      | 36.9 ms  | 40.4 ms: 1.09x slower  |
| coroutines                 | 10.7 ms  | 11.8 ms: 1.10x slower  |
| deepcopy                   | 144 us   | 159 us: 1.10x slower   |
| sphinx                     | 603 ms   | 666 ms: 1.10x slower   |
| xml_etree_generate         | 49.1 ms  | 54.3 ms: 1.10x slower  |
| generators                 | 14.8 ms  | 16.3 ms: 1.11x slower  |
| sympy_sum                  | 79.2 ms  | 88.0 ms: 1.11x slower  |
| connected_components       | 329 ms   | 366 ms: 1.11x slower   |
| comprehensions             | 8.64 us  | 9.60 us: 1.11x slower  |
| deepcopy_reduce            | 1.52 us  | 1.69 us: 1.11x slower  |
| xml_etree_process          | 34.0 ms  | 37.9 ms: 1.11x slower  |
| go                         | 61.5 ms  | 68.6 ms: 1.11x slower  |
| mako                       | 5.83 ms  | 6.50 ms: 1.12x slower  |
| docutils                   | 1.56 sec | 1.74 sec: 1.12x slower |
| typing_runtime_protocols   | 87.6 us  | 98.1 us: 1.12x slower  |
| json                       | 2.81 ms  | 3.16 ms: 1.12x slower  |
| json_loads                 | 14.1 us  | 15.8 us: 1.13x slower  |
| pyflate                    | 234 ms   | 264 ms: 1.13x slower   |
| fannkuch                   | 207 ms   | 233 ms: 1.13x slower   |
| pickle_pure_python         | 173 us   | 195 us: 1.13x slower   |
| scimark_sparse_mat_mult    | 1.99 ms  | 2.25 ms: 1.13x slower  |
| regex_compile              | 69.8 ms  | 79.3 ms: 1.14x slower  |
| shortest_path              | 351 ms   | 399 ms: 1.14x slower   |
| raytrace                   | 142 ms   | 162 ms: 1.14x slower   |
| deltablue                  | 1.64 ms  | 1.87 ms: 1.14x slower  |
| sympy_integrate            | 11.2 ms  | 12.9 ms: 1.15x slower  |
| unpickle_pure_python       | 107 us   | 123 us: 1.15x slower   |
| pprint_pformat             | 835 ms   | 963 ms: 1.15x slower   |
| pprint_safe_repr           | 415 ms   | 481 ms: 1.16x slower   |
| coverage                   | 39.8 ms  | 46.2 ms: 1.16x slower  |
| regex_v8                   | 13.0 ms  | 15.3 ms: 1.18x slower  |
| genshi_text                | 11.9 ms  | 14.1 ms: 1.18x slower  |
| hexiom                     | 2.98 ms  | 3.58 ms: 1.20x slower  |
| k_core                     | 1.66 sec | 2.00 sec: 1.21x slower |
| json_dumps                 | 5.66 ms  | 6.84 ms: 1.21x slower  |
| deepcopy_memo              | 14.0 us  | 17.0 us: 1.22x slower  |
| scimark_monte_carlo        | 28.6 ms  | 35.5 ms: 1.24x slower  |
| scimark_lu                 | 43.5 ms  | 55.5 ms: 1.28x slower  |
| scimark_sor                | 49.3 ms  | 63.1 ms: 1.28x slower  |
| logging_silent             | 41.1 ns  | 53.0 ns: 1.29x slower  |
| many_optionals             | 409 us   | 669 us: 1.64x slower   |
| asyncio_websockets         | 159 ms   | 315 ms: 1.98x slower   |
| mdp                        | 682 ms   | 1.56 sec: 2.28x slower |
| subparsers                 | 15.3 ms  | 41.2 ms: 2.70x slower  |
| Geometric mean             | (ref)    | 1.12x slower           |

Benchmark hidden because not significant (5): create_gc_cycles, regex_effbot, bench_thread_pool, python_startup, bench_mp_pool
Ignored benchmarks (1) of TC-MostPGO-Ex.json: thrift

- Geometric mean (including insignificant results): 1.109x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown