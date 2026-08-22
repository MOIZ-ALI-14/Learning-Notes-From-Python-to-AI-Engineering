class twoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"This is 2D_vector: {self.i}i + {self.j}j")


class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"This is 3D_vector: {self.i}i + {self.j}j + {self.k}k")


twoD = twoDvector(2, 4)
threeD = threeDvector(4, 5, 6)
twoD.show()
threeD.show()
