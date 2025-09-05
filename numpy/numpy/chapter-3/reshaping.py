"""reshape(rows,coloumn)
does not change number fo elements

does not create copy

used to convert 1d into 2d or 3d array
                2d into 3d array
"""
import numpy as np
arr = np.array([1,2,3,4,5,6])

reshape_arr = arr.reshape(2,3)
print(reshape_arr)