# instead of doing this
# def multiply(a,b):
#     return a*b
# print(multiply(2,3))

# we can also do this
multiply = lambda a, b: a * b
print(multiply(2, 4))

# similarly
addition = lambda a, b, c: a + b + c
print(addition(3, 3, 4))


# LAMBDA FUNCTION - COMPLETE REFERENCE
# ======================================
# WHAT: Lambda is a small anonymous function written in single line
# WHY:  When function is simple and used only once or twice
#       writing full def function is unnecessary and lengthy
# WHEN: Use when function has simple single expression to return
#       Use when you need quick short function without naming it formally
# HOW:  lambda parameters: expression
# IMPORTANT: Lambda can take many parameters but only one expression
#            Lambda automatically returns result - no return keyword needed
