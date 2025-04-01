# Results vs. base

- fork: unknown
- ref: clang-main
- machine: unknown-unknown
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | clang-main             |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 220 ms: 1.05x slower   |
| docutils       | 1.74 sec      | 1.65 sec: 1.05x faster |
| html5lib       | 37.2 ms       | 39.0 ms: 1.05x slower  |
| sphinx         | 666 ms        | 653 ms: 1.02x faster   |
| Geometric mean | (ref)         | 1.01x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | clang-main            |
|----------------------------|:-------------:|:---------------------:|
| asyncio_websockets         | 315 ms        | 158 ms: 1.99x faster  |
| async_tree_cpu_io_mixed    | 332 ms        | 337 ms: 1.01x slower  |
| async_tree_memoization_tg  | 209 ms        | 215 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 342 ms: 1.03x slower  |
| async_tree_memoization     | 202 ms        | 216 ms: 1.07x slower  |
| async_tree_io_tg           | 374 ms        | 407 ms: 1.09x slower  |
| async_tree_none_tg         | 160 ms        | 176 ms: 1.10x slower  |
| async_generators           | 202 ms        | 223 ms: 1.11x slower  |
| async_tree_io              | 374 ms        | 416 ms: 1.11x slower  |
| async_tree_none            | 165 ms        | 185 ms: 1.13x slower  |
| coroutines                 | 11.8 ms       | 13.4 ms: 1.13x slower |
| Geometric mean             | (ref)         | 1.01x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | clang-main            |
|----------------|:-------------:|:---------------------:|
| pidigits       | 151 ms        | 149 ms: 1.01x faster  |
| float          | 40.4 ms       | 44.7 ms: 1.11x slower |
| nbody          | 53.0 ms       | 64.2 ms: 1.21x slower |
| Geometric mean | (ref)         | 1.10x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | clang-main            |
|----------------|:-------------:|:---------------------:|
| regex_v8       | 15.3 ms       | 13.4 ms: 1.14x faster |
| regex_effbot   | 1.53 ms       | 1.39 ms: 1.10x faster |
| regex_dna      | 125 ms        | 114 ms: 1.10x faster  |
| regex_compile  | 79.3 ms       | 82.3 ms: 1.04x slower |
| Geometric mean | (ref)         | 1.07x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | clang-main             |
|----------------------|:-------------:|:----------------------:|
| xml_etree_parse      | 92.6 ms       | 87.6 ms: 1.06x faster  |
| json_loads           | 15.8 us       | 15.1 us: 1.05x faster  |
| xml_etree_generate   | 54.3 ms       | 57.2 ms: 1.05x slower  |
| xml_etree_process    | 37.9 ms       | 40.9 ms: 1.08x slower  |
| pickle_pure_python   | 195 us        | 216 us: 1.10x slower   |
| unpickle_pure_python | 123 us        | 140 us: 1.14x slower   |
| tomli_loads          | 1.18 sec      | 1.41 sec: 1.19x slower |
| Geometric mean       | (ref)         | 1.05x slower           |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-MostPGO-Ex | clang-main            |
|------------------------|:-------------:|:---------------------:|
| python_startup         | 26.4 ms       | 25.8 ms: 1.02x faster |
| python_startup_no_site | 19.9 ms       | 20.4 ms: 1.03x slower |
| Geometric mean         | (ref)         | 1.00x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | clang-main            |
|-----------------|:-------------:|:---------------------:|
| mako            | 6.50 ms       | 6.71 ms: 1.03x slower |
| genshi_xml      | 31.3 ms       | 34.2 ms: 1.09x slower |
| django_template | 22.9 ms       | 25.4 ms: 1.11x slower |
| genshi_text     | 14.1 ms       | 15.8 ms: 1.12x slower |
| Geometric mean  | (ref)         | 1.09x slower          |

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | clang-main             |
|----------------------------|:-------------:|:----------------------:|
| subparsers                 | 41.2 ms       | 15.9 ms: 2.59x faster  |
| asyncio_websockets         | 315 ms        | 158 ms: 1.99x faster   |
| mdp                        | 1.56 sec      | 799 ms: 1.95x faster   |
| many_optionals             | 669 us        | 432 us: 1.55x faster   |
| k_core                     | 2.00 sec      | 1.71 sec: 1.17x faster |
| regex_v8                   | 15.3 ms       | 13.4 ms: 1.14x faster  |
| regex_effbot               | 1.53 ms       | 1.39 ms: 1.10x faster  |
| regex_dna                  | 125 ms        | 114 ms: 1.10x faster   |
| connected_components       | 366 ms        | 336 ms: 1.09x faster   |
| shortest_path              | 399 ms        | 366 ms: 1.09x faster   |
| create_gc_cycles           | 1.35 ms       | 1.25 ms: 1.08x faster  |
| gc_traversal               | 2.21 ms       | 2.08 ms: 1.06x faster  |
| xml_etree_parse            | 92.6 ms       | 87.6 ms: 1.06x faster  |
| docutils                   | 1.74 sec      | 1.65 sec: 1.05x faster |
| json_loads                 | 15.8 us       | 15.1 us: 1.05x faster  |
| json                       | 3.16 ms       | 3.09 ms: 1.02x faster  |
| python_startup             | 26.4 ms       | 25.8 ms: 1.02x faster  |
| sphinx                     | 666 ms        | 653 ms: 1.02x faster   |
| richards_super             | 32.0 ms       | 31.5 ms: 1.02x faster  |
| pidigits                   | 151 ms        | 149 ms: 1.01x faster   |
| richards                   | 28.1 ms       | 27.8 ms: 1.01x faster  |
| sqlite_synth               | 1.56 us       | 1.58 us: 1.01x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 337 ms: 1.01x slower   |
| dulwich_log                | 41.5 ms       | 42.1 ms: 1.02x slower  |
| sympy_sum                  | 88.0 ms       | 89.6 ms: 1.02x slower  |
| async_tree_memoization_tg  | 209 ms        | 215 ms: 1.03x slower   |
| python_startup_no_site     | 19.9 ms       | 20.4 ms: 1.03x slower  |
| mako                       | 6.50 ms       | 6.71 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 342 ms: 1.03x slower   |
| regex_compile              | 79.3 ms       | 82.3 ms: 1.04x slower  |
| coverage                   | 46.2 ms       | 48.3 ms: 1.04x slower  |
| html5lib                   | 37.2 ms       | 39.0 ms: 1.05x slower  |
| xml_etree_generate         | 54.3 ms       | 57.2 ms: 1.05x slower  |
| meteor_contest             | 72.3 ms       | 76.2 ms: 1.05x slower  |
| 2to3                       | 209 ms        | 220 ms: 1.05x slower   |
| bench_thread_pool          | 819 us        | 864 us: 1.05x slower   |
| pycparser                  | 688 ms        | 728 ms: 1.06x slower   |
| telco                      | 4.60 ms       | 4.87 ms: 1.06x slower  |
| logging_silent             | 53.0 ns       | 56.3 ns: 1.06x slower  |
| sqlglot_v2_optimize        | 33.0 ms       | 35.1 ms: 1.06x slower  |
| async_tree_memoization     | 202 ms        | 216 ms: 1.07x slower   |
| logging_format             | 6.39 us       | 6.88 us: 1.08x slower  |
| sympy_expand               | 279 ms        | 301 ms: 1.08x slower   |
| sympy_str                  | 163 ms        | 175 ms: 1.08x slower   |
| xml_etree_process          | 37.9 ms       | 40.9 ms: 1.08x slower  |
| pprint_safe_repr           | 481 ms        | 521 ms: 1.08x slower   |
| async_tree_io_tg           | 374 ms        | 407 ms: 1.09x slower   |
| genshi_xml                 | 31.3 ms       | 34.2 ms: 1.09x slower  |
| logging_simple             | 5.84 us       | 6.39 us: 1.09x slower  |
| typing_runtime_protocols   | 98.1 us       | 107 us: 1.09x slower   |
| generators                 | 16.3 ms       | 17.9 ms: 1.10x slower  |
| bpe_tokeniser              | 2.67 sec      | 2.93 sec: 1.10x slower |
| async_tree_none_tg         | 160 ms        | 176 ms: 1.10x slower   |
| sqlglot_v2_normalize       | 66.7 ms       | 73.4 ms: 1.10x slower  |
| pyflate                    | 264 ms        | 291 ms: 1.10x slower   |
| pickle_pure_python         | 195 us        | 216 us: 1.10x slower   |
| float                      | 40.4 ms       | 44.7 ms: 1.11x slower  |
| django_template            | 22.9 ms       | 25.4 ms: 1.11x slower  |
| pprint_pformat             | 963 ms        | 1.07 sec: 1.11x slower |
| async_generators           | 202 ms        | 223 ms: 1.11x slower   |
| scimark_lu                 | 55.5 ms       | 61.6 ms: 1.11x slower  |
| async_tree_io              | 374 ms        | 416 ms: 1.11x slower   |
| sqlglot_v2_transpile       | 943 us        | 1.05 ms: 1.11x slower  |
| deepcopy_reduce            | 1.69 us       | 1.88 us: 1.12x slower  |
| fannkuch                   | 233 ms        | 260 ms: 1.12x slower   |
| raytrace                   | 162 ms        | 181 ms: 1.12x slower   |
| deepcopy_memo              | 17.0 us       | 19.1 us: 1.12x slower  |
| genshi_text                | 14.1 ms       | 15.8 ms: 1.12x slower  |
| async_tree_none            | 165 ms        | 185 ms: 1.13x slower   |
| deltablue                  | 1.87 ms       | 2.12 ms: 1.13x slower  |
| coroutines                 | 11.8 ms       | 13.4 ms: 1.13x slower  |
| crypto_pyaes               | 41.7 ms       | 47.3 ms: 1.13x slower  |
| deepcopy                   | 159 us        | 180 us: 1.14x slower   |
| unpickle_pure_python       | 123 us        | 140 us: 1.14x slower   |
| sqlglot_v2_parse           | 742 us        | 851 us: 1.15x slower   |
| hexiom                     | 3.58 ms       | 4.12 ms: 1.15x slower  |
| nqueens                    | 54.2 ms       | 63.5 ms: 1.17x slower  |
| chaos                      | 34.2 ms       | 40.2 ms: 1.18x slower  |
| go                         | 68.6 ms       | 80.8 ms: 1.18x slower  |
| spectral_norm              | 46.7 ms       | 55.1 ms: 1.18x slower  |
| tomli_loads                | 1.18 sec      | 1.41 sec: 1.19x slower |
| scimark_sparse_mat_mult    | 2.25 ms       | 2.69 ms: 1.20x slower  |
| comprehensions             | 9.60 us       | 11.5 us: 1.20x slower  |
| nbody                      | 53.0 ms       | 64.2 ms: 1.21x slower  |
| scimark_sor                | 63.1 ms       | 76.7 ms: 1.21x slower  |
| scimark_fft                | 151 ms        | 185 ms: 1.22x slower   |
| scimark_monte_carlo        | 35.5 ms       | 43.5 ms: 1.22x slower  |
| pathlib                    | 25.5 ms       | 32.5 ms: 1.27x slower  |
| Geometric mean             | (ref)         | 1.03x slower           |

Benchmark hidden because not significant (5): pylint, json_dumps, xml_etree_iterparse, sympy_integrate, bench_mp_pool
Ignored benchmarks (1) of TC-MostPGO-Ex.json: thrift
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown