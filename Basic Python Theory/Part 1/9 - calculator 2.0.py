
num1 = input("Enter a number : ")
num2 = input("Enter another number : ")
op = input("Enter an operator (+ | - | * | /) : ")

num1 = float(num1)
num2 = float(num2)

if op == '+':
    answer = num1 + num2
elif op == '-':
    answer = num1 - num2
elif op == '*':
    answer = num1 * num2
elif op == '/':
    answer = num1 / num2
else:
    print("Invalid Operator")
    #immidiate termination
    quit()

print("Answer is " + str(answer))