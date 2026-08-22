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
    "age": [21, 22, 23, 34, 25, 26, 27, 21, 29],
    "salary": [10000, 12000, 8000, 13000, 3000, 9000, 9000, 15000, 30000],
    "performance rate": [60, 65, 45, 75, 34, 85, 88, 76, 95],
}

df = pd.DataFrame(my_data)

print(df)

# sorting by multiple columns
df.sort_values(by=["age", "performance rate"], ascending=[True, False], inplace=True)
print(df)


# Multi-column sorting is used when we want to organize data using more than one column.
# We pass multiple column names inside a list because Pandas needs to know their sorting priority.
# Pandas processes the columns from left to right, so the first column has the highest priority.
# Here, "age" is the first priority, so employees are sorted from youngest to oldest.
# If two employees have the same age, Pandas uses "performance rate" as the second priority.
# "performance rate" is sorted in descending order because ascending=False.
# ascending=[True, False] gives a separate sorting order for each column.
# The complete rows move together, so names, salaries, ages, and performance rates stay matched.
# We use multi-column sorting when one column alone is not enough to organize the data clearly.
