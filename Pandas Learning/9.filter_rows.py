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

# filtering rows with one condition
high_performance = df[df["performance rate"] > 75]
print(f"\nprinting performance rate")
print(high_performance)

# filtering rows with multiple conditions
subset = df[(df["performance rate"] > 75) & (df["salary"] < 30000)]
print(f"\nfiltering rows based on tow conditions")
print(subset)

# using OR(|) condition
filtering_OR = df[(df["performance rate"] < 70) | (df["salary"] > 30000)]
print(filtering_OR)

# Row filtering is used when we want to select only the rows that satisfy a specific condition.
# We can filter data to focus only on the records relevant to our analysis.
# A single condition uses a comparison such as >, <, ==, >=, or <=.
# Example: df[df["performance rate"] > 75] selects employees with performance above 75.
# Multiple conditions can be combined using & (AND) when all conditions must be true.
# Example: performance > 75 AND salary < 30000 selects employees meeting both conditions.
# The | (OR) operator is used when at least one of the conditions must be true.
# Example: performance < 70 OR salary > 30000 selects employees satisfying either condition.
# Remember: one condition → one filter; & → AND; | → OR.
