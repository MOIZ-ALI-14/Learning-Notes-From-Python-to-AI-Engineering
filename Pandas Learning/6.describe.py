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
    "age": [23, 34, 34, 22, 27, 26, 31, 24, 29],
    "salary": [24000, 15000, 19000, 21000, 30000, 32000, 18000, 27000, 31000],
    "performance rate": [60, 78, 84, 90, 93, 64, 66, 76, 72],
}

df = pd.DataFrame(my_data)
print(df)
print(f"\n\n")
print(df.describe())

# describe() gives a quick statistical summary of numerical columns in a DataFrame.
# It is used to understand the data before deeper analysis and to quickly spot unusual values.
# count = number of non-missing values; in this data, age, salary, and performance rate each have 9 values.
# mean = average value; e.g., the average salary tells us the typical salary in the dataset.
# std = standard deviation; it tells us how spread out the values are around their mean.
# 25% = first quartile (Q1): 25% of the values are at or below this point.
# 50% = median (Q2): the middle value when the data is ordered.
# 75% = third quartile (Q3): 75% of the values are at or below this point.
# min = smallest value and max = largest value, showing the overall range of the data.
# In this DataFrame, describe() summarizes age, salary, and performance rate separately.
# Example: a higher salary std means salaries vary more from the average salary; a lower std means they are more similar.
# describe() is mainly useful for quickly understanding numerical data before cleaning, analysis, or machine learning.

# Standard deviation → measure the typical spread.
# Compare SD with the mean → understand how large that spread is relative to the data.
# Use the context → decide whether that amount of variation is acceptable or not.
