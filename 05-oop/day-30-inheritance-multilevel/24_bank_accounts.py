# Create BankAccount class. Create SavingsAccount and CurrentAccount as child classes with different interest rates.

class BankAccount:
    def get_interest(self):
        return 0
    
class SavingsAccount:
    def get_interest(self):
        return 0.04
    
class CurrentAccount:
    def get_interest(self):
        return 0.0
    
s = SavingsAccount()
print(s.get_interest())