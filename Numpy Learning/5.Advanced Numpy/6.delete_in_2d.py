# Deleting in 2D array

import numpy as np

arr_2d = np.array([[11, 55, 77], [22, 44, 66], [33, 44, 66]])
new_arr = np.delete(arr_2d, 1, axis=0)
print(new_arr)