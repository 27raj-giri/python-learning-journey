# Create Animal classes: Dog, Cat, Cow - each with speak() method making different sounds.

class Dog:
    def speak(self):
        print("Bark..")

class Cat:
    def speak(self):
        print("Meow..")

class Cow:
    def speak(self):
        print("Mooo..")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()