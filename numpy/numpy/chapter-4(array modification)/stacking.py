"""its like concatenate
vertically 
horizontally
np.vstack #row wise 
np.hstack #coloumn wise
"""
import numpy as np
arr1 = np.array([1,3,45,6])
arr2 = np.array([10,3,6,9])

arr3 = np.vstack(((arr1,arr2)))
arr4 = np.hstack(((arr1,arr2)))
print(arr3)
print(arr4)
