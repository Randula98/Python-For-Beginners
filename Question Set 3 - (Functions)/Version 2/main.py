
#define the getDiscountPrice function
def getDiscountPrice(noOfGuests , chargePerGuest):
    if noOfGuests > 200:
        discount = float(noOfGuests * chargePerGuest) * 10 / 100
    else:
        discount = 0
    return discount

#define the getAmount function
def getAmount(noOfGuests , chargePerGuest , discount):
    amount = (noOfGuests * chargePerGuest) - discount
    return amount

#get user inputs for number of guests
guests = input("Enter no of guests : ")
guests = int(guests)

#get user inputs for charge per guest
charge = input("Enter charge per guest : ")
charge = float(charge)

#pass the given values to the getDiscountPrice function
discount = getDiscountPrice(guests , charge)

#pass the given values to the getAmount function
amount = getAmount(guests , charge , discount)

#display the discount and the amount to be paid
print("Discount : " + str(discount))
print("Amount to be paid : " + str(amount))