pattern_size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < pattern_size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # After completing each row, print a newline character
    print()

    # Increment the row counter 
    row += 1