# Comparisons

Naming convention of the different configurations:

- TC: Tail calling interpreter
- PGO: Profile-guided-optimization
- Ex: Experimental pre-release of MSVC that supports TC (musttail and preserve_none).  NoEx is the upstream released MSVC version 19.43.34808

"NoTC-PGO-NoEx" represents the configuration currently used to make Python releases.

"TC-NoPGO-Ex" represents the aspirational build with tail calling, but the experimental compiler doesn't currently support PGO so is currently sub-optimal.

There does seem to be a small regression of 4% on NoTC builds (a) when using the experimental compiler.  Perhaps this is similar to what we saw in clang-19.

All other things being equal, the effect of moving to the tail-calling interpreter is 44% (b).

Unfortunately, the effect of PGO on a NoTC build is 37% (c), which counts considerably against the overall wins of the tail-calling interpreter, netting only 1% (d).

It still seems plausible that if we can get PGO+TC working, we will see a considerable, possibly double-digit, improvement.

|  | NoTC-PGO-NoEx | NoTC-NoPGO-NoEx | NoTC-NoPGO-Ex | TC-NoPGO-Ex |
| -- | -- | -- | -- | -- |
| NoTC-PGO-NoEx |  | 1.273x ↓[📄](NoTC-NoPGO-NoEx-vs-NoTC-PGO-NoEx.md)[📈](NoTC-NoPGO-NoEx-vs-NoTC-PGO-NoEx.svg) | 1.301x ↓[📄](NoTC-NoPGO-Ex-vs-NoTC-PGO-NoEx.md)[📈](NoTC-NoPGO-Ex-vs-NoTC-PGO-NoEx.svg) | 1.008x ↑[📄](TC-NoPGO-Ex-vs-NoTC-PGO-NoEx.md)[📈](TC-NoPGO-Ex-vs-NoTC-PGO-NoEx.svg) (d) |
| NoTC-NoPGO-NoEx | 1.376x ↑[📄](NoTC-PGO-NoEx-vs-NoTC-NoPGO-NoEx.md)[📈](NoTC-PGO-NoEx-vs-NoTC-NoPGO-NoEx.svg) (c) |  | 1.039x ↓[📄](NoTC-NoPGO-Ex-vs-NoTC-NoPGO-NoEx.md)[📈](NoTC-NoPGO-Ex-vs-NoTC-NoPGO-NoEx.svg) (a) | 1.386x ↑[📄](TC-NoPGO-Ex-vs-NoTC-NoPGO-NoEx.md)[📈](TC-NoPGO-Ex-vs-NoTC-NoPGO-NoEx.svg) |
| NoTC-NoPGO-Ex | 1.432x ↑[📄](NoTC-PGO-NoEx-vs-NoTC-NoPGO-Ex.md)[📈](NoTC-PGO-NoEx-vs-NoTC-NoPGO-Ex.svg) | 1.041x ↑[📄](NoTC-NoPGO-NoEx-vs-NoTC-NoPGO-Ex.md)[📈](NoTC-NoPGO-NoEx-vs-NoTC-NoPGO-Ex.svg) |  | 1.442x ↑[📄](TC-NoPGO-Ex-vs-NoTC-NoPGO-Ex.md)[📈](TC-NoPGO-Ex-vs-NoTC-NoPGO-Ex.svg) (b) |
| TC-NoPGO-Ex | 1.008x ↓[📄](NoTC-PGO-NoEx-vs-TC-NoPGO-Ex.md)[📈](NoTC-PGO-NoEx-vs-TC-NoPGO-Ex.svg) | 1.278x ↓[📄](NoTC-NoPGO-NoEx-vs-TC-NoPGO-Ex.md)[📈](NoTC-NoPGO-NoEx-vs-TC-NoPGO-Ex.svg) | 1.306x ↓[📄](NoTC-NoPGO-Ex-vs-TC-NoPGO-Ex.md)[📈](NoTC-NoPGO-Ex-vs-TC-NoPGO-Ex.svg) |  |


Rows are 'bases', columns are 'heads'

