def calculator():

    try: 
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        operation = input("Choose the operation (+, -, *, /): ")

        match operation:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case"*":
                result = num1 * num2
            case "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
            case _:
                print("Invalid opertion. Please choose from +, -, *, or /")

        print(f"The result is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
        calculator()


