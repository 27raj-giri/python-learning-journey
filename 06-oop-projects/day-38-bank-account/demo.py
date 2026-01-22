"""
Automated demo showing all features of the Bank Account System
Demonstrates encapsulation, PIN security, and transaction tracking
"""

from bank_system import BankAccount

def main():
    print("=" * 60)
    print("BANK ACCOUNT SYSTEM - AUTOMATED DEMO")
    print("=" * 60)
    
    
    print("\nCreating Bank Accounts...")
    print("-" * 60)
    aayush = BankAccount("Aayush Raj Giri", 5000, 1234)
    priya = BankAccount("Priya Sharma", 3000, 5678)
    raj = BankAccount("Raj Kumar", 2000, 9012)
    print("3 accounts created successfully!\n")
    
    
    print("=" * 60)
    print("TEST 1: DEPOSITS")
    print("-" * 60)
    aayush.deposit(2000)
    priya.deposit(1500)
    raj.deposit(500)
    
    
    print("\n" + "=" * 60)
    print("TEST 2: INVALID DEPOSIT")
    print("-" * 60)
    aayush.deposit(-500)
    
    
    print("\n" + "=" * 60)
    print("TEST 3: WITHDRAWAL WITH WRONG PIN")
    print("-" * 60)
    aayush.withdraw(1000, 9999)
    
    
    print("\n" + "=" * 60)
    print("TEST 4: WITHDRAWAL WITH CORRECT PIN")
    print("-" * 60)
    aayush.withdraw(1000, 1234)
    
    
    print("\n" + "=" * 60)
    print("TEST 5: WITHDRAWAL - INSUFFICIENT FUNDS")
    print("-" * 60)
    raj.withdraw(5000, 9012)
    
    
    print("\n" + "=" * 60)
    print("TEST 6: TRANSFER WITH WRONG PIN")
    print("-" * 60)
    aayush.transfer(priya, 1000, 9999)
    
    
    print("\n" + "=" * 60)
    print("TEST 7: SUCCESSFUL TRANSFER")
    print("-" * 60)
    aayush.transfer(priya, 1000, 1234)
    

    print("\n" + "=" * 60)
    print("TEST 8: TRANSFER - INSUFFICIENT FUNDS")
    print("-" * 60)
    raj.transfer(aayush, 3000, 9012)
    
    
    print("\n" + "=" * 60)
    print("TEST 9: MULTIPLE OPERATIONS")
    print("-" * 60)
    priya.deposit(500)
    priya.withdraw(1000, 5678)
    priya.transfer(raj, 500, 5678)
    
    
    print("\n" + "=" * 60)
    print("TEST 10: CHECK DETAILS - WRONG PIN")
    print("-" * 60)
    aayush.check_details(9999)
    
   
    print("\n" + "=" * 60)
    print("FINAL ACCOUNT STATEMENTS")
    print("=" * 60)
    aayush.check_details(1234)
    priya.check_details(5678)
    raj.check_details(9012)
    
    print("=" * 60)
    print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nKey Features Demonstrated:")
    print(" Private variables (__balance, __pin)")
    print(" PIN-based security")
    print(" Transaction history tracking")
    print(" Error handling (invalid amounts, wrong PIN, insufficient funds)")
    print(" Money transfers between accounts")
    print("=" * 60)

if __name__ == "__main__":
    main()