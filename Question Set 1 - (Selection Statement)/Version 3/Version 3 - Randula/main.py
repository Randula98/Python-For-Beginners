
#get user input for age
age = input("Age : ")
age = int(age)

#get user input for bank balance
bankBalance = input("Bank Balance : ")
bankBalance = float(bankBalance)
while bankBalance < 0:
    print("Invalid Input!! Try again")
    bankBalance = input("Bank Balance : ")

#find the gift according to the age and the bank balance
if age <= 18:
    if bankBalance > 100000:
        gift = "Tablet"
    else:
        gift = "School bag"
else:
    if bankBalance > 100000:
        gift = "Rice Cooker"
    else:
        gift = "Travelling Bag"

#display the gift
print("Gift : " + gift)