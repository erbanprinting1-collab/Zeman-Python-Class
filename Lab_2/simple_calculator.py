
number1 = float(input("Enter the first number: "))  # get two numbers from the user
number2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")  # ask the user for the operation

if operation == "+":                     # perform the addition operation and below other operations
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2 if number2 != 0 else "Undefined"
else:
    result = "Invalid operation"

print(f"Result: {result}")    # display the result of the operation