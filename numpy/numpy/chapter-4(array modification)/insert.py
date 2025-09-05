"""ADD at specific position
np.insert(arr,index,value,axis)
axis=0 #row
axis=1 #coloumn
"""

import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)

new_arr = np.insert(arr,2,90)
print(new_arr)

#for 2d array
arr2 = np.array([[1,2],[3,4]])
print(arr2)
new_arr2 = np.insert(arr2,1,[4,5],axis=1)
print(new_arr2)