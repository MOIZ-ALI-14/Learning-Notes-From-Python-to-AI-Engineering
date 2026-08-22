# MAP FUNCTION - COMPLETE REFERENCE
# ===================================
# WHAT: map applies a function to every item in a list
# WHY:  Instead of writing loop to apply operation on each item
#       map does it in single line cleanly
# WHEN: Use when you want to apply same operation to all list items
# HOW:  map(function, list) - returns map object - use list() to convert
# IMPORTANT: map returns lazy object - list() needed to see actual results

# map example
L = [3, 3, 4, 5, 5]
square = lambda a: a * a
sqlist = map(square, L)
print(list(sqlist))

# FILTER FUNCTION - COMPLETE REFERENCE
# ======================================
# WHAT: filter keeps only items that return True from function
# WHY:  Instead of writing loop with if condition to filter items
#       filter does it in single line cleanly
# WHEN: Use when you want to keep only specific items from list
# HOW:  filter(function, list) - function must return True or False
# IMPORTANT: filter returns lazy object - list() needed to see results


# filter example
def odd(n):
    if n % 2 == 0:
        return False
    return True


newlist = filter(odd, L)
print(list(newlist))

# REDUCE FUNCTION - COMPLETE REFERENCE
# ======================================
# WHAT: reduce applies function to list items one by one
#       combining them into single final value
# WHY:  Instead of loop to accumulate values reduce does it cleanly
# WHEN: Use when you want to combine all list items into one value
# HOW:  reduce(function, list) - must import from functools first
# IMPORTANT: reduce does NOT need list() - it already returns single value


# reduce example
from functools import reduce

addition = lambda y, z: y + z
added_list = reduce(addition, L)
print(added_list)
