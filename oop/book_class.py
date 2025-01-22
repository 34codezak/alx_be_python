class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author 
        self.year = year

        #Destructor method to handle object declaration
        def __del__(self):
            print(f"Deleting {self.title}")

        #String representation method for user-friendly output
        def __str__(self):
            return f"Book('{self.title}', '{self.author}', '{self.year}')"

            #Official representation method for debugging or object creation
            def __repr__(self):
                return f"Book('{self.title}', '{self.author}', '{self.year}')"

#Example usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(book1) #This will call __str__ method
    print(repr(book1)) #This will call __repe__ method

    #Delete the object and see the destructor in action
    del book1