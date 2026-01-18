# Create Student class with protected _marks and private __id. Demonstrate access levels.

class Student:
    def __init__(self):
        self._marks = 73
        self.__id = 231005

    def get_id(self):
        return self.__id

s = Student()

print(s._marks)

print(s.get_id())
