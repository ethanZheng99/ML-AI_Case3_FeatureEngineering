import numpy as np
from log import dataToCSV
from utils import dataloader
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

data, labels, feature_name = dataloader.dateLoad()


def chi_Squared_mean():
    transformed_data = np.zeros((180, 9))
    for i in range(9):
        start = i * 48
        end = start + 48
        # computing mean in data
        transformed_data[:, i] = np.mean(data[:, start:end], axis=1)

    selector = SelectKBest(chi2, k=9)  # k=9 select 9 features
    X_kbest = selector.fit_transform(transformed_data, labels)

    dataToCSV("chi-squared", "chi-squared_mean.csv", X_kbest)
    print("done!")


# original chi_squared
def chi_Squared():
    selector = SelectKBest(chi2, k=9)  # k=9 选择9个特征
    X_kbest = selector.fit_transform(data, labels)

    print(X_kbest)


def chi_Squared_std():
    transformed_data = np.zeros((180, 9))
    for i in range(9):
        start = i * 48
        end = start + 48
        # computing mean in data
        transformed_data[:, i] = np.std(data[:, start:end], axis=1)

    selector = SelectKBest(chi2, k=9)  # k=9 select 9 features
    X_kbest = selector.fit_transform(transformed_data, labels)

    dataToCSV("chi-squared", "chi-squared_std.csv", X_kbest)
    print("done!")


def chi_Squared_max():
    transformed_data = np.zeros((180, 9))
    for i in range(9):
        start = i * 48
        end = start + 48
        # computing mean in data
        transformed_data[:, i] = np.max(data[:, start:end], axis=1)

    selector = SelectKBest(chi2, k=9)  # k=9 select 9 features
    X_kbest = selector.fit_transform(transformed_data, labels)

    print(X_kbest)
    dataToCSV("chi-squared", "chi-squared_max.csv", X_kbest)
    print("done!")


chi_Squared_max()
