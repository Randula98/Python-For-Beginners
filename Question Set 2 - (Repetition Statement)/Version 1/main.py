
#get user inputs for pizza type
pType = input("Enter Pizza Type : ")

while pType != "-1":

    if pType != "1" and pType != "2" and pType != "3":
        print("Invalid Input")
        print()
        pType = input("Enter Pizza Type : ")
        continue

    #get user input for quantity
    quantity = input("Enter Quantity : ")
    quantity = int(quantity)

    #calculate the total and the discount
    if pType == "1":
        total = (1000 * quantity)
        discount = total * 10 / 100
    elif pType == "2":
        total = (1600 * quantity)
        discount = total * 12 / 100
    else:
        total = (1400 * quantity)
        discount = total * 15 / 100

    if quantity > 3:
        total = total - discount

    #display the total price
    print("Total Price : " + str(total))

    print()
    #get user inputs for pizza type
    pType = input("Enter Pizza Type : ")
