import numpy as np
arr = np.array([1,2,3,4,5])

print(arr)

#matrix(2d array) and assigning zero in start
#np.zeroes(shape) (3) for 1d, (3,3) for 2d

arr2 = np.zeros((3, 4))
print(arr2)

#if want to give one instead of zero
arr3 = np.ones((3,4))
print(arr3)

#if i want to give random number in matrix like 7
#use np.full()

arr4 = np.full((3,4),7)
print(arr4)