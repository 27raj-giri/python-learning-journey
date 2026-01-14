# Create multilevel inheritance: LivingBeing → Animal → Dog. Each level adds attributes.

class LivingBeing:
    alive = True

class Animal(LivingBeing):
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

d = Dog()
print(d.alive)
d.eat()
d.bark()