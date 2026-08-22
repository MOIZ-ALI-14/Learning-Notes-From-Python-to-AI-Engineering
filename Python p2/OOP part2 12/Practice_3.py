class Employee:
    salary = 300
    increament = 30

    @property
    def SalaryAfterIncreament(self):
        return self.salary + self.salary * (self.increament / 100)

    @SalaryAfterIncreament.setter
    def SalaryAfterIncreament(self, salary):
        self.increament = ((salary / self.salary) - 1) * 100


e1 = Employee()
e1.SalaryAfterIncreament = 450
print(e1.increament)
