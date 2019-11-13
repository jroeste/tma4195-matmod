import numpy as np

# f(s) as found in all tasks in report
def f_function(s, mu_g, mu_w):
    return s/(s*(1-mu_g/mu_w)+ mu_g/mu_w)

# g(s) as found in 21 in report
def g_21(s, mu_g, mu_w, rho_g, rho_w, g, K):
    return (rho_w-rho_g)*g*K*(mu_g/mu_w)*s*(1-s)/(mu_g*(s + (mu_g/mu_w)*(1-s)))

# g(s) as found in 6 and 16 in report
def g_function(s, mu_g, mu_w, a):
    return a*s*(1-s)/(s*(1-mu_g/mu_w) + mu_g/mu_w)

# Numerical scheme for task 21. It actually uses upwind in the g(s)_x s_x part, which is fine because this
# case is not really symmetrical.
def one_step_central_21(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters):

    H, theta, rho_g, rho_w, g = extra_parameters.values()

    # g(s) is set to zero at edges to close the area, thus containing the gas
    g = g_func(s_vector, mu_g, mu_w, rho_g, rho_w, g, K)
    g[0] = 0
    g[-1] = 0
    g[-2] = 0

    # Central differences in s_xx part
    w1 = g[1:-1] * (-H) * np.cos(theta) * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2

    # Upwind differences in g(s)_x s_x - part and f(s)_x - part
    w2 = ((g[1:] - g[:-1]) / (h)) * (-H * np.cos(theta) * (s_vector[1:] - s_vector[:-1]) / (h) + np.sin(theta))
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h

    # Update next step
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1)

    # Linear interpolation at end points unless boundary is 'closed', in which case left side is set to 1
    if boundary == 'open':
        s_vector[0] =  s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] - (s_vector[-2] - s_vector[-3]) * h

    # Some instability for very small values of s, resulting in negative values. This sets
    # negative values to zero, resulting in more stable solutions (which appear identical).
    s_vector = s_vector.clip(0)

    return s_vector

def one_step_semi_upwind(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters):

    a = K * extra_parameters['dp_c'] / mu_w

    # g(s) is set to zero at edges to close the area, thus containing the gas
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0

    # Central in s_xx part
    w1 = g[1:-1] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2

    # Upwind in g(s)_x s_x  and f(s)_x part
    w2 = (g[1:] - g[:-1]) * (s_vector[1:] - s_vector[:-1]) / (h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h

    # Update next step
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1)

    # Linear interpolation at end points unless boundary is 'closed', in which case left side is set to 1
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h

    return s_vector

def one_step_full_upwind(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters):

    a = K * extra_parameters['dp_c'] / mu_w

    # g(s) is set to zero at edges to close the area, thus containing the gas
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0

    # Upwind in all parts
    w1 = g[2:] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[1:] - g[:-1]) * (s_vector[1:] - s_vector[:-1]) / (h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h

    # Update next step
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    s_vector[2:] = s_vector[2:] - (k / phi) * (w1)

    # Linear interpolation at end points unless boundary is 'closed', in which case left side is set to 1
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector


def one_step_central(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters):#dp_c, rho_w, rho_g, g, H, theta):

    a = K * extra_parameters['dp_c'] / mu_w

    # g(s) is set to zero at edges to close the area, thus containing the gas
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0

    # Central in s_xx part and g(s)_x s_x part
    w1 = g[1:-1] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[2:] - g[:-2]) * (s_vector[2:] - s_vector[:-2]) / (4*h**2)

    # Upwind in f(s)_x part
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h

    # Update nect step
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1 + w2)

    # Linear interpolation at end points unless boundary is 'closed', in which case left side is set to 1
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h

    return s_vector

# Initial condition given by s(x,0) = 0
def initialize_1(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))
    s_matrix[0]=0
    return s_matrix

# Initial condition given by a column of gas in the middle, water elsewhere
def initialize_2(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))*0.01
    area = spaceSteps//10
    center = spaceSteps//2
    s_matrix[0][center-area:center+area]=0.99
    return s_matrix

# Initial conditions given by square root function
def initialize_3(spaceSteps, timeSteps, h):
    s_matrix = np.zeros((timeSteps, spaceSteps))
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    X = len(x)//2
    s_matrix[0][:X] = 1 / 8 *np.sqrt(x[X] - x[:X])
    return s_matrix

# Runs the various schemes
def num_scheme(one_step_func, s_matrix, timeSteps, u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters): # boundary, dp_c, rho_w, rho_g, g, H, theta):

    for i in range(timeSteps - 1):
        s_matrix[i+1] = one_step_func(s_matrix[i], u, k, phi, h, f_func, g_func, mu_g, mu_w, K, boundary, **extra_parameters)#boundary, dp_c, rho_w, rho_g, g, H, theta)

    return s_matrix