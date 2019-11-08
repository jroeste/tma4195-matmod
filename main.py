import numpy as np
import plotting as pl
import utility as ut
import parameters as pm
import matplotlib.pyplot as plt



def cases(case):
    if case == 1:
        u = 1
        s_matrix = ut.initialize_1(pm.spaceSteps, pm.timeSteps)
        boundary = 'closed'
    elif case == 2:
        u = 0
        s_matrix = ut.initialize_2(pm.spaceSteps, pm.timeSteps)
        boundary = 'open'
    return u, s_matrix, boundary

u, s_matrix ,boundary = cases(2)
w=np.zeros(len(s_matrix[0]))
animationInterval = 5
s_matrix = ut.upwind(s_matrix, pm.timeSteps, u, pm.k, pm.phi, pm.h, pm.mu_g, pm.mu_w, pm.a, w, boundary = boundary)
pl.plotting_17(s_matrix, pm.spaceSteps, pm.timeSteps, animationInterval, pm.h, pm.k)



