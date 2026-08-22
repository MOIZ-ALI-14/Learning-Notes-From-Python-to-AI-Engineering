def printno(n):
    if n == 0:
        return
    printno(n - 1)
    print(n)


printno(5)
