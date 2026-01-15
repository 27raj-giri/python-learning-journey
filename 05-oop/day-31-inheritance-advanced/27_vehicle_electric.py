# Create Vehicle hierarchy: Vehicle → Car → ElectricCar. Each adds specific attributes.

class Vehicle:
    brand = "Tata"

class Car(Vehicle):
    wheels = 4

class ElectricCar(Car):
    battery = "100kwh"

e = ElectricCar()
print(e.brand, e.wheels, e.battery)
