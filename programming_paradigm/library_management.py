class Book:
    def __init__(self):
        self.title = title
        self.author = author
        self._is_checked_out = False 

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True 
        else:
            raise ValueError(f"The book '{self.title}' is already checked out.")

        return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            raise ValueError(f"The book '{self.author}' was not checked out.")

    def is_available(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__ (self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"Sorry, the book '{title}' is already checked out.")
                    return

        print(f"The book '{title}' was not checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:if not book.is_available():
                book.return_book()
                return 
            else:
                print(f"The book '{title}' was not checked out.")
                return 
        print(f"Book '{title}' not in the library.")

    def list_available_books(self):
        """List all books that are currently available (not checked out)."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available.")

        
