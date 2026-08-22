# This code will raise an error:
# TypeError: unhashable type: 'list'
# Reason:
# Sets can only contain immutable elements (like int, float, string, tuple).
# Lists (or dictionaries) cannot be added directly to a set.
# The update() method works fine with an iterable of immutable elements, 
# but the set cannot contain a list inside it.
# in fact set is mutable by itself as we can add and remove items in the original set

s = {3, 35, 322, "moiz", [3, 53, 355]}
s.update([3, 53, 5555])
print(s)
 