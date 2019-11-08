import numpy as np
import plotting as pl
import utility as ut
import matplotlib.pyplot as plt

# Total time is timeSteps * k
timeSteps=5000
k=0.1

# Total space is spaceSteps * h
spaceSteps=100
h=0.1

### Parameters ###

# Porousity
phi=1/2

# Viscousity
mu_g=3.08e-5
mu_w=8.9e-4

# Density
rho_g = 1.98
rho_w = 997

# Permeability
K = 1e-9

# Pressure
#dp_c = -1e6
dp_c = -(rho_w-rho_g)*9.81*3

a = K*dp_c/mu_w

def cases(case):
    if case == 1:
        u = 1
        s_matrix = ut.initialize_1(spaceSteps, timeSteps)
        boundary = 'closed'
    elif case == 2:
        u = 0
        s_matrix = ut.initialize_2(spaceSteps, timeSteps)
        boundary = 'open'
    return u, s_matrix, boundary

u, s_matrix ,boundary = cases(2)
w=np.zeros(len(s_matrix[0]))
animationInterval = 5
s_matrix = ut.upwind(s_matrix, timeSteps, u, k, phi, h, mu_g, mu_w, a, w, boundary = boundary)
pl.plotting_17(s_matrix, spaceSteps, timeSteps, animationInterval, h, k)






