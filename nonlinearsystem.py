import numpy as np

def Newton_system(F, J, x, eps):
  
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1
        
    if abs(F_norm) > eps:
        iteration_counter = -1
    return x, iteration_counter

    def system_project():

        def F(x):
            return np.array(
            [x[2]**2 + x[2] + (50*x[2]**2) + x[2]**2 - 200,
             x[2]**2 + (20*x[2]) + x[2]**2 - 50,
             -x[2]**2 - x[2]**2 + (40*x[2]) + 57])
        def J(x):
            return np.array([
            [[2*x[2]+50], 2*x[2], 2*x[2]],
            [2*x[2], 20, 2*x[2]],
            [2*x[2], -2*x[2], 40]])
           
        
        expected = np.array([1, 0, 1])
        tol = 1e-4
        x, n = Newton_system(F, J, x=eps.array([2, 2, 2]), eps=0.00005)
        print(n, x)
        assert(error_norm < tol, 
               ’norm of error =%g’ % error_norm)
        print(’norm of error =%g’, % error_norm)