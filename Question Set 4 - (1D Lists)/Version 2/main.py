
#initialize the arrays
intArr = [0 for i in range(10)]
positiveNum = [0 for i in range(10)]
negativeNum = [0 for i in range(10)]

#get user inputs
for i in range(10):
    intArr[i] = input("Enter a number : ")
    intArr[i] = int(intArr[i])

print()

#display the user input
print("Number series :" , end = " ")
for i in range(10):
    print(str(intArr[i]) , end = " ")

#inizialize 2 integer variables to manipulate oddNum & evenNum arrays
j = 0
k = 0

#assign values to positiveNum & negativeNum arrays
for i in range(10):
    if intArr[i] < 0:
        negativeNum[j] = intArr[i]
        j = j + 1
    else:
        positiveNum[k] = intArr[i]
        k = k + 1


print()
#display positiveNum Array
print("Positive Numbers :" , end = " ")
for i in range(k):
    print(str(positiveNum[i]) , end = " ")

print()
#display negativeNum Array
print("Negative Numbers :" , end = " ")
for i in range(j):
    print(str(negativeNum[i]) , end = " ")