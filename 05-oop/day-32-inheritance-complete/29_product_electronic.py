# Create Product class. Create ElectronicProduct that inherits and adds warranty_period.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty = warranty_period

e = ElectronicProduct("Bajaj Mixer", 1200, "5 Years")
print(e.name)
print(e.warranty)
    