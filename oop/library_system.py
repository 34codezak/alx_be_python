# Base Class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, by {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition Class: Library
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

# Create a library and add books to it
library = Library()
library.add_book(book1)
library.add_book(ebook1)
library.add_book(printbook1)

# List all books in the library
library.list_books()

# Create instances of each class
book1 = Book("Pride and Prejudice", "Jane Austen")
ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

"""Explanation of library_system.py:
Base Class - Book:

The Book class has attributes title and author, and the __str__() method for string representation.
Derived Class - EBook:

The EBook class inherits from Book and adds the file_size attribute.
It calls the super().__init__() method to initialize the base class's title and author attributes.
Derived Class - PrintBook:

The PrintBook class inherits from Book and adds the page_count attribute.
Like EBook, it calls super().__init__() to initialize the title and author.
Composition Class - Library:

The Library class has a list books to store instances of Book, EBook, and PrintBook.
It has two methods:
add_book(self, book) to add books to the collection.
list_books(self) to print the details of each book in the library."""