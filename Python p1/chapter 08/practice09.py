def reverse_counting(n):
    if n==0:
        return
    print(n)
    reverse_counting(n-1)

reverse_counting(4)