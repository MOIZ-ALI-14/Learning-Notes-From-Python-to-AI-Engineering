import numpy as np

arr = np.array([1, 2, 2, 44, np.nan, 34, np.nan])
print(np.isnan(arr))


# np.nan represents a missing, unknown, or undefined numerical value.
# We can manually put np.nan when we don't know a numerical value while entering data.
# Later, np.isnan() can be used to detect which values are NaN.
# Some mathematical operations can also produce NaN automatically, such as 0/0.
# NumPy can produce NaN automatically when a calculation has an undefined numerical result.
# np.isnan() can detect both manually entered NaN values and NaN values produced by calculations.
