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

        if choice == '1':
            item_name = input("Enter item name: ")
            shopping_list.append(item_name)
            print(f"added '{item_name}' to the list")
        elif choice == '2':
            item_name = input("Enter the item to remove: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print(f"removed '{item_name}' from the list")
            else:
                print("Item not found")
        elif choice == '3':
            for items in shopping_list:
                print(items)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
