import pandas as pd

# For Customer name
cust_df = {"cust_id": [1, 2, 3, 8], "cust_name": ["Moiz", "Junaid", "ALi", "Subhan"]}

# For Orderamount
order_df = {
    "cust_id": [1, 2, 5, 6],
    "cust_name": ["Moiz2", "Junaid3", "ALi4", "Subhan5"],
}

df1 = pd.DataFrame(cust_df)
df2 = pd.DataFrame(order_df)

df_concate = pd.concat([df1, df2], axis=0, ignore_index=True)
print(df_concate)

# pd.concat() is used to combine DataFrames by stacking them together.
# axis=0 means vertical concatenation, so rows from df2 are added below df1.
# axis=1 means horizontal concatenation, so columns are added side-by-side.
# ignore_index=True creates a fresh continuous index (0, 1, 2, 3...) after concatenation.
# Without ignore_index=True, the original indexes from both DataFrames are preserved.
# Syntax: pd.concat([df1, df2], axis=0 or 1, ignore_index=True or False)
# We commonly use ignore_index=True when combining rows and want a clean new index.
