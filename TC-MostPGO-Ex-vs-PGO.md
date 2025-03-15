# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | TC-MostPGO-Ex          |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 209 ms: 1.09x faster   |
| docutils       | 1.68 sec | 1.74 sec: 1.04x slower |
| html5lib       | 40.8 ms  | 37.2 ms: 1.10x faster  |
| Geometric mean | (ref)    | 1.03x faster           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | TC-MostPGO-Ex         |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 13.5 ms | 11.8 ms: 1.14x faster |
| async_tree_none            | 187 ms  | 165 ms: 1.13x faster  |
| async_tree_io              | 423 ms  | 374 ms: 1.13x faster  |
| async_generators           | 226 ms  | 202 ms: 1.12x faster  |
| async_tree_memoization     | 224 ms  | 202 ms: 1.11x faster  |
| async_tree_none_tg         | 176 ms  | 160 ms: 1.10x faster  |
| async_tree_io_tg           | 410 ms  | 374 ms: 1.10x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 331 ms: 1.04x faster  |
| async_tree_memoization_tg  | 216 ms  | 209 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 332 ms: 1.02x faster  |
| asyncio_websockets         | 318 ms  | 315 ms: 1.01x faster  |
| Geometric mean             | (ref)   | 1.08x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 53.0 ms: 1.40x faster |
| float          | 47.8 ms | 40.4 ms: 1.18x faster |
| pidigits       | 152 ms  | 151 ms: 1.01x faster  |
| Geometric mean | (ref)   | 1.19x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 79.3 ms: 1.11x faster |
| regex_effbot   | 1.42 ms | 1.53 ms: 1.07x slower |
| regex_dna      | 112 ms  | 125 ms: 1.11x slower  |
| regex_v8       | 13.5 ms | 15.3 ms: 1.13x slower |
| Geometric mean | (ref)   | 1.05x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | TC-MostPGO-Ex          |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 123 us: 1.26x faster   |
| tomli_loads          | 1.47 sec | 1.18 sec: 1.24x faster |
| pickle_pure_python   | 237 us   | 195 us: 1.21x faster   |
| xml_etree_process    | 41.5 ms  | 37.9 ms: 1.10x faster  |
| xml_etree_generate   | 58.7 ms  | 54.3 ms: 1.08x faster  |
| json_dumps           | 7.05 ms  | 6.84 ms: 1.03x faster  |
| xml_etree_parse      | 91.2 ms  | 92.6 ms: 1.02x slower  |
| json_loads           | 14.7 us  | 15.8 us: 1.08x slower  |
| Geometric mean       | (ref)    | 1.09x faster           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | PGO     | TC-MostPGO-Ex         |
|----------------|:-------:|:---------------------:|
| python_startup | 26.1 ms | 26.4 ms: 1.01x slower |
| Geometric mean | (ref)   | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | TC-MostPGO-Ex         |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 14.1 ms: 1.17x faster |
| genshi_xml      | 36.3 ms | 31.3 ms: 1.16x faster |
| django_template | 25.1 ms | 22.9 ms: 1.09x faster |
| mako            | 6.86 ms | 6.50 ms: 1.05x faster |
| Geometric mean  | (ref)   | 1.12x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | TC-MostPGO-Ex          |
|----------------------------|:--------:|:----------------------:|
| scimark_sor                | 91.0 ms  | 63.1 ms: 1.44x faster  |
| nbody                      | 74.1 ms  | 53.0 ms: 1.40x faster  |
| scimark_monte_carlo        | 47.1 ms  | 35.5 ms: 1.33x faster  |
| spectral_norm              | 61.5 ms  | 46.7 ms: 1.32x faster  |
| go                         | 88.6 ms  | 68.6 ms: 1.29x faster  |
| chaos                      | 43.6 ms  | 34.2 ms: 1.28x faster  |
| scimark_fft                | 192 ms   | 151 ms: 1.27x faster   |
| fannkuch                   | 296 ms   | 233 ms: 1.27x faster   |
| unpickle_pure_python       | 155 us   | 123 us: 1.26x faster   |
| pathlib                    | 32.1 ms  | 25.5 ms: 1.26x faster  |
| tomli_loads                | 1.47 sec | 1.18 sec: 1.24x faster |
| deepcopy_memo              | 21.0 us  | 17.0 us: 1.24x faster  |
| logging_silent             | 65.2 ns  | 53.0 ns: 1.23x faster  |
| deltablue                  | 2.29 ms  | 1.87 ms: 1.22x faster  |
| hexiom                     | 4.38 ms  | 3.58 ms: 1.22x faster  |
| pickle_pure_python         | 237 us   | 195 us: 1.21x faster   |
| scimark_sparse_mat_mult    | 2.72 ms  | 2.25 ms: 1.21x faster  |
| scimark_lu                 | 66.9 ms  | 55.5 ms: 1.20x faster  |
| sqlglot_v2_parse           | 892 us   | 742 us: 1.20x faster   |
| crypto_pyaes               | 50.0 ms  | 41.7 ms: 1.20x faster  |
| deepcopy                   | 190 us   | 159 us: 1.19x faster   |
| pyflate                    | 315 ms   | 264 ms: 1.19x faster   |
| float                      | 47.8 ms  | 40.4 ms: 1.18x faster  |
| generators                 | 19.3 ms  | 16.3 ms: 1.18x faster  |
| comprehensions             | 11.3 us  | 9.60 us: 1.18x faster  |
| raytrace                   | 191 ms   | 162 ms: 1.18x faster   |
| nqueens                    | 63.6 ms  | 54.2 ms: 1.17x faster  |
| genshi_text                | 16.5 ms  | 14.1 ms: 1.17x faster  |
| pprint_pformat             | 1.13 sec | 963 ms: 1.17x faster   |
| sqlglot_v2_transpile       | 1.10 ms  | 943 us: 1.17x faster   |
| pprint_safe_repr           | 558 ms   | 481 ms: 1.16x faster   |
| genshi_xml                 | 36.3 ms  | 31.3 ms: 1.16x faster  |
| deepcopy_reduce            | 1.94 us  | 1.69 us: 1.15x faster  |
| coroutines                 | 13.5 ms  | 11.8 ms: 1.14x faster  |
| async_tree_none            | 187 ms   | 165 ms: 1.13x faster   |
| async_tree_io              | 423 ms   | 374 ms: 1.13x faster   |
| async_generators           | 226 ms   | 202 ms: 1.12x faster   |
| logging_simple             | 6.53 us  | 5.84 us: 1.12x faster  |
| async_tree_memoization     | 224 ms   | 202 ms: 1.11x faster   |
| regex_compile              | 88.2 ms  | 79.3 ms: 1.11x faster  |
| bpe_tokeniser              | 2.96 sec | 2.67 sec: 1.11x faster |
| sqlglot_v2_normalize       | 73.6 ms  | 66.7 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms   | 160 ms: 1.10x faster   |
| logging_format             | 7.03 us  | 6.39 us: 1.10x faster  |
| xml_etree_process          | 41.5 ms  | 37.9 ms: 1.10x faster  |
| async_tree_io_tg           | 410 ms   | 374 ms: 1.10x faster   |
| richards_super             | 35.1 ms  | 32.0 ms: 1.10x faster  |
| html5lib                   | 40.8 ms  | 37.2 ms: 1.10x faster  |
| django_template            | 25.1 ms  | 22.9 ms: 1.09x faster  |
| richards                   | 30.7 ms  | 28.1 ms: 1.09x faster  |
| 2to3                       | 227 ms   | 209 ms: 1.09x faster   |
| sympy_expand               | 302 ms   | 279 ms: 1.08x faster   |
| sympy_str                  | 176 ms   | 163 ms: 1.08x faster   |
| typing_runtime_protocols   | 106 us   | 98.1 us: 1.08x faster  |
| xml_etree_generate         | 58.7 ms  | 54.3 ms: 1.08x faster  |
| pycparser                  | 738 ms   | 688 ms: 1.07x faster   |
| telco                      | 4.89 ms  | 4.60 ms: 1.06x faster  |
| meteor_contest             | 76.9 ms  | 72.3 ms: 1.06x faster  |
| sqlglot_v2_optimize        | 35.0 ms  | 33.0 ms: 1.06x faster  |
| mako                       | 6.86 ms  | 6.50 ms: 1.05x faster  |
| bench_thread_pool          | 864 us   | 819 us: 1.05x faster   |
| mdp                        | 1.64 sec | 1.56 sec: 1.05x faster |
| sympy_integrate            | 13.5 ms  | 12.9 ms: 1.05x faster  |
| dulwich_log                | 43.4 ms  | 41.5 ms: 1.05x faster  |
| thrift                     | 507 us   | 487 us: 1.04x faster   |
| async_tree_cpu_io_mixed_tg | 343 ms   | 331 ms: 1.04x faster   |
| json_dumps                 | 7.05 ms  | 6.84 ms: 1.03x faster  |
| async_tree_memoization_tg  | 216 ms   | 209 ms: 1.03x faster   |
| sympy_sum                  | 90.5 ms  | 88.0 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 339 ms   | 332 ms: 1.02x faster   |
| sqlite_synth               | 1.59 us  | 1.56 us: 1.02x faster  |
| coverage                   | 46.8 ms  | 46.2 ms: 1.01x faster  |
| asyncio_websockets         | 318 ms   | 315 ms: 1.01x faster   |
| pidigits                   | 152 ms   | 151 ms: 1.01x faster   |
| python_startup             | 26.1 ms  | 26.4 ms: 1.01x slower  |
| xml_etree_parse            | 91.2 ms  | 92.6 ms: 1.02x slower  |
| docutils                   | 1.68 sec | 1.74 sec: 1.04x slower |
| regex_effbot               | 1.42 ms  | 1.53 ms: 1.07x slower  |
| gc_traversal               | 2.06 ms  | 2.21 ms: 1.07x slower  |
| json_loads                 | 14.7 us  | 15.8 us: 1.08x slower  |
| create_gc_cycles           | 1.25 ms  | 1.35 ms: 1.08x slower  |
| shortest_path              | 359 ms   | 399 ms: 1.11x slower   |
| regex_dna                  | 112 ms   | 125 ms: 1.11x slower   |
| connected_components       | 329 ms   | 366 ms: 1.11x slower   |
| regex_v8                   | 13.5 ms  | 15.3 ms: 1.13x slower  |
| k_core                     | 1.73 sec | 2.00 sec: 1.15x slower |
| many_optionals             | 438 us   | 669 us: 1.53x slower   |
| subparsers                 | 16.1 ms  | 41.2 ms: 2.56x slower  |
| Geometric mean             | (ref)    | 1.08x faster           |

Benchmark hidden because not significant (6): bench_mp_pool, python_startup_no_site, pylint, json, xml_etree_iterparse, sphinx

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown