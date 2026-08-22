class school:
    sector = "Government"
    name = "Quaid_e_Azam School"  # this is a class attribute
    Rooms = 33


JPS = school()
JPS.name = "Jinnah Public School"  # this is an object/instance attribute
print(JPS.name, JPS.sector, JPS.Rooms)

# object/instance attribute has preferences over class attribute
