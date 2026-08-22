# The return keyword sends the result of a function back to the caller
# and ends the function execution.
# every statement inside a function will be ignored after return
# We use return when:
# We want the function to give us a result
# We want to store that result in a variable
# We want to use that result later in the program


# function without return
def add(a, b):
    result = a + b
    print(result)


x = add(5, 3)
print(x)


# function with return
def add(a, b):
    result = a + b
    return result


r = add(5, 5)
print(r)
