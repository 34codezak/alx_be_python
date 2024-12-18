num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num3
    case "/":
        # Handle division by zero
        if num2 == 0:
            print("Error. Division by zero is not allowed.")
        else:
            result = num1 / num2
    case _:
        result = "Invalid operation."
# Output the result
print(f"The result is: {result}")
