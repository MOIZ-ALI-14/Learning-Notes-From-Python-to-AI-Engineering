prices = [100, 200, 300]
discount = 10  # 10% is discount for each item
final_prices = []
for price in prices:
    final_price = price - price * discount / 100
    final_prices.append(final_price)

print(final_prices)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# in the upper example we we calculted prices after discount
# with the help of loops that is ok for small data but in large
# datasets these loops are not best choice because they can be
# slowed down there that is why we use Broadcasting that is provided
# by numpy is helpful in working with large datasets.

# With Broadcasting:
# --> we get rid of loops
# --> mathematical operations are performed at much faster speed

# Actual Definition of Broadcastion:

# Broadcasting allows NumPy to perform operations between arrays of
# compatible shapes by automatically applying the smaller data or array
# to the larger array.
