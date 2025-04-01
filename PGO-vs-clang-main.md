# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.046x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-main | PGO                    |
|----------------|:----------:|:----------------------:|
| 2to3           | 220 ms     | 227 ms: 1.03x slower   |
| docutils       | 1.65 sec   | 1.68 sec: 1.02x slower |
| html5lib       | 39.0 ms    | 40.8 ms: 1.04x slower  |
| Geometric mean | (ref)      | 1.03x slower           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | clang-main | PGO                   |
|------------------------|:----------:|:---------------------:|
| coroutines             | 13.4 ms    | 13.5 ms: 1.01x slower |
| async_generators       | 223 ms     | 226 ms: 1.01x slower  |
| async_tree_io          | 416 ms     | 423 ms: 1.02x slower  |
| async_tree_memoization | 216 ms     | 224 ms: 1.04x slower  |
| asyncio_websockets     | 158 ms     | 318 ms: 2.02x slower  |
| Geometric mean         | (ref)      | 1.08x slower          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-main | PGO                   |
|----------------|:----------:|:---------------------:|
| pidigits       | 149 ms     | 152 ms: 1.02x slower  |
| float          | 44.7 ms    | 47.8 ms: 1.07x slower |
| nbody          | 64.2 ms    | 74.1 ms: 1.15x slower |
| Geometric mean | (ref)      | 1.08x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-main | PGO                   |
|----------------|:----------:|:---------------------:|
| regex_dna      | 114 ms     | 112 ms: 1.01x faster  |
| regex_effbot   | 1.39 ms    | 1.42 ms: 1.02x slower |
| regex_compile  | 82.3 ms    | 88.2 ms: 1.07x slower |
| Geometric mean | (ref)      | 1.02x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-main | PGO                    |
|----------------------|:----------:|:----------------------:|
| json_loads           | 15.1 us    | 14.7 us: 1.03x faster  |
| xml_etree_process    | 40.9 ms    | 41.5 ms: 1.02x slower  |
| xml_etree_generate   | 57.2 ms    | 58.7 ms: 1.03x slower  |
| tomli_loads          | 1.41 sec   | 1.47 sec: 1.04x slower |
| json_dumps           | 6.78 ms    | 7.05 ms: 1.04x slower  |
| xml_etree_parse      | 87.6 ms    | 91.2 ms: 1.04x slower  |
| pickle_pure_python   | 216 us     | 237 us: 1.10x slower   |
| unpickle_pure_python | 140 us     | 155 us: 1.11x slower   |
| Geometric mean       | (ref)      | 1.04x slower           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang-main | PGO                   |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 20.4 ms    | 19.8 ms: 1.03x faster |
| python_startup         | 25.8 ms    | 26.1 ms: 1.01x slower |
| Geometric mean         | (ref)      | 1.01x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-main | PGO                   |
|-----------------|:----------:|:---------------------:|
| django_template | 25.4 ms    | 25.1 ms: 1.01x faster |
| mako            | 6.71 ms    | 6.86 ms: 1.02x slower |
| genshi_text     | 15.8 ms    | 16.5 ms: 1.04x slower |
| genshi_xml      | 34.2 ms    | 36.3 ms: 1.06x slower |
| Geometric mean  | (ref)      | 1.03x slower          |

All benchmarks:
===============

| Benchmark                | clang-main | PGO                    |
|--------------------------|:----------:|:----------------------:|
| coverage                 | 48.3 ms    | 46.8 ms: 1.03x faster  |
| python_startup_no_site   | 20.4 ms    | 19.8 ms: 1.03x faster  |
| json_loads               | 15.1 us    | 14.7 us: 1.03x faster  |
| connected_components     | 336 ms     | 329 ms: 1.02x faster   |
| shortest_path            | 366 ms     | 359 ms: 1.02x faster   |
| regex_dna                | 114 ms     | 112 ms: 1.01x faster   |
| comprehensions           | 11.5 us    | 11.3 us: 1.01x faster  |
| django_template          | 25.4 ms    | 25.1 ms: 1.01x faster  |
| pathlib                  | 32.5 ms    | 32.1 ms: 1.01x faster  |
| typing_runtime_protocols | 107 us     | 106 us: 1.01x faster   |
| sympy_expand             | 301 ms     | 302 ms: 1.01x slower   |
| coroutines               | 13.4 ms    | 13.5 ms: 1.01x slower  |
| python_startup           | 25.8 ms    | 26.1 ms: 1.01x slower  |
| meteor_contest           | 76.2 ms    | 76.9 ms: 1.01x slower  |
| bpe_tokeniser            | 2.93 sec   | 2.96 sec: 1.01x slower |
| sympy_sum                | 89.6 ms    | 90.5 ms: 1.01x slower  |
| subparsers               | 15.9 ms    | 16.1 ms: 1.01x slower  |
| scimark_sparse_mat_mult  | 2.69 ms    | 2.72 ms: 1.01x slower  |
| many_optionals           | 432 us     | 438 us: 1.01x slower   |
| async_generators         | 223 ms     | 226 ms: 1.01x slower   |
| pycparser                | 728 ms     | 738 ms: 1.01x slower   |
| docutils                 | 1.65 sec   | 1.68 sec: 1.02x slower |
| json                     | 3.09 ms    | 3.14 ms: 1.02x slower  |
| async_tree_io            | 416 ms     | 423 ms: 1.02x slower   |
| xml_etree_process        | 40.9 ms    | 41.5 ms: 1.02x slower  |
| pidigits                 | 149 ms     | 152 ms: 1.02x slower   |
| regex_effbot             | 1.39 ms    | 1.42 ms: 1.02x slower  |
| mako                     | 6.71 ms    | 6.86 ms: 1.02x slower  |
| logging_simple           | 6.39 us    | 6.53 us: 1.02x slower  |
| logging_format           | 6.88 us    | 7.03 us: 1.02x slower  |
| xml_etree_generate       | 57.2 ms    | 58.7 ms: 1.03x slower  |
| dulwich_log              | 42.1 ms    | 43.4 ms: 1.03x slower  |
| deepcopy_reduce          | 1.88 us    | 1.94 us: 1.03x slower  |
| 2to3                     | 220 ms     | 227 ms: 1.03x slower   |
| tomli_loads              | 1.41 sec   | 1.47 sec: 1.04x slower |
| json_dumps               | 6.78 ms    | 7.05 ms: 1.04x slower  |
| async_tree_memoization   | 216 ms     | 224 ms: 1.04x slower   |
| xml_etree_parse          | 87.6 ms    | 91.2 ms: 1.04x slower  |
| scimark_fft              | 185 ms     | 192 ms: 1.04x slower   |
| html5lib                 | 39.0 ms    | 40.8 ms: 1.04x slower  |
| genshi_text              | 15.8 ms    | 16.5 ms: 1.04x slower  |
| sqlglot_v2_transpile     | 1.05 ms    | 1.10 ms: 1.05x slower  |
| sqlglot_v2_parse         | 851 us     | 892 us: 1.05x slower   |
| sympy_integrate          | 12.9 ms    | 13.5 ms: 1.05x slower  |
| deepcopy                 | 180 us     | 190 us: 1.05x slower   |
| raytrace                 | 181 ms     | 191 ms: 1.05x slower   |
| pprint_pformat           | 1.07 sec   | 1.13 sec: 1.06x slower |
| crypto_pyaes             | 47.3 ms    | 50.0 ms: 1.06x slower  |
| genshi_xml               | 34.2 ms    | 36.3 ms: 1.06x slower  |
| hexiom                   | 4.12 ms    | 4.38 ms: 1.06x slower  |
| float                    | 44.7 ms    | 47.8 ms: 1.07x slower  |
| pprint_safe_repr         | 521 ms     | 558 ms: 1.07x slower   |
| regex_compile            | 82.3 ms    | 88.2 ms: 1.07x slower  |
| generators               | 17.9 ms    | 19.3 ms: 1.08x slower  |
| pyflate                  | 291 ms     | 315 ms: 1.08x slower   |
| deltablue                | 2.12 ms    | 2.29 ms: 1.08x slower  |
| scimark_monte_carlo      | 43.5 ms    | 47.1 ms: 1.08x slower  |
| scimark_lu               | 61.6 ms    | 66.9 ms: 1.09x slower  |
| chaos                    | 40.2 ms    | 43.6 ms: 1.09x slower  |
| go                       | 80.8 ms    | 88.6 ms: 1.10x slower  |
| pickle_pure_python       | 216 us     | 237 us: 1.10x slower   |
| deepcopy_memo            | 19.1 us    | 21.0 us: 1.10x slower  |
| richards                 | 27.8 ms    | 30.7 ms: 1.10x slower  |
| unpickle_pure_python     | 140 us     | 155 us: 1.11x slower   |
| richards_super           | 31.5 ms    | 35.1 ms: 1.12x slower  |
| spectral_norm            | 55.1 ms    | 61.5 ms: 1.12x slower  |
| fannkuch                 | 260 ms     | 296 ms: 1.14x slower   |
| nbody                    | 64.2 ms    | 74.1 ms: 1.15x slower  |
| logging_silent           | 56.3 ns    | 65.2 ns: 1.16x slower  |
| scimark_sor              | 76.7 ms    | 91.0 ms: 1.19x slower  |
| asyncio_websockets       | 158 ms     | 318 ms: 2.02x slower   |
| mdp                      | 799 ms     | 1.64 sec: 2.05x slower |
| Geometric mean           | (ref)      | 1.05x slower           |

Benchmark hidden because not significant (21): gc_traversal, xml_etree_iterparse, bench_mp_pool, sqlglot_v2_optimize, bench_thread_pool, nqueens, create_gc_cycles, async_tree_cpu_io_mixed_tg, sqlglot_v2_normalize, async_tree_memoization_tg, sympy_str, telco, async_tree_none_tg, pylint, sqlite_synth, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, sphinx, regex_v8, k_core
Ignored benchmarks (8) of clang-main.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of PGO.json: thrift

- Geometric mean (including insignificant results): 1.046x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown