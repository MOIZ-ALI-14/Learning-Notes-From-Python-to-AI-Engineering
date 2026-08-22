try:
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("INFINITE")
print("The End")
