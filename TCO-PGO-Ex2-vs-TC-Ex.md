# Results vs. base

- fork: unknown
- ref: TCO-PGO-Ex2
- machine: unknown-unknown
- commit hash: 8ccca92eec
- commit date: 2025-03-26
- overall geometric mean: 1.049x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-Ex    | TCO-PGO-Ex2            |
|----------------|:--------:|:----------------------:|
| 2to3           | 231 ms   | 237 ms: 1.03x slower   |
| docutils       | 1.77 sec | 1.81 sec: 1.03x slower |
| html5lib       | 38.8 ms  | 40.8 ms: 1.05x slower  |
| sphinx         | 702 ms   | 723 ms: 1.03x slower   |
| Geometric mean | (ref)    | 1.03x slower           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-Ex   | TCO-PGO-Ex2           |
|----------------------------|:-------:|:---------------------:|
| asyncio_websockets         | 312 ms  | 304 ms: 1.03x faster  |
| async_tree_cpu_io_mixed    | 359 ms  | 362 ms: 1.01x slower  |
| async_tree_cpu_io_mixed_tg | 363 ms  | 367 ms: 1.01x slower  |
| async_tree_memoization_tg  | 210 ms  | 218 ms: 1.04x slower  |
| async_generators           | 213 ms  | 224 ms: 1.05x slower  |
| async_tree_none_tg         | 167 ms  | 178 ms: 1.06x slower  |
| async_tree_memoization     | 210 ms  | 227 ms: 1.08x slower  |
| async_tree_none            | 174 ms  | 188 ms: 1.08x slower  |
| async_tree_io_tg           | 385 ms  | 419 ms: 1.09x slower  |
| coroutines                 | 12.3 ms | 13.5 ms: 1.10x slower |
| async_tree_io              | 384 ms  | 429 ms: 1.12x slower  |
| Geometric mean             | (ref)   | 1.05x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-Ex   | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| pidigits       | 146 ms  | 147 ms: 1.01x slower  |
| float          | 41.4 ms | 44.8 ms: 1.08x slower |
| nbody          | 53.1 ms | 58.8 ms: 1.11x slower |
| Geometric mean | (ref)   | 1.06x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-Ex   | TCO-PGO-Ex2           |
|----------------|:-------:|:---------------------:|
| regex_effbot   | 1.85 ms | 1.76 ms: 1.05x faster |
| regex_dna      | 121 ms  | 117 ms: 1.03x faster  |
| regex_compile  | 81.9 ms | 88.0 ms: 1.07x slower |
| Geometric mean | (ref)   | 1.00x slower          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-Ex    | TCO-PGO-Ex2            |
|----------------------|:--------:|:----------------------:|
| json_loads           | 21.9 us  | 21.1 us: 1.04x faster  |
| xml_etree_parse      | 105 ms   | 104 ms: 1.01x faster   |
| xml_etree_iterparse  | 70.4 ms  | 71.5 ms: 1.02x slower  |
| json_dumps           | 7.79 ms  | 7.94 ms: 1.02x slower  |
| xml_etree_generate   | 64.7 ms  | 66.8 ms: 1.03x slower  |
| xml_etree_process    | 44.7 ms  | 46.5 ms: 1.04x slower  |
| unpickle_pure_python | 148 us   | 154 us: 1.04x slower   |
| pickle_pure_python   | 223 us   | 236 us: 1.06x slower   |
| tomli_loads          | 1.26 sec | 1.38 sec: 1.10x slower |
| Geometric mean       | (ref)    | 1.03x slower           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TC-Ex   | TCO-PGO-Ex2           |
|------------------------|:-------:|:---------------------:|
| python_startup         | 26.4 ms | 26.9 ms: 1.02x slower |
| python_startup_no_site | 19.4 ms | 20.1 ms: 1.04x slower |
| Geometric mean         | (ref)   | 1.03x slower          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-Ex   | TCO-PGO-Ex2           |
|-----------------|:-------:|:---------------------:|
| mako            | 7.84 ms | 7.44 ms: 1.05x faster |
| django_template | 25.2 ms | 27.5 ms: 1.09x slower |
| genshi_text     | 14.5 ms | 16.2 ms: 1.12x slower |
| genshi_xml      | 31.3 ms | 35.3 ms: 1.13x slower |
| Geometric mean  | (ref)   | 1.07x slower          |

All benchmarks:
===============

| Benchmark                  | TC-Ex    | TCO-PGO-Ex2            |
|----------------------------|:--------:|:----------------------:|
| mako                       | 7.84 ms  | 7.44 ms: 1.05x faster  |
| regex_effbot               | 1.85 ms  | 1.76 ms: 1.05x faster  |
| json_loads                 | 21.9 us  | 21.1 us: 1.04x faster  |
| regex_dna                  | 121 ms   | 117 ms: 1.03x faster   |
| asyncio_websockets         | 312 ms   | 304 ms: 1.03x faster   |
| gc_traversal               | 2.83 ms  | 2.77 ms: 1.02x faster  |
| xml_etree_parse            | 105 ms   | 104 ms: 1.01x faster   |
| pidigits                   | 146 ms   | 147 ms: 1.01x slower   |
| async_tree_cpu_io_mixed    | 359 ms   | 362 ms: 1.01x slower   |
| async_tree_cpu_io_mixed_tg | 363 ms   | 367 ms: 1.01x slower   |
| telco                      | 5.26 ms  | 5.33 ms: 1.01x slower  |
| bench_mp_pool              | 93.6 ms  | 95.0 ms: 1.01x slower  |
| dulwich_log                | 42.3 ms  | 43.0 ms: 1.02x slower  |
| xml_etree_iterparse        | 70.4 ms  | 71.5 ms: 1.02x slower  |
| scimark_lu                 | 64.2 ms  | 65.2 ms: 1.02x slower  |
| python_startup             | 26.4 ms  | 26.9 ms: 1.02x slower  |
| thrift                     | 551 us   | 561 us: 1.02x slower   |
| pathlib                    | 25.1 ms  | 25.6 ms: 1.02x slower  |
| coverage                   | 55.4 ms  | 56.4 ms: 1.02x slower  |
| json_dumps                 | 7.79 ms  | 7.94 ms: 1.02x slower  |
| docutils                   | 1.77 sec | 1.81 sec: 1.03x slower |
| crypto_pyaes               | 48.0 ms  | 49.3 ms: 1.03x slower  |
| k_core                     | 1.71 sec | 1.76 sec: 1.03x slower |
| 2to3                       | 231 ms   | 237 ms: 1.03x slower   |
| logging_silent             | 61.1 ns  | 62.9 ns: 1.03x slower  |
| shortest_path              | 347 ms   | 357 ms: 1.03x slower   |
| sphinx                     | 702 ms   | 723 ms: 1.03x slower   |
| xml_etree_generate         | 64.7 ms  | 66.8 ms: 1.03x slower  |
| create_gc_cycles           | 1.34 ms  | 1.38 ms: 1.03x slower  |
| bench_thread_pool          | 876 us   | 906 us: 1.03x slower   |
| sympy_integrate            | 13.4 ms  | 13.9 ms: 1.03x slower  |
| python_startup_no_site     | 19.4 ms  | 20.1 ms: 1.04x slower  |
| async_tree_memoization_tg  | 210 ms   | 218 ms: 1.04x slower   |
| xml_etree_process          | 44.7 ms  | 46.5 ms: 1.04x slower  |
| unpickle_pure_python       | 148 us   | 154 us: 1.04x slower   |
| connected_components       | 311 ms   | 326 ms: 1.05x slower   |
| async_generators           | 213 ms   | 224 ms: 1.05x slower   |
| meteor_contest             | 74.5 ms  | 78.1 ms: 1.05x slower  |
| bpe_tokeniser              | 3.01 sec | 3.17 sec: 1.05x slower |
| sympy_str                  | 177 ms   | 187 ms: 1.05x slower   |
| scimark_fft                | 169 ms   | 178 ms: 1.05x slower   |
| html5lib                   | 38.8 ms  | 40.8 ms: 1.05x slower  |
| sympy_sum                  | 91.4 ms  | 96.6 ms: 1.06x slower  |
| fannkuch                   | 250 ms   | 265 ms: 1.06x slower   |
| pickle_pure_python         | 223 us   | 236 us: 1.06x slower   |
| pylint                     | 205 ms   | 217 ms: 1.06x slower   |
| subparsers                 | 44.5 ms  | 47.1 ms: 1.06x slower  |
| async_tree_none_tg         | 167 ms   | 178 ms: 1.06x slower   |
| sqlglot_v2_optimize        | 36.1 ms  | 38.4 ms: 1.06x slower  |
| typing_runtime_protocols   | 106 us   | 113 us: 1.06x slower   |
| hexiom                     | 3.92 ms  | 4.17 ms: 1.06x slower  |
| sympy_expand               | 304 ms   | 324 ms: 1.07x slower   |
| logging_simple             | 6.25 us  | 6.67 us: 1.07x slower  |
| many_optionals             | 762 us   | 813 us: 1.07x slower   |
| logging_format             | 6.70 us  | 7.18 us: 1.07x slower  |
| pycparser                  | 713 ms   | 765 ms: 1.07x slower   |
| regex_compile              | 81.9 ms  | 88.0 ms: 1.07x slower  |
| scimark_sor                | 68.6 ms  | 73.9 ms: 1.08x slower  |
| sqlglot_v2_normalize       | 73.3 ms  | 79.0 ms: 1.08x slower  |
| pyflate                    | 274 ms   | 295 ms: 1.08x slower   |
| sqlglot_v2_transpile       | 1.01 ms  | 1.09 ms: 1.08x slower  |
| float                      | 41.4 ms  | 44.8 ms: 1.08x slower  |
| async_tree_memoization     | 210 ms   | 227 ms: 1.08x slower   |
| comprehensions             | 11.3 us  | 12.2 us: 1.08x slower  |
| async_tree_none            | 174 ms   | 188 ms: 1.08x slower   |
| mdp                        | 1.44 sec | 1.57 sec: 1.09x slower |
| pprint_pformat             | 1.04 sec | 1.13 sec: 1.09x slower |
| async_tree_io_tg           | 385 ms   | 419 ms: 1.09x slower   |
| django_template            | 25.2 ms  | 27.5 ms: 1.09x slower  |
| deltablue                  | 1.91 ms  | 2.09 ms: 1.09x slower  |
| pprint_safe_repr           | 510 ms   | 558 ms: 1.09x slower   |
| coroutines                 | 12.3 ms  | 13.5 ms: 1.10x slower  |
| sqlglot_v2_parse           | 798 us   | 876 us: 1.10x slower   |
| chaos                      | 37.7 ms  | 41.4 ms: 1.10x slower  |
| tomli_loads                | 1.26 sec | 1.38 sec: 1.10x slower |
| scimark_monte_carlo        | 38.9 ms  | 42.9 ms: 1.10x slower  |
| nqueens                    | 59.6 ms  | 65.7 ms: 1.10x slower  |
| deepcopy                   | 180 us   | 199 us: 1.10x slower   |
| raytrace                   | 169 ms   | 187 ms: 1.10x slower   |
| deepcopy_memo              | 19.3 us  | 21.3 us: 1.11x slower  |
| go                         | 70.4 ms  | 78.0 ms: 1.11x slower  |
| nbody                      | 53.1 ms  | 58.8 ms: 1.11x slower  |
| generators                 | 16.3 ms  | 18.1 ms: 1.11x slower  |
| genshi_text                | 14.5 ms  | 16.2 ms: 1.12x slower  |
| async_tree_io              | 384 ms   | 429 ms: 1.12x slower   |
| deepcopy_reduce            | 1.90 us  | 2.12 us: 1.12x slower  |
| genshi_xml                 | 31.3 ms  | 35.3 ms: 1.13x slower  |
| richards_super             | 35.8 ms  | 40.4 ms: 1.13x slower  |
| richards                   | 30.9 ms  | 35.0 ms: 1.13x slower  |
| spectral_norm              | 51.1 ms  | 58.4 ms: 1.14x slower  |
| Geometric mean             | (ref)    | 1.05x slower           |

Benchmark hidden because not significant (4): json, scimark_sparse_mat_mult, sqlite_synth, regex_v8

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown