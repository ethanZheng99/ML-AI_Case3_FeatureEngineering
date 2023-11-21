import random
import numpy as np
from matplotlib import pylab as plt
from utils import dataloader
import os

x, y, feature_names = dataloader.dateLoad()
system = os.name


# visualization for alpha_ac
def alpha_ac(colum: int):
    Y = x[colum][0:48]
    X = range(48)
    plt.plot(X,Y,label="Original")
    key = np.mean(Y)
    print(key)
    Y1 = np.full(48,key)
    plt.plot(X,Y1,label="Mean")
    plt.show()


def alpha_ac_Random(columList: list):
    if len(columList) == 3:

        fig, axes = plt.subplots(1, 3, figsize=(24, 6))

        X = range(48)
        yList = []
        y_mean_List = []
        (label1, label2, label3) = (lambda x: x)(columList)

        for index in columList:
            Y = x[index][0:48].tolist()
            key = np.mean(Y)
            Y1 = np.full(48, key)
            yList.append(Y)
            y_mean_List.append(Y1)

        fig.suptitle('Means Function')
        for ax in axes.flat:
            ax.set(xlabel='electrodes', ylabel='normalized alpha band power')

            # 统一设置 y 轴的刻度范围为 0 到 1.5
            ax.set_ylim(0, 1.5)

        axes[0].plot(X,yList[0],label=str(label1) + " raw")
        axes[0].plot(X,y_mean_List[0], label=str(label1) + " mean")
        axes[0].legend()
        axes[0].set_title('Raw Data ' + str(label1))

        axes[1].plot(X, yList[1], label=str(label2) + " raw")
        axes[1].plot(X, y_mean_List[1], label=str(label2) + " mean")
        axes[1].legend()
        axes[1].set_title('Raw Data ' + str(label2))

        axes[2].plot(X, yList[2], label=str(label3) + " raw")
        axes[2].plot(X, y_mean_List[2], label=str(label3) + " mean")
        axes[2].legend()
        axes[2].set_title('Raw Data ' + str(label3))

        plt.show()


def alpha_ac_Random_Iter(maxNumber: int):
    for page in range(maxNumber):
        columList = []
        for i in range(3):
            columList.append(random.randint(0, 179))
        if len(columList) == 3:
            fig, axes = plt.subplots(1, 3, figsize=(24, 6))

            X = range(48)
            yList = []
            y_mean_List = []
            (label1, label2, label3) = (lambda x: x)(columList)

            for index in columList:
                Y = x[index][0:48].tolist()
                key = np.mean(Y)
                Y1 = np.full(48, key)
                yList.append(Y)
                y_mean_List.append(Y1)

            fig.suptitle('Means Function')
            for ax in axes.flat:
                ax.set(xlabel='electrodes', ylabel='normalized alpha band power')

                # 统一设置 y 轴的刻度范围为 0 到 1.5
                ax.set_ylim(0, 1.5)

            axes[0].plot(X, yList[0], label=str(label1) + " raw")
            axes[0].plot(X, y_mean_List[0], label=str(label1) + " mean")
            axes[0].legend()
            axes[0].set_title('Raw Data ' + str(label1))

            axes[1].plot(X, yList[1], label=str(label2) + " raw")
            axes[1].plot(X, y_mean_List[1], label=str(label2) + " mean")
            axes[1].legend()
            axes[1].set_title('Raw Data ' + str(label2))

            axes[2].plot(X, yList[2], label=str(label3) + " raw")
            axes[2].plot(X, y_mean_List[2], label=str(label3) + " mean")
            axes[2].legend()
            axes[2].set_title('Raw Data ' + str(label3))

            filename = "mean_log_" + str(page) + ".png"
            if system == 'nt':
                url = "log_img//" + filename
            else:
                url = "log_img/" + filename

            print("已成功输出：" +url)
            plt.savefig(url)


alpha_ac_Random_Iter(8)
#alpha_ac(12)
"""
randomList = []
for i in range(3):
    randomList.append(random.randint(0,180))

alpha_ac_Random(randomList)

"""
