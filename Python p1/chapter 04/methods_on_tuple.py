# A tuple is a collection of items like a list, but once
# created it cannot be changed, just like a string, as
# it is also immutable like string.

my_data = (1, "shabi", "moiz", "junaid", 14, False, "shoaib", 14, "moiz")
print(my_data)

# it will count that how many times 14 appears in the tuple
print(my_data.count(14))

# it will give the index of first occurance of moiz in the tuple
print(my_data.index("moiz"))

# it will tell the length of the tuple
print(len(my_data))

# indexing and slicing
print(my_data[0])
print(my_data[1:3])

# nested tuples
t = ((1, 2), (3, 4), (7, 8))
print(t[2][1])

# it will min, max, and the sum in the tuple
t = (5, 10, 15)
print(min(t))
print(max(t))
print(sum(t))

# tuple unpacking
my_data = (1, "shabi", "moiz", "junaid", 14, False, "shoaib", 14, "moiz")
a, b, c, d, e, f, g, h, i = my_data
print(e, f)

# tuple unpacking using * it take tuple elements that has been remained between
my_data = (1, "shabi", "moiz", "junaid", 14, False, "shoaib", 14, "moiz")
a, b, *c, g, h, i = my_data
print(c)

# in — checks if an item exists
my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)  # True

# not in — checks if an item does NOT exist
my_tuple = ("apple", "banana", "cherry")
print("banana" not in my_tuple)  # False
