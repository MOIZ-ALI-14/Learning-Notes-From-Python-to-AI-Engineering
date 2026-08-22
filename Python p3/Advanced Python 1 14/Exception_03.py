# TRY EXCEPT - COMPLETE REFERENCE
# =================================
# WHAT: try except handles errors without crashing the program
# WHY:  When user gives wrong input or unexpected error occurs
#       without try except whole program crashes and stops
#       with try except program handles error and continues normally
# WHEN: Use when you have doubt that a part of code may crash
#       especially when taking input from user
# HOW:  Put risky code in try block
#       handle specific errors in except blocks
#       code after except always runs normally as usual


# IMPORTANT ORDER RULE
# =====================
# specific exceptions always FIRST
# general Exception always LAST
# if Exception is first it catches everything
# and specific exceptions like ValueError never run


# VALUEERROR
# ===========
# Use when user enters wrong TYPE of value
# Most common - when converting string to int or float fails
# int("hello") - ValueError
# int("12.5")  - ValueError
# float("abc") - ValueError

# EXCEPTION
# ==========
# Use to catch ANY other unexpected error
# ZeroDivisionError - dividing by zero
# FileNotFoundError - file does not exist
# IndexError        - list index out of range
# KeyError          - dictionary key not found
# TypeError         - wrong type operation
# NameError         - variable not defined

try:
    number = int(input("Enter a number: "))
    result = number / 0
    print(result)

except ValueError as e:
    print("!!!! string is not allowed !!!!!")

except Exception as e:
    print("Unexpected error")

print("Thank You")
