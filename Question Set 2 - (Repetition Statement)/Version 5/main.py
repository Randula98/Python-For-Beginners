total = 0

#get user input for Item number
itemNo = input("Enter Item : ")

while itemNo != "-99":
    if itemNo != "1" and itemNo != "2" and itemNo != "3":
        print("Invalid Item Number")
        #get user input for Item number
        itemNo = input("Enter Item : ")
        continue

    #get user input for the quantity
    quantity = input("Enter Quantity : ")
    quantity = float(quantity)

    if itemNo == "1":
        total = total + (30 * quantity)
    elif itemNo == "2":
        total = total + (45 * quantity)
    else:
        total = total + (55.50 * quantity)

    print()
    #get user input for Item number
    itemNo = input("Enter Item : ")

#display the total price
print("Total Price to pay Rs : " + str(total))