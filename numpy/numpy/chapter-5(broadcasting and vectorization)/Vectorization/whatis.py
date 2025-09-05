list1 = [1,2,3]
list2 = [4,5,6]

result = [x+y for x,y in zip(list1,list2)]
print(result)

"""above thing is slower for large datasets
    so to solve this problem we use vectorization in numpy"""

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])


print(arr1 + arr2)


"""
broadcasting used for smaller to bigger and faster than loops

vectorisation usen for entire array and 100 times faster than loops ,mainly used in matrix operations"""