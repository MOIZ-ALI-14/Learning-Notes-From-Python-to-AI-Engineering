class teacher:
    def subject(self, sub):
        print(f"Teaches {sub}")


class student(teacher):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def student_info(self):
        print(f"My name is {self.name} and I am in {self.grade}")


s1 = student("moiz", "14th")
s1.student_info()
s1.subject("Maths")
