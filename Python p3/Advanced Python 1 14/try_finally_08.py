# FINALLY - COMPLETE REFERENCE
# ==============================
# WHAT: finally block ALWAYS runs no matter what happens
# WHY:  Normal code after except does NOT run when return or raise exits
#       finally runs even when return or raise would skip everything
# WHEN: Use when you have cleanup code that MUST run no matter what
#       closing files closing database connections releasing resources
# IMPORTANT: finally runs even before return exits the function
#            finally runs even when raise crashes the program
#            finally is the only block guaranteed to always execute


# EXAMPLE 1 - finally with return
# ================================
# return tries to exit function immediately
# but finally still runs BEFORE return exits
def divide(a, b):
    try:
        result = a / b
        return result  # tries to exit here
    except ZeroDivisionError as e:
        return "cannot divide"  # or exits here
    finally:
        # runs BEFORE return exits - guaranteed
        print("finally ran before return!")


print(divide(10, 2))
# output:
# finally ran before return!
# 5.0

print(divide(10, 0))
# output:
# finally ran before return!
# cannot divide
