# sum of first n natural numbers using function
def sum_n_numbers(n):
    if n == 1:
        return 1
    return n + sum_n_numbers(n - 1)


user_desire = int(input("enter the number: "))
SUM = sum_n_numbers(user_desire)
print(f"sum of first {user_desire} no's is {SUM}")
