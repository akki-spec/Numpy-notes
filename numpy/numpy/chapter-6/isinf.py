'''np.isinf(arr) to check for infinite numbers like 10**1000 , 1/0 
used to detect infinite values
'''
import numpy as np

arr = np.array([1,2,np.inf,3,4, -np.inf])
print(np.isinf(arr))#to check

"""then posinf for positive infinity and neginf for negative infinity"""

arr = np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(arr)

