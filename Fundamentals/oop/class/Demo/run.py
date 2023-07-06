from  classes.library import Library
from classes.book import Book

immanuel_library = Library("Immanuel's Library")
joe_library = Library("Joe's Library")

#create books
bk1 = Book("To Kill a Mockingbird", 1960, 324)
bk2 = Book("1984", 1949, 328)
bk3 = Book("Pride and Prejudice", 1813, 432)
bk4 = Book("The Great Gatsby", 1925, 180)
bk5 = Book("The Catcher in the Rye", 1951, 224)
bk6 = Book("Moby-Dick", 1851, 635)
bk7 = Book("The Lord of the Rings", 1954, 421)
bk8 = Book("Jane Eyre", 1847, 594)
bk9 = Book("Harry Potter and the Philosopher's Stone", 1997, 223)
bk10 = Book("The Hobbit", 1937, 310)
# print(immanuel_library)


immanuel_library.add_book_to_library(bk1)
immanuel_library.add_book_to_library(bk2)
immanuel_library.add_book_to_library(bk3)

joe_library.add_book_to_library(bk4)
joe_library.add_book_to_library(bk5)
joe_library.add_book_to_library(bk6)


immanuel_library.show_books()

bk1.transfer(joe_library)
immanuel_library.show_books()
joe_library.show_books()