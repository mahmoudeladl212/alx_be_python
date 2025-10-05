class Book:
    """A class to represent a book in the library"""
    
    def __init__(self, title, author):
        """
        Initialize a Book instance
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Check out the book if available"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book to the library"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available"""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    """A class to manage a collection of books"""
    
    def __init__(self):
        """Initialize a Library instance with an empty book list"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """
        Add a book to the library
        
        Args:
            book (Book): A Book instance to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a book by title
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No available books in the library.")
        else:
            for book in available_books:
                print(book)