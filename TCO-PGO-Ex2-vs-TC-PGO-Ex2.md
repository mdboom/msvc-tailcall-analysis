# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.128x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex2            |
|----------------|:----------:|:----------------------:|
| 2to3           | 216 ms     | 237 ms: 1.10x slower   |
| docutils       | 1.63 sec   | 1.81 sec: 1.12x slower |
| html5lib       | 36.1 ms    | 40.8 ms: 1.13x slower  |
| sphinx         | 638 ms     | 723 ms: 1.13x slower   |
| Geometric mean | (ref)      | 1.12x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-PGO-Ex2 | TCO-PGO-Ex2           |
|----------------------------|:----------:|:---------------------:|
| asyncio_websockets         | 317 ms     | 304 ms: 1.04x faster  |
| async_tree_memoization_tg  | 209 ms     | 218 ms: 1.05x slower  |
| coroutines                 | 12.4 ms    | 13.5 ms: 1.08x slower |
| async_generators           | 206 ms     | 224 ms: 1.09x slower  |
| async_tree_cpu_io_mixed    | 329 ms     | 362 ms: 1.10x slower  |
| async_tree_memoization     | 205 ms     | 227 ms: 1.11x slower  |
| async_tree_none            | 170 ms     | 188 ms: 1.11x slower  |
| async_tree_none_tg         | 159 ms     | 178 ms: 1.11x slower  |
| async_tree_cpu_io_mixed_tg | 328 ms     | 367 ms: 1.12x slower  |
| async_tree_io_tg           | 371 ms     | 419 ms: 1.13x slower  |
| async_tree_io              | 375 ms     | 429 ms: 1.15x slower  |
| Geometric mean             | (ref)      | 1.09x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| nbody          | 53.3 ms    | 58.8 ms: 1.10x slower |
| float          | 40.2 ms    | 44.8 ms: 1.11x slower |
| Geometric mean | (ref)      | 1.07x slower          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-PGO-Ex2 | TCO-PGO-Ex2           |
|----------------|:----------:|:---------------------:|
| regex_dna      | 115 ms     | 117 ms: 1.02x slower  |
| regex_compile  | 74.8 ms    | 88.0 ms: 1.18x slower |
| regex_v8       | 14.1 ms    | 16.7 ms: 1.18x slower |
| regex_effbot   | 1.40 ms    | 1.76 ms: 1.26x slower |
| Geometric mean | (ref)      | 1.16x slower          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-PGO-Ex2 | TCO-PGO-Ex2            |
|----------------------|:----------:|:----------------------:|
| xml_etree_parse      | 89.0 ms    | 104 ms: 1.16x slower   |
| pickle_pure_python   | 201 us     | 236 us: 1.17x slower   |
| tomli_loads          | 1.17 sec   | 1.38 sec: 1.18x slower |
| xml_etree_iterparse  | 60.4 ms    | 71.5 ms: 1.18x slower  |
| json_dumps           | 6.48 ms    | 7.94 ms: 1.22x slower  |
| unpickle_pure_python | 123 us     | 154 us: 1.26x slower   |
| xml_etree_process    | 36.7 ms    | 46.5 ms: 1.27x slower  |
| xml_etree_generate   | 51.5 ms    | 66.8 ms: 1.30x slower  |
| json_loads           | 14.5 us    | 21.1 us: 1.46x slower  |
| Geometric mean       | (ref)      | 1.24x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-PGO-Ex2 | TCO-PGO-Ex2           |
|------------------------|:----------:|:---------------------:|
| python_startup_no_site | 19.6 ms    | 20.1 ms: 1.03x slower |
| python_startup         | 26.0 ms    | 26.9 ms: 1.03x slower |
| Geometric mean         | (ref)      | 1.03x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-PGO-Ex2 | TCO-PGO-Ex2           |
|-----------------|:----------:|:---------------------:|
| genshi_text     | 14.2 ms    | 16.2 ms: 1.14x slower |
| genshi_xml      | 30.7 ms    | 35.3 ms: 1.15x slower |
| django_template | 23.4 ms    | 27.5 ms: 1.18x slower |
| mako            | 6.12 ms    | 7.44 ms: 1.21x slower |
| Geometric mean  | (ref)      | 1.17x slower          |

All benchmarks:
===============

| Benchmark                  | TC-PGO-Ex2 | TCO-PGO-Ex2            |
|----------------------------|:----------:|:----------------------:|
| asyncio_websockets         | 317 ms     | 304 ms: 1.04x faster   |
| connected_components       | 321 ms     | 326 ms: 1.01x slower   |
| regex_dna                  | 115 ms     | 117 ms: 1.02x slower   |
| shortest_path              | 348 ms     | 357 ms: 1.03x slower   |
| k_core                     | 1.71 sec   | 1.76 sec: 1.03x slower |
| python_startup_no_site     | 19.6 ms    | 20.1 ms: 1.03x slower  |
| python_startup             | 26.0 ms    | 26.9 ms: 1.03x slower  |
| async_tree_memoization_tg  | 209 ms     | 218 ms: 1.05x slower   |
| subparsers                 | 44.9 ms    | 47.1 ms: 1.05x slower  |
| pathlib                    | 24.3 ms    | 25.6 ms: 1.05x slower  |
| bench_thread_pool          | 851 us     | 906 us: 1.06x slower   |
| bench_mp_pool              | 89.1 ms    | 95.0 ms: 1.07x slower  |
| many_optionals             | 761 us     | 813 us: 1.07x slower   |
| sqlite_synth               | 1.56 us    | 1.68 us: 1.08x slower  |
| coroutines                 | 12.4 ms    | 13.5 ms: 1.08x slower  |
| async_generators           | 206 ms     | 224 ms: 1.09x slower   |
| dulwich_log                | 39.5 ms    | 43.0 ms: 1.09x slower  |
| pylint                     | 199 ms     | 217 ms: 1.09x slower   |
| create_gc_cycles           | 1.27 ms    | 1.38 ms: 1.09x slower  |
| scimark_sparse_mat_mult    | 2.26 ms    | 2.48 ms: 1.09x slower  |
| scimark_sor                | 67.5 ms    | 73.9 ms: 1.10x slower  |
| 2to3                       | 216 ms     | 237 ms: 1.10x slower   |
| async_tree_cpu_io_mixed    | 329 ms     | 362 ms: 1.10x slower   |
| nbody                      | 53.3 ms    | 58.8 ms: 1.10x slower  |
| async_tree_memoization     | 205 ms     | 227 ms: 1.11x slower   |
| async_tree_none            | 170 ms     | 188 ms: 1.11x slower   |
| async_tree_none_tg         | 159 ms     | 178 ms: 1.11x slower   |
| float                      | 40.2 ms    | 44.8 ms: 1.11x slower  |
| docutils                   | 1.63 sec   | 1.81 sec: 1.12x slower |
| async_tree_cpu_io_mixed_tg | 328 ms     | 367 ms: 1.12x slower   |
| mdp                        | 1.40 sec   | 1.57 sec: 1.12x slower |
| fannkuch                   | 236 ms     | 265 ms: 1.12x slower   |
| meteor_contest             | 69.5 ms    | 78.1 ms: 1.12x slower  |
| raytrace                   | 166 ms     | 187 ms: 1.12x slower   |
| deltablue                  | 1.85 ms    | 2.09 ms: 1.13x slower  |
| async_tree_io_tg           | 371 ms     | 419 ms: 1.13x slower   |
| html5lib                   | 36.1 ms    | 40.8 ms: 1.13x slower  |
| logging_format             | 6.34 us    | 7.18 us: 1.13x slower  |
| sphinx                     | 638 ms     | 723 ms: 1.13x slower   |
| sympy_integrate            | 12.2 ms    | 13.9 ms: 1.14x slower  |
| pyflate                    | 260 ms     | 295 ms: 1.14x slower   |
| genshi_text                | 14.2 ms    | 16.2 ms: 1.14x slower  |
| typing_runtime_protocols   | 98.9 us    | 113 us: 1.14x slower   |
| coverage                   | 49.5 ms    | 56.4 ms: 1.14x slower  |
| go                         | 68.4 ms    | 78.0 ms: 1.14x slower  |
| spectral_norm              | 51.1 ms    | 58.4 ms: 1.14x slower  |
| async_tree_io              | 375 ms     | 429 ms: 1.15x slower   |
| genshi_xml                 | 30.7 ms    | 35.3 ms: 1.15x slower  |
| pycparser                  | 664 ms     | 765 ms: 1.15x slower   |
| logging_simple             | 5.78 us    | 6.67 us: 1.15x slower  |
| chaos                      | 35.9 ms    | 41.4 ms: 1.16x slower  |
| scimark_monte_carlo        | 37.0 ms    | 42.9 ms: 1.16x slower  |
| xml_etree_parse            | 89.0 ms    | 104 ms: 1.16x slower   |
| thrift                     | 482 us     | 561 us: 1.17x slower   |
| pprint_pformat             | 968 ms     | 1.13 sec: 1.17x slower |
| pprint_safe_repr           | 478 ms     | 558 ms: 1.17x slower   |
| scimark_fft                | 152 ms     | 178 ms: 1.17x slower   |
| pickle_pure_python         | 201 us     | 236 us: 1.17x slower   |
| bpe_tokeniser              | 2.71 sec   | 3.17 sec: 1.17x slower |
| sqlglot_v2_transpile       | 933 us     | 1.09 ms: 1.17x slower  |
| telco                      | 4.54 ms    | 5.33 ms: 1.17x slower  |
| django_template            | 23.4 ms    | 27.5 ms: 1.18x slower  |
| sympy_sum                  | 82.1 ms    | 96.6 ms: 1.18x slower  |
| regex_compile              | 74.8 ms    | 88.0 ms: 1.18x slower  |
| tomli_loads                | 1.17 sec   | 1.38 sec: 1.18x slower |
| logging_silent             | 53.3 ns    | 62.9 ns: 1.18x slower  |
| sqlglot_v2_normalize       | 66.9 ms    | 79.0 ms: 1.18x slower  |
| sympy_str                  | 158 ms     | 187 ms: 1.18x slower   |
| regex_v8                   | 14.1 ms    | 16.7 ms: 1.18x slower  |
| xml_etree_iterparse        | 60.4 ms    | 71.5 ms: 1.18x slower  |
| sqlglot_v2_parse           | 740 us     | 876 us: 1.18x slower   |
| crypto_pyaes               | 41.6 ms    | 49.3 ms: 1.18x slower  |
| sqlglot_v2_optimize        | 32.2 ms    | 38.4 ms: 1.19x slower  |
| scimark_lu                 | 54.4 ms    | 65.2 ms: 1.20x slower  |
| hexiom                     | 3.47 ms    | 4.17 ms: 1.20x slower  |
| sympy_expand               | 269 ms     | 324 ms: 1.20x slower   |
| mako                       | 6.12 ms    | 7.44 ms: 1.21x slower  |
| nqueens                    | 54.0 ms    | 65.7 ms: 1.22x slower  |
| generators                 | 14.8 ms    | 18.1 ms: 1.22x slower  |
| json_dumps                 | 6.48 ms    | 7.94 ms: 1.22x slower  |
| deepcopy                   | 160 us     | 199 us: 1.24x slower   |
| deepcopy_memo              | 17.0 us    | 21.3 us: 1.25x slower  |
| unpickle_pure_python       | 123 us     | 154 us: 1.26x slower   |
| richards_super             | 32.2 ms    | 40.4 ms: 1.26x slower  |
| comprehensions             | 9.73 us    | 12.2 us: 1.26x slower  |
| richards                   | 27.8 ms    | 35.0 ms: 1.26x slower  |
| regex_effbot               | 1.40 ms    | 1.76 ms: 1.26x slower  |
| json                       | 2.98 ms    | 3.77 ms: 1.27x slower  |
| xml_etree_process          | 36.7 ms    | 46.5 ms: 1.27x slower  |
| deepcopy_reduce            | 1.66 us    | 2.12 us: 1.28x slower  |
| xml_etree_generate         | 51.5 ms    | 66.8 ms: 1.30x slower  |
| gc_traversal               | 2.07 ms    | 2.77 ms: 1.34x slower  |
| json_loads                 | 14.5 us    | 21.1 us: 1.46x slower  |
| Geometric mean             | (ref)      | 1.15x slower           |

Benchmark hidden because not significant (1): pidigits

- Geometric mean (including insignificant results): 1.128x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown