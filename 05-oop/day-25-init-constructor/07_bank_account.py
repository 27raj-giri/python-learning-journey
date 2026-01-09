# Create a BankAccount class with account_number and balance. Add a method to display balance.

class BankAccount:
    def __init__ (self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def show_balance(self):
        print(f"Account Number {self.acc_num} has {self.balance} rupees")

acc = BankAccount("231005", "27999999999999999")
acc.show_balance()