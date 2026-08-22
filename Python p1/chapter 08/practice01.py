# finding average of marks of 10 students using function


# function definition
def average():
    sub1 = int(input("enter math's marks: "))
    sub2 = int(input("enter computer's marks: "))
    sub3 = int(input("enter physics's marks: "))

    average = (sub1 + sub2 + sub3) / 3
    print(f"Your average is {average}")


# function call
for i in range(1, 11):
    print(f"Enter the marks of student {i}")
    average()
