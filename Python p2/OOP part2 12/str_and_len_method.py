# __str__ METHOD
# Controls what you SEE when you print an object
# Without __str__ printing object shows ugly memory address
# With __str__ you can show clean readable information of object
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}"


s1 = student("Moiz", "20")
print(s1)


# __len__ METHOD
# Controls what len() returns when used on your object
# Must always return a number never a string
# Use when you want to count something inside your object
class student_data:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        return len(self.name)


s2 = student_data(["Moiz", "Shoaib", "Junaid", "Brands"])
print(len(s2))
