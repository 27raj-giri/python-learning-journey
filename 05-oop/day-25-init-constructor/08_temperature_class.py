# Create a Temperature class that converts Celsius to Fahrenheit.

class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return (self.celcius * 1.8) + 32
    
temp = Temperature(25)
print(temp.to_fahrenheit())