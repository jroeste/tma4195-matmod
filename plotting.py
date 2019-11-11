import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotting_7(s_matrix, spaceSteps, timeSteps, interval, h, k):

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

    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps)

    plt.show()

def plotting_17(s_matrix, spaceSteps, timeSteps, interval, h, k):

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

    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps)

    plt.show()

def plotting_21(s_matrix, spaceSteps, timeSteps, interval, h, k, theta):

    fig, ax = plt.subplots()
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    ax = plt.axes(xlim=(-1.5,12),ylim=(1, 0-1/10*x[-1]*np.tan(theta)))
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
        lower = -1/10*np.tan(theta)*x
        upper = -1/10*np.tan(theta)*x + 1
        y = s_matrix[i*100] - 1/10*np.tan(theta)*x
        line.set_ydata(y)
        if i % 100 == 0:
            time_text.set_text('t = ' + str(round(i * k, 2)))
        filling_grey = plt.fill_between(x, y, lower, facecolors='silver')
        filling_blue = plt.fill_between(x, y, upper, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps/100)

    plt.show()

def plot_report_7(s_matrix, h, spaceSteps, name):
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)

    axs[0].plot(x, s_matrix[0])
    axs[0].set_title("t = 0 s")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Gas saturation s')
    axs[1].plot(x, s_matrix[2000])
    axs[1].set_title("t = 2 s")
    axs[1].set_xlabel('x')
    axs[2].plot(x, s_matrix[10000])
    axs[2].set_title("t = 10 s")
    axs[2].set_xlabel('x')
    axs[3].plot(x, s_matrix[-1])
    axs[3].set_title("t = 50 s")
    axs[3].set_xlabel('x')

    #plt.savefig(name)
    plt.show()


def plot_report_17(s_matrix, h, spaceSteps, name):
    x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
    fig, axs = plt.subplots(1, 4, figsize=(12, 4), sharey=True)
    axs[0].set_ylim([1, 0])
    axs[0].plot(x, s_matrix[0])
    axs[0].fill_between(x, s_matrix[0], 0, facecolors='silver')
    axs[0].fill_between(x, s_matrix[0], 1, facecolors='lightblue')
    axs[0].set_title("t = 0 s")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('S = h/H')
    axs[1].set_ylim([1, 0])
    axs[1].plot(x, s_matrix[2000])
    axs[1].fill_between(x, s_matrix[2000], 0, facecolors='silver')
    axs[1].fill_between(x, s_matrix[2000], 1, facecolors='lightblue')
    axs[1].set_title("t = 2 s")
    axs[1].set_xlabel('x')
    axs[2].set_ylim([1, 0])
    axs[2].plot(x, s_matrix[10000])
    axs[2].fill_between(x, s_matrix[10000], 0, facecolors='silver')
    axs[2].fill_between(x, s_matrix[10000], 1, facecolors='lightblue')
    axs[2].set_title("t = 10 s")
    axs[2].set_xlabel('x')
    axs[3].set_ylim([1, 0])
    axs[3].plot(x, s_matrix[-1])
    axs[3].fill_between(x, s_matrix[-1], 0, facecolors='silver')
    axs[3].fill_between(x, s_matrix[-1], 1, facecolors='lightblue')
    axs[3].set_title("t = 50 s")
    axs[3].set_xlabel('x')


    plt.savefig(name)
    #plt.show()

# def plotting_21(s_matrix, spaceSteps, timeSteps, interval, h, k):
#
#     fig, ax = plt.subplots()
#     x = np.linspace(0, h * (spaceSteps - 1), spaceSteps)
#     ax = plt.axes(ylim=(1, 0))
#     ax.set_xlabel('x')
#     ax.set_ylabel('saturation')
#     line, = ax.plot(x, s_matrix[0])
#     time_text = ax.text(0.8, 0.8, '', transform=ax.transAxes)
#
#     def init():  # give a clean slate to start
#         line.set_ydata([np.nan] * len(x))
#         time_text.set_text('')
#         return line,
#
#     def animate(i):
#         y = s_matrix[i]
#         line.set_ydata(y)
#         if i % 100 == 0:
#             time_text.set_text('t = ' + str(round(i * k, 2)))
#         filling_grey = plt.fill_between(x, y, 0, facecolors='silver')
#         filling_blue = plt.fill_between(x, y, 1, facecolors='lightblue')
#         return line, filling_blue, filling_grey, time_text,
#
#     ani = animation.FuncAnimation(fig, animate, init_func=init, interval=interval, blit=True, save_count=timeSteps)
#
#     plt.show()