# Use a for loop when the number of iterations is known 
# or when looping over a sequence (list, tuple, string, range).


# This will print numbers from 0 to 4 (5 is excluded because range stops before the end value)
for i in range(0, 5):
    print(i)

# This will print numbers from 0 to 45 with a step (jump) of 5
# 50 is excluded, so last printed value is 45
for i in range(0, 50, 5):
    print(i)

# For loop iterating over a list (prints each element one by one)
data = ["moiz", "junaid", "shabi"]
for i in data:
    print(i)

# For loop iterating over a tuple
data = (3, 54, 55, "moiz")
for i in data:
    print(i)

# For loop iterating over a string (prints each character separately)
data = "MySelfMoiz"
for i in data:
    print(i)
