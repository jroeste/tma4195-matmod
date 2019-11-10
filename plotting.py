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