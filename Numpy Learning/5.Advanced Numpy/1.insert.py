# Syntax
# np.insert(array, index, value, axis=None)
# array--> original array
# index--> the position where we want to insert value
# value--> the value we want to insert
# axis=None → treats the entire array as one flattened 1D sequence.
# if axis=0 → operates along rows; for a 2D array, it means working
# with/inserting rows.
# if axis=1 → operates along columns; for a 2D array, it means working
# with/inserting columns.

import numpy as np

my_array = np.array([12, 13, 14, 15, 16, 17, 18])
print(my_array)
new_array = np.insert(my_array, 4, 1515, axis=None)
print(new_array)

# Important
# NumPy arrays have a fixed size once created.
# Unlike Python lists, we don't normally grow or shrink an array in place.
# To add, remove, split, or join data, NumPy usually creates a new array.
# Functions such as np.insert(),np.append(),np.concatenate(),np.delete()
# etc return a modified/new array.
# So remember: List → easily modified; NumPy array → structured, and
# size-changing operations create a new array.

# use:
# in real life, in large dataset, adding a new column of monthly sales
# data to an existing dataset
