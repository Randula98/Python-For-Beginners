
#initalize the arrays
myArray = [0 for i in range(10)]
largeNum = [0 for i in range(10)]

#define total variable to calculate the average
total = 0

#get user inputs
for i in range(10):
    myArray[i] = input("Enter the number series : ")
    myArray[i] = float(myArray[i])

#calculate the total and the average
for i in range(10):
    total = total + myArray[i]

average = total / 10

print()
#display the average
print("Average : " + str(average))

#display the myArray elements
print("myArray :" , end = " ")
for i in range(10):
    myArray[i] = int(myArray[i])
    print(str(myArray[i]) , end = " ")

print()

#inizialize an integer variable to manipulate largerNum array
j = 0

#assign values greater than average to largeNum array
for i in range(10):
    if (myArray[i] > average):
        largeNum[j] = myArray[i]
        j = j + 1

#display the largeNum elements
print("largeNum :" , end = " ")
for i in range(5):
    print(str(largeNum[i]) , end = " ")

print()