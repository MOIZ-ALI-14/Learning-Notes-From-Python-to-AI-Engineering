# RAISE KEYWORD - COMPLETE REFERENCE
# =====================================
# WHAT: raise is used to manually trigger an error yourself
#       with your own custom message
# WHY:  Sometimes Python does not raise error automatically
#       but YOU know this situation is wrong and should stop
#       raise lets YOU decide when and how error should occur
# WHEN: Use when you want to enforce your own rules and conditions
#       Use when you want to show custom meaningful error messages
#       Use when a value is technically valid but logically wrong
# HOW:  raise ErrorType("your custom message")
#       Write raise inside if condition where you detect the problem
# IMPORTANT - raise is NOT limited to ZeroDivisionError only
#             raise works with ANY error type you choose
#             ZeroDivisionError ValueError Exception
#             You choose error type based on your situation


# IMPORTANT - raise STOPS program completely
# ==========================================
# After raise runs - no code below it executes
# Program crashes at that exact point with your message
# Unless raise is inside try except block - then except catches it
# Without try except - raise crashes whole program
# With try except - raise is caught and program continues normally


# WITHOUT TRY EXCEPT - program crashes completely
first_no = int(input("enter first Number: "))
second_no = int(input("enter second Number: "))

if second_no == 0:
    raise ZeroDivisionError("Ustad g! ki lge o?????, something / 0 ni ho skda.")
    # nothing below this runs - program stopped here
else:
    print(f"division is: {first_no/second_no}")


# WITH TRY EXCEPT - raise is caught - program continues
try:
    first_no = int(input("enter first Number: "))
    second_no = int(input("enter second Number: "))

    if second_no == 0:
        raise ZeroDivisionError("something / 0 ni ho skda.")
        # raise triggers here - jumps to except block

    print(f"division is: {first_no/second_no}")

except ZeroDivisionError as e:
    # raise is caught here - program does not crash
    print(e)

# this runs normally because try except handled the raise
print("program continues normally")


# DIFFERENCE BETWEEN RAISE AND NORMAL ERROR
# ===========================================
# Normal error  - Python raises automatically when something goes wrong
# raise keyword - YOU raise manually with your own custom message
# Normal error  - message is Python default - not meaningful
# raise keyword - message is YOUR own - meaningful and clear


# COMMON ERROR TYPES USED WITH RAISE
# ====================================
# raise is NOT only for ZeroDivisionError
# raise can be used with ANY error type based on your situation
# ZeroDivisionError - when dividing by zero
# ValueError        - when value is wrong type or out of range
# TypeError         - when wrong type is passed
# Exception         - general error for any situation

# EXAMPLES OF RAISE WITH DIFFERENT ERROR TYPES
# raise ValueError("age cannot be negative")
# raise TypeError("only integers allowed here")
# raise Exception("something went wrong in program")
# raise ZeroDivisionError("cannot divide by zero")
