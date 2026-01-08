# Circle Area & Circumference

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius
    
    def get_circumference(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(5)
print("Area:", c1.get_area())
print("Circumference:", c1.get_circumference())
