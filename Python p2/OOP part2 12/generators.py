# GENERATORS - COMPLETE REFERENCE
# =================================
# WHAT: Generator is a special function that uses yield instead of return
#       It returns one value at a time and pauses until next value is needed
# WHY:  return stores ALL values in memory at once - crashes on large data
#       yield stores ONE value at a time - memory always safe and empty
# WHEN: Use when working with large datasets or large computations
#       Use when you dont need all values at once - only one at a time
# HOW:  Replace return with yield - use next() or for loop to get values
# IMPORTANT: yield pauses function and waits - resumes when next value asked
#            Generator stores nothing in memory until value is actually needed


# WITHOUT generator - memory problem
def get_numbers_return(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers  # ALL values stored in memory at once - dangerous!


# WITH generator - memory safe
def get_numbers_yield(n):
    for i in range(n):
        yield i  # ONE value at a time - pauses here - waits


# WAY 1 - using next() to get one value at a time
gen = get_numbers_yield(5)
print(next(gen))  # 0 - only this stored in memory
print(next(gen))  # 1 - only this stored in memory

# WAY 2 - using for loop to get all values one by one
for num in get_numbers_yield(5):
    print(num)  # one at a time - memory always safe

# WAY 3 - generator expression - one line version
squares = (x * x for x in range(5))  # () not [] - lazy generator
print(next(squares))  # 0
print(next(squares))  # 1
print(list(squares))  # remaining values

# GENERATOR STATE - IMPORTANT RULE
# ==================================
# Generator always remembers its current position
# It never goes backward - only moves forward
# Once a value is consumed - it is gone forever
# If you stop in middle and call again - it continues from where it stopped
# To start fresh - you must create a new generator object


squares = (x * x for x in range(5))
# generator created - position at start - nothing in memory yet

print(next(squares))  # 0 - position moves to 1 - 0 consumed and gone
# generator paused at position 1 - waiting

print(list(squares))  # [1, 4, 9, 16] - continues from position 1
# 0 is gone forever - list starts from where next() stopped
# generator now exhausted - no values remaining

# TO START FRESH - create new generator
squares = (x * x for x in range(5))  # new generator - position reset to 0
print(list(squares))  # [0, 1, 4, 9, 16] - all values from beginning
