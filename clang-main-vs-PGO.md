# Results vs. base

- fork: unknown
- ref: clang-main
- machine: unknown-unknown
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | clang-main             |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 220 ms: 1.03x faster   |
| docutils       | 1.68 sec | 1.65 sec: 1.02x faster |
| html5lib       | 40.8 ms  | 39.0 ms: 1.04x faster  |
| Geometric mean | (ref)    | 1.03x faster           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | PGO     | clang-main            |
|------------------------|:-------:|:---------------------:|
| asyncio_websockets     | 318 ms  | 158 ms: 2.02x faster  |
| async_tree_memoization | 224 ms  | 216 ms: 1.04x faster  |
| async_tree_io          | 423 ms  | 416 ms: 1.02x faster  |
| async_generators       | 226 ms  | 223 ms: 1.01x faster  |
| coroutines             | 13.5 ms | 13.4 ms: 1.01x faster |
| Geometric mean         | (ref)   | 1.08x faster          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | clang-main            |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 64.2 ms: 1.15x faster |
| float          | 47.8 ms | 44.7 ms: 1.07x faster |
| pidigits       | 152 ms  | 149 ms: 1.02x faster  |
| Geometric mean | (ref)   | 1.08x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | clang-main            |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 82.3 ms: 1.07x faster |
| regex_effbot   | 1.42 ms | 1.39 ms: 1.02x faster |
| regex_dna      | 112 ms  | 114 ms: 1.01x slower  |
| Geometric mean | (ref)   | 1.02x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | clang-main             |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 140 us: 1.11x faster   |
| pickle_pure_python   | 237 us   | 216 us: 1.10x faster   |
| xml_etree_parse      | 91.2 ms  | 87.6 ms: 1.04x faster  |
| json_dumps           | 7.05 ms  | 6.78 ms: 1.04x faster  |
| tomli_loads          | 1.47 sec | 1.41 sec: 1.04x faster |
| xml_etree_generate   | 58.7 ms  | 57.2 ms: 1.03x faster  |
| xml_etree_process    | 41.5 ms  | 40.9 ms: 1.02x faster  |
| json_loads           | 14.7 us  | 15.1 us: 1.03x slower  |
| Geometric mean       | (ref)    | 1.04x faster           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | clang-main            |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.1 ms | 25.8 ms: 1.01x faster |
| python_startup_no_site | 19.8 ms | 20.4 ms: 1.03x slower |
| Geometric mean         | (ref)   | 1.01x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | clang-main            |
|-----------------|:-------:|:---------------------:|
| genshi_xml      | 36.3 ms | 34.2 ms: 1.06x faster |
| genshi_text     | 16.5 ms | 15.8 ms: 1.04x faster |
| mako            | 6.86 ms | 6.71 ms: 1.02x faster |
| django_template | 25.1 ms | 25.4 ms: 1.01x slower |
| Geometric mean  | (ref)   | 1.03x faster          |

All benchmarks:
===============

| Benchmark                | PGO      | clang-main             |
|--------------------------|:--------:|:----------------------:|
| mdp                      | 1.64 sec | 799 ms: 2.05x faster   |
| asyncio_websockets       | 318 ms   | 158 ms: 2.02x faster   |
| scimark_sor              | 91.0 ms  | 76.7 ms: 1.19x faster  |
| logging_silent           | 65.2 ns  | 56.3 ns: 1.16x faster  |
| nbody                    | 74.1 ms  | 64.2 ms: 1.15x faster  |
| fannkuch                 | 296 ms   | 260 ms: 1.14x faster   |
| spectral_norm            | 61.5 ms  | 55.1 ms: 1.12x faster  |
| richards_super           | 35.1 ms  | 31.5 ms: 1.12x faster  |
| unpickle_pure_python     | 155 us   | 140 us: 1.11x faster   |
| richards                 | 30.7 ms  | 27.8 ms: 1.10x faster  |
| deepcopy_memo            | 21.0 us  | 19.1 us: 1.10x faster  |
| pickle_pure_python       | 237 us   | 216 us: 1.10x faster   |
| go                       | 88.6 ms  | 80.8 ms: 1.10x faster  |
| chaos                    | 43.6 ms  | 40.2 ms: 1.09x faster  |
| scimark_lu               | 66.9 ms  | 61.6 ms: 1.09x faster  |
| scimark_monte_carlo      | 47.1 ms  | 43.5 ms: 1.08x faster  |
| deltablue                | 2.29 ms  | 2.12 ms: 1.08x faster  |
| pyflate                  | 315 ms   | 291 ms: 1.08x faster   |
| generators               | 19.3 ms  | 17.9 ms: 1.08x faster  |
| regex_compile            | 88.2 ms  | 82.3 ms: 1.07x faster  |
| pprint_safe_repr         | 558 ms   | 521 ms: 1.07x faster   |
| float                    | 47.8 ms  | 44.7 ms: 1.07x faster  |
| hexiom                   | 4.38 ms  | 4.12 ms: 1.06x faster  |
| genshi_xml               | 36.3 ms  | 34.2 ms: 1.06x faster  |
| crypto_pyaes             | 50.0 ms  | 47.3 ms: 1.06x faster  |
| pprint_pformat           | 1.13 sec | 1.07 sec: 1.06x faster |
| raytrace                 | 191 ms   | 181 ms: 1.05x faster   |
| deepcopy                 | 190 us   | 180 us: 1.05x faster   |
| sympy_integrate          | 13.5 ms  | 12.9 ms: 1.05x faster  |
| sqlglot_v2_parse         | 892 us   | 851 us: 1.05x faster   |
| sqlglot_v2_transpile     | 1.10 ms  | 1.05 ms: 1.05x faster  |
| genshi_text              | 16.5 ms  | 15.8 ms: 1.04x faster  |
| html5lib                 | 40.8 ms  | 39.0 ms: 1.04x faster  |
| scimark_fft              | 192 ms   | 185 ms: 1.04x faster   |
| xml_etree_parse          | 91.2 ms  | 87.6 ms: 1.04x faster  |
| async_tree_memoization   | 224 ms   | 216 ms: 1.04x faster   |
| json_dumps               | 7.05 ms  | 6.78 ms: 1.04x faster  |
| tomli_loads              | 1.47 sec | 1.41 sec: 1.04x faster |
| 2to3                     | 227 ms   | 220 ms: 1.03x faster   |
| deepcopy_reduce          | 1.94 us  | 1.88 us: 1.03x faster  |
| dulwich_log              | 43.4 ms  | 42.1 ms: 1.03x faster  |
| xml_etree_generate       | 58.7 ms  | 57.2 ms: 1.03x faster  |
| logging_format           | 7.03 us  | 6.88 us: 1.02x faster  |
| logging_simple           | 6.53 us  | 6.39 us: 1.02x faster  |
| mako                     | 6.86 ms  | 6.71 ms: 1.02x faster  |
| regex_effbot             | 1.42 ms  | 1.39 ms: 1.02x faster  |
| pidigits                 | 152 ms   | 149 ms: 1.02x faster   |
| xml_etree_process        | 41.5 ms  | 40.9 ms: 1.02x faster  |
| async_tree_io            | 423 ms   | 416 ms: 1.02x faster   |
| json                     | 3.14 ms  | 3.09 ms: 1.02x faster  |
| docutils                 | 1.68 sec | 1.65 sec: 1.02x faster |
| pycparser                | 738 ms   | 728 ms: 1.01x faster   |
| async_generators         | 226 ms   | 223 ms: 1.01x faster   |
| many_optionals           | 438 us   | 432 us: 1.01x faster   |
| scimark_sparse_mat_mult  | 2.72 ms  | 2.69 ms: 1.01x faster  |
| subparsers               | 16.1 ms  | 15.9 ms: 1.01x faster  |
| sympy_sum                | 90.5 ms  | 89.6 ms: 1.01x faster  |
| bpe_tokeniser            | 2.96 sec | 2.93 sec: 1.01x faster |
| meteor_contest           | 76.9 ms  | 76.2 ms: 1.01x faster  |
| python_startup           | 26.1 ms  | 25.8 ms: 1.01x faster  |
| coroutines               | 13.5 ms  | 13.4 ms: 1.01x faster  |
| sympy_expand             | 302 ms   | 301 ms: 1.01x faster   |
| typing_runtime_protocols | 106 us   | 107 us: 1.01x slower   |
| pathlib                  | 32.1 ms  | 32.5 ms: 1.01x slower  |
| django_template          | 25.1 ms  | 25.4 ms: 1.01x slower  |
| comprehensions           | 11.3 us  | 11.5 us: 1.01x slower  |
| regex_dna                | 112 ms   | 114 ms: 1.01x slower   |
| shortest_path            | 359 ms   | 366 ms: 1.02x slower   |
| connected_components     | 329 ms   | 336 ms: 1.02x slower   |
| json_loads               | 14.7 us  | 15.1 us: 1.03x slower  |
| python_startup_no_site   | 19.8 ms  | 20.4 ms: 1.03x slower  |
| coverage                 | 46.8 ms  | 48.3 ms: 1.03x slower  |
| Geometric mean           | (ref)    | 1.05x faster           |

Benchmark hidden because not significant (21): k_core, regex_v8, sphinx, async_tree_cpu_io_mixed, async_tree_none, async_tree_io_tg, sqlite_synth, pylint, async_tree_none_tg, telco, sympy_str, async_tree_memoization_tg, sqlglot_v2_normalize, async_tree_cpu_io_mixed_tg, create_gc_cycles, nqueens, bench_thread_pool, sqlglot_v2_optimize, bench_mp_pool, xml_etree_iterparse, gc_traversal
Ignored benchmarks (1) of PGO.json: thrift
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown