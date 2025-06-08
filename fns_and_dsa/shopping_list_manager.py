def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        # Add Item
        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                if item in shopping_list:
                    print(f"'{item}' is already in your shopping list.")
                else:
                    shopping_list.append(item)
                    print(f"'{item}' added to your shopping list.")
            else:
                print("Cannot add an empty item.")
        
        # Remove Item
        elif choice == '2':
            if not shopping_list:
                print("Your shopping list is empty.")
                continue
                
            print("Current items:")
            for idx, item in enumerate(shopping_list, 1):
                print(f"{idx}. {item}")
                
            try:
                item_num = input("Enter item number to remove (or name): ").strip()
                if item_num.isdigit():
                    index = int(item_num) - 1
                    if 0 <= index < len(shopping_list):
                        removed_item = shopping_list.pop(index)
                        print(f"'{removed_item}' removed from your shopping list.")
                    else:
                        print("Invalid item number.")
                else:
                    if item_num in shopping_list:
                        shopping_list.remove(item_num)
                        print(f"'{item_num}' removed from your shopping list.")
                    else:
                        print(f"'{item_num}' not found in your shopping list.")
            except ValueError:
                print("Invalid input. Please enter a valid item number or name.")
        
        # View List
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
        
        # Exit
        elif choice == '4':
            print("Goodbye! Your shopping list has been saved.")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()