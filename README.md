# ML Library From Scratch

Machine learning algorithms implemented from scratch in pure NumPy.
No scikit-learn or PyTorch doing the work: they are used only to check
my results.

## Approach

Every module follows the same three steps:

1. **Derive** the math by hand, written up in my own words in `notes/`.
2. **Implement** it in NumPy.
3. **Verify** it: gradients are checked numerically with my own gradient
   checker (Module 01), and results are compared against reference
   implementations on the same data.

Each module starts with a spec in `specs/` that defines what must be true
for it to count as done.

## Modules

### Phase 1: Library
| # | Module | Status |
|---|--------|--------|
| 01 | Gradient checker | Done (write-up in progress) |
| 02 | Linear regression (normal equation + gradient descent) | In progress |
| 03 | Ridge and Lasso regression | Planned |
| 04 | Logistic regression | Planned |
| 05 | Softmax regression | Planned |
| 06 | Optimizers: SGD, momentum, RMSProp, Adam | Planned |
| 07 | Neural network with hand-written backprop | Planned |
| 08 | Decision trees | Planned |
| 09 | Random forests | Planned |
| 10 | k-Nearest Neighbors | Planned |
| 11 | Support Vector Machines | Planned |
| 12 | k-means | Planned |
| 13 | PCA | Planned |
| 14 | Gaussian mixtures with EM | Planned |

### Phase 2: Mini deep-learning framework
| # | Module | Status |
|---|--------|--------|
| 15 | Autograd engine | Planned |
| 16 | CNN with hand-written backprop | Planned |
| 17 | LSTM with backprop through time | Planned |

## Repository layout
src/        implementations
specs/      what each module must do to be considered done
notes/      derivations and explanations
PROGRESS.md current status and next steps

## Requirements

Python 3 and NumPy. scikit-learn is used only in tests, for comparison.
