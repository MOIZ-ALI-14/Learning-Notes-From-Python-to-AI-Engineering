# This function uses a default parameter.
# A default parameter means the function already has a value stored
#  for that argument.
# The default value is used only when we do NOT pass that argument
# in the function call.
# If we pass a value in the function call, the default value will
# not be used,
# and the new value will replace it.


# function definition
def message(name, ending="Stay Calm"):
    print(f"Dear {name} \nHow are you? \n{ending}")


# function call
message("Moiz", "Be Strong Mirza")
message("Junaid")
message("Shoaib")
