# The main purpose of interpolation is to estimate missing values while preserving
# the continuity or pattern of the data.

import pandas as pd

my_data = {
    "name": [
        "Ali",
        "Ahmad",
        "Ahsan",
        "Usman",
        "Umar",
        "Arslan",
        "Moiz",
        "Hamza",
        "Muhammad",
    ],
    "age": [21, 22, 23, None, 25, 26, 27, None, 29],
    "salary": [10000, 12000, 8000, None, 3000, 9000, None, 15000, 30000],
    "performance rate": [60, 65, None, 75, None, 85, 88, None, 95],
}

df = pd.DataFrame(my_data)

print(df)


# Linear interpolation
df["age"] = df["age"].interpolate(method="linear")


# Polynomial interpolation
df["salary"] = df["salary"].interpolate(method="polynomial", order=2)


# Time interpolation requires a datetime index
df.index = pd.date_range(start="2026-01-01", periods=len(df), freq="D")
# pd.date_range() is used to generate a sequence of dates and can be used as a DataFrame index.
# start defines the date from which the sequence should begin.
# periods defines how many dates should be generated, usually matching the number of rows.
# freq="D" means the dates will increase by one day for each row.
# df.index = assigns these generated dates as the DataFrame's index for time-based operations.

df["performance rate"] = df["performance rate"].interpolate(method="time")


print(df)


# Interpolation is used to estimate missing values by looking at the known values around them.
# Unlike fillna(), interpolation does not simply use one fixed value; it estimates a suitable value from nearby data.
# Linear interpolation assumes that the values change at a constant rate between two known values.
# Example: if values are 20, NaN, 30, linear interpolation estimates the missing value as 25.
# Polynomial interpolation uses a polynomial curve to estimate missing values based on surrounding known values.
# A higher polynomial order can create a more flexible curve, but very high orders can sometimes give unrealistic results.
# Time-based interpolation is useful for time-series data, where missing values are estimated according to time intervals.
# For time interpolation, the DataFrame needs a datetime index so Pandas can understand the actual time gaps.
# The main purpose of interpolation is to estimate missing values while preserving the continuity or pattern of the data.


# =========================================================================================
# Interpolation Methods:
#
# 1. Linear Interpolation:
#    - Estimates missing values by assuming a straight-line relationship between known values.
#    - Pros: Simple, fast, easy to understand, and usually gives stable results.
#    - Cons: Cannot properly capture complex or curved patterns in the data.
#    - Use when: Data changes at a relatively constant or smooth rate.
#
# 2. Polynomial Interpolation:
#    - Estimates missing values by fitting a curved polynomial relationship to known values.
#    - Pros: Can capture curved and more complex patterns better than linear interpolation.
#    - Cons: Higher polynomial orders can produce unrealistic or unstable values.
#    - Use when: The data has a clear curved pattern or trend.
#    - Example: method="polynomial", order=2
#
# 3. Time Interpolation:
#    - Estimates missing values according to the actual time intervals between known values.
#    - Pros: Very useful for time-series data and can consider unequal time gaps.
#    - Cons: Requires a proper datetime index and is mainly useful for time-based data.
#    - Use when: Data contains dates/timestamps, such as temperature, sales, sensors, etc.
#    - Example: method="time"
#
# Easy rule to remember:
# Linear     → Straight/steady trend
# Polynomial → Curved/complex trend
# Time       → Time-series data.
# =========================================================================================
