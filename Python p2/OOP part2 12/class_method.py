class bank:
    total_account = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        bank.total_account += 1

    @classmethod
    def show_total(cls):
        print(f"Total accounts are: {cls.total_account}")


acc1 = bank("Moiz", "450000")
acc2 = bank("ALi", "403030")
acc3 = bank("Shabi", "434000")
acc4 = bank("Jaidi", "330000")

bank.show_total()

# CLASS METHOD - COMPLETE REFERENCE
# ==================================
# Class method belongs to the WHOLE CLASS - not any specific object
# Use when the work is related to class itself - not individual objects
# Decorator @classmethod must be written above the method
# First parameter is always cls - not self
# cls means the class itself - just like self means the object
# Call using CLASS NAME directly - no object needed
