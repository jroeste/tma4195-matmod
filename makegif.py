import imageio
import os


moviepath = "storage/images/movies"
images = []
filenames = os.listdir(path)
filenames.sort()
for filename in filenames:
    if filename.endswith(".png"):
        images.append(imageio.imread(path + "/" + filename))
imageio.mimsave(moviepath + '/' + run_id + '.png', images, format='GIF', duration=0.5)