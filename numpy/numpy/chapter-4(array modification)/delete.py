"""
np.delete(arr,index,axis=none)
axis = none (flatten array/1d array)
"""
import numpy as np
arr = np.array([[1,2],[3,4]])
arr1 = np.delete(arr,2,axis=None)#if we use arr here it will make it 1d array
print(arr1)
arr = np.delete(arr,0,axis=0)
print(arr)