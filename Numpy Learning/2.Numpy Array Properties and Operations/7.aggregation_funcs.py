import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6])
# Sum of all elements
print(np.sum(my_array))
# Mean of all elements
print(np.mean(my_array))
# Median of all elements
print(np.median(my_array))
# minimum value
print(np.min(my_array))
# maximum value
print(np.max(my_array))
# variance of all elements
print(np.var(my_array))
# standard deviation of all elements
print(np.std(my_array))

# we will use these functions in Ai engineering to analyze data and extract meaningful insights.
# Aggregation functions like sum, mean, median, min, max, variance, and standard deviation are
# essential for summarizing datasets and understanding their distribution.

# Now what is variance and standard deviation, i will cover in pandas lecture InShaAllah.

# For now, i know that we find variance by calculating the average of the squared differences
# from the mean, and standard deviation is the square root of variance. These metrics help us
# understand how spread out the data is around the mean.

# ===> we find standard deviation to check whether our data is normally distributed or not.
# If the standard deviation is small, it means that the data points are close to the mean,
# indicating a normal distribution(consistent data). Conversely, a large standard deviation
# suggests that the data points are spread out over a wider range of values, indicating a
# non-normal distribution(inconsistent data).
