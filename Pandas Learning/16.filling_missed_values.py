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


df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())
df["performance rate"] = df["performance rate"].fillna(df["performance rate"].mean())
print(df)


# fillna() is used to replace missing (NaN) values instead of removing the data.
# It is useful when we want to keep the row but provide a suitable value for the missing data.
# Unlike dropna(), fillna() does not delete the row or column containing the missing value.
# We can use fillna() column-wise by specifying the particular column we want to modify.
# We can provide a fixed/default value to replace missing values, such as 0, "Unknown", or another value.
# We can also calculate a value automatically and use it for filling, such as mean, median, or mode.
# For numerical columns, mean or median is commonly used when we want a reasonable replacement value.
# fillna() can therefore handle missing values while preserving the original size and structure of the DataFrame.
# In contrast, dropna() can remove rows or columns, with axis=0 for rows and axis=1 for columns.
