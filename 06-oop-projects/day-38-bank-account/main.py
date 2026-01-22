from bank_system import BankAccount

def main():
    
    print("=" * 50)
    print("BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 50)
    
    user1 = BankAccount("Aayush Raj Giri", 1000, 3984)
    user2 = BankAccount("Raj Kumar", 500, 9864)
    
    print("\n Two accounts created successfully!\n")
    
    
    print("-" * 50)
    print("TEST 1: DEPOSIT")
    print("-" * 50)
    user1.deposit(500)
    
   
    print("\n" + "-" * 50)
    print("TEST 2: WITHDRAWAL (Wrong PIN)")
    print("-" * 50)
    user1.withdraw(200, 1010)
    
    
    print("\n" + "-" * 50)
    print("TEST 3: WITHDRAWAL (Correct PIN)")
    print("-" * 50)
    user1.withdraw(200, 3984)
    
   
    print("\n" + "-" * 50)
    print("TEST 4: TRANSFER")
    print("-" * 50)
    user1.transfer(user2, 300, 3984)
    

    print("\n" + "=" * 50)
    print("FINAL ACCOUNT STATEMENTS")
    print("=" * 50)
    user1.check_details(3984)
    user2.check_details(9864)

if __name__ == "__main__":
    main()