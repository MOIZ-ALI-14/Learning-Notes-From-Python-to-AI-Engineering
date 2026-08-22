class person:
    def __init__(self, name, contact, age):
        self.name = name
        self.contact = contact
        self.age = age

    def getinfo(self):
        print(
            f"My name is {self.name} and age is {self.age} and my contact is {self.contact}"
        )


class teacher(person):
    subject = "English"
    salary = "450000"

    def teach(self):
        print(f"My name is {self.name} and i teach {self.subject}")


class student(teacher):
    grade = "14th"
    college = "UOG"

    def student_info(self):
        print(
            f"I am of {self.age}, My name is {self.name} and i study in {self.college} and tommorow is my {self.subject} exam."
        )


s_info = student("Moiz", "4546646", "21")
s_info.getinfo()
s_info.teach()
s_info.student_info()
