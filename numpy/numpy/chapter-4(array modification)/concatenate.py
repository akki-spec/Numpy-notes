"""
np.concatenate((array1,array2),axis)

axis = 0 > vertical stacking (row addition)
axis = 1 > horizontal stacking (coloumn addition)
"""
import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr2 = np.concatenate((arr1,arr2),axis=1)
print(arr2)