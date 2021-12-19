#import files
from book import Book

#create objects and set values
b1 = Book("1212" , "Jane Eyre" , "Charlotte Bronte")
b2 = Book("1234" , "Divergent" , "Veronica Roth")
b3 = Book("3456" , "Matilda" , "Ronald Dahl")

#set new id for objects
id = input("Input new book ID 1 : ")
b1.setBookID(id)

id = input("Input new book ID 2 : ")
b2.setBookID(id)

id = input("Input new book ID 3 : ")
b3.setBookID(id)

#display object variables
b1.displayBookDetails()
b2.displayBookDetails()
b3.displayBookDetails()