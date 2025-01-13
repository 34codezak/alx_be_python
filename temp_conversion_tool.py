# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor to convert Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor to convert Celsius to Fahrenheit

# Conversion Functions
def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    # Use the global conversion factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    # Use the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction
def main():
    try:
        # Prompt the user to enter a temperature and specify the scale
        temp_input = input("Enter the temperature (e.g., 100 for Celsius or 212 for Fahrenheit): ")
        scale_input = input("Is the entered temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Validate the temperature input (ensure it's a valid number)
        temperature = float(temp_input)  # This will raise an error if it's not a valid number

        # Perform the conversion based on the scale input
        if scale_input == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
        elif scale_input == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
        else:
            # Handle invalid scale input
            print("Invalid scale input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle invalid temperature input
        print("Invalid temperature. Please enter a numeric value.")

# Execute the main function
if __name__ == "__main__":
    main()
