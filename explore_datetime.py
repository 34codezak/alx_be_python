import datetime

def display_current_datetime():
    """Displays the current date and time in the format YYYY-MM-DD HH:MM:SS."""
    # Get the current date and time
    current_date = datetime.datetime.now()
    
    # Format the current date and time in the desired format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    """Calculates a future date by adding a specified number of days to the current date."""
    # Prompt the user to enter the number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer for the number of days.")
        return
    
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the future date
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Format the future date in the desired format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print(f"The future date after {days_to_add} days will be: {formatted_future_date}")

# Main code to call the functions
if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display a future date
    calculate_future_date()
