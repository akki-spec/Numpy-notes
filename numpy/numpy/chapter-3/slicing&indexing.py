"""
Array[index] for 1d

Array[row,coloumn] for 2d
"""
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[-1])

"""Slicing
Array[start,step,stop]
"""

print(arr[1:5])# index 1 to 4
print(arr[:4])# index 0 to 3
print(arr[::2])#every second element
print(arr[::-1])#reverse


