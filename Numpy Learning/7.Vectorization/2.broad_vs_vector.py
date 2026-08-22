# VECTORISATION
# Vectorisation means applying an operation to an entire NumPy array at once, without using an explicit Python loop.
# It is used when the same operation needs to be performed on multiple or all elements of an array.
# NumPy performs these operations efficiently using optimized internal operations.
# Example: prices * 2 multiplies every element of prices by 2.
# Main purpose: faster and cleaner array operations compared with traditional Python loops.


# BROADCASTING
# Broadcasting is a NumPy feature that allows operations between arrays of compatible shapes.
# It automatically adjusts the smaller array or value so that it can work with the larger array during the operation.
# It is used when arrays have different but compatible shapes.
# Example: prices + 10 adds 10 to every element of the prices array.
# Main purpose: perform operations between compatible arrays without manually matching their shapes.


# KEY DIFFERENCE
# Vectorisation focuses on performing operations on arrays without explicit loops.
# Broadcasting focuses on making compatible shapes work together during an operation.
# Both can occur together in the same NumPy expression.
