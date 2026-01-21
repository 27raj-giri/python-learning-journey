class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} is [{status}]"
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book Added: {title}")

    def display_books(self):
        print("\n-------- LIBRARY CATALOG --------------------")
        if not self.books:
            print("The library is empty")
        else:
            for book in self.books:
                print(book)
        print("----------------------------------------------\n")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"✓ You have borrowed '{book.title}'. Enjoy!!")
                    return
                else:
                    print(f"✗ Sorry, '{book.title}' is already borrowed")
                    return
        print(f"✗ Book '{title}' not found in the library")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"✓ Thank you for returning '{book.title}'")
                    return
                else:
                    print("✗ This book was not borrowed from us")
                    return
        print(f"✗ Book '{title}' does not belong to this library")