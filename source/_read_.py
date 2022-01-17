import os
import json
import pickle
import pandas as pd
import ast

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

filename = "pymmw_2022-01-13_15-31-38"
path = os.getcwd()
filename = os.path.join(path, 'log', filename)



def read_json(filename):
    try:
        with open(filename + '.json', 'r') as openfile:
            json_object = json.load(openfile)
            return json_object
    except Exception as e:
        print(f"Reading file unsuccessful.: {e}")

def read_pickle(filename):
    try:
        with open(filename + '.log', 'r') as openfile:
            pickle_object = pickle.load(openfile)
            return pickle_object
    except Exception as e:
        print(e)

def read_log(filename):
    try:
        with open(filename + '.log', 'rt') as openfile:
            datastring = openfile.read()
            datalist = [d.strip() for d in datastring.splitlines()]
            datadict = []
            for item in datalist:
                datadict.append(ast.literal_eval(item))
                # print(f"==========={len(datalist)}")
        return datadict
    except Exception as e:
        print(f"Exception occured: {e}")


    
def plot_range(datadict=None):
    if datadict==None:
        datadict = read_log(filename)
    def animator(frame):
        frame_dict = datadict[frame]
        d = frame_dict['dataFrame']['range_profile']
        f = frame_dict['dataFrame']['noise_profile']
        ax.clear()
        ax.set_xlim(0, 360)
        ax.set_ylim(0, 70)
        ax.plot(d)
        ax.plot(f)
        ax.set_xlabel("range index")
        ax.set_ylabel("range profile")
        ax.set_title(f"Range Profile data, frame: {frame}")
        ax.grid()
        ax.legend(["range_profile", "noise_profile"])
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animator, frames=255, interval=500, repeat=True)
    plt.show()

if __name__ == '__main__':
    datadict = read_log(filename)
    plot_range(datadict)