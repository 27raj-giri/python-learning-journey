# Create a Car class with brand, model, and year. Add a method to display car info.

class Car:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.year} {self.model} {self.brand}")

my_car = Car(2022, "Legender", "Toyota")
my_car.info()
        