# What is Indexing of an Array in NumPy?

# Indexing allows you to access individual elements of an array using their position (or index).

# We do indexing when we want to access or modify one specific element of an array.

# =========================================================================================

# What is Slicing of an Array in NumPy?

# Slicing allows you to access a range of elements in an array by specifying a start, stop, and step index.

# It creates a new view of the original array without copying the data.

# We use slicing when we want to perform operations on multiple elements of an array at once,

# rather than accessing them one by one.

# =========================================================================================

# What is Fancy Indexing of an Array in NumPy?

# Fancy indexing allows you to access multiple specific elements of an array using an array or list of indices.

# In easy terms, it allows you to select multiple elements from an array using a list or array of indices.

# We use it when we want to access or modify multiple specific elements of an array at once,

# rather than accessing them one by one.

# For example:

# arr[[0, 3, 5]] will return the elements at indices 0, 3, and 5 of the array arr.

# We can also use one index multiple times to access the same element multiple times.

# For example:

# arr[[0, 0, 1]] will return the elements at indices 0, 0, and 1 of the array arr.

# Note: Boolean masking is also a type of advanced indexing in NumPy,

# but it is better to learn it separately because it uses Boolean conditions/masks

# rather than integer indices.

# =========================================================================================

# What is Boolean Masking of an Array in NumPy?

# Boolean masking allows you to access elements of an array based on a condition or a Boolean array.

# It creates a new array (a copy) containing the elements that satisfy the condition.

# We use it when we want to filter elements of an array based on a condition,

# rather than accessing them one by one.

# For example:

# arr[arr > 10] will return the elements whose values are greater than 10.

# A Boolean mask looks like:

# [True, False, True, False]

# NumPy selects the elements where the mask is True.

# =========================================================================================

# IMPORTANT: View vs Copy

# Basic Indexing -> Refers to the original array element

# Changes made to the indexed element directly affect the original array.

# Slicing -> View

# Changes made through the slice can affect the original array.

# Fancy indexing -> Copy

# Changes made to the result do not affect the original array.

# Boolean masking -> Copy

# Changes made to the result do not affect the original array.
