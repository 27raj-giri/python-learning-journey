# Create Animal class with method sound(). Create Dog class that inherits from Animal and overrides sound().

class Animal:
    def sound(self):
        print("Some Generic Sound")

class Dog(Animal):
    def sound(self):
        print("Bark Bark!")

a = Animal()
a.sound()

d = Dog()
d.sound()