import numpy as np

float_array = np.array([1.5, 2.3, 3.7, 4.1])
print(float_array)
print(float_array.dtype)

int_array = float_array.astype(int)
print(int_array)
print(int_array.dtype)

# we use astype when we want conversion of the data type of the array elements. For example,
# we can convert an array of floats to an array of integers using astype(int). The resulting 
# array will have the integer data type, and all the float values will be truncated to their
# integer parts.