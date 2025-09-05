"""
Create a 1D NumPy array of numbers 1 to 10 and print:

Shape of the array

Size of the array

Data type of the array"""

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.shape)
print(arr.size)
print(arr.dtype)

print("_________________________________________________________________________________________________")

"""
Create a 3×3 NumPy array of random integers and print:

Number of dimensions

Shape

Total elements count"""

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)

print("_____________________________________________________________________________________________________________")
#aggregation function
"""Create an array [3, 5, 7, 9, 11] and find:

Sum of all elements

Maximum value

Minimum value

Mean value
"""
arr3 = np.array([3,5,7,9,11])
print(np.sum(arr3))
print(np.max(arr3))
print(np.min(arr3))
print(np.mean(arr3))
print("_____________________________________________________________________________________________________________")


"""Create a 2×4 array of random numbers and find:

Sum across rows

Sum across columns"""

arr4 = np.array([[1,2,3,4],[3,4,5,6]])
print(np.sum(arr4, axis=1))#for row axis=1
print(np.sum(arr4, axis=0))#for coloumn 

print("_____________________________________________________________________________________________________________")
#Astype
"""Create an array of integers and convert it to float type using astype."""
print(arr3.dtype)
arr_float= arr3.astype(float)
print(arr_float.dtype)

print("_____________________________________________________________________________________________________________")

#dtype
"""Create a NumPy array of complex numbers and print its dtype."""


# Create a NumPy array of complex numbers
arr5 = np.array([1 + 2j, 3 + 4j, 5 + 6j])

# Print the array
print("Array:", arr5)

# Print the dtype
print("Data type:", arr5.dtype)

print("_____________________________________________________________________________________________________________")
"""Create two arrays: a = [1, 2, 3] and b = [4, 5, 6].
Perform:

Addition

Subtraction

Multiplication

Division"""

print(arr + arr3)
print(arr - arr3)
print(arr * arr3)
print(arr / arr3)

print(np.log(arr))#for logarithmic function
print(np.log10(arr))