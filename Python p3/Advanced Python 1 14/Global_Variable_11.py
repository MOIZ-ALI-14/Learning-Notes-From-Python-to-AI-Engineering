# GLOBAL VARIABLE - COMPLETE REFERENCE
# ======================================
# WHAT: A variable defined at top of program outside all functions
#       accessible from every function and every part of program
# WHY:  When you need same variable to be shared across all functions
# WHEN: Use when a value needs to be accessed or changed everywhere
# IMPORTANT: Reading global variable inside function needs no keyword
#            Changing global variable inside function needs global keyword
#            Without global keyword - change is local to that function only
#            With global keyword - change affects whole program permanently


a = 1  # global variable - accessible everywhere


def change_local():
    a = 3  # local only - new variable inside function
    print(a)  # 3 - local value
    # global a is still 1 - not changed


def change_global():
    global a  # tell Python - use and change the global a
    a = 3  # now global a is changed for whole program
    print(a)  # 3 - global value changed


change_local()  # 3
print(a)  # 1 - global unchanged

change_global()  # 3
print(a)  # 3 - global changed permanently
