
#take user inputs for time period
timePeriod = input("Time Period : ")
timePeriod = float(timePeriod)

#take user inputs for number of times
noOfTimes = input("Number of times : ")
noOfTimes = float(noOfTimes)

#take user inputs for peak time feature
peakTime = input("Peak time (Y /N) : ")
while peakTime != "Y" and peakTime != "y" and peakTime != "N" and peakTime != "n":
    print("Invalid Input! Try again!! " + peakTime)
    peakTime = input("Peak time (Y /N) : ")

#calculate basic price
if timePeriod > 60:
    total = 25000 * noOfTimes
elif timePeriod >= 45:
    total = 12000 * noOfTimes
else:
    total = 7500 * noOfTimes

#calculate and add extra fee for peak time
if peakTime == "Y" or peakTime == "y":
    total = total * 120 / 100

#print output
print("Total amount to be paid : " + str(total))
