# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.063x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2             |
|----------------|:----------:|:----------------------:|
| 2to3           | 204 ms     | 216 ms: 1.06x slower   |
| docutils       | 1.58 sec   | 1.63 sec: 1.03x slower |
| html5lib       | 35.5 ms    | 36.1 ms: 1.02x slower  |
| sphinx         | 615 ms     | 638 ms: 1.04x slower   |
| Geometric mean | (ref)      | 1.04x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | TC-PGO-Ex3 | TC-PGO-Ex2            |
|---------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed   | 327 ms     | 329 ms: 1.01x slower  |
| async_generators          | 199 ms     | 206 ms: 1.04x slower  |
| async_tree_memoization_tg | 201 ms     | 209 ms: 1.04x slower  |
| asyncio_websockets        | 304 ms     | 317 ms: 1.04x slower  |
| async_tree_io_tg          | 356 ms     | 371 ms: 1.04x slower  |
| async_tree_memoization    | 196 ms     | 205 ms: 1.04x slower  |
| async_tree_io             | 353 ms     | 375 ms: 1.06x slower  |
| async_tree_none_tg        | 150 ms     | 159 ms: 1.06x slower  |
| async_tree_none           | 157 ms     | 170 ms: 1.08x slower  |
| coroutines                | 10.8 ms    | 12.4 ms: 1.15x slower |
| Geometric mean            | (ref)      | 1.05x slower          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:----------:|:---------------------:|
| pidigits       | 145 ms     | 146 ms: 1.01x slower  |
| float          | 37.1 ms    | 40.2 ms: 1.08x slower |
| nbody          | 45.7 ms    | 53.3 ms: 1.16x slower |
| Geometric mean | (ref)      | 1.08x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex3 | TC-PGO-Ex2            |
|----------------|:----------:|:---------------------:|
| regex_dna      | 121 ms     | 115 ms: 1.05x faster  |
| regex_effbot   | 1.45 ms    | 1.40 ms: 1.04x faster |
| regex_compile  | 70.7 ms    | 74.8 ms: 1.06x slower |
| Geometric mean | (ref)      | 1.01x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex3 | TC-PGO-Ex2             |
|----------------------|:----------:|:----------------------:|
| json_loads           | 14.8 us    | 14.5 us: 1.02x faster  |
| xml_etree_iterparse  | 59.5 ms    | 60.4 ms: 1.01x slower  |
| xml_etree_generate   | 49.4 ms    | 51.5 ms: 1.04x slower  |
| json_dumps           | 6.19 ms    | 6.48 ms: 1.05x slower  |
| xml_etree_process    | 33.8 ms    | 36.7 ms: 1.09x slower  |
| pickle_pure_python   | 184 us     | 201 us: 1.09x slower   |
| unpickle_pure_python | 110 us     | 123 us: 1.12x slower   |
| tomli_loads          | 1.03 sec   | 1.17 sec: 1.14x slower |
| Geometric mean       | (ref)      | 1.06x slower           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex3 | TC-PGO-Ex2            |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 18.7 ms    | 19.6 ms: 1.05x slower |
| python_startup         | 24.7 ms    | 26.0 ms: 1.05x slower |
| Geometric mean         | (ref)      | 1.05x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex3 | TC-PGO-Ex2            |
|-----------------|:----------:|:---------------------:|
| genshi_xml      | 29.5 ms    | 30.7 ms: 1.04x slower |
| mako            | 5.80 ms    | 6.12 ms: 1.06x slower |
| django_template | 20.9 ms    | 23.4 ms: 1.12x slower |
| genshi_text     | 12.3 ms    | 14.2 ms: 1.15x slower |
| Geometric mean  | (ref)      | 1.09x slower          |

All benchmarks:
===============

| Benchmark                 | TC-PGO-Ex3 | TC-PGO-Ex2             |
|---------------------------|:----------:|:----------------------:|
| regex_dna                 | 121 ms     | 115 ms: 1.05x faster   |
| regex_effbot              | 1.45 ms    | 1.40 ms: 1.04x faster  |
| json_loads                | 14.8 us    | 14.5 us: 1.02x faster  |
| mdp                       | 1.41 sec   | 1.40 sec: 1.01x faster |
| pidigits                  | 145 ms     | 146 ms: 1.01x slower   |
| async_tree_cpu_io_mixed   | 327 ms     | 329 ms: 1.01x slower   |
| json                      | 2.95 ms    | 2.98 ms: 1.01x slower  |
| dulwich_log               | 39.1 ms    | 39.5 ms: 1.01x slower  |
| xml_etree_iterparse       | 59.5 ms    | 60.4 ms: 1.01x slower  |
| html5lib                  | 35.5 ms    | 36.1 ms: 1.02x slower  |
| sympy_integrate           | 12.0 ms    | 12.2 ms: 1.02x slower  |
| sympy_sum                 | 80.7 ms    | 82.1 ms: 1.02x slower  |
| telco                     | 4.45 ms    | 4.54 ms: 1.02x slower  |
| k_core                    | 1.67 sec   | 1.71 sec: 1.02x slower |
| sympy_expand              | 263 ms     | 269 ms: 1.02x slower   |
| sympy_str                 | 153 ms     | 158 ms: 1.03x slower   |
| docutils                  | 1.58 sec   | 1.63 sec: 1.03x slower |
| crypto_pyaes              | 40.4 ms    | 41.6 ms: 1.03x slower  |
| pathlib                   | 23.6 ms    | 24.3 ms: 1.03x slower  |
| pylint                    | 193 ms     | 199 ms: 1.03x slower   |
| pycparser                 | 642 ms     | 664 ms: 1.03x slower   |
| sphinx                    | 615 ms     | 638 ms: 1.04x slower   |
| async_generators          | 199 ms     | 206 ms: 1.04x slower   |
| async_tree_memoization_tg | 201 ms     | 209 ms: 1.04x slower   |
| xml_etree_generate        | 49.4 ms    | 51.5 ms: 1.04x slower  |
| generators                | 14.2 ms    | 14.8 ms: 1.04x slower  |
| genshi_xml                | 29.5 ms    | 30.7 ms: 1.04x slower  |
| asyncio_websockets        | 304 ms     | 317 ms: 1.04x slower   |
| async_tree_io_tg          | 356 ms     | 371 ms: 1.04x slower   |
| meteor_contest            | 66.6 ms    | 69.5 ms: 1.04x slower  |
| async_tree_memoization    | 196 ms     | 205 ms: 1.04x slower   |
| sqlglot_v2_transpile      | 894 us     | 933 us: 1.04x slower   |
| thrift                    | 461 us     | 482 us: 1.04x slower   |
| python_startup_no_site    | 18.7 ms    | 19.6 ms: 1.05x slower  |
| json_dumps                | 6.19 ms    | 6.48 ms: 1.05x slower  |
| python_startup            | 24.7 ms    | 26.0 ms: 1.05x slower  |
| sqlglot_v2_optimize       | 30.5 ms    | 32.2 ms: 1.06x slower  |
| mako                      | 5.80 ms    | 6.12 ms: 1.06x slower  |
| regex_compile             | 70.7 ms    | 74.8 ms: 1.06x slower  |
| 2to3                      | 204 ms     | 216 ms: 1.06x slower   |
| async_tree_io             | 353 ms     | 375 ms: 1.06x slower   |
| async_tree_none_tg        | 150 ms     | 159 ms: 1.06x slower   |
| sqlglot_v2_parse          | 695 us     | 740 us: 1.06x slower   |
| logging_simple            | 5.42 us    | 5.78 us: 1.07x slower  |
| sqlglot_v2_normalize      | 62.6 ms    | 66.9 ms: 1.07x slower  |
| coverage                  | 46.2 ms    | 49.5 ms: 1.07x slower  |
| logging_format            | 5.90 us    | 6.34 us: 1.07x slower  |
| bpe_tokeniser             | 2.52 sec   | 2.71 sec: 1.07x slower |
| async_tree_none           | 157 ms     | 170 ms: 1.08x slower   |
| scimark_fft               | 140 ms     | 152 ms: 1.08x slower   |
| float                     | 37.1 ms    | 40.2 ms: 1.08x slower  |
| xml_etree_process         | 33.8 ms    | 36.7 ms: 1.09x slower  |
| nqueens                   | 49.7 ms    | 54.0 ms: 1.09x slower  |
| deepcopy                  | 147 us     | 160 us: 1.09x slower   |
| richards                  | 25.5 ms    | 27.8 ms: 1.09x slower  |
| richards_super            | 29.4 ms    | 32.2 ms: 1.09x slower  |
| pickle_pure_python        | 184 us     | 201 us: 1.09x slower   |
| deepcopy_reduce           | 1.51 us    | 1.66 us: 1.10x slower  |
| pyflate                   | 236 ms     | 260 ms: 1.10x slower   |
| typing_runtime_protocols  | 89.7 us    | 98.9 us: 1.10x slower  |
| subparsers                | 40.6 ms    | 44.9 ms: 1.11x slower  |
| pprint_safe_repr          | 429 ms     | 478 ms: 1.11x slower   |
| django_template           | 20.9 ms    | 23.4 ms: 1.12x slower  |
| unpickle_pure_python      | 110 us     | 123 us: 1.12x slower   |
| scimark_sparse_mat_mult   | 2.02 ms    | 2.26 ms: 1.12x slower  |
| go                        | 61.0 ms    | 68.4 ms: 1.12x slower  |
| comprehensions            | 8.65 us    | 9.73 us: 1.13x slower  |
| deltablue                 | 1.64 ms    | 1.85 ms: 1.13x slower  |
| pprint_pformat            | 853 ms     | 968 ms: 1.14x slower   |
| tomli_loads               | 1.03 sec   | 1.17 sec: 1.14x slower |
| raytrace                  | 145 ms     | 166 ms: 1.14x slower   |
| chaos                     | 31.3 ms    | 35.9 ms: 1.15x slower  |
| genshi_text               | 12.3 ms    | 14.2 ms: 1.15x slower  |
| coroutines                | 10.8 ms    | 12.4 ms: 1.15x slower  |
| many_optionals            | 659 us     | 761 us: 1.16x slower   |
| deepcopy_memo             | 14.7 us    | 17.0 us: 1.16x slower  |
| hexiom                    | 3.00 ms    | 3.47 ms: 1.16x slower  |
| fannkuch                  | 203 ms     | 236 ms: 1.16x slower   |
| nbody                     | 45.7 ms    | 53.3 ms: 1.16x slower  |
| scimark_monte_carlo       | 31.5 ms    | 37.0 ms: 1.17x slower  |
| logging_silent            | 44.1 ns    | 53.3 ns: 1.21x slower  |
| scimark_lu                | 44.3 ms    | 54.4 ms: 1.23x slower  |
| spectral_norm             | 40.9 ms    | 51.1 ms: 1.25x slower  |
| scimark_sor               | 51.1 ms    | 67.5 ms: 1.32x slower  |
| Geometric mean            | (ref)      | 1.07x slower           |

Benchmark hidden because not significant (8): gc_traversal, xml_etree_parse, sqlite_synth, connected_components, create_gc_cycles, shortest_path, async_tree_cpu_io_mixed_tg, regex_v8
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.063x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown