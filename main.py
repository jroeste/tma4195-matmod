import plotting as pl
import utility as ut
import parameters as pm

# This chunk controls what to plot. Case is either "task7", "task17_1", "task17_2" or "task21".
# Plot is either "animation" (makes animation), "report" (makes 4 plots for different times),
# or "scheme_discussion" (plots used in presentation to justify numerical scheme).
# save_to_gif = True will make animation as gif. This might not work without some preparations on pc.
case = "task21"
plot = 'report'
save_to_gif = False

# Set parameters to task 7
if case == "task7" and plot != "scheme_discussion":

    # Which functions to use: Numerical scheme, f(s) and g(s)
    one_step_func = ut.one_step_central
    f_func = ut.f_function
    g_func = ut.g_function

    # Parameters and boundary conditions
    timeSteps = 200000
    u = 1.5e-6 # speed
    boundary = 'closed'
    k = 10 # delta t
    extra_parameters = {'dp_c' : -pm.P_0}

    # Initial conditions
    s_matrix = ut.initialize_1(pm.spaceSteps, timeSteps)

    # Animation speed control
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 100


elif case == "task17_1" and plot != "scheme_discussion":

    # Which functions to use: Numerical scheme, f(s) and g(s)
    one_step_func = ut.one_step_central
    f_func = ut.f_function
    g_func = ut.g_function

    # Parameters and boundary conditions
    timeSteps = 200000
    u = 1.5e-6
    boundary = 'closed'
    k = 10  # delta t
    H = 100
    extra_parameters = {'dp_c': -(pm.rho_w - pm.rho_g) * pm.g * H}

    # Initial conditions
    s_matrix = ut.initialize_1(pm.spaceSteps, timeSteps)

    # Animation speed control
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 100

elif case == "task17_2" or plot == "scheme_discussion":

    # Which functions to use: Numerical scheme, f(s) and g(s)
    one_step_func = ut.one_step_central
    f_func = ut.f_function
    g_func = ut.g_function

    # Parameters and boundary conditions
    timeSteps = 75000
    u = 0
    boundary = 'open'
    k = 2  # delta t
    H = 100
    extra_parameters = {'dp_c': -(pm.rho_w - pm.rho_g) * pm.g * H}

    # Initial conditions
    s_matrix = ut.initialize_2(pm.spaceSteps, timeSteps)

    # Animation speed control
    if save_to_gif:
        scale_animation_time = 500
    else:
        scale_animation_time = 50

elif case == "task21" and plot != "scheme_discussion":

    # Which functions to use: Numerical scheme, f(s) and g(s)
    one_step_func = ut.one_step_central_21
    f_func = ut.f_function
    g_func = ut.g_21

    # Parameters and boundary conditions
    timeSteps = 60000
    u = 0
    boundary = 'open'
    k = 50 # delta t
    extra_parameters = {'H' : 10, 'theta' : 1, 'rho_g' : pm.rho_g, 'rho_w' : pm.rho_w, 'g' : pm.g}

    # Initial conditions
    s_matrix = ut.initialize_3(pm.spaceSteps, timeSteps, pm.h)

    # Animation speed control
    if save_to_gif:
        scale_animation_time = 1000
    else:
        scale_animation_time = 20


# Solves equation by numerical scheme and plots appropriate stuff
if plot == 'animation':
    s_matrix = ut.num_scheme(one_step_func, s_matrix, timeSteps, u, k, pm.phi, pm.h, f_func,
                             g_func, pm.mu_g, pm.mu_w, pm.K, boundary, **extra_parameters)
    pl.plot_animation(s_matrix, pm.spaceSteps, timeSteps, pm.animationSpeed, pm.h, k, case, scale_animation_time, save_to_gif, **extra_parameters)
elif plot == 'report':
    s_matrix = ut.num_scheme(one_step_func, s_matrix, timeSteps, u, k, pm.phi, pm.h, f_func,
                             g_func, pm.mu_g, pm.mu_w, pm.K, boundary, **extra_parameters)
    pl.plot_report(s_matrix, pm.h, pm.spaceSteps, timeSteps, k, case, **extra_parameters)
elif plot == "scheme_discussion":

    # Plot one
    one_step_func = ut.one_step_full_upwind
    timeSteps = 50
    s_matrix_1 = ut.initialize_2(pm.spaceSteps, timeSteps)
    s_matrix_1 = ut.num_scheme(one_step_func, s_matrix_1, timeSteps, u, k, pm.phi, pm.h, f_func,
                             g_func, pm.mu_g, pm.mu_w, pm.K, boundary, **extra_parameters)

    # Plot two
    one_step_func = ut.one_step_semi_upwind
    timeSteps = 3000
    s_matrix_2 = ut.initialize_2(pm.spaceSteps, timeSteps)
    s_matrix_2 = ut.num_scheme(one_step_func, s_matrix_2, timeSteps, u, k, pm.phi, pm.h, f_func,
                               g_func, pm.mu_g, pm.mu_w, pm.K, boundary, **extra_parameters)

    pl.plot_discuss_schemes(s_matrix_1, s_matrix_2, pm.spaceSteps, pm.h)



