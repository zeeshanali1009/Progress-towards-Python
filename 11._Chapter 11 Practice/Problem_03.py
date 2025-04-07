class Employee:
    salary = 10000
    increment = 100

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment / 100))

    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


a = Employee()
a.increment = 10
a.salaryafterincrement = 280.8
print(a.increment)
