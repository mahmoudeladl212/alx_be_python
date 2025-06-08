def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        # Add Item
        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to your shopping list.")
            else:
                print("Cannot add an empty item.")
        
        # Remove Item
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty.")
                continue
                
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
        
        # View List
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
        
        # Exit
        elif choice == '4':
            print("Goodbye!")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()