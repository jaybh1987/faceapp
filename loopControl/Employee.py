
class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print(Employee.empCount)

    def displayemp(self):
        print("name", self.name,  ", sal: ", self.salary)
