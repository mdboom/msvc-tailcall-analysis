# Results vs. base

- fork: unknown
- ref: clang
- machine: unknown-unknown
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | clang                  |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 207 ms: 1.01x faster   |
| docutils       | 1.74 sec      | 1.56 sec: 1.12x faster |
| html5lib       | 37.2 ms       | 34.9 ms: 1.07x faster  |
| sphinx         | 666 ms        | 603 ms: 1.10x faster   |
| Geometric mean | (ref)         | 1.07x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | clang                 |
|----------------------------|:-------------:|:---------------------:|
| asyncio_websockets         | 315 ms        | 159 ms: 1.98x faster  |
| coroutines                 | 11.8 ms       | 10.7 ms: 1.10x faster |
| async_generators           | 202 ms        | 187 ms: 1.08x faster  |
| async_tree_memoization     | 202 ms        | 187 ms: 1.08x faster  |
| async_tree_io_tg           | 374 ms        | 351 ms: 1.07x faster  |
| async_tree_none_tg         | 160 ms        | 150 ms: 1.06x faster  |
| async_tree_memoization_tg  | 209 ms        | 197 ms: 1.06x faster  |
| async_tree_io              | 374 ms        | 353 ms: 1.06x faster  |
| async_tree_cpu_io_mixed    | 332 ms        | 313 ms: 1.06x faster  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 316 ms: 1.05x faster  |
| async_tree_none            | 165 ms        | 159 ms: 1.04x faster  |
| Geometric mean             | (ref)         | 1.13x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | clang                 |
|----------------|:-------------:|:---------------------:|
| float          | 40.4 ms       | 36.9 ms: 1.09x faster |
| nbody          | 53.0 ms       | 49.1 ms: 1.08x faster |
| pidigits       | 151 ms        | 145 ms: 1.04x faster  |
| Geometric mean | (ref)         | 1.07x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | clang                 |
|----------------|:-------------:|:---------------------:|
| regex_v8       | 15.3 ms       | 13.0 ms: 1.18x faster |
| regex_compile  | 79.3 ms       | 69.8 ms: 1.14x faster |
| regex_dna      | 125 ms        | 117 ms: 1.06x faster  |
| Geometric mean | (ref)         | 1.09x faster          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | clang                  |
|----------------------|:-------------:|:----------------------:|
| json_dumps           | 6.84 ms       | 5.66 ms: 1.21x faster  |
| unpickle_pure_python | 123 us        | 107 us: 1.15x faster   |
| pickle_pure_python   | 195 us        | 173 us: 1.13x faster   |
| json_loads           | 15.8 us       | 14.1 us: 1.13x faster  |
| xml_etree_process    | 37.9 ms       | 34.0 ms: 1.11x faster  |
| xml_etree_generate   | 54.3 ms       | 49.1 ms: 1.10x faster  |
| tomli_loads          | 1.18 sec      | 1.09 sec: 1.09x faster |
| xml_etree_iterparse  | 64.2 ms       | 61.5 ms: 1.04x faster  |
| xml_etree_parse      | 92.6 ms       | 89.4 ms: 1.04x faster  |
| Geometric mean       | (ref)         | 1.11x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-MostPGO-Ex | clang                 |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 19.9 ms       | 20.9 ms: 1.05x slower |
| Geometric mean         | (ref)         | 1.03x slower          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | clang                 |
|-----------------|:-------------:|:---------------------:|
| genshi_text     | 14.1 ms       | 11.9 ms: 1.18x faster |
| mako            | 6.50 ms       | 5.83 ms: 1.12x faster |
| genshi_xml      | 31.3 ms       | 29.0 ms: 1.08x faster |
| django_template | 22.9 ms       | 21.3 ms: 1.08x faster |
| Geometric mean  | (ref)         | 1.11x faster          |

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | clang                  |
|----------------------------|:-------------:|:----------------------:|
| subparsers                 | 41.2 ms       | 15.3 ms: 2.70x faster  |
| mdp                        | 1.56 sec      | 682 ms: 2.28x faster   |
| asyncio_websockets         | 315 ms        | 159 ms: 1.98x faster   |
| many_optionals             | 669 us        | 409 us: 1.64x faster   |
| logging_silent             | 53.0 ns       | 41.1 ns: 1.29x faster  |
| scimark_sor                | 63.1 ms       | 49.3 ms: 1.28x faster  |
| scimark_lu                 | 55.5 ms       | 43.5 ms: 1.28x faster  |
| scimark_monte_carlo        | 35.5 ms       | 28.6 ms: 1.24x faster  |
| deepcopy_memo              | 17.0 us       | 14.0 us: 1.22x faster  |
| json_dumps                 | 6.84 ms       | 5.66 ms: 1.21x faster  |
| k_core                     | 2.00 sec      | 1.66 sec: 1.21x faster |
| hexiom                     | 3.58 ms       | 2.98 ms: 1.20x faster  |
| genshi_text                | 14.1 ms       | 11.9 ms: 1.18x faster  |
| regex_v8                   | 15.3 ms       | 13.0 ms: 1.18x faster  |
| coverage                   | 46.2 ms       | 39.8 ms: 1.16x faster  |
| pprint_safe_repr           | 481 ms        | 415 ms: 1.16x faster   |
| pprint_pformat             | 963 ms        | 835 ms: 1.15x faster   |
| unpickle_pure_python       | 123 us        | 107 us: 1.15x faster   |
| sympy_integrate            | 12.9 ms       | 11.2 ms: 1.15x faster  |
| deltablue                  | 1.87 ms       | 1.64 ms: 1.14x faster  |
| raytrace                   | 162 ms        | 142 ms: 1.14x faster   |
| shortest_path              | 399 ms        | 351 ms: 1.14x faster   |
| regex_compile              | 79.3 ms       | 69.8 ms: 1.14x faster  |
| scimark_sparse_mat_mult    | 2.25 ms       | 1.99 ms: 1.13x faster  |
| pickle_pure_python         | 195 us        | 173 us: 1.13x faster   |
| fannkuch                   | 233 ms        | 207 ms: 1.13x faster   |
| pyflate                    | 264 ms        | 234 ms: 1.13x faster   |
| json_loads                 | 15.8 us       | 14.1 us: 1.13x faster  |
| json                       | 3.16 ms       | 2.81 ms: 1.12x faster  |
| typing_runtime_protocols   | 98.1 us       | 87.6 us: 1.12x faster  |
| docutils                   | 1.74 sec      | 1.56 sec: 1.12x faster |
| mako                       | 6.50 ms       | 5.83 ms: 1.12x faster  |
| go                         | 68.6 ms       | 61.5 ms: 1.11x faster  |
| xml_etree_process          | 37.9 ms       | 34.0 ms: 1.11x faster  |
| deepcopy_reduce            | 1.69 us       | 1.52 us: 1.11x faster  |
| comprehensions             | 9.60 us       | 8.64 us: 1.11x faster  |
| connected_components       | 366 ms        | 329 ms: 1.11x faster   |
| sympy_sum                  | 88.0 ms       | 79.2 ms: 1.11x faster  |
| generators                 | 16.3 ms       | 14.8 ms: 1.11x faster  |
| xml_etree_generate         | 54.3 ms       | 49.1 ms: 1.10x faster  |
| sphinx                     | 666 ms        | 603 ms: 1.10x faster   |
| deepcopy                   | 159 us        | 144 us: 1.10x faster   |
| coroutines                 | 11.8 ms       | 10.7 ms: 1.10x faster  |
| float                      | 40.4 ms       | 36.9 ms: 1.09x faster  |
| sympy_str                  | 163 ms        | 149 ms: 1.09x faster   |
| dulwich_log                | 41.5 ms       | 38.0 ms: 1.09x faster  |
| spectral_norm              | 46.7 ms       | 42.8 ms: 1.09x faster  |
| sympy_expand               | 279 ms        | 256 ms: 1.09x faster   |
| sqlglot_v2_parse           | 742 us        | 682 us: 1.09x faster   |
| tomli_loads                | 1.18 sec      | 1.09 sec: 1.09x faster |
| chaos                      | 34.2 ms       | 31.4 ms: 1.09x faster  |
| nqueens                    | 54.2 ms       | 49.8 ms: 1.09x faster  |
| scimark_fft                | 151 ms        | 139 ms: 1.08x faster   |
| meteor_contest             | 72.3 ms       | 66.8 ms: 1.08x faster  |
| telco                      | 4.60 ms       | 4.25 ms: 1.08x faster  |
| nbody                      | 53.0 ms       | 49.1 ms: 1.08x faster  |
| sqlglot_v2_transpile       | 943 us        | 873 us: 1.08x faster   |
| genshi_xml                 | 31.3 ms       | 29.0 ms: 1.08x faster  |
| async_generators           | 202 ms        | 187 ms: 1.08x faster   |
| async_tree_memoization     | 202 ms        | 187 ms: 1.08x faster   |
| django_template            | 22.9 ms       | 21.3 ms: 1.08x faster  |
| pylint                     | 202 ms        | 188 ms: 1.07x faster   |
| logging_format             | 6.39 us       | 5.96 us: 1.07x faster  |
| richards                   | 28.1 ms       | 26.3 ms: 1.07x faster  |
| async_tree_io_tg           | 374 ms        | 351 ms: 1.07x faster   |
| html5lib                   | 37.2 ms       | 34.9 ms: 1.07x faster  |
| regex_dna                  | 125 ms        | 117 ms: 1.06x faster   |
| pycparser                  | 688 ms        | 647 ms: 1.06x faster   |
| async_tree_none_tg         | 160 ms        | 150 ms: 1.06x faster   |
| async_tree_memoization_tg  | 209 ms        | 197 ms: 1.06x faster   |
| async_tree_io              | 374 ms        | 353 ms: 1.06x faster   |
| sqlglot_v2_optimize        | 33.0 ms       | 31.1 ms: 1.06x faster  |
| richards_super             | 32.0 ms       | 30.2 ms: 1.06x faster  |
| async_tree_cpu_io_mixed    | 332 ms        | 313 ms: 1.06x faster   |
| logging_simple             | 5.84 us       | 5.55 us: 1.05x faster  |
| bpe_tokeniser              | 2.67 sec      | 2.55 sec: 1.05x faster |
| async_tree_cpu_io_mixed_tg | 331 ms        | 316 ms: 1.05x faster   |
| crypto_pyaes               | 41.7 ms       | 39.9 ms: 1.04x faster  |
| xml_etree_iterparse        | 64.2 ms       | 61.5 ms: 1.04x faster  |
| pidigits                   | 151 ms        | 145 ms: 1.04x faster   |
| sqlglot_v2_normalize       | 66.7 ms       | 64.2 ms: 1.04x faster  |
| async_tree_none            | 165 ms        | 159 ms: 1.04x faster   |
| xml_etree_parse            | 92.6 ms       | 89.4 ms: 1.04x faster  |
| sqlite_synth               | 1.56 us       | 1.51 us: 1.03x faster  |
| 2to3                       | 209 ms        | 207 ms: 1.01x faster   |
| python_startup_no_site     | 19.9 ms       | 20.9 ms: 1.05x slower  |
| pathlib                    | 25.5 ms       | 30.7 ms: 1.20x slower  |
| gc_traversal               | 2.21 ms       | 2.76 ms: 1.25x slower  |
| Geometric mean             | (ref)         | 1.12x faster           |

Benchmark hidden because not significant (5): bench_mp_pool, python_startup, bench_thread_pool, regex_effbot, create_gc_cycles
Ignored benchmarks (1) of TC-MostPGO-Ex.json: thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown