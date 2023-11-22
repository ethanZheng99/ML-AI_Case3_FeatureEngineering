from dataloader import dateLoad
import numpy as np
import dcor
from log import dataToCSV

data, labels, feature_name = dateLoad()
transformed_data = np.zeros((180, 9))

def dCor_mean():
    for i in range(9):
        start_col = i * 48
        end_col = start_col + 48
        transformed_data[:, i] = np.mean(data[:, start_col:end_col], axis=1)
    dcor_values = [dcor.distance_correlation(transformed_data[:, i], labels) for i in range(9)]
    selected_indices = np.argsort(dcor_values)[-9:]  # 选择9个特征
    selected_features = transformed_data[:, selected_indices]
    dataToCSV("dCor", "dCor_mean.csv", selected_features)
    print("dCor mean Done")

def dCor_std():
    for i in range(9):
        start_col = i * 48
        end_col = start_col + 48
        transformed_data[:, i] = np.std(data[:, start_col:end_col], axis=1)
    dcor_values = [dcor.distance_correlation(transformed_data[:, i], labels) for i in range(9)]
    selected_indices = np.argsort(dcor_values)[-9:]  # 选择9个特征
    selected_features = transformed_data[:, selected_indices]
    dataToCSV("dCor", "dCor_std.csv", selected_features)
    print("dCor std Done")
def dCor_max():
    for i in range(9):
        start_col = i * 48
        end_col = start_col + 48
        transformed_data[:, i] = np.max(data[:, start_col:end_col], axis=1)
    dcor_values = [dcor.distance_correlation(transformed_data[:, i], labels) for i in range(9)]
    selected_indices = np.argsort(dcor_values)[-9:]  # 选择9个特征
    selected_features = transformed_data[:, selected_indices]
    dataToCSV("dCor", "dCor_max.csv", selected_features)
    print("dCor max Done")


dCor_mean()
dCor_std()
dCor_max()
