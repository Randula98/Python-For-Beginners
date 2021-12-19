#define class
class Book:
   #define class variables
   def __init__ (self , bookID , bookName , author):
        self.bookID = bookID
        self.bookName = bookName
        self.author = author

   #define class functions
   def displayBookDetails(self):
        print()
        print("Book ID = " + str(self.bookID))
        print("Book Name = " + self.bookName)
        print("Book Author = " + self.author)

   def setBookID(self , pid):
        self.bookID = pid

