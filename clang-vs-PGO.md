# Results vs. base

- fork: unknown
- ref: clang
- machine: unknown-unknown
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.214x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | PGO      | clang                  |
|----------------|:--------:|:----------------------:|
| 2to3           | 227 ms   | 207 ms: 1.10x faster   |
| docutils       | 1.68 sec | 1.56 sec: 1.08x faster |
| html5lib       | 40.8 ms  | 34.9 ms: 1.17x faster  |
| sphinx         | 658 ms   | 603 ms: 1.09x faster   |
| Geometric mean | (ref)    | 1.11x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | PGO     | clang                 |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 318 ms  | 159 ms: 2.00x faster  |
| coroutines                 | 13.5 ms | 10.7 ms: 1.26x faster |
| async_generators           | 226 ms  | 187 ms: 1.21x faster  |
| async_tree_io              | 423 ms  | 353 ms: 1.20x faster  |
| async_tree_memoization     | 224 ms  | 187 ms: 1.20x faster  |
| async_tree_none            | 187 ms  | 159 ms: 1.17x faster  |
| async_tree_none_tg         | 176 ms  | 150 ms: 1.17x faster  |
| async_tree_io_tg           | 410 ms  | 351 ms: 1.17x faster  |
| async_tree_memoization_tg  | 216 ms  | 197 ms: 1.10x faster  |
| async_tree_cpu_io_mixed_tg | 343 ms  | 316 ms: 1.09x faster  |
| async_tree_cpu_io_mixed    | 339 ms  | 313 ms: 1.08x faster  |
| Geometric mean             | (ref)   | 1.22x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | PGO     | clang                 |
|----------------|:-------:|:---------------------:|
| nbody          | 74.1 ms | 49.1 ms: 1.51x faster |
| float          | 47.8 ms | 36.9 ms: 1.29x faster |
| pidigits       | 152 ms  | 145 ms: 1.05x faster  |
| Geometric mean | (ref)   | 1.27x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | PGO     | clang                 |
|----------------|:-------:|:---------------------:|
| regex_compile  | 88.2 ms | 69.8 ms: 1.26x faster |
| regex_v8       | 13.5 ms | 13.0 ms: 1.04x faster |
| regex_dna      | 112 ms  | 117 ms: 1.04x slower  |
| regex_effbot   | 1.42 ms | 1.54 ms: 1.08x slower |
| Geometric mean | (ref)   | 1.04x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | PGO      | clang                  |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 155 us   | 107 us: 1.45x faster   |
| pickle_pure_python   | 237 us   | 173 us: 1.37x faster   |
| tomli_loads          | 1.47 sec | 1.09 sec: 1.35x faster |
| json_dumps           | 7.05 ms  | 5.66 ms: 1.25x faster  |
| xml_etree_process    | 41.5 ms  | 34.0 ms: 1.22x faster  |
| xml_etree_generate   | 58.7 ms  | 49.1 ms: 1.20x faster  |
| json_loads           | 14.7 us  | 14.1 us: 1.05x faster  |
| xml_etree_iterparse  | 63.7 ms  | 61.5 ms: 1.04x faster  |
| xml_etree_parse      | 91.2 ms  | 89.4 ms: 1.02x faster  |
| Geometric mean       | (ref)    | 1.21x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | PGO     | clang                 |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.1 ms | 26.4 ms: 1.01x slower |
| python_startup_no_site | 19.8 ms | 20.9 ms: 1.05x slower |
| Geometric mean         | (ref)   | 1.03x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | PGO     | clang                 |
|-----------------|:-------:|:---------------------:|
| genshi_text     | 16.5 ms | 11.9 ms: 1.38x faster |
| genshi_xml      | 36.3 ms | 29.0 ms: 1.25x faster |
| django_template | 25.1 ms | 21.3 ms: 1.18x faster |
| mako            | 6.86 ms | 5.83 ms: 1.18x faster |
| Geometric mean  | (ref)   | 1.25x faster          |

All benchmarks:
===============

| Benchmark                  | PGO      | clang                  |
|----------------------------|:--------:|:----------------------:|
| mdp                        | 1.64 sec | 682 ms: 2.40x faster   |
| asyncio_websockets         | 318 ms   | 159 ms: 2.00x faster   |
| scimark_sor                | 91.0 ms  | 49.3 ms: 1.85x faster  |
| scimark_monte_carlo        | 47.1 ms  | 28.6 ms: 1.65x faster  |
| logging_silent             | 65.2 ns  | 41.1 ns: 1.58x faster  |
| scimark_lu                 | 66.9 ms  | 43.5 ms: 1.54x faster  |
| nbody                      | 74.1 ms  | 49.1 ms: 1.51x faster  |
| deepcopy_memo              | 21.0 us  | 14.0 us: 1.51x faster  |
| hexiom                     | 4.38 ms  | 2.98 ms: 1.47x faster  |
| unpickle_pure_python       | 155 us   | 107 us: 1.45x faster   |
| go                         | 88.6 ms  | 61.5 ms: 1.44x faster  |
| spectral_norm              | 61.5 ms  | 42.8 ms: 1.44x faster  |
| fannkuch                   | 296 ms   | 207 ms: 1.43x faster   |
| deltablue                  | 2.29 ms  | 1.64 ms: 1.40x faster  |
| chaos                      | 43.6 ms  | 31.4 ms: 1.39x faster  |
| genshi_text                | 16.5 ms  | 11.9 ms: 1.38x faster  |
| scimark_fft                | 192 ms   | 139 ms: 1.38x faster   |
| pickle_pure_python         | 237 us   | 173 us: 1.37x faster   |
| scimark_sparse_mat_mult    | 2.72 ms  | 1.99 ms: 1.37x faster  |
| pprint_pformat             | 1.13 sec | 835 ms: 1.35x faster   |
| tomli_loads                | 1.47 sec | 1.09 sec: 1.35x faster |
| pyflate                    | 315 ms   | 234 ms: 1.34x faster   |
| pprint_safe_repr           | 558 ms   | 415 ms: 1.34x faster   |
| raytrace                   | 191 ms   | 142 ms: 1.34x faster   |
| deepcopy                   | 190 us   | 144 us: 1.31x faster   |
| comprehensions             | 11.3 us  | 8.64 us: 1.31x faster  |
| generators                 | 19.3 ms  | 14.8 ms: 1.31x faster  |
| sqlglot_v2_parse           | 892 us   | 682 us: 1.31x faster   |
| float                      | 47.8 ms  | 36.9 ms: 1.29x faster  |
| deepcopy_reduce            | 1.94 us  | 1.52 us: 1.28x faster  |
| nqueens                    | 63.6 ms  | 49.8 ms: 1.28x faster  |
| regex_compile              | 88.2 ms  | 69.8 ms: 1.26x faster  |
| sqlglot_v2_transpile       | 1.10 ms  | 873 us: 1.26x faster   |
| coroutines                 | 13.5 ms  | 10.7 ms: 1.26x faster  |
| genshi_xml                 | 36.3 ms  | 29.0 ms: 1.25x faster  |
| crypto_pyaes               | 50.0 ms  | 39.9 ms: 1.25x faster  |
| json_dumps                 | 7.05 ms  | 5.66 ms: 1.25x faster  |
| xml_etree_process          | 41.5 ms  | 34.0 ms: 1.22x faster  |
| typing_runtime_protocols   | 106 us   | 87.6 us: 1.21x faster  |
| async_generators           | 226 ms   | 187 ms: 1.21x faster   |
| sympy_integrate            | 13.5 ms  | 11.2 ms: 1.21x faster  |
| async_tree_io              | 423 ms   | 353 ms: 1.20x faster   |
| async_tree_memoization     | 224 ms   | 187 ms: 1.20x faster   |
| xml_etree_generate         | 58.7 ms  | 49.1 ms: 1.20x faster  |
| sympy_str                  | 176 ms   | 149 ms: 1.18x faster   |
| sympy_expand               | 302 ms   | 256 ms: 1.18x faster   |
| logging_format             | 7.03 us  | 5.96 us: 1.18x faster  |
| django_template            | 25.1 ms  | 21.3 ms: 1.18x faster  |
| coverage                   | 46.8 ms  | 39.8 ms: 1.18x faster  |
| logging_simple             | 6.53 us  | 5.55 us: 1.18x faster  |
| mako                       | 6.86 ms  | 5.83 ms: 1.18x faster  |
| async_tree_none            | 187 ms   | 159 ms: 1.17x faster   |
| async_tree_none_tg         | 176 ms   | 150 ms: 1.17x faster   |
| richards                   | 30.7 ms  | 26.3 ms: 1.17x faster  |
| async_tree_io_tg           | 410 ms   | 351 ms: 1.17x faster   |
| html5lib                   | 40.8 ms  | 34.9 ms: 1.17x faster  |
| bpe_tokeniser              | 2.96 sec | 2.55 sec: 1.16x faster |
| richards_super             | 35.1 ms  | 30.2 ms: 1.16x faster  |
| telco                      | 4.89 ms  | 4.25 ms: 1.15x faster  |
| meteor_contest             | 76.9 ms  | 66.8 ms: 1.15x faster  |
| sqlglot_v2_normalize       | 73.6 ms  | 64.2 ms: 1.15x faster  |
| sympy_sum                  | 90.5 ms  | 79.2 ms: 1.14x faster  |
| pycparser                  | 738 ms   | 647 ms: 1.14x faster   |
| dulwich_log                | 43.4 ms  | 38.0 ms: 1.14x faster  |
| sqlglot_v2_optimize        | 35.0 ms  | 31.1 ms: 1.13x faster  |
| json                       | 3.14 ms  | 2.81 ms: 1.11x faster  |
| 2to3                       | 227 ms   | 207 ms: 1.10x faster   |
| async_tree_memoization_tg  | 216 ms   | 197 ms: 1.10x faster   |
| sphinx                     | 658 ms   | 603 ms: 1.09x faster   |
| async_tree_cpu_io_mixed_tg | 343 ms   | 316 ms: 1.09x faster   |
| async_tree_cpu_io_mixed    | 339 ms   | 313 ms: 1.08x faster   |
| docutils                   | 1.68 sec | 1.56 sec: 1.08x faster |
| many_optionals             | 438 us   | 409 us: 1.07x faster   |
| pylint                     | 201 ms   | 188 ms: 1.07x faster   |
| subparsers                 | 16.1 ms  | 15.3 ms: 1.05x faster  |
| sqlite_synth               | 1.59 us  | 1.51 us: 1.05x faster  |
| bench_thread_pool          | 864 us   | 823 us: 1.05x faster   |
| pidigits                   | 152 ms   | 145 ms: 1.05x faster   |
| pathlib                    | 32.1 ms  | 30.7 ms: 1.05x faster  |
| json_loads                 | 14.7 us  | 14.1 us: 1.05x faster  |
| k_core                     | 1.73 sec | 1.66 sec: 1.04x faster |
| regex_v8                   | 13.5 ms  | 13.0 ms: 1.04x faster  |
| xml_etree_iterparse        | 63.7 ms  | 61.5 ms: 1.04x faster  |
| shortest_path              | 359 ms   | 351 ms: 1.03x faster   |
| xml_etree_parse            | 91.2 ms  | 89.4 ms: 1.02x faster  |
| python_startup             | 26.1 ms  | 26.4 ms: 1.01x slower  |
| regex_dna                  | 112 ms   | 117 ms: 1.04x slower   |
| python_startup_no_site     | 19.8 ms  | 20.9 ms: 1.05x slower  |
| regex_effbot               | 1.42 ms  | 1.54 ms: 1.08x slower  |
| create_gc_cycles           | 1.25 ms  | 1.36 ms: 1.09x slower  |
| gc_traversal               | 2.06 ms  | 2.76 ms: 1.34x slower  |
| Geometric mean             | (ref)    | 1.21x faster           |

Benchmark hidden because not significant (2): bench_mp_pool, connected_components
Ignored benchmarks (1) of PGO.json: thrift

- Geometric mean (including insignificant results): 1.214x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown