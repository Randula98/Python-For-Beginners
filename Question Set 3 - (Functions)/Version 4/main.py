
#define calculateTotalCost function
def calculateTotalCost(itemNo , quantity):
    if itemNo == "1":
        unitPrice = 100
    elif itemNo == "2":
        unitPrice = 200
    else:
        unitPrice = 300

    totalCost = unitPrice * quantity
    return totalCost

#define printDetails function
def printDetails(itemNo , quantity , totalCost):
    print()
    print("Item No : " + str(itemNo))
    print("Quantity : " + str(quantity))
    print("Total Cost : " + str(totalCost))


#get user inputs for item no
itemNo = input("Enter Item Number : ")
while itemNo != "1" and itemNo != "2" and itemNo != "3":
    print("Invalid Input!! Try again")
    #get user inputs for item no
    itemNo = input("Enter Item Number : ")

#get user inputs for quantity
quantity = input("Enter quantity : ")
quantity = int(quantity)

#pass the given values to calculateTotalCost function
totalCost = calculateTotalCost(itemNo , quantity)

#pass the given values to printDetails function
printDetails(itemNo , quantity , totalCost)