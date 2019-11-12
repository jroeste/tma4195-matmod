import numpy as np

def f_function(s, mu_g, mu_w):
    return s/(s*(1-mu_g/mu_w)+ mu_g/mu_w)

def g_21(s, mu_g, mu_w, rho_g, rho_w, g, K):
    return (rho_w-rho_g)*g*K*(mu_g/mu_w)*s*(1-s)/(mu_g*(s + (mu_g/mu_w)*(1-s)))

def g_function(s, mu_g, mu_w, a):
    return a*s*(1-s)/(s*(1-mu_g/mu_w) + mu_g/mu_w)

def one_step_central_21(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, rho_w, rho_g, K, g, H, theta, boundary):
    g = g_func(s_vector, mu_g, mu_w, rho_g, rho_w, g, K)
    g[0] = 0
    g[-1] = 0
    g[-2] = 0
    #g[-3] = 0
    w1 = g[1:-1] * (-H) * np.cos(theta) * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    #w2 = ((g[2:] - g[:-2])/(2*h)) * (-H*np.cos(theta)*(s_vector[2:] - s_vector[:-2]) / (2*h) + np.sin(theta))
    w2 = ((g[1:] - g[:-1]) / (h)) * (-H * np.cos(theta) * (s_vector[1:] - s_vector[:-1]) / (h) + np.sin(theta))
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h
    #s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    #s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1 + w2)
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1)
    if boundary == 'open':
        s_vector[0] =  s_vector[1] + (s_vector[1] - s_vector[2])*h #max(0, s_vector[1] + (s_vector[1] - s_vector[2])*h)
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] - (s_vector[-2] - s_vector[-3]) * h
    s_vector = s_vector.clip(0)
    return s_vector

def upwind_21(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, rho_w, rho_g, K, g, H, theta, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_central_21(s_matrix[i], u, k, phi, h, f_function, g_21, mu_g, mu_w, rho_w, rho_g, K, g, H, theta, boundary)

    return s_matrix

def one_step_full_central(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, boundary):
    g = g_func(s_vector, mu_g, mu_w, a)
    w1 = g[1:-1] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[2:] - g[:-2]) * (s_vector[2:] - s_vector[:-2]) / (4*h**2)
    f_diff = (f_func(s_vector[2:], mu_g, mu_w) - f_func(s_vector[:-2], mu_g, mu_w)) /(2 * h)
    s_vector[1:-1] = s_vector[1:-1] - (u * k / phi) * f_diff
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1 + w2)
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector

def full_central(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_full_central(s_matrix[i], u, k, phi, h, f_function, g_function, mu_g, mu_w, a, boundary)

    return s_matrix

def one_step_semi_upwind(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, boundary):
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0
    w1 = g[1:-1] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[1:] - g[:-1]) * (s_vector[1:] - s_vector[:-1]) / (h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1)
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector

def semi_upwind(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_semi_upwind(s_matrix[i], u, k, phi, h, f_function, g_function, mu_g, mu_w, a, boundary)

    return s_matrix

def one_step_full_upwind(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, boundary):
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0
    w1 = g[2:] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[1:] - g[:-1]) * (s_vector[1:] - s_vector[:-1]) / (h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff - (k / phi) * (w2)
    s_vector[2:] = s_vector[2:] - (k / phi) * (w1)
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector

def full_upwind(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_full_upwind(s_matrix[i], u, k, phi, h, f_function, g_function, mu_g, mu_w, a, boundary)

    return s_matrix


def one_step_central(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, boundary):
    g = g_func(s_vector, mu_g, mu_w, a)
    g[0] = 0
    g[-1] = 0
    w1 = g[1:-1] * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2]) / h ** 2
    w2 = (g[2:] - g[:-2]) * (s_vector[2:] - s_vector[:-2]) / (4*h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1 + w2)
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector

def initialize_1(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))
    s_matrix[0]=0
    return s_matrix


def initialize_2(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))*0.01
    area = spaceSteps//10
    center = spaceSteps//2
    s_matrix[0][center-area:center+area]=0.99
    return s_matrix

def initialize_3(spaceSteps, timeSteps, h):
    s_matrix = np.zeros((timeSteps, spaceSteps))
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    X = len(x)//2
    print(x[:X])
    #s_matrix[0][:X]=1/5*np.log(1+ 1*(x[X]-x[:X]))
    s_matrix[0][:X] = 1 / 8 *np.sqrt(1 * (x[X] - x[:X]))
    return s_matrix

def upwind(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_central(s_matrix[i], u, k, phi, h, f_function, g_function, mu_g, mu_w, a, boundary)

    return s_matrix