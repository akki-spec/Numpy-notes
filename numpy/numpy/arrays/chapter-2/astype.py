#used to convert data type of any array
import numpy as np
arr = np.array([1.2,2.4,3.6,4.8])
print(arr.dtype)

arr_int = arr.astype(int)
print(arr_int)
print(arr_int.dtype)
