# Create Shape class with method area(). Create Rectangle and Circle classes that inherit and implement area().

class Shape:
    def area(self):
        return 0
    
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
    
r = Rectangle(10, 5)
c = Circle(7)

print(r.area())
print(c.area())
