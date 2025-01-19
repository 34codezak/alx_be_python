def safe_divide(numerator, denominator):
    try:
        #Convert inputs to floats to handle non-numeric inputs
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/denominator
        return f"Result: The result of the division is {result}"

    except ZeroDivisionError:
        #Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        #Handle non-numeric input
        return "Error: Please enter numeric values only."