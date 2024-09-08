todo_list = []

def show_menu():
    print("\nMenu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item():
    item = input("Enter item to add: ")
    todo_list.append(item)
    print(f"'{item}' added to the list.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in todo_list:
        todo_list.remove(item)
        print(f"'{item}' removed from the list.")
    else:
        print(f"'{item}' not found in the list.")

def view_list():
    print("\nTo-Do List:")
    for i, item in enumerate(todo_list, 1):
        print(f"{i}. {item}")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
