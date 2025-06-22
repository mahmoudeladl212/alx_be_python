class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"{super().__str__()} [EBook, File Size: {self.file_size}KB]"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"{super().__str__()} [Print Book, Pages: {self.page_count}]"


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Can only add Book objects to the library")
    
    def list_books(self):
        if not self.books:
            print("The library is empty")
        else:
            print("Library Contents:")
            for book in self.books:
                print(f"- {book}")