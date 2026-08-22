# delete() is used to delete any element in the array
# it also returns new array and does'nt change the original array
# syntax: np.delete(arry,index,axis=None)
# axis=None means for flattened or 1D array

import numpy as np

arr = np.array([11, 22, 33, 44, 55, 66, 77])
print(arr)
new_arr = np.delete(arr, 1, axis=None)
print(new_arr)
