class BankAccount:
    """Represents a bank account with secure PIN protection"""
    
    def __init__(self, name, initial_balance, pin):
        self.name = name
        self.__balance = initial_balance  
        self.__pin = pin                   
        self.history = []
        
        self.history.append(f"Account created with {initial_balance} rupees")

    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.__balance += amount
            self.history.append(f"Deposited: +{amount} rupees")
            print(f"{amount} rupees deposited successfully!")
        else:
            print("Invalid amount.")

    def withdraw(self, amount, pin):
        """Withdraw money with PIN verification"""
        if pin != self.__pin:
            print("Wrong PIN! Access denied.")
            return
        
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.__balance -= amount
            self.history.append(f"Withdrew: -{amount} rupees")
            print(f"Withdrew {amount} rupees. Remaining: {self.__balance} rupees")
    
    def transfer(self, recipient, amount, pin):
        """Transfer money to another account"""
        if pin != self.__pin:
            print("Wrong PIN! Transfer failed.")
            return
        
        if self.__balance >= amount:
            self.__balance -= amount
            recipient.deposit(amount)
            self.history.append(f"Transferred {amount} rupees to {recipient.name}")
            print(f"Transferred {amount} rupees to {recipient.name}")
        else:
            print("Insufficient balance for transfer.")
    
    def check_details(self, pin):
        """Display account statement with PIN verification"""
        if pin == self.__pin:
            print(f"\n{'=' * 40}")
            print(f"ACCOUNT STATEMENT - {self.name}")
            print(f"{'=' * 40}")
            print(f"Current Balance: {self.__balance} rupees")
            print(f"\nTransaction History:")
            for log in self.history:
                print(f"  • {log}")
            print(f"{'=' * 40}\n")
        else:
            print("Wrong PIN! Access denied.")
    
    def get_balance(self, pin):
        """Get current balance with PIN verification"""
        if pin == self.__pin:
            return self.__balance
        else:
            print("Wrong PIN!")
            return None