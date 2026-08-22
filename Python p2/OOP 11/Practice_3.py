class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def sqroot(self):
        print(f"The square root is {1/2**self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    @staticmethod
    def greet():
        print("THE END")


task = calculator(7)
task.cube()
task.sqroot()
task.square()
task.greet()
