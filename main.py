import numpy as np
import plotting as pl
import utility as ut
import parameters as pm
import matplotlib.pyplot as plt


# Total time is timeSteps * k

# 1000 steps for slow plot in 7
# 150000 steps for fast plot in 7
# timeSteps = 500001 for plot in 17
timeSteps = 10000#0


# Total space is spaceSteps * h
spaceSteps = 101


case = "task17_1" # "task17_1" "task17_2"
speed = "slow"

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
    s_matrix = ut.initialize_2(spaceSteps, timeSteps)
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

elif case == "task21":
    u = 0
    boundary = 'open'
    k = 0.001 # delta t
    h = 0.1 # delta x
    K = 1e-9 # permeability
    g = 9.81
    H = 10
    theta = 1
    s_matrix = ut.initialize_3(spaceSteps, timeSteps, h)
    plot_func =  pl.plot_report_21
    name = 'task21.pdf'

w = np.zeros(len(s_matrix[0]))
animationInterval = 5

if case == "task21":
   s_matrix = ut.upwind_21(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, pm.rho_w, pm.rho_g, K, g, H, theta, boundary)
   #plot_func(s_matrix, h, spaceSteps, name, theta,timeSteps,k)
   #plt.plot(s_matrix[0])
   #plt.show()
   pl.plotting_21(s_matrix, spaceSteps, timeSteps, animationInterval, h, k, theta,speed)
else:
   s_matrix = ut.upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w, boundary = boundary)
   plot_func_ani(s_matrix, spaceSteps, timeSteps, animationInterval, h, k, speed) # plotting_7 or plotting_17
   # plot_func(s_matrix, h, spaceSteps, name = name)


# import os
# filename = "anim_task21"
# path = "C:\\Users\julie\Downloads\\"+filename
# os.system("ffmpeg -i "+path+".mp4 "+path+".gif")

# u = 0
# boundary = 'open'
# k = 0.001 # delta t
# h = 0.1 # delta x
# K = 1e-10 # permeability
# dp_c = -(pm.rho_w - pm.rho_g) * 9.81 * 100 # pre
#
#
#
# x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
#
# timeSteps = 50
# s_matrix = ut.initialize_2(spaceSteps, timeSteps)
# s_matrix = ut.full_upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w, boundary = boundary)
# fig, axs = plt.subplots(1,2,figsize = (15,4),sharey = True)
#
# axs[0].plot(x, s_matrix[-1])
#
# axs[0].set_title("Full upwind")
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('S')
# axs[0].grid()
#
#
# #plt.plot(x,s_matrix[-1])
# #plt.show()
#
# timeSteps = 3000
# s_matrix = ut.initialize_2(spaceSteps, timeSteps)
# s_matrix = ut.semi_upwind(s_matrix, timeSteps, u, k, pm.phi, h, pm.mu_g, pm.mu_w, K * dp_c / pm.mu_w, boundary = boundary)
#
#
# axs[1].plot(x, s_matrix[-1])
# axs[1].set_title("Semi upwind")
# axs[1].set_xlabel('x')
# axs[1].grid()
# #plt.plot(x,s_matrix[-1])
# plt.savefig("num_stability.pdf",transparent=True)
#
