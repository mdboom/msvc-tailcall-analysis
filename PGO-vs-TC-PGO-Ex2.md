# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.089x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | PGO                    |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 227 ms: 1.05x slower   |
| docutils       | 1.63 sec   | 1.68 sec: 1.03x slower |
| html5lib       | 36.1 ms    | 40.8 ms: 1.13x slower  |
| sphinx         | 638 ms     | 658 ms: 1.03x slower   |
| Geometric mean | (ref)      | 1.06x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | PGO                   |
|----------------------------|:----------:|:---------------------:|
| async_tree_cpu_io_mixed    | 329 ms     | 339 ms: 1.03x slower  |
| async_tree_memoization_tg  | 209 ms     | 216 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 343 ms: 1.05x slower  |
| coroutines                 | 12.4 ms    | 13.5 ms: 1.08x slower |
| async_tree_memoization     | 205 ms     | 224 ms: 1.10x slower  |
| async_generators           | 206 ms     | 226 ms: 1.10x slower  |
| async_tree_none            | 170 ms     | 187 ms: 1.10x slower  |
| async_tree_io_tg           | 371 ms     | 410 ms: 1.10x slower  |
| async_tree_none_tg         | 159 ms     | 176 ms: 1.11x slower  |
| async_tree_io              | 375 ms     | 423 ms: 1.13x slower  |
| Geometric mean             | (ref)      | 1.07x slower          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | PGO                   |
|----------------|:----------:|:---------------------:|
| pidigits       | 146 ms     | 152 ms: 1.04x slower  |
| float          | 40.2 ms    | 47.8 ms: 1.19x slower |
| nbody          | 53.3 ms    | 74.1 ms: 1.39x slower |
| Geometric mean | (ref)      | 1.20x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | PGO                   |
|----------------|:----------:|:---------------------:|
| regex_v8       | 14.1 ms    | 13.5 ms: 1.04x faster |
| regex_dna      | 115 ms     | 112 ms: 1.02x faster  |
| regex_effbot   | 1.40 ms    | 1.42 ms: 1.02x slower |
| regex_compile  | 74.8 ms    | 88.2 ms: 1.18x slower |
| Geometric mean | (ref)      | 1.03x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | PGO                    |
|----------------------|:----------:|:----------------------:|
| json_loads           | 14.5 us    | 14.7 us: 1.02x slower  |
| xml_etree_parse      | 89.0 ms    | 91.2 ms: 1.03x slower  |
| xml_etree_iterparse  | 60.4 ms    | 63.7 ms: 1.06x slower  |
| json_dumps           | 6.48 ms    | 7.05 ms: 1.09x slower  |
| xml_etree_process    | 36.7 ms    | 41.5 ms: 1.13x slower  |
| xml_etree_generate   | 51.5 ms    | 58.7 ms: 1.14x slower  |
| pickle_pure_python   | 201 us     | 237 us: 1.18x slower   |
| tomli_loads          | 1.17 sec   | 1.47 sec: 1.25x slower |
| unpickle_pure_python | 123 us     | 155 us: 1.27x slower   |
| Geometric mean       | (ref)      | 1.12x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | PGO                   |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 19.8 ms: 1.01x slower |
| Geometric mean         | (ref)      | 1.01x slower          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | PGO                   |
|-----------------|:----------:|:---------------------:|
| django_template | 23.4 ms    | 25.1 ms: 1.07x slower |
| mako            | 6.12 ms    | 6.86 ms: 1.12x slower |
| genshi_text     | 14.2 ms    | 16.5 ms: 1.16x slower |
| genshi_xml      | 30.7 ms    | 36.3 ms: 1.18x slower |
| Geometric mean  | (ref)      | 1.13x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | PGO                    |
|----------------------------|:----------:|:----------------------:|
| subparsers                 | 44.9 ms    | 16.1 ms: 2.79x faster  |
| many_optionals             | 761 us     | 438 us: 1.74x faster   |
| coverage                   | 49.5 ms    | 46.8 ms: 1.06x faster  |
| regex_v8                   | 14.1 ms    | 13.5 ms: 1.04x faster  |
| regex_dna                  | 115 ms     | 112 ms: 1.02x faster   |
| create_gc_cycles           | 1.27 ms    | 1.25 ms: 1.01x faster  |
| python_startup_no_site     | 19.6 ms    | 19.8 ms: 1.01x slower  |
| json_loads                 | 14.5 us    | 14.7 us: 1.02x slower  |
| regex_effbot               | 1.40 ms    | 1.42 ms: 1.02x slower  |
| sqlite_synth               | 1.56 us    | 1.59 us: 1.02x slower  |
| xml_etree_parse            | 89.0 ms    | 91.2 ms: 1.03x slower  |
| connected_components       | 321 ms     | 329 ms: 1.03x slower   |
| async_tree_cpu_io_mixed    | 329 ms     | 339 ms: 1.03x slower   |
| sphinx                     | 638 ms     | 658 ms: 1.03x slower   |
| shortest_path              | 348 ms     | 359 ms: 1.03x slower   |
| docutils                   | 1.63 sec   | 1.68 sec: 1.03x slower |
| async_tree_memoization_tg  | 209 ms     | 216 ms: 1.03x slower   |
| pidigits                   | 146 ms     | 152 ms: 1.04x slower   |
| async_tree_cpu_io_mixed_tg | 328 ms     | 343 ms: 1.05x slower   |
| 2to3                       | 216 ms     | 227 ms: 1.05x slower   |
| thrift                     | 482 us     | 507 us: 1.05x slower   |
| json                       | 2.98 ms    | 3.14 ms: 1.05x slower  |
| xml_etree_iterparse        | 60.4 ms    | 63.7 ms: 1.06x slower  |
| typing_runtime_protocols   | 98.9 us    | 106 us: 1.07x slower   |
| django_template            | 23.4 ms    | 25.1 ms: 1.07x slower  |
| telco                      | 4.54 ms    | 4.89 ms: 1.08x slower  |
| coroutines                 | 12.4 ms    | 13.5 ms: 1.08x slower  |
| json_dumps                 | 6.48 ms    | 7.05 ms: 1.09x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 35.0 ms: 1.09x slower  |
| richards_super             | 32.2 ms    | 35.1 ms: 1.09x slower  |
| bpe_tokeniser              | 2.71 sec   | 2.96 sec: 1.09x slower |
| async_tree_memoization     | 205 ms     | 224 ms: 1.10x slower   |
| dulwich_log                | 39.5 ms    | 43.4 ms: 1.10x slower  |
| async_generators           | 206 ms     | 226 ms: 1.10x slower   |
| async_tree_none            | 170 ms     | 187 ms: 1.10x slower   |
| sqlglot_v2_normalize       | 66.9 ms    | 73.6 ms: 1.10x slower  |
| sympy_sum                  | 82.1 ms    | 90.5 ms: 1.10x slower  |
| richards                   | 27.8 ms    | 30.7 ms: 1.10x slower  |
| async_tree_io_tg           | 371 ms     | 410 ms: 1.10x slower   |
| meteor_contest             | 69.5 ms    | 76.9 ms: 1.11x slower  |
| async_tree_none_tg         | 159 ms     | 176 ms: 1.11x slower   |
| sympy_integrate            | 12.2 ms    | 13.5 ms: 1.11x slower  |
| logging_format             | 6.34 us    | 7.03 us: 1.11x slower  |
| pycparser                  | 664 ms     | 738 ms: 1.11x slower   |
| sympy_str                  | 158 ms     | 176 ms: 1.12x slower   |
| mako                       | 6.12 ms    | 6.86 ms: 1.12x slower  |
| sympy_expand               | 269 ms     | 302 ms: 1.12x slower   |
| async_tree_io              | 375 ms     | 423 ms: 1.13x slower   |
| logging_simple             | 5.78 us    | 6.53 us: 1.13x slower  |
| html5lib                   | 36.1 ms    | 40.8 ms: 1.13x slower  |
| xml_etree_process          | 36.7 ms    | 41.5 ms: 1.13x slower  |
| xml_etree_generate         | 51.5 ms    | 58.7 ms: 1.14x slower  |
| raytrace                   | 166 ms     | 191 ms: 1.15x slower   |
| genshi_text                | 14.2 ms    | 16.5 ms: 1.16x slower  |
| pprint_pformat             | 968 ms     | 1.13 sec: 1.16x slower |
| comprehensions             | 9.73 us    | 11.3 us: 1.16x slower  |
| pprint_safe_repr           | 478 ms     | 558 ms: 1.17x slower   |
| deepcopy_reduce            | 1.66 us    | 1.94 us: 1.17x slower  |
| mdp                        | 1.40 sec   | 1.64 sec: 1.17x slower |
| pickle_pure_python         | 201 us     | 237 us: 1.18x slower   |
| nqueens                    | 54.0 ms    | 63.6 ms: 1.18x slower  |
| regex_compile              | 74.8 ms    | 88.2 ms: 1.18x slower  |
| sqlglot_v2_transpile       | 933 us     | 1.10 ms: 1.18x slower  |
| genshi_xml                 | 30.7 ms    | 36.3 ms: 1.18x slower  |
| deepcopy                   | 160 us     | 190 us: 1.19x slower   |
| float                      | 40.2 ms    | 47.8 ms: 1.19x slower  |
| crypto_pyaes               | 41.6 ms    | 50.0 ms: 1.20x slower  |
| scimark_sparse_mat_mult    | 2.26 ms    | 2.72 ms: 1.20x slower  |
| spectral_norm              | 51.1 ms    | 61.5 ms: 1.20x slower  |
| sqlglot_v2_parse           | 740 us     | 892 us: 1.21x slower   |
| pyflate                    | 260 ms     | 315 ms: 1.21x slower   |
| chaos                      | 35.9 ms    | 43.6 ms: 1.22x slower  |
| logging_silent             | 53.3 ns    | 65.2 ns: 1.22x slower  |
| scimark_lu                 | 54.4 ms    | 66.9 ms: 1.23x slower  |
| deepcopy_memo              | 17.0 us    | 21.0 us: 1.23x slower  |
| deltablue                  | 1.85 ms    | 2.29 ms: 1.24x slower  |
| tomli_loads                | 1.17 sec   | 1.47 sec: 1.25x slower |
| fannkuch                   | 236 ms     | 296 ms: 1.26x slower   |
| hexiom                     | 3.47 ms    | 4.38 ms: 1.26x slower  |
| scimark_fft                | 152 ms     | 192 ms: 1.27x slower   |
| unpickle_pure_python       | 123 us     | 155 us: 1.27x slower   |
| scimark_monte_carlo        | 37.0 ms    | 47.1 ms: 1.27x slower  |
| go                         | 68.4 ms    | 88.6 ms: 1.30x slower  |
| generators                 | 14.8 ms    | 19.3 ms: 1.30x slower  |
| pathlib                    | 24.3 ms    | 32.1 ms: 1.32x slower  |
| scimark_sor                | 67.5 ms    | 91.0 ms: 1.35x slower  |
| nbody                      | 53.3 ms    | 74.1 ms: 1.39x slower  |
| Geometric mean             | (ref)      | 1.10x slower           |

Benchmark hidden because not significant (7): gc_traversal, bench_mp_pool, python_startup, asyncio_websockets, pylint, k_core, bench_thread_pool

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown