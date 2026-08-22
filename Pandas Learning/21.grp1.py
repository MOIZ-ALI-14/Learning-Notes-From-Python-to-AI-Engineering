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
    "age": [21, 22, 22, 21, 25, 23, 27, 21, 23],
    "salary": [10000, 12000, 8000, 13000, 3000, 9000, 9000, 15000, 30000],
    "performance rate": [60, 65, 45, 75, 34, 85, 88, 76, 95],
}

df = pd.DataFrame(my_data)

print(df)

grouped = df.groupby("age")["salary"]
print(grouped.sum())


# groupby() is used when we want to divide our data into groups based on a specific column.
# Here, "age" is the grouping column, so employees with the same age are placed in the same group.
# After grouping, we select "salary" because we want to perform an operation on salaries.
# grouped = df.groupby("age")["salary"] means: group salaries according to each age.
# We can then apply operations such as sum(), mean(), min(), max(), or count() to each group.
# grouped.sum() calculates the total salary for each age group.
# For example, age 21 has salaries 10,000, 13,000, and 15,000, so their total is 38,000.
# The result gives one summary value for each unique age group instead of showing every individual row.
# Simple idea: GROUP BY → divide data; SELECT COLUMN → choose what to analyze; FUNCTION → perform the calculation.
