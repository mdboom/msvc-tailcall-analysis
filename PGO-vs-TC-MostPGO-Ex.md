# Results vs. base

- fork: unknown
- ref: PGO
- machine: unknown-unknown
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.075x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | TC-MostPGO-Ex | PGO                    |
|----------------|:-------------:|:----------------------:|
| 2to3           | 209 ms        | 227 ms: 1.09x slower   |
| docutils       | 1.74 sec      | 1.68 sec: 1.04x faster |
| html5lib       | 37.2 ms       | 40.8 ms: 1.10x slower  |
| Geometric mean | (ref)         | 1.03x slower           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | TC-MostPGO-Ex | PGO                   |
|----------------------------|:-------------:|:---------------------:|
| asyncio_websockets         | 315 ms        | 318 ms: 1.01x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 339 ms: 1.02x slower  |
| async_tree_memoization_tg  | 209 ms        | 216 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 343 ms: 1.04x slower  |
| async_tree_io_tg           | 374 ms        | 410 ms: 1.10x slower  |
| async_tree_none_tg         | 160 ms        | 176 ms: 1.10x slower  |
| async_tree_memoization     | 202 ms        | 224 ms: 1.11x slower  |
| async_generators           | 202 ms        | 226 ms: 1.12x slower  |
| async_tree_io              | 374 ms        | 423 ms: 1.13x slower  |
| async_tree_none            | 165 ms        | 187 ms: 1.13x slower  |
| coroutines                 | 11.8 ms       | 13.5 ms: 1.14x slower |
| Geometric mean             | (ref)         | 1.08x slower          |

Benchmarks with tag 'math':
===========================

| Benchmark      | TC-MostPGO-Ex | PGO                   |
|----------------|:-------------:|:---------------------:|
| pidigits       | 151 ms        | 152 ms: 1.01x slower  |
| float          | 40.4 ms       | 47.8 ms: 1.18x slower |
| nbody          | 53.0 ms       | 74.1 ms: 1.40x slower |
| Geometric mean | (ref)         | 1.19x slower          |

Benchmarks with tag 'regex':
============================

| Benchmark      | TC-MostPGO-Ex | PGO                   |
|----------------|:-------------:|:---------------------:|
| regex_v8       | 15.3 ms       | 13.5 ms: 1.13x faster |
| regex_dna      | 125 ms        | 112 ms: 1.11x faster  |
| regex_effbot   | 1.53 ms       | 1.42 ms: 1.07x faster |
| regex_compile  | 79.3 ms       | 88.2 ms: 1.11x slower |
| Geometric mean | (ref)         | 1.05x faster          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | TC-MostPGO-Ex | PGO                    |
|----------------------|:-------------:|:----------------------:|
| json_loads           | 15.8 us       | 14.7 us: 1.08x faster  |
| xml_etree_parse      | 92.6 ms       | 91.2 ms: 1.02x faster  |
| json_dumps           | 6.84 ms       | 7.05 ms: 1.03x slower  |
| xml_etree_generate   | 54.3 ms       | 58.7 ms: 1.08x slower  |
| xml_etree_process    | 37.9 ms       | 41.5 ms: 1.10x slower  |
| pickle_pure_python   | 195 us        | 237 us: 1.21x slower   |
| tomli_loads          | 1.18 sec      | 1.47 sec: 1.24x slower |
| unpickle_pure_python | 123 us        | 155 us: 1.26x slower   |
| Geometric mean       | (ref)         | 1.09x slower           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | TC-MostPGO-Ex | PGO                   |
|----------------|:-------------:|:---------------------:|
| python_startup | 26.4 ms       | 26.1 ms: 1.01x faster |
| Geometric mean | (ref)         | 1.01x faster          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | TC-MostPGO-Ex | PGO                   |
|-----------------|:-------------:|:---------------------:|
| mako            | 6.50 ms       | 6.86 ms: 1.05x slower |
| django_template | 22.9 ms       | 25.1 ms: 1.09x slower |
| genshi_xml      | 31.3 ms       | 36.3 ms: 1.16x slower |
| genshi_text     | 14.1 ms       | 16.5 ms: 1.17x slower |
| Geometric mean  | (ref)         | 1.12x slower          |

All benchmarks:
===============

| Benchmark                  | TC-MostPGO-Ex | PGO                    |
|----------------------------|:-------------:|:----------------------:|
| subparsers                 | 41.2 ms       | 16.1 ms: 2.56x faster  |
| many_optionals             | 669 us        | 438 us: 1.53x faster   |
| k_core                     | 2.00 sec      | 1.73 sec: 1.15x faster |
| regex_v8                   | 15.3 ms       | 13.5 ms: 1.13x faster  |
| connected_components       | 366 ms        | 329 ms: 1.11x faster   |
| regex_dna                  | 125 ms        | 112 ms: 1.11x faster   |
| shortest_path              | 399 ms        | 359 ms: 1.11x faster   |
| create_gc_cycles           | 1.35 ms       | 1.25 ms: 1.08x faster  |
| json_loads                 | 15.8 us       | 14.7 us: 1.08x faster  |
| gc_traversal               | 2.21 ms       | 2.06 ms: 1.07x faster  |
| regex_effbot               | 1.53 ms       | 1.42 ms: 1.07x faster  |
| docutils                   | 1.74 sec      | 1.68 sec: 1.04x faster |
| xml_etree_parse            | 92.6 ms       | 91.2 ms: 1.02x faster  |
| python_startup             | 26.4 ms       | 26.1 ms: 1.01x faster  |
| pidigits                   | 151 ms        | 152 ms: 1.01x slower   |
| asyncio_websockets         | 315 ms        | 318 ms: 1.01x slower   |
| coverage                   | 46.2 ms       | 46.8 ms: 1.01x slower  |
| sqlite_synth               | 1.56 us       | 1.59 us: 1.02x slower  |
| async_tree_cpu_io_mixed    | 332 ms        | 339 ms: 1.02x slower   |
| sympy_sum                  | 88.0 ms       | 90.5 ms: 1.03x slower  |
| async_tree_memoization_tg  | 209 ms        | 216 ms: 1.03x slower   |
| json_dumps                 | 6.84 ms       | 7.05 ms: 1.03x slower  |
| async_tree_cpu_io_mixed_tg | 331 ms        | 343 ms: 1.04x slower   |
| thrift                     | 487 us        | 507 us: 1.04x slower   |
| dulwich_log                | 41.5 ms       | 43.4 ms: 1.05x slower  |
| sympy_integrate            | 12.9 ms       | 13.5 ms: 1.05x slower  |
| mdp                        | 1.56 sec      | 1.64 sec: 1.05x slower |
| bench_thread_pool          | 819 us        | 864 us: 1.05x slower   |
| mako                       | 6.50 ms       | 6.86 ms: 1.05x slower  |
| sqlglot_v2_optimize        | 33.0 ms       | 35.0 ms: 1.06x slower  |
| meteor_contest             | 72.3 ms       | 76.9 ms: 1.06x slower  |
| telco                      | 4.60 ms       | 4.89 ms: 1.06x slower  |
| pycparser                  | 688 ms        | 738 ms: 1.07x slower   |
| xml_etree_generate         | 54.3 ms       | 58.7 ms: 1.08x slower  |
| typing_runtime_protocols   | 98.1 us       | 106 us: 1.08x slower   |
| sympy_str                  | 163 ms        | 176 ms: 1.08x slower   |
| sympy_expand               | 279 ms        | 302 ms: 1.08x slower   |
| 2to3                       | 209 ms        | 227 ms: 1.09x slower   |
| richards                   | 28.1 ms       | 30.7 ms: 1.09x slower  |
| django_template            | 22.9 ms       | 25.1 ms: 1.09x slower  |
| html5lib                   | 37.2 ms       | 40.8 ms: 1.10x slower  |
| richards_super             | 32.0 ms       | 35.1 ms: 1.10x slower  |
| async_tree_io_tg           | 374 ms        | 410 ms: 1.10x slower   |
| xml_etree_process          | 37.9 ms       | 41.5 ms: 1.10x slower  |
| logging_format             | 6.39 us       | 7.03 us: 1.10x slower  |
| async_tree_none_tg         | 160 ms        | 176 ms: 1.10x slower   |
| sqlglot_v2_normalize       | 66.7 ms       | 73.6 ms: 1.10x slower  |
| bpe_tokeniser              | 2.67 sec      | 2.96 sec: 1.11x slower |
| regex_compile              | 79.3 ms       | 88.2 ms: 1.11x slower  |
| async_tree_memoization     | 202 ms        | 224 ms: 1.11x slower   |
| logging_simple             | 5.84 us       | 6.53 us: 1.12x slower  |
| async_generators           | 202 ms        | 226 ms: 1.12x slower   |
| async_tree_io              | 374 ms        | 423 ms: 1.13x slower   |
| async_tree_none            | 165 ms        | 187 ms: 1.13x slower   |
| coroutines                 | 11.8 ms       | 13.5 ms: 1.14x slower  |
| deepcopy_reduce            | 1.69 us       | 1.94 us: 1.15x slower  |
| genshi_xml                 | 31.3 ms       | 36.3 ms: 1.16x slower  |
| pprint_safe_repr           | 481 ms        | 558 ms: 1.16x slower   |
| sqlglot_v2_transpile       | 943 us        | 1.10 ms: 1.17x slower  |
| pprint_pformat             | 963 ms        | 1.13 sec: 1.17x slower |
| genshi_text                | 14.1 ms       | 16.5 ms: 1.17x slower  |
| nqueens                    | 54.2 ms       | 63.6 ms: 1.17x slower  |
| raytrace                   | 162 ms        | 191 ms: 1.18x slower   |
| comprehensions             | 9.60 us       | 11.3 us: 1.18x slower  |
| generators                 | 16.3 ms       | 19.3 ms: 1.18x slower  |
| float                      | 40.4 ms       | 47.8 ms: 1.18x slower  |
| pyflate                    | 264 ms        | 315 ms: 1.19x slower   |
| deepcopy                   | 159 us        | 190 us: 1.19x slower   |
| crypto_pyaes               | 41.7 ms       | 50.0 ms: 1.20x slower  |
| sqlglot_v2_parse           | 742 us        | 892 us: 1.20x slower   |
| scimark_lu                 | 55.5 ms       | 66.9 ms: 1.20x slower  |
| scimark_sparse_mat_mult    | 2.25 ms       | 2.72 ms: 1.21x slower  |
| pickle_pure_python         | 195 us        | 237 us: 1.21x slower   |
| hexiom                     | 3.58 ms       | 4.38 ms: 1.22x slower  |
| deltablue                  | 1.87 ms       | 2.29 ms: 1.22x slower  |
| logging_silent             | 53.0 ns       | 65.2 ns: 1.23x slower  |
| deepcopy_memo              | 17.0 us       | 21.0 us: 1.24x slower  |
| tomli_loads                | 1.18 sec      | 1.47 sec: 1.24x slower |
| pathlib                    | 25.5 ms       | 32.1 ms: 1.26x slower  |
| unpickle_pure_python       | 123 us        | 155 us: 1.26x slower   |
| fannkuch                   | 233 ms        | 296 ms: 1.27x slower   |
| scimark_fft                | 151 ms        | 192 ms: 1.27x slower   |
| chaos                      | 34.2 ms       | 43.6 ms: 1.28x slower  |
| go                         | 68.6 ms       | 88.6 ms: 1.29x slower  |
| spectral_norm              | 46.7 ms       | 61.5 ms: 1.32x slower  |
| scimark_monte_carlo        | 35.5 ms       | 47.1 ms: 1.33x slower  |
| nbody                      | 53.0 ms       | 74.1 ms: 1.40x slower  |
| scimark_sor                | 63.1 ms       | 91.0 ms: 1.44x slower  |
| Geometric mean             | (ref)         | 1.08x slower           |

Benchmark hidden because not significant (6): sphinx, xml_etree_iterparse, json, pylint, python_startup_no_site, bench_mp_pool

- Geometric mean (including insignificant results): 1.075x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown