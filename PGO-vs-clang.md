# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.176x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | clang    | PGO                    |
|----------------|:--------:|:----------------------:|
| 2to3           | 207 ms   | 227 ms: 1.10x slower   |
| docutils       | 1.56 sec | 1.68 sec: 1.08x slower |
| html5lib       | 34.9 ms  | 40.8 ms: 1.17x slower  |
| sphinx         | 603 ms   | 658 ms: 1.09x slower   |
| Geometric mean | (ref)    | 1.11x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | clang   | PGO                   |
|----------------------------|:-------:|:---------------------:|
| async_tree_cpu_io_mixed    | 313 ms  | 339 ms: 1.08x slower  |
| async_tree_cpu_io_mixed_tg | 316 ms  | 343 ms: 1.09x slower  |
| async_tree_memoization_tg  | 197 ms  | 216 ms: 1.10x slower  |
| async_tree_io_tg           | 351 ms  | 410 ms: 1.17x slower  |
| async_tree_none_tg         | 150 ms  | 176 ms: 1.17x slower  |
| async_tree_none            | 159 ms  | 187 ms: 1.17x slower  |
| async_tree_memoization     | 187 ms  | 224 ms: 1.20x slower  |
| async_tree_io              | 353 ms  | 423 ms: 1.20x slower  |
| async_generators           | 187 ms  | 226 ms: 1.21x slower  |
| coroutines                 | 10.7 ms | 13.5 ms: 1.26x slower |
| asyncio_websockets         | 159 ms  | 318 ms: 2.00x slower  |
| Geometric mean             | (ref)   | 1.22x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | clang   | PGO                   |
|----------------|:-------:|:---------------------:|
| pidigits       | 145 ms  | 152 ms: 1.05x slower  |
| float          | 36.9 ms | 47.8 ms: 1.29x slower |
| nbody          | 49.1 ms | 74.1 ms: 1.51x slower |
| Geometric mean | (ref)   | 1.27x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | clang   | PGO                   |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.54 ms | 1.42 ms: 1.08x faster |
| regex_dna      | 117 ms  | 112 ms: 1.04x faster  |
| regex_v8       | 13.0 ms | 13.5 ms: 1.04x slower |
| regex_compile  | 69.8 ms | 88.2 ms: 1.26x slower |
| Geometric mean | (ref)   | 1.04x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | clang    | PGO                    |
|----------------------|:--------:|:----------------------:|
| xml_etree_parse      | 89.4 ms  | 91.2 ms: 1.02x slower  |
| xml_etree_iterparse  | 61.5 ms  | 63.7 ms: 1.04x slower  |
| json_loads           | 14.1 us  | 14.7 us: 1.05x slower  |
| xml_etree_generate   | 49.1 ms  | 58.7 ms: 1.20x slower  |
| xml_etree_process    | 34.0 ms  | 41.5 ms: 1.22x slower  |
| json_dumps           | 5.66 ms  | 7.05 ms: 1.25x slower  |
| tomli_loads          | 1.09 sec | 1.47 sec: 1.35x slower |
| pickle_pure_python   | 173 us   | 237 us: 1.37x slower   |
| unpickle_pure_python | 107 us   | 155 us: 1.45x slower   |
| Geometric mean       | (ref)    | 1.21x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | clang   | PGO                   |
|------------------------|:-------:|:---------------------:|
| python_startup_no_site | 20.9 ms | 19.8 ms: 1.05x faster |
| python_startup         | 26.4 ms | 26.1 ms: 1.01x faster |
| Geometric mean         | (ref)   | 1.03x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | clang   | PGO                   |
|-----------------|:-------:|:---------------------:|
| mako            | 5.83 ms | 6.86 ms: 1.18x slower |
| django_template | 21.3 ms | 25.1 ms: 1.18x slower |
| genshi_xml      | 29.0 ms | 36.3 ms: 1.25x slower |
| genshi_text     | 11.9 ms | 16.5 ms: 1.38x slower |
| Geometric mean  | (ref)   | 1.25x slower          |

All benchmarks:
===============

| Benchmark                  | clang    | PGO                    |
|----------------------------|:--------:|:----------------------:|
| gc_traversal               | 2.76 ms  | 2.06 ms: 1.34x faster  |
| create_gc_cycles           | 1.36 ms  | 1.25 ms: 1.09x faster  |
| regex_effbot               | 1.54 ms  | 1.42 ms: 1.08x faster  |
| python_startup_no_site     | 20.9 ms  | 19.8 ms: 1.05x faster  |
| regex_dna                  | 117 ms   | 112 ms: 1.04x faster   |
| python_startup             | 26.4 ms  | 26.1 ms: 1.01x faster  |
| xml_etree_parse            | 89.4 ms  | 91.2 ms: 1.02x slower  |
| shortest_path              | 351 ms   | 359 ms: 1.03x slower   |
| xml_etree_iterparse        | 61.5 ms  | 63.7 ms: 1.04x slower  |
| regex_v8                   | 13.0 ms  | 13.5 ms: 1.04x slower  |
| k_core                     | 1.66 sec | 1.73 sec: 1.04x slower |
| json_loads                 | 14.1 us  | 14.7 us: 1.05x slower  |
| pathlib                    | 30.7 ms  | 32.1 ms: 1.05x slower  |
| pidigits                   | 145 ms   | 152 ms: 1.05x slower   |
| bench_thread_pool          | 823 us   | 864 us: 1.05x slower   |
| sqlite_synth               | 1.51 us  | 1.59 us: 1.05x slower  |
| subparsers                 | 15.3 ms  | 16.1 ms: 1.05x slower  |
| pylint                     | 188 ms   | 201 ms: 1.07x slower   |
| many_optionals             | 409 us   | 438 us: 1.07x slower   |
| docutils                   | 1.56 sec | 1.68 sec: 1.08x slower |
| async_tree_cpu_io_mixed    | 313 ms   | 339 ms: 1.08x slower   |
| async_tree_cpu_io_mixed_tg | 316 ms   | 343 ms: 1.09x slower   |
| sphinx                     | 603 ms   | 658 ms: 1.09x slower   |
| async_tree_memoization_tg  | 197 ms   | 216 ms: 1.10x slower   |
| 2to3                       | 207 ms   | 227 ms: 1.10x slower   |
| json                       | 2.81 ms  | 3.14 ms: 1.11x slower  |
| sqlglot_v2_optimize        | 31.1 ms  | 35.0 ms: 1.13x slower  |
| dulwich_log                | 38.0 ms  | 43.4 ms: 1.14x slower  |
| pycparser                  | 647 ms   | 738 ms: 1.14x slower   |
| sympy_sum                  | 79.2 ms  | 90.5 ms: 1.14x slower  |
| sqlglot_v2_normalize       | 64.2 ms  | 73.6 ms: 1.15x slower  |
| meteor_contest             | 66.8 ms  | 76.9 ms: 1.15x slower  |
| telco                      | 4.25 ms  | 4.89 ms: 1.15x slower  |
| richards_super             | 30.2 ms  | 35.1 ms: 1.16x slower  |
| bpe_tokeniser              | 2.55 sec | 2.96 sec: 1.16x slower |
| html5lib                   | 34.9 ms  | 40.8 ms: 1.17x slower  |
| async_tree_io_tg           | 351 ms   | 410 ms: 1.17x slower   |
| richards                   | 26.3 ms  | 30.7 ms: 1.17x slower  |
| async_tree_none_tg         | 150 ms   | 176 ms: 1.17x slower   |
| async_tree_none            | 159 ms   | 187 ms: 1.17x slower   |
| mako                       | 5.83 ms  | 6.86 ms: 1.18x slower  |
| logging_simple             | 5.55 us  | 6.53 us: 1.18x slower  |
| coverage                   | 39.8 ms  | 46.8 ms: 1.18x slower  |
| django_template            | 21.3 ms  | 25.1 ms: 1.18x slower  |
| logging_format             | 5.96 us  | 7.03 us: 1.18x slower  |
| sympy_expand               | 256 ms   | 302 ms: 1.18x slower   |
| sympy_str                  | 149 ms   | 176 ms: 1.18x slower   |
| xml_etree_generate         | 49.1 ms  | 58.7 ms: 1.20x slower  |
| async_tree_memoization     | 187 ms   | 224 ms: 1.20x slower   |
| async_tree_io              | 353 ms   | 423 ms: 1.20x slower   |
| sympy_integrate            | 11.2 ms  | 13.5 ms: 1.21x slower  |
| async_generators           | 187 ms   | 226 ms: 1.21x slower   |
| typing_runtime_protocols   | 87.6 us  | 106 us: 1.21x slower   |
| xml_etree_process          | 34.0 ms  | 41.5 ms: 1.22x slower  |
| json_dumps                 | 5.66 ms  | 7.05 ms: 1.25x slower  |
| crypto_pyaes               | 39.9 ms  | 50.0 ms: 1.25x slower  |
| genshi_xml                 | 29.0 ms  | 36.3 ms: 1.25x slower  |
| coroutines                 | 10.7 ms  | 13.5 ms: 1.26x slower  |
| sqlglot_v2_transpile       | 873 us   | 1.10 ms: 1.26x slower  |
| regex_compile              | 69.8 ms  | 88.2 ms: 1.26x slower  |
| nqueens                    | 49.8 ms  | 63.6 ms: 1.28x slower  |
| deepcopy_reduce            | 1.52 us  | 1.94 us: 1.28x slower  |
| float                      | 36.9 ms  | 47.8 ms: 1.29x slower  |
| sqlglot_v2_parse           | 682 us   | 892 us: 1.31x slower   |
| generators                 | 14.8 ms  | 19.3 ms: 1.31x slower  |
| comprehensions             | 8.64 us  | 11.3 us: 1.31x slower  |
| deepcopy                   | 144 us   | 190 us: 1.31x slower   |
| raytrace                   | 142 ms   | 191 ms: 1.34x slower   |
| pprint_safe_repr           | 415 ms   | 558 ms: 1.34x slower   |
| pyflate                    | 234 ms   | 315 ms: 1.34x slower   |
| tomli_loads                | 1.09 sec | 1.47 sec: 1.35x slower |
| pprint_pformat             | 835 ms   | 1.13 sec: 1.35x slower |
| scimark_sparse_mat_mult    | 1.99 ms  | 2.72 ms: 1.37x slower  |
| pickle_pure_python         | 173 us   | 237 us: 1.37x slower   |
| scimark_fft                | 139 ms   | 192 ms: 1.38x slower   |
| genshi_text                | 11.9 ms  | 16.5 ms: 1.38x slower  |
| chaos                      | 31.4 ms  | 43.6 ms: 1.39x slower  |
| deltablue                  | 1.64 ms  | 2.29 ms: 1.40x slower  |
| fannkuch                   | 207 ms   | 296 ms: 1.43x slower   |
| spectral_norm              | 42.8 ms  | 61.5 ms: 1.44x slower  |
| go                         | 61.5 ms  | 88.6 ms: 1.44x slower  |
| unpickle_pure_python       | 107 us   | 155 us: 1.45x slower   |
| hexiom                     | 2.98 ms  | 4.38 ms: 1.47x slower  |
| deepcopy_memo              | 14.0 us  | 21.0 us: 1.51x slower  |
| nbody                      | 49.1 ms  | 74.1 ms: 1.51x slower  |
| scimark_lu                 | 43.5 ms  | 66.9 ms: 1.54x slower  |
| logging_silent             | 41.1 ns  | 65.2 ns: 1.58x slower  |
| scimark_monte_carlo        | 28.6 ms  | 47.1 ms: 1.65x slower  |
| scimark_sor                | 49.3 ms  | 91.0 ms: 1.85x slower  |
| asyncio_websockets         | 159 ms   | 318 ms: 2.00x slower   |
| mdp                        | 682 ms   | 1.64 sec: 2.40x slower |
| Geometric mean             | (ref)    | 1.21x slower           |

Benchmark hidden because not significant (2): connected_components, bench_mp_pool
Ignored benchmarks (1) of PGO.json: thrift

- Geometric mean (including insignificant results): 1.176x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown