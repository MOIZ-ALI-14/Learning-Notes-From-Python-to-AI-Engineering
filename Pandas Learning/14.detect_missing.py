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
    "age": [23, 34, 34, None, 27, 26, 31, 24, 29],
    "salary": [24000, 15000, 19000, 21000, 30000, None, 18000, 27000, 31000],
    "performance rate": [None, 78, 84, 90, 93, 64, 66, 76, 72],
}

df = pd.DataFrame(my_data)
print(df)

# detecting where data is missed
print(df.isnull())


# it will tell how many values are missed in each column
print(df.isnull().sum())


# None represents a missing value when creating our DataFrame.
# Pandas recognizes None as a missing value and can detect it with isnull().
# NaN (Not a Number) is another common representation of missing numerical data.
# Pandas also recognizes NaN as a missing value, so isnull() detects both None and NaN.
# df.isnull() returns True where a value is missing and False where a value exists.
# df.isnull().sum() counts the missing values in each column.

# NumPy mainly focuses on numerical and array operations, where NaN and infinity can appear during calculations.
# NaN means "Not a Number" and can represent an undefined or missing numerical value.
# Pandas mainly focuses on structured data, so it provides tools to detect and handle missing values.
# In Pandas, missing values can commonly appear as None or NaN.
# df.isnull() detects missing values, whether they are represented by None or NaN.
# NumPy → numerical/array computation; Pandas → data handling, cleaning, and missing-value management.
