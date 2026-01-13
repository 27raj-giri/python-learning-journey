# Use super() to call parent class __init__ in child class constructor.

class Parents:
    def __init__(self, surname, property):
        self.surname = surname
        self.property = property

class Child(Parents):
    def __init__(self, surname, property, business):
        super().__init__(surname, property)
        self.business = business

c1 = Child("Giri", "Land", "Woods")
print(c1.surname)
