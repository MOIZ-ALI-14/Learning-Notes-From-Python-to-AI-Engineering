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

# this method adds column at the end
df["Bonus"] = df["salary"] * 10 / 100
print(df)

# using insert method or adding column at specific position
df.insert(0, "Employee ID", [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(df)

# Adding a column is useful when we want to store new information or calculated results in our DataFrame.
# The simple df["Bonus"] = ... method adds the new column at the end of the DataFrame.
# We can perform operations on an existing column to calculate the new column.
# Example: df["salary"] * 10 / 100 calculates 10% of every salary and returns a Series.
# That resulting Series is stored as a new "Bonus" column.
# The insert() method allows us to add a new column at a specific position.
# In insert(), we provide the position, column name, and values, such as a list of Employee IDs.
# The list must contain the appropriate number of values for the DataFrame's rows.
