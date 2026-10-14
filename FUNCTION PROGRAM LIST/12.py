fruits = ["Apple", "Banana", "Mango"]

def show_fruits():
    print("Fruits:", fruits)

def add_fruit(name):
    fruits.append(name)

def insert_fruit(name, position=1):
    fruits.insert(position, name)

def update_fruit(old_name=None, new_name=None):
    for i in range(len(fruits)):
        if fruits[i] == old_name:
            fruits[i] = new_name
            break

def remove_fruit(value):
    if isinstance(value, int):
        if 0 <= value < len(fruits):
            fruits.pop(value)
    elif value in fruits:
        fruits.remove(value)

def arrange_fruits():
    fruits.sort()

show_fruits()
add_fruit("Orange")
insert_fruit("Grapes")
update_fruit(old_name="Banana", new_name="Papaya")
remove_fruit("Mango")
arrange_fruits()
show_fruits()
