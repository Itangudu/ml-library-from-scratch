import numpy as np

def linear_regression(X, y):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    X = np.column_stack((X, np.ones(X.shape[0])))
    X_tran = np.transpose(X)
    w = np.linalg.solve(X_tran@X, X_tran@y)
    return w

X = [[1, 2, 0],
     [2, 1, 4],
     [0, 3, 2],
     [3, 0, 1],
     [1, 1, 1]]
y = [3, 10, -1, 13.5, 5.5]
print(linear_regression(X, y))


rng = np.random.default_rng(0)
X = rng.normal(size=(100, 3))
y = X @ np.array([3, -2, 0.5]) + 4 + rng.normal(scale=0.1, size=100)
print(linear_regression(X, y))
    