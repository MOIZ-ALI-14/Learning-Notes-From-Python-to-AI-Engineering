# function definition
def greatestno(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


# function call
TheGreatestNumber = greatestno(23, 4, 3)
print(TheGreatestNumber)
