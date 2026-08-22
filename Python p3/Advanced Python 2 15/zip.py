# Definition: zip() combines elements from two or more iterables position by position.
# zip() pairs corresponding elements from multiple iterables.
# The first elements are paired, then the second, then the third, and so on.
# zip() returns a zip object (iterator), so we commonly use list() to see its contents.
# If the iterables have different lengths, zip() stops at the shortest iterable.
# It is commonly used for processing related data together, such as names with ages or products with prices.
# 🧠 Memory trick: zip() = pair things by position.

names = ["Ali", "Sara", "John"]
ages = [18, 19, 20]

result = zip(names, ages)

print(list(result))


products = ["Laptop", "Mouse", "Keyboard", "pad"]
prices = [80000, 2000, 5000, 300]

for product, price in zip(products, prices):
    print(product, price)
