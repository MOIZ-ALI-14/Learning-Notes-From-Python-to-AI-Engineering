from random import randint


class train:
    def __init__(self, trainno, fro, to):
        self.trainno = trainno
        self.fro=fro
        self.to=to
    def book(self):
        print(f"Ticket is booked of {self.trainno} from {self.fro} to {self.to}")

    def getstatus(self):
        print(f"Train no {self.trainno} is running on the time")

    def getfare(self,too):
        print(
            f"Ticket fare in train no:{self.trainno} from {self.fro} to {too} is {randint(1111,3434)} "
        )


t = train(10101,"karach","Gujrat")
t.book()
t.getstatus()
t.getfare("lahore")
