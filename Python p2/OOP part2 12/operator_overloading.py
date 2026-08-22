# OPERATOR OVERLOADING - COMPLETE REFERENCE
# ==========================================
# WHAT: Giving extra meaning to operators like + - * >
#       for your own classes
# WHY:  Python does not know how to use operators on your objects
#       You have to teach Python what + or - means for your objects
# WHEN: Use when you want to perform operations between two objects
# HOW:  Use special methods like __add__ __sub__ __mul__ __gt__ __lt__


class student:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        return self.a + b.a

    def __sub__(self, b):
        return self.a - b.a

    def __mul__(self, b):
        return self.a * b.a

    def __gt__(self, b):
        return self.a > b.a

    def __lt__(self, b):
        return self.a < b.a


s1 = student(45)
s2 = student(55)
print(s1 + s2)
print(s1 - s2)
print(s1 * s2)
print(s1 > s2)
print(s1 < s2)
