

class Library:
    all_libraries = []
    def __init__(self, name):
        self.name = name
        self.books = []
        
        Library.all_libraries.append(self)
        
    def show_books(self):
        if len(self.books) > 0:
            for idx, book in enumerate(self.books):
                print(idx, book.name)
        else:
            print(f"There are no books in {self.name}")
        return self
    
    def add_book_to_library(self,book):
        if not book.library:
            self.books.append(book)
            book.library = self
            return self
        else:
            print(f"Book is already in the library: {book.library.name}. You must transfer it out")
            
    def remove_book(self, book):
        for idx, book_in_library in enumerate(self.books):
            print(f"looking at book in library: {book_in_library} vs book: {book}")
            if book_in_library == book:
                print("Found the book")
                return self.books.pop(idx)
                # return book
        return self