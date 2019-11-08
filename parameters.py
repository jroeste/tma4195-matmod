# Total time is timeSteps * k
timeSteps=50000
k=0.1

# Total space is spaceSteps * h
spaceSteps=101
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