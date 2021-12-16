#import file
from salesman import Salesman

#create objects
s1 = Salesman(1 , "John" , 30000 , "772358375")
s2 = Salesman(2 , "Ann" , 40000 , "773029452")
s3 = Salesman(3 , "Leema" , 35000 , "778294526")

#set new contact numbers
s1.setSalesmanContactNo()
s2.setSalesmanContactNo()
s3.setSalesmanContactNo()

#display details
s1.displaySalesmanDetails()
s2.displaySalesmanDetails()
s3.displaySalesmanDetails()