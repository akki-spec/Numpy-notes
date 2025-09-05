#nan_to_num(arr,nan = value) | default nan = 0
import numpy as np

arr = np.array([1,2,np.nan ,3,4, np.nan])
arr = np.nan_to_num(arr,nan =  7)
print(arr)
