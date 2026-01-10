# Create a Student class with private __marks attribute. Use getter and setter methods.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, new_marks):
        self.__marks = new_marks

s1 = Student("Aayush Raj Giri", 73)

print(s1.get_marks())
s1.set_marks(83)
print(s1.get_marks())

    