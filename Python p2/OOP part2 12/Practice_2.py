class animals:
    barking = "bow bow"
    pass


class pets(animals):
    pass


class dog(pets):
    def Bark(self):
        print(self.barking)


b = dog()
b.Bark()
