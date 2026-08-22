import pandas as pd

# read data from json file into a dataframe
my_dataframe = pd.read_json("sample_Data.json")
print(my_dataframe)

print(my_dataframe.head(7))
print(my_dataframe.tail(4))

# head() shows the first 5 rows by default.
# tail() shows the last 5 rows by default.
# We can pass a number, such as head(7) or tail(4), to view that many rows.
# We use head() and tail() to quickly inspect whether the data was loaded correctly.
# They help us understand the beginning and end of the dataset and spot obvious problems.
# We can also use them to check whether the data structure looks consistent.
