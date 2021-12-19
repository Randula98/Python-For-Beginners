
#create class
class Salesman:
    #define class variables
    def __init__(self , salesmanid , salesmanName , salary , contactNo):
        self.salesmanid = salesmanid
        self.salesmanName = salesmanName
        self.salary = salary
        self.contactNo = contactNo

    #define class functions
    def displaySalesmanDetails(self):
        print()
        print("Salesman ID : " + str(self.salesmanid))
        print("Salesman Name : " + self.salesmanName)
        print("Salary : " + str(self.salary))
        print("Contact No : " + self.contactNo)

    def setSalesmanContactNo(self):
        self.contactNo = input("Input new contact number of salesman " + str(self.salesmanid) + " : ")

