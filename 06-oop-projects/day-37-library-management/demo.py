"""
Automated demo showing all features of the Library Management System
Run this to see the system in action without manual input

"""

from library_system import Library

def main():
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - AUTOMATED DEMO")
    print("=" * 60)
    
    # Initialize library
    library = Library()
    print("\n📚 Library initialized!\n")
    
    # Test 1: Add books
    print("=" * 60)
    print("TEST 1: Adding Books")
    print("-" * 60)
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("Pride and Prejudice", "Jane Austen")
    
    # Test 2: Display all books
    print("\n" + "=" * 60)
    print("TEST 2: Display All Books")
    print("-" * 60)
    library.display_books()
    
    # Test 3: Borrow books
    print("=" * 60)
    print("TEST 3: Borrowing Books")
    print("-" * 60)
    library.lend_book("1984")
    library.lend_book("The Great Gatsby")
    
    # Test 4: Try to borrow already borrowed book
    print("\n" + "=" * 60)
    print("TEST 4: Try to Borrow Already Borrowed Book")
    print("-" * 60)
    library.lend_book("1984")
    
    # Test 5: Display after borrowing
    print("\n" + "=" * 60)
    print("TEST 5: Display Books After Borrowing")
    print("-" * 60)
    library.display_books()
    
    # Test 6: Return book
    print("=" * 60)
    print("TEST 6: Return Book")
    print("-" * 60)
    library.return_book("1984")
    
    # Test 7: Try to return non-borrowed book
    print("\n" + "=" * 60)
    print("TEST 7: Try to Return Non-Borrowed Book")
    print("-" * 60)
    library.return_book("Pride and Prejudice")
    
    # Test 8: Try to return non-existent book
    print("\n" + "=" * 60)
    print("TEST 8: Try to Return Non-Existent Book")
    print("-" * 60)
    library.return_book("Harry Potter")
    
    # Test 9: Final status
    print("\n" + "=" * 60)
    print("TEST 9: Final Library Status")
    print("-" * 60)
    library.display_books()
    
    print("=" * 60)
    print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    main()