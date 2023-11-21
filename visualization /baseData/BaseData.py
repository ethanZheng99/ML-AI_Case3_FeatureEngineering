import numpy as np
from matplotlib import pylab as plt
from utils import dataloader

x, y, feature_names = dataloader.dateLoad()


# visualization for alpha_ac
def alpha_ac(colum: int):
    print(x[colum])
    print(len(x[colum]))  # 432


alpha_ac(0)
