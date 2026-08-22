L = [3, 15, 122, 23, 444, 56, 70, 400]


def divisible(a):
    if a % 5 == 0:
        return True
    return False


newList = filter(divisible, L)
print(list(newList))
