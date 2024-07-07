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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item=input("Enter an item")
            shopping_list.append(item)
            pass
        elif choice == '2':
            if item in shopping_list:
                shopping_list.remove(item)
            elif item not in shopping_list:
                return "Item isn't on the shopping list"
            pass
        elif choice == '3':
            shopping_list_display = print_item()
            return print(shopping_list_display)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()