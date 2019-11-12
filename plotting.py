import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utility as ut

import os

def save_animations(anim_object,filename):
    path = "C:\\Users\julie\Downloads\\"+filename
    anim_object.save(path+".mp4", writer="ffmpeg", fps=30)
    os.system("ffmpeg -i "+path+".mp4 "+path+".gif")


def plotting_7(s_matrix, spaceSteps, timeSteps, interval, h, k, save_to_gif):

    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    ax = plt.axes(ylim=(0, 1))
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('saturation')
    line, = ax.plot(x, s_matrix[0])

    time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

    def init():  # give a clean slate to start
        line.set_ydata([np.nan] * len(x))
        time_text.set_text('')
        return line,

    def animate(i):
        y = s_matrix[i]
        line.set_ydata(y)
        if i % 100 == 0:
            time_text.set_text('t = ' + str(round(i * k, 2)))
        return line,time_text,

    def animate_to_gif_slow(i):
        y = s_matrix[10*i]
        line.set_ydata(y)
        if 10*i % 100 == 0:
            time_text.set_text('t = ' + str(round(10*i * k, 2)))
        return line, time_text,

    def animate_to_gif_fast(i):
        y = s_matrix[1000*i]
        line.set_ydata(y)
        time_text.set_text('t = ' + str(round(200*i * k, 2)))
        return line, time_text,

    if save_to_gif=="slow":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif_slow, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps/10)
        save_animations(ani_to_gif, "anim_task7_slow")

    elif save_to_gif=="fast":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif_fast, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps / 1000)
        save_animations(ani_to_gif, "anim_task7_fast")

    else:
        ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps)
        plt.show()

def plotting_17(s_matrix, spaceSteps, timeSteps, interval, h, k,save_to_gif):

    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    ax = plt.axes(xlim=(-1.5,12),ylim=(1, 0))
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    line, = ax.plot(x, s_matrix[0])
    time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

    def init():  # give a clean slate to start
        line.set_ydata([np.nan] * len(x))
        time_text.set_text('')
        return line,

    def animate(i):
        y = s_matrix[i]
        line.set_ydata(y)
        if i % 100 == 0:
            time_text.set_text('t = ' + str(round(i * k, 2)))
        filling_grey = plt.fill_between(x, y, 0, facecolors='silver')
        filling_blue = plt.fill_between(x, y, 1, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    def animate_to_gif(i):
        scalar = 2*100
        y = s_matrix[i*scalar]
        line.set_ydata(y)
        time_text.set_text('t = ' + str(round(scalar*i * k, 2)))
        filling_grey = plt.fill_between(x, y, 0, facecolors='silver')
        filling_blue = plt.fill_between(x, y, 1, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    if save_to_gif=="slow":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps/(2*100))
        save_animations(ani_to_gif, "anim_task17_1")
    else:
        ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps)
        plt.show()

def plotting_21(s_matrix, spaceSteps, timeSteps, interval, h, k, theta,save_to_gif):

    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    ax = plt.axes(xlim=(-1.5,12),ylim=(1, 0-1/10*x[-1]*np.tan(theta)))
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    line, = ax.plot(x, s_matrix[0])
    time_text = ax.text(0.1, 0.8, '', transform=ax.transAxes)

    def init():  # give a clean slate to start
        line.set_ydata([np.nan] * len(x))
        time_text.set_text('')
        return line,

    def animate(i):
        scalar = 100*2
        lower = -1/10*np.tan(theta)*x
        upper = -1/10*np.tan(theta)*x + 1
        y = s_matrix[i*scalar] - 1/10*np.tan(theta)*x
        line.set_ydata(y)
        if i*scalar % 100 == 0:
            time_text.set_text('t = ' + str(round(i*scalar * k, 2)))
        filling_grey = plt.fill_between(x, y, lower, facecolors='silver')
        filling_blue = plt.fill_between(x, y, upper, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    def animate_to_gif(i):
        scalar = 40*100
        lower = -1/10*np.tan(theta)*x
        upper = -1/10*np.tan(theta)*x + 1
        y = s_matrix[i*scalar] - 1/10*np.tan(theta)*x
        line.set_ydata(y)
        if i*scalar % 100 == 0:
            time_text.set_text('t = ' + str(round(i*scalar * k, 2)))
        filling_grey = plt.fill_between(x, y, lower, facecolors='silver')
        filling_blue = plt.fill_between(x, y, upper, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    if save_to_gif=="slow":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps /(40*100))
        save_animations(ani_to_gif, "anim_task21")
    else:
        ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps/(2*100))
        plt.show()

def plot_report_7(s_matrix, h, spaceSteps,timeSteps, k, name):
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    indexes = np.array([0,5000,25000,timeSteps-1])
    times = np.round(indexes*k/(3600),1)
    print(times)

    axs[0].plot(x, s_matrix[indexes[0]])
    axs[0].set_title("t = "+str(times[0])+" h")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Gas saturation s')
    axs[1].plot(x, s_matrix[indexes[1]])
    axs[1].set_title("t = "+str(times[1])+" h")
    axs[1].set_xlabel('x')
    axs[2].plot(x, s_matrix[indexes[2]])
    axs[2].set_title("t = "+str(times[2])+" h")
    axs[2].set_xlabel('x')
    axs[3].plot(x, s_matrix[indexes[3]])
    axs[3].set_title("t = "+str(times[3])+" h")
    axs[3].set_xlabel('x')

    plt.savefig(name)
    plt.show()

def plot_report_17(s_matrix, h, spaceSteps,timeSteps,k, name):
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    indexes = np.array([0, 8000, 25000, timeSteps - 1])
    times = np.round(indexes * k / (3600), 1)
    print(times)

    axs[0].set_ylim([1, 0])
    y = s_matrix[indexes[0]]
    axs[0].plot(x, y)
    axs[0].fill_between(x, y, 0, facecolors='silver')
    axs[0].fill_between(x,y, 1, facecolors='lightblue')
    axs[0].set_title("t = "+str(times[0])+" h")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('S = h/H')
    axs[0].grid()

    axs[1].set_ylim([1, 0])
    y = s_matrix[indexes[1]]
    axs[1].plot(x, y)
    axs[1].fill_between(x, y, 0, facecolors='silver')
    axs[1].fill_between(x, y, 1, facecolors='lightblue')
    axs[1].set_title("t = "+str(times[1])+" h")
    axs[1].set_xlabel('x')
    axs[1].grid()
    y = s_matrix[indexes[2]]
    axs[2].set_ylim([1, 0])
    axs[2].plot(x,y)
    axs[2].fill_between(x, y, 0, facecolors='silver')
    axs[2].fill_between(x,y, 1, facecolors='lightblue')
    axs[2].set_title("t = "+str(times[2])+" h")
    axs[2].set_xlabel('x')
    axs[2].grid()

    axs[3].set_ylim([1, 0])
    axs[3].plot(x, s_matrix[-1])
    axs[3].fill_between(x, s_matrix[-1], 0, facecolors='silver')
    axs[3].fill_between(x, s_matrix[-1], 1, facecolors='lightblue')
    axs[3].set_title("t = "+str(times[3])+" h")
    axs[3].set_xlabel('x')
    axs[3].grid()


    plt.savefig(name)
    #plt.show()

def plot_report_21(s_matrix, h, spaceSteps, name, theta,timeSteps,k):

    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1,4,figsize = (15,4),sharey = True)

    time_0 = 0*k
    axs[0].set_xlim([-1.5, 12])
    axs[0].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(theta)])
    y = s_matrix[0]-1/10*np.tan(theta)*x
    axs[0].plot(x, y)
    axs[0].fill_between(x, y, -1/10*np.tan(theta)*x, facecolors='silver')
    axs[0].fill_between(x, y, 1-1/10*np.tan(theta)*x, facecolors='lightblue')
    axs[0].set_title("t = "+str(time_0/(3600*24))+" days")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('S + x/X * tan(theta)')
    axs[0].grid()

    axs[1].set_xlim([-1.5, 12])
    axs[1].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(theta)])
    time_0 = 15000*k
    y = s_matrix[15000] - 1 / 10 * np.tan(theta) * x
    axs[1].plot(x, y)
    axs[1].fill_between(x, y, - 1 / 10 * np.tan(theta) * x , facecolors='silver')
    axs[1].fill_between(x, y, 1 - 1 / 10 * np.tan(theta) * x, facecolors='lightblue')
    axs[1].set_title("t = "+str(round(time_0/(3600*24),1))+" days")
    axs[1].set_xlabel('x')
    axs[1].grid()

    axs[2].set_xlim([-1.5, 12])
    axs[2].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(theta)])
    time_0 = 30000* k
    y = s_matrix[30000] - 1 / 10 * np.tan(theta) * x
    axs[2].plot(x, y)
    axs[2].fill_between(x, y, - 1 / 10 * np.tan(theta) * x, facecolors='silver')
    axs[2].fill_between(x, y, 1 - 1 / 10 * np.tan(theta) * x, facecolors='lightblue')
    axs[2].set_title("t = "+str(round(time_0/(3600*24),1))+" days")
    axs[2].set_xlabel('x')
    axs[2].grid()

    axs[3].set_xlim([-1.5, 12])
    axs[3].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(theta)])
    time_0 = timeSteps*k
    y = s_matrix[-1] - 1 / 10 * np.tan(theta) * x
    axs[3].plot(x, y)
    axs[3].fill_between(x, y,- 1 / 10 * np.tan(theta) * x , facecolors='silver')
    axs[3].fill_between(x, y, 1- 1 / 10 * np.tan(theta) * x, facecolors='lightblue')
    axs[3].set_title("t = "+str(round(time_0/(3600*24),1))+" days")
    axs[3].set_xlabel('x')
    axs[3].grid()


    plt.savefig(name)

def plot_discuss_schemes(s_matrix_1,s_matrix_2,spaceSteps,h):

    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1,2,figsize = (15,4),sharey = True)
    axs[0].plot(x, s_matrix_1[-1])
    axs[0].set_title("Full upwind")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('S')
    axs[0].grid()

    axs[1].plot(x, s_matrix_2[-1])
    axs[1].set_title("Semi upwind")
    axs[1].set_xlabel('x')
    axs[1].grid()
    plt.savefig("num_stability.pdf",transparent=True)