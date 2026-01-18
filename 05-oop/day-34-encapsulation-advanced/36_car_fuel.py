# Create Car class with private __fuel_level. Add methods to refuel (max 100) and drive (decreases fuel).

class Car:
    def __init__(self):
        self.__fuel = 50

    def refuel(self, amount):
        if self.__fuel + amount > 100:
            self.__fuel = 100
            print("Tank Full!")

        else:
            self.__duel += amount

    def drive(self):
        if self.__fuel > 0:
            self.__fuel -= 10
            print("Driving....")

        else:
            print("Out of Fuel...")
        
c = Car()
c.refuel(60)
c.drive()