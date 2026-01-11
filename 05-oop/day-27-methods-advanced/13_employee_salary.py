# Create a Employee class with methods to set salary and calculate annual salary.

class Employee:
    def set_salary(self, monthly_salary):
        self.salary = monthly_salary

    def get_annaul_salary(self):
        return self.salary * 12
    
emp1 = Employee()
emp1.set_salary(50000)
print("Annual Package:", emp1.get_annaul_salary())
