class book:
    def __init__(self,bookID,Title,Author,Price,Category):
        self.bookID = bookID
        self.Title = Title
        self.Author = Author
        self.Price = Price
        self.Category = Category


class library:

    def list(self):
        self.booklist = []

    def addbook(self,book):
        self.booklist.append(book)

    def display(self):
        if len(list) == 0:
            print("no books are available")
        else:
            print(book)




Library = library()

bookID = int(input("Enter the book ID:"))
Title = input("Enter the book Tile:")
Author = input("Enter the Name of the Author:")
Price = float(input("Enter the price if the book:"))
Category = input("enter the category(premium/standard):")


book1 = book(bookID,Title,Author,Price,Category)
Library.addbook(book1)

print("\n library Book")
library.display()










        
