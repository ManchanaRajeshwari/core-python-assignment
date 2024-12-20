menu = eval(input("Enter today's items (e.g., ['Pizza', 'Burger', 'Pasta']): "))
def add(item):
    menu.append(item)
    print(f"After item added the updated menu is {menu}")
def remove(item):
    if item in menu:
        menu.remove(item)
        print(f"After item removed, the updated menu is {menu}")
    else:
        print(f"Item '{item}' not found in the menu.")
def check_item(item):
    if item in menu:
        print(f"Availability: {item} is available")
    else:
        print(f"Availability {item} is not available")
def display():
    while True:
        print("Menu Management Options:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Check if an item is available")
        print("4. Exit")
        choice=int(input("Enter your choice"))
        if choice== 1:
            item_to_add=input("Enter item to add")
            add(item_to_add)
        if choice== 2:
            item_to_remove=input("Enter item to remove")
            remove(item_to_remove)
        if choice== 3:
            item_to_check=input("Enter item to check")
            check_item(item_to_check)
        if choice== 4:
            print("Exiting from the menu")
            break
display()
