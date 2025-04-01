# Comparisons

|  | default | PGO | Ex | TC-Ex | TC-MostPGO-Ex | clang |
| -- | -- | -- | -- | -- | -- | -- |
| default |  | 1.376x ↑[📄](PGO-vs-default.md)[📈](PGO-vs-default.svg) | 1.039x ↓[📄](Ex-vs-default.md)[📈](Ex-vs-default.svg) | 1.386x ↑[📄](TC-Ex-vs-default.md)[📈](TC-Ex-vs-default.svg) | 1.487x ↑[📄](TC-MostPGO-Ex-vs-default.md)[📈](TC-MostPGO-Ex-vs-default.svg) | 1.670x ↑[📄](clang-vs-default.md)[📈](clang-vs-default.svg) |
| PGO | 1.273x ↓[📄](default-vs-PGO.md)[📈](default-vs-PGO.svg) |  | 1.301x ↓[📄](Ex-vs-PGO.md)[📈](Ex-vs-PGO.svg) | 1.008x ↑[📄](TC-Ex-vs-PGO.md)[📈](TC-Ex-vs-PGO.svg) | 1.081x ↑[📄](TC-MostPGO-Ex-vs-PGO.md)[📈](TC-MostPGO-Ex-vs-PGO.svg) | 1.214x ↑[📄](clang-vs-PGO.md)[📈](clang-vs-PGO.svg) |
| Ex | 1.041x ↑[📄](default-vs-Ex.md)[📈](default-vs-Ex.svg) | 1.432x ↑[📄](PGO-vs-Ex.md)[📈](PGO-vs-Ex.svg) |  | 1.442x ↑[📄](TC-Ex-vs-Ex.md)[📈](TC-Ex-vs-Ex.svg) | 1.547x ↑[📄](TC-MostPGO-Ex-vs-Ex.md)[📈](TC-MostPGO-Ex-vs-Ex.svg) | 1.738x ↑[📄](clang-vs-Ex.md)[📈](clang-vs-Ex.svg) |
| TC-Ex | 1.278x ↓[📄](default-vs-TC-Ex.md)[📈](default-vs-TC-Ex.svg) | 1.008x ↓[📄](PGO-vs-TC-Ex.md)[📈](PGO-vs-TC-Ex.svg) | 1.306x ↓[📄](Ex-vs-TC-Ex.md)[📈](Ex-vs-TC-Ex.svg) |  | 1.073x ↑[📄](TC-MostPGO-Ex-vs-TC-Ex.md)[📈](TC-MostPGO-Ex-vs-TC-Ex.svg) | 1.203x ↑[📄](clang-vs-TC-Ex.md)[📈](clang-vs-TC-Ex.svg) |
| TC-MostPGO-Ex | 1.327x ↓[📄](default-vs-TC-MostPGO-Ex.md)[📈](default-vs-TC-MostPGO-Ex.svg) | 1.075x ↓[📄](PGO-vs-TC-MostPGO-Ex.md)[📈](PGO-vs-TC-MostPGO-Ex.svg) | 1.353x ↓[📄](Ex-vs-TC-MostPGO-Ex.md)[📈](Ex-vs-TC-MostPGO-Ex.svg) | 1.067x ↓[📄](TC-Ex-vs-TC-MostPGO-Ex.md)[📈](TC-Ex-vs-TC-MostPGO-Ex.svg) |  | 1.123x ↑[📄](clang-vs-TC-MostPGO-Ex.md)[📈](clang-vs-TC-MostPGO-Ex.svg) |
| clang | 1.401x ↓[📄](default-vs-clang.md)[📈](default-vs-clang.svg) | 1.176x ↓[📄](PGO-vs-clang.md)[📈](PGO-vs-clang.svg) | 1.424x ↓[📄](Ex-vs-clang.md)[📈](Ex-vs-clang.svg) | 1.169x ↓[📄](TC-Ex-vs-clang.md)[📈](TC-Ex-vs-clang.svg) | 1.109x ↓[📄](TC-MostPGO-Ex-vs-clang.md)[📈](TC-MostPGO-Ex-vs-clang.svg) |  |


Rows are 'bases', columns are 'heads'

