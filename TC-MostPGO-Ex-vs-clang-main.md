# Results vs. base

- fork: unknown
- ref: TC-MostPGO-Ex
- machine: unknown-unknown
- commit hash: 65a24e98fc
- commit date: 2025-03-14
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-main | TC-MostPGO-Ex          |
|----------------|:----------:|:----------------------:|
| 2to3           | 220 ms     | 209 ms: 1.05x faster   |
| docutils       | 1.65 sec   | 1.74 sec: 1.05x slower |
| html5lib       | 39.0 ms    | 37.2 ms: 1.05x faster  |
| sphinx         | 653 ms     | 666 ms: 1.02x slower   |
| Geometric mean | (ref)      | 1.01x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-main | TC-MostPGO-Ex         |
|----------------------------|:----------:|:---------------------:|
| coroutines                 | 13.4 ms    | 11.8 ms: 1.13x faster |
| async_tree_none            | 185 ms     | 165 ms: 1.13x faster  |
| async_tree_io              | 416 ms     | 374 ms: 1.11x faster  |
| async_generators           | 223 ms     | 202 ms: 1.11x faster  |
| async_tree_none_tg         | 176 ms     | 160 ms: 1.10x faster  |
| async_tree_io_tg           | 407 ms     | 374 ms: 1.09x faster  |
| async_tree_memoization     | 216 ms     | 202 ms: 1.07x faster  |
| async_tree_cpu_io_mixed_tg | 342 ms     | 331 ms: 1.03x faster  |
| async_tree_memoization_tg  | 215 ms     | 209 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 337 ms     | 332 ms: 1.01x faster  |
| asyncio_websockets         | 158 ms     | 315 ms: 1.99x slower  |
| Geometric mean             | (ref)      | 1.01x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-main | TC-MostPGO-Ex         |
|----------------|:----------:|:---------------------:|
| nbody          | 64.2 ms    | 53.0 ms: 1.21x faster |
| float          | 44.7 ms    | 40.4 ms: 1.11x faster |
| pidigits       | 149 ms     | 151 ms: 1.01x slower  |
| Geometric mean | (ref)      | 1.10x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-main | TC-MostPGO-Ex         |
|----------------|:----------:|:---------------------:|
| regex_compile  | 82.3 ms    | 79.3 ms: 1.04x faster |
| regex_dna      | 114 ms     | 125 ms: 1.10x slower  |
| regex_effbot   | 1.39 ms    | 1.53 ms: 1.10x slower |
| regex_v8       | 13.4 ms    | 15.3 ms: 1.14x slower |
| Geometric mean | (ref)      | 1.07x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-main | TC-MostPGO-Ex          |
|----------------------|:----------:|:----------------------:|
| tomli_loads          | 1.41 sec   | 1.18 sec: 1.19x faster |
| unpickle_pure_python | 140 us     | 123 us: 1.14x faster   |
| pickle_pure_python   | 216 us     | 195 us: 1.10x faster   |
| xml_etree_process    | 40.9 ms    | 37.9 ms: 1.08x faster  |
| xml_etree_generate   | 57.2 ms    | 54.3 ms: 1.05x faster  |
| json_loads           | 15.1 us    | 15.8 us: 1.05x slower  |
| xml_etree_parse      | 87.6 ms    | 92.6 ms: 1.06x slower  |
| Geometric mean       | (ref)      | 1.05x faster           |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-main | TC-MostPGO-Ex         |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 20.4 ms    | 19.9 ms: 1.03x faster |
| python_startup         | 25.8 ms    | 26.4 ms: 1.02x slower |
| Geometric mean         | (ref)      | 1.00x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-main | TC-MostPGO-Ex         |
|-----------------|:----------:|:---------------------:|
| genshi_text     | 15.8 ms    | 14.1 ms: 1.12x faster |
| django_template | 25.4 ms    | 22.9 ms: 1.11x faster |
| genshi_xml      | 34.2 ms    | 31.3 ms: 1.09x faster |
| mako            | 6.71 ms    | 6.50 ms: 1.03x faster |
| Geometric mean  | (ref)      | 1.09x faster          |

All benchmarks:
===============

| Benchmark                  | clang-main | TC-MostPGO-Ex          |
|----------------------------|:----------:|:----------------------:|
| pathlib                    | 32.5 ms    | 25.5 ms: 1.27x faster  |
| scimark_monte_carlo        | 43.5 ms    | 35.5 ms: 1.22x faster  |
| scimark_fft                | 185 ms     | 151 ms: 1.22x faster   |
| scimark_sor                | 76.7 ms    | 63.1 ms: 1.21x faster  |
| nbody                      | 64.2 ms    | 53.0 ms: 1.21x faster  |
| comprehensions             | 11.5 us    | 9.60 us: 1.20x faster  |
| scimark_sparse_mat_mult    | 2.69 ms    | 2.25 ms: 1.20x faster  |
| tomli_loads                | 1.41 sec   | 1.18 sec: 1.19x faster |
| spectral_norm              | 55.1 ms    | 46.7 ms: 1.18x faster  |
| go                         | 80.8 ms    | 68.6 ms: 1.18x faster  |
| chaos                      | 40.2 ms    | 34.2 ms: 1.18x faster  |
| nqueens                    | 63.5 ms    | 54.2 ms: 1.17x faster  |
| hexiom                     | 4.12 ms    | 3.58 ms: 1.15x faster  |
| sqlglot_v2_parse           | 851 us     | 742 us: 1.15x faster   |
| unpickle_pure_python       | 140 us     | 123 us: 1.14x faster   |
| deepcopy                   | 180 us     | 159 us: 1.14x faster   |
| crypto_pyaes               | 47.3 ms    | 41.7 ms: 1.13x faster  |
| coroutines                 | 13.4 ms    | 11.8 ms: 1.13x faster  |
| deltablue                  | 2.12 ms    | 1.87 ms: 1.13x faster  |
| async_tree_none            | 185 ms     | 165 ms: 1.13x faster   |
| genshi_text                | 15.8 ms    | 14.1 ms: 1.12x faster  |
| deepcopy_memo              | 19.1 us    | 17.0 us: 1.12x faster  |
| raytrace                   | 181 ms     | 162 ms: 1.12x faster   |
| fannkuch                   | 260 ms     | 233 ms: 1.12x faster   |
| deepcopy_reduce            | 1.88 us    | 1.69 us: 1.12x faster  |
| sqlglot_v2_transpile       | 1.05 ms    | 943 us: 1.11x faster   |
| async_tree_io              | 416 ms     | 374 ms: 1.11x faster   |
| scimark_lu                 | 61.6 ms    | 55.5 ms: 1.11x faster  |
| async_generators           | 223 ms     | 202 ms: 1.11x faster   |
| pprint_pformat             | 1.07 sec   | 963 ms: 1.11x faster   |
| django_template            | 25.4 ms    | 22.9 ms: 1.11x faster  |
| float                      | 44.7 ms    | 40.4 ms: 1.11x faster  |
| pickle_pure_python         | 216 us     | 195 us: 1.10x faster   |
| pyflate                    | 291 ms     | 264 ms: 1.10x faster   |
| sqlglot_v2_normalize       | 73.4 ms    | 66.7 ms: 1.10x faster  |
| async_tree_none_tg         | 176 ms     | 160 ms: 1.10x faster   |
| bpe_tokeniser              | 2.93 sec   | 2.67 sec: 1.10x faster |
| generators                 | 17.9 ms    | 16.3 ms: 1.10x faster  |
| typing_runtime_protocols   | 107 us     | 98.1 us: 1.09x faster  |
| logging_simple             | 6.39 us    | 5.84 us: 1.09x faster  |
| genshi_xml                 | 34.2 ms    | 31.3 ms: 1.09x faster  |
| async_tree_io_tg           | 407 ms     | 374 ms: 1.09x faster   |
| pprint_safe_repr           | 521 ms     | 481 ms: 1.08x faster   |
| xml_etree_process          | 40.9 ms    | 37.9 ms: 1.08x faster  |
| sympy_str                  | 175 ms     | 163 ms: 1.08x faster   |
| sympy_expand               | 301 ms     | 279 ms: 1.08x faster   |
| logging_format             | 6.88 us    | 6.39 us: 1.08x faster  |
| async_tree_memoization     | 216 ms     | 202 ms: 1.07x faster   |
| sqlglot_v2_optimize        | 35.1 ms    | 33.0 ms: 1.06x faster  |
| logging_silent             | 56.3 ns    | 53.0 ns: 1.06x faster  |
| telco                      | 4.87 ms    | 4.60 ms: 1.06x faster  |
| pycparser                  | 728 ms     | 688 ms: 1.06x faster   |
| bench_thread_pool          | 864 us     | 819 us: 1.05x faster   |
| 2to3                       | 220 ms     | 209 ms: 1.05x faster   |
| meteor_contest             | 76.2 ms    | 72.3 ms: 1.05x faster  |
| xml_etree_generate         | 57.2 ms    | 54.3 ms: 1.05x faster  |
| html5lib                   | 39.0 ms    | 37.2 ms: 1.05x faster  |
| coverage                   | 48.3 ms    | 46.2 ms: 1.04x faster  |
| regex_compile              | 82.3 ms    | 79.3 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 342 ms     | 331 ms: 1.03x faster   |
| mako                       | 6.71 ms    | 6.50 ms: 1.03x faster  |
| python_startup_no_site     | 20.4 ms    | 19.9 ms: 1.03x faster  |
| async_tree_memoization_tg  | 215 ms     | 209 ms: 1.03x faster   |
| sympy_sum                  | 89.6 ms    | 88.0 ms: 1.02x faster  |
| dulwich_log                | 42.1 ms    | 41.5 ms: 1.02x faster  |
| async_tree_cpu_io_mixed    | 337 ms     | 332 ms: 1.01x faster   |
| sqlite_synth               | 1.58 us    | 1.56 us: 1.01x faster  |
| richards                   | 27.8 ms    | 28.1 ms: 1.01x slower  |
| pidigits                   | 149 ms     | 151 ms: 1.01x slower   |
| richards_super             | 31.5 ms    | 32.0 ms: 1.02x slower  |
| sphinx                     | 653 ms     | 666 ms: 1.02x slower   |
| python_startup             | 25.8 ms    | 26.4 ms: 1.02x slower  |
| json                       | 3.09 ms    | 3.16 ms: 1.02x slower  |
| json_loads                 | 15.1 us    | 15.8 us: 1.05x slower  |
| docutils                   | 1.65 sec   | 1.74 sec: 1.05x slower |
| xml_etree_parse            | 87.6 ms    | 92.6 ms: 1.06x slower  |
| gc_traversal               | 2.08 ms    | 2.21 ms: 1.06x slower  |
| create_gc_cycles           | 1.25 ms    | 1.35 ms: 1.08x slower  |
| shortest_path              | 366 ms     | 399 ms: 1.09x slower   |
| connected_components       | 336 ms     | 366 ms: 1.09x slower   |
| regex_dna                  | 114 ms     | 125 ms: 1.10x slower   |
| regex_effbot               | 1.39 ms    | 1.53 ms: 1.10x slower  |
| regex_v8                   | 13.4 ms    | 15.3 ms: 1.14x slower  |
| k_core                     | 1.71 sec   | 2.00 sec: 1.17x slower |
| many_optionals             | 432 us     | 669 us: 1.55x slower   |
| mdp                        | 799 ms     | 1.56 sec: 1.95x slower |
| asyncio_websockets         | 158 ms     | 315 ms: 1.99x slower   |
| subparsers                 | 15.9 ms    | 41.2 ms: 2.59x slower  |
| Geometric mean             | (ref)      | 1.03x faster           |

Benchmark hidden because not significant (5): bench_mp_pool, sympy_integrate, xml_etree_iterparse, json_dumps, pylint
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of TC-MostPGO-Ex.json: thrift

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown