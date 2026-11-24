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

def gradient_check(computed_grad, expected_grad, tolerance=1e-6):
    expected = np.array(expected_grad, dtype=float)
    computed = np.array(computed_grad, dtype=float)
    norm_error = np.linalg.norm(expected - computed)
    size = np.linalg.norm(computed) + np.linalg.norm(expected)
    if size == 0:
        return True
    relative_error = norm_error/size
    return relative_error < tolerance


def f_square(p):
    return p[0] ** 2

def f_two_var(p):
    return p[0] ** 2 + 3 * p[0] * p[1]

def f_sin(p):
    return np.sum(np.sin(p))

def run_test(name, f, point, claimed, should_pass):
    point = np.array(point, dtype=float)
    est = gradient(f, point)
    # same ratio gradient_check uses, printed so you can see it
    err = np.linalg.norm(est - np.array(claimed, dtype=float))
    size = np.linalg.norm(est) + np.linalg.norm(np.array(claimed, dtype=float))
    rel = err / size if size != 0 else 0.0
    result = gradient_check(est, claimed)
    status = "OK" if result == should_pass else "UNEXPECTED"
    print(f"{name:32s} rel_error={rel:.3e}  check={result}  expected={should_pass}  [{status}]")

# ---- the tests ----
run_test("correct: x^2 at 3",          f_square,  [3.0],      [6.0],      True)
run_test("wrong: x^2 at 3, claim 7",   f_square,  [3.0],      [7.0],      False)
run_test("subtle: one entry off",      f_two_var, [2.0, 1.0], [7.0, 6.5], False)
run_test("correct: sin",               f_sin,     [0.5, 1.2, 2.0], np.cos([0.5, 1.2, 2.0]), True)
