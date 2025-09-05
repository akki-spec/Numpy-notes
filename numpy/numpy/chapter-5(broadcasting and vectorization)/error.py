import numpy as np


arr_2d = np.array([[1,2,3],[4,5,6]])
arr_1d = np.array([10,20])
"""

print(arr_2d + arr_1d) it will give value error because of dimensions"""

print(arr_2d + arr_1d.reshape(2,1))#we have use reshaping first to resolve error



