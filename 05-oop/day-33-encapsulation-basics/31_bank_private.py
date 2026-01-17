# Create BankAccount with private __balance. Access it only through methods.

class BankAccount:
    def __init__(self, initial_amount):
        self.__balance = initial_amount

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}")

    def get_balance(self):
        return self.__balance
    
acc = BankAccount(1000)
acc.deposit(500)

print("Current Balance is:", acc.get_balance())