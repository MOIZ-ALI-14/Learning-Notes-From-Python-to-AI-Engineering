class teacher1:
    def subject(self, sub):
        print(f"Teaches {sub}")


class teacher2:
    def college(self, col):
        print(f"college is {col}")


class student(teacher1, teacher2):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def student_info(self):
        print(f"My name is {self.name} and I am in {self.grade}")


s1 = student("moiz", "14th")
s1.student_info()
s1.subject("Maths")
s1.college("UOG")
