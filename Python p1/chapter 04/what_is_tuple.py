# A tuple is a collection of items like a list, but once
# created it cannot be changed, just like a string, as
# it is also immutable like string.

my_data = (1, "moiz", "junaid", 14, False, "shoaib")
print(my_data)
print(my_data[3])
print(my_data[2:4])
print(type(my_data))

# let's try changing the list as it will fail because tuple is immutable
my_data[1] = 999
print(my_data)

