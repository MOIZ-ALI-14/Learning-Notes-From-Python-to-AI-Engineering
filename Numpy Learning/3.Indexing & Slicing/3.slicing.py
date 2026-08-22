# syntax:
# array[start:stop:step]

import numpy as np

array_1d = np.array([11, 22, 33, 44, 55, 66])
print(
    array_1d[0:3]
)  # will print [11 22 33] by slicing the array from index 0 to index 2 (stop index is exclusive)
print(
    array_1d[2:]
)  # will print [33 44 55 66] by slicing the array from index 2 to the end
print(
    array_1d[:4]
)  # will print [11 22 33 44] by slicing the array from the start to index 3 (stop index is exclusive)
print(
    array_1d[::-1]
)  # will print [66 55 44 33 22 11] by slicing the array in reverse order
print(array_1d[::2])  # will print [11 33 55] by slicing the array with a step of 2
print(
    array_1d[1::2]
)  # will print [22 44 66] by slicing the array from index 1 to the end with a step of 2
print(
    array_1d[1:5:2]
)  # will print [22 44] by slicing the array from index 1 to index 4 with a step of 2