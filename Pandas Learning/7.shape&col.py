# Before manipulating or analyzing data, we should first understand its basic structure.
# df.shape returns (rows, columns), helping us know how large the DataFrame is.
# This helps us understand whether we are working with a small or large dataset.
# df.columns returns the names of all columns in the DataFrame.
# Column names help us identify what type of information is available in the dataset.
# These attributes give us a quick overview before selecting, cleaning, or analyzing data.
# Example: df.shape → (1000, 5) means 1000 rows and 5 columns.
# Example: df.columns → shows the names of those 5 columns.

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
print(f"{df}\n\n")
print(f"Shape of Dataframe: {df.shape}")
print(f"Columns of Dataframe: {df.columns}")
