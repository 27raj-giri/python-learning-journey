# Create a Product class with class variable total_products that tracks how many products are created.

class Product:
    total_products = 0

    def __init__(self, name):
        self.name = name

        Product.total_products = Product.total_products + 1

p1 = Product("Laptop")
p2 = Product("Phone")
p3 = Product("Mouse")

print(Product.total_products)