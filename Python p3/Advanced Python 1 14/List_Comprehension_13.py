# List comprehension provides a shorter and more readable way to create lists

# It replaces the need for writing a full for-loop with append()

# A new list is created based on an existing iterable (like myList)

# This method improves code readability and reduces lines of code

# Even if we reuse the same variable name, a new list is created and assigned

# To prevent this
# myList = [2, 4, 5, 2, 7, 7, 8, 9]
# newList = []
# for item in myList:
#     newList.append(item * item)
# print(newList)

# we do this
myList = [2, 4, 5, 2, 7, 7, 8, 9]
newList = [item * item for item in myList]
print(newList)
