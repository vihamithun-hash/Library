class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for theBook in self.books:
            theBook.display()

    def find_book(self, book_title):
        for theBook in self.books:
            if theBook.title == book_title:
                return theBook
            return None  