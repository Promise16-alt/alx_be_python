def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Define an empty shopping list (array)
    shopping_list = []

    while True:
        display_menu()  # Call display_menu function

        # Validate input to ensure it is a number
        try:
            choice = int(input("Enter your choice (1-4): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # Restart the loop if input is not a valid number

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)  # Append item to list
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Invalid input. Please enter a valid item.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == 3:
            print("\nYour Shopping List:")
            if shopping_list:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye! Thank you for using the shopping list manager.")
            break  # Exit the loop

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
