import glob
import os
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D


def get_all_files(folder):
    files = glob.glob(folder + "*_locations.csv")
    return files


def graph(files):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    x = []
    y = []
    z = []
    df = pd.DataFrame(
        columns=["label", "PCL Intersection", "Mesh Intersection", "image", "location"]
    )
    for file in files:
        # with open(file, "r") as f:
        #     for line in f:
        #         if "PCL Intersection" in line:
        #             nums = re.findall(
        #                 r"[-+]?\d*\.\d+|\d+", line
        #             )  # [x, y, z, roll, pitch, yaw]
        #             x.append(float(nums[0]))
        #             y.append(float(nums[1]))
        #             z.append(float(nums[2]))
        # data = np.genfromtxt(file, delimiter=';', dtype=str, missing_values=None)
        # print("Line 900:", data[899])
        df2 = pd.read_csv(file, delimiter=";", skiprows=[1])
        df = pd.concat([df, df2])
        # with open(file, 'r') as f:
        #     lines = f.readlines()'

        # # Print line 900
        # print("Line 900:", lines[899])
    print(df)
    for row in df["PCL Intersection"].tolist():
        nums = re.findall(r"[-+]?\d*\.\d+|\d+", row)
        x.append(float(nums[0]))
        y.append(float(nums[1]))
        z.append(float(nums[2]))
    #     nums = data[:, 1]
    #     nums = [re.findall(r"[-+]?\d*\.\d+|\d+", i) for i in nums]
    #     for i in nums:
    #         x.append(float(i[0]))
    #         y.append(float(i[1]))
    #         z.append(float(i[2]))

    ax.scatter(x, y, z)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.title("Label Locations on ISS")

    plt.show()
    # return plt


if __name__ == "__main__":
    # files = get_all_files(os.getcwd())
    # plt = graph(files)
    # plt.show()
    files = [os.path.join(os.getcwd(), "all_locations.csv")]
    graph(files)
