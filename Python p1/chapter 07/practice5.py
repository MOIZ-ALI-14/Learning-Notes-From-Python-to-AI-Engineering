number = int(input("enter a number Please to check whether it is prime or not: " ""))
if number < 2:
    print("this can't be prime no")
    exit()
for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not a prime no")
        break
else:
    print(f"{number} is a prime no")
