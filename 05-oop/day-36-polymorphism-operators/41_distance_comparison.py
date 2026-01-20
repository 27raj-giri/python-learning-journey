# Create Distance class. Overload <, >, == operators to compare distances.

class Distance:
    def __init__(self, km):
        self.km = km

    def __lt__(self, other):
        return self.km < other.km
    
    def __gt__(self, other):
        return self.km > other.km
    
    def __eq__(self, other):
        return self.km == other.km
    
d1 = Distance(10)
d2 = Distance(20)

if d1 < d2:
    print("d1 is shorter")
elif d1 > d2:
    print("d1 is greater")
else:
    print("Both are equal")
    
