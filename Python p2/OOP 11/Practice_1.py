class programmer:
    Company = "Microsoft"

    def __init__(self, name, income, pincode):
        self.name = name
        self.income = income
        self.pincode = pincode


p1 = programmer("Moiz", "6000000", "45343")
print(p1.name, p1.income, p1.pincode, p1.Company)
p2 = programmer("Junaid", "9000000", "32432")
print(p2.name, p2.income, p2.pincode, p2.Company)
