class school:
    sector = "Government"  # this is a class attribute
    Rooms = 33


JPS = school()
JPS.name = "Jinnah Public School"  # this is an object/instance attribute
print(JPS.name, JPS.sector, JPS.Rooms)

APS = school()
APS.name = "Jinnah Public School"  # this is an object/instance attribute
print(APS.name, APS.sector, APS.Rooms)

# here name is an object/instance attribute and sector and Rooms are
# class attributes as they directly belong to class
