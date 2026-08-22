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

# updating single value
# Syntax: df.loc[row_index, "column_name"] = new_value
df.loc[5, "performance rate"] = 99
print(df)

# Updating values is useful when existing data is incorrect or needs to be changed.
# loc[] lets us select a specific row and column using their labels/positions.
# df.loc[5, "performance rate"] selects the value of 6th row in the "performance rate" column.
# = 99 replaces the old value with the new value 99.
# This changes the original DataFrame directly.
# We can use the same method to update other individual values in the DataFrame.
# Example: df.loc[2, "salary"] = 25000 updates the salary of third row.
