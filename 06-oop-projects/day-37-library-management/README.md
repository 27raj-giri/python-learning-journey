# Day 37: Library Management System

A simple yet functional library management system demonstrating core OOP concepts.

## 🎯 Concepts Practiced

- **Classes & Objects:** `Book` and `Library` classes
- **Encapsulation:** Book properties and library collection
- **Methods:** Instance methods for operations
- **Lists:** Managing collection of book objects
- **String Methods:** Case-insensitive search
- **Control Flow:** Menu-driven interface

## 🏗️ System Architecture

### Book Class
```python
Properties:
- title (str)
- author (str)
- is_available (bool)

Methods:
- __str__(): Display book info
```

### Library Class
```python
Properties:
- books (list of Book objects)

Methods:
- add_book(title, author): Add new book
- display_books(): Show all books
- lend_book(title): Borrow a book
- return_book(title): Return a book
```

## 📁 Files

- **library_system.py** - Core classes (Book, Library)
- **main.py** - Interactive menu-driven interface
- **demo.py** - Automated demonstration
- **output.txt** - Sample program output

## 🚀 How to Run

### Interactive Mode:
```bash
python main.py
```

### Demo Mode:
```bash
python demo.py
```

### Generate Output:
```bash
python demo.py > output.txt
```

## 💡 Sample Usage
```python
from library_system import Library

# Create library
library = Library()

# Add books
library.add_book("1984", "George Orwell")
library.add_book("Atomic Habits", "James Clear")

# Display all books
library.display_books()

# Borrow a book
library.lend_book("1984")

# Return a book
library.return_book("1984")
```

## 📊 Features

✅ Add books to library  
✅ Display all books with availability status  
✅ Borrow books (updates availability)  
✅ Return books (restores availability)  
✅ Case-insensitive book search  
✅ Error handling for edge cases  
✅ Menu-driven interface  
✅ Clean status messages  

## 🎓 Learning Outcomes

- Designed multi-class system
- Managed object collections (list of objects)
- Implemented state management (available/borrowed)
- Created user-friendly menu interface
- Applied proper error handling
- Used `__str__` for clean object representation

## 🔍 Edge Cases Handled

- Empty library display
- Book not found
- Book already borrowed
- Book not borrowed (return attempt)
- Case-insensitive search
- Invalid menu choices

---

**Day:** 37 | **Module:** OOP Projects  
**Date:** January 21, 2026  
**Status:** ✅ Complete