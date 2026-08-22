import numpy as np

prices = np.array([100, 200, 300])
discount = 10  # 10% discount to each item

final_prices = prices - (prices * discount / 100)

print(final_prices)

# we can see that broadcastion prevents extra lines of code
# it helps to get rid of using loops
# performing faster operation

# Important

# When 'prices' is a NumPy array, the operation automatically applies to every element.
# The result of the array operation is also stored as a new NumPy array in 'final_prices'.

# Broadcastion Rules:

# 1. Matching dimensions
# Definition: Both arrays have the same shape, so NumPy performs the operation element-by-element.
# [1, 2, 3] + [10, 20, 30]
# # [11, 22, 33]


# 2. Expanding a single element
# Definition: A single value can be broadcast across every element of a compatible array.
# [1, 2, 3] + 10
# # [11, 12, 13]
# And yes, multiplication works too:
# [1, 2, 3] * 10
# # [10, 20, 30]
 

# 3. Incompatible shapes
# Definition: If the shapes cannot be matched according to NumPy's broadcasting rules, NumPy raises an error.
# [1, 2, 3] + [10, 20]
# # ❌ Error
# Because (3,) and (2,) cannot be broadcast together.
