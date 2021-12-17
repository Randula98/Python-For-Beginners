total = 0

#get user input for item number
itemNo = input("Enter Item : ")

while itemNo != "-1":
    #check for invalid input
    if itemNo != "1" and itemNo != "2" and itemNo != "3":
        print("Invalid Input")
        #get user input for item number
        itemNo = input("Enter Item : ")
        continue

    #take user inputs for quantity
    quantity = input("Enter Quantity : ")
    quantity = float(quantity)

    if itemNo == "1":
        total = total + (300.25 * quantity)
    elif itemNo == "2":
        total = total + (145.50 * quantity)
    else:
        total = total + (525.00 * quantity)

    print()
    #get user input for item number
    itemNo = input("Enter Item : ")

#display total price
print("Total Price to pay Rs : " + str(total))