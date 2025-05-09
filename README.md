# Comparisons

- `default`: A default CPython built with the upstream compiler
- `PGO`: A default CPython with `--pgo`,  built with the upstream compiler
- `Ex`: A default CPython built with the experimental compiler
- `TC-Ex`: A tail-calling CPython, built with the experimental compiler
- `TC-PGO-Ex2`: A tail-calling CPython, with PGO, built with the (second version) experimental compiler
- `TCO-Ex2`: A tail-calling CPython, only using `musttail`, built with the (second version) experimental compiler
- `TCO-PGO-Ex2`: A tail-calling CPython, only using `musttail`, built with the (second version) experimental compiler

|  | default | PGO | Ex | TC-Ex | TC-PGO-Ex2 | TCO-Ex2 | TCO-PGO-Ex2 |
| -- | -- | -- | -- | -- | -- | -- | -- |
| default |  | 1.376x ↑[📄](PGO-vs-default.md)[📈](PGO-vs-default.svg) | 1.039x ↓[📄](Ex-vs-default.md)[📈](Ex-vs-default.svg) | 1.386x ↑[📄](TC-Ex-vs-default.md)[📈](TC-Ex-vs-default.svg) | 1.512x ↑[📄](TC-PGO-Ex2-vs-default.md)[📈](TC-PGO-Ex2-vs-default.svg) | 1.318x ↑[📄](TCO-Ex2-vs-default.md)[📈](TCO-Ex2-vs-default.svg) | 1.318x ↑[📄](TCO-PGO-Ex2-vs-default.md)[📈](TCO-PGO-Ex2-vs-default.svg) |
| PGO | 1.273x ↓[📄](default-vs-PGO.md)[📈](default-vs-PGO.svg) |  | 1.301x ↓[📄](Ex-vs-PGO.md)[📈](Ex-vs-PGO.svg) | 1.008x ↑[📄](TC-Ex-vs-PGO.md)[📈](TC-Ex-vs-PGO.svg) | 1.098x ↑[📄](TC-PGO-Ex2-vs-PGO.md)[📈](TC-PGO-Ex2-vs-PGO.svg) | 1.041x ↓[📄](TCO-Ex2-vs-PGO.md)[📈](TCO-Ex2-vs-PGO.svg) | 1.041x ↓[📄](TCO-PGO-Ex2-vs-PGO.md)[📈](TCO-PGO-Ex2-vs-PGO.svg) |
| Ex | 1.041x ↑[📄](default-vs-Ex.md)[📈](default-vs-Ex.svg) | 1.432x ↑[📄](PGO-vs-Ex.md)[📈](PGO-vs-Ex.svg) |  | 1.442x ↑[📄](TC-Ex-vs-Ex.md)[📈](TC-Ex-vs-Ex.svg) | 1.573x ↑[📄](TC-PGO-Ex2-vs-Ex.md)[📈](TC-PGO-Ex2-vs-Ex.svg) | 1.371x ↑[📄](TCO-Ex2-vs-Ex.md)[📈](TCO-Ex2-vs-Ex.svg) | 1.371x ↑[📄](TCO-PGO-Ex2-vs-Ex.md)[📈](TCO-PGO-Ex2-vs-Ex.svg) |
| TC-Ex | 1.278x ↓[📄](default-vs-TC-Ex.md)[📈](default-vs-TC-Ex.svg) | 1.008x ↓[📄](PGO-vs-TC-Ex.md)[📈](PGO-vs-TC-Ex.svg) | 1.306x ↓[📄](Ex-vs-TC-Ex.md)[📈](Ex-vs-TC-Ex.svg) |  | 1.090x ↑[📄](TC-PGO-Ex2-vs-TC-Ex.md)[📈](TC-PGO-Ex2-vs-TC-Ex.svg) | 1.049x ↓[📄](TCO-Ex2-vs-TC-Ex.md)[📈](TCO-Ex2-vs-TC-Ex.svg) | 1.049x ↓[📄](TCO-PGO-Ex2-vs-TC-Ex.md)[📈](TCO-PGO-Ex2-vs-TC-Ex.svg) |
| TC-PGO-Ex2 | 1.338x ↓[📄](default-vs-TC-PGO-Ex2.md)[📈](default-vs-TC-PGO-Ex2.svg) | 1.089x ↓[📄](PGO-vs-TC-PGO-Ex2.md)[📈](PGO-vs-TC-PGO-Ex2.svg) | 1.364x ↓[📄](Ex-vs-TC-PGO-Ex2.md)[📈](Ex-vs-TC-PGO-Ex2.svg) | 1.082x ↓[📄](TC-Ex-vs-TC-PGO-Ex2.md)[📈](TC-Ex-vs-TC-PGO-Ex2.svg) |  | 1.128x ↓[📄](TCO-Ex2-vs-TC-PGO-Ex2.md)[📈](TCO-Ex2-vs-TC-PGO-Ex2.svg) | 1.128x ↓[📄](TCO-PGO-Ex2-vs-TC-PGO-Ex2.md)[📈](TCO-PGO-Ex2-vs-TC-PGO-Ex2.svg) |
| TCO-Ex2 | 1.241x ↓[📄](default-vs-TCO-Ex2.md)[📈](default-vs-TCO-Ex2.svg) | 1.044x ↑[📄](PGO-vs-TCO-Ex2.md)[📈](PGO-vs-TCO-Ex2.svg) | 1.270x ↓[📄](Ex-vs-TCO-Ex2.md)[📈](Ex-vs-TCO-Ex2.svg) | 1.052x ↑[📄](TC-Ex-vs-TCO-Ex2.md)[📈](TC-Ex-vs-TCO-Ex2.svg) | 1.147x ↑[📄](TC-PGO-Ex2-vs-TCO-Ex2.md)[📈](TC-PGO-Ex2-vs-TCO-Ex2.svg) |  | not sig[📄](TCO-PGO-Ex2-vs-TCO-Ex2.md)[📈](TCO-PGO-Ex2-vs-TCO-Ex2.svg) |
| TCO-PGO-Ex2 | 1.241x ↓[📄](default-vs-TCO-PGO-Ex2.md)[📈](default-vs-TCO-PGO-Ex2.svg) | 1.044x ↑[📄](PGO-vs-TCO-PGO-Ex2.md)[📈](PGO-vs-TCO-PGO-Ex2.svg) | 1.270x ↓[📄](Ex-vs-TCO-PGO-Ex2.md)[📈](Ex-vs-TCO-PGO-Ex2.svg) | 1.052x ↑[📄](TC-Ex-vs-TCO-PGO-Ex2.md)[📈](TC-Ex-vs-TCO-PGO-Ex2.svg) | 1.147x ↑[📄](TC-PGO-Ex2-vs-TCO-PGO-Ex2.md)[📈](TC-PGO-Ex2-vs-TCO-PGO-Ex2.svg) | not sig[📄](TCO-Ex2-vs-TCO-PGO-Ex2.md)[📈](TCO-Ex2-vs-TCO-PGO-Ex2.svg) |  |


Rows are 'bases', columns are 'heads'

