# Results vs. base

- fork: unknown
- ref: TC-Ex
- machine: unknown-unknown
- commit hash: 06bc3bd2f9
- commit date: 2025-03-07
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-Ex                  |
|----------------|:-----------:|:----------------------:|
| 2to3           | 237 ms      | 231 ms: 1.03x faster   |
| docutils       | 1.81 sec    | 1.77 sec: 1.03x faster |
| html5lib       | 40.8 ms     | 38.8 ms: 1.05x faster  |
| sphinx         | 723 ms      | 702 ms: 1.03x faster   |
| Geometric mean | (ref)       | 1.03x faster           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TCO-PGO-Ex2 | TC-Ex                 |
|----------------------------|:-----------:|:---------------------:|
| async_tree_io              | 429 ms      | 384 ms: 1.12x faster  |
| coroutines                 | 13.5 ms     | 12.3 ms: 1.10x faster |
| async_tree_io_tg           | 419 ms      | 385 ms: 1.09x faster  |
| async_tree_none            | 188 ms      | 174 ms: 1.08x faster  |
| async_tree_memoization     | 227 ms      | 210 ms: 1.08x faster  |
| async_tree_none_tg         | 178 ms      | 167 ms: 1.06x faster  |
| async_generators           | 224 ms      | 213 ms: 1.05x faster  |
| async_tree_memoization_tg  | 218 ms      | 210 ms: 1.04x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 363 ms: 1.01x faster  |
| async_tree_cpu_io_mixed    | 362 ms      | 359 ms: 1.01x faster  |
| asyncio_websockets         | 304 ms      | 312 ms: 1.03x slower  |
| Geometric mean             | (ref)       | 1.05x faster          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TCO-PGO-Ex2 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| nbody          | 58.8 ms     | 53.1 ms: 1.11x faster |
| float          | 44.8 ms     | 41.4 ms: 1.08x faster |
| pidigits       | 147 ms      | 146 ms: 1.01x faster  |
| Geometric mean | (ref)       | 1.06x faster          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TCO-PGO-Ex2 | TC-Ex                 |
|----------------|:-----------:|:---------------------:|
| regex_compile  | 88.0 ms     | 81.9 ms: 1.07x faster |
| regex_dna      | 117 ms      | 121 ms: 1.03x slower  |
| regex_effbot   | 1.76 ms     | 1.85 ms: 1.05x slower |
| Geometric mean | (ref)       | 1.00x faster          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | TCO-PGO-Ex2 | TC-Ex                  |
|----------------------|:-----------:|:----------------------:|
| tomli_loads          | 1.38 sec    | 1.26 sec: 1.10x faster |
| pickle_pure_python   | 236 us      | 223 us: 1.06x faster   |
| unpickle_pure_python | 154 us      | 148 us: 1.04x faster   |
| xml_etree_process    | 46.5 ms     | 44.7 ms: 1.04x faster  |
| xml_etree_generate   | 66.8 ms     | 64.7 ms: 1.03x faster  |
| json_dumps           | 7.94 ms     | 7.79 ms: 1.02x faster  |
| xml_etree_iterparse  | 71.5 ms     | 70.4 ms: 1.02x faster  |
| xml_etree_parse      | 104 ms      | 105 ms: 1.01x slower   |
| json_loads           | 21.1 us     | 21.9 us: 1.04x slower  |
| Geometric mean       | (ref)       | 1.03x faster           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | TCO-PGO-Ex2 | TC-Ex                 |
|------------------------|:-----------:|:---------------------:|
| python_startup_no_site | 20.1 ms     | 19.4 ms: 1.04x faster |
| python_startup         | 26.9 ms     | 26.4 ms: 1.02x faster |
| Geometric mean         | (ref)       | 1.03x faster          |

Benchmarks with tag 'template':
===============================

| Benchmark       | TCO-PGO-Ex2 | TC-Ex                 |
|-----------------|:-----------:|:---------------------:|
| genshi_xml      | 35.3 ms     | 31.3 ms: 1.13x faster |
| genshi_text     | 16.2 ms     | 14.5 ms: 1.12x faster |
| django_template | 27.5 ms     | 25.2 ms: 1.09x faster |
| mako            | 7.44 ms     | 7.84 ms: 1.05x slower |
| Geometric mean  | (ref)       | 1.07x faster          |

All benchmarks:
===============

| Benchmark                  | TCO-PGO-Ex2 | TC-Ex                  |
|----------------------------|:-----------:|:----------------------:|
| spectral_norm              | 58.4 ms     | 51.1 ms: 1.14x faster  |
| richards                   | 35.0 ms     | 30.9 ms: 1.13x faster  |
| richards_super             | 40.4 ms     | 35.8 ms: 1.13x faster  |
| genshi_xml                 | 35.3 ms     | 31.3 ms: 1.13x faster  |
| deepcopy_reduce            | 2.12 us     | 1.90 us: 1.12x faster  |
| async_tree_io              | 429 ms      | 384 ms: 1.12x faster   |
| genshi_text                | 16.2 ms     | 14.5 ms: 1.12x faster  |
| generators                 | 18.1 ms     | 16.3 ms: 1.11x faster  |
| nbody                      | 58.8 ms     | 53.1 ms: 1.11x faster  |
| go                         | 78.0 ms     | 70.4 ms: 1.11x faster  |
| deepcopy_memo              | 21.3 us     | 19.3 us: 1.11x faster  |
| raytrace                   | 187 ms      | 169 ms: 1.10x faster   |
| deepcopy                   | 199 us      | 180 us: 1.10x faster   |
| nqueens                    | 65.7 ms     | 59.6 ms: 1.10x faster  |
| scimark_monte_carlo        | 42.9 ms     | 38.9 ms: 1.10x faster  |
| tomli_loads                | 1.38 sec    | 1.26 sec: 1.10x faster |
| chaos                      | 41.4 ms     | 37.7 ms: 1.10x faster  |
| sqlglot_v2_parse           | 876 us      | 798 us: 1.10x faster   |
| coroutines                 | 13.5 ms     | 12.3 ms: 1.10x faster  |
| pprint_safe_repr           | 558 ms      | 510 ms: 1.09x faster   |
| deltablue                  | 2.09 ms     | 1.91 ms: 1.09x faster  |
| django_template            | 27.5 ms     | 25.2 ms: 1.09x faster  |
| async_tree_io_tg           | 419 ms      | 385 ms: 1.09x faster   |
| pprint_pformat             | 1.13 sec    | 1.04 sec: 1.09x faster |
| mdp                        | 1.57 sec    | 1.44 sec: 1.09x faster |
| async_tree_none            | 188 ms      | 174 ms: 1.08x faster   |
| comprehensions             | 12.2 us     | 11.3 us: 1.08x faster  |
| async_tree_memoization     | 227 ms      | 210 ms: 1.08x faster   |
| float                      | 44.8 ms     | 41.4 ms: 1.08x faster  |
| sqlglot_v2_transpile       | 1.09 ms     | 1.01 ms: 1.08x faster  |
| pyflate                    | 295 ms      | 274 ms: 1.08x faster   |
| sqlglot_v2_normalize       | 79.0 ms     | 73.3 ms: 1.08x faster  |
| scimark_sor                | 73.9 ms     | 68.6 ms: 1.08x faster  |
| regex_compile              | 88.0 ms     | 81.9 ms: 1.07x faster  |
| pycparser                  | 765 ms      | 713 ms: 1.07x faster   |
| logging_format             | 7.18 us     | 6.70 us: 1.07x faster  |
| many_optionals             | 813 us      | 762 us: 1.07x faster   |
| logging_simple             | 6.67 us     | 6.25 us: 1.07x faster  |
| sympy_expand               | 324 ms      | 304 ms: 1.07x faster   |
| hexiom                     | 4.17 ms     | 3.92 ms: 1.06x faster  |
| typing_runtime_protocols   | 113 us      | 106 us: 1.06x faster   |
| sqlglot_v2_optimize        | 38.4 ms     | 36.1 ms: 1.06x faster  |
| async_tree_none_tg         | 178 ms      | 167 ms: 1.06x faster   |
| subparsers                 | 47.1 ms     | 44.5 ms: 1.06x faster  |
| pylint                     | 217 ms      | 205 ms: 1.06x faster   |
| pickle_pure_python         | 236 us      | 223 us: 1.06x faster   |
| fannkuch                   | 265 ms      | 250 ms: 1.06x faster   |
| sympy_sum                  | 96.6 ms     | 91.4 ms: 1.06x faster  |
| html5lib                   | 40.8 ms     | 38.8 ms: 1.05x faster  |
| scimark_fft                | 178 ms      | 169 ms: 1.05x faster   |
| sympy_str                  | 187 ms      | 177 ms: 1.05x faster   |
| bpe_tokeniser              | 3.17 sec    | 3.01 sec: 1.05x faster |
| meteor_contest             | 78.1 ms     | 74.5 ms: 1.05x faster  |
| async_generators           | 224 ms      | 213 ms: 1.05x faster   |
| connected_components       | 326 ms      | 311 ms: 1.05x faster   |
| unpickle_pure_python       | 154 us      | 148 us: 1.04x faster   |
| xml_etree_process          | 46.5 ms     | 44.7 ms: 1.04x faster  |
| async_tree_memoization_tg  | 218 ms      | 210 ms: 1.04x faster   |
| python_startup_no_site     | 20.1 ms     | 19.4 ms: 1.04x faster  |
| sympy_integrate            | 13.9 ms     | 13.4 ms: 1.03x faster  |
| bench_thread_pool          | 906 us      | 876 us: 1.03x faster   |
| create_gc_cycles           | 1.38 ms     | 1.34 ms: 1.03x faster  |
| xml_etree_generate         | 66.8 ms     | 64.7 ms: 1.03x faster  |
| sphinx                     | 723 ms      | 702 ms: 1.03x faster   |
| shortest_path              | 357 ms      | 347 ms: 1.03x faster   |
| logging_silent             | 62.9 ns     | 61.1 ns: 1.03x faster  |
| 2to3                       | 237 ms      | 231 ms: 1.03x faster   |
| k_core                     | 1.76 sec    | 1.71 sec: 1.03x faster |
| crypto_pyaes               | 49.3 ms     | 48.0 ms: 1.03x faster  |
| docutils                   | 1.81 sec    | 1.77 sec: 1.03x faster |
| json_dumps                 | 7.94 ms     | 7.79 ms: 1.02x faster  |
| coverage                   | 56.4 ms     | 55.4 ms: 1.02x faster  |
| pathlib                    | 25.6 ms     | 25.1 ms: 1.02x faster  |
| thrift                     | 561 us      | 551 us: 1.02x faster   |
| python_startup             | 26.9 ms     | 26.4 ms: 1.02x faster  |
| scimark_lu                 | 65.2 ms     | 64.2 ms: 1.02x faster  |
| xml_etree_iterparse        | 71.5 ms     | 70.4 ms: 1.02x faster  |
| dulwich_log                | 43.0 ms     | 42.3 ms: 1.02x faster  |
| bench_mp_pool              | 95.0 ms     | 93.6 ms: 1.01x faster  |
| telco                      | 5.33 ms     | 5.26 ms: 1.01x faster  |
| async_tree_cpu_io_mixed_tg | 367 ms      | 363 ms: 1.01x faster   |
| async_tree_cpu_io_mixed    | 362 ms      | 359 ms: 1.01x faster   |
| pidigits                   | 147 ms      | 146 ms: 1.01x faster   |
| xml_etree_parse            | 104 ms      | 105 ms: 1.01x slower   |
| gc_traversal               | 2.77 ms     | 2.83 ms: 1.02x slower  |
| asyncio_websockets         | 304 ms      | 312 ms: 1.03x slower   |
| regex_dna                  | 117 ms      | 121 ms: 1.03x slower   |
| json_loads                 | 21.1 us     | 21.9 us: 1.04x slower  |
| regex_effbot               | 1.76 ms     | 1.85 ms: 1.05x slower  |
| mako                       | 7.44 ms     | 7.84 ms: 1.05x slower  |
| Geometric mean             | (ref)       | 1.05x faster           |

Benchmark hidden because not significant (4): regex_v8, sqlite_synth, scimark_sparse_mat_mult, json

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown