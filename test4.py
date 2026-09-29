class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(self.title + " has been borrowed.")

    def return_book(self):
        self.is_borrowed = False
        print(self.title + " has been returned.")

book1 = Book("The Hobbit", "Tolkien")
book2 = Book("1984", "Orwell")
book3 = Book("The Matrix", "Wachowski")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()
