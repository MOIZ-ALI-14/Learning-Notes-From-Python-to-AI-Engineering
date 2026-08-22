class teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject


class student(teacher):

    def __init__(self, name, age, subject):
        super().__init__(name, age, subject)
        print(f"My name is {self.name} and i am of {self.age} and my subject is {self.subject}")


s1 = student("Moiz", "20", "English")

# SUPER() COMPLETE REFERENCE
# ===========================
# super() gives access to parent class constructor from child class
# Only use when child class has its OWN constructor
# If child has no constructor - Python uses parent automatically - no super() needed

# MOST IMPORTANT RULE:
# When child class has its own constructor - ONLY child constructor runs automatically
# Parent constructor is COMPLETELY IGNORED without super()
# So parent attributes like self.name self.age are LOST forever
# The ONLY way to run parent constructor from child = super()
# Without super() - you can NEVER access parent constructor attributes in child
