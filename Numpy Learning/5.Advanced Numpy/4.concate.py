# np.concatenate() is used to join two or more NumPy arrays together into one array.
# axis=0(also called vertical stacking) → joins row-wise; for 2D arrays, it adds rows.
# axis=1(also called horizontal stacking) → joins column-wise; for 2D arrays, it adds columns.
# axis=None → treats the arrays as flattened 1D sequences before joining them.
# The arrays must have compatible shapes along the other dimensions.
# 1D example: np.concatenate(([1,2,3], [4,5,6])) → [1,2,3,4,5,6].
# Real-life use: combine data from different students, months, files, or datasets
# into one larger dataset.
# it also creates new array and doesn't change the original array
# 🧠 Remember: 0 → rows, 1 → columns, None → flattened(1d).

import numpy as np

arr1 = np.array([11, 22, 33, 44])
arr2 = np.array([55, 66, 77, 88])
joined_array = np.concatenate((arr1, arr2), axis=None)
print(joined_array)

# Concatenate joins arrays; axis tells it the direction of joining. It doesn't
# magically turn 1D arrays into 2D arrays.
