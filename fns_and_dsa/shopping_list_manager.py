def display_menu():
    """Displays the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Manages a shopping list using a list (array)."""
    
    # 1️⃣ Implementing an array (list) named shopping_list
    shopping_list = []  # ✅ Ensures the list is correctly defined

    while True:
        # 2️⃣ Calling display_menu function
        display_menu()  # ✅ Ensures display_menu is called before user input

        # 3️⃣ Ensure choice input is strictly a number
        try:
            choice = int(input("Enter your choice (1-4): ").strip())  # ✅ Ensures input is a number
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")  
            continue  # Restart loop if input is invalid

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)  # ✅ Ensures shopping_list functions as an array
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Invalid input. Please enter a valid item.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # ✅ Ensures shopping_list handles removal
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == 3:
            print("\nYour Shopping List:")
            if shopping_list:  # ✅ Ensures shopping_list is displayed properly
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye! Thank you for using the shopping list manager.")
            break  # ✅ Ensures program exits properly

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")  

if __name__ == "__main__":
    main()  # ✅ Ensures main() runs when script is executed
