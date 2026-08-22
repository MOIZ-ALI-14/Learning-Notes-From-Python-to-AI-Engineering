import numpy as np

arr = np.array([1, 2, 3, 4, 6])
print(arr.dtype)

arr1 = np.array([2, 3, 4, 3.2])
print(arr1.dtype)

arr2 = np.array(["apple", "banana", "cherry"])
print(arr2.dtype)

# we use dtype to define the data type of the array elements. For example,
# we can create an array of integers, floats, or strings. The dtype attribute
# allows us to check the data type of the elements in the array.

# one important thing to note is that when we create an array with mixed data
# types, NumPy will automatically upcast the data type to accommodate all elements.
# For example, if we create an array with both integers and floats, the resulting array
# will have a float data type as numpy gives priority to that data type that can represent
# all the elements and all element's type would be converted to float.
# After that, if we use dtype to check the data type of the array, it will return float64.
# Similarly, if we create an array with both strings and numbers, the resulting array
# will have a string data type.
