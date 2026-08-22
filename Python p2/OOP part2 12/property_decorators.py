# PROPERTY DECORATOR - COMPLETE REFERENCE
# =========================================
# WHAT: Property decorator is a way to protect and control
#       the data stored in your class
# WHY:  Without it anyone can change your data directly
#       with invalid values and no one stops them
# WHEN: Use it when you want to validate and protect
#       an attribute from invalid values
# HOW:  Three steps - private variable + getter + setter

#                Encapsulation

# 🟢 Public variable
# Public variables are accessible from anywhere in the program.
# They use the normal name, without _ or __.
# They can be directly accessed and modified.
# Use them when no special access restriction is needed.
# 🟡 Protected variable
# Protected variables use a single underscore, like _age.
# Python treats this mainly as a developer convention, not strict protection.
# They are intended for use inside the class and its subclasses.
# Outside access is possible, but generally discouraged.
# 🔴 Private variable
# Private variables use double underscores, like __age.
# Python applies name mangling to make direct external access harder.
# They are intended to be controlled through methods or @property.
# This is commonly used when you want encapsulation and controlled access.


class Student:

    def __init__(self, name, marks):
        self.name = name
        # STEP 1: Always create empty private box first
        # __ makes it private - only accessible inside class
        # Outside class cannot touch self.__marks directly
        self.__marks = 0
        # STEP 2: Send to setter for validation from beginning
        # self.marks calls setter - not self.__marks
        # If you write self.__marks = marks it bypasses setter
        self.marks = marks

    # STEP 3: GETTER - @property
    # Controls HOW data is READ from outside
    # Outside writes s1.marks - getter runs automatically
    # IMPORTANT: Always return self.__marks not self.marks
    # If you return self.marks - infinite loop - crash!
    # self.marks calls getter again - forever loop
    @property
    def marks(self):
        return self.__marks

    # STEP 4: SETTER - @marks.setter
    # Name must be SAME as property name above
    # Controls HOW data is CHANGED from outside
    # Outside writes s1.marks = 75 - setter runs automatically
    # value parameter receives whatever is on right side of =
    # IMPORTANT: Store in self.__marks not self.marks
    # If you write self.marks = value - infinite loop - crash!
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Enter marks between 0 and 100!")
        else:
            # Only valid value reaches here and gets stored
            # self.__marks is the actual locked box
            self.__marks = value

    # Another property - result has no concern with marks property
    # It directly reads self.__marks from locked box
    # No setter needed - result cannot be changed manually
    @property
    def result(self):
        if self.__marks < 40:
            return "Fail"
        else:
            return "Pass"


s1 = Student("Moiz", 75)
print(s1.marks)  # getter runs - returns self.__marks
print(s1.result)  # reads self.__marks directly

s1.marks = 34  # setter runs - rejected - self.__marks unchanged
print(s1.result)

# RULES TO REMEMBER FOREVER:
# 1. Always use __ to make attribute private
# 2. Always use self.__marks inside getter and setter
# 3. Never use self.marks inside getter or setter - infinite loop!
# 4. Property name, setter name, function names must all be SAME
# 5. In __init__ use self.marks = marks not self.__marks = marks
# 6. Outside class always use s1.marks never s1.__marks
