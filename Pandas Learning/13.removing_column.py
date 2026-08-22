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


# deleting one column
df.drop(columns=["age"], inplace=True)
print(df)

# deleting multiple columns
df.drop(columns=["salary", "performance rate"], inplace=True)
print(df)

# Deleting columns is useful when we no longer need certain data for our analysis.
# drop() can remove one or multiple columns from a DataFrame.
# columns=["age"] removes the single "age" column.
# columns=["salary", "performance rate"] removes multiple columns at once.
# inplace=True applies the deletion directly to the original DataFrame.
# Without inplace=True, drop() returns a new DataFrame and the original remains unchanged.
# We can remove unnecessary columns to keep our DataFrame clean and easier to work with.
# Remember: one column → one name; multiple columns → list of names.
