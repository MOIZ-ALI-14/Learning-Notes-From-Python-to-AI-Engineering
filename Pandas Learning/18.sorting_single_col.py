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

# sorting by single column
df.sort_values(by="salary", ascending=False, inplace=True)
print(df)


# Sorting is used to arrange data in a meaningful order, making it easier to compare and analyze.
# sort_values() sorts the DataFrame according to the values of a selected column.
# Syntax: df.sort_values(by="column_name", ascending=True/False)
# ascending=True sorts from smallest to largest; ascending=False sorts from largest to smallest.
# Here, salary is sorted in descending order, so the highest salary appears at the top.
# Although we sort by only one column, the complete rows move together, so the related name, age, and performance also stay connected.
# inplace=True applies the sorting directly to the original DataFrame.
