class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static Method: add
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method: multiply
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage:
if __name__ == "__main__":
    # Using static method to add numbers
    result_addition = Calculator.add(5, 3)
    print(f"Sum: {result_addition}")

    # Using class method to multiply numbers
    result_multiplication = Calculator.multiply(4, 6)
    print(f"Product: {result_multiplication}")
