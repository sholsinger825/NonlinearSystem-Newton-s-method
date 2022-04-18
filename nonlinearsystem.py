import sys
from numpy import *
def Newton_system(F, J, x, eps):
    
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x0 + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1
    # Here, either a solution is found, or too many iterations
    if abs(F_norm) > eps:
        iteration_counter = -1
    return x, iteration_counter
    
    def F(x):
        return matrix(
            [x[2]**2 + x[2] + (50*x[2]**2) + x[2]**2 - 200,
            x[2]**2 + (20*x[2]) + x[2]**2 - 50,
            -x[2]**2 - x[2]**2 + (40*x[2]) + 57])
    def J(x):
        return matrix([
            [[2*x[2]+50], 2*x[2], 2*x[2]],
            [2*x[2], 20, 2*x[2]],
            [2*x[2], -2*x[2], 40]])
            
            
    expected = matrix([[2.0, 2.0, 2.0]]).T # Starting vector

    tol = 1e-4
    x, n = Newton_system(F, J, x=matrix([2, 2, 2]), eps=0.00005)
    print(n, x)
    error_norm = np.linalg.norm(expected - x, ord=2)
    assert error_norm < tol, "norm of error =%g" % error_norm

    print("norm of error =%g" % error_norm)
