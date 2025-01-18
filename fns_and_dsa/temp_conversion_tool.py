# Define Global Conversion Factors
Fahrenheit=(Celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
FAHRENHEIT_OFFSET = 32

# Function to Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Use the global factor to convert to Celsius
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # Use the global factor to convert to Fahrenheit
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_OFFSET
    return fahrenheit

# User Interaction
def main():
    while True:
        try:
            # Ask the user for the temperature and the unit
            temperature_input = input("Enter the temperature followed by its unit (C for Celsius, F for Fahrenheit): ")
            temp_value, unit = temperature_input.split()

            # Convert the temperature value to a float
            temp_value = float(temp_value)

            # Validate the unit and perform the conversion
            if unit.upper() == 'F':
                celsius = convert_to_celsius(temp_value)
                print(f"{temp_value} Fahrenheit is {celsius:.2f} Celsius.")
            elif unit.upper() == 'C':
                fahrenheit = convert_to_fahrenheit(temp_value)
                print(f"{temp_value} Celsius is {fahrenheit:.2f} Fahrenheit.")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                continue

            # Ask the user if they want to perform another conversion
            again = input("Do you want to perform another conversion? (yes/no): ").lower()
            if again != 'yes':
                print("Exiting the temperature conversion tool.")
                break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
