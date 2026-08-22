# A set in Python is an unordered and mutable collection of unique elements,
# which means it does not allow duplicate values.
# set items cannot be modified directly because sets are unordered, but items can be added or removed
numbers = {3, 35, 35, 55, 55, 33, 23, 55}
print(numbers)

# how to make empty set
s = set()  # note that don't make empty set as set={} as it will create empty dictionary
print(type(s))
