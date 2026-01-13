# Create Employee class with name and salary. Create Manager class that inherits and adds department.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

emp1 = Manager("Aayush Raj Giri", 50000, "IT")
print(emp1.name, emp1.salary, emp1.department)

