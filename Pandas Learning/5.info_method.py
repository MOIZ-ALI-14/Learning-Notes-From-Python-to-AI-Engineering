# why do we need to understand data?

# We understand the data because we may not know how many rows and columns it contains.
# We may not know what type of data each column stores, such as integer, float, or string.
# We may also not know which columns contain missing (null) values.


# info() shows the DataFrame's number of rows and columns and provides an overview of its structure.
# It shows column names and the data type (dtype) of each column.
# It shows non-null counts, helping us identify columns with missing values.
# It also shows the DataFrame's memory usage.
# Use df.info() for a quick overview of the DataFrame's structure and data quality.

import pandas as pd

# read data from json file into a dataframe
my_dataframe = pd.read_json("sample_Data.json")
print(my_dataframe)
print(my_dataframe.info())
print(f"\n\n\n")

# now let's check the info of our own dataframe

# Create our own DataFrame from Python data.
my_data = {
    "Name": ["Moiz", "Junaid", "Shoaib"],
    "Age": [21, 18, 14],
    "Class": ["15th", "11th", "8th"],
}

df = pd.DataFrame(my_data)
print(df)
print(df.info())
