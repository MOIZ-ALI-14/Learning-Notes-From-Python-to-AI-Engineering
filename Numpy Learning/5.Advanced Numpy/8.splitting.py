# np.split() → splits an array into multiple smaller arrays at equal divisions.
# np.array_split() → also splits an array, but it can handle unequal divisions when the size doesn't divide evenly.
# np.hsplit() → splits a 2D array horizontally, meaning it separates columns.
# np.vsplit() → splits a 2D array vertically, meaning it separates rows.
# axis=0 → splitting is based on rows.
# axis=1 → splitting is based on columns.
# np.split() normally requires the array to be divisible equally according to the number of sections.
# Real-life use: split a large dataset into smaller parts for processing, analysis, or different tasks.
# 🧠 Remember: split = general, hsplit = columns, vsplit = rows, array_split = unequal sizes allowed.

import numpy as np

arr_1d = np.array([11, 33, 55, 77, 99, 12, 13, 14, 15, 15])
split_1d = np.split(arr_1d, 2)
print(split_1d)

arr_1d_2 = np.array([11, 33, 55, 77, 99, 12, 13, 14, 15, 16])
split_1d_2 = np.array_split(arr_1d_2, 4)
print(split_1d_2)

arr_2d = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_2d)
split_2d = np.hsplit(arr_2d, 2)
print(split_2d)

arr_2d_2 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr_2d_2)
split_2d_2 = np.vsplit(arr_2d_2, 3)
print(split_2d_2)
