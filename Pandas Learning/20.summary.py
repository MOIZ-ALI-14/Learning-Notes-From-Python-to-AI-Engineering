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

average_age = df["age"].mean()  # Average age
minimum_performance = df["performance rate"].min()  # Lowest performance rate
highest_performance = df["performance rate"].max()  # Highest performance rate
average_salary = df["salary"].mean()  # Average salary
total_salary = df["salary"].sum()  # Total of all salaries
youngest_age = df["age"].min()  # Youngest age
oldest_age = df["age"].max()  # Oldest age

print(f"Average age: {average_age}")
print(f"Minimum performance: {minimum_performance}")
print(f"Highest performance: {highest_performance}")
print(f"Average salary: {average_salary}")
print(f"Total salary: {total_salary}")
print(f"Youngest age: {youngest_age}")
print(f"Oldest age: {oldest_age}")


# Summary calculations give us a quick overview of important information in our data.
# They help us understand values without checking every row manually.
# Pandas provides simple functions to calculate different summaries.
# mean() → finds the average value.
# min() → finds the smallest value, while max() → finds the largest value.
# sum() → calculates the total, and count() → counts the available values.
# We can apply these functions to any suitable numerical column.
# Example: df["salary"].mean() gives the average salary, while df["age"].max() gives the oldest age.
