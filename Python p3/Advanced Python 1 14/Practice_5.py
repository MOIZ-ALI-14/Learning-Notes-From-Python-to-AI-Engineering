number = int(input("Enter a number:"))
table = [number * item for item in range(1, 11)]
print(table)
with open("Advanced Python 1 14/Practice_5.txt", "a") as f:
    f.write(f"Table of {number}: {str(table)}\n")
print(f"Table of {number} has been written to Practice_5.txt")
