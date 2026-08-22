# A set in Python is an unordered and mutable collection of unique elements,
# which means it does not allow duplicate values.
# set items cannot be modified directly because sets are unordered, but items can be added or removed
numbers = {3, 35, 55, 55, 33, 23, 55, "MoizALi"}
print(numbers)
print(type(numbers))

# this will add Fajr in set at any location, i mean not in order and the type will
# still remain set
numbers.add("Fajr")
print(numbers)
print(type(numbers))

# add() adds one element, update() adds multiple elements using a collection
# update() requires brackets because it accepts an iterable (list, tuple, set, etc.)
numbers.update(["Fajr", "duhar", "asar", "maghrib", "isha"])
print(numbers)
print(type(numbers))

# this will print the length of  the set
length = len(numbers)
print(length)

# this will remove the 55 from the set
numbers.remove(55)
print(numbers)

# this will also remove the element but if element doesn't present then it will not raise
# error like remove method
numbers.discard(5555)
print(numbers)

# this will clear the set
numbers.clear()
print(numbers)

# union in sets - commutative
set1 = {2, 4, 55, 65, 34, "mirza"}
set2 = {4, 45, 55, "mirza", 56, 66, 35, 533}
print(set1.union(set2))
print(set2.union(set1))

# intersection in sets - commutative
set1 = {2, 4, 55, 65, 34, "mirza"}
set2 = {4, 45, 55, "mirza", 56, 66, 35, 533}
print(set1.intersection(set2))
print(set2.intersection(set1))

# difference in sets
set1 = {2, 4, 55, 65, 34, "mirza"}
set2 = {4, 45, 55, "mirza", 56, 66, 35, 533}
print(set1.difference(set2))
print(set2.difference(set1))

# symmetric difference in sets
# symmetric_difference returns elements NOT common in both sets
# it is also commutative
set1 = {2, 4, 55, 65, 34, "mirza"}
set2 = {4, 45, 55, "mirza", 56, 66, 35, 533}
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))
