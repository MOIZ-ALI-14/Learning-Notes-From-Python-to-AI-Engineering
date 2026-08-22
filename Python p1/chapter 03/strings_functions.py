# Strings are immutable in Python, so any change creates a new string, not the original one.

my_name = "moiz is first name and surname is Ali"

# length of string
print(len(my_name))

# change case functions
print(my_name.capitalize())  # makes first letter capital
print(my_name.endswith("Ali"))  # checks if string ends with "Ali"
print(my_name.startswith("Moiz"))  # checks if string starts with "Moiz"
print(my_name.upper())  # converts all letters to uppercase
print(my_name.lower())  # converts all letters to lowercase
print(my_name.title())  # makes first letter of each word capital
print(my_name.swapcase())  # swaps upper case to lower and lower to upper

# string with extra spaces
my_name = "    moiz is first name and surname is Ali     "

# strip functions (remove spaces from sides only)
print(my_name.strip())  # removes spaces from both left and right
print(my_name.lstrip())  # removes spaces from left side only
print(my_name.rstrip())  # removes spaces from right side only

# find, index, count
print(my_name.find("moiz"))  # returns index, -1 if not found
print(my_name.index("moiz"))  # returns index error if not found
print(my_name.count("moiz"))  # counts how many times word appears

# replace() creates a new string, original string stays same
text = "I like Java Java"
print(text.replace("Java", "Python"))  # replaces Java with Python
print(text.replace("I", "We"))  # replaces I with We

# CHECK TYPE OF STRING CONTENT
print(my_name.isalpha())
# False because space is not a letter
print(my_name.isalnum())
# False because _ is not letter or number
print(my_name.isdigit())
# False because letters are present
print(my_name.isupper())
# False because letters are not all uppercase
print(my_name.islower())
# False because letters are not all lowercase

# split and join
data = "my name is Moiz Ali"
print(data.split(" "))
# splits string by spaces
print(data.split("is"))
# splits string using word "is"
print(data.split("Ali"))
# splits string using word "Ali"
data = "a,b,c,d"
print(data.split(","))
# splits string using comma
data = "2026-02-06"
print(data.split("-"))
# splits string using dash
text = "this is his list"
print(text.split("is"))
# splits string using is
words = ["my", "name", "is", "Moiz"]
print(" ".join(words))
# joins list into string with space
print("-".join(words))
# joins list into string with dash
print("*".join(words))
# joins list into string with *


