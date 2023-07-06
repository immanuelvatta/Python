
class Book:
    all_books = []
    
    def __init__(self, name, year, num_of_pages):
        self.name = name
        self.year = year
        self.num_of_pages = num_of_pages
        self.library = None
        
        Book.all_books.append(self)
        
    def transfer(self, new_library):
        if not self.library:
            print("There is no library attached to this book")
            # return self
            print(f"attaching {self.name}to the new library {new_library}")
            self.library = new_library
        else:
            #remove the book from the old library
            self.library.remove_book(self)
            #add the book to the new library
            self.library = None
            new_library.add_book_to_library(self)
            #update instance attribute to the new library
            self.library = new_library