# Complex class represents a complex number with real and imaginary parts.
# In __add__ method, we use 'Complex' because it is the class name and
# we must return a new Complex object — not just a number. This is important
# because when we add two complex numbers, the result must also be a
# Complex object. The __add__ method never changes c1 or c2 — it always
# creates a brand new third object with the added values. The __str__ method
# is must because without it Python cannot print our custom object in a
# readable way — it would print a memory address instead. These dunder
# (double underscore) methods like __add__ and __str__ are called
# automatically by Python — __add__ runs when we use + operator and
# __str__ runs when we use print().

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(3, 2)
c2 = Complex(5, 4)
print(c1 + c2)
