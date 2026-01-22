# Day 38: Bank Account System

A secure banking system demonstrating **encapsulation** and **data protection** through private variables and PIN-based authentication.

## 🎯 Concepts Practiced

- **Encapsulation:** Private variables (`__balance`, `__pin`)
- **Data Protection:** PIN-based security
- **Access Control:** Secure methods for sensitive operations
- **State Management:** Transaction tracking
- **Error Handling:** Validation and security checks

## 🔒 Security Features

### Private Variables (Encapsulation)
```python
self.__balance  # Cannot be accessed directly from outside
self.__pin      # Protected from external access
```

### PIN-Based Authentication
- ✅ Withdraw requires PIN
- ✅ Transfer requires PIN
- ✅ Check details requires PIN
- ✅ Wrong PIN = Access denied

## 🏗️ System Architecture

### BankAccount Class
```python
Properties:
- name (str): Account holder name
- __balance (private int): Current balance
- __pin (private int): 4-digit PIN
- history (list): Transaction log

Methods:
- deposit(amount): Add money (no PIN needed)
- withdraw(amount, pin): Remove money (PIN required)
- transfer(recipient, amount, pin): Send money (PIN required)
- check_details(pin): View statement (PIN required)
- get_balance(pin): Check balance (PIN required)
```

## 📁 Files

- **bank_system.py** - BankAccount class with security
- **main.py** - Interactive demonstration
- **demo.py** - Automated test suite


## 🚀 How to Run

### Interactive Mode:
```bash
python main.py
```

### Automated Demo:
```bash
python demo.py
```

### Generate Output:
```bash
python demo.py > output.txt
```

## 💡 Sample Usage
```python
from bank_system import BankAccount

# Create account
account = BankAccount("Aayush", 1000, 1234)

# Deposit (no PIN needed)
account.deposit(500)

# Withdraw (PIN required)
account.withdraw(200, 1234)  # ✓ Success
account.withdraw(200, 9999)  # ✗ Wrong PIN

# Transfer (PIN required)
recipient = BankAccount("Raj", 500, 5678)
account.transfer(recipient, 300, 1234)

# Check balance (secure)
account.check_details(1234)
```

## 📊 Features Demonstrated

✅ **Private Variables:** `__balance` and `__pin` cannot be accessed externally  
✅ **PIN Security:** All sensitive operations require authentication  
✅ **Transaction History:** Complete log of all operations  
✅ **Input Validation:** Checks for invalid amounts  
✅ **Balance Verification:** Prevents overdrafts  
✅ **Error Messages:** Clear feedback for failed operations  
✅ **Money Transfers:** Secure transfers between accounts  

## 🎓 Learning Outcomes

### Encapsulation Mastery:
- Implemented truly private variables (name mangling)
- Created controlled access through methods
- Protected sensitive data from external modification

### Security Implementation:
- PIN-based authentication system
- Access control on critical operations
- Validation before state changes

### Real-World Banking:
- Deposit/withdraw/transfer operations
- Transaction history tracking
- Balance management
- Multi-account system

## 🔍 Edge Cases Handled

✅ **Invalid Amounts:**
- Negative deposits → Rejected
- Zero or negative withdrawals → Rejected

✅ **Wrong PIN:**
- Withdrawal attempt → Denied
- Transfer attempt → Denied
- Balance check → Denied

✅ **Insufficient Funds:**
- Withdrawal → Rejected with message
- Transfer → Rejected with message

## 💎 Why This Code is Excellent

### 1. **True Encapsulation:**
```python
account.__balance  # ❌ AttributeError
account.get_balance(pin)  # ✅ Correct way
```

### 2. **Security First:**
- Every sensitive operation verified
- No backdoor access to balance
- PIN protection implemented correctly

### 3. **Professional Structure:**
- Clear method separation
- Good error messages
- Transaction logging
- Clean code organization

---

**Day:** 38 | **Module:** OOP Projects  
**Date:** January 22, 2026  
**Status:** ✅ Complete

**Key Achievement:** Mastered encapsulation and data protection! 🔒