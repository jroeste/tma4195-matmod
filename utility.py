import numpy as np

def f_function(s, mu_g, mu_w):
    return s/(s*(1-mu_g/mu_w)+ mu_g/mu_w)



def g_function(s, mu_g, mu_w, a):
    return a*s*(1-s)/(s*(1-mu_g/mu_w) + mu_g/mu_w)

def one_step_upwind(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, w):
    w[1:] = g_func(s_vector[1:], mu_g, mu_w, a)*(s_vector[1:]-s_vector[:-1])/h
    f_diff = f_func(s_vector[1:], mu_g, mu_w)-f_func(s_vector[:-1], mu_g, mu_w)
    new_s = s_vector[1:] - ((u*k)/(phi*h))*f_diff - ((k)/(phi*h))*(w[1:]-w[:-1])
    return (new_s)

def one_step_central(s_vector, u, k, phi, h, f_func, g_func, mu_g, mu_w, a, w, boundary):
    w1 = g_func(s_vector[1:-1], mu_g, mu_w, a) * (s_vector[2:] - 2 * s_vector[1:-1] + s_vector[:-2])/h**2
    w2 = (g_func(s_vector[2:], mu_g, mu_w, a) - g_func(s_vector[:-2], mu_g, mu_w, a)) * \
         (s_vector[2:] - s_vector[:-2]) / (4*h**2)
    f_diff = (f_func(s_vector[1:], mu_g, mu_w) - f_func(s_vector[:-1], mu_g, mu_w)) / h
    s_vector[1:] = s_vector[1:] - (u * k / phi) * f_diff
    s_vector[1:-1] = s_vector[1:-1] - (k / phi) * (w1 + w2)
    if boundary == 'open':
        s_vector[0] = s_vector[1] + (s_vector[1] - s_vector[2])*h
        s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    else:
        s_vector[0] = 1
    s_vector[-1] = s_vector[-2] + (s_vector[-2] - s_vector[-3]) * h
    return s_vector

def initialize_1(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))
    s_matrix[0][1:]=0
    return s_matrix


def initialize_2(spaceSteps, timeSteps):
    s_matrix = np.ones((timeSteps, spaceSteps))*0.01
    area = spaceSteps//10
    center = spaceSteps//2
    s_matrix[0][center-area:center+area]=0.99
    return s_matrix

def upwind(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, w, boundary):

    for i in range(timeSteps-1):
        s_matrix[i+1] = one_step_central(s_matrix[i], u, k, phi, h, f_function, g_function, mu_g, mu_w, a, w, boundary)

    return s_matrix