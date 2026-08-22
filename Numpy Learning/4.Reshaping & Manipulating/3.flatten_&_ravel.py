# .flatten and .ravel, both are used for converting multidimensional arrays
# to one-dimensional array but the difference is this that flatten creates
# a copy of original array however ravel create views means thats changing
# values after using ravel will affect original array.

import numpy as np

multi_arr = np.array(
    [[[1, 1, 1], [3, 3, 3], [5, 5, 5]], [[2, 2, 2], [4, 4, 4], [6, 6, 6]]]
)

print(multi_arr.flatten())# creates copy
print(multi_arr.ravel())# creates view
