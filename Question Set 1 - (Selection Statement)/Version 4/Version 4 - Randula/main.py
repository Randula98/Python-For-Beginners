
#taking user inputs for package type
pType = input("Package Type : ")
while pType != "S" and pType != "s" and pType != "G" and pType != "g":
    print("Invalid Input!! Try again")
    pType = input("Package Type : ")

#taking user inputs for food type
fType = input("Food type : ")
while fType != "1" and fType != "2" and fType != "3":
    print("Invalid Input!! Try again")
    fType = input("Food type : ")

#taking user inputs for number of guests
noOfGuests = input("Number of guests : ")
noOfGuests = float(noOfGuests)

#select the package price by the user input
if pType == "S" or pType == "s":
    pPrice = 10000
else:
    pPrice = 25000

#select the food price by the user input
if fType == "1":
    fPrice = 1000
elif fType == "2":
    fPrice = 2000
else:
    fPrice = 1500

#calculate the total bill
total = pPrice + (fPrice * noOfGuests)

#display the total price
print("Bill Amount : " + str(total))