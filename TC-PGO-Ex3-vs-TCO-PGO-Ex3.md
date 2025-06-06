# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.008x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 212 ms      | 216 ms: 1.02x slower   |
| docutils       | 1.67 sec    | 1.63 sec: 1.03x faster |
| html5lib       | 37.9 ms     | 36.1 ms: 1.05x faster  |
| sphinx         | 645 ms      | 638 ms: 1.01x faster   |
| Geometric mean | (ref)       | 1.02x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|--------------------|:-----------:|:---------------------:|
| async_tree_io      | 384 ms      | 375 ms: 1.02x faster  |
| async_tree_io_tg   | 377 ms      | 371 ms: 1.02x faster  |
| async_generators   | 202 ms      | 206 ms: 1.02x slower  |
| coroutines         | 11.9 ms     | 12.4 ms: 1.04x slower |
| asyncio_websockets | 301 ms      | 317 ms: 1.05x slower  |
| Geometric mean     | (ref)       | 1.01x slower          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| float          | 41.9 ms     | 40.2 ms: 1.04x faster |
| nbody          | 55.2 ms     | 53.3 ms: 1.04x faster |
| pidigits       | 145 ms      | 146 ms: 1.01x slower  |
| Geometric mean | (ref)       | 1.02x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.46 ms     | 1.40 ms: 1.05x faster |
| regex_dna      | 120 ms      | 115 ms: 1.05x faster  |
| regex_compile  | 78.1 ms     | 74.8 ms: 1.04x faster |
| regex_v8       | 13.2 ms     | 14.1 ms: 1.06x slower |
| Geometric mean | (ref)       | 1.02x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|----------------------|:-----------:|:---------------------:|
| xml_etree_generate   | 53.6 ms     | 51.5 ms: 1.04x faster |
| unpickle_pure_python | 127 us      | 123 us: 1.04x faster  |
| json_loads           | 14.7 us     | 14.5 us: 1.02x faster |
| xml_etree_iterparse  | 61.2 ms     | 60.4 ms: 1.01x faster |
| json_dumps           | 6.55 ms     | 6.48 ms: 1.01x faster |
| xml_etree_process    | 37.0 ms     | 36.7 ms: 1.01x faster |
| pickle_pure_python   | 199 us      | 201 us: 1.01x slower  |
| Geometric mean       | (ref)       | 1.01x faster          |

Benchmark hidden because not significant (2): xml_etree_parse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 18.7 ms     | 19.6 ms: 1.05x slower |
| python_startup         | 24.7 ms     | 26.0 ms: 1.05x slower |
| Geometric mean         | (ref)       | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex3 | TC-PGO-Ex3            |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 32.8 ms     | 30.7 ms: 1.07x faster |
| mako            | 6.28 ms     | 6.12 ms: 1.03x faster |
| django_template | 22.9 ms     | 23.4 ms: 1.02x slower |
| Geometric mean  | (ref)       | 1.02x faster          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | TCO-PGO-Ex3 | TC-PGO-Ex3             |
|------------------------|:-----------:|:----------------------:|
| mdp                    | 1.62 sec    | 1.40 sec: 1.16x faster |
| crypto_pyaes           | 47.4 ms     | 41.6 ms: 1.14x faster  |
| generators             | 16.5 ms     | 14.8 ms: 1.11x faster  |
| genshi_xml             | 32.8 ms     | 30.7 ms: 1.07x faster  |
| html5lib               | 37.9 ms     | 36.1 ms: 1.05x faster  |
| sympy_integrate        | 12.8 ms     | 12.2 ms: 1.05x faster  |
| sympy_sum              | 86.3 ms     | 82.1 ms: 1.05x faster  |
| sympy_expand           | 282 ms      | 269 ms: 1.05x faster   |
| regex_effbot           | 1.46 ms     | 1.40 ms: 1.05x faster  |
| regex_dna              | 120 ms      | 115 ms: 1.05x faster   |
| regex_compile          | 78.1 ms     | 74.8 ms: 1.04x faster  |
| deepcopy               | 167 us      | 160 us: 1.04x faster   |
| float                  | 41.9 ms     | 40.2 ms: 1.04x faster  |
| xml_etree_generate     | 53.6 ms     | 51.5 ms: 1.04x faster  |
| sympy_str              | 164 ms      | 158 ms: 1.04x faster   |
| sqlglot_v2_transpile   | 970 us      | 933 us: 1.04x faster   |
| unpickle_pure_python   | 127 us      | 123 us: 1.04x faster   |
| go                     | 70.9 ms     | 68.4 ms: 1.04x faster  |
| nbody                  | 55.2 ms     | 53.3 ms: 1.04x faster  |
| sqlglot_v2_normalize   | 69.3 ms     | 66.9 ms: 1.04x faster  |
| sqlglot_v2_parse       | 766 us      | 740 us: 1.04x faster   |
| logging_simple         | 5.97 us     | 5.78 us: 1.03x faster  |
| richards               | 28.7 ms     | 27.8 ms: 1.03x faster  |
| pyflate                | 268 ms      | 260 ms: 1.03x faster   |
| pycparser              | 686 ms      | 664 ms: 1.03x faster   |
| richards_super         | 33.1 ms     | 32.2 ms: 1.03x faster  |
| chaos                  | 36.9 ms     | 35.9 ms: 1.03x faster  |
| sqlglot_v2_optimize    | 33.0 ms     | 32.2 ms: 1.03x faster  |
| mako                   | 6.28 ms     | 6.12 ms: 1.03x faster  |
| logging_format         | 6.50 us     | 6.34 us: 1.03x faster  |
| docutils               | 1.67 sec    | 1.63 sec: 1.03x faster |
| async_tree_io          | 384 ms      | 375 ms: 1.02x faster   |
| deepcopy_reduce        | 1.70 us     | 1.66 us: 1.02x faster  |
| json_loads             | 14.7 us     | 14.5 us: 1.02x faster  |
| hexiom                 | 3.54 ms     | 3.47 ms: 1.02x faster  |
| dulwich_log            | 40.2 ms     | 39.5 ms: 1.02x faster  |
| connected_components   | 326 ms      | 321 ms: 1.02x faster   |
| deltablue              | 1.88 ms     | 1.85 ms: 1.02x faster  |
| async_tree_io_tg       | 377 ms      | 371 ms: 1.02x faster   |
| gc_traversal           | 2.11 ms     | 2.07 ms: 1.02x faster  |
| comprehensions         | 9.87 us     | 9.73 us: 1.01x faster  |
| scimark_fft            | 154 ms      | 152 ms: 1.01x faster   |
| shortest_path          | 353 ms      | 348 ms: 1.01x faster   |
| xml_etree_iterparse    | 61.2 ms     | 60.4 ms: 1.01x faster  |
| sphinx                 | 645 ms      | 638 ms: 1.01x faster   |
| meteor_contest         | 70.2 ms     | 69.5 ms: 1.01x faster  |
| json_dumps             | 6.55 ms     | 6.48 ms: 1.01x faster  |
| xml_etree_process      | 37.0 ms     | 36.7 ms: 1.01x faster  |
| bpe_tokeniser          | 2.72 sec    | 2.71 sec: 1.00x faster |
| pidigits               | 145 ms      | 146 ms: 1.01x slower   |
| pathlib                | 24.1 ms     | 24.3 ms: 1.01x slower  |
| pickle_pure_python     | 199 us      | 201 us: 1.01x slower   |
| pprint_safe_repr       | 470 ms      | 478 ms: 1.02x slower   |
| async_generators       | 202 ms      | 206 ms: 1.02x slower   |
| 2to3                   | 212 ms      | 216 ms: 1.02x slower   |
| django_template        | 22.9 ms     | 23.4 ms: 1.02x slower  |
| deepcopy_memo          | 16.6 us     | 17.0 us: 1.03x slower  |
| coverage               | 48.2 ms     | 49.5 ms: 1.03x slower  |
| scimark_monte_carlo    | 36.0 ms     | 37.0 ms: 1.03x slower  |
| spectral_norm          | 49.4 ms     | 51.1 ms: 1.04x slower  |
| raytrace               | 160 ms      | 166 ms: 1.04x slower   |
| coroutines             | 11.9 ms     | 12.4 ms: 1.04x slower  |
| python_startup_no_site | 18.7 ms     | 19.6 ms: 1.05x slower  |
| python_startup         | 24.7 ms     | 26.0 ms: 1.05x slower  |
| asyncio_websockets     | 301 ms      | 317 ms: 1.05x slower   |
| fannkuch               | 223 ms      | 236 ms: 1.06x slower   |
| regex_v8               | 13.2 ms     | 14.1 ms: 1.06x slower  |
| scimark_lu             | 50.9 ms     | 54.4 ms: 1.07x slower  |
| logging_silent         | 49.4 ns     | 53.3 ns: 1.08x slower  |
| subparsers             | 40.7 ms     | 44.9 ms: 1.10x slower  |
| scimark_sor            | 61.1 ms     | 67.5 ms: 1.10x slower  |
| many_optionals         | 665 us      | 761 us: 1.14x slower   |
| Geometric mean         | (ref)       | 1.01x faster           |

Benchmark hidden because not significant (20): telco, nqueens, genshi_text, async_tree_cpu_io_mixed_tg, create_gc_cycles, async_tree_memoization, async_tree_cpu_io_mixed, xml_etree_parse, sqlite_synth, async_tree_none, tomli_loads, scimark_sparse_mat_mult, thrift, k_core, async_tree_memoization_tg, pylint, pprint_pformat, typing_runtime_protocols, json, async_tree_none_tg
Ignored benchmarks (2) of TC-PGO-Ex3.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown