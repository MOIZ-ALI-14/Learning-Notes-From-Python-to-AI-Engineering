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


# updating complete column
df["salary"] = df["salary"] + (df["salary"] / 2)
print(df)

# Updating a complete column is useful when we want to change or perform an operation on every value in that column.
# Unlike loc[], this method updates the entire selected column at once.
# Example: df["salary"] = df["salary"] + (df["salary"] / 2) increases every salary by 50%.
# The operation is performed element-by-element on the whole Series.
# If the column name before = exactly matches an existing column, that column is updated.
# If the name is different, Pandas creates a new column at the end of the DataFrame.
# Even a small difference in spelling or capitalization creates a new column instead of updating the old one.
# Remember: same column name → update; new/different column name → create new column.
