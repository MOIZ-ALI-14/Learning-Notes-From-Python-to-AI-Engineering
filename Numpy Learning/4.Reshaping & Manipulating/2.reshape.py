# Syntax
# reshape(rows, columns) # specify new shape works only if dimensions match. for example,
# if we have an array with 12 elements, we can reshape it into a 3x4 array or a
# 4x3 array, but we cannot reshape it into a 2x5 array because that would require
# 10 elements.

# important note: Reshaping never creates a copy, it creates view means that the
# changing values in new shape will definitely affect the original array.


import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped1_array = my_array.reshape(6, 2)
reshaped2_array = my_array.reshape(4, 3)
print(reshaped1_array)
print(reshaped2_array)
