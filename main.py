#Create class Book, and characteristics
class Book():
    def __init__(self,title,author,available=True):
        self.title=title
        self.author=author
        self.available=available

#create empty library
class Library():
    def __init__(self):
        self.books=[]
#create function add book
    def add_book(self,title,author):
        book=Book(title,author)
        self.books.append(book)

#create search_book
    def search_book(self,title):
        for book in self.books:
            if book.title==title:
                return book
        return None
#create borrow_book
    def borrow_book(self,title):
        book=self.search_book(title)
        if book and book.available:
            book.available=False
            print("Book is borrowed successfully")
        elif book and not book.available:
            print("Book is already borrowed")
        else:
            print("Book is not available")

#create return_book
    def return_book(self,title):
        book=self.search_book(title)
        if book and not book.available:
            book.available=True
            print("Book returned successfully")
        elif book and book.available:
            book.available=True
            print("Book is already available")
        else:
            print("Book is not recognized")

#adding borrowing etc
library=Library()
library.add_book("Najbogatszy człowiek w Babilonie","George Samuel Clason")
library.borrow_book('Najbogatszy człowiek w Babilonie')
library.borrow_book('Najbogatszy człowiek w Babilonie')
library.return_book('Najbogatszy człowiek w Babilonie')