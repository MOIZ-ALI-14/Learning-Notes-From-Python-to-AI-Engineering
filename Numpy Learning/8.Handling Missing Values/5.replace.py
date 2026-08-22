import numpy as np

arr = np.array([1, 2, 2, 44, np.inf, 34, -np.inf])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=100, neginf=-100)
print(cleaned_arr)


# posinf is used to specify the replacement value for positive infinity (+inf).
# neginf is used to specify the replacement value for negative infinity (-inf).
# Example: np.nan_to_num(arr, posinf=100, neginf=-100)
# This replaces +inf with 100 and -inf with -100.
# The values 100 and -100 are chosen by us according to the project.
