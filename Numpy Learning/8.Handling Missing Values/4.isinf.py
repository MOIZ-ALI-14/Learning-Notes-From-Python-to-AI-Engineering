import numpy as np

arr = np.array([1, 2, 2, 44, np.inf, 34, -np.inf])
print(np.isinf(arr))


# np.isinf() is used to detect infinite values in an array.
# It detects both positive infinity (np.inf) and negative infinity (-np.inf).
# np.isinf(arr) returns True where the value is +inf or -inf.
# arr == np.inf checks specifically for positive infinity.
# arr == -np.inf checks specifically for negative infinity.
# np.nan_to_num() can be used later to replace these infinite values.
