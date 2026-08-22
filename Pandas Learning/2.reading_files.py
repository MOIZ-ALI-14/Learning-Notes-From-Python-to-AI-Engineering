import pandas as pd

# We first read the CSV, JSON, or Excel file into a Pandas DataFrame.
# After loading the data, we inspect it to find missing, duplicate, or incorrect values.
# Then we clean and transform the data so it is ready for analysis or machine learning.

# read data from json file into a dataframe
my_dataframe = pd.read_json("sample_Data.json")
print(my_dataframe)

# read data from excel file into a dataframe
my_newdf = pd.read_excel("save_in.xlsx")
print(my_newdf)

# read data from csv file into a dataframe
csv_data = pd.read_csv("color_srgb.csv")
print(csv_data)


# important points:

# If reading a file causes an encoding error, try encoding="utf-8" or encoding="latin-1".
# For data stored in cloud storage, libraries such as gcsfs can be used to access the files.
# If the dataset is too large for memory, read it in smaller chunks using chunksize.
# A for loop can then process each chunk separately instead of loading the entire file.
# These techniques help handle encoding issues, cloud-based files, and large datasets.
