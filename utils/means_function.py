from dataloader import dateLoad
from log import dataToCSV
import numpy as np


def mean_feature():
    data, labels, feature_names = dateLoad()
    res = []
    for row in range(180):
        res_colum = []
        feature = []
        for colum in range(432):
            feature.append(data[row][colum])
            if (colum + 1) % 48 == 0:
                key = np.mean(feature)
                res_colum.append(key)
                feature = []
                print("计算完成：第{}行 第{}列 第{}列".format(row,colum-47,colum))

        res.append(res_colum)
        res_colum = []

    res_np = np.array(res)

    print("Done！")
    dataToCSV("mean","mean_data.csv",res_np)








mean_feature()