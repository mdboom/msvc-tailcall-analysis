# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.067x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | TC-Ex                  |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 231 ms: 1.11x slower   |
| docutils       | 1.74 sec      | 1.77 sec: 1.02x slower |
| html5lib       | 37.2 ms       | 38.8 ms: 1.04x slower  |
| sphinx         | 666 ms        | 702 ms: 1.05x slower   |
| Geometric mean | (ref)         | 1.05x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | TC-Ex                 |
|----------------------------|:-------------:|:---------------------:|
| async_tree_io              | 374 ms        | 384 ms: 1.03x slower  |
| async_tree_io_tg           | 374 ms        | 385 ms: 1.03x slower  |
| coroutines                 | 11.8 ms       | 12.3 ms: 1.04x slower |
| async_tree_memoization     | 202 ms        | 210 ms: 1.04x slower  |
| async_tree_none_tg         | 160 ms        | 167 ms: 1.05x slower  |
| async_tree_none            | 165 ms        | 174 ms: 1.05x slower  |
| async_generators           | 202 ms        | 213 ms: 1.06x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 359 ms: 1.08x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 363 ms: 1.10x slower  |
| Geometric mean             | (ref)         | 1.04x slower          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | TC-Ex                 |
|----------------|:-------------:|:---------------------:|
| pidigits       | 151 ms        | 146 ms: 1.04x faster  |
| float          | 40.4 ms       | 41.4 ms: 1.03x slower |
| Geometric mean | (ref)         | 1.00x faster          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | TC-Ex                 |
|----------------|:-------------:|:---------------------:|
| regex_dna      | 125 ms        | 121 ms: 1.04x faster  |
| regex_compile  | 79.3 ms       | 81.9 ms: 1.03x slower |
| regex_v8       | 15.3 ms       | 16.3 ms: 1.07x slower |
| regex_effbot   | 1.53 ms       | 1.85 ms: 1.21x slower |
| Geometric mean | (ref)         | 1.06x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | TC-Ex                  |
|----------------------|:-------------:|:----------------------:|
| tomli_loads          | 1.18 sec      | 1.26 sec: 1.06x slower |
| xml_etree_iterparse  | 64.2 ms       | 70.4 ms: 1.10x slower  |
| xml_etree_parse      | 92.6 ms       | 105 ms: 1.13x slower   |
| json_dumps           | 6.84 ms       | 7.79 ms: 1.14x slower  |
| pickle_pure_python   | 195 us        | 223 us: 1.14x slower   |
| xml_etree_process    | 37.9 ms       | 44.7 ms: 1.18x slower  |
| xml_etree_generate   | 54.3 ms       | 64.7 ms: 1.19x slower  |
| unpickle_pure_python | 123 us        | 148 us: 1.20x slower   |
| json_loads           | 15.8 us       | 21.9 us: 1.38x slower  |
| Geometric mean       | (ref)         | 1.17x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-MostPGO-Ex | TC-Ex                 |
|------------------------|:-------------:|:---------------------:|
| python_startup_no_site | 19.9 ms       | 19.4 ms: 1.02x faster |
| Geometric mean         | (ref)         | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | TC-Ex                 |
|-----------------|:-------------:|:---------------------:|
| genshi_text     | 14.1 ms       | 14.5 ms: 1.03x slower |
| django_template | 22.9 ms       | 25.2 ms: 1.10x slower |
| mako            | 6.50 ms       | 7.84 ms: 1.21x slower |
| Geometric mean  | (ref)         | 1.08x slower          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | TC-Ex                  |
|----------------------------|:-------------:|:----------------------:|
| connected_components       | 366 ms        | 311 ms: 1.18x faster   |
| k_core                     | 2.00 sec      | 1.71 sec: 1.17x faster |
| shortest_path              | 399 ms        | 347 ms: 1.15x faster   |
| mdp                        | 1.56 sec      | 1.44 sec: 1.08x faster |
| pidigits                   | 151 ms        | 146 ms: 1.04x faster   |
| regex_dna                  | 125 ms        | 121 ms: 1.04x faster   |
| python_startup_no_site     | 19.9 ms       | 19.4 ms: 1.02x faster  |
| pathlib                    | 25.5 ms       | 25.1 ms: 1.01x faster  |
| docutils                   | 1.74 sec      | 1.77 sec: 1.02x slower |
| dulwich_log                | 41.5 ms       | 42.3 ms: 1.02x slower  |
| deltablue                  | 1.87 ms       | 1.91 ms: 1.02x slower  |
| async_tree_io              | 374 ms        | 384 ms: 1.03x slower   |
| go                         | 68.6 ms       | 70.4 ms: 1.03x slower  |
| float                      | 40.4 ms       | 41.4 ms: 1.03x slower  |
| genshi_text                | 14.1 ms       | 14.5 ms: 1.03x slower  |
| meteor_contest             | 72.3 ms       | 74.5 ms: 1.03x slower  |
| async_tree_io_tg           | 374 ms        | 385 ms: 1.03x slower   |
| regex_compile              | 79.3 ms       | 81.9 ms: 1.03x slower  |
| pycparser                  | 688 ms        | 713 ms: 1.04x slower   |
| pyflate                    | 264 ms        | 274 ms: 1.04x slower   |
| coroutines                 | 11.8 ms       | 12.3 ms: 1.04x slower  |
| sympy_sum                  | 88.0 ms       | 91.4 ms: 1.04x slower  |
| sympy_integrate            | 12.9 ms       | 13.4 ms: 1.04x slower  |
| async_tree_memoization     | 202 ms        | 210 ms: 1.04x slower   |
| html5lib                   | 37.2 ms       | 38.8 ms: 1.04x slower  |
| async_tree_none_tg         | 160 ms        | 167 ms: 1.05x slower   |
| raytrace                   | 162 ms        | 169 ms: 1.05x slower   |
| logging_format             | 6.39 us       | 6.70 us: 1.05x slower  |
| sphinx                     | 666 ms        | 702 ms: 1.05x slower   |
| async_tree_none            | 165 ms        | 174 ms: 1.05x slower   |
| bench_mp_pool              | 88.6 ms       | 93.6 ms: 1.06x slower  |
| async_generators           | 202 ms        | 213 ms: 1.06x slower   |
| pprint_safe_repr           | 481 ms        | 510 ms: 1.06x slower   |
| tomli_loads                | 1.18 sec      | 1.26 sec: 1.06x slower |
| regex_v8                   | 15.3 ms       | 16.3 ms: 1.07x slower  |
| bench_thread_pool          | 819 us        | 876 us: 1.07x slower   |
| logging_simple             | 5.84 us       | 6.25 us: 1.07x slower  |
| sqlite_synth               | 1.56 us       | 1.68 us: 1.07x slower  |
| fannkuch                   | 233 ms        | 250 ms: 1.07x slower   |
| sqlglot_v2_transpile       | 943 us        | 1.01 ms: 1.07x slower  |
| sqlglot_v2_parse           | 742 us        | 798 us: 1.07x slower   |
| pprint_pformat             | 963 ms        | 1.04 sec: 1.08x slower |
| subparsers                 | 41.2 ms       | 44.5 ms: 1.08x slower  |
| typing_runtime_protocols   | 98.1 us       | 106 us: 1.08x slower   |
| async_tree_cpu_io_mixed    | 332 ms        | 359 ms: 1.08x slower   |
| scimark_sor                | 63.1 ms       | 68.6 ms: 1.09x slower  |
| sympy_str                  | 163 ms        | 177 ms: 1.09x slower   |
| sympy_expand               | 279 ms        | 304 ms: 1.09x slower   |
| spectral_norm              | 46.7 ms       | 51.1 ms: 1.09x slower  |
| sqlglot_v2_optimize        | 33.0 ms       | 36.1 ms: 1.09x slower  |
| hexiom                     | 3.58 ms       | 3.92 ms: 1.09x slower  |
| scimark_monte_carlo        | 35.5 ms       | 38.9 ms: 1.10x slower  |
| xml_etree_iterparse        | 64.2 ms       | 70.4 ms: 1.10x slower  |
| scimark_sparse_mat_mult    | 2.25 ms       | 2.47 ms: 1.10x slower  |
| richards                   | 28.1 ms       | 30.9 ms: 1.10x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 363 ms: 1.10x slower   |
| django_template            | 22.9 ms       | 25.2 ms: 1.10x slower  |
| sqlglot_v2_normalize       | 66.7 ms       | 73.3 ms: 1.10x slower  |
| nqueens                    | 54.2 ms       | 59.6 ms: 1.10x slower  |
| chaos                      | 34.2 ms       | 37.7 ms: 1.10x slower  |
| 2to3                       | 209 ms        | 231 ms: 1.11x slower   |
| scimark_fft                | 151 ms        | 169 ms: 1.12x slower   |
| richards_super             | 32.0 ms       | 35.8 ms: 1.12x slower  |
| deepcopy_reduce            | 1.69 us       | 1.90 us: 1.12x slower  |
| bpe_tokeniser              | 2.67 sec      | 3.01 sec: 1.13x slower |
| xml_etree_parse            | 92.6 ms       | 105 ms: 1.13x slower   |
| deepcopy_memo              | 17.0 us       | 19.3 us: 1.13x slower  |
| thrift                     | 487 us        | 551 us: 1.13x slower   |
| deepcopy                   | 159 us        | 180 us: 1.14x slower   |
| many_optionals             | 669 us        | 762 us: 1.14x slower   |
| json_dumps                 | 6.84 ms       | 7.79 ms: 1.14x slower  |
| pickle_pure_python         | 195 us        | 223 us: 1.14x slower   |
| telco                      | 4.60 ms       | 5.26 ms: 1.14x slower  |
| crypto_pyaes               | 41.7 ms       | 48.0 ms: 1.15x slower  |
| logging_silent             | 53.0 ns       | 61.1 ns: 1.15x slower  |
| scimark_lu                 | 55.5 ms       | 64.2 ms: 1.16x slower  |
| comprehensions             | 9.60 us       | 11.3 us: 1.18x slower  |
| xml_etree_process          | 37.9 ms       | 44.7 ms: 1.18x slower  |
| xml_etree_generate         | 54.3 ms       | 64.7 ms: 1.19x slower  |
| json                       | 3.16 ms       | 3.78 ms: 1.20x slower  |
| coverage                   | 46.2 ms       | 55.4 ms: 1.20x slower  |
| unpickle_pure_python       | 123 us        | 148 us: 1.20x slower   |
| mako                       | 6.50 ms       | 7.84 ms: 1.21x slower  |
| regex_effbot               | 1.53 ms       | 1.85 ms: 1.21x slower  |
| gc_traversal               | 2.21 ms       | 2.83 ms: 1.28x slower  |
| json_loads                 | 15.8 us       | 21.9 us: 1.38x slower  |
| Geometric mean             | (ref)         | 1.07x slower           |

Benchmark hidden because not significant (8): asyncio_websockets, create_gc_cycles, generators, genshi_xml, nbody, python_startup, async_tree_memoization_tg, pylint

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown