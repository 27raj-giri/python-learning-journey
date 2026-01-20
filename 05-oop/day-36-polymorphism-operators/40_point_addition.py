# Create Point class. Overload + operator to add two points (x1+x2, y1+y2).

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2

print(p3)