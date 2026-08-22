# checking whether user is eligible of CNIC or not

# These are two separate if statements.
# The first if-else block executes independently and finishes completely.
# After it ends, Python starts executing the second if-elif-else block.
# Both conditions are checked separately because they are not connected.
# If we wanted only one block to run among multiple conditions,
# we would use a single if-elif-else chain instead of two separate if statements.

age = int(input("Please enter your age: "))

# if statement no 1
if age % 2 == 0:
    print("WOW buddy! even age")
else:
    print("Oh! odd age")
# end of 1 if statement


# if statement no 2
if age >= 18:
    print("You are eligible for CNIC!")
    print("Congratulations!")

elif age == 0:
    print("Are you mad? I mean entering 0 age")

elif age < 0:
    print("how can age be negative?")

else:
    print("You are not eligible for CNIC!")
# end of 2 if statement

print("End of Program")
