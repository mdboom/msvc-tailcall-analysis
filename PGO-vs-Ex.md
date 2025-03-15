# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | Ex       | PGO                    |
|----------------|:--------:|:----------------------:|
| 2to3           | 309 ms   | 227 ms: 1.36x faster   |
| docutils       | 2.31 sec | 1.68 sec: 1.37x faster |
| html5lib       | 52.5 ms  | 40.8 ms: 1.29x faster  |
| sphinx         | 933 ms   | 658 ms: 1.42x faster   |
| Geometric mean | (ref)    | 1.36x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | Ex      | PGO                   |
|----------------------------|:-------:|:---------------------:|
| coroutines                 | 22.4 ms | 13.5 ms: 1.66x faster |
| async_generators           | 348 ms  | 226 ms: 1.54x faster  |
| async_tree_none            | 267 ms  | 187 ms: 1.43x faster  |
| async_tree_memoization_tg  | 304 ms  | 216 ms: 1.41x faster  |
| async_tree_io_tg           | 576 ms  | 410 ms: 1.40x faster  |
| async_tree_memoization     | 313 ms  | 224 ms: 1.39x faster  |
| async_tree_none_tg         | 243 ms  | 176 ms: 1.38x faster  |
| async_tree_io              | 570 ms  | 423 ms: 1.35x faster  |
| async_tree_cpu_io_mixed    | 455 ms  | 339 ms: 1.34x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms  | 343 ms: 1.29x faster  |
| asyncio_websockets         | 330 ms  | 318 ms: 1.04x faster  |
| Geometric mean             | (ref)   | 1.38x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | Ex      | PGO                   |
|----------------|:-------:|:---------------------:|
| float          | 78.0 ms | 47.8 ms: 1.63x faster |
| nbody          | 103 ms  | 74.1 ms: 1.40x faster |
| pidigits       | 156 ms  | 152 ms: 1.03x faster  |
| Geometric mean | (ref)   | 1.33x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | Ex      | PGO                   |
|----------------|:-------:|:---------------------:|
| regex_compile  | 130 ms  | 88.2 ms: 1.47x faster |
| regex_effbot   | 1.87 ms | 1.42 ms: 1.31x faster |
| regex_v8       | 17.5 ms | 13.5 ms: 1.29x faster |
| regex_dna      | 123 ms  | 112 ms: 1.10x faster  |
| Geometric mean | (ref)   | 1.29x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | Ex       | PGO                    |
|----------------------|:--------:|:----------------------:|
| unpickle_pure_python | 284 us   | 155 us: 1.83x faster   |
| xml_etree_process    | 66.9 ms  | 41.5 ms: 1.61x faster  |
| json_loads           | 23.3 us  | 14.7 us: 1.58x faster  |
| xml_etree_generate   | 92.6 ms  | 58.7 ms: 1.58x faster  |
| pickle_pure_python   | 364 us   | 237 us: 1.54x faster   |
| xml_etree_iterparse  | 94.3 ms  | 63.7 ms: 1.48x faster  |
| tomli_loads          | 2.07 sec | 1.47 sec: 1.41x faster |
| json_dumps           | 9.44 ms  | 7.05 ms: 1.34x faster  |
| xml_etree_parse      | 112 ms   | 91.2 ms: 1.23x faster  |
| Geometric mean       | (ref)    | 1.50x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | Ex      | PGO                   |
|------------------------|:-------:|:---------------------:|
| python_startup         | 29.5 ms | 26.1 ms: 1.13x faster |
| python_startup_no_site | 22.0 ms | 19.8 ms: 1.11x faster |
| Geometric mean         | (ref)   | 1.12x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | Ex      | PGO                   |
|-----------------|:-------:|:---------------------:|
| mako            | 12.1 ms | 6.86 ms: 1.76x faster |
| django_template | 38.0 ms | 25.1 ms: 1.51x faster |
| genshi_text     | 23.9 ms | 16.5 ms: 1.45x faster |
| genshi_xml      | 50.4 ms | 36.3 ms: 1.39x faster |
| Geometric mean  | (ref)   | 1.52x faster          |

All benchmarks:
===============

| Benchmark                  | Ex       | PGO                    |
|----------------------------|:--------:|:----------------------:|
| richards_super             | 67.7 ms  | 35.1 ms: 1.93x faster  |
| richards                   | 59.0 ms  | 30.7 ms: 1.92x faster  |
| logging_silent             | 124 ns   | 65.2 ns: 1.91x faster  |
| generators                 | 35.6 ms  | 19.3 ms: 1.84x faster  |
| deltablue                  | 4.22 ms  | 2.29 ms: 1.84x faster  |
| unpickle_pure_python       | 284 us   | 155 us: 1.83x faster   |
| scimark_lu                 | 119 ms   | 66.9 ms: 1.79x faster  |
| comprehensions             | 20.1 us  | 11.3 us: 1.78x faster  |
| mako                       | 12.1 ms  | 6.86 ms: 1.76x faster  |
| hexiom                     | 7.44 ms  | 4.38 ms: 1.70x faster  |
| coroutines                 | 22.4 ms  | 13.5 ms: 1.66x faster  |
| spectral_norm              | 102 ms   | 61.5 ms: 1.65x faster  |
| raytrace                   | 313 ms   | 191 ms: 1.64x faster   |
| float                      | 78.0 ms  | 47.8 ms: 1.63x faster  |
| scimark_sparse_mat_mult    | 4.43 ms  | 2.72 ms: 1.63x faster  |
| deepcopy_memo              | 34.0 us  | 21.0 us: 1.62x faster  |
| xml_etree_process          | 66.9 ms  | 41.5 ms: 1.61x faster  |
| scimark_monte_carlo        | 75.8 ms  | 47.1 ms: 1.61x faster  |
| crypto_pyaes               | 80.1 ms  | 50.0 ms: 1.60x faster  |
| chaos                      | 69.3 ms  | 43.6 ms: 1.59x faster  |
| go                         | 140 ms   | 88.6 ms: 1.58x faster  |
| json_loads                 | 23.3 us  | 14.7 us: 1.58x faster  |
| gc_traversal               | 3.25 ms  | 2.06 ms: 1.58x faster  |
| xml_etree_generate         | 92.6 ms  | 58.7 ms: 1.58x faster  |
| sqlglot_v2_parse           | 1.41 ms  | 892 us: 1.58x faster   |
| pickle_pure_python         | 364 us   | 237 us: 1.54x faster   |
| async_generators           | 348 ms   | 226 ms: 1.54x faster   |
| sqlglot_v2_transpile       | 1.69 ms  | 1.10 ms: 1.53x faster  |
| nqueens                    | 96.9 ms  | 63.6 ms: 1.52x faster  |
| scimark_sor                | 139 ms   | 91.0 ms: 1.52x faster  |
| pyflate                    | 477 ms   | 315 ms: 1.51x faster   |
| django_template            | 38.0 ms  | 25.1 ms: 1.51x faster  |
| sqlglot_v2_optimize        | 52.8 ms  | 35.0 ms: 1.51x faster  |
| bpe_tokeniser              | 4.45 sec | 2.96 sec: 1.50x faster |
| sqlglot_v2_normalize       | 109 ms   | 73.6 ms: 1.48x faster  |
| xml_etree_iterparse        | 94.3 ms  | 63.7 ms: 1.48x faster  |
| pprint_safe_repr           | 825 ms   | 558 ms: 1.48x faster   |
| bench_thread_pool          | 1.28 ms  | 864 us: 1.48x faster   |
| deepcopy_reduce            | 2.86 us  | 1.94 us: 1.48x faster  |
| pprint_pformat             | 1.66 sec | 1.13 sec: 1.47x faster |
| regex_compile              | 130 ms   | 88.2 ms: 1.47x faster  |
| deepcopy                   | 278 us   | 190 us: 1.47x faster   |
| typing_runtime_protocols   | 154 us   | 106 us: 1.45x faster   |
| genshi_text                | 23.9 ms  | 16.5 ms: 1.45x faster  |
| scimark_fft                | 276 ms   | 192 ms: 1.43x faster   |
| async_tree_none            | 267 ms   | 187 ms: 1.43x faster   |
| logging_simple             | 9.30 us  | 6.53 us: 1.42x faster  |
| sphinx                     | 933 ms   | 658 ms: 1.42x faster   |
| fannkuch                   | 418 ms   | 296 ms: 1.41x faster   |
| logging_format             | 9.92 us  | 7.03 us: 1.41x faster  |
| tomli_loads                | 2.07 sec | 1.47 sec: 1.41x faster |
| async_tree_memoization_tg  | 304 ms   | 216 ms: 1.41x faster   |
| async_tree_io_tg           | 576 ms   | 410 ms: 1.40x faster   |
| sympy_str                  | 247 ms   | 176 ms: 1.40x faster   |
| thrift                     | 710 us   | 507 us: 1.40x faster   |
| nbody                      | 103 ms   | 74.1 ms: 1.40x faster  |
| async_tree_memoization     | 313 ms   | 224 ms: 1.39x faster   |
| genshi_xml                 | 50.4 ms  | 36.3 ms: 1.39x faster  |
| sympy_expand               | 419 ms   | 302 ms: 1.39x faster   |
| async_tree_none_tg         | 243 ms   | 176 ms: 1.38x faster   |
| pycparser                  | 1.01 sec | 738 ms: 1.37x faster   |
| docutils                   | 2.31 sec | 1.68 sec: 1.37x faster |
| sympy_sum                  | 123 ms   | 90.5 ms: 1.36x faster  |
| sympy_integrate            | 18.4 ms  | 13.5 ms: 1.36x faster  |
| coverage                   | 63.7 ms  | 46.8 ms: 1.36x faster  |
| 2to3                       | 309 ms   | 227 ms: 1.36x faster   |
| async_tree_io              | 570 ms   | 423 ms: 1.35x faster   |
| async_tree_cpu_io_mixed    | 455 ms   | 339 ms: 1.34x faster   |
| telco                      | 6.56 ms  | 4.89 ms: 1.34x faster  |
| json_dumps                 | 9.44 ms  | 7.05 ms: 1.34x faster  |
| pylint                     | 269 ms   | 201 ms: 1.34x faster   |
| subparsers                 | 21.5 ms  | 16.1 ms: 1.34x faster  |
| regex_effbot               | 1.87 ms  | 1.42 ms: 1.31x faster  |
| json                       | 4.07 ms  | 3.14 ms: 1.30x faster  |
| async_tree_cpu_io_mixed_tg | 444 ms   | 343 ms: 1.29x faster   |
| meteor_contest             | 99.5 ms  | 76.9 ms: 1.29x faster  |
| regex_v8                   | 17.5 ms  | 13.5 ms: 1.29x faster  |
| html5lib                   | 52.5 ms  | 40.8 ms: 1.29x faster  |
| many_optionals             | 559 us   | 438 us: 1.28x faster   |
| k_core                     | 2.18 sec | 1.73 sec: 1.26x faster |
| xml_etree_parse            | 112 ms   | 91.2 ms: 1.23x faster  |
| sqlite_synth               | 1.96 us  | 1.59 us: 1.23x faster  |
| shortest_path              | 437 ms   | 359 ms: 1.22x faster   |
| dulwich_log                | 52.4 ms  | 43.4 ms: 1.21x faster  |
| connected_components       | 395 ms   | 329 ms: 1.20x faster   |
| pathlib                    | 37.5 ms  | 32.1 ms: 1.17x faster  |
| mdp                        | 1.89 sec | 1.64 sec: 1.15x faster |
| bench_mp_pool              | 101 ms   | 88.7 ms: 1.14x faster  |
| create_gc_cycles           | 1.42 ms  | 1.25 ms: 1.13x faster  |
| python_startup             | 29.5 ms  | 26.1 ms: 1.13x faster  |
| python_startup_no_site     | 22.0 ms  | 19.8 ms: 1.11x faster  |
| regex_dna                  | 123 ms   | 112 ms: 1.10x faster   |
| asyncio_websockets         | 330 ms   | 318 ms: 1.04x faster   |
| pidigits                   | 156 ms   | 152 ms: 1.03x faster   |
| Geometric mean             | (ref)    | 1.43x faster           |

- Geometric mean (including insignificant results): 1.432x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown