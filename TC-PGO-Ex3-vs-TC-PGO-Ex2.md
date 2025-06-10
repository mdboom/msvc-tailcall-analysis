# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3             |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 204 ms: 1.06x faster   |
| docutils       | 1.63 sec   | 1.58 sec: 1.03x faster |
| html5lib       | 36.1 ms    | 35.5 ms: 1.02x faster  |
| sphinx         | 638 ms     | 615 ms: 1.04x faster   |
| Geometric mean | (ref)      | 1.04x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | TC-PGO-Ex2 | TC-PGO-Ex3            |
|---------------------------|:----------:|:---------------------:|
| coroutines                | 12.4 ms    | 10.8 ms: 1.15x faster |
| async_tree_none           | 170 ms     | 157 ms: 1.08x faster  |
| async_tree_none_tg        | 159 ms     | 150 ms: 1.06x faster  |
| async_tree_io             | 375 ms     | 353 ms: 1.06x faster  |
| async_tree_memoization    | 205 ms     | 196 ms: 1.04x faster  |
| async_tree_io_tg          | 371 ms     | 356 ms: 1.04x faster  |
| asyncio_websockets        | 317 ms     | 304 ms: 1.04x faster  |
| async_tree_memoization_tg | 209 ms     | 201 ms: 1.04x faster  |
| async_generators          | 206 ms     | 199 ms: 1.04x faster  |
| async_tree_cpu_io_mixed   | 329 ms     | 327 ms: 1.01x faster  |
| Geometric mean            | (ref)      | 1.05x faster          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:----------:|:---------------------:|
| nbody          | 53.3 ms    | 45.7 ms: 1.16x faster |
| float          | 40.2 ms    | 37.1 ms: 1.08x faster |
| pidigits       | 146 ms     | 145 ms: 1.01x faster  |
| Geometric mean | (ref)      | 1.08x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TC-PGO-Ex3            |
|----------------|:----------:|:---------------------:|
| regex_compile  | 74.8 ms    | 70.7 ms: 1.06x faster |
| regex_effbot   | 1.40 ms    | 1.45 ms: 1.04x slower |
| regex_dna      | 115 ms     | 121 ms: 1.05x slower  |
| Geometric mean | (ref)      | 1.01x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TC-PGO-Ex3             |
|----------------------|:----------:|:----------------------:|
| tomli_loads          | 1.17 sec   | 1.03 sec: 1.14x faster |
| unpickle_pure_python | 123 us     | 110 us: 1.12x faster   |
| pickle_pure_python   | 201 us     | 184 us: 1.09x faster   |
| xml_etree_process    | 36.7 ms    | 33.8 ms: 1.09x faster  |
| json_dumps           | 6.48 ms    | 6.19 ms: 1.05x faster  |
| xml_etree_generate   | 51.5 ms    | 49.4 ms: 1.04x faster  |
| xml_etree_iterparse  | 60.4 ms    | 59.5 ms: 1.01x faster  |
| json_loads           | 14.5 us    | 14.8 us: 1.02x slower  |
| Geometric mean       | (ref)      | 1.06x faster           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TC-PGO-Ex3            |
|------------------------|:----------:|:---------------------:|
| python_startup         | 26.0 ms    | 24.7 ms: 1.05x faster |
| python_startup_no_site | 19.6 ms    | 18.7 ms: 1.05x faster |
| Geometric mean         | (ref)      | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TC-PGO-Ex3            |
|-----------------|:----------:|:---------------------:|
| genshi_text     | 14.2 ms    | 12.3 ms: 1.15x faster |
| django_template | 23.4 ms    | 20.9 ms: 1.12x faster |
| mako            | 6.12 ms    | 5.80 ms: 1.06x faster |
| genshi_xml      | 30.7 ms    | 29.5 ms: 1.04x faster |
| Geometric mean  | (ref)      | 1.09x faster          |

All benchmarks:
===============

| Benchmark                 | TC-PGO-Ex2 | TC-PGO-Ex3             |
|---------------------------|:----------:|:----------------------:|
| scimark_sor               | 67.5 ms    | 51.1 ms: 1.32x faster  |
| spectral_norm             | 51.1 ms    | 40.9 ms: 1.25x faster  |
| scimark_lu                | 54.4 ms    | 44.3 ms: 1.23x faster  |
| logging_silent            | 53.3 ns    | 44.1 ns: 1.21x faster  |
| scimark_monte_carlo       | 37.0 ms    | 31.5 ms: 1.17x faster  |
| nbody                     | 53.3 ms    | 45.7 ms: 1.16x faster  |
| fannkuch                  | 236 ms     | 203 ms: 1.16x faster   |
| hexiom                    | 3.47 ms    | 3.00 ms: 1.16x faster  |
| deepcopy_memo             | 17.0 us    | 14.7 us: 1.16x faster  |
| many_optionals            | 761 us     | 659 us: 1.16x faster   |
| coroutines                | 12.4 ms    | 10.8 ms: 1.15x faster  |
| genshi_text               | 14.2 ms    | 12.3 ms: 1.15x faster  |
| chaos                     | 35.9 ms    | 31.3 ms: 1.15x faster  |
| raytrace                  | 166 ms     | 145 ms: 1.14x faster   |
| tomli_loads               | 1.17 sec   | 1.03 sec: 1.14x faster |
| pprint_pformat            | 968 ms     | 853 ms: 1.14x faster   |
| deltablue                 | 1.85 ms    | 1.64 ms: 1.13x faster  |
| comprehensions            | 9.73 us    | 8.65 us: 1.13x faster  |
| go                        | 68.4 ms    | 61.0 ms: 1.12x faster  |
| scimark_sparse_mat_mult   | 2.26 ms    | 2.02 ms: 1.12x faster  |
| unpickle_pure_python      | 123 us     | 110 us: 1.12x faster   |
| django_template           | 23.4 ms    | 20.9 ms: 1.12x faster  |
| pprint_safe_repr          | 478 ms     | 429 ms: 1.11x faster   |
| subparsers                | 44.9 ms    | 40.6 ms: 1.11x faster  |
| typing_runtime_protocols  | 98.9 us    | 89.7 us: 1.10x faster  |
| pyflate                   | 260 ms     | 236 ms: 1.10x faster   |
| deepcopy_reduce           | 1.66 us    | 1.51 us: 1.10x faster  |
| pickle_pure_python        | 201 us     | 184 us: 1.09x faster   |
| richards_super            | 32.2 ms    | 29.4 ms: 1.09x faster  |
| richards                  | 27.8 ms    | 25.5 ms: 1.09x faster  |
| deepcopy                  | 160 us     | 147 us: 1.09x faster   |
| nqueens                   | 54.0 ms    | 49.7 ms: 1.09x faster  |
| xml_etree_process         | 36.7 ms    | 33.8 ms: 1.09x faster  |
| float                     | 40.2 ms    | 37.1 ms: 1.08x faster  |
| scimark_fft               | 152 ms     | 140 ms: 1.08x faster   |
| async_tree_none           | 170 ms     | 157 ms: 1.08x faster   |
| bpe_tokeniser             | 2.71 sec   | 2.52 sec: 1.07x faster |
| logging_format            | 6.34 us    | 5.90 us: 1.07x faster  |
| coverage                  | 49.5 ms    | 46.2 ms: 1.07x faster  |
| sqlglot_v2_normalize      | 66.9 ms    | 62.6 ms: 1.07x faster  |
| logging_simple            | 5.78 us    | 5.42 us: 1.07x faster  |
| sqlglot_v2_parse          | 740 us     | 695 us: 1.06x faster   |
| async_tree_none_tg        | 159 ms     | 150 ms: 1.06x faster   |
| async_tree_io             | 375 ms     | 353 ms: 1.06x faster   |
| 2to3                      | 216 ms     | 204 ms: 1.06x faster   |
| regex_compile             | 74.8 ms    | 70.7 ms: 1.06x faster  |
| mako                      | 6.12 ms    | 5.80 ms: 1.06x faster  |
| sqlglot_v2_optimize       | 32.2 ms    | 30.5 ms: 1.06x faster  |
| python_startup            | 26.0 ms    | 24.7 ms: 1.05x faster  |
| json_dumps                | 6.48 ms    | 6.19 ms: 1.05x faster  |
| python_startup_no_site    | 19.6 ms    | 18.7 ms: 1.05x faster  |
| thrift                    | 482 us     | 461 us: 1.04x faster   |
| sqlglot_v2_transpile      | 933 us     | 894 us: 1.04x faster   |
| async_tree_memoization    | 205 ms     | 196 ms: 1.04x faster   |
| meteor_contest            | 69.5 ms    | 66.6 ms: 1.04x faster  |
| async_tree_io_tg          | 371 ms     | 356 ms: 1.04x faster   |
| asyncio_websockets        | 317 ms     | 304 ms: 1.04x faster   |
| genshi_xml                | 30.7 ms    | 29.5 ms: 1.04x faster  |
| generators                | 14.8 ms    | 14.2 ms: 1.04x faster  |
| xml_etree_generate        | 51.5 ms    | 49.4 ms: 1.04x faster  |
| async_tree_memoization_tg | 209 ms     | 201 ms: 1.04x faster   |
| async_generators          | 206 ms     | 199 ms: 1.04x faster   |
| sphinx                    | 638 ms     | 615 ms: 1.04x faster   |
| pycparser                 | 664 ms     | 642 ms: 1.03x faster   |
| pylint                    | 199 ms     | 193 ms: 1.03x faster   |
| pathlib                   | 24.3 ms    | 23.6 ms: 1.03x faster  |
| crypto_pyaes              | 41.6 ms    | 40.4 ms: 1.03x faster  |
| docutils                  | 1.63 sec   | 1.58 sec: 1.03x faster |
| sympy_str                 | 158 ms     | 153 ms: 1.03x faster   |
| sympy_expand              | 269 ms     | 263 ms: 1.02x faster   |
| k_core                    | 1.71 sec   | 1.67 sec: 1.02x faster |
| telco                     | 4.54 ms    | 4.45 ms: 1.02x faster  |
| sympy_sum                 | 82.1 ms    | 80.7 ms: 1.02x faster  |
| sympy_integrate           | 12.2 ms    | 12.0 ms: 1.02x faster  |
| html5lib                  | 36.1 ms    | 35.5 ms: 1.02x faster  |
| xml_etree_iterparse       | 60.4 ms    | 59.5 ms: 1.01x faster  |
| dulwich_log               | 39.5 ms    | 39.1 ms: 1.01x faster  |
| json                      | 2.98 ms    | 2.95 ms: 1.01x faster  |
| async_tree_cpu_io_mixed   | 329 ms     | 327 ms: 1.01x faster   |
| pidigits                  | 146 ms     | 145 ms: 1.01x faster   |
| mdp                       | 1.40 sec   | 1.41 sec: 1.01x slower |
| json_loads                | 14.5 us    | 14.8 us: 1.02x slower  |
| regex_effbot              | 1.40 ms    | 1.45 ms: 1.04x slower  |
| regex_dna                 | 115 ms     | 121 ms: 1.05x slower   |
| Geometric mean            | (ref)      | 1.07x faster           |

Benchmark hidden because not significant (8): regex_v8, async_tree_cpu_io_mixed_tg, shortest_path, create_gc_cycles, connected_components, sqlite_synth, xml_etree_parse, gc_traversal
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown