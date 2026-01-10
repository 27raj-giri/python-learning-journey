# Create a Calculator class with methods: add(), subtract(), multiply(), divide().

class Calculator:

    def addition(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
calc = Calculator()
print("Sum:", calc.addition(5, 10))
print("Product:", calc.multiply(9, 9))