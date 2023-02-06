class Library:
    def __init__(self):
        self.no_of_book = 0
        self.book=[]

    def addBooks(self,book):
        self.book.append(input("Enter the book to Add:")) #this will add books
        self.no_of_book=len(self.book) #count
    def showdetails(self):
        print(f"There are {self.no_of_book} books in Library and the books are:")
        for b in self.book:
            print(b)
l=Library()
l.addBooks()
l.addBooks()
l.addBooks()
l.showdetails()
