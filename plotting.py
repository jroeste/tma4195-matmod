import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import os

# This has some issues, saving animation to gif will probably not work
def save_animations(anim_object,filename):
    FFwriter = animation.FFMpegWriter()
    #path = "C:\\Users\julie\Downloads\\"+filename
    path = "C:\\Users\jnols\Downloads\\"+filename
    anim_object.save(path+".mp4", writer='ffmpeg', fps=30)
    os.system("ffmpeg -i "+path+".mp4 "+path+".gif")

# Plots animation
def plot_animation(s_matrix, spaceSteps, timeSteps, interval, h, k, name, scale_animation_time, save_to_gif = False, **extra_parameters):

    # Set figure and x-values
    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    X = (spaceSteps-1)*h

    # Set axes and labels
    if name == 'task7':
        ax = plt.axes(ylim=(0, 1))
        ax.set_ylabel('saturation')
    elif name == 'task17_1' or name=='task17_2':
        ax = plt.axes(xlim=(-1.5, 12), ylim=(1, 0))
        ax.set_ylabel('S = h/H')
    elif name == 'task21':
        ax = plt.axes(xlim=(-1.5, 12), ylim=(1, 0 - x[-1] / X * np.tan(extra_parameters['theta'])))
        ax.set_ylabel('S = h/H - x/X * tan(theta)')

    ax.grid()
    ax.set_xlabel('x')

    # Define line and time in animation
    line, = ax.plot(x, s_matrix[0])
    time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)

    # Initialization of animation
    def init():
        line.set_ydata([np.nan] * len(x))
        time_text.set_text('')
        return line,

    # Updates animation in a loop-like fashion
    def animate(i):

        # scale_animation_time increases animation speed
        index = i * scale_animation_time

        # Add tilt in 21, and updates time text and line values
        if name=='task21':
            lower = -1 / X * np.tan(extra_parameters['theta']) * x
            upper = -1 / X * np.tan(extra_parameters['theta']) * x + 1
            y = s_matrix[index] - x / X * np.tan(extra_parameters['theta'])
            if i % 20 == 0:
                time_text.set_text('t = ' + str(round(index * k / (3600*24), 2)) + ' days')
        else:
            y = s_matrix[index]
            if i % 20 == 0:
                time_text.set_text('t = ' + str(round(index * k / 3600, 2)) + ' h')

        line.set_ydata(y)

        # Adds fill areas to appropriate plots
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

    # Run animation
    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval,
                                  blit=True, save_count=timeSteps / scale_animation_time)

    # Save to gif (currently not working) or show plot
    if save_to_gif==True:
        save_animations(ani, "anim_"+name)
    else:
        plt.show()

# Plots 4 plots at different times, as in the report
def plot_report(s_matrix, h, spaceSteps,timeSteps, k, name, **extra_parameters):

    # Set figure and x-values
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    # Defines at which time (by index) the different plots should be plotted
    if name == 'task7':
        indexes = np.array([0,5000,25000,timeSteps-1])
    elif name == 'task17_1':
        indexes = np.array([0, 10000, 60000, timeSteps - 1])
    elif name == 'task17_2':
        indexes = np.array([0, 8000, 25000, timeSteps - 1])
    elif name == 'task21':
        indexes = np.array([0, 15000, 30000, timeSteps - 1])

    # Set time for each plot
    times = np.round(indexes*k/(3600),1)

    # For each plot
    for j in range(4):

        # Set y-value
        y = s_matrix[indexes[j]]

        # Add title (timestamp), y-label, defines axes and makes fill colors to the appropriate plots
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

            # X is max(x), used to make dimensionless x-axis.
            X = (spaceSteps-1)*h

            # Subtracts dimensionless theta-slope to all values
            y -= x / X * np.tan(extra_parameters['theta'])
            axs[j].set_xlim([-1.5, 12])
            axs[j].set_ylim([1, 0 - 1 / 10 * x[-1] * np.tan(extra_parameters['theta'])])
            axs[j].fill_between(x, y, - x / X * np.tan(extra_parameters['theta']), facecolors='silver')
            axs[j].fill_between(x, y, 1 - x / X * np.tan(extra_parameters['theta']), facecolors='lightblue')
            axs[j].set_title("t = " + str(np.round(times[j] / 24,1)) + " days")
            if j==0:
                axs[j].set_ylabel('S + x/X * tan(theta)')

        # Plots line and labels
        axs[j].plot(x, y)
        axs[j].set_xlabel('x')
        axs[j].grid()

    #plt.savefig(name+'.pdf')
    plt.show()


# This makes plots used to justify numerical scheme
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