import numpy as np
import random
from utils import dataloader
from matplotlib import pylab as plt
import os

system = os.name
data_mean, labels, _ = dataloader.normal_dataLoad("chi-squared", 'chi-squared_mean.csv')
data_max, _, _ = dataloader.normal_dataLoad("chi-squared", 'chi-squared_max.csv')
data_std, _, _ = dataloader.normal_dataLoad("chi-squared", 'chi-squared_std.csv')
data, _, _ = dataloader.dateLoad()
feature_name = ['alpha_ec', "beta_ec", "theta_ec", "alpha_eo", "beta_eo", "theta_eo", "alpha_eo/ec", "beta_eo/ec",
                "theta_eo/ec"]


def visualization_chi_squared_max():
    columList = []
    for i in range(6):
        if i < 3:
            columList.append(random.randint(0, 100))
        if i >= 3:
            columList.append(random.randint(101, 179))

    for row in columList:
        Y = []
        X = range(48)
        for i in range(9):
            start = i * 48
            end = start + 48
            # computing mean in data
            Y.append(data[row, start:end])

        # Y initial
        Y1 = data_max[row, :]
        Y0 = np.array(Y)

        fig, axes = plt.subplots(1, 9, figsize=(34, 6))
        fig.suptitle('Chi-Squared Max Function in: ' + str(row + 1))
        for i, ax in enumerate(axes.flat):
            # 为每个子图设置 x 轴和 y 轴标签
            ax.set(xlabel='electrodes', ylabel='value')

            # 根据子图的索引设置不同的 y 轴范围
            # 前 6 个子图的索引是 0 到 5
            if i < 6:
                ax.set_ylim(0, 3)
            else:
                ax.set_ylim(0, 15)

        for index in range(9):
            axes[index].plot(X, Y0[index], label=str(row + 1) + " raw")
            axes[index].plot(X, np.full(48, Y1[index]), label=str(row + 1) + " C-S-Max")
            axes[index].legend()
            axes[index].set_title(feature_name[index])

        filename = "Chi-squared_max_log_" + str(row + 1) + ".png"
        if system == 'nt':
            url = "log_img//" + filename
        else:
            url = "log_img/" + filename

        print("已成功输出：" + url)
        plt.savefig(url)

        Y = []


def visualization_chi_squared_mean():
    columList = []
    for i in range(6):
        if i < 3:
            columList.append(random.randint(0, 100))
        if i >= 3:
            columList.append(random.randint(101, 179))

    for row in columList:
        Y = []
        X = range(48)
        for i in range(9):
            start = i * 48
            end = start + 48
            # computing mean in data
            Y.append(data[row, start:end])

        # Y initial
        Y1 = data_mean[row, :]
        Y0 = np.array(Y)

        fig, axes = plt.subplots(1, 9, figsize=(34, 6))
        fig.suptitle('Chi-Squared Mean Function in: ' + str(row + 1))
        for i, ax in enumerate(axes.flat):
            # 为每个子图设置 x 轴和 y 轴标签
            ax.set(xlabel='electrodes', ylabel='value')

            # 根据子图的索引设置不同的 y 轴范围
            # 前 6 个子图的索引是 0 到 5
            if i < 6:
                ax.set_ylim(0, 3)
            else:
                ax.set_ylim(0, 15)

        for index in range(9):
            axes[index].plot(X, Y0[index], label=str(row + 1) + " raw")
            axes[index].plot(X, np.full(48, Y1[index]), label=str(row + 1) + " C-S-Mean")
            axes[index].legend()
            axes[index].set_title(feature_name[index])

        filename = "Chi-squared_mean_log_" + str(row + 1) + ".png"
        if system == 'nt':
            url = "log_img//" + filename
        else:
            url = "log_img/" + filename

        print("已成功输出：" + url)
        plt.savefig(url)

        Y = []
def visualization_chi_squared_std():
    columList = []
    for i in range(6):
        if i < 3:
            columList.append(random.randint(0, 100))
        if i >= 3:
            columList.append(random.randint(101, 179))

    for row in columList:
        Y = []
        X = range(48)
        for i in range(9):
            start = i * 48
            end = start + 48
            # computing mean in data
            Y.append(data[row, start:end])

        # Y initial
        Y1 = data_std[row, :]
        Y0 = np.array(Y)

        fig, axes = plt.subplots(1, 9, figsize=(34, 6))
        fig.suptitle('Chi-Squared STD Function in: ' + str(row + 1))
        for i, ax in enumerate(axes.flat):
            # 为每个子图设置 x 轴和 y 轴标签
            ax.set(xlabel='electrodes', ylabel='value')

            # 根据子图的索引设置不同的 y 轴范围
            # 前 6 个子图的索引是 0 到 5
            if i < 6:
                ax.set_ylim(0, 3)
            else:
                ax.set_ylim(0, 15)

        for index in range(9):
            axes[index].plot(X, Y0[index], label=str(row + 1) + " raw")
            axes[index].plot(X, np.full(48, Y1[index]), label=str(row + 1) + " C-S-std")
            axes[index].legend()
            axes[index].set_title(feature_name[index])

        filename = "Chi-squared_std_log_" + str(row + 1) + ".png"
        if system == 'nt':
            url = "log_img//" + filename
        else:
            url = "log_img/" + filename

        print("已成功输出：" + url)
        plt.savefig(url)

        Y = []


#visualization_chi_squared_max()
#visualization_chi_squared_mean()
visualization_chi_squared_std()
