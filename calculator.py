# 🧮 Simple Calculator in Python

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +  -  *  /")
operation = input("Enter operation: ")

# Performing calculation
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation")
