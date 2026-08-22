# Creating an array from a list in Python
# we use this method of making array when we know the list
# of elements we want to include in the array.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
# ==================================================================

# Creating array with default values
# we use this method of making array when we want to create
# an array with default values on which we can perform operations later.
zeros_arr = np.zeros(
    5
)  # .zeros() method creates an array of given shape and fills it with zeros.
print(zeros_arr)

ones_arr_2d = np.ones(
    (4, 3)
)  # .ones() method creates an array of given shape and fills it with ones.
print(ones_arr_2d)

# Creating array with specific values
# syntax: np.full(shape, value)
filled_arr = np.full(
    (4, 5), 2
)  # .full() method creates an array of given shape and fills it with a specified value.
print(filled_arr)
# ==================================================================


# Creating sequences of numbers in numpy
# In real life, sequences of numbers can be useful for generating
# test data, creating ranges of values for simulations, or defining
# intervals for analysis. Numpy provides several methods to create
# sequences of numbers efficiently.
# syntax: np.arange(start, stop, step)
arr_range = np.arange(
    1, 13, 3
)  # .arange() method creates an array with evenly spaced values within a given interval.
print(arr_range)
# ==================================================================


# Creating identity matrix in numpy
# in real life, identity matrices are often used in linear algebra and
# matrix operations. They can be used to represent transformations,
# syntax: np.eye(size)
identity_matrix = np.eye(
    5
)  # .eye() method creates a 2-D array with ones on the diagonal and zeros elsewhere.
print(identity_matrix)
# ==================================================================
