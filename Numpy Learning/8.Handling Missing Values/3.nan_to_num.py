import numpy as np

arr = np.array([1, 2, 2, 44, np.nan, 34, np.nan])
print(arr)

cleaned_arr = np.nan_to_num(arr)
print(cleaned_arr)

cleaned_arr = np.nan_to_num(arr, nan=77)
print(cleaned_arr)

# np.nan_to_num() is used to replace NaN and infinite values in an array.
# We use it after detecting NaN values when we want to replace them.
# By default, np.nan_to_num() replaces NaN values with 0.
# Syntax: np.nan_to_num(array)
# We can specify our own value for NaN using: np.nan_to_num(array, nan=value)
# Example: np.nan_to_num(arr, nan=50) -> replaces NaN values with 50.
