import os
from _read_ import *
import numpy as np 
from matplotlib.animation import FuncAnimation

filename = "pymmw_2022-01-13_15-37-54"
path = os.getcwd()
filename = os.path.join(path, 'log', filename)

datadict = read_log(filename)

# for frame in range(len(datadict)):
#     try:
#         print(len(datadict[frame]['dataFrame']['range_doppler']))
#     except Exception as KeyError:
#         print(f"{datadict[frame]['dataFrame'].keys()}")

def animate(frame):
    try:
        range_doppler = np.array(datadict[frame]['dataFrame']['range_doppler'])
        # print(len(datadict[frame]['dataFrame']['range_doppler']))
        ax.clear()
        ax.set_title(f"frame: {frame}")
        ax.imshow(range_doppler.reshape(64, 64))
        

    except Exception as KeyError:
        print(f"key range_doppler not in frame {frame}")

nframes = len(datadict)
fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate, frames = nframes, interval=200, repeat=True)
plt.show()