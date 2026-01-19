# Create Shape with area() method. Create Rectangle, Circle, Triangle - each implements area() differently.

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w
    
class Circle(Shape):
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return 3.14 * self.r * self.r
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.b = base
        self.h = height
    def area(self):
        return 0.5 * self.b * self.h
    
shapes = [Rectangle(10,5), Circle(7), Triangle(10, 5)]

for s in shapes:
    print(s.area())

    