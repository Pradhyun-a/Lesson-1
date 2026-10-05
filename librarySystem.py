class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  

    def borrow(self):
        if self.is_borrowed == True:
            print("Already borrowed!")
        else:
            self.is_borrowed = True
            print("Borrowed successfully!")

    def return_book(self):
        if self.is_borrowed == False:
            print("Was not borrowed!")
        else:
            self.is_borrowed = False
            print("Returned successfully!")

    def __str__(self):
        if self.is_borrowed == True:
            return self.title + " by " + self.author + " [Borrowed]"
        else:
            return self.title + " by " + self.author + " [Available]"

book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("The Hobbit", "J.R.R. Tolkien")

print("=" * 42)
print("         📚  LIBRARY SYSTEM")
print("=" * 42)

print(book1)
print(book2)
print(book3)

print("\n--- Testing Borrow ---")
book1.borrow()
book1.borrow()

print("\n--- Testing Return ---")
book1.return_book()
book3.return_book()

print("\n--- Final Status ---")
print(book1)
print(book2)
print(book3)
