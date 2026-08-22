# checking whether user is eligible of CNIC or not

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible for CNIC!")
    print("Congratulations!")

elif age == 0:
    print("Are you mad? I mean entering 0 age")

elif age < 0:
    print("how can age be negative?")

else:
    print("You are not eligible for CNIC!")

print("End of Program")
