# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.157x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang-PGO | PGO                    |
|----------------|:---------:|:----------------------:|
| 2to3           | 204 ms    | 227 ms: 1.12x slower   |
| docutils       | 1.55 sec  | 1.68 sec: 1.09x slower |
| html5lib       | 35.2 ms   | 40.8 ms: 1.16x slower  |
| sphinx         | 599 ms    | 658 ms: 1.10x slower   |
| Geometric mean | (ref)     | 1.11x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang-PGO | PGO                   |
|----------------------------|:---------:|:---------------------:|
| asyncio_websockets         | 400 ms    | 318 ms: 1.26x faster  |
| async_tree_cpu_io_mixed    | 309 ms    | 339 ms: 1.10x slower  |
| async_tree_memoization_tg  | 195 ms    | 216 ms: 1.10x slower  |
| async_tree_cpu_io_mixed_tg | 310 ms    | 343 ms: 1.11x slower  |
| async_tree_io_tg           | 352 ms    | 410 ms: 1.16x slower  |
| async_tree_memoization     | 190 ms    | 224 ms: 1.18x slower  |
| async_tree_none_tg         | 147 ms    | 176 ms: 1.20x slower  |
| async_generators           | 188 ms    | 226 ms: 1.20x slower  |
| async_tree_none            | 155 ms    | 187 ms: 1.20x slower  |
| async_tree_io              | 349 ms    | 423 ms: 1.21x slower  |
| coroutines                 | 11.1 ms   | 13.5 ms: 1.21x slower |
| Geometric mean             | (ref)     | 1.13x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang-PGO | PGO                   |
|----------------|:---------:|:---------------------:|
| pidigits       | 148 ms    | 152 ms: 1.03x slower  |
| float          | 38.5 ms   | 47.8 ms: 1.24x slower |
| nbody          | 52.9 ms   | 74.1 ms: 1.40x slower |
| Geometric mean | (ref)     | 1.21x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang-PGO | PGO                   |
|----------------|:---------:|:---------------------:|
| regex_effbot   | 1.65 ms   | 1.42 ms: 1.16x faster |
| regex_dna      | 121 ms    | 112 ms: 1.07x faster  |
| regex_compile  | 73.4 ms   | 88.2 ms: 1.20x slower |
| Geometric mean | (ref)     | 1.01x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang-PGO | PGO                    |
|----------------------|:---------:|:----------------------:|
| xml_etree_parse      | 88.8 ms   | 91.2 ms: 1.03x slower  |
| json_loads           | 14.2 us   | 14.7 us: 1.04x slower  |
| xml_etree_iterparse  | 60.7 ms   | 63.7 ms: 1.05x slower  |
| xml_etree_generate   | 48.4 ms   | 58.7 ms: 1.21x slower  |
| xml_etree_process    | 34.0 ms   | 41.5 ms: 1.22x slower  |
| json_dumps           | 5.76 ms   | 7.05 ms: 1.22x slower  |
| tomli_loads          | 1.13 sec  | 1.47 sec: 1.30x slower |
| pickle_pure_python   | 175 us    | 237 us: 1.35x slower   |
| unpickle_pure_python | 109 us    | 155 us: 1.43x slower   |
| Geometric mean       | (ref)     | 1.20x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | clang-PGO | PGO                   |
|----------------|:---------:|:---------------------:|
| python_startup | 26.6 ms   | 26.1 ms: 1.02x faster |
| Geometric mean | (ref)     | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | clang-PGO | PGO                   |
|-----------------|:---------:|:---------------------:|
| mako            | 5.72 ms   | 6.86 ms: 1.20x slower |
| django_template | 19.5 ms   | 25.1 ms: 1.28x slower |
| genshi_xml      | 27.4 ms   | 36.3 ms: 1.33x slower |
| genshi_text     | 12.0 ms   | 16.5 ms: 1.38x slower |
| Geometric mean  | (ref)     | 1.30x slower          |

All benchmarks:
===============

| Benchmark                  | clang-PGO | PGO                    |
|----------------------------|:---------:|:----------------------:|
| gc_traversal               | 2.79 ms   | 2.06 ms: 1.36x faster  |
| asyncio_websockets         | 400 ms    | 318 ms: 1.26x faster   |
| regex_effbot               | 1.65 ms   | 1.42 ms: 1.16x faster  |
| create_gc_cycles           | 1.37 ms   | 1.25 ms: 1.10x faster  |
| regex_dna                  | 121 ms    | 112 ms: 1.07x faster   |
| python_startup             | 26.6 ms   | 26.1 ms: 1.02x faster  |
| connected_components       | 325 ms    | 329 ms: 1.01x slower   |
| pidigits                   | 148 ms    | 152 ms: 1.03x slower   |
| xml_etree_parse            | 88.8 ms   | 91.2 ms: 1.03x slower  |
| json_loads                 | 14.2 us   | 14.7 us: 1.04x slower  |
| shortest_path              | 345 ms    | 359 ms: 1.04x slower   |
| xml_etree_iterparse        | 60.7 ms   | 63.7 ms: 1.05x slower  |
| pathlib                    | 30.4 ms   | 32.1 ms: 1.06x slower  |
| sqlite_synth               | 1.49 us   | 1.59 us: 1.06x slower  |
| k_core                     | 1.61 sec  | 1.73 sec: 1.08x slower |
| many_optionals             | 405 us    | 438 us: 1.08x slower   |
| docutils                   | 1.55 sec  | 1.68 sec: 1.09x slower |
| async_tree_cpu_io_mixed    | 309 ms    | 339 ms: 1.10x slower   |
| dulwich_log                | 39.5 ms   | 43.4 ms: 1.10x slower  |
| sphinx                     | 599 ms    | 658 ms: 1.10x slower   |
| pylint                     | 182 ms    | 201 ms: 1.10x slower   |
| async_tree_memoization_tg  | 195 ms    | 216 ms: 1.10x slower   |
| async_tree_cpu_io_mixed_tg | 310 ms    | 343 ms: 1.11x slower   |
| json                       | 2.83 ms   | 3.14 ms: 1.11x slower  |
| sympy_sum                  | 81.4 ms   | 90.5 ms: 1.11x slower  |
| 2to3                       | 204 ms    | 227 ms: 1.12x slower   |
| meteor_contest             | 68.7 ms   | 76.9 ms: 1.12x slower  |
| subparsers                 | 14.2 ms   | 16.1 ms: 1.13x slower  |
| coverage                   | 40.9 ms   | 46.8 ms: 1.14x slower  |
| sympy_integrate            | 11.8 ms   | 13.5 ms: 1.15x slower  |
| sympy_str                  | 153 ms    | 176 ms: 1.15x slower   |
| html5lib                   | 35.2 ms   | 40.8 ms: 1.16x slower  |
| pycparser                  | 637 ms    | 738 ms: 1.16x slower   |
| async_tree_io_tg           | 352 ms    | 410 ms: 1.16x slower   |
| sympy_expand               | 259 ms    | 302 ms: 1.17x slower   |
| telco                      | 4.20 ms   | 4.89 ms: 1.17x slower  |
| thrift                     | 434 us    | 507 us: 1.17x slower   |
| sqlglot_v2_optimize        | 29.8 ms   | 35.0 ms: 1.18x slower  |
| async_tree_memoization     | 190 ms    | 224 ms: 1.18x slower   |
| bpe_tokeniser              | 2.50 sec  | 2.96 sec: 1.18x slower |
| async_tree_none_tg         | 147 ms    | 176 ms: 1.20x slower   |
| mako                       | 5.72 ms   | 6.86 ms: 1.20x slower  |
| regex_compile              | 73.4 ms   | 88.2 ms: 1.20x slower  |
| async_generators           | 188 ms    | 226 ms: 1.20x slower   |
| async_tree_none            | 155 ms    | 187 ms: 1.20x slower   |
| logging_format             | 5.83 us   | 7.03 us: 1.20x slower  |
| logging_simple             | 5.39 us   | 6.53 us: 1.21x slower  |
| xml_etree_generate         | 48.4 ms   | 58.7 ms: 1.21x slower  |
| async_tree_io              | 349 ms    | 423 ms: 1.21x slower   |
| coroutines                 | 11.1 ms   | 13.5 ms: 1.21x slower  |
| xml_etree_process          | 34.0 ms   | 41.5 ms: 1.22x slower  |
| json_dumps                 | 5.76 ms   | 7.05 ms: 1.22x slower  |
| generators                 | 15.8 ms   | 19.3 ms: 1.22x slower  |
| sqlglot_v2_normalize       | 59.9 ms   | 73.6 ms: 1.23x slower  |
| typing_runtime_protocols   | 86.2 us   | 106 us: 1.23x slower   |
| float                      | 38.5 ms   | 47.8 ms: 1.24x slower  |
| mdp                        | 1.30 sec  | 1.64 sec: 1.26x slower |
| sqlglot_v2_transpile       | 868 us    | 1.10 ms: 1.27x slower  |
| crypto_pyaes               | 39.4 ms   | 50.0 ms: 1.27x slower  |
| comprehensions             | 8.84 us   | 11.3 us: 1.28x slower  |
| django_template            | 19.5 ms   | 25.1 ms: 1.28x slower  |
| pprint_pformat             | 874 ms    | 1.13 sec: 1.29x slower |
| pyflate                    | 245 ms    | 315 ms: 1.29x slower   |
| pprint_safe_repr           | 432 ms    | 558 ms: 1.29x slower   |
| tomli_loads                | 1.13 sec  | 1.47 sec: 1.30x slower |
| sqlglot_v2_parse           | 686 us    | 892 us: 1.30x slower   |
| deepcopy_reduce            | 1.49 us   | 1.94 us: 1.30x slower  |
| deepcopy                   | 145 us    | 190 us: 1.31x slower   |
| genshi_xml                 | 27.4 ms   | 36.3 ms: 1.33x slower  |
| scimark_sparse_mat_mult    | 2.05 ms   | 2.72 ms: 1.33x slower  |
| nqueens                    | 47.7 ms   | 63.6 ms: 1.33x slower  |
| scimark_fft                | 143 ms    | 192 ms: 1.35x slower   |
| pickle_pure_python         | 175 us    | 237 us: 1.35x slower   |
| scimark_lu                 | 49.1 ms   | 66.9 ms: 1.36x slower  |
| go                         | 65.1 ms   | 88.6 ms: 1.36x slower  |
| spectral_norm              | 44.7 ms   | 61.5 ms: 1.38x slower  |
| genshi_text                | 12.0 ms   | 16.5 ms: 1.38x slower  |
| raytrace                   | 137 ms    | 191 ms: 1.39x slower   |
| deepcopy_memo              | 15.1 us   | 21.0 us: 1.40x slower  |
| nbody                      | 52.9 ms   | 74.1 ms: 1.40x slower  |
| hexiom                     | 3.13 ms   | 4.38 ms: 1.40x slower  |
| richards                   | 21.9 ms   | 30.7 ms: 1.40x slower  |
| chaos                      | 31.1 ms   | 43.6 ms: 1.40x slower  |
| fannkuch                   | 209 ms    | 296 ms: 1.42x slower   |
| richards_super             | 24.6 ms   | 35.1 ms: 1.43x slower  |
| unpickle_pure_python       | 109 us    | 155 us: 1.43x slower   |
| scimark_monte_carlo        | 32.8 ms   | 47.1 ms: 1.44x slower  |
| deltablue                  | 1.59 ms   | 2.29 ms: 1.44x slower  |
| logging_silent             | 44.5 ns   | 65.2 ns: 1.47x slower  |
| scimark_sor                | 59.1 ms   | 91.0 ms: 1.54x slower  |
| Geometric mean             | (ref)     | 1.19x slower           |

Benchmark hidden because not significant (2): python_startup_no_site, regex_v8
Ignored benchmarks (2) of PGO.json: bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.157x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown