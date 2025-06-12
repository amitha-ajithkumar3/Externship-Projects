inventory = {
    "socks": (10, 9.99),
    "shoes": (20, 30.5),
    "shirts": (15, 29.9),
    "pants": (20, 39.99)
}

choice = input("Welcome to your inventory management program! Select a to add, u to update, r to remove an item, n to stop: ")

while choice != 'n':
    print ("Current Inventory:  ")
    for item, (num, price) in inventory.items():
        print(f"Item: {item}, Quantity: {num}, Price: ${price}")

    if choice == 'a':
        item = input("Enter an item to add to your inventory: ")
        if item in inventory:
            print("Your chosen item is present in the inventory")
        else:
            num = int(input("Enter number of items: "))
            price = float(input("Enter price for items: "))
            inventory[item] = (num, price)
            
        print ("Updated Inventory:  ")
        for item, (num, price) in inventory.items():
            print(f"Item: {item}, Quantity: {num}, Price: ${price}")

    elif choice == 'u':
        item = input("Enter the item name to update: ")
        if item in inventory:
            num = input(f"Enter new number of items to update: ")
            price = input("Enter updated price of items:")
            inventory[item] = (num, price)
        else:
            print("Invalid entry")

        print ("Updated Inventory:  ")
        for item, (num, price) in inventory.items():
            print(f"Item: {item}, Quantity: {num}, Price: ${price}")

    elif choice == 'r':
        item = input("Enter the item to remove: ")
        if item in inventory:
            del inventory[item]
        else:
            print("Item not present")
        print ("Updated Inventory:  ")
        for item, (num, price) in inventory.items():
            print(f"Item: {item}, Quantity: {num}, Price: ${price}")

    else:
        print("Invalid answer")

    choice = input(" a to add, u to update, r to remove, n to stop: ")

print ("Final Inventory:  ")
for item, (num, price) in inventory.items():
        print(f"Item: {item}, Quantity: {num}, Price: ${price}")

