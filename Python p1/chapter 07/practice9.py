# drawing pattern when n=6
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

for i in range(1, 7):
    print(" " * (6 - i), end="")
    print("*" * (2 * i - 1))

# but if we want the user tell us the size of pyramid
n = int(input("enter the number:"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
