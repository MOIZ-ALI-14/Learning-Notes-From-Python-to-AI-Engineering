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

# selecting single column
ages = df["age"]
print(f"\nsingle column returns series")
print(ages)

# selecting multiple columns
subset = df[["name", "salary"]]
print(f"\nMultiple columns return dataframe")
print(subset)

# Column selection is used when we need to work with specific information from a DataFrame.
# We may not need all columns, so selecting only the required columns makes the data easier to work with.
# Selecting one column with df["age"] returns a Pandas Series.
# Example: df["age"] selects only the age values from our DataFrame.
# Selecting multiple columns with df[["name", "salary"]] returns a DataFrame.
# Example: df[["name", "salary"]] gives us only the employees' names and salaries.
# We can use selected columns for calculations, filtering, cleaning, or further analysis.
# Selecting columns prevents unnecessary data from being included in our operation.
# Remember: single column → Series; multiple columns → DataFrame.
