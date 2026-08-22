class school:
    sector = "Government"
    name = "Quaid_e_Azam School"
    Rooms = 33

    def getinfo(self):
        sector="private"
        print(
            f"The sector is {sector} and the rooms in the sector are {self.Rooms}"
        )

    @staticmethod
    def greet():
        print("The End")


JPS = school()
# JPS.sector = "Private"  # this is an object/instance attribute
print(JPS.sector, JPS.Rooms)
JPS.getinfo()
JPS.greet()

# Instance method:
# when we call JPS.getinfo(), Python internally calls school.getinfo(JPS)
# JPS is passed as 'self', so the method works with that object

# Static method:
# when we call JPS.greet(), Python internally calls school.greet()
# no object is passed, because static methods don't use instance data

# 🔥 Simple way to decide

# Ask yourself:

# ❓ Do I need object data?

# YES → use self (instance method)

# NO → use @staticmethod
