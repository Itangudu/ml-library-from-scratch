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
    
def gradient_descent(X, y, lr, iterations, tolerance):
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)
    X = np.column_stack((X, np.ones(X.shape[0])))
    X_tran = np.transpose(X)
    w = np.zeros(X.shape[1], dtype=float)
    for i in range (iterations):
        gradient = (2/X.shape[0])*(X_tran@X@w-X_tran@y)
        if np.linalg.norm(gradient) > tolerance:
            w = w-lr*gradient
        else:
            break
    return w, i

def check(name, X, y, lr, iterations, tolerance=1e-6):
    result = gradient_descent(X, y, lr, iterations, tolerance)
    # works whether you return just w, or (w, iterations_used)
    if isinstance(result, tuple):
        w_gd, used = result
    else:
        w_gd, used = result, "?"
    w_ne = linear_regression(X, y)
    diff = np.max(np.abs(np.array(w_gd) - np.array(w_ne)))
    status = "OK" if diff < 1e-3 else "MISMATCH"
    print(f"{name}")
    print(f"  gradient descent: {np.round(w_gd, 4)}   (iterations: {used})")
    print(f"  normal equation:  {np.round(w_ne, 4)}")
    print(f"  max difference:   {diff:.2e}   [{status}]\n")

# 1. One feature (true: slope 2, bias 1)
check("one feature", [[1], [2], [3]], [3, 5, 7], lr=0.05, iterations=10000)

# 2. Three features, no noise (true: [3, -2, 0.5, 4])
X2 = [[1, 2, 0], [2, 1, 4], [0, 3, 2], [3, 0, 1], [1, 1, 1]]
y2 = [3, 10, -1, 13.5, 5.5]
check("three features", X2, y2, lr=0.1, iterations=10000)

# 3. 100 noisy points (close to [3, -2, 0.5, 4])
rng = np.random.default_rng(0)
X3 = rng.normal(size=(100, 3))
y3 = X3 @ np.array([3, -2, 0.5]) + 4 + rng.normal(scale=0.1, size=100)
check("noisy, 100 points", X3, y3, lr=0.05, iterations=10000)

# 4. Learning rate too big: should blow up, not match
check("lr too big (should MISMATCH)", X2, y2, lr=0.2, iterations=200)