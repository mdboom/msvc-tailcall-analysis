# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex3
- machine: unknown-unknown
- commit hash: 8ccca92
- commit date: 2025-03-26
- overall geometric mean: 1.008x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3            |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 212 ms: 1.02x faster   |
| docutils       | 1.63 sec   | 1.67 sec: 1.03x slower |
| html5lib       | 36.1 ms    | 37.9 ms: 1.05x slower  |
| sphinx         | 638 ms     | 645 ms: 1.01x slower   |
| Geometric mean | (ref)      | 1.02x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|--------------------|:----------:|:---------------------:|
| asyncio_websockets | 317 ms     | 301 ms: 1.05x faster  |
| coroutines         | 12.4 ms    | 11.9 ms: 1.04x faster |
| async_generators   | 206 ms     | 202 ms: 1.02x faster  |
| async_tree_io_tg   | 371 ms     | 377 ms: 1.02x slower  |
| async_tree_io      | 375 ms     | 384 ms: 1.02x slower  |
| Geometric mean     | (ref)      | 1.01x faster          |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 145 ms: 1.01x faster  |
| nbody          | 53.3 ms    | 55.2 ms: 1.04x slower |
| float          | 40.2 ms    | 41.9 ms: 1.04x slower |
| Geometric mean | (ref)      | 1.02x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------|:----------:|:---------------------:|
| regex_v8       | 14.1 ms    | 13.2 ms: 1.06x faster |
| regex_compile  | 74.8 ms    | 78.1 ms: 1.04x slower |
| regex_dna      | 115 ms     | 120 ms: 1.05x slower  |
| regex_effbot   | 1.40 ms    | 1.46 ms: 1.05x slower |
| Geometric mean | (ref)      | 1.02x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|----------------------|:----------:|:---------------------:|
| pickle_pure_python   | 201 us     | 199 us: 1.01x faster  |
| xml_etree_process    | 36.7 ms    | 37.0 ms: 1.01x slower |
| json_dumps           | 6.48 ms    | 6.55 ms: 1.01x slower |
| xml_etree_iterparse  | 60.4 ms    | 61.2 ms: 1.01x slower |
| json_loads           | 14.5 us    | 14.7 us: 1.02x slower |
| unpickle_pure_python | 123 us     | 127 us: 1.04x slower  |
| xml_etree_generate   | 51.5 ms    | 53.6 ms: 1.04x slower |
| Geometric mean       | (ref)      | 1.01x slower          |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|------------------------|:----------:|:---------------------:|
| python_startup         | 26.0 ms    | 24.7 ms: 1.05x faster |
| python_startup_no_site | 19.6 ms    | 18.7 ms: 1.05x faster |
| Geometric mean         | (ref)      | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TCO-PGO-Ex3           |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 22.9 ms: 1.02x faster |
| mako            | 6.12 ms    | 6.28 ms: 1.03x slower |
| genshi_xml      | 30.7 ms    | 32.8 ms: 1.07x slower |
| Geometric mean  | (ref)      | 1.02x slower          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | TC-PGO-Ex2 | TCO-PGO-Ex3            |
|------------------------|:----------:|:----------------------:|
| many_optionals         | 761 us     | 665 us: 1.14x faster   |
| scimark_sor            | 67.5 ms    | 61.1 ms: 1.10x faster  |
| subparsers             | 44.9 ms    | 40.7 ms: 1.10x faster  |
| logging_silent         | 53.3 ns    | 49.4 ns: 1.08x faster  |
| scimark_lu             | 54.4 ms    | 50.9 ms: 1.07x faster  |
| regex_v8               | 14.1 ms    | 13.2 ms: 1.06x faster  |
| fannkuch               | 236 ms     | 223 ms: 1.06x faster   |
| asyncio_websockets     | 317 ms     | 301 ms: 1.05x faster   |
| python_startup         | 26.0 ms    | 24.7 ms: 1.05x faster  |
| python_startup_no_site | 19.6 ms    | 18.7 ms: 1.05x faster  |
| coroutines             | 12.4 ms    | 11.9 ms: 1.04x faster  |
| raytrace               | 166 ms     | 160 ms: 1.04x faster   |
| spectral_norm          | 51.1 ms    | 49.4 ms: 1.04x faster  |
| scimark_monte_carlo    | 37.0 ms    | 36.0 ms: 1.03x faster  |
| coverage               | 49.5 ms    | 48.2 ms: 1.03x faster  |
| deepcopy_memo          | 17.0 us    | 16.6 us: 1.03x faster  |
| django_template        | 23.4 ms    | 22.9 ms: 1.02x faster  |
| 2to3                   | 216 ms     | 212 ms: 1.02x faster   |
| async_generators       | 206 ms     | 202 ms: 1.02x faster   |
| pprint_safe_repr       | 478 ms     | 470 ms: 1.02x faster   |
| pickle_pure_python     | 201 us     | 199 us: 1.01x faster   |
| pathlib                | 24.3 ms    | 24.1 ms: 1.01x faster  |
| pidigits               | 146 ms     | 145 ms: 1.01x faster   |
| bpe_tokeniser          | 2.71 sec   | 2.72 sec: 1.00x slower |
| xml_etree_process      | 36.7 ms    | 37.0 ms: 1.01x slower  |
| json_dumps             | 6.48 ms    | 6.55 ms: 1.01x slower  |
| meteor_contest         | 69.5 ms    | 70.2 ms: 1.01x slower  |
| sphinx                 | 638 ms     | 645 ms: 1.01x slower   |
| xml_etree_iterparse    | 60.4 ms    | 61.2 ms: 1.01x slower  |
| shortest_path          | 348 ms     | 353 ms: 1.01x slower   |
| scimark_fft            | 152 ms     | 154 ms: 1.01x slower   |
| comprehensions         | 9.73 us    | 9.87 us: 1.01x slower  |
| gc_traversal           | 2.07 ms    | 2.11 ms: 1.02x slower  |
| async_tree_io_tg       | 371 ms     | 377 ms: 1.02x slower   |
| deltablue              | 1.85 ms    | 1.88 ms: 1.02x slower  |
| connected_components   | 321 ms     | 326 ms: 1.02x slower   |
| dulwich_log            | 39.5 ms    | 40.2 ms: 1.02x slower  |
| hexiom                 | 3.47 ms    | 3.54 ms: 1.02x slower  |
| json_loads             | 14.5 us    | 14.7 us: 1.02x slower  |
| deepcopy_reduce        | 1.66 us    | 1.70 us: 1.02x slower  |
| async_tree_io          | 375 ms     | 384 ms: 1.02x slower   |
| docutils               | 1.63 sec   | 1.67 sec: 1.03x slower |
| logging_format         | 6.34 us    | 6.50 us: 1.03x slower  |
| mako                   | 6.12 ms    | 6.28 ms: 1.03x slower  |
| sqlglot_v2_optimize    | 32.2 ms    | 33.0 ms: 1.03x slower  |
| chaos                  | 35.9 ms    | 36.9 ms: 1.03x slower  |
| richards_super         | 32.2 ms    | 33.1 ms: 1.03x slower  |
| pycparser              | 664 ms     | 686 ms: 1.03x slower   |
| pyflate                | 260 ms     | 268 ms: 1.03x slower   |
| richards               | 27.8 ms    | 28.7 ms: 1.03x slower  |
| logging_simple         | 5.78 us    | 5.97 us: 1.03x slower  |
| sqlglot_v2_parse       | 740 us     | 766 us: 1.04x slower   |
| sqlglot_v2_normalize   | 66.9 ms    | 69.3 ms: 1.04x slower  |
| nbody                  | 53.3 ms    | 55.2 ms: 1.04x slower  |
| go                     | 68.4 ms    | 70.9 ms: 1.04x slower  |
| unpickle_pure_python   | 123 us     | 127 us: 1.04x slower   |
| sqlglot_v2_transpile   | 933 us     | 970 us: 1.04x slower   |
| sympy_str              | 158 ms     | 164 ms: 1.04x slower   |
| xml_etree_generate     | 51.5 ms    | 53.6 ms: 1.04x slower  |
| float                  | 40.2 ms    | 41.9 ms: 1.04x slower  |
| deepcopy               | 160 us     | 167 us: 1.04x slower   |
| regex_compile          | 74.8 ms    | 78.1 ms: 1.04x slower  |
| regex_dna              | 115 ms     | 120 ms: 1.05x slower   |
| regex_effbot           | 1.40 ms    | 1.46 ms: 1.05x slower  |
| sympy_expand           | 269 ms     | 282 ms: 1.05x slower   |
| sympy_sum              | 82.1 ms    | 86.3 ms: 1.05x slower  |
| sympy_integrate        | 12.2 ms    | 12.8 ms: 1.05x slower  |
| html5lib               | 36.1 ms    | 37.9 ms: 1.05x slower  |
| genshi_xml             | 30.7 ms    | 32.8 ms: 1.07x slower  |
| generators             | 14.8 ms    | 16.5 ms: 1.11x slower  |
| crypto_pyaes           | 41.6 ms    | 47.4 ms: 1.14x slower  |
| mdp                    | 1.40 sec   | 1.62 sec: 1.16x slower |
| Geometric mean         | (ref)      | 1.01x slower           |

Benchmark hidden because not significant (20): async_tree_none_tg, json, typing_runtime_protocols, pprint_pformat, pylint, async_tree_memoization_tg, k_core, thrift, scimark_sparse_mat_mult, tomli_loads, async_tree_none, sqlite_synth, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_memoization, create_gc_cycles, async_tree_cpu_io_mixed_tg, genshi_text, nqueens, telco
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown