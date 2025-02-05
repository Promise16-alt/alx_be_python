# library_system.py

class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an EBook, inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book, inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class using composition to manage a collection of books."""
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):  # Ensure only Book objects are added
            self.books.append(book)

    def list_books(self):
        """Prints all books in the library."""
        for book in self.books:
            print(book)
