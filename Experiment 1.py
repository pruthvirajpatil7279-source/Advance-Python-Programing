
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Patron:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        self.books.append(Book(title))

    def register_patron(self, name):
        self.patrons.append(Patron(name))

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(title, "borrowed")
                return

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(title, "returned")

# Driver Code
lib = Library()
lib.add_book("Python")
lib.register_patron("Alice")
lib.borrow_book("Python")
lib.return_book("Python")