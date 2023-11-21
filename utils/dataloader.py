import csv
import numpy as np
from matplotlib import pylab as plt


def dateLoad():
    x = np.loadtxt('../data/data.csv', delimiter=',')
    y = np.loadtxt('../data/labels.csv', delimiter=',')
    with open('../data/feature_names.csv') as f:
        csvreader = csv.reader(f, delimiter=',')
        feature_names = [row for row in csvreader][0]
    return x, y, feature_names


def samplePlot():
    X, y, feature_names = dateLoad()
    # plotting data in 2D with axes sampled
    # a) at random
    # b) from same electrode
    # c) from same feature type
    num_features = 9
    num_electrodes = 48

    # a) indices drawn at random
    i0, i1 = np.random.randint(0, X.shape[1], size=2)

    # b) same electrode, different feature (uncomment lines below)
    # f0, f1 = np.random.randint(0, num_features, size=2)
    # e = np.random.randint(0, num_electrodes)
    # i0, i1 = f0*num_electrodes + e, f1*num_electrodes + e

    # c) same feature, different electrode (uncomment lines below)
    # f = np.random.randint(0, num_features)
    # e0, e1 = np.random.randint(0, num_electrodes, size=2)
    # i0, i1 = f*num_electrodes + e0, f*num_electrodes + e1

    fig, axes = plt.subplots(1, 3, figsize=(24, 6))
    colors = ['blue', 'red']

    # select features i0, i1 and separate by class
    X00, X01 = X[y == 0][:, i0], X[y == 1][:, i0]
    X10, X11 = X[y == 0][:, i1], X[y == 1][:, i1]
    # plot cumulative distribution of feature i0 separate for each class
    axes[0].hist(X00, bins=20, label='y=0, ' + feature_names[i0], density=True, alpha=0.5)
    axes[0].hist(X01, bins=20, label='y=1, ' + feature_names[i0], density=True, alpha=0.5)
    axes[0].hist(X10, bins=20, label='y=0, ' + feature_names[i1], density=True, alpha=0.5)
    axes[0].hist(X11, bins=20, label='y=1, ' + feature_names[i1], density=True, alpha=0.5)
    axes[0].set_title('histograms')
    axes[0].legend()
    axes[1].plot(np.sort(X00), np.linspace(0, 1, X00.shape[0]), label='y=0, ' + feature_names[i0], alpha=0.5)
    axes[1].plot(np.sort(X01), np.linspace(0, 1, X01.shape[0]), label='y=1, ' + feature_names[i0], alpha=0.5)
    axes[1].plot(np.sort(X10), np.linspace(0, 1, X10.shape[0]), label='y=0, ' + feature_names[i1], alpha=0.5)
    axes[1].plot(np.sort(X11), np.linspace(0, 1, X11.shape[0]), label='y=1, ' + feature_names[i1], alpha=0.5)
    axes[1].set_title('empirical cumulative distribution functions')
    axes[1].legend()
    axes[2].scatter(X00, X10, label='y=0')
    axes[2].scatter(X01, X11, label='y=1')
    axes[2].set_xlabel(feature_names[i0])
    axes[2].set_ylabel(feature_names[i1])
    axes[2].set_title('scatter plot')
    axes[2].legend()

    plt.show()


def check_name_List():
    x, y, feature_names = dateLoad()
    count = 0
    res = "alpha_ec_0" + "\t"
    resList = []
    for i in range(1, len(feature_names)):
        res += feature_names[i] + "\t"
        if (i + 1) % 48 == 0 and i != 0:
            resList.append(res)
            res = ""
            print("from " + str(count) + "->" + str(i))
            count = i + 1
    for i in resList:
        print(i)


# check_name_List()
# samplePlot()
