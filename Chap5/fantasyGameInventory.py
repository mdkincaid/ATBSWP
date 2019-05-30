#displays the inventory and total number of items in a raw structure
def display_inventory(inventory):
    print("\nInventory:")
    total_items = 0
    for item, quantity in inventory.items():
        print(str(quantity) + ' ' + item)
        total_items += quantity
    print("\nTotal number of items: " + str(total_items))

#adds a list of items to the inventory
def add_to_inventory(inventory, items_to_add):
    for item in items_to_add:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory

#adds any item to the inventory
def pickup_item(inventory, item):
    inventory.setdefault(item, 0)
    inventory[item] = inventory[item] + 1

#prints the inventory in a neat structure
def print_inventory(inventory, left_width, right_width):
    print('INVENTORY'.center(left_width + right_width,'-'))
    for item, quantity in inventory.items():
        print(item.ljust(left_width,'.') + str(quantity).rjust(right_width))
    
inv = {'gold coin': 42, 'rope': 1}

#used to pick up a list of items
#dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#add_to_inventory(inv, dragon_loot)
#display_inventory(inv)

#used to pickup items
print_inventory(inv, 12, 5)
print('\nYou find a sharp stick and a barrel lid. Which would you like to pick up?')
item_to_pickup = input()
pickup_item(inv, item_to_pickup)
print('\nYou picked up the ' + item_to_pickup)
print_inventory(inv, 12, 5)

