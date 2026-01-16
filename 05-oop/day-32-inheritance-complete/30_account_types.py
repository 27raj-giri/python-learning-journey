# Create Account parent class. Create SavingsAccount and CheckingAccount children with different withdrawal rules.

class Account:
    def withdraw(self, amount):
        print(f"Withdrawing {amount}...")

class SavingsAccount(Account):
    pass

class CheckingAccount(SavingsAccount):
    def withdraw(self, amount):
        print(f"Withdrawing {amount} + 10 Rupees Fee")

s = SavingsAccount()
c = CheckingAccount()

s.withdraw(1000)
c.withdraw(1000)