import numpy as np

my_2d_array = np.array([[1, 2], [3, 4]])
print(my_2d_array)
new_2d_array = np.insert(my_2d_array, 0, [6, 7], axis=0)
print(new_2d_array)

# keep in mind that if axis=0, new numpy array will insert the value
# in row wise, if axis=1, new numpy array will insert the value in
# column wise, if axis=None, then new value will be entered as in 1d array.
