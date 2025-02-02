shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the shopping list")
    print("4. Exit")

def add_item():
    item = input("Enter the name of the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the list.")

def remove_item():
    item = input("Enter the name of the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"Item '{item}' not found in the list.")

def view_list():
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is currently empty.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Please select an option (1-4): "))
            if choice == 1:
                add_item()
            elif choice == 2:
                remove_item()
            elif choice == 3:
                view_list()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
