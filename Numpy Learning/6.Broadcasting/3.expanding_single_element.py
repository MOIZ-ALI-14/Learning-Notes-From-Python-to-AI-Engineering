import numpy as np

arr = np.array([100, 200, 300])
result = arr + 10
print(result)

# This is an example of broadcasting rule --> expanding single element:
# mean that a single value can be broadcast across every element
# of a compatible array.
# ======================================================================


# 1d to 2d opertion practice:
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
result = vector + matrix
print(result)

# This is almost the same rule, here[10,20,30] is broadcast across each row
# of the 2D array
# mean that broadcasting the smaller array across the larger array
# First rule is also applied in thes way that element by element operation
# can be applied successfully.
# ======================================================================
