
#get user input for burger type
bType = input("Enter Burger Type : ")

while bType == "1" or bType == "2" or bType == "3":
    total = 0
    #get user input for quantity
    quantity = input("Enter Quantity : ")
    quantity = float(quantity)

    if bType == "1":
        total = (500 * quantity)
    elif bType == "2":
        total = (500 + 50) * quantity
    else:
        total = (500 + 100) * quantity

    #diplay total price
    print("Total Price : " + str(total))

    print()
    #get user input for burger type
    bType = input("Enter Burger Type : ")


