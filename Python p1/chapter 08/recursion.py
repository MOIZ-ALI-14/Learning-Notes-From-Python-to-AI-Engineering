# A recursive function is a function that repeats itself until a
# stopping condition is met.
# We use recursion when:
# A problem can be broken into smaller similar problems.
# The problem has a clear stopping condition (base case).
# It makes the code shorter and cleaner.


# function definition
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("enter the number to find factorial: "))
print(f"factorial is {factorial(n)}")


# ==========================================
# RECURSION GENERAL GUIDE (FOR ANY PROBLEM)
# ==========================================

# Recursion:
# A function that calls itself to solve a problem.

# --------------------------------------------------
# 1) BASE CASE (Stopping Condition)
# --------------------------------------------------
# Always write a condition that stops the function.
# This prevents infinite recursion.
# Base case handles the smallest possible input.

# Example idea:
# if n == smallest_value:
#     return known_answer


# --------------------------------------------------
# 2) RECURSIVE CASE
# --------------------------------------------------
# The function must call itself.
# It should reduce the problem size.
# Each call should move closer to the base case.

# Example idea:
# return something + function_name(smaller_input)


# --------------------------------------------------
# 3) PROBLEM MUST GET SMALLER
# --------------------------------------------------
# In every recursive call:
# Input must change toward base case.
# If input does not reduce, recursion will never stop.


# --------------------------------------------------
# 4) THINKING TECHNIQUE
# --------------------------------------------------
# Step 1: Identify smallest version of problem.
# Step 2: Assume function works for smaller input.
# Step 3: Use smaller result to build bigger result.


# --------------------------------------------------
# 5) IMPORTANT RULES
# --------------------------------------------------
# - Always write base case first.
# - Recursive call must depend on smaller input.
# - There must be a clear return statement.
# - Every recursive function needs a stopping point.


# --------------------------------------------------
# 6) COMMON MISTAKES
# --------------------------------------------------
# - Forgetting base case.
# - Base case never being reached.
# - Not returning recursive call.
# - Input not decreasing.
# - Infinite recursion error.


# --------------------------------------------------
# 7) SIMPLE STRUCTURE TEMPLATE
# --------------------------------------------------

# def function_name(parameters):
#     # Base Case
#     if stopping_condition:
#         return base_value
#
#     # Recursive Case
#     return function_name(smaller_input)


# --------------------------------------------------
# GOLDEN RULE
# --------------------------------------------------
# Recursion = Base Case + Smaller Problem + Self Call
# Trust the recursive call to solve the smaller part.
