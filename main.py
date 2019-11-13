import numpy as np
import plotting as pl
import utility as ut
import parameters as pm

# Total space is spaceSteps * h
spaceSteps = 101

case = "task17_2" # "task17_1" "task17_2"
plot = 'report'
save_to_gif = False

if case == "task7":
    one_step_func = ut.one_step_central
    timeSteps = 200000
    u = 1.5e-6 # speed
    s_matrix = ut.initialize_1(spaceSteps, timeSteps)
    boundary = 'closed'
    k = 10 # delta t
    h = 0.1 # delta x
    K = 1e-13 # permeability
    dp_c = -1e6 # pressure
    H = None
    theta = None
    f_func = ut.f_function
    g_func = ut.g_function
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 100


elif case == "task17_1":
    one_step_func = ut.one_step_central
    timeSteps = 200000
    u = 1.5e-6
    s_matrix = ut.initialize_1(spaceSteps, timeSteps)
    boundary = 'closed'
    k = 10 # delta t
    h = 0.1 # delta x
    K = 1e-13 # permeability
    H = 100
    dp_c = -(pm.rho_w - pm.rho_g) * pm.g * H # pressure
    theta = None
    f_func = ut.f_function
    g_func = ut.g_function
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 100

elif case == "task17_2":
    one_step_func = ut.one_step_central
    timeSteps = 75000
    u = 0
    s_matrix = ut.initialize_2(spaceSteps, timeSteps)
    boundary = 'open'
    k = 2 # delta t
    h = 0.1 # delta x
    K = 1e-13# permeability
    H = 100
    dp_c = -(pm.rho_w - pm.rho_g) * pm.g * H # pressure
    theta = None
    f_func = ut.f_function
    g_func = ut.g_function
    if save_to_gif:
        scale_animation_time = 500
    else:
        scale_animation_time = 50

elif case == "task21":
    one_step_func = ut.one_step_central_21
    timeSteps = 60000
    u = 0
    boundary = 'open'
    k = 50 # delta t
    h = 0.1 # delta x
    K = 1e-13 # permeability
    dp_c = None
    H = 10
    theta = 1
    f_func = ut.f_function
    g_func = ut.g_21
    s_matrix = ut.initialize_3(spaceSteps, timeSteps, h)
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 20

animationSpeed = 5

s_matrix = ut.num_scheme(one_step_func, s_matrix, timeSteps, u, k, dp_c, pm.phi, h, pm.mu_g, pm.mu_w, pm.rho_w, pm.rho_g, K, pm.g, H, theta, boundary, f_func, g_func)

if plot == 'animation':
    pl.plot_animation(s_matrix, spaceSteps, timeSteps, animationSpeed, h, k, case, scale_animation_time, theta, save_to_gif)
else:
    pl.plot_report(s_matrix, h, spaceSteps, timeSteps,k, case, theta)

"""
elif case == "discuss_schemes":
    u = 0
    boundary = 'open'
    k = 10  # delta t
    h = 0.1  # delta x
    K = 1e-13  # permeability
    dp_c = -(pm.rho_w - pm.rho_g) * 9.81 * 100  # pre

    timeSteps = 50
    s_matrix_1 = ut.initialize_2(spaceSteps, timeSteps)
    s_matrix_1 = ut.full_upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w,
                                boundary=boundary)

    s_matrix_2 = ut.initialize_2(spaceSteps, timeSteps)
    s_matrix_2 = ut.semi_upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w,
                                boundary=boundary)
    pl.plot_discuss_schemes(s_matrix_1, s_matrix_2, spaceSteps, h)
"""





