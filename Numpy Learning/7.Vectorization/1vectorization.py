# Definition:
# Without using loops applying operaion on an entire
# array(on each element of the array) at once is
# called vectorization.
# Calculation becomes 100x faster with it, then we
# don't need to use traditional python loops.


# in simple python we do:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [x + y for x, y in zip(list1, list2)]
print(result)
# this upper code will work but while working
# with long lists it will be slowed down.

# Now with Vectorization in Numpy
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)
# IN large datasets such vectorization performs
# much faster actions than simple python

# one more example
arr_last = np.array([2, 3, 4])
multiply = arr_last * 4
print(multiply)
# performing multiplication on entire array
