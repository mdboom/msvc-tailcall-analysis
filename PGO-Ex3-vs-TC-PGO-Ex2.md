# Results vs. base

- fork: unknown
- ref: PGO-Ex3
- machine: unknown-unknown
- commit hash: 2ea4123
- commit date: 2025-03-12
- overall geometric mean: 1.089x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | PGO-Ex3                |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 227 ms: 1.05x slower   |
| docutils       | 1.63 sec   | 1.71 sec: 1.05x slower |
| html5lib       | 36.1 ms    | 40.5 ms: 1.12x slower  |
| sphinx         | 638 ms     | 670 ms: 1.05x slower   |
| Geometric mean | (ref)      | 1.07x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | PGO-Ex3               |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 317 ms     | 311 ms: 1.02x faster  |
| async_tree_cpu_io_mixed    | 329 ms     | 340 ms: 1.03x slower  |
| async_tree_memoization_tg  | 209 ms     | 219 ms: 1.05x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 344 ms: 1.05x slower  |
| coroutines                 | 12.4 ms    | 13.1 ms: 1.06x slower |
| async_generators           | 206 ms     | 219 ms: 1.06x slower  |
| async_tree_memoization     | 205 ms     | 223 ms: 1.09x slower  |
| async_tree_none            | 170 ms     | 186 ms: 1.09x slower  |
| async_tree_none_tg         | 159 ms     | 176 ms: 1.10x slower  |
| async_tree_io_tg           | 371 ms     | 410 ms: 1.11x slower  |
| async_tree_io              | 375 ms     | 417 ms: 1.11x slower  |
| Geometric mean             | (ref)      | 1.07x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | PGO-Ex3               |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 148 ms: 1.02x slower  |
| float          | 40.2 ms    | 44.2 ms: 1.10x slower |
| nbody          | 53.3 ms    | 78.3 ms: 1.47x slower |
| Geometric mean | (ref)      | 1.18x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | PGO-Ex3               |
|----------------|:----------:|:---------------------:|
| regex_v8       | 14.1 ms    | 13.8 ms: 1.02x faster |
| regex_dna      | 115 ms     | 116 ms: 1.01x slower  |
| regex_effbot   | 1.40 ms    | 1.46 ms: 1.04x slower |
| regex_compile  | 74.8 ms    | 86.1 ms: 1.15x slower |
| Geometric mean | (ref)      | 1.04x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | PGO-Ex3                |
|----------------------|:----------:|:----------------------:|
| json_dumps           | 6.48 ms    | 6.69 ms: 1.03x slower  |
| xml_etree_iterparse  | 60.4 ms    | 62.3 ms: 1.03x slower  |
| json_loads           | 14.5 us    | 15.3 us: 1.06x slower  |
| pickle_pure_python   | 201 us     | 217 us: 1.08x slower   |
| xml_etree_process    | 36.7 ms    | 39.7 ms: 1.08x slower  |
| xml_etree_generate   | 51.5 ms    | 56.8 ms: 1.10x slower  |
| unpickle_pure_python | 123 us     | 147 us: 1.20x slower   |
| tomli_loads          | 1.17 sec   | 1.44 sec: 1.22x slower |
| Geometric mean       | (ref)      | 1.09x slower           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | PGO-Ex3               |
|------------------------|:----------:|:---------------------:|
| python_startup         | 26.0 ms    | 24.5 ms: 1.06x faster |
| python_startup_no_site | 19.6 ms    | 18.7 ms: 1.05x faster |
| Geometric mean         | (ref)      | 1.05x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | PGO-Ex3               |
|-----------------|:----------:|:---------------------:|
| mako            | 6.12 ms    | 6.50 ms: 1.06x slower |
| django_template | 23.4 ms    | 25.5 ms: 1.09x slower |
| genshi_text     | 14.2 ms    | 15.8 ms: 1.12x slower |
| genshi_xml      | 30.7 ms    | 35.0 ms: 1.14x slower |
| Geometric mean  | (ref)      | 1.10x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | PGO-Ex3                |
|----------------------------|:----------:|:----------------------:|
| many_optionals             | 761 us     | 695 us: 1.10x faster   |
| subparsers                 | 44.9 ms    | 41.0 ms: 1.09x faster  |
| python_startup             | 26.0 ms    | 24.5 ms: 1.06x faster  |
| python_startup_no_site     | 19.6 ms    | 18.7 ms: 1.05x faster  |
| regex_v8                   | 14.1 ms    | 13.8 ms: 1.02x faster  |
| asyncio_websockets         | 317 ms     | 311 ms: 1.02x faster   |
| create_gc_cycles           | 1.27 ms    | 1.25 ms: 1.01x faster  |
| regex_dna                  | 115 ms     | 116 ms: 1.01x slower   |
| connected_components       | 321 ms     | 324 ms: 1.01x slower   |
| pathlib                    | 24.3 ms    | 24.6 ms: 1.01x slower  |
| pidigits                   | 146 ms     | 148 ms: 1.02x slower   |
| shortest_path              | 348 ms     | 354 ms: 1.02x slower   |
| json_dumps                 | 6.48 ms    | 6.69 ms: 1.03x slower  |
| xml_etree_iterparse        | 60.4 ms    | 62.3 ms: 1.03x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 340 ms: 1.03x slower   |
| regex_effbot               | 1.40 ms    | 1.46 ms: 1.04x slower  |
| telco                      | 4.54 ms    | 4.75 ms: 1.05x slower  |
| 2to3                       | 216 ms     | 227 ms: 1.05x slower   |
| async_tree_memoization_tg  | 209 ms     | 219 ms: 1.05x slower   |
| pylint                     | 199 ms     | 208 ms: 1.05x slower   |
| docutils                   | 1.63 sec   | 1.71 sec: 1.05x slower |
| sphinx                     | 638 ms     | 670 ms: 1.05x slower   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 344 ms: 1.05x slower   |
| coroutines                 | 12.4 ms    | 13.1 ms: 1.06x slower  |
| json_loads                 | 14.5 us    | 15.3 us: 1.06x slower  |
| json                       | 2.98 ms    | 3.16 ms: 1.06x slower  |
| async_generators           | 206 ms     | 219 ms: 1.06x slower   |
| mako                       | 6.12 ms    | 6.50 ms: 1.06x slower  |
| meteor_contest             | 69.5 ms    | 74.3 ms: 1.07x slower  |
| logging_silent             | 53.3 ns    | 57.0 ns: 1.07x slower  |
| typing_runtime_protocols   | 98.9 us    | 106 us: 1.07x slower   |
| dulwich_log                | 39.5 ms    | 42.4 ms: 1.07x slower  |
| pickle_pure_python         | 201 us     | 217 us: 1.08x slower   |
| xml_etree_process          | 36.7 ms    | 39.7 ms: 1.08x slower  |
| bpe_tokeniser              | 2.71 sec   | 2.93 sec: 1.08x slower |
| thrift                     | 482 us     | 522 us: 1.08x slower   |
| async_tree_memoization     | 205 ms     | 223 ms: 1.09x slower   |
| django_template            | 23.4 ms    | 25.5 ms: 1.09x slower  |
| async_tree_none            | 170 ms     | 186 ms: 1.09x slower   |
| float                      | 40.2 ms    | 44.2 ms: 1.10x slower  |
| async_tree_none_tg         | 159 ms     | 176 ms: 1.10x slower   |
| xml_etree_generate         | 51.5 ms    | 56.8 ms: 1.10x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 35.6 ms: 1.11x slower  |
| sympy_sum                  | 82.1 ms    | 90.8 ms: 1.11x slower  |
| async_tree_io_tg           | 371 ms     | 410 ms: 1.11x slower   |
| async_tree_io              | 375 ms     | 417 ms: 1.11x slower   |
| pprint_safe_repr           | 478 ms     | 532 ms: 1.11x slower   |
| sympy_integrate            | 12.2 ms    | 13.6 ms: 1.12x slower  |
| fannkuch                   | 236 ms     | 263 ms: 1.12x slower   |
| genshi_text                | 14.2 ms    | 15.8 ms: 1.12x slower  |
| sympy_str                  | 158 ms     | 177 ms: 1.12x slower   |
| pycparser                  | 664 ms     | 745 ms: 1.12x slower   |
| html5lib                   | 36.1 ms    | 40.5 ms: 1.12x slower  |
| logging_format             | 6.34 us    | 7.11 us: 1.12x slower  |
| deepcopy_memo              | 17.0 us    | 19.1 us: 1.12x slower  |
| scimark_lu                 | 54.4 ms    | 61.1 ms: 1.12x slower  |
| pprint_pformat             | 968 ms     | 1.09 sec: 1.12x slower |
| logging_simple             | 5.78 us    | 6.53 us: 1.13x slower  |
| deepcopy_reduce            | 1.66 us    | 1.88 us: 1.13x slower  |
| sympy_expand               | 269 ms     | 305 ms: 1.13x slower   |
| spectral_norm              | 51.1 ms    | 58.1 ms: 1.14x slower  |
| genshi_xml                 | 30.7 ms    | 35.0 ms: 1.14x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 76.3 ms: 1.14x slower  |
| comprehensions             | 9.73 us    | 11.2 us: 1.15x slower  |
| regex_compile              | 74.8 ms    | 86.1 ms: 1.15x slower  |
| nqueens                    | 54.0 ms    | 62.2 ms: 1.15x slower  |
| pyflate                    | 260 ms     | 300 ms: 1.15x slower   |
| deepcopy                   | 160 us     | 185 us: 1.16x slower   |
| mdp                        | 1.40 sec   | 1.62 sec: 1.16x slower |
| scimark_sparse_mat_mult    | 2.26 ms    | 2.63 ms: 1.16x slower  |
| crypto_pyaes               | 41.6 ms    | 48.6 ms: 1.17x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.09 ms: 1.17x slower  |
| chaos                      | 35.9 ms    | 42.2 ms: 1.18x slower  |
| sqlglot_v2_parse           | 740 us     | 870 us: 1.18x slower   |
| deltablue                  | 1.85 ms    | 2.18 ms: 1.18x slower  |
| unpickle_pure_python       | 123 us     | 147 us: 1.20x slower   |
| raytrace                   | 166 ms     | 201 ms: 1.21x slower   |
| tomli_loads                | 1.17 sec   | 1.44 sec: 1.22x slower |
| scimark_monte_carlo        | 37.0 ms    | 45.3 ms: 1.22x slower  |
| go                         | 68.4 ms    | 84.1 ms: 1.23x slower  |
| hexiom                     | 3.47 ms    | 4.28 ms: 1.23x slower  |
| scimark_fft                | 152 ms     | 187 ms: 1.23x slower   |
| richards                   | 27.8 ms    | 34.5 ms: 1.24x slower  |
| richards_super             | 32.2 ms    | 39.9 ms: 1.24x slower  |
| scimark_sor                | 67.5 ms    | 84.2 ms: 1.25x slower  |
| generators                 | 14.8 ms    | 20.0 ms: 1.35x slower  |
| nbody                      | 53.3 ms    | 78.3 ms: 1.47x slower  |
| Geometric mean             | (ref)      | 1.10x slower           |

Benchmark hidden because not significant (5): coverage, gc_traversal, xml_etree_parse, sqlite_synth, k_core
Ignored benchmarks (2) of TC-PGO-Ex2.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown