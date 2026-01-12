# Create Vehicle class with brand and model. Create Car class that inherits and adds num_doors.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)

        self.num_doors = num_doors

c = Car("Toyota", "Fortuner", 5)
print(c.brand, c.model, c.num_doors)
