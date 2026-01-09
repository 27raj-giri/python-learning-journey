# Create a Book class with title, author, and price. Create 3 book objects.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author 
        self.price = price

b1 = Book("Harry Potter", "Jk Rowling", 500)
b2 = Book("The Alchemist", "Paulo", 300)
b3 = Book("Python Basics", "Aayush", 100)

print(b1.title)
print(b2.title)
print(b3.title)