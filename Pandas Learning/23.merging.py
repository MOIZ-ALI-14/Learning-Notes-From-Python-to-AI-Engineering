import pandas as pd

# For Customer name
cust_df = {"cust_id": [1, 2, 3, 8], "cust_name": ["Moiz", "Junaid", "ALi", "Subhan"]}

# For Orderamount
order_df = {"cust_id": [1, 2, 5, 6], "order_amount": [23, 34, 55, 53]}

df1 = pd.DataFrame(cust_df)
df2 = pd.DataFrame(order_df)

df_final = pd.merge(df1, df2, on="cust_id", how="outer")
print(df_final)

# pd.merge() is used to join two DataFrames using a common column or key.
# Syntax: pd.merge(df1, df2, on="common_column", how="join_type")
# Here, "cust_id" is the common column used to connect customers with their orders.
#
# INNER JOIN → keeps only rows where the key exists in BOTH DataFrames.
# Example: cust_id 1 and 2 exist in both, so only those customers appear.
# Real life: find customers who actually have matching orders in the order table.
#
# OUTER JOIN → keeps ALL rows from BOTH DataFrames.
# If a key exists on only one side, Pandas fills the missing information with NaN.
# Here, customers 3 and 8 have no matching order, while orders 5 and 6 have no matching customer.
# Real life: compare two complete datasets and find both matching and missing records.
#
# LEFT JOIN → keeps ALL rows from the LEFT DataFrame (df1).
# Matching information from the RIGHT DataFrame (df2) is added when available; otherwise NaN appears.
# Real life: show every customer and their order information, even customers who have never ordered.
#
# RIGHT JOIN → keeps ALL rows from the RIGHT DataFrame (df2).
# Matching information from the LEFT DataFrame is added when available; otherwise NaN appears.
# Real life: show every order and find which orders have matching customer information.
#
# CROSS JOIN → creates every possible combination between the two DataFrames.
# It does NOT match using a common column, so do not use on="cust_id" with how="cross".
# Example: 4 customers × 4 orders = 16 combinations.
# Real life: create every possible combination, such as every product with every available size.
#
# IMPORTANT: "on=" tells Pandas which common column to use for matching.
# "how=" tells Pandas which type of join to perform: inner, outer, left, right, or cross.
# For cross join, use pd.merge(df1, df2, how="cross") without on=.
