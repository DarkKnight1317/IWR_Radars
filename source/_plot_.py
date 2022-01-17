import os
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import numpy as np

from _read_ import *

filename = "pymmw_2022-01-13_15-31-38"

class PlotGraph():
    def __init__(self, filename=""):
        if filename == None:
            raise Exception("Filename not provided")
        self.filename = os.path.join(os.getcwd(), 'log', filename)
        self.datadict = read_log(self.filename)
        self.nframes = len(self.datadict)

    def plot_range(self):
        print(f"Plotting Range from collected data...")
        def animate(frame):
            frame_dict = self.datadict[frame]
            range_profile = frame_dict['dataFrame']['range_profile']
            noise_profile = frame_dict['dataFrame']['noise_profile']
            ax.clear()
            ax.set_xlim(0, 256)
            ax.set_ylim(0, 70)
            ax.plot(range_profile)
            ax.plot(noise_profile)
            ax.set_xlabel("range index")
            ax.set_ylabel("range profile")
            ax.set_title(f"Range Profile data, frame: {frame}")
            ax.grid()
            ax.legend(["range_profile", "noise_profile"])
        fig, ax = plt.subplots()
        ani = FuncAnimation(fig, animate, frames=self.nframes, interval=200, repeat=True)
        plt.show()

    def plot_range_doppler(self, datadict=None):
        print(f"Plotting Range Doppler Heatmap from colected data...")
        def animate(frame):
            frame_dict = self.datadict[frame]
            range_doppler = frame_dict['dataFrame']['range_doppler']
            ax.clear()
            ax.imshow(np.array(range_doppler).reshape(20, -1))
            ax.set_xlabel("range velocity")
            # ax.set_ylabel("range profile")
            ax.set_title(f"Range Doppler Heatmap, frame: {frame}")
            ax.grid()
            # ax.legend(["range_profile", "noise_profile"])
        fig, ax = plt.subplots()
        ani = FuncAnimation(fig, animate, frames=self.nframes, interval=200, repeat=True)
        plt.show()






if __name__ == '__main__':
    plotter = PlotGraph(filename)
    plotter.plot_range()
