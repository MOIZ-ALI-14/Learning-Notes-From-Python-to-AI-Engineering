# unlike strings, lists are mutable.
# It means that change in list will change the original list

my_data = ["Moiz_Ali", 14, "Computer Science", "UOG", 3.14]
print(my_data)
print(my_data[4])
print(my_data[3:5])
print(type(my_data))

# let's try changing the list
my_data[1] = 999
print(my_data)
