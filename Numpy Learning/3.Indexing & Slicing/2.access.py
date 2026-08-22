# syntax:
# array[index] # 1d array
# array[row_index, column_index] # 2d array
# array[depth_index, row_index, column_index] # 3d or multidimensional array

import numpy as np

array_1d = np.array([11, 22, 33, 44, 55, 66])
print(array_1d[0])
print(array_1d[-1])  # last element
print(array_1d[4])

array_2d = np.array([[22, 22, 22], [44, 100, 44]])
print(array_2d[0, 1])  # will print 100 by accessing the element at row 0 and column 1


array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(
    array_3d[0, 0, 1]
)  # will print 2 by accessing the element at depth 0, row 0 and column 1
