import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
        y = s_matrix[200*i]
        line.set_ydata(y)
        time_text.set_text('t = ' + str(round(200*i * k, 2)))
        return line, time_text,

    if save_to_gif=="slow":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif_slow, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps/10)
        save_animations(ani_to_gif, "anim_task7_slow")

    elif save_to_gif=="fast":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif_fast, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps / 200)
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
        scalar = 10
        y = s_matrix[i*scalar]
        line.set_ydata(y)
        if i*scalar % 100 == 0:
            time_text.set_text('t = ' + str(round(scalar*i * k, 2)))
        filling_grey = plt.fill_between(x, y, 0, facecolors='silver')
        filling_blue = plt.fill_between(x, y, 1, facecolors='lightblue')
        return line, filling_blue, filling_grey, time_text,

    if save_to_gif=="slow":
        ani_to_gif = animation.FuncAnimation(fig, animate_to_gif, init_func=init, interval=interval, blit=True,
                                             save_count=timeSteps/10)
        save_animations(ani_to_gif, "anim_task17")
    else:
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