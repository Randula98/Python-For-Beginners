
#define the arrays
numArr = [0 for i in range(6)]
oddNum = [0 for i in range(6)]
evenNum = [0 for i in range(6)]

#get user inputs for numArr
for i in range(6):
    numArr[i] = input("Enter a number : ")

print()


#display the user input
print("Number series :" , end = " ")
for i in range(6):
    print(numArr[i] , end = " ")
print()

#inizialize 2 integer variables to manipulate oddNum & evenNum arrays
j = 0
k = 0

#assign values to oddNum & evenNum arrays
for i in range(6):
    numArr[i] = int(numArr[i])
    if(numArr[i] % 2 == 1):
        oddNum[j] = numArr[i]
        j = j + 1
    else:
        evenNum[k] = numArr[i]
        k = k + 1


#display oddNum array
print("Odd Numbers :" , end = " ")
for i in range(j):
    print(oddNum[i] , end = " ")

print()
#display evenNum Array
print("Even Numbers :" , end = " ")
for i in range(k):
    print(evenNum[i] , end = " ")