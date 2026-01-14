# Create Bird class with fly() method. Create Penguin class that overrides fly() to say "Can't fly".

class Bird:
    def fly(self):
        print("I am flying")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")

p = Penguin()
p.fly()