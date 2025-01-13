# Initialize the shopping list as an empty list
shopping_list = []

def show_menu():
    """Display the menu of options to the user."""
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    """Prompt the user to add an item to the shopping list."""
    item = input("Enter the item name to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item():
    """Prompt the user to remove an item from the shopping list."""
    item = input("Enter the item name to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")

def view_list():
    """Display all items in the shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    """Main loop to handle user input and manage the shopping list."""
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from 1 to 4.")

if __name__ == "__main__":
    main()
