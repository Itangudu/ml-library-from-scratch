
## Goal
Fit a linear model to data in pure NumPy, solving it two different ways
(normal equation and gradient descent), and prove the results are correct.

## Done when
- Given a feature matrix X (n samples x d features) and targets y, the
  library can fit a linear model two ways: with the normal equation and
  with gradient descent.
- On a well-behaved dataset, both methods produce the same weights
  (within a tolerance I choose and justify in my notes).
- The fitted model can predict on new data.
- An intercept (bias) term is supported.
- The gradient of the loss with respect to the weights, as implemented,
  passes my Module 01 gradient checker.
- On a test dataset, my weights match a reference implementation
  (scikit-learn's LinearRegression). The reference is only used to
  compare, never inside my code.
- Gradient descent demonstrably converges: the loss decreases over
  iterations, and I can show a plot or printout of it.
- notes/02_linear_regression.md contains, in my own words:
  - the loss function I'm minimizing, and why
  - a derivation of its gradient with respect to the weight vector
  - a derivation of the normal equation
  - what happens when X^T X is not invertible, and why
  - what goes wrong with a learning rate that is too large or too small
- Work is committed and PROGRESS.md is updated.