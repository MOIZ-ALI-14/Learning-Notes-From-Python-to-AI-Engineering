# Constructor (__init__):
# It is a special method that runs automatically when an object is created

# Why we use constructor:
# To initialize (assign) values to object variables at the time of creation

# When we use constructor:
# When we want every object to start with some initial data automatically


class school:
    def __init__(self, name, sector, rooms):
        self.name = name
        self.sector = sector
        self.rooms = rooms
        print("i am a constructor")


JPS = school("Jinnah Public School", "Government", "50")
print(JPS.name, JPS.sector, JPS.rooms)
