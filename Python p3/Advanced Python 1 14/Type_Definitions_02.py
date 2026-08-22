# TYPE HINTS - COMPLETE REFERENCE
# =================================
# WHAT: Type hints tell what type of value a variable or function expects
# WHY:  Makes code readable for programmer and team members
#       IDE like VS Code shows warnings if wrong type is passed
#       Professional standard in real jobs and projects
# WHEN: Use in functions and variables when working in teams
#       or when you want your code to be clean and readable
# IMPORTANT: Python COMPLETELY ignores type hints at runtime
#            They are just like comments - only for readability
#            Wrong type can still be passed - no error will occur


# VARIABLE TYPE HINTS
# ====================

name: str = "Moiz"
# str means this variable should store a string text

age: int = 20
# int means this variable should store a whole number

marks: float = 95.5
# float means this variable should store a decimal number

is_student: bool = True
# bool means this variable should store True or False only

students: list = ["Moiz", "Ali", "Ahmed"]
# list means this variable should store a list of items

data: dict = {"name": "Moiz", "age": 20}
# dict means this variable should store key value pairs


# FUNCTION TYPE HINTS
# ====================


# a: int means a should be integer
# b: int means b should be integer
# -> int means function will return integer
def add(a: int, b: int) -> int:
    return a + b


# name: str means name should be string
# -> str means function will return string
def greet(name: str) -> str:
    return f"Hello {name}"


# age: int means age should be integer
# -> bool means function will return True or False
def is_adult(age: int) -> bool:
    return age >= 18


# -> None means function returns nothing
def show_info(name: str, age: int) -> None:
    print(f"Name: {name} Age: {age}")


# marks: float means marks should be decimal number
# -> str means function will return string
def get_grade(marks: float) -> str:
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    else:
        return "C"


# PROOF THAT PYTHON IGNORES TYPE HINTS AT RUNTIME
# =================================================
add("Moiz", "Ali")  # works! returns MoizAli - no error
add(5.5, 2.2)  # works! returns 7.7 - no error
# type hints did NOT stop wrong types
# they only showed warning in VS Code

# TYPING MODULE - COMPLETE REFERENCE
# ====================================
# WHAT: typing module gives more powerful and specific type hints
# WHY:  Basic types like list and dict do not tell what is INSIDE them
#       typing module lets you specify exactly what is inside
# WHEN: Use when you want to be more specific about types
#       especially when working with lists tuples and multiple types
# HOW:  from typing import List, Tuple, Union, Optional, Dict


from typing import List, Tuple, Union, Optional, Dict


# LIST
# =====
# Basic list does not tell what is inside
numbers: list = [1, 2, 3]  # we do not know what is inside

# List from typing tells exactly what is inside
numbers: List[int] = [1, 2, 3]  # now we know - integers inside
names: List[str] = ["Moiz", "Ali"]  # strings inside
marks: List[float] = [95.5, 88.2]  # floats inside


# TUPLE
# ======
# Tuple from typing tells exactly what each position contains
# Tuple is like list but fixed size and cannot be changed
person: Tuple[str, int] = ("Moiz", 20)
# position 0 must be string - name
# position 1 must be integer - age

student: Tuple[str, int, float] = ("Moiz", 20, 95.5)
# position 0 - string - name
# position 1 - integer - age
# position 2 - float - marks


# UNION
# ======
# WHAT: Union means variable can be MORE THAN ONE type
# WHY:  Sometimes a variable can accept both int and string
# WHEN: Use when a value can be two or more different types
def show_id(user_id: Union[int, str]) -> None:
    print(f"User ID is {user_id}")


show_id(123)  # works - integer
show_id("ABC123")  # works - string
# Union[int, str] means accept both int and string


# OPTIONAL
# =========
# WHAT: Optional means value can be a type OR None
# WHY:  Sometimes a value may exist or may not exist
# WHEN: Use when a parameter or variable can be empty or None
def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello Guest"
    return f"Hello {name}"


greet("Moiz")  # Hello Moiz
greet()  # Hello Guest - name is None
# Optional[str] means value is either string or None


# DICT
# =====
# Basic dict does not tell what keys and values are inside
data: dict = {"name": "Moiz"}  # we do not know types

# Dict from typing tells exactly what keys and values are
data: Dict[str, int] = {"age": 20}  # key is string value is int
scores: Dict[str, float] = {"math": 95.5, "english": 88.2}
# key must be string - subject name
# value must be float - marks


# REAL WORLD FUNCTION EXAMPLE USING ALL TOGETHER
# ================================================
def student_info(
    name: str,  # must be string
    age: int,  # must be integer
    marks: List[float],  # list of decimal marks
    grade: Union[str, int],  # can be A or 1
    address: Optional[str] = None,  # can be empty
) -> Dict[str, Union[str, int, float]]:  # returns dictionary
    return {
        "name": name,
        "age": age,
        "marks": marks,
        "grade": grade,
        "address": address,
    }


print(student_info("moiz", 89, [3, 4, 4, 4, 4], "A", "Gujrat"))

# SUMMARY TABLE
# ==============
# List[int]         - list that contains integers
# List[str]         - list that contains strings
# Tuple[str, int]   - tuple with string at 0 and int at 1
# Union[int, str]   - accepts both integer and string
# Optional[str]     - accepts string or None
# Dict[str, int]    - dictionary with string keys and int values
