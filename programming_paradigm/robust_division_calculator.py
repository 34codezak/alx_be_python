def safe_divide(numerator, denominator):
    try:
        #Convert inputs to floats to handle non-numeric inputs
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/denominator
        return f"Result: {result}"

    except ZeroDivisionError:
        #Handle division by zero
        return "Error: Cannot divide by zero."

    except ValueError:
        #Handle non-numeric input
        return "Error: Both inputs must be numeric."