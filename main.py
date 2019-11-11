import numpy as np
import plotting as pl
import utility as ut
import parameters as pm
import matplotlib.pyplot as plt


# Total time is timeSteps * k
# 1000 steps for slow plot in 7
# 150000 steps for fast plot in 7
timeSteps = 5000

# Total space is spaceSteps * h
spaceSteps = 101

case = "task17" # "task17"

if case == "task7":
    u = 0.1 # speed
    s_matrix = ut.initialize_1(spaceSteps, timeSteps)
    boundary = 'closed'
    k = 0.01 # delta t
    h = 0.1 # delta x
    K = 1e-12 # permeability
    dp_c = -1e6 # pressure

elif case == "task17":
    u = 0
    s_matrix = ut.initialize_2(spaceSteps, timeSteps)
    boundary = 'open'
    k = 0.01 # delta t
    h = 0.1 # delta x
    K = 1e-8 # permeability
    dp_c = -(pm.rho_w - pm.rho_g) * 9.81 * 3 # pressure


w = np.zeros(len(s_matrix[0]))
animationInterval = 5
s_matrix = ut.upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w, w, boundary = boundary)
pl.plotting_17(s_matrix, spaceSteps, timeSteps, animationInterval, h, k,"slow") # plotting_7 or plotting_17


