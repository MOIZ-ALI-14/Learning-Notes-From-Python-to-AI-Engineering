class school:
    sector = "Government"
    name = "Quaid_e_Azam School"
    Rooms = 33

    def getinfo(self):
        print(
            f"The sector is {self.sector} and the rooms in the sector are {self.Rooms}"
        )

    def greet(self):
        print(f"The End {self.name}")


JPS = school()
JPS.sector = "Private"  # this is an object/instance attribute
JPS.name="Mirza G ka School"
print(JPS.sector, JPS.Rooms)
JPS.getinfo()
JPS.greet()

# when we call JPS.getinfo(), Python internally calls school.getinfo(JPS)
# here, JPS is passed as an argument and received as 'self'
# this ensures the method works with the JPS object

# 👉 self is just a reference to the current object
# 👉 It allows methods to work with that specific object’s data
