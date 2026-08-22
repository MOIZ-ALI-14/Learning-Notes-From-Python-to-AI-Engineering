class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, other):
        return vector(self.i + other.i, self.j + other.j, self.k + other.k)

    def __mul__(self, other):
        return f"Dot Product: {self.i * other.i + self.j * other.j + self.k * other.k}"

    def __str__(self):
        return f"The sum is: {self.i}i + {self.j}j + {self.k}k"


v1 = vector(3, 5, 6)
v2 = vector(3, 6, 3)
print(v1 + v2)
print(v1 * v2)
