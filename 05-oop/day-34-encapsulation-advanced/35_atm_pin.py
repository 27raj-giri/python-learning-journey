# Create ATM class with private __pin. Add methods to change PIN (requires old PIN verification).

class ATM:
    def __init__(self):
        self.__pin = 3984

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
           self.__pin == new_pin
           print("Password Updated Successfully")
        
        else:
            print("Wrong Password")

my_atm = ATM()
my_atm.change_pin(3976, 9864)
my_atm.change_pin(3984, 9864)

