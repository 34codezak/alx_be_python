from datetime import datetime, timedelta

# First block: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time in "YYYY-MM-DD HH:MM:SS" format
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current Date and Time: {formatted_date}")

# Second block: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter the number of days
    days_to_add = int(input("Enter the number of days to add: "))
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date in "YYYY-MM-DD" format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the calculated future date
    print(f"The future date after {days_to_add} days will be: {formatted_future_date}")

def main():
    # Display the current date and time
    display_current_datetime()
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
