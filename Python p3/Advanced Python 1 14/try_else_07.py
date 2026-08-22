# TRY EXCEPT ELSE - COMPLETE REFERENCE
# ======================================
# WHAT: else block runs only when try was completely successful
# WHY:  Separate success code from risky code cleanly
# WHEN: Use when you want to run code only if no error occurred
# IMPORTANT: else never runs if except block ran

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError as e:
    print("Please enter a number!")
    print(e)

except ZeroDivisionError as e:
    print("Cannot divide by zero!")
    print(e)

else:
    # runs ONLY when try was completely successful
    print(f"Result is: {result}")
    print("Everything went well!")

print("Program continues normally")
