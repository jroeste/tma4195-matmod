import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import utility as ut

import os

def save_animations(anim_object,filename):
    FFwriter = animation.FFMpegWriter()
    #path = "C:\\Users\julie\Downloads\\"+filename
    path = "C:\\Users\jnols\Downloads\\"+filename
    anim_object.save(path+".mp4", writer='ffmpeg', fps=30)
    os.system("ffmpeg -i "+path+".mp4 "+path+".gif")

def plot_animation(s_matrix, spaceSteps, timeSteps, interval, h, k, name, scale_animation_time, theta, save_to_gif = False):

    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    X = (spaceSteps-1)*h


    if name == 'task7':
        ax = plt.axes(ylim=(0, 1))
        ax.set_ylabel('saturation')
    elif name == 'task17_1' or name=='task17_2':
        ax = plt.axes(xlim=(-1.5, 12), ylim=(1, 0))
        ax.set_ylabel('S = h/H')
    elif name == 'task21':
        ax = plt.axes(xlim=(-1.5, 12), ylim=(1, 0 - x[-1] / X * np.tan(theta)))
        ax.set_ylabel('S = h/H - x/X * tan(theta)')

    ax.grid()
    ax.set_xlabel('x')

    line, = ax.plot(x, s_matrix[0])
    time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

    def init():
        line.set_ydata([np.nan] * len(x))
        time_text.set_text('')
        return line,

    def animate(i):

        index = i * scale_animation_time

        if name=='task21':
            lower = -1 / X * np.tan(theta) * x
            upper = -1 / X * np.tan(theta) * x + 1
            y = s_matrix[index] - x / X * np.tan(theta)
            if i % 20 == 0:
                time_text.set_text('t = ' + str(round(index * k / (3600*24), 2)) + ' days')
        else:
            y = s_matrix[index]
            if i % 20 == 0:
                time_text.set_text('t = ' + str(round(index * k / 3600, 2)) + ' h')

        line.set_ydata(y)


        if name == 'task7':
            return line, time_text,
        elif name == 'task17_1' or name=='task17_2':
            filling_grey = plt.fill_between(x, y, 0, facecolors='silver')
            filling_blue = plt.fill_between(x, y, 1, facecolors='lightblue')
            return line, filling_blue, filling_grey, time_text,
        elif name == 'task21':
            filling_grey = plt.fill_between(x, y, lower, facecolors='silver')
            filling_blue = plt.fill_between(x, y, upper, facecolors='lightblue')
            return line, filling_blue, filling_grey, time_text,

    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval,
                                  blit=True, save_count=timeSteps / scale_animation_time)

    if save_to_gif==True:
        save_animations(ani, "anim_"+name)
    else:
        plt.show()


def plot_report(s_matrix, h, spaceSteps,timeSteps, k, name, theta):
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    if name == 'task7':
        indexes = np.array([0,5000,25000,timeSteps-1])
    elif name == 'task17_1':
        indexes = np.array([0, 10000, 60000, timeSteps - 1])
    elif name == 'task17_2':
        indexes = np.array([0, 8000, 25000, timeSteps - 1])
    elif name == 'task21':
        indexes = np.array([0, 15000, 30000, timeSteps - 1])

    times = np.round(indexes*k/(3600),1)

    for j in range(4):

        y = s_matrix[indexes[j]]

        if name == 'task7':
            axs[j].set_title("t = " + str(times[j]) + " h")
            if j==0:
                axs[j].set_ylabel('Gas saturation s')
        elif name == 'task17_1' or name == 'task17_2':
            axs[j].set_ylim([1,0])
            axs[j].fill_between(x, y, 0, facecolors='silver')
            axs[j].fill_between(x, y, 1, facecolors='lightblue')
            axs[j].set_title("t = " + str(times[j]) + " h")
            if j==0:
                axs[j].set_ylabel('S = h/H')
        elif name == 'task21':
            X = (spaceSteps-1)*h
            y -= 1 / X * np.tan(theta) * x
            axs[j].set_xlim([-1.5, 12])
            axs[j].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(theta)])
            axs[j].fill_between(x, y, -1 / X * np.tan(theta) * x, facecolors='silver')
            axs[j].fill_between(x, y, 1 - 1 / X * np.tan(theta) * x, facecolors='lightblue')
            axs[j].set_title("t = " + str(np.round(times[j] / 24,1)) + " days")
            if j==0:
                axs[j].set_ylabel('S + x/X * tan(theta)')

        axs[j].plot(x, y)
        axs[j].set_xlabel('x')
        axs[j].grid()

    #plt.savefig(name+'.pdf')
    plt.show()



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
    #plt.savefig("num_stability.pdf",transparent=True)
    plt.show()