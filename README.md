# Comparisons

Naming convention of the different configurations:

- TC: Tail calling interpreter
- PGO: Profile-guided-optimization.  "MostPGO" means using PGO for everything in the runtime except for the tail-calling interpreter.
- Ex: Experimental pre-release of MSVC that supports TC (musttail and preserve_none).  NoEx is the upstream released MSVC version 19.43.34808

"PGO" represents the configuration currently used to make Python releases.

"TC-MostPGO-Ex" represents the closest thing to the aspirational build with tail calling. The experimental compiler doesn't currently support PGO instrumentation on tailcalls, so we collect PGO data on the "classic" interpreter and apply it to a build with the tail-calling interpreter.  This means that the tail calling interpreter gets "default" optimizations with no additional guidance from PGO.

## Observations

There does seem to be a small regression of 4% on non-tail-calling builds (a) when using the experimental compiler.  Perhaps this is similar to what we saw in clang-19.

Without PGO getting involved, and all other variables being equal, the effect of moving to the tail-calling interpreter is 44% (b).

Unfortunately, the effect of PGO in the normal case is 37% (c), which counts considerably against the overall wins of the tail-calling interpreter without PGO, netting only 1% (d).

While we are waiting for PGO instrumentation to be supported on functions with the `musttail` annotation, we can approximate the effect of PGO on the tail calling interpreter by collecting PGO data on everything *but* the functions that make up the tail calling interpreter.  When doing that, we see a substantial improvement of 8.1% (e).  This is the geometric mean of all benchmarks -- it's worth noting that on interpreter-heavy benchmarks the improvement is 10%-44% which is extremely impressive.  This represents a "worst case" improvement that should be possible when full PGO+tail calling is implemented.

This suggests to me that the work on `preserve_none` and `musttail` in MSVC has been very valuable to CPython and the additional work to make it compatible with PGO will not be in vain.  8% improvements are very hard to come by.

|  | default | PGO | Ex | TC-Ex | TC-MostPGO-Ex |
| -- | -- | -- | -- | -- | -- |
| default |  | 1.376x ↑[📄](PGO-vs-default.md)[📈](PGO-vs-default.svg) (c) | 1.039x ↓[📄](Ex-vs-default.md)[📈](Ex-vs-default.svg) (a) | 1.386x ↑[📄](TC-Ex-vs-default.md)[📈](TC-Ex-vs-default.svg) | 1.487x ↑[📄](TC-MostPGO-Ex-vs-default.md)[📈](TC-MostPGO-Ex-vs-default.svg) |
| PGO | 1.273x ↓[📄](default-vs-PGO.md)[📈](default-vs-PGO.svg) |  | 1.301x ↓[📄](Ex-vs-PGO.md)[📈](Ex-vs-PGO.svg) | 1.008x ↑[📄](TC-Ex-vs-PGO.md)[📈](TC-Ex-vs-PGO.svg) (d) | 1.081x ↑[📄](TC-MostPGO-Ex-vs-PGO.md)[📈](TC-MostPGO-Ex-vs-PGO.svg) (e) |
| Ex | 1.041x ↑[📄](default-vs-Ex.md)[📈](default-vs-Ex.svg) | 1.432x ↑[📄](PGO-vs-Ex.md)[📈](PGO-vs-Ex.svg) |  | 1.442x ↑[📄](TC-Ex-vs-Ex.md)[📈](TC-Ex-vs-Ex.svg) (b) | 1.547x ↑[📄](TC-MostPGO-Ex-vs-Ex.md)[📈](TC-MostPGO-Ex-vs-Ex.svg) |
| TC-Ex | 1.278x ↓[📄](default-vs-TC-Ex.md)[📈](default-vs-TC-Ex.svg) | 1.008x ↓[📄](PGO-vs-TC-Ex.md)[📈](PGO-vs-TC-Ex.svg) | 1.306x ↓[📄](Ex-vs-TC-Ex.md)[📈](Ex-vs-TC-Ex.svg) |  | 1.073x ↑[📄](TC-MostPGO-Ex-vs-TC-Ex.md)[📈](TC-MostPGO-Ex-vs-TC-Ex.svg) |
| TC-MostPGO-Ex | 1.327x ↓[📄](default-vs-TC-MostPGO-Ex.md)[📈](default-vs-TC-MostPGO-Ex.svg) | 1.075x ↓[📄](PGO-vs-TC-MostPGO-Ex.md)[📈](PGO-vs-TC-MostPGO-Ex.svg) | 1.353x ↓[📄](Ex-vs-TC-MostPGO-Ex.md)[📈](Ex-vs-TC-MostPGO-Ex.svg) | 1.067x ↓[📄](TC-Ex-vs-TC-MostPGO-Ex.md)[📈](TC-Ex-vs-TC-MostPGO-Ex.svg) |  |


Rows are 'bases', columns are 'heads'

