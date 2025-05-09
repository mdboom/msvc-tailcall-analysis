# Results vs. base

- fork: unknown
- ref: TC-PGO-Ex2
- machine: unknown-unknown
- commit hash: 2ea41232d0
- commit date: 2025-03-12
- overall geometric mean: 1.147x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex2             |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 216 ms: 1.10x faster   |
| docutils       | 1.81 sec    | 1.63 sec: 1.12x faster |
| html5lib       | 40.8 ms     | 36.1 ms: 1.13x faster  |
| sphinx         | 723 ms      | 638 ms: 1.13x faster   |
| Geometric mean | (ref)       | 1.12x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex2            |
|----------------------------|:-----------:|:---------------------:|
| async_tree_io              | 429 ms      | 375 ms: 1.15x faster  |
| async_tree_io_tg           | 419 ms      | 371 ms: 1.13x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 328 ms: 1.12x faster  |
| async_tree_none_tg         | 178 ms      | 159 ms: 1.11x faster  |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster  |
| async_tree_memoization     | 227 ms      | 205 ms: 1.11x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 329 ms: 1.10x faster  |
| async_generators           | 224 ms      | 206 ms: 1.09x faster  |
| coroutines                 | 13.5 ms     | 12.4 ms: 1.08x faster |
| async_tree_memoization_tg  | 218 ms      | 209 ms: 1.05x faster  |
| asyncio_websockets         | 304 ms      | 317 ms: 1.04x slower  |
| Geometric mean             | (ref)       | 1.09x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex2            |
|----------------|:-----------:|:---------------------:|
| float          | 44.8 ms     | 40.2 ms: 1.11x faster |
| nbody          | 58.8 ms     | 53.3 ms: 1.10x faster |
| Geometric mean | (ref)       | 1.07x faster          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TC-PGO-Ex2            |
|----------------|:-----------:|:---------------------:|
| regex_effbot   | 1.76 ms     | 1.40 ms: 1.26x faster |
| regex_v8       | 16.7 ms     | 14.1 ms: 1.18x faster |
| regex_compile  | 88.0 ms     | 74.8 ms: 1.18x faster |
| regex_dna      | 117 ms      | 115 ms: 1.02x faster  |
| Geometric mean | (ref)       | 1.16x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TC-PGO-Ex2             |
|----------------------|:-----------:|:----------------------:|
| json_loads           | 21.1 us     | 14.5 us: 1.46x faster  |
| xml_etree_generate   | 66.8 ms     | 51.5 ms: 1.30x faster  |
| xml_etree_process    | 46.5 ms     | 36.7 ms: 1.27x faster  |
| unpickle_pure_python | 154 us      | 123 us: 1.26x faster   |
| json_dumps           | 7.94 ms     | 6.48 ms: 1.22x faster  |
| xml_etree_iterparse  | 71.5 ms     | 60.4 ms: 1.18x faster  |
| tomli_loads          | 1.38 sec    | 1.17 sec: 1.18x faster |
| pickle_pure_python   | 236 us      | 201 us: 1.17x faster   |
| xml_etree_parse      | 104 ms      | 89.0 ms: 1.16x faster  |
| Geometric mean       | (ref)       | 1.24x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TC-PGO-Ex2            |
|------------------------|:-----------:|:---------------------:|
| python_startup         | 26.9 ms     | 26.0 ms: 1.03x faster |
| python_startup_no_site | 20.1 ms     | 19.6 ms: 1.03x faster |
| Geometric mean         | (ref)       | 1.03x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TC-PGO-Ex2            |
|-----------------|:-----------:|:---------------------:|
| mako            | 7.44 ms     | 6.12 ms: 1.21x faster |
| django_template | 27.5 ms     | 23.4 ms: 1.18x faster |
| genshi_xml      | 35.3 ms     | 30.7 ms: 1.15x faster |
| genshi_text     | 16.2 ms     | 14.2 ms: 1.14x faster |
| Geometric mean  | (ref)       | 1.17x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TC-PGO-Ex2             |
|----------------------------|:-----------:|:----------------------:|
| json_loads                 | 21.1 us     | 14.5 us: 1.46x faster  |
| gc_traversal               | 2.77 ms     | 2.07 ms: 1.34x faster  |
| xml_etree_generate         | 66.8 ms     | 51.5 ms: 1.30x faster  |
| deepcopy_reduce            | 2.12 us     | 1.66 us: 1.28x faster  |
| xml_etree_process          | 46.5 ms     | 36.7 ms: 1.27x faster  |
| json                       | 3.77 ms     | 2.98 ms: 1.27x faster  |
| regex_effbot               | 1.76 ms     | 1.40 ms: 1.26x faster  |
| richards                   | 35.0 ms     | 27.8 ms: 1.26x faster  |
| comprehensions             | 12.2 us     | 9.73 us: 1.26x faster  |
| richards_super             | 40.4 ms     | 32.2 ms: 1.26x faster  |
| unpickle_pure_python       | 154 us      | 123 us: 1.26x faster   |
| deepcopy_memo              | 21.3 us     | 17.0 us: 1.25x faster  |
| deepcopy                   | 199 us      | 160 us: 1.24x faster   |
| json_dumps                 | 7.94 ms     | 6.48 ms: 1.22x faster  |
| generators                 | 18.1 ms     | 14.8 ms: 1.22x faster  |
| nqueens                    | 65.7 ms     | 54.0 ms: 1.22x faster  |
| mako                       | 7.44 ms     | 6.12 ms: 1.21x faster  |
| sympy_expand               | 324 ms      | 269 ms: 1.20x faster   |
| hexiom                     | 4.17 ms     | 3.47 ms: 1.20x faster  |
| scimark_lu                 | 65.2 ms     | 54.4 ms: 1.20x faster  |
| sqlglot_v2_optimize        | 38.4 ms     | 32.2 ms: 1.19x faster  |
| crypto_pyaes               | 49.3 ms     | 41.6 ms: 1.18x faster  |
| sqlglot_v2_parse           | 876 us      | 740 us: 1.18x faster   |
| xml_etree_iterparse        | 71.5 ms     | 60.4 ms: 1.18x faster  |
| regex_v8                   | 16.7 ms     | 14.1 ms: 1.18x faster  |
| sympy_str                  | 187 ms      | 158 ms: 1.18x faster   |
| sqlglot_v2_normalize       | 79.0 ms     | 66.9 ms: 1.18x faster  |
| logging_silent             | 62.9 ns     | 53.3 ns: 1.18x faster  |
| tomli_loads                | 1.38 sec    | 1.17 sec: 1.18x faster |
| regex_compile              | 88.0 ms     | 74.8 ms: 1.18x faster  |
| sympy_sum                  | 96.6 ms     | 82.1 ms: 1.18x faster  |
| django_template            | 27.5 ms     | 23.4 ms: 1.18x faster  |
| telco                      | 5.33 ms     | 4.54 ms: 1.17x faster  |
| sqlglot_v2_transpile       | 1.09 ms     | 933 us: 1.17x faster   |
| bpe_tokeniser              | 3.17 sec    | 2.71 sec: 1.17x faster |
| pickle_pure_python         | 236 us      | 201 us: 1.17x faster   |
| scimark_fft                | 178 ms      | 152 ms: 1.17x faster   |
| pprint_safe_repr           | 558 ms      | 478 ms: 1.17x faster   |
| pprint_pformat             | 1.13 sec    | 968 ms: 1.17x faster   |
| thrift                     | 561 us      | 482 us: 1.17x faster   |
| xml_etree_parse            | 104 ms      | 89.0 ms: 1.16x faster  |
| scimark_monte_carlo        | 42.9 ms     | 37.0 ms: 1.16x faster  |
| chaos                      | 41.4 ms     | 35.9 ms: 1.16x faster  |
| logging_simple             | 6.67 us     | 5.78 us: 1.15x faster  |
| pycparser                  | 765 ms      | 664 ms: 1.15x faster   |
| genshi_xml                 | 35.3 ms     | 30.7 ms: 1.15x faster  |
| async_tree_io              | 429 ms      | 375 ms: 1.15x faster   |
| spectral_norm              | 58.4 ms     | 51.1 ms: 1.14x faster  |
| go                         | 78.0 ms     | 68.4 ms: 1.14x faster  |
| coverage                   | 56.4 ms     | 49.5 ms: 1.14x faster  |
| typing_runtime_protocols   | 113 us      | 98.9 us: 1.14x faster  |
| genshi_text                | 16.2 ms     | 14.2 ms: 1.14x faster  |
| pyflate                    | 295 ms      | 260 ms: 1.14x faster   |
| sympy_integrate            | 13.9 ms     | 12.2 ms: 1.14x faster  |
| sphinx                     | 723 ms      | 638 ms: 1.13x faster   |
| logging_format             | 7.18 us     | 6.34 us: 1.13x faster  |
| html5lib                   | 40.8 ms     | 36.1 ms: 1.13x faster  |
| async_tree_io_tg           | 419 ms      | 371 ms: 1.13x faster   |
| deltablue                  | 2.09 ms     | 1.85 ms: 1.13x faster  |
| raytrace                   | 187 ms      | 166 ms: 1.12x faster   |
| meteor_contest             | 78.1 ms     | 69.5 ms: 1.12x faster  |
| fannkuch                   | 265 ms      | 236 ms: 1.12x faster   |
| mdp                        | 1.57 sec    | 1.40 sec: 1.12x faster |
| async_tree_cpu_io_mixed_tg | 367 ms      | 328 ms: 1.12x faster   |
| docutils                   | 1.81 sec    | 1.63 sec: 1.12x faster |
| float                      | 44.8 ms     | 40.2 ms: 1.11x faster  |
| async_tree_none_tg         | 178 ms      | 159 ms: 1.11x faster   |
| async_tree_none            | 188 ms      | 170 ms: 1.11x faster   |
| async_tree_memoization     | 227 ms      | 205 ms: 1.11x faster   |
| nbody                      | 58.8 ms     | 53.3 ms: 1.10x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 329 ms: 1.10x faster   |
| 2to3                       | 237 ms      | 216 ms: 1.10x faster   |
| scimark_sor                | 73.9 ms     | 67.5 ms: 1.10x faster  |
| scimark_sparse_mat_mult    | 2.48 ms     | 2.26 ms: 1.09x faster  |
| create_gc_cycles           | 1.38 ms     | 1.27 ms: 1.09x faster  |
| pylint                     | 217 ms      | 199 ms: 1.09x faster   |
| dulwich_log                | 43.0 ms     | 39.5 ms: 1.09x faster  |
| async_generators           | 224 ms      | 206 ms: 1.09x faster   |
| coroutines                 | 13.5 ms     | 12.4 ms: 1.08x faster  |
| sqlite_synth               | 1.68 us     | 1.56 us: 1.08x faster  |
| many_optionals             | 813 us      | 761 us: 1.07x faster   |
| bench_mp_pool              | 95.0 ms     | 89.1 ms: 1.07x faster  |
| bench_thread_pool          | 906 us      | 851 us: 1.06x faster   |
| pathlib                    | 25.6 ms     | 24.3 ms: 1.05x faster  |
| subparsers                 | 47.1 ms     | 44.9 ms: 1.05x faster  |
| async_tree_memoization_tg  | 218 ms      | 209 ms: 1.05x faster   |
| python_startup             | 26.9 ms     | 26.0 ms: 1.03x faster  |
| python_startup_no_site     | 20.1 ms     | 19.6 ms: 1.03x faster  |
| k_core                     | 1.76 sec    | 1.71 sec: 1.03x faster |
| shortest_path              | 357 ms      | 348 ms: 1.03x faster   |
| regex_dna                  | 117 ms      | 115 ms: 1.02x faster   |
| connected_components       | 326 ms      | 321 ms: 1.01x faster   |
| asyncio_websockets         | 304 ms      | 317 ms: 1.04x slower   |
| Geometric mean             | (ref)       | 1.15x faster           |

Benchmark hidden because not significant (1): pidigits

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown