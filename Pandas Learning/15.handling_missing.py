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

# this will delete each row that has None/NaN value
newdf = df.dropna(inplace=False, axis=0)
print(newdf)

# this will delete each column that has None/NaN value
df.dropna(inplace=True, axis=1)
print(df)

# dropna() is used to remove rows or columns that contain missing values.
# axis=0 means we check rows; a row containing a missing value will be removed.
# axis=1 means we check columns; a column containing a missing value will be removed.
# inplace=False returns a new DataFrame, so the original DataFrame remains unchanged.
# inplace=True changes the original DataFrame directly.
# In our data, axis=0 removes rows containing None/NaN values.
# axis=1 removes columns containing None/NaN values.
# dropna() is useful when missing data cannot be kept and we want a cleaner DataFrame.
# If axis is not specified, dropna() uses axis=0 by default and removes rows containing
# missing values.


# We use dropna() when missing values are not useful and removing the affected data won't hurt our analysis.

# Drop rows when only a few records have missing values and those records can safely be removed.
# Drop columns when a column has too many missing values and isn't useful enough to keep.
# We shouldn't blindly remove missing data if those rows/columns contain important information.

# For example, if only 2 out of 10,000 employee records have missing salaries, removing those 2 rows may
# be reasonable. But if 8,000 salaries are missing, dropping the entire salary column might lose important information
