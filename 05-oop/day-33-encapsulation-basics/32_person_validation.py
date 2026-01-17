# Create Person with private __age. Use setter to validate age (must be > 0 and < 150).

class Person:
    def set_age(self, age):
        if age > 0 and age < 150:
            self.__age = age
            print("Age is acceptable")
        else:
            print("Age not acceptable. Should be between 0 and 150.")

    def get_age(self):
        return self.__age
    
p = Person()
p.set_age(500)
p.set_age(25)
