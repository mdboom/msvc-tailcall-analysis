# Comparisons

|  | default | PGO | Ex | TC-Ex | TC-MostPGO-Ex | clang-main |
| -- | -- | -- | -- | -- | -- | -- |
| default |  | 1.376x ↑[📄](PGO-vs-default.md)[📈](PGO-vs-default.svg) | 1.039x ↓[📄](Ex-vs-default.md)[📈](Ex-vs-default.svg) | 1.386x ↑[📄](TC-Ex-vs-default.md)[📈](TC-Ex-vs-default.svg) | 1.487x ↑[📄](TC-MostPGO-Ex-vs-default.md)[📈](TC-MostPGO-Ex-vs-default.svg) | 1.443x ↑[📄](clang-main-vs-default.md)[📈](clang-main-vs-default.svg) |
| PGO | 1.273x ↓[📄](default-vs-PGO.md)[📈](default-vs-PGO.svg) |  | 1.301x ↓[📄](Ex-vs-PGO.md)[📈](Ex-vs-PGO.svg) | 1.008x ↑[📄](TC-Ex-vs-PGO.md)[📈](TC-Ex-vs-PGO.svg) | 1.081x ↑[📄](TC-MostPGO-Ex-vs-PGO.md)[📈](TC-MostPGO-Ex-vs-PGO.svg) | 1.048x ↑[📄](clang-main-vs-PGO.md)[📈](clang-main-vs-PGO.svg) |
| Ex | 1.041x ↑[📄](default-vs-Ex.md)[📈](default-vs-Ex.svg) | 1.432x ↑[📄](PGO-vs-Ex.md)[📈](PGO-vs-Ex.svg) |  | 1.442x ↑[📄](TC-Ex-vs-Ex.md)[📈](TC-Ex-vs-Ex.svg) | 1.547x ↑[📄](TC-MostPGO-Ex-vs-Ex.md)[📈](TC-MostPGO-Ex-vs-Ex.svg) | 1.502x ↑[📄](clang-main-vs-Ex.md)[📈](clang-main-vs-Ex.svg) |
| TC-Ex | 1.278x ↓[📄](default-vs-TC-Ex.md)[📈](default-vs-TC-Ex.svg) | 1.008x ↓[📄](PGO-vs-TC-Ex.md)[📈](PGO-vs-TC-Ex.svg) | 1.306x ↓[📄](Ex-vs-TC-Ex.md)[📈](Ex-vs-TC-Ex.svg) |  | 1.073x ↑[📄](TC-MostPGO-Ex-vs-TC-Ex.md)[📈](TC-MostPGO-Ex-vs-TC-Ex.svg) | 1.040x ↑[📄](clang-main-vs-TC-Ex.md)[📈](clang-main-vs-TC-Ex.svg) |
| TC-MostPGO-Ex | 1.327x ↓[📄](default-vs-TC-MostPGO-Ex.md)[📈](default-vs-TC-MostPGO-Ex.svg) | 1.075x ↓[📄](PGO-vs-TC-MostPGO-Ex.md)[📈](PGO-vs-TC-MostPGO-Ex.svg) | 1.353x ↓[📄](Ex-vs-TC-MostPGO-Ex.md)[📈](Ex-vs-TC-MostPGO-Ex.svg) | 1.067x ↓[📄](TC-Ex-vs-TC-MostPGO-Ex.md)[📈](TC-Ex-vs-TC-MostPGO-Ex.svg) |  | 1.030x ↓[📄](clang-main-vs-TC-MostPGO-Ex.md)[📈](clang-main-vs-TC-MostPGO-Ex.svg) |
| clang-main | 1.307x ↓[📄](default-vs-clang-main.md)[📈](default-vs-clang-main.svg) | 1.046x ↓[📄](PGO-vs-clang-main.md)[📈](PGO-vs-clang-main.svg) | 1.334x ↓[📄](Ex-vs-clang-main.md)[📈](Ex-vs-clang-main.svg) | 1.038x ↓[📄](TC-Ex-vs-clang-main.md)[📈](TC-Ex-vs-clang-main.svg) | 1.031x ↑[📄](TC-MostPGO-Ex-vs-clang-main.md)[📈](TC-MostPGO-Ex-vs-clang-main.svg) |  |


Rows are 'bases', columns are 'heads'

