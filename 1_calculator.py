
operation = input("Please write + or - or * or /   ")
if operation == "+":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif operation == "-":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif operation == "*":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif operation == "/":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2)
else:
    print("false operation")