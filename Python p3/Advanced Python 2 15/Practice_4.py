from functools import reduce

L = [3, 15, 1322, 23, 401, 56, 70, 400]


def maxCheck(a, b):
    if a > b:
        return a
    return b


maximumNo = reduce(maxCheck, L)
print(maximumNo)
