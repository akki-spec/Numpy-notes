# 1 - size
import numpy as np

arr = np.array([[1,2,3],
                  [4,5,6]])
print(arr.shape)# here (2,3) means 2 rows and 3 coloumns

#2 - size 
print(arr.size)#no. of element

#3 - no. of dimensions (ndim)
arr_1d = np.array([1,2])
arr_2d = np.array([[1,2],[3,4]])
arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(arr_1d.ndim)# 1 = 1D in output
print(arr_2d.ndim)# 2 = 2D in output
print(arr_3d.ndim)# 3 = 3D in output


