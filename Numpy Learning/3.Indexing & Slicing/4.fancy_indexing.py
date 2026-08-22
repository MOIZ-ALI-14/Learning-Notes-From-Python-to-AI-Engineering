import numpy as np

my_array = np.array([222, 444, 555, 666])
print(my_array[[3, 0, 0, 1]])

# we do fancy indexing especially when we want to access multiple
# elements of an array at once. In this case, we are accessing the
# elements at indices 3, 0, 0, and 1 of the array `my_array`. The
# output will be: [666 222 222 444]
# Fancy indexing is useful we want elements from a non-sequential
# order or when we want to repeat elements.
