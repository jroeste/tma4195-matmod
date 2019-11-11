import numpy as np
import plotting as pl
import utility as ut
import parameters as pm
import matplotlib.pyplot as plt


# Total time is timeSteps * k
timeSteps = 500001

# Total space is spaceSteps * h
spaceSteps = 101

case = "task17_2" # "task17"

if case == "task7":
    u = 2 # speed
    s_matrix = ut.initialize_1(spaceSteps, timeSteps)
    boundary = 'closed'
    k = 0.001 # delta t
    h = 0.1 # delta x
    K = 1e-10 # permeability
    dp_c = -1e6 # pressure
    plot_func_ani = pl.plotting_7
    plot_func = pl.plot_report_7
    name = 'task7.pdf'


elif case == "task17_1":
    u = 2
    s_matrix = ut.initialize_1(spaceSteps, timeSteps)
    boundary = 'closed'
    k = 0.001 # delta t
    h = 0.1 # delta x
    K = 1e-10 # permeability
    dp_c = -(pm.rho_w - pm.rho_g) * 9.81 * 100 # pressure
    plot_func_ani = pl.plotting_17
    plot_func = pl.plot_report_17
    name = 'task17_1.pdf'


elif case == "task17_2":
    u = 0
    s_matrix = ut.initialize_2(spaceSteps, timeSteps)
    boundary = 'open'
    k = 0.001 # delta t
    h = 0.1 # delta x
    K = 1e-10 # permeability
    dp_c = -(pm.rho_w - pm.rho_g) * 9.81 * 100 # pressure
    plot_func_ani = pl.plotting_17
    plot_func = pl.plot_report_17
    name = 'task17_2.pdf'




animationInterval = 1
#s_matrix = ut.upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w, boundary = boundary)
#plot_func_ani(s_matrix, spaceSteps, timeSteps, animationInterval, h, k) # plotting_7 or plotting_17

#plot_func(s_matrix, h, spaceSteps, name = name)

u = 0
s_matrix = ut.initialize_3(spaceSteps, timeSteps, h)
boundary = 'open'
k = 0.001 # delta t
h = 0.1 # delta x
K = 3e-10 # permeability
g = 9.81
H = 10
theta = 1

x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)

s_matrix = ut.upwind_21(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, pm.rho_w, pm.rho_g, K, g, H, theta, boundary)

pl.plotting_21(s_matrix, spaceSteps, timeSteps, animationInterval, h, k, theta)

