# Strings are immutable in Python, so any change creates a new string, not modifies the original one.


My_name = "Mirza Moiz Ali"
my_new_name = My_name[
    6:14
]  # it will print all chars from index 6 to all the way till 14 buy excluding 14
print(my_new_name)

# for printing just one char
My_name = "Mirza Moiz Ali"
nickname = My_name[6]
print(nickname)

# negative slicing
My_name = "Mirza Moiz Ali"
negative_name = My_name[
    -8:-2
]  # negative slicing starts from right side from -1,-2,......   and here it will print -2 to all the way till -8 but excluding -2
print(negative_name)

# skip value
alphabets = "abcdefghijklmnopqrstuvwxyz"
new_letters = alphabets[
    7:21:4
]  # this will take 7 char to all the way till 21 but excluding 21 and will print all the chars on the 4 step
print(new_letters)
