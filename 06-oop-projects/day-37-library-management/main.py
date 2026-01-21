from library_system import Book, Library

def main():
    my_library = Library()

    my_library.add_book("Python Basics", "Aayush Raj Giri")
    my_library.add_book("Atomic Habits", "James Clear")

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")
        print("=" * 37)

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            my_library.add_book(title, author)

        elif choice == '2':
            my_library.display_books()

        elif choice == '3':
            title = input("Enter Book Title to Borrow: ").strip()
            my_library.lend_book(title)

        elif choice == '4':
            title = input("Enter Book Title to Return: ").strip()
            my_library.return_book(title)

        elif choice == '5':
            print("\nThank you for using the Library System. Goodbye! 📚")
            break

        else:
            print("\n✗ Invalid choice! Please enter a number between 1-5.")


if __name__ == "__main__":
    main()