inventory = {}

def add_item():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty

def remove_item():
    name = input("Enter product name to remove: ")
    if name in inventory:
        del inventory[name]

def update_qty():
    name = input("Enter product name: ")
    qty = int(input("Enter new quantity: "))
    if name in inventory:
        inventory[name] = qty

def display_inventory():
    print(inventory)

def low_stock():
    for name in inventory:
        if inventory[name] < 5:
            print(name, ":", inventory[name])

add_item()
add_item()
display_inventory()
update_qty()
remove_item()
display_inventory()
low_stock()