# unlike strings, lists are mutable.
# It means that change in list will change the original list

my_data = ["Moiz_Ali", 14, "Computer Science", "UOG", 3.14]
print(my_data)

# it will add fajr at the end of the list
my_data.append("fajr")
print(my_data)

# it will reverse the list
my_marks = [81, 83, 75, 82, 44]
my_marks.reverse()
print(my_marks)

# it will sort the list
my_marks = [81, 83, 75, 82, 44]
my_marks.sort()
print(my_marks)

# it will insert 99 at 3rd index
my_marks = [81, 83, 75, 82, 44]
my_marks.insert(3, 99)
print(my_marks)

# it will remove 75 in the list and doesn't return the deleted value
my_marks = [81, 83, 75, 82, 44]
my_marks.remove(75)
print(my_marks)

# it will remove the value at index 2 in the list and returns as well the deleted value
my_marks = [81, 83, 75, 82, 44]
print(my_marks.pop(2))
print(my_marks)

# in — checks if an item exists
my_list = [1, 2, 3, 4]
print(2 in my_list)  # True
print(5 in my_list)  # False

# not in — checks if an item does NOT exist
my_list = [1, 2, 3, 4]
print(5 not in my_list)  # True
print(2 not in my_list)  # False
