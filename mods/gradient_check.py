import numpy as np

def gradient(function, point, nudge_size=1e-5):
    point = np.array(point, dtype=float)
    grad = np.zeros_like(point)
    for i in range(len(point)):
        point_plus = point.copy()
        point_minus = point.copy()
        point_plus[i] += nudge_size
        point_minus[i] -= nudge_size
        grad[i] = (function(point_plus)-function(point_minus))/(2*nudge_size)
    return grad

def gradient_check(computed_grad, expected_grad, tolerance=0.001):
    expected = np.array(expected_grad, dtype=float)
    computed = np.array(computed_grad, dtype=float)
    mean_error = np.mean(np.abs(expected - computed))
    return mean_error < tolerance


def f(p):
    return p[0]**2 + 3 * p[1]

point = [3.0, 2.0]
num_grad = gradient(f, point)      # Yields ~[6.0, 3.0]
exact_grad = [6.0, 3.0]            # Analytical gradient

print(gradient_check(num_grad, exact_grad))

