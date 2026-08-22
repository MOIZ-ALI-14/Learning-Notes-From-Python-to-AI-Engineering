# ============================================================
#          HANDLING MISSING VALUES IN NUMPY
# ============================================================

# Why do we need to handle missing values?
# Missing or invalid values can appear in real-world datasets.
# If we don't handle them, they can cause incorrect calculations
# or unexpected results.

# Example 1:
# A student's marks may be missing:
# [85, 90, np.nan, 78]
# Calculating statistics without handling the missing value
# may produce an unwanted NaN result.

# Example 2:
# A dataset may contain infinite values:
# [10, 20, np.inf, 40]
# Infinite values can affect calculations and should be handled.

# Example 3:
# Data collected from files, sensors, or databases may contain
# NaN or infinite values, so we need to detect and replace them
# before performing further calculations.


# ============================================================
# NumPy provides useful built-in functions for this:
# ============================================================

# 1. np.isnan()
# Used to check whether values are NaN (Not a Number).
# It returns True for NaN values and False for normal values.


# 2. np.nan_to_num()
# Used to replace NaN and infinite values with suitable numbers.
# By default, NaN is replaced with 0, while positive and negative
# infinity are replaced with large finite values.
# We can also specify our own replacement values.


# 3. np.isinf()
# Used to check whether values are positive or negative infinity.
# It returns True for infinite values and False for finite values.


# ============================================================
# In short:
# np.isnan()      -> Detect NaN values
# np.isinf()      -> Detect infinite values
# np.nan_to_num() -> Replace NaN and infinite values
# ============================================================
