import pandas as pd

my_data = {
    "name": [
        "Ali",
        "Ahmad",
        "Ahmad",
        "Ali",
        "Umar",
        "Arslan",
        "Moiz",
        "Ali",
        "Muhammad",
    ],
    "age": [21, 22, 22, 21, 25, 23, 27, 21, 23],
    "salary": [10000, 12000, 8000, 13000, 3000, 9000, 9000, 15000, 30000],
    "performance rate": [60, 65, 45, 75, 34, 85, 88, 76, 95],
}

df = pd.DataFrame(my_data)

print(df)

grouped = df.groupby(["age", "name"])["salary"]
print(grouped.sum())

# grouped = df.groupby(["name", "age"])["salary"]
# print(grouped.sum())


# Multiple grouping is used when we need to divide data based on two or more columns together.
# Each group is created from the unique combination of the specified columns.
# Here, ["age", "name"] means Pandas groups rows having the same age AND the same name.
# "salary" is selected because it is the column on which we want to perform the calculation.
# grouped.sum() calculates the total salary for every age-name combination.
# For example, age 21 + Ali forms one group, and its salaries are 10,000 and 13,000.
# Therefore, the total salary for the 21-year-old Ali group is 23,000.
# We use multiple grouping when one column alone is not enough to identify the group we need.
# The order of the grouping columns represents the grouping hierarchy, while the complete rows remain correctly matched.
